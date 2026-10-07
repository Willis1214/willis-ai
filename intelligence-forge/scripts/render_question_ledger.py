#!/usr/bin/env python3
"""Render high-value user questions from validation and blind-validation artifacts."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from _dki_common import read_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render question_ledger.md from blocked or uncertain claims.")
    parser.add_argument("--claims", required=True)
    parser.add_argument("--universality", required=True)
    parser.add_argument("--blind-validation")
    parser.add_argument("--feedback")
    parser.add_argument("--out", required=True)
    parser.add_argument("--max-questions", type=int, default=10)
    return parser.parse_args()


def read_universality(path: str):
    with open(path, "r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def blockers(row):
    raw = row.get("blockers") or "[]"
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return [raw]


def affected_fields_for(reason_type: str, row_blockers: list[str]) -> list[str]:
    fields = set()
    if reason_type in {"contradiction", "scope_boundary", "scope_needed"}:
        fields.update(["scope", "applies_when", "does_not_apply_when", "regression_cases"])
    if reason_type in {"promotion_gate", "source_boundary"}:
        fields.update(["status", "source_class", "coverage_denominator", "target_lane"])
    if reason_type in {"subtype_drift", "special_case"}:
        fields.update(["scope", "target_lane", "regression_cases"])
    if "missing_coverage_denominator" in row_blockers:
        fields.add("coverage_denominator")
    if "missing_applies_when" in row_blockers:
        fields.add("applies_when")
    if "missing_does_not_apply_when" in row_blockers:
        fields.add("does_not_apply_when")
    return sorted(fields) or ["status", "scope"]


def answer_capture_for(reason_type: str) -> str:
    if reason_type == "source_boundary":
        return "user_confirmed_rule|rejected_assumption"
    if reason_type in {"contradiction", "scope_boundary", "subtype_drift", "special_case", "scope_needed"}:
        return "scope_guard|user_confirmed_rule|rejected_assumption"
    if reason_type == "promotion_gate":
        return "scope_guard|open_question|cannot_infer"
    return "user_confirmed_rule|open_question"


def main() -> int:
    args = parse_args()
    claims = {row["claim_id"]: row for row in read_jsonl(args.claims, missing_ok=False)}
    universality = {row["claim_id"]: row for row in read_universality(args.universality)}
    blind = {row["claim_id"]: row for row in read_jsonl(args.blind_validation)} if args.blind_validation else {}
    feedback = read_jsonl(args.feedback) if args.feedback else []
    answered_claims = {claim_id for row in feedback for claim_id in row.get("claim_ids", [])}

    candidates = []
    for claim_id, row in universality.items():
        claim = claims.get(claim_id, {})
        row_blockers = blockers(row)
        blind_row = blind.get(claim_id, {})
        blind_verdict = blind_row.get("blind_verdict")
        reasons = []
        reason_type = None
        priority = 0

        if "feedback_regression_blocks_generalization" in row_blockers:
            reason_type = "regression_conflict"
            priority += 100
            reasons.append("Prior user feedback blocks generalization.")
        if "source_class_not_promotable_for_general" in row_blockers:
            reason_type = reason_type or "source_boundary"
            priority += 95
            reasons.append("Source class cannot support general promotion without file evidence or user confirmation.")
        if "domain_core_support_below_threshold" in row_blockers:
            reason_type = reason_type or "subtype_drift"
            priority += 90
            reasons.append("Domain-core promotion needs broader cross-strata support or overlay routing.")
        if "unresolved_counterexamples" in row_blockers or blind_verdict == "contradicted":
            reason_type = reason_type or "contradiction"
            priority += 80
            reasons.append("Counterexample evidence changes claim scope.")
        if "missing_coverage_denominator" in row_blockers:
            reason_type = reason_type or "promotion_gate"
            priority += 70
            reasons.append("Coverage denominator is missing for a promotable claim.")
        if "missing_applies_when" in row_blockers or "missing_does_not_apply_when" in row_blockers:
            reason_type = reason_type or "scope_boundary"
            priority += 60
            reasons.append("Reusable constraint needs explicit applies_when and does_not_apply_when.")
        if "min_iteration_not_met" in row_blockers:
            priority += 10
            reasons.append("Configured minimum iteration guard not met.")
        if blind_verdict in {"unsupported", "insufficient_evidence", "scope_needed"}:
            reason_type = reason_type or blind_verdict
            priority += 40
            reasons.append(f"Blind validation verdict: {blind_verdict}.")
        if claim.get("status") == "special_case" and claim_id not in answered_claims:
            reason_type = reason_type or "special_case"
            priority += 50
            reasons.append("Special-case preservation needs user decision.")

        if not reason_type:
            continue
        candidates.append((priority, claim_id, reason_type, reasons))

    candidates.sort(reverse=True)
    lines = ["# Question Ledger", ""]
    if not candidates:
        lines.extend(["No high-impact user questions for this iteration.", ""])
    for index, (priority, claim_id, reason_type, reasons) in enumerate(candidates[: args.max_questions], start=1):
        claim = claims.get(claim_id, {})
        lines.append(f"## Q-AUTO-{index:03d}: {claim_id}")
        lines.append("")
        lines.append(f"- reason: `{reason_type}`")
        lines.append(f"- priority: {priority}")
        lines.append(f"- claim: {claim.get('claim_text', '')}")
        lines.append(f"- current_status: `{claim.get('status', 'unknown')}`")
        if claim.get("scope"):
            lines.append(f"- current_scope: {claim.get('scope')}")
        lines.append(f"- affected_fields: `{', '.join(affected_fields_for(reason_type, row_blockers))}`")
        lines.append("- why ask:")
        for reason in reasons:
            lines.append(f"  - {reason}")
        lines.append("- options: `approve_general`, `scope_contextual`, `mark_special_case`, `project_overlay`, `subtype_overlay`, `cannot_infer`, `reject`, `answer_freeform`")
        lines.append(f"- answer_capture: `{answer_capture_for(reason_type)}`")
        lines.append("- blocking_promotion: true")
        lines.append("")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
