#!/usr/bin/env python3
"""Run daily source updates and email a digest."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = ROOT / ".env.daily-digest.local"
BOOKMARKS_REPORT = ROOT / "sources/library/bookmarks/bookmarks.md"
FRESHRSS_REPORT = ROOT / "sources/library/freshrss/freshrss-latest.md"
HF_REPORT = ROOT / "sources/library/hf-daily-papers/hf-daily-papers-latest.md"


@dataclass
class CommandResult:
    name: str
    cmd: list[str]
    returncode: int
    stdout: str
    stderr: str


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


def run_command(name: str, cmd: list[str]) -> CommandResult:
    timeout = int(env("DAILY_DIGEST_STEP_TIMEOUT", required=False, default="1800"))
    retries = int(env("DAILY_DIGEST_STEP_RETRIES", required=False, default="1"))
    attempt = 0
    last_result: CommandResult | None = None
    while attempt <= retries:
        try:
            completed = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False, timeout=timeout)
            result = CommandResult(
                name=name,
                cmd=cmd,
                returncode=completed.returncode,
                stdout=completed.stdout.strip(),
                stderr=completed.stderr.strip(),
            )
        except subprocess.TimeoutExpired as exc:
            result = CommandResult(
                name=name,
                cmd=cmd,
                returncode=124,
                stdout=(exc.stdout or "").strip() if isinstance(exc.stdout, str) else "",
                stderr=f"timed out after {timeout}s",
            )
        if result.returncode == 0:
            return result
        last_result = result
        attempt += 1
    assert last_result is not None
    return last_result


def read_text_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def summary_value(report_text: str, key: str) -> str:
    match = re.search(rf"^- {re.escape(key)}: (.+)$", report_text, re.MULTILINE)
    return match.group(1).strip() if match else "unknown"


def parse_markdown_links_under_section(report_text: str, section: str, limit: int = 5) -> list[str]:
    pattern = rf"^## {re.escape(section)}\n\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, report_text, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    block = match.group(1)
    items = re.findall(r"^- \[(.+?)\]\((.+?)\)", block, re.MULTILINE)
    result: list[str] = []
    for title, url in items[:limit]:
        result.append(f"- {title} | {url}")
    return result


def parse_staged_files(report_text: str, limit: int = 10) -> list[str]:
    match = re.search(r"^## Staged Files\n\n(.*?)(?=^## |\Z)", report_text, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    return re.findall(r"^- `(.+?)`", match.group(1), re.MULTILINE)[:limit]


def parse_bookmarks_latest(report_text: str) -> list[str]:
    items = re.findall(r"^- \[(.+?)\]\((.+?)\)\n  - added: `([^`]+)`", report_text, re.MULTILINE)
    return [f"- {title} | {added} | {url}" for title, url, added in items[:5]]


def build_digest(results: list[CommandResult]) -> str:
    bookmarks_text = read_text_if_exists(BOOKMARKS_REPORT)
    freshrss_text = read_text_if_exists(FRESHRSS_REPORT)
    hf_text = read_text_if_exists(HF_REPORT)
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

    lines = [
        f"Wiki daily sources digest",
        f"generated_at: {generated_at}",
        "",
        "Run status",
    ]
    for result in results:
        status = "ok" if result.returncode == 0 else f"failed({result.returncode})"
        lines.append(f"- {result.name}: {status}")
        if result.stdout:
            lines.append(f"  stdout: {result.stdout}")
        if result.stderr:
            lines.append(f"  stderr: {result.stderr}")

    lines.extend(
        [
            "",
            "Bookmarks",
            f"- generated_at: {summary_value(bookmarks_text, 'generated_at')}",
            f"- total_links: {summary_value(bookmarks_text, 'total_links')}",
            f"- archived_links: {summary_value(bookmarks_text, 'archived_links')}",
            f"- favourited_links: {summary_value(bookmarks_text, 'favourited_links')}",
            "- latest links:",
        ]
    )
    latest_bookmarks = parse_bookmarks_latest(bookmarks_text)
    if latest_bookmarks:
        lines.extend(latest_bookmarks)
    else:
        lines.append("- none")

    lines.extend(
        [
            "",
            "FreshRSS",
            f"- generated_at: {summary_value(freshrss_text, 'generated_at')}",
            f"- total_items: {summary_value(freshrss_text, 'total_items')}",
            f"- accepted: {summary_value(freshrss_text, 'accepted')}",
            f"- maybe: {summary_value(freshrss_text, 'maybe')}",
            f"- rejected: {summary_value(freshrss_text, 'rejected')}",
            f"- staged_for_ingest: {summary_value(freshrss_text, 'staged_for_ingest')}",
            "- accepted:",
        ]
    )
    freshrss_accept = parse_markdown_links_under_section(freshrss_text, "Accepted")
    lines.extend(freshrss_accept or ["- none"])
    lines.append("- maybe:")
    freshrss_maybe = parse_markdown_links_under_section(freshrss_text, "Maybe")
    lines.extend(freshrss_maybe or ["- none"])
    staged = parse_staged_files(freshrss_text)
    if staged:
        lines.append("- staged files:")
        lines.extend(f"- {path}" for path in staged)

    lines.extend(
        [
            "",
            "HF Daily Papers",
            f"- generated_at: {summary_value(hf_text, 'generated_at')}",
            f"- total_items: {summary_value(hf_text, 'total_items')}",
            f"- accepted: {summary_value(hf_text, 'accepted')}",
            f"- maybe: {summary_value(hf_text, 'maybe')}",
            f"- rejected: {summary_value(hf_text, 'rejected')}",
            f"- staged_for_ingest: {summary_value(hf_text, 'staged_for_ingest')}",
            "- accepted:",
        ]
    )
    hf_accept = parse_markdown_links_under_section(hf_text, "Accept")
    lines.extend(hf_accept or ["- none"])
    lines.append("- maybe:")
    hf_maybe = parse_markdown_links_under_section(hf_text, "Maybe")
    lines.extend(hf_maybe or ["- none"])

    return "\n".join(lines).rstrip() + "\n"


def send_via_sendmail(subject: str, body: str) -> None:
    to_addr = env("DAILY_DIGEST_TO")
    sendmail_bin = env("DAILY_DIGEST_SENDMAIL_BIN", required=False, default="/usr/sbin/sendmail")
    from_addr = env("DAILY_DIGEST_FROM", required=False, default=f"wiki@{os.uname().nodename}")
    reply_to = env("DAILY_DIGEST_REPLY_TO", required=False, default="")
    timeout = int(env("DAILY_DIGEST_SEND_TIMEOUT", required=False, default="120"))

    msg = EmailMessage()
    msg["To"] = to_addr
    msg["From"] = from_addr
    msg["Subject"] = subject
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content(body)

    completed = subprocess.run(
        [sendmail_bin, "-t", "-oi"],
        input=msg.as_string(),
        text=True,
        capture_output=True,
        check=False,
        timeout=timeout,
    )
    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip() or f"exit code {completed.returncode}"
        raise SystemExit(f"sendmail failed: {details}")


def main() -> int:
    load_env_file(DEFAULT_ENV_FILE)

    runs = [
        ("bookmarks", ["python3", "scripts/update_bookmarks.py"]),
        ("freshrss", ["python3", "scripts/update_freshrss.py"]),
        ("hf-daily-papers", ["python3", "scripts/update_hf_daily_papers.py"]),
    ]
    results = [run_command(name, cmd) for name, cmd in runs]

    subject_prefix = env("DAILY_DIGEST_SUBJECT_PREFIX", required=False, default="[wiki]")
    subject = f"{subject_prefix} daily sources digest {datetime.now(timezone.utc).astimezone().date().isoformat()}"
    body = build_digest(results)
    send_via_sendmail(subject, body)

    failures = [result.name for result in results if result.returncode != 0]
    if failures:
        print(f"Daily digest sent with failures: {', '.join(failures)}")
        for result in results:
            if result.returncode == 0:
                continue
            print(f"[{result.name}] returncode={result.returncode}")
            if result.stdout:
                print(f"[{result.name}] stdout: {result.stdout}")
            if result.stderr:
                print(f"[{result.name}] stderr: {result.stderr}")
        return 1

    print("Daily digest sent successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
    timeout = int(env("DAILY_DIGEST_SEND_TIMEOUT", required=False, default="120"))
