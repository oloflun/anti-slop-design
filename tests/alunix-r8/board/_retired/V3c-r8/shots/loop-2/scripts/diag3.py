"""diag3.py <out-dir>: loop-2 diagnostics for the lead's three R7 findings.

A. Frames do not wake: log every IntersectionObserver entry for the two iframes
   (init script wraps the IO callback), walk the page two ways (stepwise like a
   reader, and the lead's jump sequence), record wrapper class / content-visibility
   / iframe src at each stop; then prove the hypothesis in-page (observe the
   wrapper instead of the iframe) and re-walk.
B. Ground drift: sample raw-ground pixels outside the panels at five scroll stops,
   at the current tone strength (62%) and at candidate strengths, plus the
   grayscale-only baseline.
C. Giant headline: width of the word VARUMÄRKE. vs the text column at candidate
   sizes / tracking, hyphens off.
Plus the loop-1 geometry block (diag.py JS_GEOM) so the plans have fresh numbers.
"""
import asyncio, io, json, sys
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"

IO_LOG_INIT = r"""
(() => {
  window.__ioLog = [];
  const Orig = window.IntersectionObserver;
  window.IntersectionObserver = function(cb, opts){
    const wrapped = function(entries, obs){
      for (const e of entries){
        if (e.target.tagName === 'IFRAME' || (e.target.classList && e.target.classList.contains('frame-wrap'))){
          window.__ioLog.push({t: Math.round(performance.now()), tag: e.target.tagName,
            cls: e.target.className || '', title: e.target.title || '', inter: e.isIntersecting,
            ratio: +e.intersectionRatio.toFixed(3), top: Math.round(e.boundingClientRect.top),
            h: Math.round(e.boundingClientRect.height), scrollY: Math.round(scrollY)});
        }
      }
      return cb(entries, obs);
    };
    return new Orig(wrapped, opts);
  };
  window.IntersectionObserver.prototype = Orig.prototype;
})();
"""

JS_FRAMES = r"""
() => [...document.querySelectorAll('.frame-wrap')].map(w => {
  const f = w.querySelector('iframe'); const r = w.getBoundingClientRect(); const fr = f.getBoundingClientRect();
  return {wrap: w.className.replace('frame-wrap ', ''), top: Math.round(r.top), bottom: Math.round(r.bottom),
          iframeTop: Math.round(fr.top), iframeH: Math.round(fr.height),
          cv: getComputedStyle(w).contentVisibility, src: !!f.getAttribute('src'), dataSrc: f.hasAttribute('data-src'),
          visible: f.__visible, pending: f.__pending, scrollY: Math.round(scrollY)};
})
"""

JS_GEOM = r"""
() => {
  const q = s => document.querySelector(s);
  const r = e => { const b = e.getBoundingClientRect(); return {top: Math.round(b.top+scrollY), left: Math.round(b.left), w: Math.round(b.width), h: Math.round(b.height)}; };
  const cs = (s, p) => getComputedStyle(q(s)).getPropertyValue(p);
  const out = {};
  out.docH = document.documentElement.scrollHeight;
  out.hero = r(q('section.hero'));
  out.stagger = r(q('.stagger'));
  out.thesis = r(q('.panel-thesis'));
  out.giant = r(q('.panel-giant'));
  out.giantH2 = r(q('.giant'));
  out.calyx = r(q('.calyx-fig'));
  out.calyxWrap = r(q('.calyx-wrap'));
  out.horai = r(q('.horai-fig'));
  out.horaiWrap = r(q('.horai-wrap'));
  out.price = r(q('.price'));
  out.process = r(q('#process'));
  out.processGrid = r(q('.process-grid'));
  out.processStick = r(q('.process-stick'));
  out.principles = r(q('#principer'));
  out.close = r(q('footer.close'));
  out.mailto = r(q('.close-mailto'));
  out.giantFont = cs('.giant', 'font-size');
  out.giantRects = q('.giant').getClientRects().length;
  out.giantLines = Math.round(q('.giant').getBoundingClientRect().height / (parseFloat(cs('.giant','font-size')) * 0.96));
  out.priceBg = cs('.price', 'background-color');
  out.stepVars = {};
  for (let i = 1; i <= 7; i++) { out.stepVars['s'+i] = cs('#process','--s'+i).trim(); out.stepVars['e'+i] = cs('#process','--e'+i).trim(); }
  return out;
}
"""

