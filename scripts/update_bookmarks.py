#!/usr/bin/env python3
"""Sync bookmarks into a local markdown source file."""

from __future__ import annotations

import json
import os
import socket
import ssl
import sys
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, parse, request


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = ROOT / ".env.bookmarks.local"
DEFAULT_OUTPUT = ROOT / "sources/library/bookmarks/bookmarks.md"


@dataclass
class Bookmark:
    bookmark_id: str
    url: str
    title: str
    created_at: str
    archived: bool
    favourited: bool
    tags: list[str]
    lists: list[str]
    note: str

    @property
    def month_key(self) -> str:
        if len(self.created_at) >= 7:
            return self.created_at[:7]
        return "unknown"


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


def candidate_api_bases(base_url: str) -> list[str]:
    clean = base_url.rstrip("/")
    candidates = []
    explicit = os.environ.get("BOOKMARKS_API_BASE", "").rstrip("/")
    if explicit:
        candidates.append(explicit)
    candidates.extend([f"{clean}/api/v1", f"{clean}/api", clean])
    deduped: list[str] = []
    for item in candidates:
        if item and item not in deduped:
            deduped.append(item)
    return deduped


def api_get_json(api_base: str, api_key: str, path: str, params: dict[str, Any]) -> Any:
    query = parse.urlencode({key: value for key, value in params.items() if value is not None})
    url = f"{api_base}{path}"
    if query:
        url = f"{url}?{query}"
    req = request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "wiki-bookmarks-sync/1.0",
        },
    )
    timeout = float(env("BOOKMARKS_TIMEOUT", required=False, default="30"))
    context = build_ssl_context()
    with force_ip_family_if_needed():
        with request.urlopen(req, timeout=timeout, context=context) as resp:
            return json.load(resp)


def build_ssl_context() -> ssl.SSLContext | None:
    verify_tls = env("BOOKMARKS_VERIFY_TLS", required=False, default="1").lower()
    if verify_tls in {"0", "false", "no"}:
        return ssl._create_unverified_context()
    return None


@contextmanager
def force_ip_family_if_needed():
    ipv6 = env("BOOKMARKS_FORCE_IPV6", required=False, default="0").lower() in {"1", "true", "yes"}
    ipv4 = env("BOOKMARKS_FORCE_IPV4", required=False, default="0").lower() in {"1", "true", "yes"}
    family = 0
    if ipv6:
        family = socket.AF_INET6
    elif ipv4:
        family = socket.AF_INET

    if family == 0:
        yield
        return

    original = socket.getaddrinfo

    def force_family(host: str, port: int, family: int = 0, type: int = 0, proto: int = 0, flags: int = 0):
        return original(host, port, forced_family, type, proto, flags)

    forced_family = family
    socket.getaddrinfo = force_family
    try:
        yield
    finally:
        socket.getaddrinfo = original


def discover_api_base(base_url: str, api_key: str) -> str:
    last_error: Exception | None = None
    for api_base in candidate_api_bases(base_url):
        try:
            api_get_json(api_base, api_key, "/bookmarks", {"limit": 1})
            return api_base
        except error.HTTPError as exc:
            last_error = exc
            if exc.code in {401, 403}:
                raise SystemExit(f"Authentication failed against {api_base}: HTTP {exc.code}") from exc
            if exc.code == 404:
                continue
            continue
        except Exception as exc:  # pragma: no cover - network failures are runtime-dependent
            last_error = exc
            continue
    if last_error:
        raise SystemExit(f"Unable to discover bookmarks API base: {last_error}")
    raise SystemExit("Unable to discover bookmarks API base")


def extract_string_list(items: Any) -> list[str]:
    result: list[str] = []
    if not isinstance(items, list):
        return result
    for item in items:
        if isinstance(item, str):
            value = item.strip()
        elif isinstance(item, dict):
            value = str(
                item.get("name")
                or item.get("title")
                or item.get("label")
                or item.get("slug")
                or ""
            ).strip()
        else:
            value = ""
        if value and value not in result:
            result.append(value)
    return result


def first_non_empty(*values: Any) -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def parse_bookmark(item: dict[str, Any]) -> Bookmark | None:
    content = item.get("content")
    if not isinstance(content, dict):
        content = {}

    url = first_non_empty(
        item.get("url"),
        content.get("url"),
        item.get("origin"),
    )
    if not url:
        return None

    title = first_non_empty(
        item.get("title"),
        content.get("title"),
        item.get("description"),
        url,
    )
    created_at = first_non_empty(
        item.get("createdAt"),
        item.get("created_at"),
        item.get("savedAt"),
        item.get("updatedAt"),
        "unknown",
    )
    note = first_non_empty(
        item.get("note"),
        item.get("summary"),
        content.get("description"),
        "",
    )

    return Bookmark(
        bookmark_id=str(item.get("id", "")),
        url=url,
        title=title,
        created_at=created_at,
        archived=bool(item.get("archived")),
        favourited=bool(item.get("favourited") or item.get("favorited")),
        tags=extract_string_list(item.get("tags")),
        lists=extract_string_list(item.get("lists")),
        note=note,
    )


