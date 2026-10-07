#!/usr/bin/env python3
"""Create a Markdown-only SDD Quality Guarantee output skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "spec.md": "# Spec\n\n## Task Identity\n\n## Background And Goal\n\n## Scope\n\n## Non-Goals\n\n## Inputs And Outputs\n\n## Requirements\n\n| ID | Requirement | Source | Priority | Acceptance Anchor | Status |\n| --- | --- | --- | --- | --- | --- |\n| SDD-REQ-001 | [fill] | [fill] | P0 | SDD-ACC-001 | Confirmed/TBD |\n\n## Constraints And Dependencies\n\n## Risks And TBD\n",
    "acceptance.md": "# Acceptance\n\n## Gate Status\n**Pass / Fail / Reject**\n\n## Acceptance Matrix\n\n| Acceptance ID | Spec ID | Expected Behavior | Evidence | Observed Result | Status |\n| --- | --- | --- | --- | --- | --- |\n| SDD-ACC-001 | SDD-REQ-001 | [fill] | [fill] | [fill] | Pass/Fail/Reject |\n\n## Workflow UAT\n\n## Side-Effect And Readback\n\n## Blockers\n\n## Verification Gaps\n",
    "diagram.md": "# Architecture And Traceability Diagram\n\n## Diagram Type\n\n## Mermaid\n\n```mermaid\nflowchart LR\n  Request[User Request] --> Spec[Confirmed Spec]\n  Spec --> Target[Target Deliverable]\n  Target --> Evidence[Evidence]\n  Evidence --> Acceptance[Final Acceptance]\n```\n\n## Legend\n\n## Scope Not Shown\n",
    "SDD.md": "# SDD Quality Guarantee\n\n## Review Summary\n\n## Task And Scope\n\n## Spec Summary\n\n## Architecture Summary\n\n## Acceptance Decision\n**Pass / Fail / Reject**\n\n## Evidence Index\n\n## Requirement-to-Evidence Traceability\n| Spec ID | Acceptance ID | TDD Case IDs | Evidence | Result |\n| --- | --- | --- | --- | --- |\n| SDD-REQ-001 | SDD-ACC-001 | TDD-CASE-001 | EVID-001 | Pass/Fail/Reject |\n\n## Risks, Gaps And TBD\n\n## Reviewer Checklist\n\n## Linked Markdown Artifacts\n",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    root = Path(args.output_dir).expanduser().resolve() / "SDD"
    root.mkdir(parents=True, exist_ok=True)
    for name, content in FILES.items():
        path = root / name
        existed = path.exists()
        if not existed:
            path.write_text(content, encoding="utf-8")
        print(f"[OK] {path} ({'kept' if existed else 'created'})")


if __name__ == "__main__":
    main()
