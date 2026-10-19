"""astra-r18: kantlinje runt ramarna. Rektangeln ur preview-läget (samma scrollY som hjulbilden),
pixlar ur hjulbilden ours/P17-1/P19-1/P19-6. Per kant: profil -3..+3 px över kanten på 40 punkter."""
import asyncio, json
from PIL import Image
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
PAIRS = [("P17-1", "case-calyx-01", "#case-calyx"), ("P17-5", "case-calyx-05", "#case-calyx"),
         ("P19-1", "case-horai-01", "#case-horai"), ("P19-6", "case-horai-06", "#case-horai")]


def profile(im, r, W, H):
    out = {}
    L, T, R, B = [round(v) for v in (r['left'], r['top'], r['right'], r['bottom'])]
    xs = [L + (R - L) * k // 41 for k in range(1, 41)]; ys = [T + (B - T) * k // 41 for k in range(1, 41)]
    def get(x, y):
        return im.getpixel((x, y)) if 0 <= x < W and 0 <= y < H else None
    for edge, pts in (('top', [(x, T + d) for x in xs for d in range(-3, 4)]),
                      ('bottom', [(x, B - 1 + d) for x in xs for d in range(-3, 4)]),
                      ('left', [(L + d, y) for y in ys for d in range(-3, 4)]),
                      ('right', [(R - 1 + d, y) for y in ys for d in range(-3, 4)])):
        if edge == 'top' and T <= 0 or edge == 'bottom' and B >= H or edge == 'left' and L <= 0 or edge == 'right' and R >= W:
            out[edge] = 'viewport-kant'; continue
        # medelvärde per offset
        rows = {}
        for i, (x, y) in enumerate(pts):
            d = i % 7 - 3; p = get(x, y)
            if p: rows.setdefault(d, []).append(p)
        out[edge] = {d: tuple(round(sum(c[j] for c in v) / len(v)) for j in range(3)) for d, v in sorted(rows.items())}
    return out


async def main():
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in [(1920, 930), (1440, 900), (390, 844)]:
            for rid, mode, sel in PAIRS:
                pg = await b.new_page(viewport={'width': w, 'height': h})
                await pg.goto(URL + "?preview=" + mode); await pg.wait_for_timeout(3500)
                r = await pg.evaluate(f"(()=>{{const e=document.querySelector('{sel} .case-wrap').getBoundingClientRect();return {{left:e.left,top:e.top,right:e.right,bottom:e.bottom,y:scrollY}}}})()")
                await pg.close()
                try:
                    im = Image.open(f"ours/{rid}-{w}.png").convert('RGB')
                except FileNotFoundError:
                    continue
                res[f"{rid}-{w}"] = {'rect': r, 'edges': profile(im, r, im.width, im.height)}
                print(rid, w, json.dumps(res[f"{rid}-{w}"]), flush=True)
        await b.close()
    open('edges18.json', 'w').write(json.dumps(res, indent=1))

asyncio.run(main())
