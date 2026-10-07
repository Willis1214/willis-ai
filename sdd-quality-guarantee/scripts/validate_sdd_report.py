#!/usr/bin/env python3
"""Validate the Markdown-only SDD Quality Guarantee report contract."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED = {"spec.md", "acceptance.md", "diagram.md", "SDD.md"}


def require_text(path: Path, text: str, errors: list[str]) -> None:
    if text not in path.read_text(encoding="utf-8"):
        errors.append(f"{path.name}: missing {text!r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    errors: list[str] = []
    if not root.is_dir():
        errors.append(f"missing directory: {root}")
    else:
        names = {path.name for path in root.iterdir() if path.is_file()}
        errors.extend(f"missing file: {name}" for name in sorted(REQUIRED - names))
        errors.extend(f"non-Markdown output: {path.name}" for path in root.rglob("*") if path.is_file() and path.suffix != ".md")
        if (root / "spec.md").exists():
            require_text(root / "spec.md", "SDD-REQ-", errors)
        if (root / "acceptance.md").exists():
            require_text(root / "acceptance.md", "SDD-ACC-", errors)
        if (root / "diagram.md").exists():
            require_text(root / "diagram.md", "```mermaid", errors)
        if (root / "SDD.md").exists():
            for token in ("Requirement-to-Evidence Traceability", "Pass", "Fail", "Reject"):
                require_text(root / "SDD.md", token, errors)
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print(f"[PASS] SDD Markdown report contract: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
