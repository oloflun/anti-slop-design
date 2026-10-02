#!/usr/bin/env python3
"""motion_entry.py - turn a reading of a captured showcase site into entries/<slug>/entry.md.

The split is deliberate: what has to be SEEN (register, grammar, lane, why it works,
the motion sequence, the signature move) is written by a person or the lead after
looking at entries/<slug>/motion/sheet.webp, one JSON line per site in
design-catalogue/showcase-readings.jsonl. What can be MEASURED is never typed:

  palette   quantized from fold.webp + two scroll slices (PIL), 6 colours max
  type      document.fonts at capture (fallback/icon faces dropped)
  stack     motion/probe.json: GSAP version, pins, Lenis, WebGL, page transitions, smoothing

Reading keys: slug title cat cat2 fam dna reg gram mode lane traits why borrow leave sig
motion img floor (2 = sets the floor, 1 = solid, 0 = one move worth keeping).

    python scripts/catalogue/motion_entry.py            # render every reading without an entry.md
    python scripts/catalogue/motion_entry.py --redo     # overwrite (only entries this script wrote)
    python scripts/catalogue/motion_entry.py --selftest
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent.parent
CAT = ROOT / "design-catalogue"
ENTRIES = CAT / "entries"
READINGS = CAT / "showcase-readings.jsonl"
SITES = CAT / "showcase-sites.json"
MARK = "<!-- motion_entry.py -->"

REGISTERS = {"editorial print", "cinematic dark", "illustrated dark", "modern clean",
             "warm photographic", "historical art", "other"}
GRAMMARS = {"filmic one-shot", "chaptered editorial", "live surface", "continuous world",
            "typographic poster", "gallery/catalog", "split stage", "rhythmic cutlist", "none"}
MODES = {"persuade", "operate", "read", "experience"}
CATEGORIES = {"playful", "institutional", "portfolio", "product-focused", "editorial",
              "hospitality", "consumer-brand", "luxury-craft"}
GENERIC_FONT = re.compile(r"fallback|icon|awesome|material|swiper|slick|^body font$|^heading font$|emoji|symbol", re.I)


def palette(d: Path, n=6):
    imgs = [d / "fold.webp"] + sorted((d / "slices").glob("*.webp"))[2:8:3]
    px = []
    for p in imgs:
        if p.exists():
            im = Image.open(p).convert("RGB").resize((160, 100))
            px.append(im)
    if not px:
        return []
    strip = Image.new("RGB", (160, 100 * len(px)))
    for i, im in enumerate(px):
        strip.paste(im, (0, 100 * i))
    q = strip.quantize(colors=12, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[:36]
    counts = sorted(q.getcolors(), reverse=True)
    out = []
    for cnt, idx in counts:
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        if all(sum(abs(a - b) for a, b in zip(rgb, o)) > 60 for o in out):
            out.append(rgb)
        if len(out) == n:
            break
    return ["#%02X%02X%02X" % c for c in out]


def fonts(probe):
    seen = []
    for f in probe.get("fonts") or []:
        f = f.strip()
        if f and not GENERIC_FONT.search(f) and f not in seen:
            seen.append(f)
    return seen[:4]


def stack_line(p):
    bits = []
    if p.get("gsapVersions"):
        bits.append("GSAP " + "/".join(p["gsapVersions"]))
    st = p.get("scrollTriggersAfterScroll") or p.get("scrollTriggers")
    if st:
        bits.append(f"{st} ScrollTriggers")
    pins = max(p.get("pinSpacers") or 0, p.get("pinSpacersAfterScroll") or 0)
    if pins:
        bits.append(f"{pins} pinned sections")
    if p.get("lenis"):
        bits.append("Lenis")
    if p.get("scrollSmoother"):
        bits.append("ScrollSmoother")
    if p.get("locomotive"):
        bits.append("Locomotive")
    for k, name in (("barba", "Barba"), ("swup", "Swup"), ("taxi", "Taxi")):
        if p.get(k):
            bits.append(name + " page transitions")
    if p.get("webglCanvases"):
        bits.append(f"WebGL canvas x{p['webglCanvases']}" + (" (three.js)" if p.get("three") else ""))
    if p.get("videos"):
        bits.append(f"{p['videos']} video")
    if (p.get("splitTextSuspect") or 0) > 40:
        bits.append("split text")
    lag = [v for v in (p.get("smoothingLagPx") or []) if v > 0]
    if p.get("smoothed") and lag:
        bits.append(f"smoothed scroll (median {sorted(lag)[len(lag) // 2]} px still travelling after input stops)")
    elif (p.get("scrollYs") or [1])[-1] == 0:
        bits.append("virtual scroll (window never scrolls; transform/WebGL scroller)")
    if p.get("unlocked"):
        bits.append("entry gate: " + ", ".join(p["unlocked"]))
    return "; ".join(bits) or "no motion library detected on window"


def check(r):
    errs = []
    for k in ("slug", "title", "cat", "fam", "dna", "reg", "gram", "mode", "lane", "traits", "why",
              "borrow", "leave", "sig", "motion", "img", "floor"):
        if k not in r or r[k] in ("", None):
            errs.append("missing " + k)
    if r.get("reg") not in REGISTERS:
        errs.append("register " + str(r.get("reg")))
    if r.get("gram") not in GRAMMARS:
        errs.append("grammar " + str(r.get("gram")))
    if r.get("mode") not in MODES:
        errs.append("mode " + str(r.get("mode")))
    for k in ("cat", "cat2"):
        if r.get(k) and r[k] not in CATEGORIES:
            errs.append(f"{k} {r[k]}")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", r.get("fam", "")):
        errs.append("family not kebab-case")
    return errs


def q(s):
    return '"' + str(s).replace('"', "'") + '"'


def render(r, site, probe, d):
    pal = palette(d)
    ty = fonts(probe)
    stack = stack_line(probe)
    tier = {2: "sets the floor", 1: "solid", 0: "one move worth keeping"}[int(r["floor"])]
    fm = [
        "---",
        f"title: {q(r['title'])}",
        f"url: {site['url']}",
        f"source_url: {site['url']}",
        f"captured: {date.today().isoformat()}",
        "origin: raw-url",
        "extract: none",
        f"category: {r['cat']}",
        f"category2: {q(r.get('cat2', ''))}",
        f"family: {r['fam']}",
        f"dna: {q(r['dna'])}",
        f"register: {r['reg']}",
        f"grammar: {r['gram']}",
        f"lane: {q(r['lane'])}",
        f"mode: {r['mode']}",
        "traits: [" + ", ".join(q(t) for t in r["traits"]) + "]",
        "palette: [" + ", ".join(q(c) for c in pal) + "]",
        "type: [" + ", ".join(q(t) for t in ty) + "]",
        f"measured: {q('palette quantized from motion captures; type from document.fonts; stack from motion/probe.json')}",
        "kind: reference-style",
        "source: claude",
        "status: ready",
        f"showcase: {site['src']}",
        f"motion_floor: {r['floor']}",
        "---",
        "",
    ]
    bl = lambda xs: "\n".join("- " + x for x in xs)
    credits = ", ".join(c for c in site.get("credits", []) if c)[:200]
    body = f"""{MARK}
