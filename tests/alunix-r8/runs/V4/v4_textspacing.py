#!/usr/bin/env python3
"""WCAG 1.4.12 text spacing on V4, plus the 320x640 contact check.

    python tests/alunix-r8/browser_lock.py -- python tests/alunix-r8/runs/V4/v4_textspacing.py

For each size: load, finish the intro, inject the 1.4.12 overrides (line-height 1.5,
letter-spacing .12em, word-spacing .16em, paragraph spacing 2em), then jump to each act
(lenis.scrollTo immediate, then a real wheel nudge) and record:
  - clipped: text elements whose content overflows an ancestor with overflow hidden/clip
  - offscreen: visible text whose box leaves the viewport horizontally
  - overlap: pairs of text blocks in the same act whose boxes intersect
and save a screenshot per act. M3: the same check runs once on a deliberately broken
variant (a 40px-wide overflow:hidden box around the hero h1) and must report > 0.
"""
import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"
OUT = Path(__file__).parent / "shots" / "textspacing"
OUT.mkdir(parents=True, exist_ok=True)
CSS = """* { line-height: 1.5 !important; letter-spacing: .12em !important; word-spacing: .16em !important; }
p { margin-bottom: 2em !important; }"""
CHECK = r"""(scope) => {
  const vw = innerWidth, vh = innerHeight;
  const texts = [...document.querySelectorAll('h1,h2,h3,p,a,li,span.row,b')].filter(e => {
    const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < vh && cs.visibility !== 'hidden' && +cs.opacity > 0.05
      && e.textContent.trim() && !e.closest('[aria-hidden="true"]') && !e.closest('.frame');
  });
  const clipped = [], offscreen = [];
  const onTop = e => { const r = e.getBoundingClientRect();
    const x = Math.min(vw - 1, Math.max(0, r.left + Math.min(r.width / 2, 20))), y = Math.min(vh - 1, Math.max(0, r.top + r.height / 2));
    const t = document.elementFromPoint(x, y); return !!t && (e.contains(t) || t.contains(e)); };
  for (const e of texts) {
    let a = e;
    while (a && a !== document.body) {
      const cs = getComputedStyle(a);
      if (/(hidden|clip)/.test(cs.overflowX + cs.overflowY) && !a.classList.contains('stage')) {
        if (e.scrollWidth > a.clientWidth + 2 || a.scrollHeight > a.clientHeight + 2) { clipped.push(e.textContent.trim().slice(0, 40)); }
        break;
      }
      a = a.parentElement;
    }
    const r = e.getBoundingClientRect();
    if ((r.left < -1 || r.right > vw + 1) && !e.closest('.p-track')) offscreen.push(e.textContent.trim().slice(0, 40) + ` [${Math.round(r.left)}..${Math.round(r.right)}]`);
  }
  const blocks = texts.filter(e => /^(H1|H2|H3|P)$/.test(e.tagName) && onTop(e));
  const overlap = [];
  for (let i = 0; i < blocks.length; i++) for (let j = i + 1; j < blocks.length; j++) {
    const A = blocks[i], B = blocks[j];
    if (A.contains(B) || B.contains(A)) continue;
    const a = A.getBoundingClientRect(), b = B.getBoundingClientRect();
    const ix = Math.min(a.right, b.right) - Math.max(a.left, b.left), iy = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
    if (ix > 4 && iy > 4) overlap.push(A.textContent.trim().slice(0, 24) + ' × ' + B.textContent.trim().slice(0, 24));
  }
  return { clipped: [...new Set(clipped)], offscreen: [...new Set(offscreen)], overlap };
}"""
ACTS = [("hero", 0.1), ("thesis", 0.75), ("process", 0.0), ("process", 0.5), ("pkg", 0.7)]
res = {}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for W, H in [(1440, 900), (390, 844)]:
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.goto(URL, wait_until="load"); time.sleep(4.6)
        pg.add_style_tag(content=CSS); time.sleep(0.4)
        pg.evaluate("window.__v4.ScrollTrigger.refresh()"); time.sleep(0.6)
        pg.mouse.move(W - 4, H * 0.5)
        r = {}
        for act, prog in ACTS + [("examples", None), ("contact", None)]:
            if prog is None:
                sel = {"examples": "#exempel .decisions", "contact": "#kontakt .c-mail"}[act]
                pg.evaluate(f"window.__v4.lenis.scrollTo(document.querySelector('{sel}'), {{immediate:true, force:true, offset:-200}})")
            else:
                pg.evaluate(f"(()=>{{const st=window.__v4.ScrollTrigger.getById('{act}'); window.__v4.lenis.scrollTo(st.start+{prog}*(st.end-st.start),{{immediate:true,force:true}})}})()")
            time.sleep(0.5); pg.mouse.wheel(0, 30); time.sleep(1.4)
            key = f"{act}{'' if prog is None else '-' + str(prog)}"
            r[key] = pg.evaluate(CHECK, None)
            pg.screenshot(path=str(OUT / f"{W}-{key}.png"))
        res[f"{W}x{H}"] = r
        pg.close()
    # M3: broken variant must be caught
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(URL, wait_until="load"); time.sleep(4.6)
    pg.add_style_tag(content=".hero-h .r2 { display:block; width:40px; overflow:hidden; white-space:nowrap; } .hero-h .r2::after{content:''}")
    pg.evaluate("document.querySelector('.hero-h .r2').innerHTML = '<span style=\"display:inline-block\">' + document.querySelector('.hero-h .r2').textContent + '</span>'")
    time.sleep(0.3)
    res["broken-variant"] = pg.evaluate(CHECK, None)
    pg.close()
    # 320x640 contact
    pg = b.new_page(viewport={"width": 320, "height": 640})
    pg.goto(URL, wait_until="load"); time.sleep(4.6)
    pg.evaluate("window.__v4.lenis.scrollTo(document.querySelector('#kontakt'), {immediate:true, force:true})"); time.sleep(0.4)
    pg.mouse.wheel(0, 2000); time.sleep(2.5)
    res["320x640-contact"] = pg.evaluate(CHECK, None)
    res["320x640-hscroll"] = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
    pg.screenshot(path=str(OUT / "320-contact.png"))
    pg.evaluate("window.__v4.lenis.scrollTo(0, {immediate:true, force:true})"); time.sleep(1.2)
    pg.screenshot(path=str(OUT / "320-hero.png"))
    b.close()
(OUT / "textspacing.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps(res, indent=1, ensure_ascii=False))
