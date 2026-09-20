"""astra-r22 fix 1: 2px ljus KOLUMN vid planets klippta vanster-/hogerkant?
real = sidan som den ar. break = medvetet trasig kontroll, ::after{display:none}.
En skarmbild per sida. Skriver column22.json + col-*.png i cwd.
"""
import asyncio, json
from PIL import Image
from playwright.async_api import async_playwright

BASE = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=tes-till-ritning-"

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
  const seams=[...document.querySelectorAll('.seam i')].map(i=>{
    const q=i.getBoundingClientRect(); const c=getComputedStyle(i);
    return {cls:(i.className||'')+'', l:i.dataset.l||'', x:+q.left.toFixed(1), w:+q.width.toFixed(1),
            top:+q.top.toFixed(1), bot:+q.bottom.toFixed(1), op:c.opacity};
  });
  return {plane:[r.left,r.top,r.right,r.bottom], ins:v, pos:cs.position,
          clipped:{left:r.left+v[3], top:r.top+v[0], right:r.right-v[1], bottom:r.bottom-v[2]},
          tx:tx, edge:isNaN(tx)?0:cl((tx-0.6)/0.3),
          afterBorder:[a.borderTopWidth,a.borderLeftWidth,a.borderLeftColor],
          afterInset:[a.top,a.right,a.bottom,a.left], afterDisplay:a.display,
          seams:seams, dpr:devicePixelRatio, vw:innerWidth, vh:innerHeight};
}"""


def lum(px):
    return 0.2126*px[0] + 0.7152*px[1] + 0.0722*px[2]


def scan(img, y, edge, half=8):
    W = img.size[0]
    x0, x1 = max(0, int(edge)-half), min(W-1, int(edge)+half)
    L = [lum(img.getpixel((x, y))) for x in range(x0, x1+1)]
    base = sorted(L)[1]
    thr = base + 12
    best = None
    i = 0
    while i < len(L):
        if L[i] >= thr:
            j = i
            while j+1 < len(L) and L[j+1] >= thr:
                j += 1
            run = (x0+i, x0+j, max(L[i:j+1]))
            if best is None or run[2] > best[2]:
                best = run
            i = j+1
        else:
            i += 1
    if best is None:
        return None
    return {'start': best[0], 'end': best[1], 'w': best[1]-best[0]+1,
            'peak': round(best[2], 1), 'base': round(base, 1)}


def summ(runs, expected, which):
    ok = 0
    deltas = []
    widths = []
    for r in runs:
        if not r:
            continue
        d = (r['start']-expected) if which == 'l' else (r['end']+1-expected)
        deltas.append(round(d, 1))
        widths.append(r['w'])
        if abs(d) <= 1 and 1 <= r['w'] <= 4:
            ok += 1
    return {'found': ok, 'of': len(runs), 'deltas': deltas, 'widths': widths}


async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in ((1920, 930), (1440, 900), (390, 844)):
            for k in (3, 4):
                for mode in ('real', 'break'):
                    pg = await b.new_page(viewport={'width': w, 'height': h})
                    await pg.goto(BASE+str(k), wait_until='load')
                    await pg.wait_for_timeout(3500)
                    if mode == 'break':
                        await pg.add_style_tag(content='.tes-plane::after{display:none!important;}')
                        await pg.wait_for_timeout(400)
                    g = await pg.evaluate(GEO)
                    name = "col-t%d-%d-%s.png" % (k, w, mode)
                    await pg.screenshot(path=name)
                    await pg.close()
                    img = Image.open(name).convert('RGB')
                    c = g['clipped']
                    top = max(0, c['top']) + 8
                    bot = min(h, c['bottom']) - 8
                    rows = [int(top + (bot-top)*f) for f in (0.15, 0.35, 0.5, 0.65, 0.85)] if bot-top > 20 else []
                    res = {'tx': round(g['tx'], 4), 'edge': round(g['edge'], 4), 'pos': g['pos'],
                           'clippedLeft': round(c['left'], 1), 'clippedRight': round(c['right'], 1),
                           'clippedTop': round(c['top'], 1), 'clippedBottom': round(c['bottom'], 1),
                           'afterDisplay': g['afterDisplay'], 'afterBorder': g['afterBorder'],
                           'rows': rows, 'left': [], 'right': [], 'img': name}
                    for y in rows:
                        res['left'].append(scan(img, y, c['left']))
                        res['right'].append(scan(img, y, c['right']))
                    res['leftSum'] = summ(res['left'], c['left'], 'l')
                    res['rightSum'] = summ(res['right'], c['right'], 'r')
                    res['seamNearLeft'] = [s['cls'] for s in g['seams'] if abs(s['x']-c['left']) <= 8]
                    res['seamNearRight'] = [s['cls'] for s in g['seams'] if abs(s['x']+s['w']-c['right']) <= 8]
                    out["%d-t%d-%s" % (w, k, mode)] = res
                    print("%d-t%d-%s tx=%.3f edge=%.2f L%d/%d d=%s w=%s R%d/%d d=%s w=%s" % (
                        w, k, mode, res['tx'], res['edge'],
                        res['leftSum']['found'], res['leftSum']['of'], res['leftSum']['deltas'], res['leftSum']['widths'],
                        res['rightSum']['found'], res['rightSum']['of'], res['rightSum']['deltas'], res['rightSum']['widths']), flush=True)
        await b.close()
    open('column22.json', 'w').write(json.dumps(out, indent=1))

asyncio.run(main())