## Why it works

{r['why']}

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
{site['src'].replace('+', ' and ')} showcase{(' (credits: ' + credits + ')') if credits else ''}.

## What to borrow (principle)

{bl(r['borrow'])}

## What to leave

{bl(r['leave'])}

## Signature move

{r['sig']}

## Motion

{r['motion']}

Measured (`motion/probe.json`): {stack}. Floor tier: **{tier}** (`references/scroll/showcase-floor.md`).

## Brief

A {r['reg']} page in the {r['gram']} grammar: {r['lane'][0].lower() + r['lane'][1:]} Type: {', '.join(ty) or 'read from the captures'}.
Ground and ink from the measured palette ({', '.join(pal[:3])}). Motion carries the page through
{r['sig'][0].lower() + r['sig'][1:]} Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — {r['img']}

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: {r['img']}

## Reference lock

Primary reference/direction: {r['title']} — {r['lane']}
Preserve (3-5 traits): {'; '.join(r['traits'][:5])}.
Borrow only (1-2): {'; '.join(r['borrow'][:2])}
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: {r['img']}
Reject: {'; '.join(r['leave'])}
Token commitments: palette {', '.join(pal) or '-'}; type {', '.join(ty) or '-'}; engine GSAP + Lenis linked (never vendored).
"""
    return "\n".join(fm) + body


def main():
    redo = "--redo" in sys.argv
    sites = {s["slug"]: s for s in json.loads(SITES.read_text(encoding="utf-8"))}
    rows = [json.loads(l) for l in READINGS.read_text(encoding="utf-8").splitlines() if l.strip()]
    done = bad = 0
    for r in rows:
        d = ENTRIES / r["slug"]
        errs = check(r)
        site = sites.get(r["slug"])
        probe_p = d / "motion" / "probe.json"
        if not site:
            errs.append("slug not in showcase-sites.json")
        if not probe_p.exists():
            errs.append("no motion/probe.json")
        ef = d / "entry.md"
        if ef.exists() and (not redo or MARK not in ef.read_text(encoding="utf-8")):
            continue  # never overwrite an entry this script did not write
        if errs:
            print(f"SKIP {r['slug']}: {'; '.join(errs)}")
            bad += 1
            continue
        ef.write_text(render(r, site, json.loads(probe_p.read_text(encoding="utf-8")), d), encoding="utf-8")
        done += 1
    print(f"motion_entry: wrote {done}, skipped {bad}, readings {len(rows)}")
    return 1 if bad else 0


def selftest():
    r = {"slug": "x", "title": "X", "cat": "portfolio", "fam": "a-b", "dna": "A x B", "reg": "modern clean",
         "gram": "none", "mode": "persuade", "lane": "L.", "traits": ["t"], "why": "w", "borrow": ["b"],
         "leave": ["l"], "sig": "S.", "motion": "m", "img": "i", "floor": 1}
    assert check(r) == []
    assert "register bad" in check({**r, "reg": "bad"})
    assert "family not kebab-case" in check({**r, "fam": "A B"})
    assert stack_line({"gsapVersions": ["3.15.0"], "pinSpacers": 2, "lenis": True}) == "GSAP 3.15.0; 2 pinned sections; Lenis"
    assert fonts({"fonts": ["Inter", "arial narrow fallback", "Font Awesome", "Inter"]}) == ["Inter"]
    print("selftest ok")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        sys.exit(main())
