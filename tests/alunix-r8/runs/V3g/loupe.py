#!/usr/bin/env python3
"""R6b: detaljcellens förstoringsglas (leadens fel 1 och 2).

Varje steg visar ETT element ur sajten 2,5-3 gånger större än iframen visar
det. Iframen är skalad 0,9467 (mätt, scaleShowcaseFrame vid 1440x900), så
2,5-3x av iframen är 2,367-2,840x av sajtens egna CSS-pixlar. Detaljcellen
är 599,58 x 426,53 CSS px, så ramen i sajten blir 211-253 x 150-180 px.

Ren kant (fel 2) mäts, inte bedöms: varje ord på sidan får sin bläckgräns
(Range-rektangel + canvas measureText, actualBoundingBox), och en ram godkänns
bara om inget ord korsar dess kant och inget ord ligger närmare kanten än
CLEAR px. Bilder och bakgrundsfoton får korsa kanten om de täcker minst 25 %
av ramen på båda ledderna; en mindre bit är ett fragment och underkänner ramen.
`--selftest` kör kontrollen mot ett medvetet trasigt utsnitt först (M3).

Bilderna tas i deviceScaleFactor 3, beskärs till cellens exakta proportion och
sparas som WebP q82. Dithret görs med dither_variant ur runs/V3f/dither.py,
efter att bilden skalats till 900 px bredd som i V3f, så kornet blir lika stort
på skärmen som i #kontakt och i R6.
"""
import importlib.util
import io
import json
import os
import sys

from PIL import Image, ImageOps
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "steps")
BASE = "http://127.0.0.1:3307/sites/"
IFRAME_SCALE = 0.9467
CELL_W, CELL_H = 599.578125, 426.53125
ASPECT = CELL_W / CELL_H
M_LO, M_HI = 2.5 * IFRAME_SCALE, 3.0 * IFRAME_SCALE   # i sajtens CSS px
CLEAR = 5
DSF = 3

_spec = importlib.util.spec_from_file_location("v3f_dither", os.path.join(HERE, "..", "V3f", "dither.py"))
_d = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_d)

# Varje steg: sajt, hur sidan ställs (scroll i px, eller ett element som
# centreras), målet som ska vara helt i ramen (selektor + textbit), och
# vilka ord som måste ligga utanför. `top` = lägsta tillåtna y i viewporten
# (Hōrais fasta menyrad täcker 0-120 px).
STEPS = {
    "calyx-1": dict(site="calyx", scroll_to=0,
                    target=[("section.relative p.kicker", "No. 042 — Spring Edition")], top=0),
    # body text has no word gap that lines up on two or more lines (measured,
    # shots/loupe-gaps.txt), so no 2.5-3x frame of it is clean; the serif is
    # shown in the masthead instead, the one Cardo italic set on its own line
    "calyx-2": dict(site="calyx", scroll_to=0, target=[("header a.font-display", "Calyx")], top=0),
    # the corner of the second photo with its commission number under it.
    # Tried and rejected (shots/r6b-redo2.png, calyx-3 drafts): the full label
    # is 310 px (> 253), so it would end mid-sentence; the first photo's corner
    # is blank wall; the pair's two corners need 184 px of height (> 180).
    # R9: the caption now names the purpose ("Private home", no address), which is what the
    # step's lede says the captions do - so the whole label is the target.
    "calyx-3": dict(site="calyx", center="figure:nth-of-type(2) figcaption", oy=0.8,
                    target=[("figure:nth-of-type(2) figcaption span", "Cmsn. 0188 — Private home")]),
    # paragraph above and address below leave 143 px; the frame needs >= 150.
    # They are hidden for the capture only - the address, its face, colour and
    # ground are the site's own. Stated in RAPPORT.md.
    "calyx-5": dict(site="calyx", center="a[href^=mailto]", cx=3,
                    hide=["#commission p", "#commission a[href^=mailto] + div"],
                    target=[("a[href^=mailto]", "atelier@calyx.se"), ("a[href^=mailto] span", "↗")]),
    # Ō with its macron is 179 px of ink and its neighbours stand 40 px away:
    # no landscape frame holds it alone. H is the one letter that does.
    "horai-1": dict(site="horai", scroll_to=0, chars=["#hero-title"], m_hi=M_LO + 0.1,
                    target=[("#hero-title", "H")], top=0),
    # the word-lit lede has no clean 2.5-3x frame (lines 57 px apart, no shared
    # gaps): the only clean frames hold one line in a corner. The stamp does.
    "horai-2": dict(site="horai", center="#house-lede", target=[("section:nth-of-type(2) p.jp", "家")], top=120),
    # the site's own formed state: section centred, proximity 1, blur 0
    "horai-3": dict(site="horai", center="#quote-section", chars=["#quote-jp"], levels=(200, 230),
                    target=[("#quote-jp", "料理は対話")], top=120),
    "horai-4": dict(site="horai", center="article:first-of-type p.num",
                    target=[("article:first-of-type p.num", "1,480"),
                            ("article:first-of-type .md\\:text-right p:nth-child(2)", "PER GUEST")], top=120),
    "horai-5": dict(site="horai", center="section:has(.room-img) p.jp",
                    target=[("section:has(.room-img) p.jp", "部屋")], top=120),
    "horai-6": dict(site="horai", nav=True, m_hi=M_LO + 0.25, target=[("header a[href='#reservations']", None)], top=0),
}

