"""Lead R22: finns en 2px ljus KOLUMN vid planets klippta sidor? Mätt i PNG, inte i CSS."""
import asyncio, json
from playwright.async_api import async_playwright
from PIL import Image
BASE = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=tes-till-ritning-"
OUT = "."

async def main():
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in ((1920, 930), (1440, 900), (390, 844)):
            for k in (3, 4):
                pg = await b.new_page(viewport={'width': w, 'height': h})
                await pg.goto(BASE + str(k)); await pg.wait_for_timeout(3500)
                g = await pg.evaluate("""()=>{
                  const e=document.querySelector('.tes-plane');const r=e.getBoundingClientRect();
                  const cs=getComputedStyle(e);
                  const m=/inset\\(([^)]+)\\)/.exec(cs.clipPath);
                  const v=m?m[1].trim().split(/\\s+/).map(parseFloat):[0,0,0,0];
                  return {L:r.left+v[3], T:r.top+v[0], R:r.right-v[1], B:r.bottom-v[2],
                          edge:getComputedStyle(e,'::after').opacity};
                }""")
                f = f"{OUT}/t{k}-{w}.png"
                await pg.screenshot(path=f)
                im = Image.open(f).convert('RGB')
                # mät i tre rader innanför rektangeln
                ys = [int(g['T'] + (g['B'] - g['T']) * q) for q in (.3, .5, .7)]
                ys = [y for y in ys if 0 <= y < im.height]
                def lum(px): return .2126*px[0] + .7152*px[1] + .0722*px[2]
                def scan(xc):
                    hit = None
                    for dx in range(-3, 4):
                        x = int(round(xc)) + dx
                        if not (0 <= x < im.width): continue
                        vals = [lum(im.getpixel((x, y))) for y in ys]
                        inside = [lum(im.getpixel((min(im.width-1, max(0, x + (12 if dx <= 0 else -12))), y))) for y in ys]
                        if min(vals) - max(inside) > 60:
                            hit = (dx, round(min(vals)), round(max(inside)))
                            break
                    return hit
                res[f"{w}-t{k}"] = {'clipL': round(g['L'],1), 'clipR': round(g['R'],1),
                                    'edgeOpacity': g['edge'],
                                    'left': scan(g['L']), 'right': scan(g['R'])}
                print(f"{w}-t{k}", res[f"{w}-t{k}"], flush=True)
                await pg.close()
        await b.close()
    open(f"{OUT}/col.json", 'w').write(json.dumps(res, indent=1))

asyncio.run(main())
