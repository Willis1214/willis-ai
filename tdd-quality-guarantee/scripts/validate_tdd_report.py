#!/usr/bin/env python3
"""Validate the Markdown-only TDD Quality Guarantee report contract."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED = {"spec_inventory.md", "test_cases.md", "test_results.md", "TDD.md"}


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
        if (root / "spec_inventory.md").exists():
            require_text(root / "spec_inventory.md", "SDD Requirements", errors)
        if (root / "test_cases.md").exists():
            for token in ("Acceptance", "Workflow", "Edge", "Regression", "Integration", "Side-effect", "TDD-CASE-"):
                require_text(root / "test_cases.md", token, errors)
        if (root / "test_results.md").exists():
            for token in ("Passed", "Failed", "Blocked", "Not Executed"):
                require_text(root / "test_results.md", token, errors)
        if (root / "TDD.md").exists():
            for token in ("Spec-to-Test-to-Evidence Traceability", "TDD-CASE-", "Complete", "Failed", "Incomplete"):
                require_text(root / "TDD.md", token, errors)
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print(f"[PASS] TDD Markdown report contract: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
