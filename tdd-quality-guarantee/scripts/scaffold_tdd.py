#!/usr/bin/env python3
"""Create a Markdown-only TDD Quality Guarantee output skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "spec_inventory.md": "# Spec Inventory\n\n## Source Documents\n\n## SDD Requirements\n| Spec ID | Requirement | Workflow/Function | Acceptance Anchor | TDD Coverage |\n| --- | --- | --- | --- | --- |\n| SDD-REQ-001 | [fill] | [fill] | SDD-ACC-001 | TDD-CASE-001 |\n\n## Unclear Or Unmapped Requirements\n",
    "test_cases.md": "# Test Cases\n\n## Coverage Gate\n- Acceptance\n- Workflow\n- Edge\n- Regression\n- Integration\n- Side-effect\n\n## Case Matrix\n| Case ID | Type | Spec Anchor | Function/Workflow | Preconditions | Input | Action | Expected | Evidence Method | Priority |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| TDD-CASE-001 | Acceptance | SDD-REQ-001 | [fill] | [fill] | [fill] | [fill] | [fill] | [fill] | P0 |\n\n## Case Design Rationale\n\n## Waivers And Non-Applicable Cases\n",
    "test_results.md": "# Test Results\n\n## Execution Summary\n- Planned\n- Passed\n- Failed\n- Blocked\n- Not Executed\n\n## Result Matrix\n| Case ID | Spec Anchor | Expected | Observed | Evidence | Result | Failure/Gap |\n| --- | --- | --- | --- | --- | --- | --- |\n| TDD-CASE-001 | SDD-REQ-001 | [fill] | [fill] | EVID-001 | Passed/Failed/Blocked/Not Executed | [fill] |\n\n## Red-Green-Refactor Evidence\n\n## Failed And Blocked Cases\n\n## Unmapped Findings\n",
    "TDD.md": "# TDD Quality Guarantee\n\n## Review Summary\n\n## SDD Content Covered\n\n## Case Design Summary\n\n## Execution Result Summary\n\n## Spec-to-Test-to-Evidence Traceability\n| Spec ID | Case IDs | Expected | Observed | Evidence | Result |\n| --- | --- | --- | --- | --- | --- |\n| SDD-REQ-001 | TDD-CASE-001 | [fill] | [fill] | EVID-001 | Complete/Failed/Incomplete |\n\n## Positive/Negative/Edge/Regression/Integration Coverage\n\n## Coverage\n\n## Failures, Blockers And Unmapped Requirements\n\n## Final TDD Conclusion\n**Complete / Failed / Incomplete**\n\n## Reviewer Checklist\n\n## Linked Markdown Artifacts\n",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    root = Path(args.output_dir).expanduser().resolve() / "TDD"
    root.mkdir(parents=True, exist_ok=True)
    for name, content in FILES.items():
        path = root / name
        existed = path.exists()
        if not existed:
            path.write_text(content, encoding="utf-8")
        print(f"[OK] {path} ({'kept' if existed else 'created'})")


if __name__ == "__main__":
    main()
