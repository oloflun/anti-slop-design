#!/usr/bin/env python3
"""select.py - pick the 2-4 catalogue entries a brief must be measured against.

Why this exists
---------------
r7 (2026-09-06/07) put the slugs straight into the builder prompt. The builders
read them, so the reference floor was satisfied, and `Skill(design-catalog)`
was still never invoked: the *selection* came out of the orchestrator's memory,
not out of the catalogue. Nothing could tell the difference afterwards.

This script is that difference. It scores every entry in index.json against the
brief's declared register / grammar / category / authority plus its free text,
prints a ranked list, and writes ONE `catalogue-select` row into the session
ledger naming the chosen slugs. design-gate.py's reference floor requires that
row before the first UI write, so a build cannot proceed on recalled references.

Deterministic. No model call anywhere in here.

    python scripts/catalogue/select.py --brief BRIEF.md [--k 4] [--wildcard]
                                       [--exclude slug,slug] [--explain] [--json]
                                       [--root DIR] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
CATALOGUE = REPO / "design-catalogue"
INDEX = CATALOGUE / "index.json"

# The build's own example sites are output, not reference. Measuring a new
# Alunix concept against Calyx is measuring it against ourselves.
OWN_SITES = {"calyx", "horai", "hyperborea", "tidvatten", "klova",
             "vintergatan", "vinterspelen", "before-ai-slop"}

STOP = {
    "och", "att", "det", "som", "med", "den", "ett", "har", "ska", "the", "and",
    "for", "with", "this", "that", "from", "into", "page", "site", "sida",
    "sidan", "design", "av", "till", "inte", "ur", "eller", "ett", "vid",
}

FIELDS_TEXT = ("lane", "dna", "family", "title")


def load_index() -> list:
    if not INDEX.exists():
        sys.exit("select: " + str(INDEX) + " saknas - kor scripts/catalogue/index.py forst.")
    return json.loads(INDEX.read_text(encoding="utf-8"))


def read_brief(path: Path) -> dict:
    """Pull declared fields out of a brief, plus its free text.

    Accepts `Register: modern clean` and the markdown-bolded
    `**Register:** modern clean` the chain's own BRIEF template uses.
    """
    text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    out = {"text": text}
    for key in ("register", "grammar", "category", "category2", "mode", "authority", "family"):
        m = re.search(r"^[#*\s]*" + key + r"\s*[:*]+\s*(.+)$", text, re.I | re.M)
        if m:
            out[key] = m.group(1).strip().strip("*_` ").lower()
    return out


def words(s):
    return set(w for w in re.findall(r"[a-zaaoAAO][a-zaao\-]{2,}", (s or "").lower())
               if w not in STOP)


def prior_primaries(repo: Path) -> set:
    """Slugs already used as a primary reference for this client. Reusing one
    is how two rounds end up looking like each other."""
    out = set()
    for brief in repo.glob("tests/alunix-*/**/BRIEF.md"):
        try:
            t = brief.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in re.finditer(r"^\s*[-*]?\s*Primary\s*[:*]+\s*([a-z0-9\-]+)", t, re.I | re.M):
            out.add(m.group(1).strip().lower())
    return out


def score(entry: dict, brief: dict, prior: set):
    s = 0
    why = []

    def eq(a, b):
        return bool(a) and bool(b) and str(a).strip().lower() == str(b).strip().lower()

    if eq(entry.get("register"), brief.get("register")):
        s += 3
        why.append("+3 register")
    if eq(entry.get("grammar"), brief.get("grammar")):
        s += 3
        why.append("+3 grammatik")
    for k in ("category", "category2"):
        if eq(entry.get(k), brief.get("category")) or eq(entry.get(k), brief.get("category2")):
            s += 2
            why.append("+2 " + k)
            break
    if eq(entry.get("mode"), brief.get("mode")):
        s += 1
        why.append("+1 mode")

    auth = brief.get("authority", "")
    hay = " ".join(str(entry.get(f, "")) for f in ("lane", "traits", "dna", "family")).lower()
    if auth and auth.split()[0] in hay:
        s += 2
        why.append("+2 auktoritet")

    bw = words(brief.get("text", ""))
    ew = set()
    for f in FIELDS_TEXT:
        ew |= words(str(entry.get(f, "")))
    for t in entry.get("traits", []) or []:
        ew |= words(str(t))
    overlap = bw & ew
    if overlap:
        bonus = min(len(overlap), 6)
        s += bonus
        why.append("+" + str(bonus) + " fritext (" + ", ".join(sorted(overlap)[:4]) + ")")

    slug = entry.get("slug", "")
    if slug in OWN_SITES:
        s -= 5
        why.append("-5 egen exempelsajt")
    if slug in prior:
        s -= 2
        why.append("-2 primar i foregaende runda")
    return s, why


def ledger_write(root: Path, slugs, brief):
    """One `catalogue-select` row, in the shape the hooks write."""
    d = root / ".impeccable"
    try:
        d.mkdir(parents=True, exist_ok=True)
        rec = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "event": "catalogue-select",
            "slugs": list(slugs),
            "brief": str(brief),
        }
        sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
        if sid:
            rec["session"] = sid
        p = d / "design-session.jsonl"
        with p.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return p
    except Exception as e:
        sys.stderr.write("select: kunde inte skriva ledgerrad (" + str(e) + ")\n")
        return None


def photo_line(slug: str) -> str:
    ep = CATALOGUE / "entries" / slug / "entry.md"
    if not ep.exists():
        return ""
    t = ep.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^##\s*Photo search\s*\n(.+?)(?=\n##|\Z)", t, re.S | re.M)
    return " ".join(m.group(1).split())[:140] if m else ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--brief", required=True)
    ap.add_argument("--k", type=int, default=4)
    ap.add_argument("--exclude", default="")
    ap.add_argument("--wildcard", action="store_true",
                    help="add one high-scoring entry from OUTSIDE the brief's category "
                         "- the catalogue IS the category, so a move it does not "
                         "contain has to come from somewhere else")
    ap.add_argument("--explain", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=".", help="project root whose ledger gets the row")
    ap.add_argument("--dry-run", action="store_true", help="rank, write no ledger row")
    args = ap.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    brief_path = Path(args.brief)
    brief = read_brief(brief_path)
    entries = load_index()
    prior = prior_primaries(REPO)
    excl = set(s.strip().lower() for s in args.exclude.split(",") if s.strip())

    ranked = []
    for e in entries:
        if e.get("slug", "") in excl:
            continue
        sc, why = score(e, brief, prior)
        ranked.append((sc, e, why))
    ranked.sort(key=lambda r: (-r[0], r[1].get("slug", "")))

    picked = list(ranked[:max(1, args.k)])

    if args.wildcard and brief.get("category"):
        cat = brief["category"]
        chosen = set(e.get("slug") for _, e, _ in picked)
        for sc, e, why in ranked:
            if e.get("slug") in chosen or e.get("slug") in OWN_SITES:
                continue
            if str(e.get("category", "")).lower() == cat or str(e.get("category2", "")).lower() == cat:
                continue
            picked.append((sc, e, why + ["wildcard: utanfor kategorin"]))
            break

    slugs = [e.get("slug", "") for _, e, _ in picked]
    if not slugs:
        sys.stderr.write("select: inga poster matchade - bredda registret, slapp "
                         "grammatiken, prova en angransande kategori, eller sok pa "
                         "ett kant varumarke.\n")
        return 1

    if args.json:
        print(json.dumps([{"slug": e.get("slug"), "score": sc,
                           "register": e.get("register"), "grammar": e.get("grammar"),
                           "why": why} for sc, e, why in picked],
                         ensure_ascii=False, indent=2))
    else:
        print("Brief: " + str(brief_path) + "  ->  " + str(len(slugs)) + " poster\n")
        for sc, e, why in picked:
            print("  %3d  %-24s %-22s %s" % (sc, e.get("slug", ""),
                                             e.get("register", ""), e.get("grammar", "")))
            if args.explain:
                print("       " + (" | ".join(why) if why else "ingen traff"))
        if args.explain:
            print("\nMediastrategi ur posternas egna falt (Photo search) - "
                  "locken ska inte gissa:")
            for _, e, _ in picked:
                line = photo_line(e.get("slug", ""))
                if line:
                    print("  - " + e.get("slug", "") + ": " + line)

    if not args.dry_run:
        p = ledger_write(Path(args.root).resolve(), slugs, brief_path)
        if p:
            print("\ncatalogue-select skriven: " + ", ".join(slugs) + "  ->  " + str(p))
    return 0


if __name__ == "__main__":
    sys.exit(main())
