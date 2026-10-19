"""diagA2.py <out-dir>: (1) prove the frame fix with the page's own iframe-observer
disabled (observe() on an IFRAME target becomes a no-op; a wrapper-observer does the
mount/sleep instead); reader walk, back to Calyx, at Horai, back to top.
(2) extra ground-drift images at the giant stop for mix-40 and multiply-62.
(3) 390: same frame check (reader walk) with and without the fix."""
import asyncio, io, json, sys
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"

FIX_INIT = r"""
(() => {
  const Orig = window.IntersectionObserver;
  const origObserve = Orig.prototype.observe;
  Orig.prototype.observe = function(t){ if (t && t.tagName === 'IFRAME') return; return origObserve.call(this, t); };
  addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
      const wraps = [...document.querySelectorAll('.frame-wrap')];
      const io2 = new Orig(es => {
        for (const e of es){
          const w = e.target, f = w.querySelector('iframe');
          if (e.isIntersecting){
            w.classList.remove('is-asleep');
            if (f.hasAttribute('data-src')){ f.src = f.getAttribute('data-src'); f.removeAttribute('data-src'); }
          } else if (!f.hasAttribute('data-src')) { w.classList.add('is-asleep'); }
        }
      }, {rootMargin: '40% 0px'});
      wraps.forEach(w => origObserve.call(io2, w));
      window.__fixApplied = true;
    }, 50);
  });
})();
"""

JS_FRAMES = r"""
() => [...document.querySelectorAll('.frame-wrap')].map(w => {
  const f = w.querySelector('iframe'); const r = w.getBoundingClientRect();
  return {wrap: w.className.replace('frame-wrap ', ''), top: Math.round(r.top), bottom: Math.round(r.bottom),
          cv: getComputedStyle(w).contentVisibility, src: !!f.getAttribute('src'), dataSrc: f.hasAttribute('data-src'), scrollY: Math.round(scrollY)};
})
"""

async def walk(pg, ys, wait):
    log = []
    for y in ys:
        await pg.evaluate(f"window.scrollTo(0,{y})")
        await pg.wait_for_timeout(wait)
        log.append({"y": y, "frames": await pg.evaluate(JS_FRAMES)})
    return log

async def run(b, w, h, tag, fix, out, res):
    pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
    if fix:
        await pg.add_init_script(FIX_INIT)
    await pg.goto(BASE, wait_until="networkidle", timeout=60000)
    await pg.wait_for_timeout(1200)
    g = await pg.evaluate("() => { const r = s => { const b = document.querySelector(s).getBoundingClientRect(); return {top: Math.round(b.top+scrollY), h: Math.round(b.height)}; }; return {stagger: r('.stagger'), calyx: r('.calyx-wrap'), horai: r('.horai-wrap'), process: r('#process')}; }")
    key = f"{tag}-{'fix' if fix else 'r7'}"
    ys = list(range(g["stagger"]["top"] - h, g["process"]["top"], 300))
    res[key + "-walk"] = await walk(pg, ys, 250)
    await pg.wait_for_timeout(2500)
    res[key + "-final"] = await pg.evaluate(JS_FRAMES)
    yc = g["calyx"]["top"] - (h - g["calyx"]["h"]) / 2
    await pg.evaluate(f"window.scrollTo(0,{yc})"); await pg.wait_for_timeout(3000)
    res[key + "-calyx"] = await pg.evaluate(JS_FRAMES)
    await pg.screenshot(path=str(out / f"A2-{key}-calyx.png"))
    yh = g["horai"]["top"] - (h - g["horai"]["h"]) / 2
    await pg.evaluate(f"window.scrollTo(0,{yh})"); await pg.wait_for_timeout(3000)
    res[key + "-horai"] = await pg.evaluate(JS_FRAMES)
    await pg.screenshot(path=str(out / f"A2-{key}-horai.png"))
    await pg.evaluate("window.scrollTo(0,0)"); await pg.wait_for_timeout(1500)
    res[key + "-top"] = await pg.evaluate(JS_FRAMES)
    res[key + "-resources"] = await pg.evaluate("() => performance.getEntriesByType('resource').map(e => e.name).filter(n => /sites\\/|\\/null$/.test(n))")
    await pg.close()

async def main(out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for fix in (False, True):
            await run(b, 1440, 900, "1440", fix, out, res)
            await run(b, 390, 844, "390", fix, out, res)
        # extra ground images at the giant stop
        pg = await b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1, reduced_motion="reduce")
        await pg.goto(BASE, wait_until="networkidle", timeout=60000); await pg.wait_for_timeout(1500)
        gtop = await pg.evaluate("document.querySelector('.panel-giant').getBoundingClientRect().top + scrollY")
        ttop = await pg.evaluate("() => { const b = document.querySelector('.panel-thesis').getBoundingClientRect(); return b.top + scrollY - (900 - b.height)/2; }")
        for name, css in (("mix-40", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 40%,transparent) !important}"),
                          ("multiply-62", ".ground::after{mix-blend-mode:multiply !important}"),
                          ("mix-28", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 28%,transparent) !important}"),
                          ("mix-34", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 34%,transparent) !important}")):
            hnd = await pg.add_style_tag(content=css)
            for sname, y in (("giant", gtop - 200), ("thesis", ttop)):
                await pg.evaluate(f"window.scrollTo(0,{y})"); await pg.wait_for_timeout(500)
                shot = await pg.screenshot()
                im = Image.open(io.BytesIO(shot)).convert("RGB")
                res[f"B2-{name}-{sname}"] = {"gutter": im.getpixel((720, 450)), "rightMargin": im.getpixel((1420, 850)), "left": im.getpixel((20, 450))}
                im.save(out / f"B2-{name}-{sname}.png")
            await hnd.evaluate("e => e.remove()")
        await pg.close()
        await b.close()
    (out / "diagA2.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    for k, v in res.items():
        if k.endswith("-walk"):
            asleep_in_view = [s for s in v for f in s["frames"] if f["top"] < (900 if k.startswith("1440") else 844) and f["bottom"] > 0 and "is-asleep" in f["wrap"]]
            print(k, "stops with an asleep wrapper in view:", len(asleep_in_view), "of", len(v))
        else:
            print(k, json.dumps(v))

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
