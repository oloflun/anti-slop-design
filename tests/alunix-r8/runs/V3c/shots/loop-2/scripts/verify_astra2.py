"""verify_astra2.py: verify Astra loop-2 fixes 1 and 3 against the live page.
Fix 1: --s1/--e1 and g[data-step=01] data-on in ?preview=process-05 (1440, 390); then
       measureAct re-run while scrolled (simulating load/resize after scroll).
Fix 3: li 01 opacity/transform at the process-1440 life-01 frame; li rects with and
       without the engine's sc-in reveal."""
import asyncio, json, sys
from playwright.async_api import async_playwright
sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"

JS_STATE = """() => { const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const g1 = p.querySelector('.process-sheet g[data-step="01"]');
  const stick = p.querySelector('.process-stick').getBoundingClientRect();
  return {scrollY: Math.round(scrollY), s1: cs.getPropertyValue('--s1').trim(), e1: cs.getPropertyValue('--e1').trim(),
    s2: cs.getPropertyValue('--s2').trim(), on01: g1.hasAttribute('data-on'), outlineDisplay: getComputedStyle(g1).display,
    stickTop: Math.round(stick.top), k1: cs.getPropertyValue('--k1').trim().slice(0,40)}; }"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for w, h in ((1440, 900), (390, 844)):
            pg = await b.new_page(viewport={"width": w, "height": h}, reduced_motion="reduce")
            await pg.goto(BASE + "?preview=process-05", wait_until="networkidle", timeout=60000)
            await pg.wait_for_timeout(1500)
            st = await pg.evaluate(JS_STATE)
            print(w, "preview-05 state:", json.dumps(st))
            # simulate a resize after scroll (fonts.ready -> resize -> measureAct)
            await pg.evaluate("dispatchEvent(new Event('resize'))"); await pg.wait_for_timeout(300)
            print(w, "after resize while scrolled:", json.dumps(await pg.evaluate(JS_STATE)))
            await pg.close()
            # fix 3: life frame 1 at this width
            pg = await b.new_page(viewport={"width": w, "height": h}, reduced_motion="reduce")
            await pg.goto(BASE, wait_until="networkidle", timeout=60000); await pg.wait_for_timeout(1500)
            box = await pg.evaluate("() => { const r = document.getElementById('process').getBoundingClientRect(); return {top: r.top + scrollY, h: r.height}; }")
            y = box["top"] - h + (box["h"] + h) * 1 / 11
            await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(700)
            r = await pg.evaluate("""() => { const li = document.querySelector('.process-steps li'); const cs = getComputedStyle(li); const ol = document.querySelector('.process-steps');
              return {liOpacity: cs.opacity, liTransform: cs.transform, olClass: ol.className, olOpacity: getComputedStyle(ol).opacity, liTop: Math.round(li.getBoundingClientRect().top)}; }""")
            print(w, "life-01 li01:", json.dumps(r))
            # rect contamination: li rects at load (before sc-in) vs after forcing sc-in
            await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(300)
            pre = await pg.evaluate("() => [...document.querySelectorAll('.process-steps li')].map(li => Math.round(li.getBoundingClientRect().top + scrollY))")
            await pg.evaluate("() => { const ol = document.querySelector('.process-steps'); ol.classList.add('sc-in'); [...ol.children].forEach(k => { k.style.transitionDelay = '0ms'; k.classList.add('sc-in'); }); }")
            await pg.wait_for_timeout(1200)
            post = await pg.evaluate("() => [...document.querySelectorAll('.process-steps li')].map(li => Math.round(li.getBoundingClientRect().top + scrollY))")
            print(w, "li tops before reveal:", pre, "after:", post, "delta:", [a - b for a, b in zip(post, pre)])
            await pg.close()
        await b.close()
asyncio.run(main())
