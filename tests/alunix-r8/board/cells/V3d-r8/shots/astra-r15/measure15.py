"""astra-r15: ridå (rubrikklipp, hjul 20px), casen (överlagrade steg/case-line, hjul 20px),
delade ord i rubriker, hscroll 320-1920. Chromium utan --hide-scrollbars."""
import asyncio, json, re
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
SW = open('../r12/scripts/sweep.py', encoding='utf-8').read()
SWEEP_JS = re.search(r'SWEEP_JS = """(.*?)"""', SW, re.S).group(1).replace('\\\\', '\\')
HEAD = "h1, h2, h3, .ts, .statement, .close-mailto"
CASEJS = r"""(sel)=>{const s=document.querySelector(sel);const vis=[];
 for(const li of s.querySelectorAll('.cs')){const r=li.getBoundingClientRect();const m=/inset\(([^)]*)\)/.exec(getComputedStyle(li).clipPath);
  let t=0,b=0;if(m){const k=m[1].trim().split(/\s+/).map(x=>x.endsWith('%')?parseFloat(x)/100*r.height:parseFloat(x));t=k[0];b=k.length>2?k[2]:k[0];}
  const vh=r.height-t-b;if(vh>1)vis.push({i:li.style.getPropertyValue('--i').trim(),vt:Math.round(r.top+t),vb:Math.round(r.bottom-b),h3full:(()=>{const h=li.querySelector('h3').getBoundingClientRect();return h.top>=r.top+t-0.5&&h.bottom<=r.bottom-b+0.5})()});}
 const cl=s.querySelector('.case-line');const clr=cl.getBoundingClientRect();const clo=parseFloat(getComputedStyle(cl).opacity);
 const st=s.querySelector('.case-stage')||s;const sr=st.getBoundingClientRect();
 return {ps:parseFloat(getComputedStyle(s).getPropertyValue('--sc-ps')),vis,cl:{op:clo,h:Math.round(clr.height),b:Math.round(clr.bottom)},stageB:Math.round(Math.min(sr.bottom,innerHeight)),y:scrollY}}"""
SPLIT = r"""(sel)=>{const out=[];for(const el of document.querySelectorAll(sel)){if(!el.getClientRects().length)continue;
 const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){const re=/\S+/g;let m;while(m=re.exec(n.data)){const r=document.createRange();r.setStart(n,m.index);r.setEnd(n,m.index+m[0].length);
 const tops=new Set([...r.getClientRects()].filter(q=>q.width>0).map(q=>Math.round(q.top)));if(tops.size>1)out.push({el:el.className||el.tagName,w:m[0]});}}}return out}"""


async def wheel_to(pg, y, step=120):
    for _ in range(3000):
        d = y - await pg.evaluate("scrollY")
        if abs(d) < 2: break
        await pg.mouse.wheel(0, max(-step, min(step, d))); await pg.wait_for_timeout(30)


async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, h in [(1920, 930), (1440, 900), (390, 844)]:
            o = out[w] = {}
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(URL); await pg.wait_for_timeout(2500)
            await pg.mouse.move(w / 2, h / 2)
            o['split'] = await pg.evaluate(SPLIT, ".ts,.case-name,.case-line,.cs h3,.process-title,.cases-title,.bridge-title,.statement,h1,h2,h3")
            r0 = await pg.evaluate("(()=>{const t=document.getElementById('tes');return t.getBoundingClientRect().top+scrollY+t.offsetHeight-2*innerHeight})()")
            r1 = await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY+1.3*innerHeight})()")
            await wheel_to(pg, r0); await pg.wait_for_timeout(800)
            hits = []; n = 0
            while (await pg.evaluate("scrollY")) < r1 and n < 400:
                await pg.mouse.wheel(0, 20); await pg.wait_for_timeout(45); n += 1
                hh = await pg.evaluate(SWEEP_JS, HEAD)
                y = await pg.evaluate("scrollY")
                for x in hh: x['y'] = y
                hits += hh
            o['rida'] = {'frames': n, 'hits': len(hits), 'sample': hits[:6],
                         'kinds': sorted({x['heading'][:40] + ' <- ' + str(x['hitCls'])[:30] for x in hits})}
            for sel in ('#case-calyx', '#case-horai'):
                c0 = await pg.evaluate(f"(()=>{{const s=document.querySelector('{sel}');return s.getBoundingClientRect().top+scrollY-innerHeight*0.2}})()")
                c1 = await pg.evaluate(f"(()=>{{const s=document.querySelector('{sel}');return s.getBoundingClientRect().top+scrollY+s.offsetHeight-innerHeight}})()")
                await wheel_to(pg, c0); await pg.wait_for_timeout(800)
                fr = []; n = 0
                while (await pg.evaluate("scrollY")) < c1 and n < 700:
                    await pg.mouse.wheel(0, 20); await pg.wait_for_timeout(45); n += 1
                    fr.append(await pg.evaluate(CASEJS, sel))
                dbl = [f for f in fr if len(f['vis']) > 1]
                ovl = [f for f in fr if f['cl']['op'] > 0.02 and any(v['i'] != '0' for v in f['vis'])]
                noh3 = [f for f in fr if f['vis'] and not any(v['h3full'] for v in f['vis'])]
                over = [f for f in fr if f['vis'] and max(v['vb'] for v in f['vis']) > f['stageB'] and 0 < f['ps'] < 1]
                o[sel] = {'frames': n, 'double': len(dbl), 'caseline_with_step2plus': len(ovl), 'no_full_h3': len(noh3),
                          'no_full_h3_ps': [round(f['ps'], 3) for f in noh3][:80], 'below_stage': len(over), 'below_sample': over[:3]}
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
    open('measure15.json', 'w', encoding='utf-8').write(json.dumps(out, indent=1, ensure_ascii=False))
    for w in (1920, 1440, 390):
        o = out[w]; print(w, 'split', o['split'], 'rida', {k: o['rida'][k] for k in ('frames', 'hits', 'kinds')})
        for s in ('#case-calyx', '#case-horai'): print('  ', s, {k: v for k, v in o[s].items() if k != 'below_sample'})
    print('hscroll', hs)

asyncio.run(main())
