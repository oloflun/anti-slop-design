#!/usr/bin/env python3
"""sweep_raw.py - which saved sources have not become catalogue entries yet.

The gap this closes
-------------------
index.py walks entries/ and never opens raw/ or processed/. So the catalogue
could tell you an entry was missing an image, and could not tell you a source
had arrived and been ignored. Coverage was 100% only because it had been kept
by hand, and there was no way to notice the day that stopped being true.

Step 0 of the chain (catalogue-first) runs this before anything else: a source
Anton saved and the chain never looked at is a reference that cannot be
selected, which is the same failure as not having it.

    python scripts/catalogue/sweep_raw.py [--json] [--quiet]

Exit 1 when something is unprocessed, 0 when the sweep is clean, so it can gate
a step. Ignore a file permanently by adding its name (one per line, `#` for a
comment) to design-catalogue/raw/.ignore together with the reason.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
CATALOGUE = REPO / "design-catalogue"
ENTRIES = CATALOGUE / "entries"
RAW = CATALOGUE / "raw"
PROCESSED = CATALOGUE / "processed"

IMAGE_EXT = (".webp", ".png", ".jpg", ".jpeg", ".avif")

# raw filenames are `<hex hash>-<slug>.<ext>`. The hash is content-derived, so
# a re-save of the same site produces a NEW filename. The slug half is useful
# for spotting that, but it is NOT unique - 20 of the 55 files are
# `<hash>-screenshot.webp` and would all collapse onto one key - so coverage is
# always decided on the exact basename.
HASHED = re.compile(r"^[0-9a-f]{8,32}-(.+)$", re.I)


def stem_key(name: str) -> str:
    stem = Path(name).stem
    m = HASHED.match(stem)
    return (m.group(1) if m else stem).lower()


def referenced():
    """Every raw and processed filename any entry claims.

    Values are whole paths and MAY CONTAIN SPACES ("processed/Aevi
    Wellness.md", "raw/refero.design 2637b30a-....png"), so the only legal
    separator is a comma. Splitting on whitespace turned 13 correctly
    referenced exports into phantom orphans on this script's first run.
    """
    raw_refs, proc_refs = set(), set()
    for entry in sorted(ENTRIES.glob("*/entry.md")):
        text = entry.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            km = re.match(r"^(raw|refero):\s*(.+)$", line.strip())
            if not km:
                continue
            val = km.group(2).strip().strip("'\"")
            if not val or val.lower() in ("none", "null"):
                continue
            for part in val.split(","):
                part = part.strip()
                if not part:
                    continue
                if km.group(1) == "raw":
                    raw_refs.add(Path(part).name.lower())
                else:
                    proc_refs.add(Path(part).name.lower())
    return raw_refs, proc_refs


def ignored() -> dict:
    out = {}
    p = RAW / ".ignore"
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, _, reason = line.partition("#")
        name = name.strip()
        if name:
            out[name.lower()] = reason.strip() or "utan angiven orsak"
    return out


def domain_guess(name: str) -> str:
    """SCHEMA.md's derivation: `www-happyrobot-ai` -> https://www.happyrobot.ai.
    `*-webflow-io` / `*-framer-website` are template hosts."""
    key = stem_key(name)
    if key.startswith("screenshot") or " " in key:
        return ""
    parts = key.split("-")
    if len(parts) < 2:
        return ""
    if key.endswith("-webflow-io"):
        return "https://" + "-".join(parts[:-2]) + ".webflow.io"
    if key.endswith("-framer-website"):
        return "https://" + "-".join(parts[:-2]) + ".framer.website"
    tld = parts[-1]
    if len(tld) > 4 or not tld.isalpha():
        return ""
    return "https://" + ".".join(parts[:-1]) + "." + tld


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    raw_refs, proc_refs = referenced()
    skip = ignored()
    unprocessed = []

    if RAW.is_dir():
        for f in sorted(RAW.iterdir()):
            if f.name.startswith(".") or f.suffix.lower() not in IMAGE_EXT:
                continue
            if f.name.lower() in raw_refs or f.name.lower() in skip:
                continue
            g = domain_guess(f.name)
            note = "" if g else "domanlost filnamn - identifiera sajten ur bilden (SCHEMA raw-image)"
            key = stem_key(f.name)
            if key != "screenshot" and any(stem_key(r) == key for r in raw_refs):
                note = ("samma slug som en redan refererad raw-fil - trolig omsparning, "
                        "inte en ny kalla. Bekrafta mot posten innan du skapar en till.")
            unprocessed.append({
                "file": "raw/" + f.name,
                "origin_guess": "raw-url" if g else "raw-image",
                "domain_guess": g,
                "note": note,
            })

    if PROCESSED.is_dir():
        for f in sorted(PROCESSED.glob("*.md")):
            if f.name.lower() in proc_refs:
                continue
            unprocessed.append({
                "file": "processed/" + f.name,
                "origin_guess": "refero",
                "domain_guess": "",
                "note": "refero-export utan post",
            })

    on_disk = set(p.name.lower() for p in RAW.iterdir()) if RAW.is_dir() else set()
    on_disk |= set(p.name.lower() for p in PROCESSED.glob("*.md")) if PROCESSED.is_dir() else set()
    orphan_refs = sorted(r for r in (raw_refs | proc_refs) if r not in on_disk)

    if args.json:
        print(json.dumps({"unprocessed": unprocessed, "ignored": len(skip),
                          "orphan_refs": orphan_refs}, ensure_ascii=False, indent=2))
    elif not args.quiet:
        if not unprocessed:
            print("sweep: rent - varje kalla under raw/ och processed/ har en post ("
                  + str(len(skip)) + " ignorerade).")
        else:
            print(str(len(unprocessed)) + " kalla(or) utan post:\n")
            for u in unprocessed:
                line = "  " + u["file"] + "  [" + u["origin_guess"] + "]"
                if u["domain_guess"]:
                    line += "  -> " + u["domain_guess"]
                print(line)
                if u["note"]:
                    print("      " + u["note"])
            print("\nSteg 2-4 i catalogue-first galler var och en innan urvalet gors.")
        if orphan_refs:
            print("\nPoster som pekar pa en kalla som inte finns: " + ", ".join(orphan_refs))

    return 1 if unprocessed else 0


if __name__ == "__main__":
    sys.exit(main())
