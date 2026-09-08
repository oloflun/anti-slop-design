"""Verification for K3: screenshots, console, overflow, frames. Run from repo root with server on :3103."""
import sys, json
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3103/tests/alunix-ab-r6/runs/A/K3/index.html"
OUT = "tests/alunix-ab-r6/runs/A/K3/shots"

OVERFLOW_JS = """
() => {
  const vw = document.documentElement.clientWidth;
  const bad = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0) continue;
    if (r.right > vw + 1 || r.left < -1) {
      const cs = getComputedStyle(el);
      if (el.closest('.card') || el.classList.contains('hero-photo') || el.closest('.hero-photo')) continue;
      bad.push({tag: el.tagName, cls: el.className && el.className.baseVal === undefined ? el.className : '', l: Math.round(r.left), r: Math.round(r.right)});
    }
  }
  return {vw, sw: document.documentElement.scrollWidth, bad: bad.slice(0, 12)};
}
"""

def run(step_mode):
    with sync_playwright() as p:
        b = p.chromium.launch()
        results = {}
        for (W, H, reduce, tag) in [(1440, 900, False, "1440"), (390, 844, False, "390"), (1440, 900, True, "rm"), (320, 700, False, "320"), (768, 1024, False, "768")]:
            ctx = b.new_context(viewport={"width": W, "height": H}, reduced_motion="reduce" if reduce else "no-preference", device_scale_factor=1)
            pg = ctx.new_page()
            logs = []
            pg.on("console", lambda m: logs.append((m.type, m.text)))
            pg.on("pageerror", lambda e: logs.append(("pageerror", str(e))))
            pg.goto(URL, wait_until="load"); pg.add_style_tag(content="html{scroll-behavior:auto !important}")
            pg.wait_for_timeout(2500)
            if tag in ("1440", "390", "rm"):
                pg.screenshot(path=f"{OUT}/{tag}-fold.png")
            geo = pg.evaluate("() => ({scene: document.getElementById('scene').offsetHeight, total: document.documentElement.scrollHeight, pinned: document.getElementById('scene').classList.contains('is-pinned')})")
            # scroll through in 300px steps
            total = geo["total"]
            y = 0
            sig = []
            while y < total:
                pg.evaluate(f"window.scrollTo(0,{y})")
                pg.wait_for_timeout(step_mode)
                y += 300
            pg.wait_for_timeout(600)
            if tag in ("1440", "390", "rm"):
                pg.screenshot(path=f"{OUT}/{tag}-full.png", full_page=True)
            # signature shots: three positions inside the pinned scene (1440 and 390)
            if tag in ("1440", "390"):
                pin = pg.evaluate("() => { const s=document.getElementById('scene'); return {top: s.offsetTop-56, h: s.offsetHeight-(innerHeight-56)}; }")
                for i, f in enumerate([0.18, 0.5, 0.82]):
                    yy = int(pin["top"] + pin["h"] * f)
                    pg.evaluate(f"window.scrollTo(0,{yy})")
                    pg.wait_for_timeout(900)
                    pg.screenshot(path=f"{OUT}/{tag}-sig-{i}.png")
                    sig.append(pg.evaluate("() => ({y: scrollY, sec: document.getElementById('cSec').textContent, pct: document.getElementById('cPct').textContent, fst: document.getElementById('fHorai').contentDocument.documentElement.scrollTop})"))
                # release moment + a bit
                yy = int(pin["top"] + pin["h"] + 140)
                pg.evaluate(f"window.scrollTo(0,{yy})"); pg.wait_for_timeout(900)
                pg.screenshot(path=f"{OUT}/{tag}-release.png")
                yy = int(pin["top"] + pin["h"] + 900)
                pg.evaluate(f"window.scrollTo(0,{yy})"); pg.wait_for_timeout(1200)
                pg.screenshot(path=f"{OUT}/{tag}-build.png")
                # open Utveckling via tab
                pg.click('.tab[data-tab="utveckling"]'); pg.wait_for_timeout(1500)
                pg.screenshot(path=f"{OUT}/{tag}-build-tab2.png")
            ov = pg.evaluate(OVERFLOW_JS)
            titles = pg.evaluate("() => [...document.querySelectorAll('iframe')].map(f => [f.title, f.hidden, f.contentDocument && f.contentDocument.title])")
            results[tag] = {"geo": geo, "overflow": ov, "titles": titles, "sig": sig, "logs": [l for l in logs if l[0] in ("error", "pageerror", "warning")]}
            ctx.close()
        b.close()
    print(json.dumps(results, indent=1, ensure_ascii=False))

if __name__ == "__main__":
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
