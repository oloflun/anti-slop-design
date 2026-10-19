"""Plattans geometri: --cp-* och de dokumentkoordinater de raknas ur."""
import asyncio, json
from playwright.async_api import async_playwright

URL = "http://localhost:3304/tests/alunix-r8/runs/V3d/index.html"

READ = """() => {
  const g = (e, p) => { if (!e) return null;
    const v = getComputedStyle(e).getPropertyValue(p).trim(); return v; };
  const caseEl = document.getElementById('case');
  const plate = document.querySelector('.chapter-plate');
  const sheet = document.querySelector('.process-sheet') || document.querySelector('.tes-plane');
  const R = e => { const r = e.getBoundingClientRect();
    return [Math.round(r.left), Math.round(r.top + scrollY),
            Math.round(r.right), Math.round(r.bottom + scrollY)]; };
  return {
    cp: {up: g(caseEl,'--cp-up'), t: g(caseEl,'--cp-t'), b: g(caseEl,'--cp-b'),
         l: g(caseEl,'--cp-l'), r: g(caseEl,'--cp-r'), dn: g(caseEl,'--cp-dn')},
    caseDoc: R(caseEl), plateDoc: R(plate),
    sheetSel: sheet ? sheet.className : null, sheetDoc: sheet ? R(sheet) : null,
    processDoc: R(document.getElementById('process')),
    vw: innerWidth, y: Math.round(scrollY)
  };
}"""


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': 1920, 'height': 930})
        await pg.goto(URL)
        await pg.wait_for_timeout(2400)
        for y in (0, 16844):
            await pg.evaluate("(y) => window.scrollTo(0, y)", y)
            await pg.wait_for_timeout(400)
            d = await pg.evaluate(READ)
            print(f"--- y={d['y']} vw={d['vw']}")
            print("  cp :", d['cp'])
            print("  caseDoc   [l,top,r,bottom]:", d['caseDoc'])
            print("  plateDoc  [l,top,r,bottom]:", d['plateDoc'])
            print("  sheetSel:", d['sheetSel'], d['sheetDoc'])
            print("  processDoc:", d['processDoc'])
        await b.close()


asyncio.run(main())