def fetch_all_bookmarks(api_base: str, api_key: str, limit: int) -> list[Bookmark]:
    bookmarks: list[Bookmark] = []
    cursor: str | None = None
    while True:
        payload = api_get_json(api_base, api_key, "/bookmarks", {"limit": limit, "cursor": cursor})
        if isinstance(payload, dict):
            items = payload.get("bookmarks")
            if not isinstance(items, list):
                items = payload.get("items")
            if not isinstance(items, list):
                items = payload.get("data")
            if not isinstance(items, list):
                raise SystemExit("Unexpected bookmarks response shape: missing bookmark list")
            next_cursor = payload.get("nextCursor") or payload.get("next_cursor")
        elif isinstance(payload, list):
            items = payload
            next_cursor = None
        else:
            raise SystemExit("Unexpected bookmarks response shape")

        for item in items:
            if not isinstance(item, dict):
                continue
            bookmark = parse_bookmark(item)
            if bookmark is not None:
                bookmarks.append(bookmark)

        if not next_cursor:
            break
        cursor = str(next_cursor)

    bookmarks.sort(key=lambda item: item.created_at, reverse=True)
    return bookmarks


def format_note(note: str) -> str:
    cleaned = " ".join(note.split())
    if len(cleaned) > 220:
        return f"{cleaned[:217]}..."
    return cleaned


def render_markdown(bookmarks: list[Bookmark], generated_at: str) -> str:
    archived_count = sum(1 for item in bookmarks if item.archived)
    favourited_count = sum(1 for item in bookmarks if item.favourited)
    by_month: dict[str, list[Bookmark]] = defaultdict(list)
    for bookmark in bookmarks:
        by_month[bookmark.month_key].append(bookmark)

    lines = [
        "---",
        "type: source-summary",
        "status: active",
        "tags: [bookmarks, generated]",
        f"source_count: {len(bookmarks)}",
        f"updated: {generated_at[:10]}",
        "generator: scripts/update_bookmarks.py",
        "---",
        "",
        "# Bookmarks",
        "",
        "## Summary",
        "",
        f"- generated_at: {generated_at}",
        f"- total_links: {len(bookmarks)}",
        f"- archived_links: {archived_count}",
        f"- favourited_links: {favourited_count}",
        "- source: local bookmarks sync",
        "",
        "## Notes",
        "",
        "- This file is generated from the bookmark sync script and should be updated by script, not edited by hand.",
        "- Instance URL and API key are read from local ignored config and are not stored here.",
        "",
        "## Links",
        "",
    ]

    for month in sorted(by_month.keys(), reverse=True):
        lines.extend([f"### {month}", ""])
        for bookmark in by_month[month]:
            lines.append(f"- [{escape_markdown(bookmark.title)}]({bookmark.url})")
            meta_bits = [f"added: `{bookmark.created_at}`"]
            if bookmark.tags:
                meta_bits.append("tags: " + ", ".join(f"`{escape_backticks(tag)}`" for tag in bookmark.tags))
            if bookmark.lists:
                meta_bits.append("lists: " + ", ".join(f"`{escape_backticks(name)}`" for name in bookmark.lists))
            status_bits = []
            if bookmark.archived:
                status_bits.append("archived")
            if bookmark.favourited:
                status_bits.append("favourited")
            if status_bits:
                meta_bits.append("status: " + ", ".join(status_bits))
            lines.append(f"  - {'; '.join(meta_bits)}")
            if bookmark.note:
                lines.append(f"  - note: {escape_markdown(format_note(bookmark.note))}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def escape_markdown(text: str) -> str:
    return text.replace("\n", " ").replace("[", r"\[").replace("]", r"\]")


def escape_backticks(text: str) -> str:
    return text.replace("`", "'")


def main() -> int:
    load_env_file(DEFAULT_ENV_FILE)

    base_url = env("BOOKMARKS_BASE_URL")
    api_key = env("BOOKMARKS_API_KEY")
    output = Path(env("BOOKMARKS_OUTPUT", required=False, default=str(DEFAULT_OUTPUT)))
    if not output.is_absolute():
        output = ROOT / output
    limit = int(env("BOOKMARKS_LIMIT", required=False, default="100"))

    api_base = discover_api_base(base_url, api_key)
    bookmarks = fetch_all_bookmarks(api_base, api_key, limit)
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    markdown = render_markdown(bookmarks, generated_at)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(markdown, encoding="utf-8")

    print(f"Updated {output.relative_to(ROOT)} with {len(bookmarks)} links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
