"""Lead R24: matter de nio felen i renderingen, och tar bilder jag kan doma pa.

Riktig hjulscroll (mouse.wheel, 20 px), aldrig ?preview= - fel 4 ar just att
forhandsvisningslagena siktar pa ett utganget tx-fonster, sa att doma i dem ar
att mata fel scrollage.

    python mat.py 1920 930 r24-1920
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

# Synlig textyta i viewporten, och de matt som fel 2-6 doms pa.
PROBE = """() => {
  const px = s => { const e=document.querySelector(s); return e?parseFloat(getComputedStyle(e).fontSize):null; };
  const rect = s => { const e=document.querySelector(s); if(!e) return null;
    const r=e.getBoundingClientRect(); return {x:Math.round(r.left),y:Math.round(r.top),
      w:Math.round(r.width),h:Math.round(r.height)}; };
  const abs = s => { const e=document.querySelector(s); if(!e) return null;
    const r=e.getBoundingClientRect(); return Math.round(r.top + scrollY); };
  let ink = 0;
  const walk=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
  let n; const vw=innerWidth, vh=innerHeight;
  while((n=walk.nextNode())){
    if(!n.nodeValue.trim()) continue;
    const rg=document.createRange(); rg.selectNodeContents(n);
    for(const r of rg.getClientRects()){
      const w=Math.max(0,Math.min(r.right,vw)-Math.max(r.left,0));
      const h=Math.max(0,Math.min(r.bottom,vh)-Math.max(r.top,0));
      ink += w*h;
    }
  }
  const cs = s => { const e=document.querySelector(s); return e?getComputedStyle(e).backgroundColor:null; };
  return {
    scrollY: Math.round(scrollY), docH: Math.round(document.documentElement.scrollHeight),
    inkPct: +(100*ink/(vw*vh)).toFixed(1),
    tx: (()=>{ const e=document.querySelector('.tes-plane')||document.documentElement;
               return +parseFloat(getComputedStyle(e).getPropertyValue('--tx')).toFixed(3); })(),
    planeBg: cs('.tes-plane'), stageBg: cs('.thesis-stage'),
    y: { tes: abs('#tes'), process: abs('#process'), case: abs('#case'),
         calyx: abs('#case-calyx'), pris: abs('#pris'), kontakt: abs('#kontakt') },
    sheet: rect('.process-sheet'), plate: rect('.chapter-plate'),
    num: rect('.ledger-num'), p01: rect('.process-p'),
    title: rect('.process-title'),
    kontaktBg: cs('#kontakt'), lead: rect('.contact-lead'),
  };
}"""


async def main():
    w, h, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    out = {"view": f"{w}x{h}", "frames": []}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto(URL)
        await pg.wait_for_timeout(3500)

        base = await pg.evaluate(PROBE)
        out["base"] = base
        print("dokumenthojd: %d px" % base["docH"], flush=True)
        print("ankare:", base["y"], flush=True)

        # --- fel 3: textyta per bildruta, 20 px hjul, hela akten -------------
        y0, y1 = base["y"]["tes"], base["y"]["pris"]
        ys = list(range(int(y0), int(y1), 20))
        low, lowest, nlow = 0, None, 0
        for y in ys:
            await pg.evaluate("y => window.scrollTo(0, y)", y)
            await pg.wait_for_timeout(60)
            ink = await pg.evaluate("""() => {
              let ink=0; const walk=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
              let n; const vw=innerWidth, vh=innerHeight;
              while((n=walk.nextNode())){
                if(!n.nodeValue.trim()) continue;
                const rg=document.createRange(); rg.selectNodeContents(n);
                for(const r of rg.getClientRects()){
                  const a=Math.max(0,Math.min(r.right,vw)-Math.max(r.left,0));
                  const b=Math.max(0,Math.min(r.bottom,vh)-Math.max(r.top,0));
                  ink += a*b; } }
              return +(100*ink/(vw*vh)).toFixed(1); }""")
            if ink < 18:
                nlow += 1
                if lowest is None or ink < lowest[1]:
                    lowest = (y, ink)
            out["frames"].append({"y": y, "ink": ink})
        out["fel3"] = {"ramar": len(ys), "under18": nlow, "lagst": lowest}
        print("fel 3: %d av %d bildrutor under 18 %%, lägst %s" % (nlow, len(ys), lowest), flush=True)

        # --- fel 2: pixelprover pa planet och tesbandet ----------------------
        probe_y = base["y"]["tes"] + 300
        await pg.evaluate("y => window.scrollTo(0, y)", probe_y)
        await pg.wait_for_timeout(700)
        shots = {}
        for name, sel in (("plane", ".tes-plane"), ("stage", ".thesis-stage")):
            el = await pg.query_selector(sel)
            if el:
                box = await el.bounding_box()
                if box and box["width"] > 4 and box["height"] > 4:
                    cx = box["x"] + box["width"] / 2
                    cy = max(2, min(h - 2, box["y"] + box["height"] / 2))
                    await pg.screenshot(path=f"_px_{name}.png",
                                        clip={"x": cx - 2, "y": cy - 2, "width": 4, "height": 4})
                    shots[name] = f"_px_{name}.png"
        out["fel2"] = {"prover": shots, "y": probe_y}

        # --- namngivna stills ------------------------------------------------
        marks = {}
        for k, y in base["y"].items():
            marks[k] = int(y)
        # overgangen: fyra jamna steg genom akten
        tes, proc = int(base["y"]["tes"]), int(base["y"]["process"])
        span = max(1, proc - tes)
        for i in range(5):
            marks[f"overgang-{i}"] = tes + int(span * i / 4)
        for name, y in marks.items():
            await pg.evaluate("y => window.scrollTo(0, y)", y)
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{name}-{tag}.png")
        out["stills"] = sorted(marks)

        out["jsErrors"] = len(errs)
        print("js-fel:", len(errs), flush=True)
        await b.close()
    open(f"mat-{tag}.json", "w", encoding="utf-8").write(json.dumps(out, indent=1))
    print("skrev mat-%s.json" % tag)


asyncio.run(main())
