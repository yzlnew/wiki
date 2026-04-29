#!/usr/bin/env python3
"""Run daily source updates and email a digest."""

from __future__ import annotations

import html as html_lib
import os
import re
import base64
import json
import smtplib
import ssl
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path
from urllib import error, parse, request


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


def parse_markdown_links_under_section(report_text: str, section: str, limit: int = 5) -> list[tuple[str, str]]:
    pattern = rf"^## {re.escape(section)}\n\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, report_text, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    block = match.group(1)
    items = re.findall(r"^- \[(.+?)\]\((.+?)\)", block, re.MULTILINE)
    return [(title, url) for title, url in items[:limit]]


def parse_staged_files(report_text: str, limit: int = 10) -> list[str]:
    match = re.search(r"^## Staged Files\n\n(.*?)(?=^## |\Z)", report_text, re.MULTILINE | re.DOTALL)
    if not match:
        return []
    return re.findall(r"^- `(.+?)`", match.group(1), re.MULTILINE)[:limit]


def parse_bookmarks_latest(report_text: str, limit: int = 5) -> list[tuple[str, str, str]]:
    items = re.findall(r"^- \[(.+?)\]\((.+?)\)\n  - added: `([^`]+)`", report_text, re.MULTILINE)
    return [(title, url, added) for title, url, added in items[:limit]]


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
        for title, url, added in latest_bookmarks:
            lines.append(f"- {title} | {added} | {url}")
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
    if freshrss_accept:
        lines.extend(f"- {title} | {url}" for title, url in freshrss_accept)
    else:
        lines.append("- none")
    lines.append("- maybe:")
    freshrss_maybe = parse_markdown_links_under_section(freshrss_text, "Maybe")
    if freshrss_maybe:
        lines.extend(f"- {title} | {url}" for title, url in freshrss_maybe)
    else:
        lines.append("- none")
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
    if hf_accept:
        lines.extend(f"- {title} | {url}" for title, url in hf_accept)
    else:
        lines.append("- none")
    lines.append("- maybe:")
    hf_maybe = parse_markdown_links_under_section(hf_text, "Maybe")
    if hf_maybe:
        lines.extend(f"- {title} | {url}" for title, url in hf_maybe)
    else:
        lines.append("- none")

    return "\n".join(lines).rstrip() + "\n"


def _h(s: str) -> str:
    return html_lib.escape(s, quote=True)


def _section_heading(text: str) -> str:
    return (
        f'<h3 style="margin:20px 0 8px 0;font-size:16px;border-bottom:1px solid #d0d7de;'
        f'padding-bottom:4px;color:#1f2328;">{_h(text)}</h3>'
    )


def _kv_table(rows: list[tuple[str, str]]) -> str:
    body = "".join(
        f'<tr>'
        f'<td style="padding:4px 10px;border:1px solid #d0d7de;color:#57606a;'
        f'background:#f6f8fa;width:170px;font-family:ui-monospace,Menlo,Consolas,monospace;'
        f'font-size:12px;">{_h(k)}</td>'
        f'<td style="padding:4px 10px;border:1px solid #d0d7de;">{_h(v)}</td>'
        f'</tr>'
        for k, v in rows
    )
    return (
        '<table style="border-collapse:collapse;font-size:13px;margin:0 0 12px 0;">'
        f'{body}</table>'
    )


def _link_list(items: list[tuple[str, str]]) -> str:
    if not items:
        return '<p style="color:#57606a;font-size:13px;margin:0 0 12px 0;">none</p>'
    li = "".join(
        f'<li style="margin:4px 0;"><a href="{_h(url)}" '
        f'style="color:#0969da;text-decoration:none;">{_h(title)}</a></li>'
        for title, url in items
    )
    return f'<ul style="padding-left:22px;font-size:14px;margin:0 0 12px 0;">{li}</ul>'


def _bookmarks_list(items: list[tuple[str, str, str]]) -> str:
    if not items:
        return '<p style="color:#57606a;font-size:13px;margin:0 0 12px 0;">none</p>'
    li = "".join(
        f'<li style="margin:4px 0;">'
        f'<a href="{_h(url)}" style="color:#0969da;text-decoration:none;">{_h(title)}</a> '
        f'<span style="color:#57606a;font-size:12px;">· added {_h(added)}</span>'
        f'</li>'
        for title, url, added in items
    )
    return f'<ul style="padding-left:22px;font-size:14px;margin:0 0 12px 0;">{li}</ul>'


def _subheading(text: str) -> str:
    return (
        f'<div style="font-size:12px;color:#57606a;margin:8px 0 4px 0;'
        f'text-transform:uppercase;letter-spacing:0.5px;">{_h(text)}</div>'
    )


