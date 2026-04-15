#!/usr/bin/env python3
"""Sync recent FreshRSS items, filter them, and stage accepted articles for ingest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import socket
import ssl
import sys
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib import parse, request


sys.path.insert(0, str(Path(__file__).resolve().parent))
from interests import load_interests, get_rss_rules

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = ROOT / ".env.freshrss.local"
DEFAULT_REPORT = ROOT / "sources/library/freshrss/freshrss-latest.md"
DEFAULT_INBOX_DIR = ROOT / "sources/inbox/freshrss"

# Loaded from system/interests.json (or .example.json as fallback).
_interests = load_interests()
PRIMARY_INTEREST_RULES, STYLE_RULES, SOURCE_BOOST_RULES, WEAK_SIGNAL_RULES, DOWNRANK_RULES = get_rss_rules(_interests)


@dataclass
class FeedItem:
    item_id: str
    title: str
    url: str
    source: str
    source_url: str
    published: datetime
    categories: list[str]
    summary_html: str


@dataclass
class FilterResult:
    decision: str
    score: int
    reason: str
    matched_interests: list[str] = field(default_factory=list)
    weak_signals: list[str] = field(default_factory=list)
    downrank_signals: list[str] = field(default_factory=list)


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


def normalize_base_url(base_url: str) -> str:
    clean = base_url.strip()
    if not clean:
        raise SystemExit("FRESHRSS_BASE_URL must not be empty")
    if not clean.startswith(("http://", "https://")):
        clean = f"http://{clean}"
    return clean.rstrip("/")


def freshrss_api_base(base_url: str) -> str:
    explicit = env("FRESHRSS_API_BASE", required=False, default="").strip()
    if explicit:
        return explicit.rstrip("/")
    return f"{normalize_base_url(base_url)}/api/greader.php"


def http_request(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    data: bytes | None = None,
    timeout_env: str,
    verify_env: str,
    ip_prefix: str,
) -> request.addinfourl:
    req = request.Request(
        url,
        data=data,
        headers={
            "User-Agent": env("FRESHRSS_USER_AGENT", required=False, default="wiki-freshrss-sync/1.0"),
            **(headers or {}),
        },
    )
    timeout = float(env(timeout_env, required=False, default="30"))
    context = build_ssl_context(verify_env)
    with force_ip_family_if_needed(ip_prefix):
        return request.urlopen(req, timeout=timeout, context=context)


def client_login(api_base: str, username: str, api_password: str) -> str:
    payload = parse.urlencode({"Email": username, "Passwd": api_password}).encode("utf-8")
    with http_request(
        f"{api_base}/accounts/ClientLogin",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=payload,
        timeout_env="FRESHRSS_TIMEOUT",
        verify_env="FRESHRSS_VERIFY_TLS",
        ip_prefix="FRESHRSS",
    ) as resp:
        body = resp.read().decode("utf-8", errors="replace")

    for line in body.splitlines():
        if line.startswith("Auth="):
            token = line.split("=", 1)[1].strip()
            if token:
                return token
    raise SystemExit("FreshRSS ClientLogin succeeded but Auth token was missing")


def api_get_json(api_base: str, auth_token: str, path: str, params: dict[str, Any]) -> Any:
    query = parse.urlencode({key: value for key, value in params.items() if value is not None})
    url = f"{api_base}{path}"
    if query:
        url = f"{url}?{query}"
    with http_request(
        url,
        headers={
            "Authorization": f"GoogleLogin auth={auth_token}",
            "Accept": "application/json",
        },
        timeout_env="FRESHRSS_TIMEOUT",
        verify_env="FRESHRSS_VERIFY_TLS",
        ip_prefix="FRESHRSS",
    ) as resp:
        return json.load(resp)


def extract_first_href(items: Any) -> str:
    if not isinstance(items, list):
        return ""
    for item in items:
        if isinstance(item, dict):
            href = str(item.get("href", "")).strip()
            if href:
                return href
    return ""


def parse_feed_item(raw_item: dict[str, Any]) -> FeedItem | None:
    title = collapse_whitespace(str(raw_item.get("title", "")))
    url = extract_first_href(raw_item.get("canonical")) or extract_first_href(raw_item.get("alternate"))
    origin = raw_item.get("origin")
    source = ""
    source_url = ""
    if isinstance(origin, dict):
        source = collapse_whitespace(str(origin.get("title", "")))
        source_url = str(origin.get("htmlUrl", "")).strip()
    if not title or not url:
        return None

    published_raw = raw_item.get("published")
    try:
        published = datetime.fromtimestamp(int(published_raw), tz=timezone.utc).astimezone()
    except Exception:
        published = datetime.now(timezone.utc).astimezone()

    summary = raw_item.get("summary")
    summary_html = ""
    if isinstance(summary, dict):
        summary_html = str(summary.get("content", "")).strip()

    categories = [str(item).strip() for item in raw_item.get("categories", []) if str(item).strip()]

    return FeedItem(
        item_id=str(raw_item.get("id", "")),
        title=title,
        url=url,
        source=source or "unknown",
        source_url=source_url,
        published=published,
        categories=categories,
        summary_html=summary_html,
    )


def fetch_recent_items(api_base: str, auth_token: str, limit: int) -> list[FeedItem]:
    payload = api_get_json(
        api_base,
        auth_token,
        "/reader/api/0/stream/contents/reading-list",
        {"n": limit, "output": "json"},
    )
    items = payload.get("items") if isinstance(payload, dict) else None
    if not isinstance(items, list):
        raise SystemExit("Unexpected FreshRSS response shape: missing items array")

    parsed: list[FeedItem] = []
    for raw_item in items:
        if not isinstance(raw_item, dict):
            continue
        item = parse_feed_item(raw_item)
        if item is not None:
            parsed.append(item)
    return parsed


def collapse_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def contains_any(text: str, patterns: tuple[str, ...]) -> bool:
    return any(pattern in text for pattern in patterns)


def score_item(item: FeedItem) -> FilterResult:
    title_text = item.title.lower()
    source_text = item.source.lower()
    combined = f"{source_text} {title_text}"

    score = 40
    matched_interests: list[str] = []
    weak_signals: list[str] = []
    downrank_signals: list[str] = []

    for label, weight, patterns in PRIMARY_INTEREST_RULES:
        if contains_any(combined, patterns):
            score += weight
            matched_interests.append(label)

    for label, weight, patterns in STYLE_RULES:
        if contains_any(title_text, patterns):
            score += weight
            matched_interests.append(label)

    for label, weight, patterns in SOURCE_BOOST_RULES:
        if contains_any(source_text, patterns):
            score += weight
            matched_interests.append(label)

    for label, weight, patterns in WEAK_SIGNAL_RULES:
        if contains_any(combined, patterns):
            score += weight
            weak_signals.append(label)

    for label, weight, patterns in DOWNRANK_RULES:
        if contains_any(combined, patterns):
            score += weight
            downrank_signals.append(label)

    if title_text.endswith("?"):
        score -= 8
        downrank_signals.append("question-title")
    if re.search(r"\b(help|question|thoughts|anyone|worth)\b", title_text):
        score -= 10
        downrank_signals.append("discussion-title")
    if not matched_interests:
        score -= 24
        downrank_signals.append("no-strong-interest-match")

    score = max(0, min(100, score))

    if score >= 80:
        decision = "accept"
    elif score >= 55:
        decision = "maybe"
    else:
        decision = "reject"

    if matched_interests and decision == "accept":
        reason = f"Strong fit for {matched_interests[0]} with useful signal in source/title."
    elif matched_interests and decision == "maybe":
        reason = f"Relevant to {matched_interests[0]} but signal is mixed before full-text fetch."
    elif downrank_signals:
        reason = f"Low-value metadata due to {downrank_signals[0]}."
    else:
        reason = "Weak match based on source and title only."

    return FilterResult(
        decision=decision,
        score=score,
        reason=reason,
        matched_interests=dedupe_preserve_order(matched_interests),
        weak_signals=dedupe_preserve_order(weak_signals),
        downrank_signals=dedupe_preserve_order(downrank_signals),
    )


def dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


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


def fetch_article_text(url: str) -> tuple[str, str, str]:
    with http_request(
        url,
        headers={"Accept": "text/html,application/xhtml+xml"},
        timeout_env="ARTICLE_TIMEOUT",
        verify_env="ARTICLE_VERIFY_TLS",
        ip_prefix="ARTICLE",
    ) as resp:
        content_type = resp.headers.get("Content-Type", "")
        raw = resp.read()

    charset = "utf-8"
    match = re.search(r"charset=([\w-]+)", content_type, re.IGNORECASE)
    if match:
        charset = match.group(1)
    html = raw.decode(charset, errors="replace")
    title, text = html_to_text(html)
    description = extract_meta_description(html)
    return title, description, text


def summary_snippet(summary_html: str, limit: int = 320) -> str:
    _, text = html_to_text(summary_html)
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def summary_text(summary_html: str) -> str:
    _, text = html_to_text(summary_html)
    return text


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:80] or "item"


def item_suffix(item_id: str) -> str:
    match = re.search(r"([0-9a-f]{8,})$", item_id.lower())
    if match:
        return match.group(1)[-10:]
    return hashlib.sha1(item_id.encode("utf-8")).hexdigest()[:10]


def render_report(items: list[tuple[FeedItem, FilterResult]], generated_at: str, staged_files: list[Path]) -> str:
    counts = {"accept": 0, "maybe": 0, "reject": 0}
    for _, result in items:
        counts[result.decision] += 1

    lines = [
        "---",
        "type: source-summary",
        "status: active",
        "tags: [freshrss, rss, generated]",
        f"source_count: {len(items)}",
        f"updated: {generated_at[:10]}",
        "generator: scripts/update_freshrss.py",
        "---",
        "",
        "# FreshRSS Latest",
        "",
        "## Summary",
        "",
        f"- generated_at: {generated_at}",
        f"- total_items: {len(items)}",
        f"- accepted: {counts['accept']}",
        f"- maybe: {counts['maybe']}",
        f"- rejected: {counts['reject']}",
        f"- staged_for_ingest: {len(staged_files)}",
        "- filter_input: source + title only before article fetch",
        "",
        "## Notes",
        "",
        "- This file is generated from FreshRSS metadata and should be updated by script, not edited by hand.",
        "- Accepted items are fetched to `sources/inbox/freshrss/` for later ingest.",
        "- FreshRSS credentials are read from local ignored config and are not stored here.",
        "",
        "## Accepted",
        "",
    ]

    for decision in ("accept", "maybe", "reject"):
        decision_items = [(item, result) for item, result in items if result.decision == decision]
        if decision != "accept":
            lines.extend([f"## {decision.title()}", ""])
        if not decision_items:
            lines.extend(["- none", ""])
            continue
        for item, result in decision_items:
            lines.append(f"- [{escape_markdown(item.title)}]({item.url})")
            meta = [
                f"source: `{escape_backticks(item.source)}`",
                f"published: `{item.published.isoformat(timespec='seconds')}`",
                f"decision: `{result.decision}`",
                f"score: `{result.score}`",
            ]
            lines.append(f"  - {'; '.join(meta)}")
            lines.append(f"  - reason: {escape_markdown(result.reason)}")
            if result.matched_interests:
                lines.append("  - matched: " + ", ".join(f"`{escape_backticks(item)}`" for item in result.matched_interests))
            if result.weak_signals:
                lines.append("  - weak_signals: " + ", ".join(f"`{escape_backticks(item)}`" for item in result.weak_signals))
            if result.downrank_signals:
                lines.append("  - downrank: " + ", ".join(f"`{escape_backticks(item)}`" for item in result.downrank_signals))
        lines.append("")

    if staged_files:
        lines.extend(["## Staged Files", ""])
        for path in staged_files:
            lines.append(f"- `{path.relative_to(ROOT)}`")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def escape_markdown(text: str) -> str:
    return text.replace("\n", " ").replace("[", r"\[").replace("]", r"\]")


def escape_backticks(text: str) -> str:
    return text.replace("`", "'")


def write_article_file(
    item: FeedItem,
    result: FilterResult,
    output_dir: Path,
    *,
    fetched_title: str,
    fetched_description: str,
    fetched_text: str,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(item.title)
    filename = f"{item.published.date().isoformat()}-{slug}-{item_suffix(item.item_id)}.md"
    path = output_dir / filename
    summary = summary_snippet(item.summary_html)
    lines = [
        "---",
        "type: source-summary",
        "status: active",
        "tags: [freshrss, rss, inbox]",
        "source_count: 1",
        f"updated: {datetime.now(timezone.utc).astimezone().date().isoformat()}",
        f"source_url: {item.url}",
        f"feed_source: {item.source}",
        f"published: {item.published.isoformat(timespec='seconds')}",
        f"decision: {result.decision}",
        f"score: {result.score}",
        "generator: scripts/update_freshrss.py",
        "---",
        "",
        f"# {item.title}",
        "",
        "## Summary",
        "",
        f"- source_feed: `{item.source}`",
        f"- original_url: {item.url}",
        f"- published: `{item.published.isoformat(timespec='seconds')}`",
        f"- filter_reason: {result.reason}",
        "",
        "## Feed Metadata",
        "",
    ]
    if item.source_url:
        lines.append(f"- source_home: {item.source_url}")
    if item.categories:
        lines.append("- categories: " + ", ".join(f"`{escape_backticks(category)}`" for category in item.categories))
    if summary:
        lines.append(f"- feed_summary: {escape_markdown(summary)}")
    if fetched_title:
        lines.append(f"- fetched_page_title: {escape_markdown(fetched_title)}")
    if fetched_description:
        lines.append(f"- fetched_page_description: {escape_markdown(fetched_description)}")
    lines.extend(["", "## Full Text", ""])
    if fetched_text:
        lines.append(fetched_text)
    else:
        lines.append("Full text fetch failed or returned too little content.")
    lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def should_stage(result: FilterResult, include_maybe: bool) -> bool:
    return result.decision == "accept" or (include_maybe and result.decision == "maybe")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=None, help="Number of recent FreshRSS items to inspect.")
    parser.add_argument(
        "--include-maybe",
        action="store_true",
        help="Also fetch full text for maybe items instead of only accepted ones.",
    )
    parser.add_argument("--report", type=Path, default=None, help="Generated markdown report path.")
    parser.add_argument("--inbox-dir", type=Path, default=None, help="Where accepted article files should be written.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    load_env_file(DEFAULT_ENV_FILE)

    base_url = env("FRESHRSS_BASE_URL")
    username = env("FRESHRSS_USERNAME")
    api_password = env("FRESHRSS_API_PASSWORD")
    limit = args.limit or int(env("FRESHRSS_LIMIT", required=False, default="50"))
    include_maybe = args.include_maybe or env("FRESHRSS_INCLUDE_MAYBE", required=False, default="0").lower() in {"1", "true", "yes"}

    report_path = args.report or Path(env("FRESHRSS_REPORT", required=False, default=str(DEFAULT_REPORT)))
    if not report_path.is_absolute():
        report_path = ROOT / report_path

    inbox_dir = args.inbox_dir or Path(env("FRESHRSS_INBOX_DIR", required=False, default=str(DEFAULT_INBOX_DIR)))
    if not inbox_dir.is_absolute():
        inbox_dir = ROOT / inbox_dir

    api_base = freshrss_api_base(base_url)
    auth_token = client_login(api_base, username, api_password)
    items = fetch_recent_items(api_base, auth_token, limit)

    scored_items = [(item, score_item(item)) for item in items]
    staged_files: list[Path] = []

    for item, result in scored_items:
        if not should_stage(result, include_maybe):
            continue
        fetched_title = ""
        fetched_description = ""
        fetched_text = ""
        try:
            fetched_title, fetched_description, fetched_text = fetch_article_text(item.url)
        except Exception as exc:  # pragma: no cover - depends on remote sites
            fetched_description = f"fetch_error: {exc}"

        summary_full = summary_text(item.summary_html)
        if "reddit.com" in item.url and len(summary_full) >= 400:
            fetched_text = summary_full
        elif len(fetched_text) < 800 and len(summary_full) > len(fetched_text):
            fetched_text = summary_full[:4000]

        staged_files.append(
            write_article_file(
                item,
                result,
                inbox_dir,
                fetched_title=fetched_title,
                fetched_description=fetched_description,
                fetched_text=fetched_text,
            )
        )

    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    report = render_report(scored_items, generated_at, staged_files)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")

    print(
        f"Updated {report_path.relative_to(ROOT)} with {len(items)} items; "
        f"staged {len(staged_files)} files in {inbox_dir.relative_to(ROOT)}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
