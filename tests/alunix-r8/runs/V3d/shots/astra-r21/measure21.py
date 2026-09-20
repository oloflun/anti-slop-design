"""astra-r21 mätsvep: seam-h-geometri, 20px-hjul genom tre övergångar (rubrikklipp),
stegband (glyfspringor), pris på en skärm, delade ord, hscroll."""
import asyncio, json, re
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
SW = open('../r12/scripts/sweep.py', encoding='utf-8').read()
SWEEP_JS = re.search(r'SWEEP_JS = """(.*?)"""', SW, re.S).group(1).replace('\\\\', '\\')
HEAD = "h1, h2, h3, .ts, .statement, .close-mailto"
SPLIT = r"""(sel)=>{const out=[];for(const el of document.querySelectorAll(sel)){if(!el.getClientRects().length)continue;
 const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const re=/\S+/g;let m;while(m=re.exec(n.data)){const r=document.createRange();r.setStart(n,m.index);r.setEnd(n,m.index+m[0].length);
 const tops=new Set([...r.getClientRects()].filter(q=>q.width>0).map(q=>Math.round(q.top)));if(tops.size>1)out.push({el:el.className||el.tagName,w:m[0]});}}}return out}"""
BANDS = r"""()=>{const out=[];
 for(const b of document.querySelectorAll('.process-steps .step-band')){const r=b.getBoundingClientRect();const cs=getComputedStyle(b);
  const m=/inset\(([^)]*)\)/.exec(cs.clipPath);let t=0;if(m){const k=m[1].trim().split(/\s+/)[0];t=k.endsWith('%')?parseFloat(k)/100*r.height:parseFloat(k);}
  const top=Math.max(r.top+t,0),bot=Math.min(r.bottom,innerHeight);const vis=bot-top;
  if(vis>1)out.push({s:b.closest('li').dataset.step,top:Math.round(r.top),vt:Math.round(top),vis:Math.round(vis),h:Math.round(r.height),slit:parseFloat(cs.getPropertyValue('--slit-p'))});}
 return out}"""
SEAMH = r"""()=>{const h=document.querySelector('.seam-h');const r=h.getBoundingClientRect();const c=document.querySelector('.process-chapter');
 return {w:r.width,h:r.height,left:r.left,top:r.top,cssW:getComputedStyle(h).width,x1:c.style.getPropertyValue('--x1'),x4:c.style.getPropertyValue('--x4'),tx:getComputedStyle(c).getPropertyValue('--tx')}}"""
PRIS = r"""()=>{const t=document.getElementById('pris-title').getBoundingClientRect();const m=document.querySelector('.close-mailto');const mr=m.getBoundingClientRect();
 return {titleTop:Math.round(t.top),mailBottom:Math.round(mr.bottom),ih:innerHeight,y:scrollY,max:document.documentElement.scrollHeight-innerHeight}}"""


async def wheel_to(pg, y, step=120):
    for _ in range(3000):
        d = y - await pg.evaluate("scrollY")
        if abs(d) < 2: break
        await pg.mouse.wheel(0, max(-step, min(step, d))); await pg.wait_for_timeout(25)


async def sweep(pg, y0, y1, fn, arg=None, cap=900):
    await wheel_to(pg, y0); await pg.wait_for_timeout(700)
    fr = []; n = 0
    while (await pg.evaluate("scrollY")) < y1 and n < cap:
        await pg.mouse.wheel(0, 20); await pg.wait_for_timeout(40); n += 1
        v = await pg.evaluate(fn, arg) if arg is not None else await pg.evaluate(fn)
        fr.append((await pg.evaluate("scrollY"), v))
    return fr


