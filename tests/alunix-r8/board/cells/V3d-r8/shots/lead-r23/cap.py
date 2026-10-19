"""Lead R23: enskilda bilder av de lagen Anton domer pa, plus numeriska matvarden.

En skarmbild per sida, aldrig kontaktark. Chromium utan --hide-scrollbars.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

BASE = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview="
MODES = ["tes-till-ritning-2", "tes-till-ritning-3", "tes-till-ritning-4",
         "chapter", "process-01", "process-03", "cases", "kontakt"]

PROBE = """() => {
  const px = s => { const e=document.querySelector(s); return e?parseFloat(getComputedStyle(e).fontSize):null; };
  const rect = s => { const e=document.querySelector(s); if(!e) return null;
    const r=e.getBoundingClientRect(); return {x:Math.round(r.left),y:Math.round(r.top),
      w:Math.round(r.width),h:Math.round(r.height)}; };
  // synlig textyta i viewporten
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
  return {
    inkPct: +(100*ink/(vw*vh)).toFixed(1),
    sheet: rect('.process-sheet'),
    stamp: rect('.chapter-stamp'),
    casesTitle: px('.cases-title'),
    calyxName: px('.case--calyx .case-name'),
    priceValue: px('.price-row .value'),
    priceLabel: px('.price-row .label'),
    statement: px('.price .statement'),
    kontakt: rect('#kontakt'),
    serif: [...document.querySelectorAll('*')].filter(e=>getComputedStyle(e).fontFamily.includes('Young')).length,
  };
}"""


async def main():
    w, h, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for m in MODES:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(BASE + m); await pg.wait_for_timeout(3500)
            await pg.screenshot(path=f"{m}-{tag}.png")
            g = await pg.evaluate(PROBE)
            g['jsErrors'] = len(errs)
            out[m] = g
            print(f"{m:22} ink={g['inkPct']:5}%  sheet={g['sheet']}  err={g['jsErrors']}", flush=True)
            await pg.close()
        await b.close()
    open(f"probe-{tag}.json", 'w').write(json.dumps(out, indent=1))


asyncio.run(main())
