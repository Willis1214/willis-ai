#!/usr/bin/env python3
"""Extract simple evidence-backed candidate claims from shallow corpus files.

This draft extractor is intentionally conservative. It produces observations,
evidence records, and candidate claims, but it does not validate generality.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from _dki_common import read_jsonl, stable_id, tokenize, write_jsonl


PATTERNS = {
    "export_report": {
        "terms": {"export_report", "report_summary"},
        "claim_id": "C-auto-export-report-workflow",
        "claim_text": "Observed workflows may end by exporting a report.",
        "claim_type": "workflow",
        "scope": "files with export_report or report_summary evidence",
        "status": "candidate",
        "support_terms": ["export_report", "report_summary"],
        "counterexample_terms": [],
    },
    "common_layers_required": {
        "terms": {"common_layers_required", "common_layers"},
        "claim_id": "C-auto-common-layers-required",
        "claim_text": "Standard-flow files may require common_layers before checks run.",
        "claim_type": "invariant",
        "scope": "standard flow candidates; must exclude independent_mode and explicit no_common_layers cases",
        "status": "candidate",
        "support_terms": ["common_layers_required", "common_layers"],
        "counterexample_terms": ["no_common_layers", "independent_mode"],
    },
    "legacy_shortcut": {
        "terms": {"legacy_shortcut", "compact_mode", "waiver_mode"},
        "claim_id": "C-auto-legacy-shortcut-special",
        "claim_text": "Legacy compact-mode files may use a shortcut path and waiver mode.",
        "claim_type": "exception",
        "scope": "legacy compact_mode only",
        "status": "special_case",
        "support_terms": ["legacy_shortcut", "compact_mode", "waiver_mode"],
        "counterexample_terms": [],
    },
    "density_check": {
        "terms": {"density"},
        "claim_id": "C-auto-density-contextual",
        "claim_text": "Some files include density checks.",
        "claim_type": "workflow",
        "scope": "files with explicit density evidence",
        "status": "candidate",
        "support_terms": ["density"],
        "counterexample_terms": [],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract observations, candidate claims, and evidence records.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--out-observations", required=True)
    parser.add_argument("--out-claims", required=True)
    parser.add_argument("--out-evidence", required=True)
    parser.add_argument("--max-bytes", type=int, default=1_000_000)
    parser.add_argument("--include-excerpts", action="store_true", help="Include short raw excerpts in evidence records.")
    return parser.parse_args()


def read_text(path: str, max_bytes: int) -> str:
    return Path(path).read_bytes()[:max_bytes].decode("utf-8", errors="replace")


def line_hits(text: str, terms: Iterable[str]) -> List[Tuple[int, str, List[str]]]:
    hits: List[Tuple[int, str, List[str]]] = []
    wanted = {term.lower() for term in terms}
    for line_no, line in enumerate(text.splitlines(), start=1):
        tokens = set(tokenize(line))
        matched = sorted(tokens & wanted)
        if matched:
            hits.append((line_no, line.strip()[:240], matched))
    return hits


def main() -> int:
    args = parse_args()
    manifest = [row for row in read_jsonl(args.manifest, missing_ok=False) if not row.get("excluded")]
    profiles = {row["file_id"]: row for row in read_jsonl(args.profiles, missing_ok=False)}

    observations: List[Dict] = []
    evidence: List[Dict] = []
    claim_support = defaultdict(set)
    claim_evidence = defaultdict(list)
    claim_matched_terms = defaultdict(set)

    for row in manifest:
        file_id = row["file_id"]
        text = read_text(row["path"], args.max_bytes)
        for pattern_name, pattern in PATTERNS.items():
            hits = line_hits(text, pattern["terms"])
            if not hits:
                continue
            observation_id = stable_id("O", f"{file_id}:{pattern_name}")
            observations.append(
                {
                    "observation_id": observation_id,
                    "file_id": file_id,
                    "pattern": pattern_name,
                    "matched_terms": sorted({term for _, _, matched in hits for term in matched}),
                    "profile_state": profiles.get(file_id, {}).get("profile_state"),
                }
            )
            for line_no, line_text, matched in hits[:5]:
                evidence_id = stable_id("E", f"{file_id}:{pattern_name}:{line_no}:{line_text}")
                record = {
                    "evidence_id": evidence_id,
                    "file_id": file_id,
                    "pointer": f"line:{line_no}",
                    "summary": f"matched {', '.join(matched)} in pattern {pattern_name}",
                }
                if args.include_excerpts:
                    record["excerpt"] = line_text
                evidence.append(record)
                claim_evidence[pattern["claim_id"]].append(evidence_id)
                claim_matched_terms[pattern["claim_id"]].update(matched)
            claim_support[pattern["claim_id"]].add(file_id)

    claims: List[Dict] = []
    for pattern in PATTERNS.values():
        claim_id = pattern["claim_id"]
        support_files = sorted(claim_support.get(claim_id, set()))
        if not support_files:
            continue
        claims.append(
            {
                "claim_id": claim_id,
                "claim_text": pattern["claim_text"],
                "claim_type": pattern["claim_type"],
                "scope": pattern["scope"],
                "source_evidence": claim_evidence.get(claim_id, []),
                "supporting_files": support_files,
                "contradicting_files": [],
                "support_terms": pattern["support_terms"],
                "counterexample_terms": pattern["counterexample_terms"],
                "matched_terms": sorted(claim_matched_terms.get(claim_id, set())),
                "confidence": 0.5,
                "status": pattern["status"],
            }
        )

    write_jsonl(args.out_observations, observations)
    write_jsonl(args.out_claims, claims)
    write_jsonl(args.out_evidence, evidence)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
