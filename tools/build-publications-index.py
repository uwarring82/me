#!/usr/bin/env python3
"""Aggregator for publications/data/publications.json.

Contract (see site-blueprint v0.2.1 §6):
- Reads every publications/papers/*/rights.json.
- Extracts index-relevant fields and writes publications/data/publications.json.
- Exits non-zero on schema failure or unresolved licence:"unverified"
  without discriminant_action.
- Idempotent: sorted keys, entries ordered by date_published desc then slug.
- Stdlib only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCHEMA_VERSION = "0.2"
ALLOWED_TIERS = {"A", "B", "C"}
ALLOWED_DISPLAY_STATUS = {"planned", "live", "audit-hold"}
ALLOWED_NOTICE_TEMPLATES = {
    "summary-only",
    "cc-by-4.0-standard",
    "aps-accepted-manuscript",
    "springer-nature-accepted-manuscript",
}
INDEX_FIELDS = (
    "slug", "doi", "title", "date_published",
    "journal", "tier", "display_status", "themes",
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = REPO_ROOT / "publications" / "papers"
OUTPUT = REPO_ROOT / "publications" / "data" / "publications.json"
WARNING = (
    "GENERATED ARTEFACT. Do not edit. "
    "Source: papers/*/rights.json. "
    "Regenerate with tools/build-publications-index.py."
)


class ValidationError(Exception):
    pass


def _require(d: dict, key: str, where: str) -> object:
    if key not in d:
        raise ValidationError(f"{where}: missing required field '{key}'")
    return d[key]


def validate(slug: str, r: dict) -> None:
    where = f"papers/{slug}/rights.json"
    if _require(r, "schema_version", where) != SCHEMA_VERSION:
        raise ValidationError(f"{where}: schema_version must be {SCHEMA_VERSION!r}")
    for key in ("doi", "canonical_url", "date_published", "title", "journal", "themes"):
        _require(r, key, where)

    display = _require(r, "display", where)
    tier = _require(display, "tier", where + ".display")
    if tier not in ALLOWED_TIERS:
        raise ValidationError(f"{where}: display.tier must be one of {sorted(ALLOWED_TIERS)}")
    status = _require(display, "display_status", where + ".display")
    if status not in ALLOWED_DISPLAY_STATUS:
        raise ValidationError(f"{where}: display.display_status must be one of {sorted(ALLOWED_DISPLAY_STATUS)}")
    template = _require(display, "notice_template", where + ".display")
    if template not in ALLOWED_NOTICE_TEMPLATES:
        raise ValidationError(f"{where}: display.notice_template {template!r} not in attribution-templates.html registry")

    rights = _require(r, "rights", where)
    text_version = _require(rights, "text_version_allowed", where + ".rights")
    if text_version == "unverified" and not rights.get("discriminant_action"):
        raise ValidationError(f"{where}: rights.text_version_allowed is 'unverified' — discriminant_action required")

    for i, fig in enumerate(rights.get("figures") or []):
        figref = f"{where}.rights.figures[{i}]"
        for k in ("id", "source", "rights_holder", "licence", "can_host"):
            _require(fig, k, figref)
        if fig["licence"] == "unverified" and not fig.get("discriminant_action"):
            raise ValidationError(f"{figref}: licence is 'unverified' — discriminant_action required")

    _require(r, "audit", where)
    _require(r, "site_policy", where)


def build_entry(slug: str, r: dict) -> dict:
    return {
        "slug": slug,
        "doi": r["doi"],
        "title": r["title"],
        "date_published": r["date_published"],
        "journal": r["journal"],
        "tier": r["display"]["tier"],
        "display_status": r["display"]["display_status"],
        "themes": list(r.get("themes") or []),
    }


def main() -> int:
    if not PAPERS_DIR.exists():
        print(f"error: {PAPERS_DIR} does not exist", file=sys.stderr)
        return 2

    entries: list[dict] = []
    errors: list[str] = []
    for paper_dir in sorted(p for p in PAPERS_DIR.iterdir() if p.is_dir()):
        rights_path = paper_dir / "rights.json"
        if not rights_path.exists():
            errors.append(f"{paper_dir.name}: rights.json missing")
            continue
        try:
            r = json.loads(rights_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{paper_dir.name}: invalid JSON — {e}")
            continue
        try:
            validate(paper_dir.name, r)
        except ValidationError as e:
            errors.append(str(e))
            continue
        entries.append(build_entry(paper_dir.name, r))

    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        return 1

    entries.sort(key=lambda e: (e["date_published"], e["slug"]), reverse=True)

    payload = {
        "_warning": WARNING,
        "schema_version": SCHEMA_VERSION,
        "entries": entries,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False) + "\n"
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(REPO_ROOT)} ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