JS_WORD = r"""
(cfg) => {
  const g = document.querySelector('.giant');
  const head = g.parentNode;
  const colW = head.getBoundingClientRect().width;
  const out = {colW: +colW.toFixed(1), rows: []};
  const probe = document.createElement('span');
  probe.textContent = 'VARUMÄRKE.';
  probe.style.cssText = 'position:absolute;white-space:nowrap;visibility:hidden;font-family:' + getComputedStyle(g).fontFamily + ';font-weight:700;text-transform:uppercase;';
  document.body.appendChild(probe);
  for (const fs of cfg.sizes){
    for (const ls of cfg.tracks){
      probe.style.fontSize = fs + 'px'; probe.style.letterSpacing = ls + 'em';
      const w = probe.getBoundingClientRect().width;
      out.rows.push({fs, ls, wordW: +w.toFixed(1), fits: w <= colW});
    }
  }
  probe.remove();
  // actual render at candidate sizes with hyphens off: lines and overflow
  out.render = [];
  const saved = g.style.cssText;
  for (const fs of cfg.sizes){
    g.style.fontSize = fs + 'px'; g.style.hyphens = 'manual'; g.style.overflowWrap = 'normal';
    const r = g.getBoundingClientRect();
    const lines = Math.round(r.height / (fs * 0.96));
    const over = g.scrollWidth > g.clientWidth + 1;
    out.render.push({fs, lines, h: +r.height.toFixed(1), overflow: over, text: g.innerText.replace(/\n/g,' / ')});
  }
  g.style.cssText = saved;
  return out;
}
"""

def px(png_bytes, x, y):
    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    return im.getpixel((x, y))

def chroma(c):
    return max(c) - min(c)

async def frames_walk(pg, label, ys, wait):
    log = []
    for y in ys:
        await pg.evaluate(f"window.scrollTo(0,{y})")
        await pg.wait_for_timeout(wait)
        st = await pg.evaluate(JS_FRAMES)
        log.append({"y": y, "frames": st})
    return log

