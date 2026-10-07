#!/usr/bin/env python3
"""Plan the next deep-read wave from manifest, profiles, and search results."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from _dki_common import first_path_segment, read_jsonl, write_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build deep_read_queue.csv and optional cluster_map.json.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profiles", required=True)
    parser.add_argument("--claims")
    parser.add_argument("--search-results")
    parser.add_argument("--out", required=True)
    parser.add_argument("--cluster-map-out")
    parser.add_argument("--max-files", type=int, default=20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = read_jsonl(args.manifest, missing_ok=False)
    profiles = {row["file_id"]: row for row in read_jsonl(args.profiles, missing_ok=False)}
    claims = read_jsonl(args.claims) if args.claims else []
    search = read_jsonl(args.search_results) if args.search_results else []

    supported_files = set()
    for claim in claims:
        supported_files.update(claim.get("supporting_files") or [])

    search_statuses = defaultdict(list)
    for row in search:
        search_statuses[row["file_id"]].append(row.get("search_status"))

    clusters = defaultdict(list)
    queue_rows = []
    for row in manifest:
        file_id = row["file_id"]
        profile = profiles.get(file_id, {})
        structural_tokens = profile.get("structural_tokens") or []
        cluster_key = "|".join(
            [
                row.get("ext") or "no_ext",
                first_path_segment(row.get("relpath") or "."),
                str(structural_tokens[0] if structural_tokens else "no_token"),
            ]
        )
        clusters[cluster_key].append(file_id)

        if row.get("excluded"):
            queue_rows.append(
                {
                    "priority_rank": "",
                    "file_id": file_id,
                    "relpath": row.get("relpath"),
                    "priority": 0,
                    "sampling_role": "excluded",
                    "state": "excluded_with_reason",
                    "reasons": row.get("exclude_reason") or "excluded",
                    "cluster_key": cluster_key,
                }
            )
            continue

        priority = 0
        reasons = []
        statuses = search_statuses.get(file_id, [])
        if "counterexample_hint" in statuses:
            priority += 50
            reasons.append("counterexample_hint")
        if "needs_deep_read" in statuses:
            priority += 20
            reasons.append("claim_search_needs_deep_read")
        if profile.get("deep_read_recommended"):
            priority += 15
            reasons.append(profile.get("recommendation_reason") or "profile_recommends_deep_read")
        if profile.get("rare_tokens"):
            priority += min(len(profile.get("rare_tokens") or []), 10)
            reasons.append("rare_tokens")
        if file_id not in supported_files:
            priority += 10
            reasons.append("coverage_gap_no_supporting_claim")
        if not reasons:
            reasons.append("low_priority_holdout")

        state = "queued" if priority > 0 else "holdout"
        if "counterexample_hint" in reasons:
            sampling_role = "counterexample"
        elif profile.get("rare_tokens"):
            sampling_role = "rare_subtype"
        elif file_id not in supported_files:
            sampling_role = "uncovered_stratum"
        elif profile.get("deep_read_recommended"):
            sampling_role = "representative"
        elif state == "holdout":
            sampling_role = "holdout"
        else:
            sampling_role = "representative"
        queue_rows.append(
            {
                "priority_rank": "",
                "file_id": file_id,
                "relpath": row.get("relpath"),
                "priority": priority,
                "sampling_role": sampling_role,
                "state": state,
                "reasons": ";".join(reasons),
                "cluster_key": cluster_key,
            }
        )

    sortable = [row for row in queue_rows if row["state"] == "queued"]
    sortable.sort(key=lambda item: (-int(item["priority"]), item["relpath"]))
    rank_by_file = {row["file_id"]: index + 1 for index, row in enumerate(sortable[: args.max_files])}
    for row in queue_rows:
        if row["file_id"] in rank_by_file:
            row["priority_rank"] = rank_by_file[row["file_id"]]
            row["state"] = "deep_read"
        elif row["state"] == "queued":
            row["state"] = "queued_later"

    write_csv(
        args.out,
        ["priority_rank", "file_id", "relpath", "priority", "sampling_role", "state", "reasons", "cluster_key"],
        sorted(queue_rows, key=lambda item: (str(item["state"]), str(item["priority_rank"]), item["relpath"] or "")),
    )

    if args.cluster_map_out:
        cluster_records = {
            key: {"cluster_id": f"CL-{index:04d}", "file_ids": sorted(file_ids)}
            for index, (key, file_ids) in enumerate(sorted(clusters.items()), start=1)
        }
        with open(args.cluster_map_out, "w", encoding="utf-8") as fh:
            json.dump(cluster_records, fh, ensure_ascii=False, indent=2, sort_keys=True)
            fh.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