async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in [(1920, 930), (1440, 900), (390, 844)]:
            o = out[w] = {}
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(URL); await pg.wait_for_timeout(2500)
            await pg.mouse.move(w / 2, h / 2)
            o['split'] = await pg.evaluate(SPLIT, ".ts,.case-name,.case-line,.cs h3,.process-title,.process-step-title,.process-p,.cases-title,.cases-lead,.statement,.price-ingress,#pris-title,.price-row,h1,h2,h3")
            r0 = await pg.evaluate("(()=>{const t=document.getElementById('tes');return t.getBoundingClientRect().top+scrollY+t.offsetHeight-2*innerHeight})()")
            r1 = await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY+1.3*innerHeight})()")
            fr = await sweep(pg, r0, r1, SWEEP_JS, HEAD)
            hits = [(y, x) for y, v in fr for x in v]
            o['tes_ritning'] = {'frames': len(fr), 'hits': len(hits), 'kinds': sorted({x['heading'][:40] + ' <- ' + str(x['hitCls'])[:30] for _, x in hits})}
            await wheel_to(pg, await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY})()")); await pg.wait_for_timeout(1200)
            o['seam_h'] = await pg.evaluate(SEAMH)
            p0 = await pg.evaluate("(()=>{const t=document.querySelector('.process-steps');return t.getBoundingClientRect().top+scrollY-innerHeight})()")
            p1 = await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY+t.offsetHeight-innerHeight})()")
            fr = await sweep(pg, p0, p1, BANDS, cap=1600)
            multi = [(y, v) for y, v in fr if len(v) > 1]
            slivers = [(y, x) for y, v in fr for x in v if 1 < x['vis'] < 40 and not (0 < x['slit'] < 1)]
            o['bands'] = {'frames': len(fr), 'multi_visible': len(multi), 'multi_sample': multi[:4],
                          'slivers_outside_slit': len(slivers), 'sliver_sample': slivers[:6]}
            for name, a, z in (('calyx_horai', "document.getElementById('case-calyx')", "document.getElementById('case-horai')"),
                               ('horai_pris', "document.getElementById('case-horai')", "document.getElementById('pris')")):
                y0 = await pg.evaluate(f"(()=>{{const s={a};return s.getBoundingClientRect().top+scrollY+s.offsetHeight-1.6*innerHeight}})()")
                y1 = await pg.evaluate(f"(()=>{{const s={z};return s.getBoundingClientRect().top+scrollY+0.6*innerHeight}})()")
                fr = await sweep(pg, y0, y1, SWEEP_JS, HEAD)
                hits = [x for _, v in fr for x in v]
                o[name] = {'frames': len(fr), 'hits': len(hits), 'kinds': sorted({x['heading'][:40] + ' <- ' + str(x['hitCls'])[:30] for x in hits})}
            await wheel_to(pg, await pg.evaluate("document.documentElement.scrollHeight-innerHeight")); await pg.wait_for_timeout(2500)
            o['pris'] = await pg.evaluate(PRIS)
            await pg.close()
        hs = {}
        for w in (320, 375, 390, 414, 768, 1024, 1280, 1440, 1920):
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            await pg.goto(URL); await pg.wait_for_timeout(1500)
            H = await pg.evaluate("document.documentElement.scrollHeight"); mx = 0
            for y in range(0, H, 800):
                await pg.evaluate(f"scrollTo(0,{y})"); await pg.wait_for_timeout(50)
                mx = max(mx, await pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth"))
            hs[w] = mx; await pg.close()
        out['hscroll'] = hs
        await b.close()
    open('measure21.json', 'w', encoding='utf-8').write(json.dumps(out, indent=1, ensure_ascii=False))
    for w in (1920, 1440, 390):
        o = out[w]
        print(w, 'split', o['split'], 'seam_h', o['seam_h'], 'pris', o['pris'])
        for k in ('tes_ritning', 'calyx_horai', 'horai_pris'): print('  ', k, o[k])
        print('   bands', {k: v for k, v in o['bands'].items() if 'sample' not in k}, o['bands']['sliver_sample'][:3])
    print('hscroll', out['hscroll'])

asyncio.run(main())
