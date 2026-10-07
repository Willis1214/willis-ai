#!/usr/bin/env python3
"""Search shallow profiles for support and counterexample hints."""

from __future__ import annotations

import argparse
from collections import defaultdict

from _dki_common import read_jsonl, write_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build claim_search_results.jsonl and counterexample_ledger.md.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--counterexamples", required=True)
    return parser.parse_args()


def profile_terms(profile):
    terms = set(profile.get("top_keywords") or [])
    terms.update(profile.get("structural_tokens") or [])
    terms.update(profile.get("rare_tokens") or [])
    return {str(term).lower() for term in terms}


def main() -> int:
    args = parse_args()
    manifest = [row for row in read_jsonl(args.manifest, missing_ok=False) if not row.get("excluded")]
    profiles = {row["file_id"]: row for row in read_jsonl(args.profiles, missing_ok=False)}
    claims = read_jsonl(args.claims, missing_ok=False)
    rows = []
    ledger = ["# Counterexample Ledger", ""]
    counter_by_claim = defaultdict(list)

    for claim in claims:
        claim_id = claim["claim_id"]
        support_terms = {str(t).lower() for t in claim.get("support_terms", [])}
        counter_terms = {str(t).lower() for t in claim.get("counterexample_terms", [])}
        for file_row in manifest:
            file_id = file_row["file_id"]
            terms = profile_terms(profiles.get(file_id, {}))
            matched_counter = sorted(counter_terms & terms)
            matched_support = sorted(support_terms & terms)
            if matched_counter:
                status = "counterexample_hint"
                matched = matched_counter
                counter_by_claim[claim_id].append((file_id, matched))
            elif matched_support:
                status = "support_hint"
                matched = matched_support
            elif profiles.get(file_id, {}).get("deep_read_recommended"):
                status = "needs_deep_read"
                matched = []
            else:
                status = "not_relevant"
                matched = []
            rows.append(
                {
                    "claim_id": claim_id,
                    "file_id": file_id,
                    "search_status": status,
                    "matched_terms": matched,
                    "reason": "profile_term_match" if matched else "no_profile_match",
                    "evidence_id": None,
                }
            )

    for claim_id, hits in sorted(counter_by_claim.items()):
        ledger.append(f"## {claim_id}")
        for file_id, matched in hits:
            ledger.append(f"- file_id: `{file_id}`; matched_terms: `{', '.join(matched)}`")
        ledger.append("")

    write_jsonl(args.out, rows)
    with open(args.counterexamples, "w", encoding="utf-8") as fh:
        fh.write("\n".join(ledger) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
