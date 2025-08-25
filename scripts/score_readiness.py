#!/usr/bin/env python3
import sys, json, pathlib, argparse

def completeness_ok(d: dict) -> bool:
    required = ["cover","layers","warranty","retail","sme"]
    return all(k in d for k in required) and isinstance(d.get("layers",[]), list) and len(d.get("layers",[]))>0

def evidence_okay(d: dict) -> bool:
    ev = d.get("evidence", [])
    if not ev: return False
    for e in ev:
        if e.get("confidence") not in ("High","Medium"): return False
        if not e.get("url"): return False
    return True

def has_temporal_snapshot(d: dict) -> bool:
    snap = (d.get("retail") or {}).get("pricing_snapshot")
    return bool(snap and snap.get("captured_at"))

def score_doc(d: dict) -> float:
    schema = 1.0  # assume validate_json ran first
    evidence = 1.0 if evidence_okay(d) else 0.0
    complete = 1.0 if completeness_ok(d) else 0.0
    risk_penalty = 0.05 if not has_temporal_snapshot(d) else 0.0
    score = 0.35*schema + 0.40*evidence + 0.20*complete - risk_penalty
    return round(max(0.0, score)*100.0, 1)

def main():
    ap = argparse.ArgumentParser(description="Compute readiness scores")
    ap.add_argument("spec_dir")
    ap.add_argument("--min-score", type=float, default=85.0)
    args = ap.parse_args()

    ok = True
    for p in pathlib.Path(args.spec_dir).rglob("*.json"):
        d = json.loads(pathlib.Path(p).read_text())
        s = score_doc(d)
        if s < args.min_score:
            print(f"[SCORE] {p}: {s} < {args.min_score}")
            ok = False
    print("OK" if ok else "FAIL")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
