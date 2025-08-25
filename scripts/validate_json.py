#!/usr/bin/env python3
import sys, json, pathlib, argparse
from jsonschema import Draft202012Validator

def validate_file(path, validator):
    data = json.loads(path.read_text())
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        for e in errors:
            loc = ".".join(map(str, e.path)) or "(root)"
            print(f"[SCHEMA] {path}: {loc} -> {e.message}")
        return False
    return True

def main():
    ap = argparse.ArgumentParser(description="Validate JSON files against a schema")
    ap.add_argument("spec_dir")
    ap.add_argument("schema_path")
    args = ap.parse_args()
    schema = json.loads(pathlib.Path(args.schema_path).read_text())
    validator = Draft202012Validator(schema)
    ok = True
    for p in pathlib.Path(args.spec_dir).rglob("*.json"):
        ok &= validate_file(p, validator)
    print("OK" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
