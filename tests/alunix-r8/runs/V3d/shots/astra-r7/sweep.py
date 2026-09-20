"""astra-r7 sweeps, mouse.wheel only.
thesis: fina hjulsteg genom #tes (ner och upp), per bildruta: vilka .ts som har synlig yta
  (clip-path-fönstret räknat ur aktens --sc-ps med sidans egen formel) och överlapp i y
  mellan synliga fönster; skärmbild av värsta bildrutan per övergång.
cases: hjul ner genom #case-calyx och #case-horai och tillbaka, per bildruta scrollY, aktens
  --sc-ps, ramens contentWindow.scrollY, samma .cs-mått; monotonitet och fram/bak-avvikelse.
whole: hjul 150 px från topp till botten, en bild per steg (kontaktark) + rubrikkollisioner
  via elementFromPoint + horisontell scroll.
Anrop: python sweep.py <mode> <bredd>"""
import asyncio, json, sys
from pathlib import Path
from playwright.async_api import async_playwright
from PIL import Image

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r7")
DIMS = {1440: 900, 390: 844, 768: 1024}

SLOTS = r"""([sel, n]) => {
  const sec = document.querySelector(sel);
  const ps = parseFloat(getComputedStyle(sec).getPropertyValue('--sc-ps')) || 0;
  const items = [...sec.querySelectorAll(n === 5 && sel === '#tes' ? '.ts' : '.cs')];
  const N = items.length, f = .04;
  const vis = items.map((el, k) => {
    const i = k, a = i / N, b = (i + 1) / N;
    let inn = Math.min(1, Math.max(0, (ps - a + f / 2) / f));
    let out = Math.min(1, Math.max(0, (ps - b + f / 2) / f));
    if (k === 0) inn = 1; if (k === N - 1) out = 0;
    const r = el.getBoundingClientRect();
    const top = r.top + out * r.height, bot = r.bottom - (1 - inn) * r.height;
    return {k, inn: +inn.toFixed(3), out: +out.toFixed(3), top: Math.round(top), bot: Math.round(bot), h: Math.round(r.height), visible: bot - top > 1};
  });
  const v = vis.filter(x => x.visible);
  let ov = 0;
  for (let i = 0; i < v.length; i++) for (let j = i + 1; j < v.length; j++)
    ov = Math.max(ov, Math.min(v[i].bot, v[j].bot) - Math.max(v[i].top, v[j].top));
  const fr = sec.querySelector('iframe');
  let fy = null; try { fy = fr && fr.contentWindow ? fr.contentWindow.scrollY : null } catch (e) {}
  return {y: scrollY, ps: +ps.toFixed(4), nvis: v.length, vis: v.map(x => x.k), overlap: ov, detail: vis, fy};
}"""

HEADS = r"""() => {
  const sels = 'h1,h2,h3,.ts,.process-title,.process-step-title,.cases-title,.case-title,.bridge-title,.ledger-num';
  const els = [...document.querySelectorAll(sels)].filter(e => { const r = e.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight && r.width > 0; });
  const shown = els.filter(e => { const r = e.getBoundingClientRect();
    const pts = [[.25,.3],[.5,.5],[.75,.7]].map(([fx,fy]) => [r.left + r.width*fx, Math.min(innerHeight-1, Math.max(0, r.top + r.height*fy))]);
    return pts.some(([x,y]) => { const t = document.elementFromPoint(x, y); return t && (e === t || e.contains(t)); }); });
  const hits = [];
  for (let i = 0; i < shown.length; i++) for (let j = i + 1; j < shown.length; j++) {
    const a = shown[i], b = shown[j]; if (a.contains(b) || b.contains(a)) continue;
    const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
    const w = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left), h = Math.min(ra.bottom, rb.bottom) - Math.max(ra.top, rb.top);
    if (w > 4 && h > 4) {
      // bekräfta: någon punkt i skärningen där topmost ligger i a OCH en där topmost ligger i b
      const x0 = Math.max(ra.left, rb.left), y0 = Math.max(0, Math.max(ra.top, rb.top)), x1 = x0 + w, y1 = Math.min(innerHeight, y0 + h);
      let inA = 0, inB = 0;
      for (let gx = 0; gx < 8; gx++) for (let gy = 0; gy < 5; gy++) {
        const t = document.elementFromPoint(x0 + (x1 - x0) * (gx + .5) / 8, y0 + (y1 - y0) * (gy + .5) / 5);
        if (!t) continue; if (a === t || a.contains(t)) inA++; if (b === t || b.contains(t)) inB++;
      }
      if (inA && inB) hits.push({a: (a.className || a.tagName) + ':' + a.textContent.trim().slice(0, 30), b: (b.className || b.tagName) + ':' + b.textContent.trim().slice(0, 30), w: Math.round(w), h: Math.round(h)});
    }
  }
  return {y: scrollY, hs: document.documentElement.scrollWidth - innerWidth, hits};
}"""


