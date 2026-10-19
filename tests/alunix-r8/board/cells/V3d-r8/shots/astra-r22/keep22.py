"""astra-r22 § keep, bara det de tva andringarna kan ha rort:
  A. .seam-h (landningslinjen, r18 fix 1) - delar --x1/--x4 med fix 2:s geometri.
  B. horisontell scroll vid 9 bredder - fix 1 lagger ett nytt ::after i planet.
  C. konturens egen linjevikt/kontrast pa renderade pixlar (r18 fix 2:s 3:1-krav,
     nu for en NY linje) - last ur ridge22:s bilder, inte har.
Skriver keep22.json.
"""
import asyncio, json
from playwright.async_api import async_playwright

BASE = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"


async def main():
    out = {'seamH': {}, 'hscroll': {}}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in ((1920, 930), (1440, 900), (390, 844)):
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(BASE+'?preview=tes-till-ritning-4', wait_until='load')
            await pg.wait_for_timeout(3500)
            g = await pg.evaluate("""()=>{
              const h=document.querySelector('.seam .seam-h')||document.querySelector('.seam-h');
              const chap=document.querySelector('.process-chapter');
              const cs=chap?getComputedStyle(chap):null;
              const r=h?h.getBoundingClientRect():null;
              const v=n=>cs?cs.getPropertyValue(n).trim():'';
              return {w:r?+r.width.toFixed(1):null, hgt:r?+r.height.toFixed(1):null,
                      x1:v('--x1'), x4:v('--x4'), pl_l:v('--pl-l'), pl_r:v('--pl-r'),
                      title:(()=>{const t=document.querySelector('.process-title');
                        return t?getComputedStyle(t).opacity+'/'+getComputedStyle(t).color:null;})()};
            }""")
            out['seamH']["%d" % w] = g
            print(w, g, flush=True)
            await pg.close()
        for w in (320, 375, 390, 414, 768, 1024, 1280, 1440, 1920):
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            await pg.goto(BASE, wait_until='load')
            await pg.wait_for_timeout(2500)
            d = await pg.evaluate("""()=>{
              const de=document.documentElement;
              return {doc:de.scrollWidth-de.clientWidth, body:document.body.scrollWidth-de.clientWidth,
                      iw:innerWidth, cw:de.clientWidth};
            }""")
            out['hscroll']["%d" % w] = d
            print('hscroll', w, d, flush=True)
            await pg.close()
        await b.close()
    open('keep22.json', 'w').write(json.dumps(out, indent=1))

asyncio.run(main())