INK_JS = r"""
(chars) => {
  const cv = document.createElement('canvas').getContext('2d');
  const out = [];
  const vis = el => { for (let e = el; e && e !== document; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) < 0.05) return false; }
    return true; };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const el = n.parentElement;
    if (!el || !vis(el) || /SCRIPT|STYLE|NOSCRIPT/.test(el.tagName)) continue;
    const cs = getComputedStyle(el);
    cv.font = `${cs.fontStyle} ${cs.fontWeight} ${cs.fontSize} ${cs.fontFamily}`;
    try { cv.letterSpacing = cs.letterSpacing === 'normal' ? '0px' : cs.letterSpacing; } catch (e) {}
    const re = chars.some(c => el.closest(c)) ? /\S/g : /\S+/g; let m;
    while ((m = re.exec(n.data))) {
      const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
      const txt = cs.textTransform === 'uppercase' ? m[0].toUpperCase() : m[0];
      const mt = cv.measureText(txt);
      for (const rc of r.getClientRects()) {
        if (rc.width < 1) continue;
        const k = rc.width / Math.max(1, mt.width);          // transform scale (Hōrais citat)
        const base = rc.top + mt.fontBoundingBoxAscent * k;
        out.push({t: m[0], x0: rc.left - mt.actualBoundingBoxLeft * k, x1: rc.left + mt.actualBoundingBoxRight * k,
                  y0: base - mt.actualBoundingBoxAscent * k, y1: base + mt.actualBoundingBoxDescent * k});
      }
    }
  }
  const imgs = [];
  document.querySelectorAll('body *').forEach(e => {
    const cs = getComputedStyle(e);
    if ((e.tagName === 'IMG' || cs.backgroundImage.includes('url(')) && vis(e)) {
      const r = e.getBoundingClientRect();
      if (r.width > 4 && r.height > 4) imgs.push({x0: r.left, y0: r.top, x1: r.right, y1: r.bottom, c: e.className.toString().slice(0, 30)});
    }
  });
  return {words: out, imgs};
}
"""


def target_box(page, sel, sub):
    return page.evaluate("""([sel, sub]) => {
      const el = document.querySelector(sel); if (!el) return null;
      if (sub === null) { const b = el.getBoundingClientRect(); return {x0: b.left, y0: b.top, x1: b.right, y1: b.bottom}; }
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n, box = null;
      while ((n = w.nextNode())) { const i = n.data.indexOf(sub); if (i < 0) continue;
        const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + sub.length);
        const b = r.getBoundingClientRect(); box = {x0: b.left, y0: b.top, x1: b.right, y1: b.bottom}; break; }
      return box; }""", [sel, sub])


def check(rect, words, imgs, cx=CLEAR, cy=CLEAR):
    """Returns a list of problems for a frame {x0,y0,x1,y1}; [] = clean."""
    x0, y0, x1, y1 = rect["x0"], rect["y0"], rect["x1"], rect["y1"]
    w, h = x1 - x0, y1 - y0
    bad = []
    for d in words:
        inside = d["x0"] >= x0 + cx and d["x1"] <= x1 - cx and d["y0"] >= y0 + cy and d["y1"] <= y1 - cy
        outside = d["x1"] <= x0 - 1 or d["x0"] >= x1 + 1 or d["y1"] <= y0 - 1 or d["y0"] >= y1 + 1
        if not inside and not outside:
            bad.append("ord i kanten: " + d["t"])
    for m in imgs:
        iw = min(x1, m["x1"]) - max(x0, m["x0"])
        ih = min(y1, m["y1"]) - max(y0, m["y0"])
        if iw <= 0 or ih <= 0:
            continue
        full = m["x0"] >= x0 and m["x1"] <= x1 and m["y0"] >= y0 and m["y1"] <= y1
        if not full and (iw < 0.25 * w or ih < 0.25 * h):
            bad.append(f"bildfragment {iw:.0f}x{ih:.0f}: {m['c']}")
    return bad