def build_digest_html(results: list[CommandResult]) -> str:
    bookmarks_text = read_text_if_exists(BOOKMARKS_REPORT)
    freshrss_text = read_text_if_exists(FRESHRSS_REPORT)
    hf_text = read_text_if_exists(HF_REPORT)
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")

    parts: list[str] = [
        '<div style="font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif;'
        'color:#1f2328;max-width:760px;margin:0 auto;padding:8px 12px;line-height:1.5;">',
        '<h2 style="margin:0 0 4px 0;font-size:20px;">Wiki daily sources digest</h2>',
        f'<div style="color:#57606a;font-size:12px;margin-bottom:12px;">{_h(generated_at)}</div>',
    ]

    parts.append(_section_heading("Run status"))
    status_rows = []
    for r in results:
        if r.returncode == 0:
            status_html = '<span style="color:#1a7f37;font-weight:600;">ok</span>'
        else:
            status_html = (
                f'<span style="color:#cf222e;font-weight:600;">'
                f'failed ({_h(str(r.returncode))})</span>'
            )
        detail_html = ""
        if r.stderr and r.returncode != 0:
            detail_html = (
                f'<div style="color:#57606a;font-size:12px;margin-top:4px;'
                f'font-family:ui-monospace,Menlo,Consolas,monospace;white-space:pre-wrap;">'
                f'{_h(r.stderr[:500])}</div>'
            )
        status_rows.append(
            '<tr>'
            f'<td style="padding:6px 10px;border:1px solid #d0d7de;'
            f'font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;">{_h(r.name)}</td>'
            f'<td style="padding:6px 10px;border:1px solid #d0d7de;">{status_html}{detail_html}</td>'
            '</tr>'
        )
    parts.append(
        '<table style="border-collapse:collapse;font-size:14px;margin:0 0 12px 0;width:100%;">'
        '<thead><tr style="background:#f6f8fa;">'
        '<th style="text-align:left;padding:6px 10px;border:1px solid #d0d7de;width:200px;">Step</th>'
        '<th style="text-align:left;padding:6px 10px;border:1px solid #d0d7de;">Status</th>'
        '</tr></thead>'
        f'<tbody>{"".join(status_rows)}</tbody></table>'
    )

    parts.append(_section_heading("Bookmarks"))
    parts.append(_kv_table([
        ("generated_at", summary_value(bookmarks_text, "generated_at")),
        ("total_links", summary_value(bookmarks_text, "total_links")),
        ("archived_links", summary_value(bookmarks_text, "archived_links")),
        ("favourited_links", summary_value(bookmarks_text, "favourited_links")),
    ]))
    parts.append(_subheading("Latest links"))
    parts.append(_bookmarks_list(parse_bookmarks_latest(bookmarks_text)))

    parts.append(_section_heading("FreshRSS"))
    parts.append(_kv_table([
        ("generated_at", summary_value(freshrss_text, "generated_at")),
        ("total_items", summary_value(freshrss_text, "total_items")),
        ("accepted", summary_value(freshrss_text, "accepted")),
        ("maybe", summary_value(freshrss_text, "maybe")),
        ("rejected", summary_value(freshrss_text, "rejected")),
        ("staged_for_ingest", summary_value(freshrss_text, "staged_for_ingest")),
    ]))
    parts.append(_subheading("Accepted"))
    parts.append(_link_list(parse_markdown_links_under_section(freshrss_text, "Accepted")))
    parts.append(_subheading("Maybe"))
    parts.append(_link_list(parse_markdown_links_under_section(freshrss_text, "Maybe")))
    staged = parse_staged_files(freshrss_text)
    if staged:
        parts.append(_subheading("Staged files"))
        items = "".join(
            f'<li style="margin:2px 0;"><code style="background:#f6f8fa;padding:1px 6px;'
            f'border-radius:3px;font-size:12px;">{_h(p)}</code></li>'
            for p in staged
        )
        parts.append(f'<ul style="padding-left:22px;margin:0 0 12px 0;">{items}</ul>')

    parts.append(_section_heading("HF Daily Papers"))
    parts.append(_kv_table([
        ("generated_at", summary_value(hf_text, "generated_at")),
        ("total_items", summary_value(hf_text, "total_items")),
        ("accepted", summary_value(hf_text, "accepted")),
        ("maybe", summary_value(hf_text, "maybe")),
        ("rejected", summary_value(hf_text, "rejected")),
        ("staged_for_ingest", summary_value(hf_text, "staged_for_ingest")),
    ]))
    parts.append(_subheading("Accepted"))
    parts.append(_link_list(parse_markdown_links_under_section(hf_text, "Accept")))
    parts.append(_subheading("Maybe"))
    parts.append(_link_list(parse_markdown_links_under_section(hf_text, "Maybe")))

    parts.append("</div>")
    return "".join(parts)


