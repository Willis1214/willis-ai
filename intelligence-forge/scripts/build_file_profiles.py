#!/usr/bin/env python3
"""Build shallow file profiles for all manifest entries."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

from _dki_common import read_jsonl, tokenize, write_csv, write_jsonl

INCLUDE_RE = re.compile(r"\b(include|import|source|load)\b\s+([A-Za-z0-9_./:-]+)", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build shallow file_profiles.jsonl and strata_candidates.csv.")
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profile")
    parser.add_argument("--out", required=True)
    parser.add_argument("--strata-out", required=True)
    parser.add_argument("--max-bytes", type=int, default=1_000_000)
    return parser.parse_args()


def read_sample(path: str, max_bytes: int) -> str:
    data = Path(path).read_bytes()[:max_bytes]
    return data.decode("utf-8", errors="replace")


def section_markers(lines):
    markers = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or stripped.startswith("[") or stripped.lower().startswith(("section", "begin", "end")):
            markers.append(stripped[:120])
        if len(markers) >= 20:
            break
    return markers


def main() -> int:
    args = parse_args()
    manifest = read_jsonl(args.manifest, missing_ok=False)
    profiles = []
    strata_rows = []
    for row in manifest:
        if row.get("excluded"):
            profiles.append(
                {
                    "file_id": row["file_id"],
                    "profile_state": "excluded_with_reason",
                    "excluded": True,
                    "top_keywords": [],
                    "section_markers": [],
                    "include_refs": [],
                    "structural_tokens": [],
                    "rare_tokens": [],
                    "deep_read_recommended": False,
                    "recommendation_reason": row.get("exclude_reason"),
                }
            )
            continue
        text = read_sample(row["path"], args.max_bytes)
        lines = text.splitlines()
        tokens = tokenize(text)
        counts = Counter(tokens)
        top_keywords = [token for token, _ in counts.most_common(20)]
        rare_tokens = sorted([token for token, count in counts.items() if count == 1 and len(token) >= 6])[:20]
        include_refs = [match.group(2) for match in INCLUDE_RE.finditer(text)][:20]
        structural = sorted(set(top_keywords[:10] + [row.get("ext") or "no_ext"] + include_refs[:5]))
        deep_read = bool(rare_tokens[:3] or include_refs)
        profiles.append(
            {
                "file_id": row["file_id"],
                "line_count_estimate": len(lines),
                "top_keywords": top_keywords,
                "section_markers": section_markers(lines),
                "include_refs": include_refs,
                "structural_tokens": structural,
                "rare_tokens": rare_tokens,
                "profile_state": "shallow_profiled",
                "excluded": False,
                "deep_read_recommended": deep_read,
                "recommendation_reason": "rare_or_linked_content" if deep_read else None,
            }
        )
        for token in structural[:8]:
            strata_rows.append(
                {
                    "file_id": row["file_id"],
                    "stratum_key": "structural_token",
                    "stratum_value": token,
                    "source": "shallow_profile",
                }
            )
        strata_rows.append(
            {
                "file_id": row["file_id"],
                "stratum_key": "extension",
                "stratum_value": row.get("ext") or "no_ext",
                "source": "manifest",
            }
        )
    write_jsonl(args.out, profiles)
    write_csv(args.strata_out, ["file_id", "stratum_key", "stratum_value", "source"], strata_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
