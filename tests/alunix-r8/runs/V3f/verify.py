#!/usr/bin/env python3
"""V3f verification. Serve from repo root first:
  python skills/design/scripts/serve.py --port 3305 --root .
Then: python tests/alunix-r8/runs/V3f/verify.py
"""
import json
import os
import re
import sys
from collections import Counter
from bs4 import BeautifulSoup, Comment
from playwright.sync_api import sync_playwright

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
BASE = "http://127.0.0.1:3305"
URL = BASE + "/tests/alunix-r8/runs/V3f/index.html"
V3D = os.path.join(ROOT, "tests", "alunix-r8", "runs", "V3d", "index.html")
SHOTS_ROUND = os.environ.get("V3F_SHOTS_ROUND", "r2")
OUT_SHOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shots", SHOTS_ROUND)
os.makedirs(OUT_SHOTS, exist_ok=True)

VIEWPORTS = [390, 768, 1440, 1920]


def visible_text_set(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "title"]):
        tag.decompose()
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)):
        c.extract()
    for tag in soup.select('[aria-hidden="true"]'):
        tag.decompose()
    text = soup.get_text(separator="\n")
    lines = [re.sub(r"\s+", " ", l).strip() for l in text.split("\n")]
    lines = [l for l in lines if l]
    return lines


def copy_diff():
    """Membership AND occurrence-count check against V3d's visible text.

    A string is allowed in V3f only if it appears verbatim in V3d, and no
    more often in V3f than it does in V3d. Membership alone let a string
    that legitimately exists once in V3d (e.g. the contact h2, or the
    card-back "Alunix"/"Boka ett möte" strings) sneak into V3f a second or
    third time as long as SOME copy elsewhere in V3d also contained it -
    round 2's duplicate "Berätta om er verksamhet." heading is exactly
    that failure mode, and count parity is what catches it.
    """
    with open(V3D, encoding="utf-8") as f:
        v3d_html = f.read()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"), encoding="utf-8") as f:
        v3f_html = f.read()
    v3d_lines = [l.replace("‑", "-") for l in visible_text_set(v3d_html)]
    v3f_lines = [l.replace("‑", "-") for l in visible_text_set(v3f_html)]
    v3d_counts = Counter(v3d_lines)
    v3f_counts = Counter(v3f_lines)

    missing = [l for l in v3f_counts if l not in v3d_counts]
    over_count = []
    for l, n in v3f_counts.items():
        cap = v3d_counts.get(l, 0)
        if n > cap:
            over_count.append({"text": l, "v3f_count": n, "v3d_count": cap})

    return {
        "v3f_line_count": len(v3f_lines),
        "v3d_line_count": len(v3d_lines),
        "not_found_in_v3d": missing,
        "over_count_vs_v3d": over_count,
        "passed": not missing and not over_count,
    }


def emdash_check():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html"), encoding="utf-8") as f:
        html = f.read()
    lines = visible_text_set(html)
    hits = [l for l in lines if "—" in l]
    return hits


