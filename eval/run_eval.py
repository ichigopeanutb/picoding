"""Validate AutoImprove evaluation case definitions.

This first evaluator intentionally avoids external APIs, network access, and API
keys. It checks whether cases are structurally complete enough to support later
human-reviewed and automated evaluation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "id",
    "category",
    "input",
    "expected_format",
    "required_sections",
    "must_include_keywords",
]


def load_cases(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("cases.json must contain a list of case objects")
    return data


def validate_case(case: dict[str, Any], index: int) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in case:
            errors.append(f"case {index}: missing field {field}")

    for field in ["id", "category", "input", "expected_format"]:
        if field in case and not isinstance(case[field], str):
            errors.append(f"case {index}: {field} must be a string")
        elif field in case and not case[field].strip():
            errors.append(f"case {index}: {field} must not be empty")

    for field in ["required_sections", "must_include_keywords"]:
        if field in case and not isinstance(case[field], list):
            errors.append(f"case {index}: {field} must be a list")
        elif field in case:
            values = case[field]
            if not values:
                errors.append(f"case {index}: {field} must not be empty")
            for value in values:
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"case {index}: {field} entries must be non-empty strings")

    return errors


def score_cases(cases: list[dict[str, Any]]) -> int:
    total_slots = len(cases) * len(REQUIRED_FIELDS)
    if total_slots == 0:
        return 0
    filled_slots = 0
    for case in cases:
        for field in REQUIRED_FIELDS:
            value = case.get(field)
            if isinstance(value, str) and value.strip():
                filled_slots += 1
            elif isinstance(value, list) and value:
                filled_slots += 1
    return round((filled_slots / total_slots) * 100)


def main() -> int:
    cases_path = Path("eval/cases.json")
    try:
        cases = load_cases(cases_path)
    except Exception as exc:
        print(f"EVAL_ERROR={exc}")
        return 1

    errors: list[str] = []
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"case {index}: must be an object")
            continue
        errors.extend(validate_case(case, index))

    print(f"EVAL_CASES_LOADED={len(cases)}")
    print(f"EVAL_SCORE={score_cases(cases)}")

    if errors:
        for error in errors:
            print(f"EVAL_SCHEMA_ERROR={error}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
