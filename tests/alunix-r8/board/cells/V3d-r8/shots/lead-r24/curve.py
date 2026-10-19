"""Mat kurvan: --sc-ps och --cx mot scrollY, sa att malpunkterna kan rakna
ur verkligheten i stallet for att gissas."""
import asyncio, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3304/tests/alunix-r8/runs/V3d/index.html"


async def main():
    w = int(sys.argv[1]); h = int(sys.argv[2])
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto(URL)
        await pg.wait_for_timeout(2200)
        info = await pg.evaluate("""() => {
          const c = document.querySelector('.cases-chapter');
          const r = c.getBoundingClientRect();
          return {top: Math.round(r.top + scrollY), h: Math.round(c.offsetHeight),
                  docH: document.documentElement.scrollHeight, vh: innerHeight}; }""")
        print(info)
        print(f"{'y':>7} {'sc_ps':>9} {'cx':>7}  chapterTopInViewport")
        for y in range(info['top'] - 2 * h, info['top'] + 2 * h, max(40, h // 8)):
            await pg.evaluate("(y) => window.scrollTo(0, y)", y)
            await pg.wait_for_timeout(120)
            row = await pg.evaluate("""() => {
              const c = document.querySelector('.cases-chapter');
              const f = (e, p) => parseFloat(getComputedStyle(e).getPropertyValue(p));
              return {ps: f(c, '--sc-ps'), cx: f(c, '--cx'),
                      sy: Math.round(scrollY),
                      top: Math.round(c.getBoundingClientRect().top)}; }""")
            print(f"{row['sy']:>7} {row['ps']:>9.4f} {row['cx']:>7.4f}  {row['top']}")
        await b.close()


asyncio.run(main())
