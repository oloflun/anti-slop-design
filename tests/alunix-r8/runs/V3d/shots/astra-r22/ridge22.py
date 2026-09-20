"""astra-r22 fix 1, ratt detektor: en LJUS RIDGE (topp ljusare an BADA sidor) vid
planets klippta vanster-/hogerkant. column22.py:s forsta detektor var trubbig - den
slog ihop konturen med fyllningens ljussteg och gav 8-11px "runs". Tva kontroller,
bada medvetet trasiga:
  nocontour = .tes-plane::after{display:none}  -> ridge maste FORSVINNA
  noseam    = .seam{display:none}              -> ridge maste FINNAS KVAR
Den andra behovs for att vid t4 sammanfaller .seam:s konstruktionslinjer med
planets kant; utan noseam-kontrollen kan t4-kolumnen inte tillskrivas konturen.
En skarmbild per sida. Skriver ridge22.json + r22-*.png i cwd.
"""
import asyncio, json
from PIL import Image
from playwright.async_api import async_playwright

BASE = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=tes-till-ritning-"
MODES = {'real': None,
         'nocontour': '.tes-plane::after{display:none!important;}',
         'noseam': '.seam{display:none!important;}'}

GEO = r"""() => {
  const e=document.querySelector('.tes-plane'); if(!e) return null;
  const r=e.getBoundingClientRect(), cs=getComputedStyle(e);
  const m=/inset\(([^)]+)\)/.exec(cs.clipPath);
  const v=m?m[1].trim().split(/\s+/).map(parseFloat):[0,0,0,0];
  const a=getComputedStyle(e,'::after');
  const chap=document.querySelector('.process-chapter');
  const cl=x=>Math.max(0,Math.min(1,x));
  const ps=chap?parseFloat(getComputedStyle(chap).getPropertyValue('--sc-ps')):NaN;
  const tx=isNaN(ps)?NaN:cl((ps-0.07)/0.29);
  return {clipped:{left:r.left+v[3], top:r.top+v[0], right:r.right-v[1], bottom:r.bottom-v[2]},
          pos:cs.position, tx:tx, edge:isNaN(tx)?0:cl((tx-0.6)/0.3),
          after:[a.display,a.borderTopWidth,a.borderLeftWidth,a.borderBottomWidth,a.borderLeftColor]};
}"""


def lum(p):
    return 0.2126*p[0] + 0.7152*p[1] + 0.0722*p[2]


def ridge(img, y, edge, half=8, thr=20):
    W = img.size[0]
    xs = [x for x in range(max(3, int(edge)-half), min(W-4, int(edge)+half)+1)]
    L = {x: lum(img.getpixel((x, y))) for x in range(xs[0]-3, xs[-1]+4)}
    hot = [x for x in xs if L[x] - max(L[x-3], L[x+3]) >= thr]
    if not hot:
        return None
    runs = []
    s = hot[0]
    for a, b in zip(hot, hot[1:]+[None]):
        if b is None or b != a+1:
            runs.append((s, a))
            s = b
    best = max(runs, key=lambda r: max(L[x] for x in range(r[0], r[1]+1)))
    return {'start': best[0], 'end': best[1], 'w': best[1]-best[0]+1,
            'peak': round(max(L[x] for x in range(best[0], best[1]+1)), 1),
            'px': img.getpixel((best[0], y))}


def summ(runs, expected, which):
    ok = 0
    deltas = []
    widths = []
    for r in runs:
        if not r:
            deltas.append(None)
            continue
        d = (r['start']-expected) if which == 'l' else (r['end']+1-expected)
        deltas.append(round(d, 1))
        widths.append(r['w'])
        if abs(d) <= 1 and 1 <= r['w'] <= 3:
            ok += 1
    return {'found': ok, 'of': len(runs), 'deltas': deltas, 'widths': widths}


async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in ((1920, 930), (1440, 900), (390, 844)):
            for k in (3, 4):
                for mode, css in MODES.items():
                    pg = await b.new_page(viewport={'width': w, 'height': h})
                    await pg.goto(BASE+str(k), wait_until='load')
                    await pg.wait_for_timeout(3500)
                    if css:
                        await pg.add_style_tag(content=css)
                        await pg.wait_for_timeout(400)
                    g = await pg.evaluate(GEO)
                    name = "r22-t%d-%d-%s.png" % (k, w, mode)
                    await pg.screenshot(path=name)
                    await pg.close()
                    img = Image.open(name).convert('RGB')
                    c = g['clipped']
                    top = max(0, c['top']) + 8
                    bot = min(h, c['bottom']) - 8
                    rows = [int(top + (bot-top)*f) for f in (0.15, 0.35, 0.5, 0.65, 0.85)]
                    res = {'tx': round(g['tx'], 4), 'edge': round(g['edge'], 4), 'pos': g['pos'],
                           'after': g['after'], 'img': name, 'rows': rows,
                           'clippedLeft': round(c['left'], 1), 'clippedRight': round(c['right'], 1),
                           'clippedTop': round(c['top'], 1), 'clippedBottom': round(c['bottom'], 1)}
                    ls = [ridge(img, y, c['left']) for y in rows]
                    rs = [ridge(img, y, c['right']) for y in rows]
                    res['left'] = ls
                    res['right'] = rs
                    res['leftSum'] = summ(ls, c['left'], 'l')
                    res['rightSum'] = summ(rs, c['right'], 'r')
                    out["%d-t%d-%s" % (w, k, mode)] = res
                    print("%-5d t%d %-9s tx=%.2f edge=%.2f | L %d/5 d=%s w=%s | R %d/5 d=%s w=%s" % (
                        w, k, mode, res['tx'], res['edge'],
                        res['leftSum']['found'], res['leftSum']['deltas'], res['leftSum']['widths'],
                        res['rightSum']['found'], res['rightSum']['deltas'], res['rightSum']['widths']), flush=True)
        await b.close()
    open('ridge22.json', 'w').write(json.dumps(out, indent=1))

asyncio.run(main())
