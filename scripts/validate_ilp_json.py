#!/usr/bin/env python3
"""Validate ILP pack events and modeling-base seeds against local umbrella schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "schemas"


def load_schema_store() -> dict:
    store: dict = {}
    for path in SCHEMA_DIR.glob("*.json"):
        schema = json.loads(path.read_text(encoding="utf-8"))
        if "$id" in schema:
            store[schema["$id"]] = schema
        store[path.name] = schema
    return store


def validate_file(data_path: Path, schema_path: Path, store: dict) -> None:
    data_path = data_path.resolve()
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = json.loads(data_path.read_text(encoding="utf-8"))
    try:
        from jsonschema import Draft202012Validator
        from jsonschema import RefResolver

        resolver = RefResolver.from_schema(schema, store=store)
        Draft202012Validator(schema, resolver=resolver).validate(data)
        print(f"[schema] {data_path.relative_to(REPO_ROOT)}")
    except ImportError:
        print(f"[json] {data_path.relative_to(REPO_ROOT)}")


def validate_events_dir(events_dir: Path) -> int:
    events_dir = events_dir.resolve()
    store = load_schema_store()
    schema_path = SCHEMA_DIR / "cross-layer-event.json"
    errors = 0
    for event_path in sorted(events_dir.glob("*.json")):
        try:
            validate_file(event_path, schema_path, store)
        except Exception as exc:  # noqa: BLE001
            print(f"[FAIL] {event_path.name}: {exc}", file=sys.stderr)
            errors += 1
    return errors


def validate_modeling_seeds() -> int:
    store = load_schema_store()
    seeds = [
        (
            SCHEMA_DIR / "modeling-profile.json",
            REPO_ROOT
            / "docs"
            / "examples"
            / "modeling-base"
            / "profiles"
            / "eu-anticonsensus-settlements-2026.json",
        ),
        (
            SCHEMA_DIR / "modeling-run.json",
            REPO_ROOT
            / "docs"
            / "examples"
            / "modeling-base"
            / "runs"
            / "2026-09-scenario-a-uk-coalition.json",
        ),
    ]
    errors = 0
    for schema_path, data_path in seeds:
        try:
            validate_file(data_path, schema_path, store)
        except Exception as exc:  # noqa: BLE001
            print(f"[FAIL] {data_path.name}: {exc}", file=sys.stderr)
            errors += 1
    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_ilp_json.py events <dir> | seeds", file=sys.stderr)
        return 2

    mode = sys.argv[1]
    if mode == "events":
        if len(sys.argv) != 3:
            print("Usage: validate_ilp_json.py events <dir>", file=sys.stderr)
            return 2
        return validate_events_dir(Path(sys.argv[2]))
    if mode == "seeds":
        return validate_modeling_seeds()

    print(f"Unknown mode: {mode}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
