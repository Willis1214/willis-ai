#!/usr/bin/env python3
"""Build a full corpus manifest."""

from __future__ import annotations

import argparse
import fnmatch
import os
from pathlib import Path

from _dki_common import load_profile, now_iso, short_sha256_file, size_bucket, stable_id, write_jsonl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build corpus_manifest.jsonl for a same-domain corpus.")
    parser.add_argument("--profile", help="Optional domain_profile.yaml.")
    parser.add_argument("--root", action="append", help="Corpus root. Can be repeated.")
    parser.add_argument("--allowed-extension", action="append", default=[], help="Allowed extension such as .txt.")
    parser.add_argument("--out", required=True, help="Output JSONL path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    profile = load_profile(args.profile)
    roots = args.root or profile.get("corpus_roots") or []
    if isinstance(roots, str):
        roots = [roots]
    allowed = set(args.allowed_extension or profile.get("allowed_extensions") or [])
    excludes = profile.get("exclude_patterns") or []
    if isinstance(excludes, str):
        excludes = [excludes]
    if not roots:
        raise SystemExit("No corpus root provided. Use --root or corpus_roots in profile.")

    rows = []
    for root in roots:
        root_path = Path(root).expanduser().resolve()
        if not root_path.exists():
            rows.append(
                {
                    "file_id": stable_id("F", str(root_path)),
                    "path": str(root_path),
                    "relpath": ".",
                    "root": str(root_path),
                    "size_bytes": 0,
                    "size_bucket": "missing",
                    "ext": "",
                    "mtime": None,
                    "sha256_16": None,
                    "state": "excluded_with_reason",
                    "excluded": True,
                    "exclude_reason": "root_missing",
                    "cluster_id": None,
                    "notes": [],
                    "created_at": now_iso(),
                }
            )
            continue
        for dirpath, dirnames, filenames in os.walk(root_path):
            dirnames[:] = sorted([d for d in dirnames if d not in {".git", "__pycache__"}])
            for filename in sorted(filenames):
                path = Path(dirpath) / filename
                relpath = str(path.relative_to(root_path))
                ext = path.suffix.lower()
                excluded = False
                reason = None
                if allowed and ext not in allowed:
                    excluded = True
                    reason = "extension_not_allowed"
                for pattern in excludes:
                    if fnmatch.fnmatch(relpath, pattern):
                        excluded = True
                        reason = f"excluded_by_pattern:{pattern}"
                        break
                stat = path.stat()
                rows.append(
                    {
                        "file_id": stable_id("F", f"{root_path}:{relpath}"),
                        "path": str(path.resolve()),
                        "relpath": relpath,
                        "root": str(root_path),
                        "size_bytes": stat.st_size,
                        "size_bucket": size_bucket(stat.st_size),
                        "ext": ext,
                        "mtime": now_iso() if stat.st_mtime else None,
                        "sha256_16": None if excluded else short_sha256_file(path),
                        "state": "excluded_with_reason" if excluded else "indexed",
                        "excluded": excluded,
                        "exclude_reason": reason,
                        "cluster_id": None,
                        "notes": [],
                        "created_at": now_iso(),
                    }
                )
    write_jsonl(args.out, rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
