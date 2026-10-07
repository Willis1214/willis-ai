#!/usr/bin/env python3
"""Blind deterministic claim check using claims, evidence, manifest, profiles, and search results."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict

from _dki_common import read_jsonl, write_jsonl

GENERAL_RE = re.compile(r"\b(all|always|every|must|required|never)\b", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build blind_validation.jsonl without extractor rationale.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--search-results")
    parser.add_argument("--feedback")
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = [row for row in read_jsonl(args.manifest, missing_ok=False) if not row.get("excluded")]
    claims = read_jsonl(args.claims, missing_ok=False)
    evidence = read_jsonl(args.evidence)
    search = read_jsonl(args.search_results) if args.search_results else []
    feedback = read_jsonl(args.feedback) if args.feedback else []

    all_files = {row["file_id"] for row in manifest}
    evidence_ids = {row.get("evidence_id") for row in evidence}
    counter_by_claim = defaultdict(set)
    support_by_claim = defaultdict(set)
    for row in search:
        if row.get("search_status") == "counterexample_hint":
            counter_by_claim[row["claim_id"]].add(row["file_id"])
        if row.get("search_status") == "support_hint":
            support_by_claim[row["claim_id"]].add(row["file_id"])

    limiting_feedback = defaultdict(set)
    for row in feedback:
        if row.get("decision") in {"scope_contextual", "mark_special_case", "reject"}:
            for claim_id in row.get("claim_ids", []):
                limiting_feedback[claim_id].add(row.get("decision"))

    rows = []
    for claim in claims:
        claim_id = claim["claim_id"]
        support_files = set(claim.get("supporting_files") or []) | support_by_claim.get(claim_id, set())
        counter_files = set(claim.get("contradicting_files") or []) | counter_by_claim.get(claim_id, set())
        missing_evidence = [eid for eid in claim.get("source_evidence") or [] if eid not in evidence_ids]
        untested = sorted(all_files - support_files - counter_files)
        reasons = []
        verdict = "supported"

        if claim.get("status") == "rejected":
            verdict = "supported"
            reasons.append("claim_already_rejected")
        elif not support_files and not claim.get("source_evidence"):
            verdict = "unsupported"
            reasons.append("no_support_files_or_evidence")
        elif missing_evidence:
            verdict = "unsupported"
            reasons.append("missing_evidence_records")
        elif counter_files:
            verdict = "contradicted"
            reasons.append("counterexample_hint_present")
        elif claim.get("status") == "validated_general" and untested:
            verdict = "insufficient_evidence"
            reasons.append("relevant_files_untested")
        elif GENERAL_RE.search(claim.get("claim_text", "")) and untested and not claim.get("scope"):
            verdict = "scope_needed"
            reasons.append("general_language_without_full_file_support")
        elif limiting_feedback.get(claim_id) and claim.get("status") == "validated_general":
            verdict = "scope_needed"
            reasons.append("prior_feedback_limits_generalization")
        else:
            reasons.append("evidence_supports_current_scope")

        rows.append(
            {
                "claim_id": claim_id,
                "blind_verdict": verdict,
                "reasons": reasons,
                "support_files": sorted(support_files),
                "counter_files": sorted(counter_files),
                "untested_files": untested,
                "limiting_feedback": sorted(limiting_feedback.get(claim_id, set())),
            }
        )

    write_jsonl(args.out, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
