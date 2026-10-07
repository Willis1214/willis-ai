#!/usr/bin/env python3
"""Initialize and append entries to the long-term command memory markdown."""

from __future__ import annotations

import argparse
import hashlib
from datetime import datetime
from pathlib import Path
import sys


DEFAULT_MEMORY_PATH = Path.home() / ".codex" / "memories" / "long-term-commands.md"
ENTRY_TYPES = ("preference", "prohibition", "shortcut", "workflow")
SECTION_HEADERS = {entry_type: f"## {entry_type}" for entry_type in ENTRY_TYPES}
FILE_TEMPLATE = """# Long-Term Commands

This file stores approved long-term command rules for Codex.

- All entries apply across projects by default.
- Add entries only after explicit user approval.

## preference

## prohibition

## shortcut

## workflow
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize or append entries to the long-term command memory file."
    )
    parser.add_argument("--memory-path", default=str(DEFAULT_MEMORY_PATH))
    parser.add_argument("--init-only", action="store_true")
    parser.add_argument("--type", choices=ENTRY_TYPES)
    parser.add_argument("--source")
    parser.add_argument("--rule")
    parser.add_argument("--rationale")
    return parser.parse_args()


def ensure_template(memory_path: Path) -> None:
    memory_path.parent.mkdir(parents=True, exist_ok=True)
    if not memory_path.exists():
        memory_path.write_text(FILE_TEMPLATE, encoding="utf-8")


def require_fields(args: argparse.Namespace) -> None:
    missing = [
        name
        for name in ("type", "source", "rule", "rationale")
        if not getattr(args, name)
    ]
    if missing:
        raise SystemExit(f"Missing required arguments: {', '.join(missing)}")


def normalize_text(value: str) -> str:
    return " ".join(value.strip().split())


def build_entry_id(entry_type: str, rule: str) -> str:
    digest = hashlib.sha1(f"{entry_type}|{rule}".encode("utf-8")).hexdigest()[:10]
    return f"{entry_type}-{digest}"


def entry_exists(content: str, entry_type: str, rule: str) -> bool:
    normalized_rule = normalize_text(rule)
    rule_marker = f"- rule: {normalized_rule}"

    section = get_section_block(content, entry_type)
    if section is None:
        return False
    return rule_marker in section


def get_section_block(content: str, entry_type: str) -> str | None:
    header = SECTION_HEADERS[entry_type]
    start = content.find(header)
    if start == -1:
        return None

    next_positions = []
    for candidate_type, candidate_header in SECTION_HEADERS.items():
        if candidate_type == entry_type:
            continue
        position = content.find(candidate_header, start + len(header))
        if position != -1:
            next_positions.append(position)

    end = min(next_positions) if next_positions else len(content)
    return content[start:end]


def insert_entry(content: str, entry_type: str, entry: str) -> str:
    header = SECTION_HEADERS[entry_type]
    start = content.find(header)
    if start == -1:
        raise SystemExit(f"Section not found: {header}")

    insert_at = start + len(header)
    tail = content[insert_at:]
    return content[:insert_at] + "\n\n" + entry + tail


def build_entry(entry_type: str, source: str, rule: str, rationale: str) -> str:
    normalized_source = normalize_text(source)
    normalized_rule = normalize_text(rule)
    normalized_rationale = normalize_text(rationale)
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_id = build_entry_id(entry_type, normalized_rule)
    return (
        f"### {entry_id}\n"
        f"- created_at: {created_at}\n"
        f"- rule: {normalized_rule}\n"
        f"- rationale: {normalized_rationale}\n"
        f"- source: {normalized_source}\n"
    )


def main() -> int:
    args = parse_args()
    memory_path = Path(args.memory_path).expanduser()

    ensure_template(memory_path)
    if args.init_only:
        print(f"Initialized memory file: {memory_path}")
        return 0

    require_fields(args)
    content = memory_path.read_text(encoding="utf-8")

    if entry_exists(content, args.type, args.rule):
        print("Skipped duplicate entry.")
        return 0

    entry = build_entry(args.type, args.source, args.rule, args.rationale)
    updated = insert_entry(content, args.type, entry)
    memory_path.write_text(updated, encoding="utf-8")
    print(f"Appended entry: {build_entry_id(args.type, normalize_text(args.rule))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
