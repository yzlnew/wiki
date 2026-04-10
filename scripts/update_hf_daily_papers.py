#!/usr/bin/env python3
"""Sync Hugging Face Daily Papers, filter by interest, and stage relevant papers."""

from __future__ import annotations

import argparse
import json
import os
import re
import socket
import ssl
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib import parse, request


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = ROOT / ".env.hf-daily-papers.local"
DEFAULT_REPORT = ROOT / "sources/library/hf-daily-papers/hf-daily-papers-latest.md"
DEFAULT_INBOX_DIR = ROOT / "sources/inbox/hf-daily-papers"
DEFAULT_STATE = ROOT / "sources/library/hf-daily-papers/hf-daily-papers-state.json"
DEFAULT_FILTER_PROMPT = ROOT / "system/templates/hf-paper-filter-prompt.md"
DEFAULT_EXTRACTION_PROMPT = ROOT / "system/templates/hf-paper-knowledge-prompt.md"
DEFAULT_API_BASE = "https://huggingface.co/api"

RELATED_TOPIC_LINKS = {
    "reinforcement-learning": "../../../wiki/topics/reinforcement-learning-and-post-training.md",
    "post-training": "../../../wiki/topics/reinforcement-learning-and-post-training.md",
    "agents": "../../../wiki/topics/agent-workflows.md",
    "agent-evals": "../../../wiki/topics/agent-workflows.md",
    "mechanistic-interpretability": "../../../wiki/topics/llm-systems-and-training.md",
    "llm-systems": "../../../wiki/topics/llm-systems-and-training.md",
    "ai-and-llms": "../../../wiki/topics/ai-and-llms.md",
}


@dataclass
class Paper:
    paper_id: str
    title: str
    summary: str
    ai_summary: str
    ai_keywords: list[str]
    authors: list[str]
    published_at: datetime | None
    submitted_on_daily_at: datetime | None
    upvotes: int
    num_comments: int
    organization: str
    github_repo: str
    project_page: str
    paper_url: str
    api_url: str
    arxiv_url: str
    submitted_dates: list[str] = field(default_factory=list)

    @property
    def date_key(self) -> str:
        if self.submitted_on_daily_at is not None:
            return self.submitted_on_daily_at.date().isoformat()
        if self.published_at is not None:
            return self.published_at.date().isoformat()
        return date.today().isoformat()


@dataclass
class FilterResult:
    decision: str
    score: int
    reason: str
    matched_interests: list[str]
    weak_signals: list[str]
    downrank_signals: list[str]


@dataclass
class ExtractionResult:
    one_sentence_summary: str
    key_points: list[str]
    why_relevant: str
    open_questions: list[str]
    tags: list[str]


@dataclass
class ProcessedPaper:
    paper: Paper
    filter_result: FilterResult
    extraction_result: ExtractionResult | None
    inbox_path: Path | None
    reused_from_state: bool
    source_url_used: str = ""
    source_basis: str = ""


class HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._ignore_depth = 0
        self._title_depth = 0
        self._title_parts: list[str] = []
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self._ignore_depth += 1
            return
        if tag == "title":
            self._title_depth += 1
        if tag in {"p", "div", "section", "article", "header", "footer", "aside", "main", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "table"}:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self._ignore_depth > 0:
            self._ignore_depth -= 1
            return
        if tag == "title" and self._title_depth > 0:
            self._title_depth -= 1
        if tag in {"p", "div", "section", "article", "header", "footer", "aside", "main", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "table"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._ignore_depth > 0:
            return
        if self._title_depth > 0:
            self._title_parts.append(data)
        self._parts.append(data)

    @property
    def title(self) -> str:
        return collapse_whitespace(" ".join(self._title_parts))

    @property
    def text(self) -> str:
        text = "".join(self._parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        lines = [collapse_whitespace(line) for line in text.splitlines()]
        return "\n".join(line for line in lines if line).strip()


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def env(name: str, *, required: bool = True, default: str | None = None) -> str:
    value = os.environ.get(name, default)
    if required and not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value or ""


def build_ssl_context(var_name: str, default: str = "1") -> ssl.SSLContext | None:
    verify_tls = env(var_name, required=False, default=default).lower()
    if verify_tls in {"0", "false", "no"}:
        return ssl._create_unverified_context()
    return None


@contextmanager
def force_ip_family_if_needed(prefix: str):
    ipv6 = env(f"{prefix}_FORCE_IPV6", required=False, default="0").lower() in {"1", "true", "yes"}
    ipv4 = env(f"{prefix}_FORCE_IPV4", required=False, default="0").lower() in {"1", "true", "yes"}
    family = 0
    if ipv6:
        family = socket.AF_INET6
    elif ipv4:
        family = socket.AF_INET

    if family == 0:
        yield
        return

    original = socket.getaddrinfo
    forced_family = family

    def force_family(host: str, port: int, family: int = 0, type: int = 0, proto: int = 0, flags: int = 0):
        return original(host, port, forced_family, type, proto, flags)

    socket.getaddrinfo = force_family
    try:
        yield
    finally:
        socket.getaddrinfo = original


def http_get_json(url: str) -> Any:
    req = request.Request(
        url,
        headers={
            "User-Agent": env("HF_DAILY_PAPERS_USER_AGENT", required=False, default="wiki-hf-daily-papers/1.0"),
            "Accept": "application/json",
        },
    )
    timeout = float(env("HF_DAILY_PAPERS_TIMEOUT", required=False, default="30"))
    context = build_ssl_context("HF_DAILY_PAPERS_VERIFY_TLS")
    with force_ip_family_if_needed("HF_DAILY_PAPERS"):
        with request.urlopen(req, timeout=timeout, context=context) as resp:
            return json.load(resp)


def http_get_text(url: str, *, timeout_env: str, verify_env: str, ip_prefix: str) -> str:
    req = request.Request(
        url,
        headers={
            "User-Agent": env("HF_DAILY_PAPERS_USER_AGENT", required=False, default="wiki-hf-daily-papers/1.0"),
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    timeout = float(env(timeout_env, required=False, default="30"))
    context = build_ssl_context(verify_env)
    with force_ip_family_if_needed(ip_prefix):
        with request.urlopen(req, timeout=timeout, context=context) as resp:
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read()

    charset = "utf-8"
    match = re.search(r"charset=([\w-]+)", content_type, re.IGNORECASE)
    if match:
        charset = match.group(1)
    return raw.decode(charset, errors="replace")


def parse_datetime(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(text).astimezone()
    except ValueError:
        return None


def ensure_list_of_strings(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    result: list[str] = []
    for item in items:
        if isinstance(item, dict):
            value = str(item.get("name", "")).strip()
        else:
            value = str(item).strip()
        if value and value not in result:
            result.append(value)
    return result


def parse_daily_paper(item: dict[str, Any]) -> Paper | None:
    paper_info = item.get("paper")
    if isinstance(paper_info, dict):
        payload = paper_info
    else:
        payload = item

    paper_id = str(payload.get("id", "")).strip()
    title = collapse_whitespace(str(item.get("title") or payload.get("title") or ""))
    summary = collapse_whitespace(str(item.get("summary") or payload.get("summary") or ""))
    ai_summary = collapse_whitespace(str(payload.get("ai_summary") or ""))
    if not paper_id or not title:
        return None

    authors = ensure_list_of_strings(payload.get("authors"))
    ai_keywords = ensure_list_of_strings(payload.get("ai_keywords"))
    organization = ""
    organization_payload = payload.get("organization")
    if isinstance(organization_payload, dict):
        organization = collapse_whitespace(
            str(organization_payload.get("fullname") or organization_payload.get("name") or "")
        )

    github_repo = str(payload.get("githubRepo") or "").strip()
    project_page = str(payload.get("projectPage") or "").strip()
    submitted_dates: list[str] = []

    return Paper(
        paper_id=paper_id,
        title=title,
        summary=summary,
        ai_summary=ai_summary,
        ai_keywords=ai_keywords,
        authors=authors,
        published_at=parse_datetime(str(item.get("publishedAt") or payload.get("publishedAt") or "")),
        submitted_on_daily_at=parse_datetime(str(payload.get("submittedOnDailyAt") or "")),
        upvotes=int(payload.get("upvotes") or item.get("upvotes") or 0),
        num_comments=int(item.get("numComments") or payload.get("numComments") or 0),
        organization=organization,
        github_repo=github_repo,
        project_page=project_page,
        paper_url=f"https://huggingface.co/papers/{paper_id}",
        api_url=f"{normalize_api_base()}/papers/{paper_id}",
        arxiv_url=f"https://arxiv.org/abs/{paper_id}",
        submitted_dates=submitted_dates,
    )


def normalize_api_base() -> str:
    raw = env("HF_DAILY_PAPERS_API_BASE", required=False, default=DEFAULT_API_BASE).strip()
    if not raw:
        raise SystemExit("HF_DAILY_PAPERS_API_BASE must not be empty")
    if not raw.startswith(("http://", "https://")):
        raw = f"https://{raw}"
    return raw.rstrip("/")


def fetch_daily_papers(day: date) -> list[Paper]:
    query = parse.urlencode({"date": day.isoformat()})
    payload = http_get_json(f"{normalize_api_base()}/daily_papers?{query}")
    if not isinstance(payload, list):
        raise SystemExit("Unexpected Hugging Face daily papers response shape: expected a list")

    papers: list[Paper] = []
    for item in payload:
        if not isinstance(item, dict):
            continue
        paper = parse_daily_paper(item)
        if paper is None:
            continue
        paper.submitted_dates.append(day.isoformat())
        papers.append(paper)
    return papers


def collect_recent_papers(days_back: int) -> list[Paper]:
    by_id: dict[str, Paper] = {}
    today = date.today()
    for offset in range(days_back):
        current_day = today - timedelta(days=offset)
        for paper in fetch_daily_papers(current_day):
            existing = by_id.get(paper.paper_id)
            if existing is None:
                by_id[paper.paper_id] = paper
                continue
            submitted_dates = dedupe_preserve_order(existing.submitted_dates + paper.submitted_dates)
            keep = paper
            if sort_datetime(existing.submitted_on_daily_at) >= sort_datetime(paper.submitted_on_daily_at):
                keep = existing
            keep.submitted_dates = submitted_dates
            by_id[paper.paper_id] = keep

    papers = list(by_id.values())
    papers.sort(
        key=lambda paper: (
            sort_datetime(paper.submitted_on_daily_at),
            sort_datetime(paper.published_at),
            paper.paper_id,
        ),
        reverse=True,
    )
    return papers


def sort_datetime(value: datetime | None) -> datetime:
    if value is None:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def collapse_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def truncate_text(text: str, limit: int) -> str:
    clean = text.strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3].rstrip() + "..."


def dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def read_text_if_exists(path: Path) -> str:
    if not path.exists():
        try:
            display = path.relative_to(ROOT)
        except ValueError:
            display = path
        raise SystemExit(f"Required file not found: {display}")
    return path.read_text(encoding="utf-8").strip()


def resolve_root_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return ROOT / path


def sanitize_prompt_text(text: str) -> str:
    return text.replace("```", "'''")


def html_to_text(html: str) -> tuple[str, str]:
    parser = HTMLTextExtractor()
    parser.feed(html)
    parser.close()
    return parser.title, parser.text


def extract_meta_description(html: str) -> str:
    match = re.search(
        r'<meta[^>]+(?:name|property)=["\'](?:description|og:description)["\'][^>]+content=["\'](.*?)["\']',
        html,
        re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return ""
    return collapse_whitespace(unescape(match.group(1)))


def extract_arxiv_abstract(html: str) -> str:
    match = re.search(r'<blockquote[^>]+class="[^"]*abstract[^"]*"[^>]*>(.*?)</blockquote>', html, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    text = collapse_whitespace(unescape(text))
    return re.sub(r"^Abstract:\s*", "", text, flags=re.IGNORECASE)


def build_filter_input(paper: Paper) -> str:
    authors = ", ".join(paper.authors) if paper.authors else "unknown"
    keywords = ", ".join(paper.ai_keywords) if paper.ai_keywords else "unknown"
    submitted_dates = ", ".join(paper.submitted_dates) if paper.submitted_dates else "unknown"
    published = paper.published_at.isoformat(timespec="seconds") if paper.published_at else "unknown"
    submitted = paper.submitted_on_daily_at.isoformat(timespec="seconds") if paper.submitted_on_daily_at else "unknown"
    return "\n".join(
        [
            f"TITLE: {paper.title}",
            f"PAPER_ID: {paper.paper_id}",
            f"HF_PAPER_URL: {paper.paper_url}",
            f"ARXIV_URL: {paper.arxiv_url}",
            f"PUBLISHED_AT: {published}",
            f"SUBMITTED_ON_DAILY_AT: {submitted}",
            f"SEEN_IN_DAILY_FEEDS: {submitted_dates}",
            f"AUTHORS: {authors}",
            f"ORGANIZATION: {paper.organization or 'unknown'}",
            f"UPVOTES: {paper.upvotes}",
            f"NUM_COMMENTS: {paper.num_comments}",
            f"AI_KEYWORDS: {keywords}",
            f"ABSTRACT: {paper.summary or 'unknown'}",
            f"HF_AI_SUMMARY: {paper.ai_summary or 'unknown'}",
        ]
    )


def build_extraction_input(
    paper: Paper,
    filter_result: FilterResult,
    source_url: str,
    source_basis: str,
    source_text: str,
) -> str:
    matched = ", ".join(filter_result.matched_interests) if filter_result.matched_interests else "none"
    downrank = ", ".join(filter_result.downrank_signals) if filter_result.downrank_signals else "none"
    keywords = ", ".join(paper.ai_keywords) if paper.ai_keywords else "unknown"
    authors = ", ".join(paper.authors) if paper.authors else "unknown"
    return "\n".join(
        [
            f"TITLE: {paper.title}",
            f"PAPER_ID: {paper.paper_id}",
            f"HF_PAPER_URL: {paper.paper_url}",
            f"ARXIV_URL: {paper.arxiv_url}",
            f"AUTHORS: {authors}",
            f"AI_KEYWORDS: {keywords}",
            f"FILTER_DECISION: {filter_result.decision}",
            f"FILTER_SCORE: {filter_result.score}",
            f"MATCHED_INTERESTS: {matched}",
            f"DOWNRANK_SIGNALS: {downrank}",
            f"SOURCE_URL: {source_url or 'unknown'}",
            f"SOURCE_BASIS: {source_basis}",
            f"SOURCE_TEXT: {sanitize_prompt_text(source_text)}",
            f"ABSTRACT: {paper.summary or 'unknown'}",
            f"HF_AI_SUMMARY: {paper.ai_summary or 'unknown'}",
        ]
    )


def fetch_original_source_context(paper: Paper) -> tuple[str, str, str]:
    candidates = [paper.arxiv_url, paper.project_page, paper.paper_url]
    for source_url in candidates:
        if not source_url:
            continue
        try:
            html = http_get_text(
                source_url,
                timeout_env="HF_DAILY_PAPERS_SOURCE_TIMEOUT",
                verify_env="HF_DAILY_PAPERS_SOURCE_VERIFY_TLS",
                ip_prefix="HF_DAILY_PAPERS_SOURCE",
            )
        except Exception:
            continue

        if "arxiv.org" in parse.urlparse(source_url).netloc:
            abstract = extract_arxiv_abstract(html)
            if abstract:
                return source_url, "original abstract page", truncate_text(abstract, 8000)

        _, text = html_to_text(html)
        description = extract_meta_description(html)
        candidate_text = text or description
        if candidate_text:
            return source_url, "source page excerpt", truncate_text(candidate_text, 12000)

    if paper.summary:
        return paper.arxiv_url or paper.paper_url, "hf abstract fallback", truncate_text(paper.summary, 8000)
    if paper.ai_summary:
        return paper.paper_url, "hf ai summary fallback", truncate_text(paper.ai_summary, 4000)
    return paper.paper_url, "metadata fallback", truncate_text(paper.title, 1000)


def invoke_codex_json(prompt_template: str, input_block: str) -> dict[str, Any]:
    codex_bin = env("HF_DAILY_PAPERS_CODEX_BIN", required=False, default="codex")
    model = env("HF_DAILY_PAPERS_MODEL", required=False, default="gpt-5.4-mini")
    reasoning_effort = env("HF_DAILY_PAPERS_REASONING_EFFORT", required=False, default="low")
    timeout = float(env("HF_DAILY_PAPERS_CODEX_TIMEOUT", required=False, default="240"))
    full_prompt = f"{prompt_template}\n\n## Candidate\n\n```text\n{sanitize_prompt_text(input_block)}\n```\n"

    with tempfile.TemporaryDirectory(prefix="hf-daily-papers-") as temp_dir:
        output_path = Path(temp_dir) / "last-message.txt"
        cmd = [
            codex_bin,
            "exec",
            "--skip-git-repo-check",
            "--ephemeral",
            "--sandbox",
            "read-only",
            "--color",
            "never",
            "-C",
            str(ROOT),
            "-m",
            model,
            "-c",
            f'model_reasoning_effort="{reasoning_effort}"',
            "-o",
            str(output_path),
            "-",
        ]
        completed = subprocess.run(
            cmd,
            input=full_prompt,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        if completed.returncode != 0:
            stderr = completed.stderr.strip()
            stdout = completed.stdout.strip()
            details = stderr or stdout or f"exit code {completed.returncode}"
            raise RuntimeError(f"codex exec failed: {details}")
        raw = output_path.read_text(encoding="utf-8").strip()
    parsed = parse_json_response(raw)
    if not isinstance(parsed, dict):
        raise RuntimeError("codex exec returned non-object JSON")
    return parsed


def parse_json_response(text: str) -> Any:
    clean = text.strip()
    if clean.startswith("```"):
        clean = re.sub(r"^```[a-zA-Z0-9_-]*\n", "", clean)
        clean = re.sub(r"\n```$", "", clean)
        clean = clean.strip()
    try:
        return json.loads(clean)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", clean, re.DOTALL)
        if not match:
            raise
        return json.loads(match.group(0))


def parse_filter_result(payload: dict[str, Any]) -> FilterResult:
    decision = str(payload.get("decision", "")).strip().lower()
    if decision not in {"accept", "maybe", "reject"}:
        raise RuntimeError(f"Unexpected filter decision: {decision or 'missing'}")
    score = int(payload.get("score", 0))
    reason = collapse_whitespace(str(payload.get("reason", ""))) or "No reason returned."
    return FilterResult(
        decision=decision,
        score=max(0, min(100, score)),
        reason=reason,
        matched_interests=ensure_list_of_strings(payload.get("matched_interests")),
        weak_signals=ensure_list_of_strings(payload.get("weak_signals")),
        downrank_signals=ensure_list_of_strings(payload.get("downrank_signals")),
    )


def parse_extraction_result(payload: dict[str, Any]) -> ExtractionResult:
    summary = collapse_whitespace(str(payload.get("one_sentence_summary", "")))
    why_relevant = collapse_whitespace(str(payload.get("why_relevant", "")))
    if not summary:
        raise RuntimeError("Extraction result is missing one_sentence_summary")
    if not why_relevant:
        raise RuntimeError("Extraction result is missing why_relevant")
    return ExtractionResult(
        one_sentence_summary=summary,
        key_points=ensure_list_of_strings(payload.get("key_points")),
        why_relevant=why_relevant,
        open_questions=ensure_list_of_strings(payload.get("open_questions")),
        tags=ensure_list_of_strings(payload.get("tags")),
    )


def include_maybe() -> bool:
    return env("HF_DAILY_PAPERS_INCLUDE_MAYBE", required=False, default="0").lower() in {"1", "true", "yes"}


def should_stage(result: FilterResult) -> bool:
    return result.decision == "accept" or (result.decision == "maybe" and include_maybe())


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"papers": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"papers": {}}
    if not isinstance(payload, dict):
        return {"papers": {}}
    papers = payload.get("papers")
    if not isinstance(papers, dict):
        payload["papers"] = {}
    return payload


def inbox_filename(paper: Paper) -> str:
    safe_id = paper.paper_id.replace(".", "-")
    slug = slugify(paper.title)
    return f"{paper.date_key}-{safe_id}-{slug}.md"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:80] or "paper"


def state_entry_matches_file(entry: dict[str, Any]) -> Path | None:
    path_text = str(entry.get("inbox_path", "")).strip()
    if not path_text:
        return None
    path = ROOT / path_text
    if path.exists():
        return path
    return None


def processed_from_state(paper: Paper, entry: dict[str, Any]) -> ProcessedPaper | None:
    try:
        filter_result = parse_filter_result(entry.get("filter_result", {}))
    except Exception:
        return None

    extraction_result = None
    inbox_path = state_entry_matches_file(entry)
    extraction_payload = entry.get("extraction_result")
    if isinstance(extraction_payload, dict):
        try:
            extraction_result = parse_extraction_result(extraction_payload)
        except Exception:
            extraction_result = None

    if should_stage(filter_result) and inbox_path is None:
        return None

    return ProcessedPaper(
        paper=paper,
        filter_result=filter_result,
        extraction_result=extraction_result,
        inbox_path=inbox_path,
        reused_from_state=True,
        source_url_used=str(entry.get("source_url_used", "")),
        source_basis=str(entry.get("source_basis", "")),
    )


def related_links(matched_interests: list[str]) -> list[str]:
    links: list[str] = []
    seen: set[str] = set()
    for interest in matched_interests:
        target = RELATED_TOPIC_LINKS.get(interest)
        if target and target not in seen:
            seen.add(target)
            links.append(target)
    fallback = RELATED_TOPIC_LINKS["ai-and-llms"]
    if fallback not in seen:
        links.append(fallback)
    return links


def write_inbox_file(
    paper: Paper,
    filter_result: FilterResult,
    extraction_result: ExtractionResult,
    source_url_used: str,
    source_basis: str,
    source_text: str,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / inbox_filename(paper)
    tags = dedupe_preserve_order(
        ["hf-daily-papers", "papers", "inbox"] + filter_result.matched_interests + extraction_result.tags
    )
    submitted = paper.submitted_on_daily_at.isoformat(timespec="seconds") if paper.submitted_on_daily_at else "unknown"
    published = paper.published_at.isoformat(timespec="seconds") if paper.published_at else "unknown"

    lines = [
        "---",
        "type: source-summary",
        "status: active",
        f"tags: [{', '.join(tags)}]",
        "source_count: 1",
        f"updated: {date.today().isoformat()}",
        f"source_url: {source_url_used or paper.paper_url}",
        f"paper_id: {paper.paper_id}",
        f"published: {published}",
        f"submitted_on_daily: {submitted}",
        f"decision: {filter_result.decision}",
        f"score: {filter_result.score}",
        "generator: scripts/update_hf_daily_papers.py",
        "---",
        "",
        f"# {paper.title}",
        "",
        "## Summary",
        "",
        f"- one_sentence_summary: {escape_markdown(extraction_result.one_sentence_summary)}",
        f"- why_relevant: {escape_markdown(extraction_result.why_relevant)}",
        f"- filter_reason: {escape_markdown(filter_result.reason)}",
        f"- hugging_face_paper: {paper.paper_url}",
        f"- original_paper: {source_url_used or paper.arxiv_url}",
        f"- source_basis: `{escape_backticks(source_basis)}`",
        "",
        "## Key Points",
        "",
    ]

    if extraction_result.key_points:
        for point in extraction_result.key_points:
            lines.append(f"- {escape_markdown(point)}")
    else:
        lines.append("- Knowledge extraction returned no key points.")

    lines.extend(["", "## Related", ""])
    for link in related_links(filter_result.matched_interests):
        label = Path(link).stem.replace("-", " ").title()
        lines.append(f"- [{label}]({link})")

    lines.extend(["", "## Sources", ""])
    lines.append(f"- Hugging Face paper page: {paper.paper_url}")
    lines.append(f"- Hugging Face API entry: {paper.api_url}")
    lines.append(f"- arXiv abstract: {paper.arxiv_url}")
    if source_url_used and source_url_used not in {paper.paper_url, paper.arxiv_url}:
        lines.append(f"- Source page used for extraction: {source_url_used}")
    if paper.github_repo:
        lines.append(f"- GitHub: {paper.github_repo}")
    if paper.project_page:
        lines.append(f"- Project page: {paper.project_page}")

    lines.extend(["", "## Paper Metadata", ""])
    if paper.authors:
        lines.append("- authors: " + ", ".join(f"`{escape_backticks(author)}`" for author in paper.authors))
    if paper.organization:
        lines.append(f"- organization: `{escape_backticks(paper.organization)}`")
    if paper.ai_keywords:
        lines.append("- ai_keywords: " + ", ".join(f"`{escape_backticks(keyword)}`" for keyword in paper.ai_keywords))
    lines.append(f"- upvotes: `{paper.upvotes}`")
    lines.append(f"- num_comments: `{paper.num_comments}`")
    if paper.summary:
        lines.append(f"- abstract: {escape_markdown(paper.summary)}")
    if paper.ai_summary:
        lines.append(f"- hf_ai_summary: {escape_markdown(paper.ai_summary)}")

    lines.extend(["", "## Source Excerpt", ""])
    lines.append(source_text or "No original source text fetched.")

    lines.extend(["", "## Open Questions", ""])
    if extraction_result.open_questions:
        for item in extraction_result.open_questions:
            lines.append(f"- {escape_markdown(item)}")
    else:
        lines.append("- none")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def escape_markdown(text: str) -> str:
    return text.replace("\n", " ").replace("[", r"\[").replace("]", r"\]")


def escape_backticks(text: str) -> str:
    return text.replace("`", "'")


def render_report(items: list[ProcessedPaper], generated_at: str, days_back: int) -> str:
    counts = {"accept": 0, "maybe": 0, "reject": 0}
    staged_count = 0
    reused_count = 0
    for item in items:
        counts[item.filter_result.decision] += 1
        if item.inbox_path is not None:
            staged_count += 1
        if item.reused_from_state:
            reused_count += 1

    lines = [
        "---",
        "type: source-summary",
        "status: active",
        "tags: [hf-daily-papers, papers, generated]",
        f"source_count: {len(items)}",
        f"updated: {generated_at[:10]}",
        "generator: scripts/update_hf_daily_papers.py",
        "---",
        "",
        "# Hugging Face Daily Papers Latest",
        "",
        "## Summary",
        "",
        f"- generated_at: {generated_at}",
        f"- window_days: {days_back}",
        f"- total_items: {len(items)}",
        f"- accepted: {counts['accept']}",
        f"- maybe: {counts['maybe']}",
        f"- rejected: {counts['reject']}",
        f"- staged_for_ingest: {staged_count}",
        f"- reused_from_state: {reused_count}",
        "- filter_mode: cheap Codex subagent over title + abstract + HF AI summary",
        "- extraction_mode: cheap Codex subagent grounded in original paper pages or arXiv abstract pages when available",
        "",
        "## Notes",
        "",
        "- This file is generated from Hugging Face Daily Papers and should be updated by script, not edited by hand.",
        "- Accepted papers are written to `sources/inbox/hf-daily-papers/` for later ingest.",
        "- Model credentials are handled by local Codex CLI auth and local ignored env config.",
        "- Knowledge extraction prefers original paper pages or arXiv abstract pages before falling back to Hugging Face metadata.",
        "",
    ]

    for decision in ("accept", "maybe", "reject"):
        lines.extend([f"## {decision.title()}", ""])
        decision_items = [item for item in items if item.filter_result.decision == decision]
        if not decision_items:
            lines.extend(["- none", ""])
            continue
        for item in decision_items:
            paper = item.paper
            result = item.filter_result
            lines.append(f"- [{escape_markdown(paper.title)}]({paper.paper_url})")
            lines.append(
                "  - "
                + "; ".join(
                    [
                        f"paper_id: `{escape_backticks(paper.paper_id)}`",
                        f"decision: `{result.decision}`",
                        f"score: `{result.score}`",
                        f"upvotes: `{paper.upvotes}`",
                    ]
                )
            )
            lines.append(f"  - reason: {escape_markdown(result.reason)}")
            if result.matched_interests:
                lines.append(
                    "  - matched: " + ", ".join(f"`{escape_backticks(entry)}`" for entry in result.matched_interests)
                )
            if result.weak_signals:
                lines.append(
                    "  - weak_signals: "
                    + ", ".join(f"`{escape_backticks(entry)}`" for entry in result.weak_signals)
                )
            if result.downrank_signals:
                lines.append(
                    "  - downrank: "
                    + ", ".join(f"`{escape_backticks(entry)}`" for entry in result.downrank_signals)
                )
            if item.inbox_path is not None:
                lines.append(f"  - inbox_file: `{item.inbox_path.relative_to(ROOT)}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def update_state(path: Path, existing_state: dict[str, Any], processed_items: list[ProcessedPaper], generated_at: str) -> None:
    payload = {
        "generated_at": generated_at,
        "papers": dict(existing_state.get("papers", {})),
    }
    for item in processed_items:
        payload["papers"][item.paper.paper_id] = {
            "title": item.paper.title,
            "filter_result": {
                "decision": item.filter_result.decision,
                "score": item.filter_result.score,
                "reason": item.filter_result.reason,
                "matched_interests": item.filter_result.matched_interests,
                "weak_signals": item.filter_result.weak_signals,
                "downrank_signals": item.filter_result.downrank_signals,
            },
            "extraction_result": (
                {
                    "one_sentence_summary": item.extraction_result.one_sentence_summary,
                    "key_points": item.extraction_result.key_points,
                    "why_relevant": item.extraction_result.why_relevant,
                    "open_questions": item.extraction_result.open_questions,
                    "tags": item.extraction_result.tags,
                }
                if item.extraction_result is not None
                else None
            ),
            "inbox_path": str(item.inbox_path.relative_to(ROOT)) if item.inbox_path is not None else "",
            "source_url_used": item.source_url_used,
            "source_basis": item.source_basis,
            "processed_at": generated_at,
        }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days-back", type=int, default=None, help="How many recent calendar days to query.")
    parser.add_argument("--limit", type=int, default=None, help="Cap the number of unique papers processed.")
    parser.add_argument("--report", type=Path, default=None, help="Generated markdown report path.")
    parser.add_argument("--inbox-dir", type=Path, default=None, help="Where accepted paper files should be written.")
    parser.add_argument("--state", type=Path, default=None, help="JSON state path used to avoid duplicate work.")
    parser.add_argument(
        "--refresh-known",
        action="store_true",
        help="Re-run filtering and extraction even for papers already recorded in state.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env_file(DEFAULT_ENV_FILE)

    days_back = args.days_back or int(env("HF_DAILY_PAPERS_DAYS", required=False, default="3"))
    limit = args.limit or int(env("HF_DAILY_PAPERS_LIMIT", required=False, default="25"))
    report_path = args.report or Path(env("HF_DAILY_PAPERS_REPORT", required=False, default=str(DEFAULT_REPORT)))
    inbox_dir = args.inbox_dir or Path(env("HF_DAILY_PAPERS_INBOX_DIR", required=False, default=str(DEFAULT_INBOX_DIR)))
    state_path = args.state or Path(env("HF_DAILY_PAPERS_STATE", required=False, default=str(DEFAULT_STATE)))

    if not report_path.is_absolute():
        report_path = ROOT / report_path
    if not inbox_dir.is_absolute():
        inbox_dir = ROOT / inbox_dir
    if not state_path.is_absolute():
        state_path = ROOT / state_path

    filter_prompt_path = resolve_root_path(
        Path(env("HF_DAILY_PAPERS_FILTER_PROMPT", required=False, default=str(DEFAULT_FILTER_PROMPT)))
    )
    extraction_prompt_path = resolve_root_path(
        Path(env("HF_DAILY_PAPERS_EXTRACTION_PROMPT", required=False, default=str(DEFAULT_EXTRACTION_PROMPT)))
    )
    filter_prompt = read_text_if_exists(filter_prompt_path)
    extraction_prompt = read_text_if_exists(extraction_prompt_path)

    papers = collect_recent_papers(days_back)
    if limit > 0:
        papers = papers[:limit]

    state = load_state(state_path)
    state_papers = state.get("papers", {})
    processed_items: list[ProcessedPaper] = []

    for paper in papers:
        state_entry = state_papers.get(paper.paper_id)
        if isinstance(state_entry, dict) and not args.refresh_known:
            reused = processed_from_state(paper, state_entry)
            if reused is not None:
                processed_items.append(reused)
                continue

        filter_payload = invoke_codex_json(filter_prompt, build_filter_input(paper))
        filter_result = parse_filter_result(filter_payload)

        extraction_result = None
        inbox_path = None
        source_url_used = ""
        source_basis = ""
        if should_stage(filter_result):
            source_url_used, source_basis, source_text = fetch_original_source_context(paper)
            extraction_payload = invoke_codex_json(
                extraction_prompt,
                build_extraction_input(paper, filter_result, source_url_used, source_basis, source_text),
            )
            extraction_result = parse_extraction_result(extraction_payload)
            inbox_path = write_inbox_file(
                paper,
                filter_result,
                extraction_result,
                source_url_used,
                source_basis,
                source_text,
                inbox_dir,
            )

        processed_items.append(
            ProcessedPaper(
                paper=paper,
                filter_result=filter_result,
                extraction_result=extraction_result,
                inbox_path=inbox_path,
                reused_from_state=False,
                source_url_used=source_url_used,
                source_basis=source_basis,
            )
        )

    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    report = render_report(processed_items, generated_at, days_back)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    update_state(state_path, state, processed_items, generated_at)

    staged = sum(1 for item in processed_items if item.inbox_path is not None)
    print(
        f"Updated {report_path.relative_to(ROOT)} with {len(processed_items)} papers; "
        f"staged {staged} files in {inbox_dir.relative_to(ROOT)}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
