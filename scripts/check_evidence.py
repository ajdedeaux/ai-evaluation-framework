#!/usr/bin/env python3
import sys, json, pathlib, argparse, urllib.parse, yaml

def domain(u: str) -> str:
    d = urllib.parse.urlparse(u).netloc.lower()
    return d[4:] if d.startswith("www.") else d

def main():
    ap = argparse.ArgumentParser(description="Evidence coverage & confidence checks")
    ap.add_argument("spec_dir")
    ap.add_argument("registry_yaml")
    ap.add_argument("--min-high", type=int, default=1)
    ap.add_argument("--min-medium", type=int, default=2)
    args = ap.parse_args()

    reg = yaml.safe_load(pathlib.Path(args.registry_yaml).read_text())
    hi = set(reg.get("high_confidence", []))
    med = set(reg.get("medium_confidence", []))

    ok = True
    for p in pathlib.Path(args.spec_dir).rglob("*.json"):
        d = json.loads(p.read_text())
        ev = d.get("evidence", [])
        highs = sum(1 for e in ev if e.get("confidence")=="High" and domain(e.get("url","")) in hi)
        meds  = sum(1 for e in ev if e.get("confidence")=="Medium" and domain(e.get("url","")) in med)
        if highs < args.min_high or meds < args.min_medium:
            print(f"[EVIDENCE] {p}: need ≥{args.min_high} High & ≥{args.min_medium} Medium (has High={highs}, Medium={meds})")
            ok = False
    print("OK" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
