#!/usr/bin/env python3
import argparse, json, re, pathlib
PATTERN = re.compile(r':contentReference\\[oaicite:\\d+\\]\\{index=\\d+\\}')
def clean_obj(o):
    if isinstance(o, str): return PATTERN.sub('', o)
    if isinstance(o, list): return [clean_obj(i) for i in o]
    if isinstance(o, dict): return {k: clean_obj(v) for k, v in o.items()}
    return o
def main():
    ap = argparse.ArgumentParser(description="Remove inline citation markers")
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    for fp in a.inputs:
        p = pathlib.Path(fp)
        data = json.loads(p.read_text())
        (out/p.name).write_text(json.dumps(clean_obj(data), indent=2))
        print(f"[CLEAN] {out/p.name}")
if __name__ == "__main__":
    main()
