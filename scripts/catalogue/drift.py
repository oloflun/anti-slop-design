#!/usr/bin/env python3
"""drift.py - everything the catalogue says about itself that is not true.

index.py READS frontmatter with defaults and never CHECKS it. An entry written
with `register: warm photography` (not one of the seven) silently becomes
"other" in index.json, and query.py --register can then never match it: the
entry is in the catalogue and permanently unfindable. Same for a missing
`grammar`, a `## Reference lock` section the builder is told to read that was
never written, and an `extract: ok` whose directory is empty.

Every check here is a fact about a file, not a judgement about taste.

    python scripts/catalogue/drift.py [--json] [--fix-index]

Exit 1 if anything drifted, 0 when clean.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
CATALOGUE = REPO / "design-catalogue"
ENTRIES = CATALOGUE / "entries"
INDEX = CATALOGUE / "index.json"

# From SCHEMA.md. Kept here so a typo in an entry is caught at write time
# rather than discovered as a silent query miss months later.
ENUMS = {
    "origin": {"raw-url", "raw-image", "refero", "example-site"},
    "register": {"editorial print", "cinematic dark", "illustrated dark",
                 "modern clean", "warm photographic", "historical art", "other"},
    "mode": {"persuade", "operate", "read", "experience"},
    "status": {"pending", "ready"},
}

REQUIRED_KEYS = ("title", "url", "captured", "origin", "extract", "category",
                 "family", "dna", "register", "grammar", "lane", "mode",
                 "traits", "palette", "type", "kind", "source", "status")

REQUIRED_H2 = ("Why it works", "What to borrow", "What to leave", "Signature move",
               "Motion", "Brief", "Image recipe", "Photo search", "Reference lock")

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_fm(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip("'\"")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    problems = []

    def add(kind, slug, detail):
        problems.append({"kind": kind, "slug": slug, "detail": detail})

    if not ENTRIES.is_dir():
        print("drift: entries/ saknas")
        return 1

    newest_entry = 0.0
    for d in sorted(ENTRIES.iterdir()):
        if not d.is_dir():
            continue
        slug = d.name
        if not SLUG_RE.match(slug):
            add("skrapkatalog", slug,
                "slug ar inte kebab-case - kommer troligen fran att capture.py "
                "anropades med en flagga som slug (den validerar inte sys.argv[2])")
            continue
        ep = d / "entry.md"
        if not ep.exists():
            add("saknar entry.md", slug, "katalog utan post")
            continue
        newest_entry = max(newest_entry, ep.stat().st_mtime)
        text = ep.read_text(encoding="utf-8", errors="replace")
        fm = parse_fm(text)

        for k in REQUIRED_KEYS:
            if k not in fm:
                add("saknad nyckel", slug, k)
        for key, allowed in ENUMS.items():
            v = (fm.get(key) or "").lower()
            if v and v not in allowed:
                add("enum utanfor SCHEMA", slug,
                    key + " = '" + v + "' (tillatna: " + ", ".join(sorted(allowed)) + ")")

        heads = set(re.findall(r"^##\s+(.+?)\s*$", text, re.M))
        for h in REQUIRED_H2:
            if not any(h.lower() in x.lower() for x in heads):
                add("saknad H2", slug, "## " + h)

        body_motion = re.search(r"^##\s*Motion\s*\n(.*?)(?=\n##|\Z)", text, re.S | re.M)
        if body_motion and not body_motion.group(1).strip():
            add("tom Motion", slug, "## Motion finns men ar tom")

        ex = (fm.get("extract") or "").lower()
        exdir = d / "extract"
        has_dl = exdir.is_dir() and any(exdir.glob("*-design-language.md"))
        if ex.startswith("blocked"):
            pass   # a recorded, accepted fact (bot wall / block page), not drift
        elif ex.startswith("failed"):
            add("extract failed", slug, fm.get("extract", ""))
        elif ex == "ok" and not has_dl:
            add("extract ok men tom", slug,
                "frontmatter sager ok men extract/*-design-language.md saknas - "
                "referensgolvet kraver den filen")
        elif ex in ("", "none") and (fm.get("url") or "").startswith("http"):
            add("url utan extract", slug, fm.get("url", ""))

        if not (d / "fold.webp").exists():
            add("saknar fold", slug, "fold.webp - posten kan inte lasas som pixlar")

    if INDEX.exists() and newest_entry and INDEX.stat().st_mtime < newest_entry - 1:
        add("index foraldrat", "-", "index.json ar aldre an nyaste entry.md - kor index.py")

    if args.json:
        print(json.dumps(problems, ensure_ascii=False, indent=2))
    else:
        if not problems:
            print("drift: 0 avvikelser.")
        else:
            by = {}
            for p in problems:
                by.setdefault(p["kind"], []).append(p)
            print(str(len(problems)) + " avvikelser i " + str(len(by)) + " klasser:\n")
            for kind in sorted(by):
                rows = by[kind]
                print("  " + kind + " (" + str(len(rows)) + ")")
                for r in rows[:12]:
                    print("      " + r["slug"] + ": " + r["detail"])
                if len(rows) > 12:
                    print("      ... och " + str(len(rows) - 12) + " till")
                print("")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
