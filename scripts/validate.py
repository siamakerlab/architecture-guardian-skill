#!/usr/bin/env python3
"""Validate Architecture Guardian Skill package."""

from __future__ import annotations

import json
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def validate_skill_frontmatter() -> None:
    skill = ROOT / "SKILL.md"
    text = skill.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must be closed")

    frontmatter = text[4:end].strip().splitlines()
    keys: list[str] = []

    for line in frontmatter:
        if not line.strip() or line.startswith(" "):
            continue
        keys.append(line.split(":", 1)[0].strip())

    required = {"name", "description"}
    allowed = {"name", "description"}
    missing = required.difference(keys)
    extra = set(keys).difference(allowed)

    if missing:
        fail(f"SKILL.md frontmatter missing required keys: {sorted(missing)}")
    if extra:
        fail(f"SKILL.md frontmatter has unsupported keys: {sorted(extra)}")


def validate_ruleset() -> None:
    path = ROOT / "core/policy/ARCHITECTURE_GUARDIAN_RULESET.json"
    with path.open(encoding="utf-8") as f:
        ruleset = json.load(f)

    if not isinstance(ruleset.get("policy_version"), str):
        fail("ruleset policy_version must be a string")


def validate_banned_wording() -> None:
    banned = re.compile(r"CHANGE_REVIEW|FULL_AUDIT|compact|경량|concise mode")
    ignored = {".git", ".github", "VERSIONING.md", "scripts"}
    offenders: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue

        rel = path.relative_to(ROOT)
        if any(part in ignored for part in rel.parts):
            continue

        try:
            candidate = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        for index, line in enumerate(candidate.splitlines(), 1):
            if banned.search(line):
                offenders.append(f"{rel}:{index}: {line.strip()}")

    if offenders:
        fail("Banned or obsolete wording found:\n" + "\n".join(offenders))


def main() -> None:
    validate_skill_frontmatter()
    validate_ruleset()
    validate_banned_wording()
    print("Architecture Guardian Skill package is valid.")


if __name__ == "__main__":
    main()
