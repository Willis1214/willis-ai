#!/usr/bin/env python3
"""Append user feedback as supervised data and regression cases."""

from __future__ import annotations

import argparse
from pathlib import Path

from _dki_common import append_jsonl, now_iso, stable_id


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a feedback case and optional regression case.")
    parser.add_argument("--question-id", required=True)
    parser.add_argument("--answer-file", required=True)
    parser.add_argument("--claim-ids", required=True, help="Comma-separated claim ids.")
    parser.add_argument("--decision", default="answer_freeform")
    parser.add_argument("--casebook", required=True)
    parser.add_argument("--regression", required=True)
    parser.add_argument("--no-regression", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    answer = Path(args.answer_file).read_text(encoding="utf-8").strip()
    claim_ids = [item.strip() for item in args.claim_ids.split(",") if item.strip()]
    seed = f"{args.question_id}:{','.join(claim_ids)}:{answer}"
    case_id = stable_id("FB", seed)
    row = {
        "case_id": case_id,
        "question_id": args.question_id,
        "claim_ids": claim_ids,
        "answer_summary": answer[:500],
        "decision": args.decision,
        "created_at": now_iso(),
        "regression_required": not args.no_regression,
    }
    append_jsonl(args.casebook, row)
    if not args.no_regression:
        append_jsonl(
            args.regression,
            {
                "regression_id": stable_id("RG", case_id),
                "case_id": case_id,
                "claim_ids": claim_ids,
                "expected_decision": args.decision,
                "expected_behavior": "Do not promote a claim contrary to this feedback.",
                "created_at": now_iso(),
            },
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