def build_message(subject: str, body: str, html_body: str | None = None) -> EmailMessage:
    to_addr = env("DAILY_DIGEST_TO")
    from_addr = env("DAILY_DIGEST_FROM", required=False, default="")
    if not from_addr:
        from_addr = env("DAILY_DIGEST_SMTP_USERNAME", required=False, default=f"wiki@{os.uname().nodename}")
    reply_to = env("DAILY_DIGEST_REPLY_TO", required=False, default="")

    msg = EmailMessage()
    msg["To"] = to_addr
    msg["From"] = from_addr
    msg["Subject"] = subject
    if reply_to:
        msg["Reply-To"] = reply_to
    msg.set_content(body)
    if html_body:
        msg.add_alternative(html_body, subtype="html")
    return msg


def open_smtp_connection(host: str, port: int, security: str, timeout: int) -> smtplib.SMTP:
    if security == "ssl":
        smtp = smtplib.SMTP_SSL(host, port, timeout=timeout, context=ssl.create_default_context())
        smtp.ehlo()
        return smtp

    smtp = smtplib.SMTP(host, port, timeout=timeout)
    smtp.ehlo()
    if security == "starttls":
        smtp.starttls(context=ssl.create_default_context())
        smtp.ehlo()
    return smtp


def send_via_sendmail(msg: EmailMessage) -> None:
    sendmail_bin = env("DAILY_DIGEST_SENDMAIL_BIN", required=False, default="/usr/sbin/sendmail")
    timeout = int(env("DAILY_DIGEST_SEND_TIMEOUT", required=False, default="120"))

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


def fetch_gmail_oauth_access_token() -> str:
    client_id = env("DAILY_DIGEST_GMAIL_OAUTH_CLIENT_ID")
    client_secret = env("DAILY_DIGEST_GMAIL_OAUTH_CLIENT_SECRET")
    refresh_token = env("DAILY_DIGEST_GMAIL_OAUTH_REFRESH_TOKEN")
    token_url = env(
        "DAILY_DIGEST_GMAIL_OAUTH_TOKEN_URL",
        required=False,
        default="https://oauth2.googleapis.com/token",
    )
    timeout = int(env("DAILY_DIGEST_SEND_TIMEOUT", required=False, default="120"))

    payload = parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }
    ).encode("utf-8")
    req = request.Request(
        token_url,
        data=payload,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8")
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace").strip()
        raise SystemExit(f"Gmail OAuth token request failed: HTTP {exc.code}: {details}") from exc
    except error.URLError as exc:
        raise SystemExit(f"Gmail OAuth token request failed: {exc.reason}") from exc

    try:
        token_payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Gmail OAuth token response was not valid JSON: {raw[:300]}") from exc

    access_token = str(token_payload.get("access_token", "")).strip()
    if not access_token:
        raise SystemExit(f"Gmail OAuth token response missing access_token: {raw[:300]}")
    return access_token


def smtp_auth_xoauth2(smtp: smtplib.SMTP, username: str, access_token: str) -> None:
    auth_string = f"user={username}\x01auth=Bearer {access_token}\x01\x01"
    encoded = base64.b64encode(auth_string.encode("utf-8")).decode("ascii")
    code, response = smtp.docmd("AUTH", f"XOAUTH2 {encoded}")
    if code != 235:
        detail = response.decode("utf-8", errors="replace") if isinstance(response, bytes) else str(response)
        raise SystemExit(f"SMTP XOAUTH2 auth failed: {code} {detail}")


def send_via_smtp(msg: EmailMessage) -> None:
    host = env("DAILY_DIGEST_SMTP_HOST")
    username = env("DAILY_DIGEST_SMTP_USERNAME")
    port = int(env("DAILY_DIGEST_SMTP_PORT", required=False, default="465"))
    security = env("DAILY_DIGEST_SMTP_SECURITY", required=False, default="ssl").strip().lower()
    auth_method = env("DAILY_DIGEST_SMTP_AUTH_METHOD", required=False, default="password").strip().lower()
    timeout = int(env("DAILY_DIGEST_SEND_TIMEOUT", required=False, default="120"))

    if security not in {"ssl", "starttls", "none"}:
        raise SystemExit(
            "Unsupported DAILY_DIGEST_SMTP_SECURITY; expected one of: ssl, starttls, none"
        )
    if auth_method not in {"password", "gmail-oauth2"}:
        raise SystemExit(
            "Unsupported DAILY_DIGEST_SMTP_AUTH_METHOD; expected one of: password, gmail-oauth2"
        )

    with open_smtp_connection(host, port, security, timeout) as smtp:
        if auth_method == "gmail-oauth2":
            access_token = fetch_gmail_oauth_access_token()
            smtp_auth_xoauth2(smtp, username, access_token)
        else:
            password = env("DAILY_DIGEST_SMTP_PASSWORD")
            smtp.login(username, password)
        smtp.send_message(msg)


def send_digest(subject: str, body: str, html_body: str | None = None) -> None:
    msg = build_message(subject, body, html_body)
    smtp_host = env("DAILY_DIGEST_SMTP_HOST", required=False, default="")
    if smtp_host:
        send_via_smtp(msg)
        return
    send_via_sendmail(msg)


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
    html_body = build_digest_html(results)
    send_digest(subject, body, html_body)

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
