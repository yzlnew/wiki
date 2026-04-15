"""Shared loader for the central interests configuration."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INTERESTS_FILE = ROOT / "system" / "interests.json"
EXAMPLE_INTERESTS_FILE = ROOT / "system" / "interests.example.json"


def load_interests(path: Path | None = None) -> dict[str, Any]:
    """Load interests.json, falling back to interests.example.json."""
    if path and path.exists():
        return _read_json(path)
    if DEFAULT_INTERESTS_FILE.exists():
        return _read_json(DEFAULT_INTERESTS_FILE)
    if EXAMPLE_INTERESTS_FILE.exists():
        return _read_json(EXAMPLE_INTERESTS_FILE)
    raise SystemExit(
        "No interests config found. Copy system/interests.example.json to "
        "system/interests.json and customize it."
    )


def _read_json(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, dict):
        raise SystemExit(f"Expected a JSON object in {path}, got {type(data).__name__}")
    return data


def get_rss_rules(
    interests: dict[str, Any],
) -> tuple[
    list[tuple[str, int, tuple[str, ...]]],
    list[tuple[str, int, tuple[str, ...]]],
    list[tuple[str, int, tuple[str, ...]]],
    list[tuple[str, int, tuple[str, ...]]],
    list[tuple[str, int, tuple[str, ...]]],
]:
    """Return (primary, style, source_boost, weak, downrank) rule lists from config."""
    rss = interests.get("rss_filter", {})
    return (
        _rules_from_list(rss.get("primary_interests", [])),
        _rules_from_list(rss.get("style_signals", [])),
        _rules_from_list(rss.get("source_boosts", [])),
        _rules_from_list(rss.get("weak_signals", [])),
        _rules_from_list(rss.get("downranks", [])),
    )


def get_related_topic_links(interests: dict[str, Any]) -> dict[str, str]:
    """Return related_topic_links mapping from config."""
    links = interests.get("related_topic_links", {})
    return {k: v for k, v in links.items() if k != "_comment"}


def get_rss_taste_profile(interests: dict[str, Any]) -> dict[str, list[str]]:
    """Return the natural-language taste profile for the RSS filter prompt."""
    profile = interests.get("rss_taste_profile", {})
    return {k: v for k, v in profile.items() if k != "_comment" and isinstance(v, list)}


def get_paper_filter_profile(interests: dict[str, Any]) -> dict[str, list[str]]:
    """Return the research interest profile for the paper filter prompt."""
    profile = interests.get("paper_filter", {})
    return {k: v for k, v in profile.items() if k != "_comment" and isinstance(v, list)}


def get_paper_knowledge_focus(interests: dict[str, Any]) -> list[str]:
    """Return the user focus list for the paper knowledge extraction prompt."""
    pk = interests.get("paper_knowledge", {})
    return pk.get("user_focus", [])


def render_prompt(template: str, interests: dict[str, Any]) -> str:
    """Replace {{PLACEHOLDER}} markers in a prompt template with interests data.

    Supported placeholders (RSS filter prompt):
      {{HIGH_PRIORITY_INTERESTS}}, {{PREFERRED_CONTENT_STYLE}},
      {{WEAK_SIGNALS}}, {{DEFAULT_DOWNRANKS}}

    Supported placeholders (paper filter prompt):
      {{HIGHEST_PRIORITY}}, {{SECONDARY_PRIORITY}},
      {{PREFERRED_CONTENT_STYLE}}, {{DEFAULT_DOWNRANKS}}

    Supported placeholders (paper knowledge prompt):
      {{USER_FOCUS}}
    """
    taste = get_rss_taste_profile(interests)
    paper = get_paper_filter_profile(interests)
    focus = get_paper_knowledge_focus(interests)

    replacements = {
        "HIGH_PRIORITY_INTERESTS": _bullet_list(taste.get("high_priority", [])),
        "PREFERRED_CONTENT_STYLE": _bullet_list(
            taste.get("preferred_style", []) or paper.get("preferred_style", [])
        ),
        "WEAK_SIGNALS": _bullet_list(taste.get("weak_signals", [])),
        "DEFAULT_DOWNRANKS": _bullet_list(
            taste.get("default_downranks", []) or paper.get("default_downranks", [])
        ),
        "HIGHEST_PRIORITY": _bullet_list(paper.get("highest_priority", [])),
        "SECONDARY_PRIORITY": _bullet_list(paper.get("secondary", [])),
        "USER_FOCUS": _bullet_list(focus),
    }

    result = template
    for key, value in replacements.items():
        result = result.replace("{{" + key + "}}", value)
    return result


def _bullet_list(items: list[str]) -> str:
    if not items:
        return "- (none configured)"
    return "\n".join(f"- {item}" for item in items)


def _rules_from_list(items: list[dict[str, Any]]) -> list[tuple[str, int, tuple[str, ...]]]:
    rules: list[tuple[str, int, tuple[str, ...]]] = []
    for item in items:
        label = str(item.get("label", ""))
        weight = int(item.get("weight", 0))
        keywords = tuple(str(k) for k in item.get("keywords", []))
        if label and keywords:
            rules.append((label, weight, keywords))
    return rules