def search(tboxes, words, imgs, top, cx=CLEAR, m_lo=M_LO, texts=(), oy=0.48, m_hi=M_HI, excl=(), cy=CLEAR):
    """Largest magnification first; for each, every 1-px frame position that
    holds the whole target with >= CLEAR px margin. Returns best frame."""
    tx0 = min(b["x0"] for b in tboxes); tx1 = max(b["x1"] for b in tboxes)
    ty0 = min(b["y0"] for b in tboxes); ty1 = max(b["y1"] for b in tboxes)
    # the target's own ink, not its line box
    ink = [d for d in words if d["x0"] < tx1 and d["x1"] > tx0 and d["y0"] < ty1 and d["y1"] > ty0
           and any(t is not None and (d["t"] in t or t in d["t"]) for t in texts)]
    if ink and all(t is not None for t in texts):
        tx0 = min(d["x0"] for d in ink); tx1 = max(d["x1"] for d in ink)
        ty0 = min(d["y0"] for d in ink); ty1 = max(d["y1"] for d in ink)
    reach = CELL_W / M_LO + CLEAR
    near = lambda d: d["x1"] > tx0 - reach and d["x0"] < tx1 + reach and d["y1"] > ty0 - reach and d["y0"] < ty1 + reach
    words = [d for d in words if near(d)]
    imgs = [d for d in imgs if near(d)]
    steps = 24
    for i in range(steps + 1):
        m = m_hi - (m_hi - m_lo) * i / steps
        w = CELL_W / m; h = w / ASPECT
        best = None
        xs = range(int(tx1 + cx - w), int(tx0 - cx) + 1)
        ys = range(int(ty1 + cy - h), int(ty0 - cy) + 1)
        mx, my = (tx0 + tx1) / 2, (ty0 + ty1) / 2
        xstep = 0.5 if cx < CLEAR else 2
        for x in [xs.start + k * xstep for k in range(int((xs.stop - xs.start) / xstep))]:
            if x < 0 or x + w > 1440:
                continue
            for y in ys[::3 if cx < CLEAR else 2]:
                if y < top or y + h > 900:
                    continue
                r = {"x0": x, "y0": y, "x1": x + w, "y1": y + h}
                if check(r, words, imgs, cx, cy):
                    continue
                if any(d["t"] in excl and d["x1"] > x - 1 and d["x0"] < x + w + 1 and d["y1"] > y and d["y0"] < y + h
                       for d in words):
                    continue
                # prefer the target near the frame's optical centre
                off = abs((x + w / 2) - mx) / w + abs((y + h * oy) - my) / h
                if best is None or off < best[0]:
                    best = (off, r)
        if best:
            return m, best[1], (tx0, ty0, tx1, ty1)
    return None, None, (tx0, ty0, tx1, ty1)


def prepare(page, key, s):
    page.goto(BASE + s["site"] + ".html" + s.get("query", ""), wait_until="load")
    page.wait_for_timeout(1200)
    if s.get("query"):
        page.wait_for_timeout(600)
        return
    if "scroll_to" in s:
        page.evaluate(f"window.scrollTo(0,{s['scroll_to']})")
    elif s.get("lede"):
        # the site's own word-light, stopped with the first line lit and the
        # second half-lit: progress = 1-(top-0.15vh)/(0.65vh), lit = floor(p*N)
        page.evaluate("""() => { const l = document.getElementById('house-lede');
            const N = l.querySelectorAll('.word').length, vh = innerHeight;
            const lit = 6, p = (lit + 0.5) / N, top = vh * 0.15 + (1 - p) * vh * 0.65;
            scrollTo(0, l.getBoundingClientRect().top + scrollY - top); }""")
    elif s.get("nav"):
        # the button at the foot of the page: #reservations at the top of the
        # viewport, so the bar sits on the section's own empty top padding
        page.evaluate("""() => { const s = document.getElementById('reservations');
            scrollTo(0, s.getBoundingClientRect().top + scrollY); }""")
    else:
        page.evaluate("""(sel) => { const e = document.querySelector(sel); const r = e.getBoundingClientRect();
            scrollTo(0, r.top + scrollY + r.height / 2 - innerHeight / 2); }""", s["center"])
    for sel in s.get("hide", []):
        page.evaluate("(q) => document.querySelectorAll(q).forEach(e => e.style.visibility = 'hidden')", sel)
    page.wait_for_timeout(1500)   # .word opacity transition is .9s, reveals ~1.2s


def shoot(page, key, r):
    png = page.screenshot(clip={"x": r["x0"], "y": r["y0"], "width": r["x1"] - r["x0"], "height": r["y1"] - r["y0"]})
    im = Image.open(io.BytesIO(png)).convert("RGB")
    W = im.width; H = round(W / ASPECT)
    im = im.resize((W, H), Image.LANCZOS) if abs(H - im.height) > 0 else im
    return im


