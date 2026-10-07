#!/usr/bin/env python3
"""Score corpus and claim coverage by manifest/profile strata."""

from __future__ import annotations

import argparse
from collections import defaultdict

from _dki_common import first_path_segment, read_jsonl, write_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build coverage_matrix.csv.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--claims", required=True)
    parser.add_argument("--out", required=True)
    return parser.parse_args()


def add_stratum(strata, file_id, key, value):
    strata[(key, str(value or "unknown"))].add(file_id)


def main() -> int:
    args = parse_args()
    manifest = read_jsonl(args.manifest, missing_ok=False)
    profiles = {row["file_id"]: row for row in read_jsonl(args.profiles, missing_ok=False)}
    claims = read_jsonl(args.claims)
    extracted_by_file = defaultdict(int)
    validated_by_file = defaultdict(int)
    for claim in claims:
        status = claim.get("status")
        support_files = claim.get("supporting_files") or []
        for file_id in support_files:
            extracted_by_file[file_id] += 1
            if status in {"validated_general", "contextual"}:
                validated_by_file[file_id] += 1

    strata = defaultdict(set)
    excluded = set()
    for row in manifest:
        file_id = row["file_id"]
        if row.get("excluded"):
            excluded.add(file_id)
        add_stratum(strata, file_id, "extension", row.get("ext") or "no_ext")
        add_stratum(strata, file_id, "size_bucket", row.get("size_bucket"))
        add_stratum(strata, file_id, "path_segment", first_path_segment(row.get("relpath") or "."))
        profile = profiles.get(file_id, {})
        add_stratum(strata, file_id, "profile_state", profile.get("profile_state") or row.get("state"))
        for token in (profile.get("structural_tokens") or [])[:8]:
            add_stratum(strata, file_id, "structural_token", token)

    rows = []
    for (key, value), file_ids in sorted(strata.items()):
        total = len(file_ids)
        extracted = len([f for f in file_ids if extracted_by_file.get(f)])
        validated = len([f for f in file_ids if validated_by_file.get(f)])
        excluded_count = len([f for f in file_ids if f in excluded])
        rows.append(
            {
                "stratum_key": key,
                "stratum_value": value,
                "total_files": total,
                "indexed_files": total - excluded_count,
                "extracted_files": extracted,
                "validated_files": validated,
                "covered_by_claims": extracted,
                "unknown_files": max(total - extracted - excluded_count, 0),
                "excluded_files": excluded_count,
            }
        )
    write_csv(
        args.out,
        [
            "stratum_key",
            "stratum_value",
            "total_files",
            "indexed_files",
            "extracted_files",
            "validated_files",
            "covered_by_claims",
            "unknown_files",
            "excluded_files",
        ],
        rows,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
