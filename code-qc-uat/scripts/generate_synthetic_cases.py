#!/usr/bin/env python3
"""Generate reusable seed cases for code QC/UAT."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate synthetic QC/UAT case files")
    parser.add_argument(
        "--output-dir",
        default="qc_uat/testcases",
        help="Directory for generated JSON files (default: qc_uat/testcases)",
    )
    return parser.parse_args()


def build_functional_cases() -> list[dict]:
    return [
        {
            "id": "golden-minimal",
            "category": "functional",
            "purpose": "minimal valid input should succeed",
            "payload": {"name": "alice", "status": "active", "qty": 1},
            "expected": {"should_succeed": True},
        },
        {
            "id": "golden-standard",
            "category": "functional",
            "purpose": "typical valid input should preserve expected fields",
            "payload": {"name": "bob", "status": "pending", "qty": 3, "price": 9.9},
            "expected": {"should_succeed": True},
        },
        {
            "id": "golden-unicode",
            "category": "functional",
            "purpose": "valid unicode content should be handled without corruption",
            "payload": {"name": "张三", "status": "active", "qty": 2},
            "expected": {"should_succeed": True},
        },
    ]


def build_boundary_cases() -> list[dict]:
    very_long = "A" * 10000
    deep_nested = {"lvl1": {"lvl2": {"lvl3": {"lvl4": {"lvl5": "value"}}}}}

    return [
        {
            "id": "empty-object",
            "category": "boundary",
            "purpose": "empty structured input should fail cleanly or produce documented default behavior",
            "payload": {},
            "expected": {"should_crash": False},
        },
        {
            "id": "missing-required-field",
            "category": "boundary",
            "purpose": "missing required field should be reported explicitly",
            "payload": {"status": "active"},
            "expected": {"should_crash": False},
        },
        {
            "id": "wrong-type",
            "category": "boundary",
            "purpose": "wrong primitive types should not silently corrupt output",
            "payload": {"price": "not_a_number", "qty": "10"},
            "expected": {"should_crash": False},
        },
        {
            "id": "invalid-enum",
            "category": "boundary",
            "purpose": "unexpected enum value should be rejected or preserved according to contract",
            "payload": {"status": "UNEXPECTED_STATUS"},
            "expected": {"should_crash": False},
        },
        {
            "id": "control-char",
            "category": "boundary",
            "purpose": "control characters should not break parsing or logging",
            "payload": {"note": "abc\u0000\u0001\u001fxyz"},
            "expected": {"should_crash": False},
        },
        {
            "id": "max-int",
            "category": "boundary",
            "purpose": "large integer should be handled explicitly",
            "payload": {"counter": 2**63 - 1},
            "expected": {"should_crash": False},
        },
        {
            "id": "very-long-string",
            "category": "boundary",
            "purpose": "large text input should not hang or truncate silently",
            "payload": {"content": very_long},
            "expected": {"should_crash": False},
        },
        {
            "id": "deep-nesting",
            "category": "boundary",
            "purpose": "nested structured input should not trigger recursion failure",
            "payload": deep_nested,
            "expected": {"should_crash": False},
        },
    ]


def build_dirty_cases() -> list[dict]:
    return [
        {
            "id": "path-traversal",
            "category": "dirty",
            "purpose": "path-like input should be normalized or rejected when unsafe",
            "payload": {"path": "../../../../etc/passwd"},
            "expected": {"should_crash": False, "should_escape_workspace": False},
        },
        {
            "id": "command-fragment",
            "category": "dirty",
            "purpose": "command-like text should not be executed when treated as data",
            "payload": {"filename": "report.txt; rm -rf /"},
            "expected": {"should_crash": False, "should_execute_payload": False},
        },
        {
            "id": "sql-fragment",
            "category": "dirty",
            "purpose": "SQL-like text should remain inert unless the program intentionally queries SQL",
            "payload": {"query": "' OR 1=1; --"},
            "expected": {"should_crash": False, "should_execute_payload": False},
        },
    ]


def build_regression_cases() -> list[dict]:
    return [
        {
            "id": "regression-placeholder",
            "category": "regression",
            "purpose": "replace with user-reported bug or recently changed branch",
            "payload": {"case": "fill with exact prior failing input"},
            "expected": {"should_succeed": "fill according to fixed behavior"},
        }
    ]


def write_json(path: Path, data: list[dict]) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "functional_cases.json": build_functional_cases(),
        "boundary_cases.json": build_boundary_cases(),
        "dirty_cases.json": build_dirty_cases(),
        "regression_cases.json": build_regression_cases(),
    }

    for name, cases in files.items():
        path = output_dir / name
        write_json(path, cases)
        print(f"[OK] {name}: {path} ({len(cases)})")


if __name__ == "__main__":
    main()