async def goto(pg, url):
    for a in range(6):
        try:
            await pg.goto(url, wait_until="load", timeout=30000); return
        except Exception:
            if a == 5: raise


async def wheel_to(pg, y, step=150):
    for _ in range(1500):
        cur = await pg.evaluate("scrollY")
        d = y - cur
        if abs(d) < 2: return
        await pg.mouse.wheel(0, max(-step, min(step, d)))
        await pg.wait_for_timeout(30)


async def run(mode, w):
    h = DIMS[w]
    async with async_playwright() as p:
        br = await p.chromium.launch()
        ctx = await br.new_context(viewport={"width": w, "height": h})
        pg = await ctx.new_page()
        await goto(pg, URL); await pg.wait_for_timeout(1500)
        await pg.mouse.move(w / 2, h / 2)
        res = {}
        if mode == "thesis":
            top = await pg.evaluate("scrollY+document.querySelector('#tes').getBoundingClientRect().top")
            end = await pg.evaluate("(()=>{const e=document.querySelector('#tes');return scrollY+e.getBoundingClientRect().top+e.offsetHeight-innerHeight})()")
            await wheel_to(pg, top - 50); await pg.wait_for_timeout(1500)
            d = OUT / f"thesis-{w}"; d.mkdir(exist_ok=True)
            for direction in ("down", "up"):
                frames = []; sgn = 1 if direction == "down" else -1
                for i in range(2000):
                    cur = await pg.evaluate("scrollY")
                    if (sgn > 0 and cur >= end + 50) or (sgn < 0 and cur <= top - 50): break
                    await pg.mouse.wheel(0, 40 * sgn); await pg.wait_for_timeout(110)
                    m = await pg.evaluate(SLOTS, ["#tes", 5]); m["i"] = i
                    if m["nvis"] > 1 or i % 6 == 0:
                        fn = d / f"{direction}-{i:03d}.png"; await pg.screenshot(path=str(fn)); m["shot"] = fn.name
                    frames.append(m)
                res[direction] = frames
                multi = [f for f in frames if f["nvis"] > 1]
                print(direction, "frames", len(frames), "multi-visible", len(multi), "max overlap px", max([f["overlap"] for f in frames] or [0]), flush=True)
        elif mode == "cases":
            for sel, n in (("#case-calyx", 5), ("#case-horai", 6)):
                top = await pg.evaluate(f"scrollY+document.querySelector('{sel}').getBoundingClientRect().top")
                end = await pg.evaluate(f"(()=>{{const e=document.querySelector('{sel}');return scrollY+e.getBoundingClientRect().top+e.offsetHeight-innerHeight}})()")
                await wheel_to(pg, top - 100); await pg.wait_for_timeout(4000)
                for f in pg.frames[1:]:
                    try: await f.wait_for_load_state("load", timeout=8000)
                    except Exception: pass
                d = OUT / f"cases-{w}"; d.mkdir(exist_ok=True)
                key = sel[1:]
                for direction in ("down", "up"):
                    frames = []; sgn = 1 if direction == "down" else -1
                    for i in range(3000):
                        cur = await pg.evaluate("scrollY")
                        if (sgn > 0 and cur >= end + 100) or (sgn < 0 and cur <= top - 100): break
                        await pg.mouse.wheel(0, 60 * sgn); await pg.wait_for_timeout(90)
                        m = await pg.evaluate(SLOTS, [sel, n]); m["i"] = i
                        if m["nvis"] > 1 and m["overlap"] > 0 or i % 10 == 0:
                            fn = d / f"{key}-{direction}-{i:03d}.png"; await pg.screenshot(path=str(fn)); m["shot"] = fn.name
                        frames.append(m)
                    # vila: jämför synk i vila vid slutläget
                    await pg.wait_for_timeout(2500)
                    rest = await pg.evaluate(SLOTS, [sel, n])
                    res[f"{key}-{direction}"] = {"frames": frames, "rest": rest}
                    fys = [f["fy"] for f in frames if f["fy"] is not None]
                    back = sum(1 for a, b in zip(fys, fys[1:]) if (b - a) * sgn < -1)
                    print(key, direction, "frames", len(frames), "fy range", (min(fys), max(fys)) if fys else None,
                          "non-monotonic steps", back, "multi-vis", sum(1 for f in frames if f["nvis"] > 1),
                          "max overlap", max([f["overlap"] for f in frames] or [0]), flush=True)
                # fram/bak-jämförelse i vila vid fasta punkter
                pts = []
                for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
                    yy = top + frac * (end - top)
                    await wheel_to(pg, yy - 400); await pg.wait_for_timeout(2500); await wheel_to(pg, yy); await pg.wait_for_timeout(3000)
                    a = await pg.evaluate(SLOTS, [sel, n])
                    await wheel_to(pg, yy + 400); await pg.wait_for_timeout(2500); await wheel_to(pg, yy); await pg.wait_for_timeout(3000)
                    b = await pg.evaluate(SLOTS, [sel, n])
                    pts.append({"frac": frac, "fromAbove": [a["y"], a["ps"], a["fy"]], "fromBelow": [b["y"], b["ps"], b["fy"]]})
                    await pg.screenshot(path=str(d / f"{key}-rest-{int(frac*100):02d}.png"))
                res[f"{key}-pts"] = pts
                print(key, "rest pts", json.dumps(pts), flush=True)
        elif mode == "whole":
            d = OUT / f"whole-{w}"; d.mkdir(exist_ok=True)
            H = await pg.evaluate("document.documentElement.scrollHeight")
            frames = []; i = 0
            while True:
                m = await pg.evaluate(HEADS); m["i"] = i
                fn = d / f"{i:03d}.png"; await pg.screenshot(path=str(fn))
                frames.append(m)
                if m["hits"]: print(i, m["y"], m["hits"], flush=True)
                cur = await pg.evaluate("scrollY")
                if cur >= await pg.evaluate("document.documentElement.scrollHeight-innerHeight") - 1: break
                await pg.mouse.wheel(0, 150); await pg.wait_for_timeout(260); i += 1
            res["frames"] = frames
            print("frames", len(frames), "hscroll max", max(f["hs"] for f in frames), "collision frames", sum(1 for f in frames if f["hits"]), flush=True)
            # kontaktark, var 2:a bild
            ims = [Image.open(d / f"{k:03d}.png") for k in range(0, len(frames), 2)]
            cw = 240 if w > 700 else 120; ch = int(cw * h / w); cols = 10 if w > 700 else 14
            for part in range(0, len(ims), cols * 6):
                chunk = ims[part:part + cols * 6]
                rows = (len(chunk) + cols - 1) // cols
                s = Image.new("RGB", (cols * (cw + 4), rows * (ch + 4)), "white")
                for k, im in enumerate(chunk):
                    s.paste(im.convert("RGB").resize((cw, ch)), ((k % cols) * (cw + 4), (k // cols) * (ch + 4)))
                s.save(OUT / f"sheet-whole-{w}-{part // (cols * 6)}.png")
        (OUT / f"sweep-{mode}-{w}.json").write_text(json.dumps(res, indent=1))
        await br.close()

asyncio.run(run(sys.argv[1], int(sys.argv[2])))