def run():
    report = {"viewports": {}, "copy_diff": None, "emdash": None}
    report["copy_diff"] = copy_diff()
    report["emdash"] = emdash_check()

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # explicit hero-fit checks at the two mandated desktop sizes
        hero_fit = {}
        for (w, h) in [(1440, 900), (1280, 800)]:
            page = browser.new_page(viewport={"width": w, "height": h})
            page.goto(URL, wait_until="networkidle", timeout=30000)
            page.wait_for_timeout(300)
            bottom = page.evaluate("document.querySelector('.hero-stage').getBoundingClientRect().bottom")
            overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            hero_fit[f"{w}x{h}"] = {"hero_stage_bottom": bottom, "viewport_h": h, "fits": bottom <= h + 1, "overflow_px": overflow}
            page.close()
        report["hero_fit_1440x900_1280x800"] = hero_fit

        for vw in VIEWPORTS:
            page = browser.new_page(viewport={"width": vw, "height": 900})
            page.goto(URL, wait_until="networkidle", timeout=30000)
            page.wait_for_timeout(400)

            data = {}
            data["scroll_width"] = page.evaluate("document.documentElement.scrollWidth")
            data["client_width"] = page.evaluate("document.documentElement.clientWidth")
            data["overflow_px"] = data["scroll_width"] - data["client_width"]
            data["page_height"] = page.evaluate("document.documentElement.scrollHeight")

            # hero bottom vs viewport at load (first view)
            hero_bottom = page.evaluate("""() => {
                const h = document.querySelector('.hero-stage');
                if (!h) return null;
                const r = h.getBoundingClientRect();
                return r.bottom;
            }""")
            data["hero_bottom_vs_vh"] = hero_bottom
            data["viewport_h"] = 900

            # image-cell area share at this viewport
            area = page.evaluate("""() => {
                const vw = document.documentElement.clientWidth;
                let total = document.documentElement.scrollHeight * vw;
                let imgArea = 0, imgAreaStrict = 0;
                document.querySelectorAll('.img-cell, .hero-oh, .hero-nv').forEach(el => {
                    const r = el.getBoundingClientRect();
                    const a = Math.max(0, r.width) * Math.max(0, r.height);
                    imgArea += a; imgAreaStrict += a;
                });
                document.querySelectorAll('.prov-embed-cell').forEach(el => {
                    const r = el.getBoundingClientRect();
                    imgArea += Math.max(0, r.width) * Math.max(0, r.height);
                });
                return {total, imgArea, share: imgArea/total, share_strict: imgAreaStrict/total};
            }""")
            data["image_area_share"] = area["share"]
            data["image_area_share_strict_no_iframe"] = area["share_strict"]

            # distinct cell background colours
            colours = page.evaluate("""() => {
                const set = new Set();
                document.querySelectorAll('.cell, .hero-cell, .tes-line, .process-row-item, .prov-row-item, .pris-tier, .pris-lead, .footer-cell').forEach(el => {
                    const bg = getComputedStyle(el).backgroundColor;
                    set.add(bg);
                });
                return Array.from(set);
            }""")
            data["distinct_cell_colours"] = len(colours)
            data["colours_sample"] = colours[:12]

            # scroll to bottom, in steps, to trigger mounts
            total_h = page.evaluate("document.documentElement.scrollHeight")
            steps = 10
            for i in range(steps + 1):
                page.evaluate(f"window.scrollTo(0, {int(total_h * i / steps)})")
                page.wait_for_timeout(120)

            mounted = page.evaluate("""() => {
                const frames = Array.from(document.querySelectorAll('iframe'));
                return frames.map(f => ({title: f.title, src: f.src, hasSrc: !!f.src && f.src !== 'about:blank'}));
            }""")
            data["iframes_after_scroll"] = mounted

            # jump directly via anchor to test the non-IO mount path
            page.evaluate("window.scrollTo(0,0)")
            page.wait_for_timeout(100)
            # R5: #case-horai was removed (B: chooser + pinned showcase).
            # #showcase is the equivalent jump target; the Hoerai iframe
            # only mounts once selected (see verify_motion.py's showcase_check
            # for the full click/keyboard/anchor-hit coverage of that flow).
            page.evaluate("document.getElementById('showcase').scrollIntoView()")
            page.wait_for_timeout(300)
            mounted_after_jump = page.evaluate("""() => {
                const frames = Array.from(document.querySelectorAll('iframe'));
                return frames.map(f => ({title: f.title, hasSrc: !!f.src && f.src !== 'about:blank'}));
            }""")
            data["iframes_after_jump_to_showcase"] = mounted_after_jump

            data["scroll_width_after"] = page.evaluate("document.documentElement.scrollWidth")
            data["client_width_after"] = page.evaluate("document.documentElement.clientWidth")
            data["overflow_px_after_scroll"] = data["scroll_width_after"] - data["client_width_after"]

            if vw in (1440, 390):
                page.evaluate("window.scrollTo(0,0)")
                page.wait_for_timeout(200)
                page.screenshot(path=os.path.join(OUT_SHOTS, f"hero-{vw}.png"))
                page.screenshot(path=os.path.join(OUT_SHOTS, f"full-{vw}.png"), full_page=True)

            # R2 defect checks -------------------------------------------------
            page.evaluate("window.scrollTo(0,0)")
            page.wait_for_timeout(150)

            # defect 1: card size + contrast (light stock, not black-on-black)
            card = page.evaluate("""() => {
                const a = document.querySelector('.card-anchor');
                const front = document.querySelector('.face--front');
                if (!a || !front) return null;
                const r = a.getBoundingClientRect();
                const cs = getComputedStyle(front);
                return {w: r.width, h: r.height, bg: cs.backgroundColor};
            }""")
            data["card"] = card

            # defect 2: mobile hero must not leave a dead trailing viewport of
            # solid black beyond the stage's own natural content height.
            hero_mobile = page.evaluate("""() => {
                const wrap = document.getElementById('hero');
                const stage = document.querySelector('.hero-stage');
                if (!wrap || !stage) return null;
                return {wrapH: wrap.offsetHeight, stageH: stage.offsetHeight, deadSpace: wrap.offsetHeight - stage.offsetHeight};
            }""")
            data["hero_wrap_vs_stage"] = hero_mobile

            # defect 3 (R2, kept as a regression guard) -> R5: the thumb row
            # is now the case-picker's two buttons; the word must still not
            # be covered by them.
            case_check = page.evaluate("""() => {
                const word = document.querySelector('.case-word-cell');
                const picker = document.querySelector('.case-picker-cell');
                if (!word || !picker) return null;
                const wr = word.getBoundingClientRect(), tr = picker.getBoundingClientRect();
                return {wordBottom: wr.bottom, pickerTop: tr.top, overlap: wr.bottom > tr.top + 1};
            }""")
            data["exempelcase_word_vs_picker"] = case_check

            # defect 4 (R2) -> R5 §C: the kontakt headline (now in the ÖV
            # quadrant, not a giant image-cell overlay) must fit inside its
            # own cell and clear the sticky topline, exactly once in the DOM.
            kontakt_check = page.evaluate("""() => {
                const heads = Array.from(document.querySelectorAll('#kontakt h2'));
                const head = document.querySelector('.kontakt-q--ov .headline-40');
                const cell = document.querySelector('.kontakt-q--ov');
                if (!head || !cell) return {count: heads.length};
                const gr = head.getBoundingClientRect(), cr = cell.getBoundingClientRect();
                return {
                  count: heads.length,
                  fitsWithinCell: gr.top >= cr.top - 1 && gr.bottom <= cr.bottom + 1 && gr.left >= cr.left - 1 && gr.right <= cr.right + 1,
                  clearsTopline: gr.top >= 48 - 1
                };
            }""")
            data["kontakt_heading"] = kontakt_check

            # defect 5 (R2) -> R5 §C: the card now sits on the crossing of
            # the heron-mirrored quadrant; check it renders at a sane size
            # and the back's two links exist in the DOM (visibility/inert
            # state is covered by verify_motion.py's kontakt_check).
            kontakt_card = page.evaluate("""() => {
                const anchor = document.querySelector('.kontakt-card-anchor');
                const back = document.querySelector('#kontaktCardBack');
                const links = back ? back.querySelectorAll('a') : [];
                if (!anchor || !back) return null;
                const r = anchor.getBoundingClientRect();
                return {cardVisible: r.width > 0 && r.height > 0, backLinkCount: links.length};
            }""")
            data["kontakt_card_column"] = kontakt_card

            # defect 6: pris tiers must be readable (not a truncated sliver)
            # next to a big empty area.
            pris_check = page.evaluate("""() => {
                const tiers = Array.from(document.querySelectorAll('.pris-lead, .pris-tier-a, .pris-tier-b'));
                const vw = document.documentElement.clientWidth;
                return tiers.map(t => {
                    const r = t.getBoundingClientRect();
                    return {width: r.width, widthShare: r.width / vw};
                });
            }""")
            data["pris_tier_widths"] = pris_check

            report["viewports"][vw] = data
            page.close()
        browser.close()

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verify-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    sys.stdout.buffer.write(json.dumps(report, indent=2, ensure_ascii=False)[:8000].encode("utf-8"))
    print("\nFull report:", out_path)


if __name__ == "__main__":
    run()
