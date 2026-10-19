"""R24 F1-F5: matning fore och efter.

Tre fraagor, alla i RIKTIG hjulscroll (handoffen M2), aldrig i ett ?preview=-lage:
  F3  vad klipper kapitelrubriken?  -> klippande forfader + vad som malar over den
  F4  siffrans underkant mot etikettens overkant, per steg
  F5  textspaltens bredd och antal renderade rader

Kor: python probe.py <tag>
"""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = os.path.dirname(os.path.abspath(__file__))
SIZES = [(1920, 930), (1440, 900), (390, 844)]

MEASURE = r"""
() => {
  const r = e => { const b = e.getBoundingClientRect();
    return {x:+b.x.toFixed(1), y:+b.y.toFixed(1), w:+b.width.toFixed(1),
            h:+b.height.toFixed(1), b:+b.bottom.toFixed(1), rt:+b.right.toFixed(1)}; };

  // --- F3: klippande forfader till kapitelrubriken
  const title = document.querySelector('.process-title');
  const chain = [];
  for (let e = title; e && e !== document.documentElement; e = e.parentElement) {
    const cs = getComputedStyle(e);
    chain.push({sel: e.className || e.tagName,
      overflow: cs.overflow, clipPath: cs.clipPath, contain: cs.contain,
      transform: cs.transform === 'none' ? 'none' : 'YES',
      position: cs.position, zIndex: cs.zIndex, rect: r(e)});
  }
  // vad malar over rubrikens nedre rad? (punkter tva px ovanfor bottenkanten)
  const tb = title.getBoundingClientRect();
  const probes = [];
  for (const frac of [0.15, 0.5, 0.85]) {
    const px = tb.x + tb.width * frac, py = tb.bottom - 3;
    const el = document.elementFromPoint(px, py);
    probes.push({at: [Math.round(px), Math.round(py)],
      top: el ? (el.className || el.tagName) : null,
      isTitle: el === title || (el && title.contains(el))});
  }

  // --- F4/F5: stegen
  const steps = [...document.querySelectorAll('#process .step-band')].map(b => {
    const num = b.querySelector('.ledger-num');
    const lab = b.querySelector('.process-step-title');
    const par = b.querySelector('.process-p');
    const nb = num.getBoundingClientRect(), lb = lab.getBoundingClientRect();
    // antal renderade rader i stycket
    const rng = document.createRange();
    rng.selectNodeContents(par);
    const rects = [...rng.getClientRects()].filter(x => x.height > 1);
    const tops = new Set(rects.map(x => Math.round(x.top)));
    const pb = par.getBoundingClientRect();
    return {step: b.closest('li').dataset.step,
      num: r(num), lab: r(lab), par: r(par),
      gap_num_lab: +(lb.top - nb.bottom).toFixed(1),
      gap_lab_par: +(pb.top - lb.bottom).toFixed(1),
      lines: tops.size,
      inkWidth: +Math.max(...rects.map(x => x.right)).toFixed(1) - Math.min(...rects.map(x => x.left)).toFixed(1)};
  });

  // --- spaltmatten
  const grid = document.querySelector('#process .process-grid');
  const gc = getComputedStyle(grid);
  const sheet = document.querySelector('.process-sheet').getBoundingClientRect();
  const stepsCol = document.querySelector('.process-steps');

  // --- kontakt: rubrik, kort
  const kt = document.querySelector('#kontakt-title');
  const kc = document.querySelector('.contact-card');
  const kfront = document.querySelector('.contact-card .face--front');
  const kback = document.querySelector('.contact-card .card-back');
  const kb = kc ? kc.getBoundingClientRect() : null;

  return {
    vw: innerWidth, vh: innerHeight, page_h: document.documentElement.scrollHeight,
    f3: {title: r(title), chain, probes,
         stamp: document.querySelector('.chapter-stamp') ? r(document.querySelector('.chapter-stamp')) : null,
         stampOverflow: document.querySelector('.chapter-stamp') ?
            getComputedStyle(document.querySelector('.chapter-stamp')).overflow : null},
    steps,
    cols: {grid: gc.gridTemplateColumns, gap: gc.columnGap, padLeft: gc.paddingLeft,
           stepsRect: r(stepsCol), sheet: r(document.querySelector('.process-sheet')),
           sheetVwPct: +(document.querySelector('.process-sheet').getBoundingClientRect().width / innerWidth * 100).toFixed(1)},
    contact: {title: kt ? r(kt) : null,
              titleFont: kt ? getComputedStyle(kt).fontSize + ' / ' + getComputedStyle(kt).fontFamily : null,
              lead: document.querySelector('.contact-lead') ? r(document.querySelector('.contact-lead')) : null,
              card: kb ? r(kc) : null,
              cardChild: kfront ? 'face--front' : (kback ? 'card-back' : 'none')}
  };
}
"""


