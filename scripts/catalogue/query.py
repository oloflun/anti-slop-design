#!/usr/bin/env python3
"""query.py --family X --register Y --grammar Z --mode M --category C

Prints matching slugs from catalog/index.json with lane + traits.
Any filter may be omitted; omitted filters match everything.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--family")
    ap.add_argument("--register")
    ap.add_argument("--grammar")
    ap.add_argument("--mode")
    ap.add_argument("--category")
    args = ap.parse_args()

    index_path = ROOT / "design-catalogue" / "index.json"
    if not index_path.exists():
        print("no index.json found; run scripts/catalogue/index.py first")
        return
    entries = json.loads(index_path.read_text(encoding="utf-8"))

    def matches(e):
        if args.family and e.get("family") != args.family:
            return False
        if args.register and e.get("register") != args.register:
            return False
        if args.grammar and e.get("grammar") != args.grammar:
            return False
        if args.mode and e.get("mode") != args.mode:
            return False
        if args.category and args.category not in (e.get("category"), e.get("category2")):
            return False
        return True

    hits = [e for e in entries if matches(e)]
    if not hits:
        print("no matches")
        return
    for e in hits:  # index.json is already in rank order (ranking.txt, then motion_floor)
        traits = ", ".join(e.get("traits", []))
        tag = f"#{e['rank']}" if e.get("rank") else f"f{e.get('motion_floor', 0)}"
        print(f"{tag:4s} {e['slug']:20s} | {e.get('lane', '')[:40]:40s} | {traits}")


if __name__ == "__main__":
    main()
