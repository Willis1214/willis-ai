#!/usr/bin/env python3
"""Initialize a reusable QC/UAT workspace under qc_uat/."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

DEFAULT_BASE_DIR = "qc_uat"
SUBDIRS = ["plan", "testcases", "engineer", "logs"]

CHECKLIST_TEMPLATE = """# QC/UAT Checklist

## Scope
- Target program:
- Language/runtime:
- Primary entrypoint:
- Expected input contract:
- Expected output contract:
- Current risk hypothesis:

## Command Matrix
| Command | Purpose | Expected Signal | Timeout |
| --- | --- | --- | --- |
| [fill] | [golden/boundary/regression] | [exit code/output/file/assertion] | [seconds] |

## Functional Scenarios
- [ ] Minimal valid input
- [ ] Typical valid input
- [ ] Larger valid input or batch input
- [ ] Output contract check
- [ ] Repeated execution determinism

## Boundary Cases
- [ ] Missing or empty input
- [ ] Wrong type or malformed record
- [ ] Invalid path or missing file
- [ ] Unicode path/content
- [ ] Oversized input within safe local limits

## Regression Probes
- [ ] Recently changed module or branch
- [ ] User-reported bug reproduction
- [ ] Prior failure payload retained

## Language-Specific Checks
- [ ] Python / Perl / Tcl / Shell runtime risks relevant to this target

## Gate Decision
- Blocker threshold:
- Final decision: [Pass / Fail / Reject]
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold QC/UAT artifact directories")
    parser.add_argument(
        "--root",
        default=".",
        help="Target project root path (default: current directory)",
    )
    parser.add_argument(
        "--base-dir",
        default=DEFAULT_BASE_DIR,
        help=f"QC artifact base dir relative to root (default: {DEFAULT_BASE_DIR})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite checklist template if it already exists",
    )
    return parser.parse_args()


def write_text_if_needed(path: Path, content: str, force: bool) -> str:
    existed = path.exists()
    if existed and not force:
        return "kept"
    path.write_text(content, encoding="utf-8")
    return "updated" if existed else "created"


def ensure_structure(root: Path, base_dir: str, force: bool) -> dict[str, str]:
    qc_root = root / base_dir
    qc_root.mkdir(parents=True, exist_ok=True)

    for subdir in SUBDIRS:
        (qc_root / subdir).mkdir(parents=True, exist_ok=True)

    checklist_path = qc_root / "plan" / "check_list.md"
    checklist_state = write_text_if_needed(checklist_path, CHECKLIST_TEMPLATE, force)

    report_path = qc_root / "qc_uat_result.md"
    manifest_path = qc_root / "logs" / "run_manifest.json"
    manifest = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "root": str(root),
        "qc_root": str(qc_root),
        "subdirs": SUBDIRS,
        "checklist": str(checklist_path),
        "default_report": str(report_path),
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    return {
        "qc_root": str(qc_root),
        "checklist": checklist_state,
        "manifest": str(manifest_path),
        "default_report": str(report_path),
    }


def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    result = ensure_structure(root, args.base_dir, args.force)

    print(f"[OK] QC/UAT root: {result['qc_root']}")
    print(f"[OK] Checklist status: {result['checklist']}")
    print(f"[OK] Manifest: {result['manifest']}")
    print(f"[OK] Default report: {result['default_report']}")


if __name__ == "__main__":
    main()
