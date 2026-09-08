"""Extra checks: tab 3 loads Hyperborea, mid-morph frames, no-JS fallback, mobile fold with card."""
import json
from playwright.sync_api import sync_playwright
URL="http://127.0.0.1:3103/tests/alunix-ab-r6/runs/A/K3/index.html"; OUT="tests/alunix-ab-r6/runs/A/K3/shots"
with sync_playwright() as p:
    b=p.chromium.launch()
    # desktop: release morph frames + tab 3
    pg=b.new_page(viewport={"width":1440,"height":900}); errs=[]
    pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None); pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until="load"); pg.add_style_tag(content="html{scroll-behavior:auto !important}"); pg.wait_for_timeout(2000)
    rel=pg.evaluate("() => { const s=document.getElementById('scene'); return s.offsetTop-56 + s.offsetHeight-(innerHeight-56); }")
    for i,dy in enumerate([60,150,260]):
        pg.evaluate(f"window.scrollTo(0,{rel+dy})"); pg.wait_for_timeout(700); pg.screenshot(path=f"{OUT}/1440-morph-{i}.png", clip={"x":900,"y":0,"width":540,"height":420})
    # also check scrolling back up re-pins and the frame follows
    pg.evaluate(f"window.scrollTo(0,{rel-1200})"); pg.wait_for_timeout(900)
    back=pg.evaluate("() => ({pinned: document.getElementById('scene').classList.contains('is-pinned'), pct: document.getElementById('cPct').textContent, sec: document.getElementById('cSec').textContent})")
    pg.click('.tab[data-tab="system"]'); pg.wait_for_timeout(2500); pg.screenshot(path=f"{OUT}/1440-build-tab3.png")
    t3=pg.evaluate("() => [...document.querySelectorAll('#panelFrames iframe')].map(f => [f.dataset.site, f.hidden, f.contentDocument && f.contentDocument.title])")
    pg.evaluate("window.scrollTo(0, document.getElementById('paket').offsetTop - 300)"); pg.wait_for_timeout(600); pg.screenshot(path=f"{OUT}/1440-terms-entering.png")
    pg.evaluate("window.scrollTo(0, document.body.scrollHeight)"); pg.wait_for_timeout(900); pg.screenshot(path=f"{OUT}/1440-end.png")
    print("back-scroll", back); print("tab3 frames", t3); print("errors", errs)
    pg.close()
    # mobile fold with fixed card
    pg=b.new_page(viewport={"width":390,"height":844}); pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2000); pg.screenshot(path=f"{OUT}/390-fold.png")
    pg.add_style_tag(content="html{scroll-behavior:auto !important}")
    rel=pg.evaluate("() => { const s=document.getElementById('scene'); return s.offsetTop-56 + s.offsetHeight-(innerHeight-56); }")
    pg.evaluate(f"window.scrollTo(0,{rel+400})"); pg.wait_for_timeout(1000); pg.screenshot(path=f"{OUT}/390-after-release.png"); pg.close()
    # no-JS
    ctx=b.new_context(viewport={"width":1440,"height":900}, java_script_enabled=False); pg=ctx.new_page(); pg.goto(URL, wait_until="load"); pg.wait_for_timeout(1500)
    pg.screenshot(path=f"{OUT}/1440-nojs-full.png", full_page=True); print("nojs height", pg.evaluate("document.documentElement.scrollHeight")); ctx.close()
    b.close()
