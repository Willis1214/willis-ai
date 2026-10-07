#!/usr/bin/env python3
"""Validate candidate claims against evidence, coverage, counterexamples, and feedback."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from _dki_common import read_csv, read_jsonl, write_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build universality_matrix.csv.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--search-results")
    parser.add_argument("--counterexamples")
    parser.add_argument("--blind-validation")
    parser.add_argument("--feedback", required=True)
    parser.add_argument("--regression", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--iteration", type=int, default=1)
    parser.add_argument(
        "--min-iterations",
        type=int,
        default=1,
        help="Configured minimum iteration guard. This is not a quality proof; dynamic gates still decide promotion.",
    )
    parser.add_argument(
        "--min-domain-core-support-files",
        type=int,
        default=2,
        help="Default guard for domain-core promotion; tune per domain profile.",
    )
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when blocked promotions exist.")
    return parser.parse_args()


def as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def normalize_text(value) -> str:
    return str(value or "").strip().lower().replace("_", " ")


def classify_lane(claim, input_status: str, blocked: bool) -> str:
    target_lane = normalize_text(claim.get("target_lane") or claim.get("promotion_target"))
    scope = normalize_text(claim.get("scope"))
    if target_lane:
        return target_lane.replace(" ", "_")
    if input_status == "validated_general" and scope in {"domain core", "domain"}:
        return "domain_core" if not blocked else "candidate"
    if "subtype" in scope:
        return "subtype_overlay"
    if "project" in scope:
        return "project_overlay"
    if "local" in scope:
        return "local_exception"
    if input_status == "special_case":
        return "special_case"
    if input_status == "contextual":
        return "contextual_rule"
    if input_status == "validated_general":
        return "validated_general" if not blocked else "candidate"
    return input_status


def main() -> int:
    args = parse_args()
    manifest = [row for row in read_jsonl(args.manifest, missing_ok=False) if not row.get("excluded")]
    claims = read_jsonl(args.claims, missing_ok=False)
    evidence = read_jsonl(args.evidence)
    feedback = read_jsonl(args.feedback)
    regression = read_jsonl(args.regression)
    search = read_jsonl(args.search_results) if args.search_results else []
    blind = {row["claim_id"]: row for row in read_jsonl(args.blind_validation)} if args.blind_validation else {}

    evidence_by_id = {row.get("evidence_id"): row for row in evidence}
    counter_by_claim = defaultdict(set)
    support_by_claim = defaultdict(set)
    needs_deep_by_claim = defaultdict(set)
    for row in search:
        if row.get("search_status") == "counterexample_hint":
            counter_by_claim[row["claim_id"]].add(row["file_id"])
        elif row.get("search_status") == "support_hint":
            support_by_claim[row["claim_id"]].add(row["file_id"])
        elif row.get("search_status") == "needs_deep_read":
            needs_deep_by_claim[row["claim_id"]].add(row["file_id"])

    feedback_claims = defaultdict(list)
    feedback_decisions = defaultdict(set)
    for row in feedback:
        for claim_id in row.get("claim_ids", []):
            feedback_claims[claim_id].append(row.get("case_id"))
            if row.get("decision"):
                feedback_decisions[claim_id].add(row.get("decision"))

    regression_claims = defaultdict(list)
    for row in regression:
        for claim_id in row.get("claim_ids", []):
            regression_claims[claim_id].append(row.get("regression_id"))

    all_file_ids = {row["file_id"] for row in manifest}
    rows = []
    blocked = 0
    for claim in claims:
        claim_id = claim["claim_id"]
        input_status = claim.get("status", "hypothesis")
        source_classes = set(as_list(claim.get("source_class") or claim.get("source_classes")))
        scope = normalize_text(claim.get("scope"))
        target_lane = normalize_text(claim.get("target_lane") or claim.get("promotion_target"))
        coverage_denominator = claim.get("coverage_denominator")
        applies_when = as_list(claim.get("applies_when"))
        does_not_apply_when = as_list(claim.get("does_not_apply_when"))
        promoting_general = input_status == "validated_general" or target_lane in {"domain core", "domain_core", "validated general", "validated_general"}
        promoting_domain_core = target_lane in {"domain core", "domain_core"} or (
            input_status == "validated_general" and scope in {"domain core", "domain"}
        )
        support_files = set(claim.get("supporting_files") or []) | support_by_claim.get(claim_id, set())
        contradicting_files = set(claim.get("contradicting_files") or []) | counter_by_claim.get(claim_id, set())
        evidence_ids = claim.get("source_evidence") or []
        missing_evidence = [eid for eid in evidence_ids if eid not in evidence_by_id]
        untested = sorted(all_file_ids - support_files - contradicting_files)
        blockers = []
        if not support_files and not evidence_ids and input_status != "rejected":
            blockers.append("no_supporting_evidence")
        if missing_evidence:
            blockers.append("missing_evidence_records")
        if contradicting_files:
            blockers.append("unresolved_counterexamples")
        if input_status == "validated_general" and args.iteration < args.min_iterations:
            blockers.append("min_iteration_not_met")
        if promoting_general and source_classes and source_classes <= {"public_prior", "unresolved_hypothesis", "rejected_assumption"}:
            blockers.append("source_class_not_promotable_for_general")
        if promoting_general and not coverage_denominator:
            blockers.append("missing_coverage_denominator")
        if promoting_general and not applies_when:
            blockers.append("missing_applies_when")
        if promoting_general and not does_not_apply_when:
            blockers.append("missing_does_not_apply_when")
        if promoting_domain_core and len(support_files) < args.min_domain_core_support_files:
            blockers.append("domain_core_support_below_threshold")
        if input_status == "validated_general" and needs_deep_by_claim.get(claim_id):
            blockers.append("relevant_files_need_deep_read")
        if input_status == "validated_general" and untested:
            blockers.append("untested_files_remain")
        if input_status == "validated_general" and regression_claims.get(claim_id):
            limiting_feedback = feedback_decisions.get(claim_id, set()) & {"scope_contextual", "mark_special_case", "reject"}
            if limiting_feedback:
                blockers.append("feedback_regression_blocks_generalization")
        blind_verdict = (blind.get(claim_id) or {}).get("blind_verdict")
        if input_status == "validated_general" and blind_verdict in {"unsupported", "contradicted", "scope_needed", "insufficient_evidence"}:
            blockers.append(f"blind_validation_{blind_verdict}")
        if input_status == "special_case" and not claim.get("scope"):
            blockers.append("special_case_missing_scope")
        if input_status in {"rejected", "contextual", "special_case"} and feedback_claims.get(claim_id) and not regression_claims.get(claim_id):
            blockers.append("feedback_missing_regression")

        score = (
            min(len(support_files), 5)
            + min(max(len(all_file_ids) - len(untested), 0), 5)
            + (2 if not contradicting_files else -4)
            + (1 if claim.get("scope") else 0)
            + min(len(regression_claims.get(claim_id, [])), 2)
            - min(len(needs_deep_by_claim.get(claim_id, [])), 3)
        )
        if blockers:
            validation_status = "blocked"
            blocked += 1
        else:
            validation_status = "pass"
        promotion_lane = classify_lane(claim, input_status, bool(blockers))

        if input_status == "rejected" and not blockers:
            recommended = "rejected"
        elif "unresolved_counterexamples" in blockers:
            recommended = "contradicted_or_contextual"
        elif "no_supporting_evidence" in blockers or "missing_evidence_records" in blockers:
            recommended = "hypothesis"
        elif "source_class_not_promotable_for_general" in blockers:
            recommended = "candidate"
        elif "domain_core_support_below_threshold" in blockers:
            recommended = "subtype_or_project_overlay"
        elif input_status == "validated_general" and not blockers:
            recommended = "validated_general"
        elif claim.get("scope"):
            recommended = "contextual"
        else:
            recommended = "candidate"

        rows.append(
            {
                "claim_id": claim_id,
                "input_status": input_status,
                "validation_status": validation_status,
                "recommended_status": recommended,
                "promotion_lane": promotion_lane,
                "source_class": json.dumps(sorted(source_classes)),
                "scope": claim.get("scope") or "",
                "coverage_denominator": coverage_denominator or "",
                "support_files": json.dumps(sorted(support_files)),
                "contradicting_files": json.dumps(sorted(contradicting_files)),
                "untested_files": json.dumps(untested),
                "feedback_cases": json.dumps(feedback_claims.get(claim_id, [])),
                "regression_cases": json.dumps(regression_claims.get(claim_id, [])),
                "universality_score": score,
                "blockers": json.dumps(blockers),
            }
        )

    write_csv(
        args.out,
        [
            "claim_id",
            "input_status",
            "validation_status",
            "recommended_status",
            "promotion_lane",
            "source_class",
            "scope",
            "coverage_denominator",
            "support_files",
            "contradicting_files",
            "untested_files",
            "feedback_cases",
            "regression_cases",
            "universality_score",
            "blockers",
        ],
        rows,
    )
    if args.strict and blocked:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
