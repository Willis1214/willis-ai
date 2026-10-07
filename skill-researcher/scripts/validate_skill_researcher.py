#!/usr/bin/env python3
"""Validate the local Skill Researcher installation."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SKILL_PHRASES = [
    "Pre-creation research gate",
    "explicit user confirmation",
    "skills.sh",
    "GitHub",
    "skill-creator",
    "Do not run `npx skills add`",
    "<skill-research-gate>",
]

REQUIRED_METHOD_PHRASES = [
    "Candidate Scoring",
    "Research Brief Rules",
    "QC Checklist",
    "npx skills find",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def require_file(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    skill_dir = Path(sys.argv[1]).expanduser().resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill_md = require_file(skill_dir / "SKILL.md")
    method_md = require_file(skill_dir / "references" / "skill_research_methodology.md")
    openai_yaml = require_file(skill_dir / "agents" / "openai.yaml")

    if not skill_md.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = skill_md.split("---", 2)[1]
    if "name: skill-researcher" not in frontmatter:
        fail("frontmatter name must be skill-researcher")
    if "description:" not in frontmatter:
        fail("frontmatter description missing")
    frontmatter_keys = re.findall(r"^([a-zA-Z0-9_-]+):", frontmatter, flags=re.MULTILINE)
    if sorted(frontmatter_keys) != ["description", "name"]:
        fail(f"frontmatter must contain only name and description, got {frontmatter_keys}")

    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in skill_md:
            fail(f"SKILL.md missing required phrase: {phrase}")

    for phrase in REQUIRED_METHOD_PHRASES:
        if phrase not in method_md:
            fail(f"methodology reference missing required phrase: {phrase}")

    if "display_name: \"Skill Researcher\"" not in openai_yaml:
        fail("agents/openai.yaml display_name mismatch")
    if "$skill-researcher" not in openai_yaml:
        fail("agents/openai.yaml default_prompt must mention $skill-researcher")

    print("[OK] Skill Researcher structure and gate wording validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
