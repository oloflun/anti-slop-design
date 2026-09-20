"""astra-r23: hamta scrollY for de lagen jag behover, plus nyckelmatt pa kapitel/case/pris."""
import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")
MODES = ["tes-till-ritning-0","tes-till-ritning-1","tes-till-ritning-2","tes-till-ritning-3",
         "tes-till-ritning-4","chapter","process-01","cases","case-calyx-01","pris"]

MEAS = """(() => {
  const g = s => document.querySelector(s);
  const r = e => { if(!e) return null; const b=e.getBoundingClientRect();
    return {x:+b.x.toFixed(1),y:+b.y.toFixed(1),w:+b.width.toFixed(1),h:+b.height.toFixed(1),
            top:+(b.top+scrollY).toFixed(1),bottom:+(b.bottom+scrollY).toFixed(1)}; };
  const f = e => { if(!e) return null; const c=getComputedStyle(e);
    return {fs:c.fontSize,lh:c.lineHeight,ff:c.fontFamily.split(',')[0],fw:c.fontWeight,
            ls:c.letterSpacing,color:c.color}; };
  const sec = g('#case');
  const title = g('.cases-title'); const lead = g('.cases-lead');
  const calyxSec = g('#case-calyx');
  const cn = g('.case--calyx .case-name'); const cl = g('.case--calyx .case-line');
  const pt = g('#pris-title'); const val = g('.price-row .value'); const lab = g('.price-row .label');
  return {
    scrollY, vh: innerHeight, vw: innerWidth,
    caseSec: r(sec), caseSecCS: sec?{minh:getComputedStyle(sec).minHeight,pad:getComputedStyle(sec).padding}:null,
    casesTitle: {rect:r(title), font:f(title)},
    casesLead: {rect:r(lead), font:f(lead)},
    calyxSecTop: calyxSec? +(calyxSec.getBoundingClientRect().top+scrollY).toFixed(1):null,
    caseName: {rect:r(cn), font:f(cn)},
    caseLine: {rect:r(cl), font:f(cl)},
    prisTitle: {rect:r(pt), font:f(pt)},
    priceValue: {rect:r(val), font:f(val)},
    priceLabel: {rect:r(lab), font:f(lab)},
    processTitle: {rect:r(g('.process-title')), font:f(g('.process-title'))},
    processLocked:{rect:r(g('.process-locked')), font:f(g('.process-locked'))},
    body: f(g('.price-ingress')),
    docH: document.documentElement.scrollHeight
  };
})()"""

async def main():
    res = {}
    async with async_playwright() as p:
        br = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w,h in ((1920,930),(390,844)):
            res[w] = {}
            ctx = await br.new_context(viewport={"width":w,"height":h})
            pg = await ctx.new_page()
            for m in MODES:
                await pg.goto(URL+"?preview="+m, wait_until="load", timeout=40000)
                await pg.wait_for_timeout(3200)
                res[w][m] = await pg.evaluate("scrollY")
            await pg.goto(URL, wait_until="load", timeout=40000)
            await pg.wait_for_timeout(2500)
            res[w]["meas"] = await pg.evaluate(MEAS)
            await ctx.close()
        await br.close()
    (OUT/"anchors23.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))
    print(json.dumps(res, indent=1, ensure_ascii=False))

asyncio.run(main())
