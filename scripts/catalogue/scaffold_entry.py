#!/usr/bin/env python3
"""scaffold_entry.py - write entries/<slug>/entry.md with everything the extract already knows.

The gap this closes
-------------------
Step 4 of catalogue-first ("write the entry") was the only step with no script
behind it. Every new entry was typed from scratch against SCHEMA.md, which is
how entries end up missing `## Reference lock`, carrying a `register:` outside
the seven allowed values, or - worse - carrying a palette and a set of font
names that were never measured. drift.py finds all three afterwards; this
script makes them not happen.

It prefills only what the extract actually measured: the palette and the font
names out of `extract/*-design-tokens.json`, and the durations, easings and
keyframe names out of `extract/*-motion-tokens.json` + `*-design-language.md`
as the raw material for `## Motion`. Everything a human has to look at a
picture to know - register, grammar, lane, traits, the nine prose sections -
comes out as an empty, correctly named, correctly ordered skeleton.

SCHEMA.md's invariants are enforced, not merely documented:

  * **Never invent a URL.** `url:` is written only when `--url` is given.
    No `--url`, no URL, and `extract:` falls back to `none`.
  * **Never invent tokens.** designlang's generic `Body Font` / `Heading Font`
    placeholders and icon fonts are dropped rather than passed off as
    typefaces, and `measured:` records what was dropped and why.
  * The slug is validated (kebab-case, never a leading `-`). `entries/--help`
    and `entries/-h` exist in this catalogue because capture.py takes
    `sys.argv[2]` unchecked; that cannot happen through here.
  * An existing `entry.md` is never overwritten - the file is created with
    mode "x" and the script exits 1.

    python scripts/catalogue/scaffold_entry.py <slug> --origin raw-url|raw-image|refero|example-site
                                               [--url URL] [--raw FILE] [--refero FILE]
                                               [--title T] [--category C]
                                               [--source anton|claude]
                                               [--catalogue DIR] [--json]

Exit 0 on a clean write, 1 when it refuses to write (entry.md exists, or the
rendered file would not round-trip through index.py's parser), 2 on bad
arguments (slug, --url, unknown origin).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from index import parse_frontmatter          # noqa: E402  the catalogue's own parser

REPO = Path(__file__).resolve().parent.parent.parent
CATALOGUE = REPO / "design-catalogue"

# Same rule drift.py checks entry directories against.
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HEX_RE = re.compile(r"^#[0-9a-fA-F]{3,8}$")
URL_RE = re.compile(r"^(?:https?|file)://\S+$")

# SCHEMA.md's `origin` enum. The plan's step 4 names the first three; the
# fourth is in SCHEMA and in drift.py's ENUMS, so it is accepted here too.
ORIGINS = ("raw-url", "raw-image", "refero", "example-site")

MAX_PALETTE = 12
MAX_KEYFRAMES = 10

# SCHEMA.md "Frontmatter (all keys required)", in SCHEMA's order. `measured` is
# not in SCHEMA but 81 of the 95 entries carry it, and it is the only place the
# provenance of palette/type is written down, so the scaffold writes it too.
KEY_ORDER = ("title", "url", "source_url", "captured", "origin", "extract",
             "category", "category2", "family", "dna", "register", "grammar",
             "lane", "mode", "traits", "palette", "type", "measured", "kind",
             "source", "status")

# SCHEMA.md "Body - H2s in this order". The same nine drift.py requires, with
# SCHEMA's own description of each turned into the one line the agent replaces.
SECTIONS = (
    ("Why it works",
     "2-4 paragraphs on the RELATIONS - how type weight, spacing, image "
     "treatment, surface and motion depend on each other. Not a token list."),
    ("What to borrow (principle)",
     "bullets, each a transferable principle, never a value."),
    ("What to leave",
     "bullets, honest."),
    ("Signature move",
     "the one bespoke device."),
    ("Motion",
     "what the page does on scroll/hover, on top of the measured tokens below. "
     "No extract: what the screenshot implies, marked \"(inferred from image)\"."),
    ("Brief",
     "a paragraph a builder could work from - register, grammar, type, ground, "
     "accent, fold, below-fold structure, close."),
    ("Image recipe",
     "art direction with a [SUBJECT] placeholder."),
    ("Photo search",
     "source + 2-4 phrases."),
    ("Reference lock",
     "Primary / Preserve (3-5) / Borrow only (1-2) / Role rules / Media "
     "strategy / Reject / Token commitments. Same shape as entries/calyx/entry.md."),
)

# designlang emits `Body Font` / `Heading Font` / `Rich Text Font` when it could
# not resolve a real family name. Writing those into `type:` would be inventing
# a typeface, which SCHEMA forbids, so they are dropped and recorded instead.
PLACEHOLDER_FONT = re.compile(r"^(?:[A-Z][a-z]*\s+)*Font$")
ICON_FONT = re.compile(r"icon|glyph", re.I)


def fail(msg: str, code: int = 1):
    print("scaffold: " + msg, file=sys.stderr)
    sys.exit(code)


# --------------------------------------------------------------- extract reads

def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception as e:
        fail("kunde inte lasa " + path.name + ": " + str(e))


def newest(paths):
    """designlang writes one file per prefix; a re-extract can leave two."""
    ps = sorted(paths, key=lambda p: (p.stat().st_mtime, p.name))
    return ps[-1] if ps else None


def palette_from_tokens(tok: dict) -> list:
    """Hexes in the order a page is read: ground, brand, the neutral ramp, then
    whatever surfaces and text colours are left. Deduped, first wins.

    `background.bg0` is taken ahead of the rest of its own group deliberately -
    it is the page's ground and reads first. The remaining `background` tokens
    are secondary surfaces and sort with the tail. This is a presentation
    order, not a measurement: the set is exactly what designlang recorded.
    """
    color = (tok.get("primitive") or {}).get("color") or {}

    def hexes(group, only=None):
        out = []
        for name, node in (color.get(group) or {}).items():
            if only is not None and name not in only:
                continue
            v = node.get("$value") if isinstance(node, dict) else None
            if isinstance(v, str) and HEX_RE.match(v.strip()):
                out.append(v.strip().upper())
        return out

    ordered = hexes("background", only={"bg0"}) + hexes("brand") + hexes("neutral")
    for group in color:                       # surface/text/border/accent/...
        if group not in ("brand", "neutral"):
            ordered += hexes(group)
    seen, out = set(), []
    for h in ordered:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out[:MAX_PALETTE]


def palette_from_language(md: str) -> list:
    """Fallback source: the `### Full Color Inventory` table, already ordered
    by usage count. Used when there is a design-language.md but no tokens."""
    m = re.search(r"^###\s+Full Color Inventory\s*$(.*?)(?=^##\s|\Z)", md, re.S | re.M)
    if not m:
        return []
    seen, out = set(), []
    for row in re.findall(r"^\|\s*`(#[0-9a-fA-F]{3,8})`", m.group(1), re.M):
        h = row.upper()
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out[:MAX_PALETTE]


def fonts_from_tokens(tok: dict):
    """Returns (kept, dropped). Kept are family names designlang resolved."""
    ff = (tok.get("primitive") or {}).get("fontFamily") or {}
    kept, dropped = [], []
    for node in ff.values():
        v = node.get("$value") if isinstance(node, dict) else None
        if not isinstance(v, str):
            continue
        v = v.strip().strip('"\'')
        if not v:
            continue
        if PLACEHOLDER_FONT.match(v) or ICON_FONT.search(v):
            if v not in dropped:
                dropped.append(v)
            continue
        if v not in kept:
            kept.append(v)
    return kept, dropped


def motion_rows(mt: dict, md: str) -> list:
    """The `| kind | tokens |` rows for `## Motion`, from measured values only."""
    rows = []
    durs = []
    for name, node in (mt.get("duration") or {}).items():
        if isinstance(node, dict):
            ms = node.get("ms")
            val = node.get("$value") or (str(ms) + "ms" if ms is not None else "")
            durs.append((ms if isinstance(ms, (int, float)) else 1e9, name, val))
    if durs:
        rows.append(("durations",
                     " · ".join(n + " " + v for _, n, v in sorted(durs))))

    eases = []
    for name, node in (mt.get("easing") or {}).items():
        if isinstance(node, dict) and node.get("$value"):
            fam = node.get("family") or name
            eases.append(fam + " `" + str(node["$value"]) + "`")
    if eases:
        rows.append(("easings", " · ".join(eases)))

    springs = [k for k in (mt.get("spring") or {})]
    if springs:
        rows.append(("springs", " · ".join("`" + s + "`" for s in springs)))

    names = []
    if md:
        sec = re.search(r"^###\s+Keyframe Animations\s*$(.*?)(?=^##\s|\Z)", md, re.S | re.M)
        if sec:
            names = re.findall(r"^\*\*(.+?)\*\*\s*$", sec.group(1), re.M)
    if names:
        shown = " · ".join("`" + n + "`" for n in names[:MAX_KEYFRAMES])
        if len(names) > MAX_KEYFRAMES:
            shown += " · ... (" + str(len(names)) + " total)"
        rows.append(("keyframes declared", shown))
    return rows


# ------------------------------------------------------------------- rendering

def yscalar(s, force_quote: bool = False) -> str:
    """Quote only when the catalogue's own parser would otherwise misread it.
    A bare `https://...` stays bare, the way every entry in the corpus has it.

    index.py's `strip_quotes` peels a matching first/last quote and knows
    nothing about escapes, so a quote INSIDE a value must stay unquoted here
    (`measured:` in entries/aarke/entry.md is written exactly that way). The
    round-trip check in main() is what catches anything this misjudges.
    """
    s = "" if s is None else str(s)
    if force_quote or s == "" or s != s.strip() or s[0] in "[\"'#":
        return json.dumps(s, ensure_ascii=False)
    return s


def render(fm: dict, motion: list, no_extract_note: str) -> str:
    lines = ["---"]
    for key in KEY_ORDER:
        v = fm.get(key)
        if isinstance(v, list):
            lines.append(key + ": " + json.dumps(v, ensure_ascii=False))
        else:
            lines.append(key + ": " + yscalar(v, force_quote=(key == "title")))
    for key in ("raw", "refero"):              # sweep_raw.py reads these
        if fm.get(key):
            lines.append(key + ": " + yscalar(fm[key]))
    lines.append("---")
    lines.append("")

    for head, hint in SECTIONS:
        lines.append("## " + head)
        lines.append("")
        lines.append("<!-- " + hint + " -->")
        lines.append("")
        if head == "Motion":
            if motion:
                lines.append("(from designlang extract)")
                lines.append("")
                lines.append("| kind | tokens |")
                lines.append("|---|---|")
                for kind, toks in motion:
                    lines.append("| " + kind + " | " + toks + " |")
            else:
                lines.append(no_extract_note)
            lines.append("")
    return "\n".join(lines).rstrip("\n") + "\n"


# ------------------------------------------------------------------------ main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="kebab-case, never a leading '-'")
    ap.add_argument("--origin", required=True, choices=ORIGINS)
    ap.add_argument("--url", default="",
                    help="the live URL. Omitted = no URL is written (SCHEMA: never invent one)")
    ap.add_argument("--raw", default="", help="raw/<file> this entry comes from")
    ap.add_argument("--refero", default="", help="processed/<file> this entry comes from")
    ap.add_argument("--title", default="", help="default: the slug, title-cased")
    ap.add_argument("--category", default="", help="one of design-catalogue/categories.md")
    ap.add_argument("--source", default="claude", choices=("anton", "claude"))
    ap.add_argument("--catalogue", default=str(CATALOGUE),
                    help="catalogue root (for fixtures; default the repo's)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    slug = args.slug
    if slug.startswith("-"):
        fail("'" + slug + "' borjar med '-'. Det ar inte en slug, det ar en flagga som "
             "hamnat i slug-positionen - exakt sa uppstod entries/--help och entries/-h.", 2)
    if not SLUG_RE.match(slug):
        fail("'" + slug + "' ar inte kebab-case (^[a-z0-9]+(-[a-z0-9]+)*$).", 2)
    if args.url and not URL_RE.match(args.url):
        fail("--url '" + args.url + "' ar varken http(s):// eller file://. "
             "Utelamna flaggan hellre an att gissa (SCHEMA: never invent a URL).", 2)

    root = Path(args.catalogue).expanduser().resolve()
    entry_dir = root / "entries" / slug
    entry_path = entry_dir / "entry.md"
    if entry_path.exists():
        fail(entry_path.as_posix() + " finns redan. Posten skrivs aldrig over - "
             "redigera den, eller ta bort filen sjalv om den ska goras om.", 1)

    # ---- read whatever designlang left behind
    ex_dir = entry_dir / "extract"
    tok_p = newest(ex_dir.glob("*-design-tokens.json")) if ex_dir.is_dir() else None
    mot_p = newest(ex_dir.glob("*-motion-tokens.json")) if ex_dir.is_dir() else None
    lang_p = newest(ex_dir.glob("*-design-language.md")) if ex_dir.is_dir() else None

    lang = lang_p.read_text(encoding="utf-8", errors="replace") if lang_p else ""
    tok = read_json(tok_p) if tok_p else {}
    mot = read_json(mot_p) if mot_p else {}

    palette = palette_from_tokens(tok) if tok else []
    palette_src = tok_p.name if palette else ""
    if not palette and lang:
        palette = palette_from_language(lang)
        palette_src = lang_p.name + " (Full Color Inventory)" if palette else ""

    fonts, dropped = fonts_from_tokens(tok) if tok else ([], [])
    motion = motion_rows(mot, lang) if (mot or lang) else []

    # ---- frontmatter. Anything that needs eyes on a picture stays empty.
    measured = []
    if palette_src:
        measured.append("palette from " + palette_src)
    if fonts:
        measured.append("type from " + tok_p.name)
    if dropped:
        measured.append("font names unresolved in extract - generic labels only ("
                        + ", ".join("'" + d + "'" for d in dropped) + ")")
    if motion:
        feel = (mot.get("$meta") or {}).get("feel")
        scroll = (mot.get("$meta") or {}).get("scrollLinked")
        bits = [b for b in ("feel " + str(feel) if feel else "",
                            "scroll-linked" if scroll else "") if b]
        measured.append("motion tokens" + (" (" + ", ".join(bits) + ")" if bits else ""))
    prefix = "designlang" if (tok or mot or lang) else "no extract"
    measured_line = prefix + (" (scaffold: " + "; ".join(measured) + ")" if measured
                              else " (scaffold: nothing measured yet)")

    extract_state = "ok" if lang_p else "none"

    fm = {
        "title": args.title or slug.replace("-", " ").title(),
        "url": args.url,
        "source_url": args.url,
        "captured": datetime.now().strftime("%Y-%m-%d"),
        "origin": args.origin,
        "extract": extract_state,
        "category": args.category,
        "category2": "",
        "family": "",
        "dna": "",
        "register": "",
        "grammar": "",
        "lane": "",
        "mode": "",
        "traits": [],
        "palette": palette,
        "type": fonts,
        "measured": measured_line,
        "kind": "example" if args.origin == "example-site" else "reference-style",
        "source": args.source,
        "status": "pending",              # Anton flips it to ready in /catalogue
        "raw": args.raw,
        "refero": args.refero,
    }

    fallback = ("(the extract measured no durations, easings or keyframes)"
                if (tok or mot or lang) else
                "(no extract - read the palette, type and motion off `shot.png` and "
                "`slices/`, and mark this section \"(inferred from image)\".)")
    doc = render(fm, motion, fallback)

    # ---- prove the file the catalogue will read back is the file we meant
    back, _body = parse_frontmatter(doc)
    for key in KEY_ORDER + ("raw", "refero"):
        if key in ("raw", "refero") and not fm[key]:
            continue
        want = fm[key]
        got = back.get(key)
        if isinstance(want, list):
            if list(got or []) != want:
                fail("avbryter: " + key + " lases tillbaka som " + repr(got)
                     + ", inte " + repr(want) + " - inget skrivet.")
        elif (got or "") != (want or ""):
            fail("avbryter: " + key + " lases tillbaka som " + repr(got)
                 + ", inte " + repr(want) + " - inget skrivet.")
    heads = re.findall(r"^##\s+(.+?)\s*$", doc, re.M)
    if heads != [h for h, _ in SECTIONS]:
        fail("avbryter: H2-skelettet matchar inte SCHEMA-ordningen: " + repr(heads))

    entry_dir.mkdir(parents=True, exist_ok=True)
    try:
        with open(entry_path, "x", encoding="utf-8") as fh:   # never clobbers
            fh.write(doc)
    except FileExistsError:
        fail(entry_path.as_posix() + " skapades av nagon annan under korningen - "
             "inget skrivet.", 1)

    todo = [k for k in ("category", "family", "dna", "register", "grammar", "lane",
                        "mode", "traits", "palette", "type") if not fm[k]]
    result = {
        "entry": entry_path.as_posix(),
        "slug": slug,
        "origin": args.origin,
        "url": args.url,
        "extract": extract_state,
        "palette": palette,
        "type": fonts,
        "dropped_font_labels": dropped,
        "motion_rows": [k for k, _ in motion],
        "sections": [h for h, _ in SECTIONS],
        "todo": todo,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("skrev " + entry_path.as_posix())
        print("  extract: " + extract_state
              + ("" if extract_state == "ok" else "  (ingen *-design-language.md)"))
        print("  palette: " + (str(len(palette)) + " hex ur " + palette_src
                               if palette else "tom - las den ur bilden"))
        print("  type:    " + (", ".join(fonts) if fonts else "tom - las den ur bilden"))
        if dropped:
            print("           slappte " + ", ".join(dropped)
                  + " (designlangs platshallare, inte typsnittsnamn)")
        print("  motion:  " + (", ".join(k for k, _ in motion) if motion else "inget matt"))
        if not args.url:
            print("  url:     tom - fyll den ALDRIG pa gissning (SCHEMA-invarianten)")
        if args.origin in ("raw-url", "raw-image") and not args.raw:
            print("  raw:     tom - sweep_raw.py listar kallan som obearbetad tills "
                  "raw: pekar pa den")
        print("  fyll:    " + ", ".join(todo))
        print("  sedan:   python scripts/catalogue/index.py && "
              "python scripts/catalogue/drift.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
