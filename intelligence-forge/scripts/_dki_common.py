#!/usr/bin/env python3
"""Shared helpers for Intelligence Forge scripts."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Sequence


TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]{2,}")
STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "then",
    "else",
    "when",
    "where",
    "into",
    "true",
    "false",
    "file",
    "rule",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_parent(path: str | os.PathLike[str]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_jsonl(path: str | os.PathLike[str], missing_ok: bool = True) -> List[Dict]:
    p = Path(path)
    if missing_ok and not p.exists():
        return []
    rows: List[Dict] = []
    with p.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: str | os.PathLike[str], rows: Iterable[Dict]) -> None:
    ensure_parent(path)
    with Path(path).open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def append_jsonl(path: str | os.PathLike[str], row: Dict) -> None:
    ensure_parent(path)
    with Path(path).open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: str | os.PathLike[str], fieldnames: Sequence[str], rows: Iterable[Dict]) -> None:
    ensure_parent(path)
    with Path(path).open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def read_csv(path: str | os.PathLike[str], missing_ok: bool = True) -> List[Dict]:
    p = Path(path)
    if missing_ok and not p.exists():
        return []
    with p.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def short_sha256_file(path: str | os.PathLike[str], max_bytes: int | None = None) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        if max_bytes is None:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                h.update(chunk)
        else:
            h.update(fh.read(max_bytes))
    return h.hexdigest()[:16]


def stable_id(prefix: str, text: str) -> str:
    return f"{prefix}-{hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]}"


def tokenize(text: str) -> List[str]:
    return [tok.lower() for tok in TOKEN_RE.findall(text) if tok.lower() not in STOPWORDS]


def load_profile(path: str | os.PathLike[str] | None) -> Dict:
    """Parse the small YAML subset used by the draft profile contract."""
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    profile: Dict[str, object] = {}
    current_key: str | None = None
    with p.open("r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip()
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("- ") and current_key:
                profile.setdefault(current_key, [])
                value = stripped[2:].strip().strip("'\"")
                if isinstance(profile[current_key], list):
                    profile[current_key].append(value)
                continue
            if ":" in stripped and not stripped.startswith("- "):
                key, value = stripped.split(":", 1)
                key = key.strip()
                value = value.strip()
                current_key = key
                if value == "[]":
                    profile[key] = []
                elif value:
                    profile[key] = value.strip("'\"")
                else:
                    profile.setdefault(key, [])
    return profile


def size_bucket(size_bytes: int) -> str:
    if size_bytes < 10_000:
        return "small"
    if size_bytes < 100_000:
        return "medium"
    if size_bytes < 1_000_000:
        return "large"
    return "huge"


def first_path_segment(relpath: str) -> str:
    parts = Path(relpath).parts
    return parts[0] if parts else "."