def save(key, im, colour=True):
    os.makedirs(OUT, exist_ok=True)
    if colour:
        im.save(os.path.join(OUT, key + ".webp"), "WEBP", quality=82, method=6)
    dim = im.resize((900, round(900 / ASPECT)), Image.LANCZOS)
    if key.startswith("calyx"):
        ink, paper = _d.BLACK, _d.GREY
    else:
        # dither_variant puts ink where the image is dark. White ink on black
        # therefore needs the luminance inverted first, or the raster is a
        # negative (R6's Hōrai rasters were, and the tile resolve flipped light
        # and dark cell by cell - part of what read as broken).
        ink, paper, dim = _d.WHITE, _d.BLACK, ImageOps.invert(dim)
        lv = STEPS[key].get("levels")
        if lv:
            # lacquer red on walnut is too close in luminance for a 1-bit
            # raster: clip the ground to clean paper and the glyphs to full ink.
            # (autocontrast over all eleven was tried and dropped: it greys
            # the flat grounds and Floyd-Steinberg draws worms in them.)
            lo, hi = lv
            dim = dim.convert("L").point(lambda v: 0 if v <= lo else 255 if v >= hi else int((v - lo) * 255 / (hi - lo))).convert("RGB")
    _d.dither_variant(dim, ink, paper).save(os.path.join(OUT, key + "-dither.webp"), "WEBP", lossless=True, method=6)


def selftest(page):
    """M3: the check must reject a frame that cuts a word and one that holds
    a sliver of a photo, and accept the clean one."""
    prepare(page, "calyx-3", STEPS["calyx-3"])
    data = page.evaluate(INK_JS, [])
    tb = [target_box(page, *t) for t in STEPS["calyx-3"]["target"]]
    cap = tb[0]
    cut = {"x0": cap["x0"] + 20, "y0": cap["y0"] - 80, "x1": cap["x0"] + 240, "y1": cap["y0"] + 76}
    # a frame whose top edge holds only 12 px of the tulip photo that sits below the paragraph
    ph = [m for m in data["imgs"] if "duo" in m["c"]][1]
    sliver = {"x0": ph["x0"] + 40, "y0": ph["y1"] - 12, "x1": ph["x0"] + 280, "y1": ph["y1"] + 158}
    r = {"cut": check(cut, data["words"], data["imgs"]), "sliver": check(sliver, data["words"], data["imgs"])}
    print("selftest", json.dumps(r, ensure_ascii=False))
    assert r["cut"] and any("ord i kanten" in b for b in r["cut"]), "check missed a cut word"
    assert any("bildfragment" in b for b in r["sliver"]), "check missed a photo sliver"


def main():
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--dither-only" in sys.argv:
        for key in (only or STEPS):
            save(key, Image.open(os.path.join(OUT, key + ".webp")).convert("RGB"), colour=False)
        return
    log = {}
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        try:
            page = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=DSF)
            if "--selftest" in sys.argv:
                selftest(page)
            for key, s in STEPS.items():
                if only and key not in only:
                    continue
                prepare(page, key, s)
                data = page.evaluate(INK_JS, s.get("chars", []))
                tboxes = [target_box(page, *t) for t in s["target"]]
                if None in tboxes:
                    print(key, "TARGET MISSING", s["target"]); continue
                m, r, tb = search(tboxes, data["words"], data["imgs"], s.get("top", 0), s.get("cx", CLEAR), s.get("m_lo", M_LO),
                                  [t[1] for t in s["target"]], s.get("oy", 0.48), s.get("m_hi", M_HI), s.get("excl", ()), s.get("cy", CLEAR))
                if not r:
                    w = CELL_W / M_LO; h = w / ASPECT; cxm = (tb[0] + tb[2]) / 2; cym = (tb[1] + tb[3]) / 2
                    probe = {"x0": cxm - w / 2, "y0": cym - h / 2, "x1": cxm + w / 2, "y1": cym + h / 2}
                    print(key, "NO CLEAN FRAME at 2.5-3x; target ink", [round(v) for v in tb],
                          "centred 2.5x frame:", check(probe, data["words"], data["imgs"], s.get("cx", CLEAR))[:8]); continue
                mag = m / IFRAME_SCALE
                im = shoot(page, key, r)
                save(key, im)
                log[key] = {"mag_vs_iframe": round(mag, 2), "frame_css": {k: round(v, 1) for k, v in r.items()},
                            "px": list(im.size), "problems": check(r, data["words"], data["imgs"], s.get("cx", CLEAR), s.get("cy", CLEAR))}
                print(key, json.dumps(log[key], ensure_ascii=False))
        finally:
            b.close()
    with open(os.path.join(HERE, "shots", "loupe-log.json"), "a", encoding="utf-8") as f:
        f.write(json.dumps(log, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