async def main(out_dir):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)

        # ---------- geometry 1440 / 390
        for w, h, tag in ((1440, 900, "1440"), (390, 844, "390")):
            pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce")
            await pg.goto(BASE, wait_until="networkidle", timeout=60000)
            await pg.wait_for_timeout(1500)
            res["geom" + tag] = await pg.evaluate(JS_GEOM)
            await pg.close()
        g = res["geom1440"]

        # ---------- A. frames: IO log, reader walk (1440)
        pg = await b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        await pg.add_init_script(IO_LOG_INIT)
        await pg.goto(BASE, wait_until="networkidle", timeout=60000)
        await pg.wait_for_timeout(1200)
        top = g["stagger"]["top"] - 900
        ys = list(range(int(top), int(g["process"]["top"]), 300))
        res["A_reader_walk"] = await frames_walk(pg, "reader", ys, 250)
        await pg.wait_for_timeout(3000)
        res["A_reader_final"] = await pg.evaluate(JS_FRAMES)
        res["A_reader_iolog"] = await pg.evaluate("window.__ioLog")
        # scroll back up so Calyx is centred and wait: does it wake?
        yc = g["calyxWrap"]["top"] - (900 - g["calyxWrap"]["h"]) / 2
        await pg.evaluate(f"window.scrollTo(0,{yc})")
        await pg.wait_for_timeout(3000)
        res["A_reader_back_to_calyx"] = await pg.evaluate(JS_FRAMES)
        await pg.screenshot(path=str(out / "A-reader-back-to-calyx.png"))
        await pg.close()

        # ---------- A2. lead's jump sequence (1440)
        pg = await b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        await pg.add_init_script(IO_LOG_INIT)
        await pg.goto(BASE, wait_until="networkidle", timeout=60000)
        await pg.wait_for_timeout(1000)
        res["A_jump_walk"] = await frames_walk(pg, "jump", [3200, 3600, 4100, 4600], 400)
        await pg.wait_for_timeout(4000)
        res["A_jump_final"] = await pg.evaluate(JS_FRAMES)
        res["A_jump_iolog"] = await pg.evaluate("window.__ioLog")
        await pg.screenshot(path=str(out / "A-jump-4600.png"))
        # hypothesis test: an IO whose target sits inside a content-visibility:hidden
        # wrapper never reports intersecting again. Prove: force is-asleep on a mounted
        # wrapper while it is on screen, then observe the iframe fresh.
        res["A_cv_hidden_blind"] = await pg.evaluate(r"""
        () => new Promise(resolve => {
          const w = document.querySelector('.horai-wrap'); const f = w.querySelector('iframe');
          w.classList.add('is-asleep');
          const seen = [];
          const io = new IntersectionObserver(es => { es.forEach(e => seen.push({target: e.target.tagName, inter: e.isIntersecting, ratio: +e.intersectionRatio.toFixed(3), h: Math.round(e.boundingClientRect.height)})); }, {rootMargin: '40% 0px'});
          io.observe(f); io.observe(w);
          setTimeout(() => { io.disconnect(); resolve({wrapTop: Math.round(w.getBoundingClientRect().top), seen}); }, 600);
        })""")
        await pg.close()

        # ---------- A3. proposed fix proven in-page: observe the wrapper, not the iframe
        pg = await b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
        await pg.add_init_script(IO_LOG_INIT)
        await pg.add_init_script(r"""
        addEventListener('DOMContentLoaded', () => {
          // shadow the page's own observer: replace its logic by observing the wrapper.
          setTimeout(() => {
            const wraps = [...document.querySelectorAll('.frame-wrap')];
            const io2 = new IntersectionObserver(es => {
              for (const e of es){
                const w = e.target, f = w.querySelector('iframe');
                if (e.isIntersecting){
                  w.classList.remove('is-asleep');
                  if (f.hasAttribute('data-src')){ f.src = f.getAttribute('data-src'); f.removeAttribute('data-src'); }
                } else if (!f.hasAttribute('data-src')) { w.classList.add('is-asleep'); }
              }
            }, {rootMargin: '40% 0px'});
            wraps.forEach(w => io2.observe(w));
            window.__fixApplied = true;
          }, 50);
        });
        """)
        await pg.goto(BASE, wait_until="networkidle", timeout=60000)
        await pg.wait_for_timeout(1200)
        res["A_fix_applied"] = await pg.evaluate("!!window.__fixApplied")
        res["A_fix_reader_walk"] = await frames_walk(pg, "fix", ys, 250)
        await pg.wait_for_timeout(2500)
        res["A_fix_final"] = await pg.evaluate(JS_FRAMES)
        await pg.evaluate(f"window.scrollTo(0,{yc})")
        await pg.wait_for_timeout(3000)
        res["A_fix_back_to_calyx"] = await pg.evaluate(JS_FRAMES)
        await pg.screenshot(path=str(out / "A-fix-back-to-calyx.png"))
        yh = g["horaiWrap"]["top"] - (900 - g["horaiWrap"]["h"]) / 2
        await pg.evaluate(f"window.scrollTo(0,{yh})")
        await pg.wait_for_timeout(3000)
        res["A_fix_at_horai"] = await pg.evaluate(JS_FRAMES)
        await pg.screenshot(path=str(out / "A-fix-at-horai.png"))
        # sleep still works: go far away and check
        await pg.evaluate("window.scrollTo(0,0)")
        await pg.wait_for_timeout(1500)
        res["A_fix_asleep_at_top"] = await pg.evaluate(JS_FRAMES)
        await pg.close()

        # ---------- B. ground drift pixels (1440)
        pg = await b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1, reduced_motion="reduce")
        await pg.goto(BASE, wait_until="networkidle", timeout=60000)
        await pg.wait_for_timeout(1500)
        stops = {
            "fold": 0,
            "thesis": g["thesis"]["top"] - (900 - g["thesis"]["h"]) / 2,
            "giant": g["giant"]["top"] - 200,
            "calyx": g["calyxWrap"]["top"] - 200,
            "price": g["price"]["top"] - 200,
        }
        pts = {"gutter": (720, 450), "rightMargin": (1420, 850), "leftMargin": (20, 450)}
        variants = [
            ("current-62", ""),
            ("baseline-gray", ".ground::after{display:none !important}"),
            ("mix-40", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 40%,transparent) !important}"),
            ("mix-28", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 28%,transparent) !important}"),
            ("mix-20", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 20%,transparent) !important}"),
            ("mix-14", ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 14%,transparent) !important}"),
            ("softlight-62", ".ground::after{mix-blend-mode:soft-light !important}"),
            ("multiply-62", ".ground::after{mix-blend-mode:multiply !important}"),
        ]
        B = {}
        for name, css in variants:
            handle = None
            if css:
                handle = await pg.add_style_tag(content=css)
            rows = {}
            for sname, y in stops.items():
                await pg.evaluate(f"window.scrollTo(0,{y})")
                await pg.wait_for_timeout(500)
                canvas = await pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--sc-canvas').trim()")
                shot = await pg.screenshot()
                rows[sname] = {"scrollY": round(y), "canvas": canvas}
                for pn, (x, yy) in pts.items():
                    c = px(shot, x, yy)
                    rows[sname][pn] = {"rgb": c, "chroma": chroma(c), "mean": round(sum(c) / 3)}
                if name in ("current-62", "baseline-gray", "mix-28", "mix-20"):
                    Image.open(io.BytesIO(shot)).save(out / f"B-{name}-{sname}.png")
            B[name] = rows
            if handle is not None:
                await handle.evaluate("e => e.remove()")
        res["B_ground"] = B
        # deltas fold vs thesis per variant (gutter point is on the card at fold; use rightMargin)
        res["B_summary"] = {}
        for name, rows in B.items():
            f = rows["fold"]["rightMargin"]["rgb"]; t = rows["thesis"]["rightMargin"]["rgb"]; gi = rows["giant"]["rightMargin"]["rgb"]
            res["B_summary"][name] = {"fold": f, "thesis": t, "giant": gi,
                                      "delta_fold_thesis_max": max(abs(a - b) for a, b in zip(f, t)),
                                      "chroma_thesis": chroma(t), "chroma_giant": chroma(gi),
                                      "thesis_gutter": rows["thesis"]["gutter"]["rgb"], "giant_gutter": rows["giant"]["gutter"]["rgb"]}
        # ---------- C. giant word widths (same page, scroll to giant)
        await pg.evaluate(f"window.scrollTo(0,{stops['giant']})")
        await pg.wait_for_timeout(400)
        res["C_giant"] = await pg.evaluate(JS_WORD, {"sizes": [96, 92, 90, 88, 86, 84, 80, 76.8], "tracks": [-0.03, -0.04, -0.05]})
        res["C_giant_pad"] = await pg.evaluate("() => { const p = document.querySelector('.panel-giant'); const cs = getComputedStyle(p); return {panelW: p.getBoundingClientRect().width, padL: cs.paddingLeft, padR: cs.paddingRight, colRightW: document.querySelector('.col-right').getBoundingClientRect().width, gap: getComputedStyle(document.querySelector('.stagger')).gap}; }")
        await pg.close()
        await b.close()
    (out / "diag3.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    # compact print
    print("=== A reader final:", json.dumps(res["A_reader_final"]))
    print("=== A reader back to calyx:", json.dumps(res["A_reader_back_to_calyx"]))
    print("=== A reader IO log:", json.dumps(res["A_reader_iolog"]))
    print("=== A jump final:", json.dumps(res["A_jump_final"]))
    print("=== A jump IO log:", json.dumps(res["A_jump_iolog"]))
    print("=== A cv-hidden blind test:", json.dumps(res["A_cv_hidden_blind"]))
    print("=== A fix applied:", res["A_fix_applied"])
    print("=== A fix final:", json.dumps(res["A_fix_final"]))
    print("=== A fix back to calyx:", json.dumps(res["A_fix_back_to_calyx"]))
    print("=== A fix at horai:", json.dumps(res["A_fix_at_horai"]))
    print("=== A fix asleep at top:", json.dumps(res["A_fix_asleep_at_top"]))
    print("=== B summary:", json.dumps(res["B_summary"]))
    print("=== C giant:", json.dumps(res["C_giant"], ensure_ascii=False))
    print("=== C giant pad:", json.dumps(res["C_giant_pad"]))
    print("=== geom1440:", json.dumps(res["geom1440"]))
    print("=== geom390:", json.dumps(res["geom390"]))

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
