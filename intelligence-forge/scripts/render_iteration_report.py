#!/usr/bin/env python3
"""Render a human-readable iteration report."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from _dki_common import read_csv, read_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render iteration_report.md.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--coverage", required=True)
    parser.add_argument("--universality", required=True)
    parser.add_argument("--questions", required=True)
    parser.add_argument("--feedback", required=True)
    parser.add_argument("--regression", required=True)
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = read_jsonl(args.manifest, missing_ok=False)
    profiles = read_jsonl(args.profiles, missing_ok=False)
    claims = read_jsonl(args.claims, missing_ok=False)
    coverage = read_csv(args.coverage, missing_ok=False)
    universality = read_csv(args.universality, missing_ok=False)
    questions = Path(args.questions).read_text(encoding="utf-8") if Path(args.questions).exists() else ""
    feedback = read_jsonl(args.feedback)
    regression = read_jsonl(args.regression)

    status_counts = Counter([row.get("status", "hypothesis") for row in claims])
    validation_counts = Counter([row.get("validation_status", "unknown") for row in universality])
    excluded = len([row for row in manifest if row.get("excluded")])
    profiled = len([row for row in profiles if row.get("profile_state") == "shallow_profiled"])
    blocked_rows = [row for row in universality if row.get("validation_status") == "blocked"]

    lines = [
        "# Domain Knowledge Iteration Report",
        "",
        "## Corpus Coverage",
        "",
        f"- manifest_files: {len(manifest)}",
        f"- excluded_files: {excluded}",
        f"- shallow_profiled_files: {profiled}",
        f"- coverage_rows: {len(coverage)}",
        "",
        "## Claim Status Counts",
        "",
    ]
    for key, value in sorted(status_counts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Validation Counts", ""])
    for key, value in sorted(validation_counts.items()):
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Blocked Claims", ""])
    if not blocked_rows:
        lines.append("- None")
    for row in blocked_rows:
        lines.append(f"- `{row['claim_id']}` -> {row.get('recommended_status')} blockers={row.get('blockers')}")
    lines.extend(["", "## Questions For User", ""])
    lines.append(questions.strip() if questions.strip() else "- None")
    lines.extend(["", "## Feedback And Regression", ""])
    lines.append(f"- feedback_cases: {len(feedback)}")
    lines.append(f"- regression_cases: {len(regression)}")
    lines.extend(["", "## Next Iteration Focus", ""])
    if blocked_rows:
        lines.append("- Resolve blocked claims through scope narrowing, counterexample inspection, or user confirmation.")
    else:
        lines.append("- Continue holdout validation and novelty checks before any promotion.")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