async def wheel_to(pg, sel, tries=220, step=180, want=None):
    """Riktig hjulscroll tills <sel> ar i bildrutan (och villekorsvillkoret)."""
    for _ in range(tries):
        ok = await pg.evaluate(
            """([sel, want]) => { const e = document.querySelector(sel);
                 if (!e) return false; const b = e.getBoundingClientRect();
                 const vh = innerHeight;
                 if (want === 'bottom-in')  return b.bottom > vh*0.35 && b.bottom < vh*0.95;
                 if (want === 'top-third')  return b.top > vh*0.10 && b.top < vh*0.40;
                 return b.top > 0 && b.bottom < vh; }""", [sel, want])
        if ok:
            await pg.wait_for_timeout(700)
            return True
        await pg.mouse.wheel(0, step)
        await pg.wait_for_timeout(45)
    return False


async def run(tag):
    shots, data = [], {}
    async with async_playwright() as p:
        br = await p.chromium.launch(args=["--force-device-scale-factor=1"])
        for (w, h) in SIZES:
            pg = await br.new_page(viewport={"width": w, "height": h})
            await pg.goto(URL, wait_until="load")
            await pg.wait_for_timeout(1200)
            tagw = f"{w}x{h}"

            # F3: kapitlet, rubriken med botten i bildrutan
            await wheel_to(pg, '.process-title', want='bottom-in')
            f = f"{OUT}/{tag}-{tagw}-kapitel.png"
            await pg.screenshot(path=f)
            shots.append(f)
            d = await pg.evaluate(MEASURE)
            data[tagw] = {"kapitel": d["f3"]}

            # F4/F5: stegen, ett band i taget
            data[tagw]["steps"] = []
            for n in ("01", "02", "04"):
                await pg.evaluate("() => window.scrollTo(0, 0)")
                await pg.wait_for_timeout(300)
                got = await wheel_to(pg, f'li[data-step="{n}"] .process-step-title', want='top-third')
                if not got:
                    data[tagw]["steps"].append({"step": n, "reached": False})
                    continue
                f = f"{OUT}/{tag}-{tagw}-steg{n}.png"
                await pg.screenshot(path=f)
                shots.append(f)
                d = await pg.evaluate(MEASURE)
                row = next((s for s in d["steps"] if s["step"] == n), None)
                if row:
                    row["reached"] = True
                    row["cols"] = d["cols"]
                data[tagw]["steps"].append(row or {"step": n, "reached": False})

            # kontakt
            await pg.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
            await pg.wait_for_timeout(1400)
            f = f"{OUT}/{tag}-{tagw}-kontakt.png"
            await pg.screenshot(path=f)
            shots.append(f)
            d = await pg.evaluate(MEASURE)
            data[tagw]["contact"] = d["contact"]
            await pg.close()
        await br.close()
    json.dump(data, open(f"{OUT}/{tag}.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("shots:", len(shots))
    for k, v in data.items():
        st = [s for s in v["steps"] if s.get("reached")]
        print(f"-- {k}  sheet {v['steps'][0]['cols']['sheetVwPct']}% vw"
              if st else f"-- {k}")
        for s in st:
            print(f"   steg{s['step']}  siffra->etikett {s['gap_num_lab']}px  "
                  f"etikett->text {s['gap_lab_par']}px  rader {s['lines']}  "
                  f"textbredd {s['par']['w']}px")
        print("   kontakt:", json.dumps(v["contact"], ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(run(sys.argv[1] if len(sys.argv) > 1 else "baseline"))
