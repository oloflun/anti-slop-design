"""Case-texten vid 390/375: sista synliga glyfens underkant mot viewport/stage, per steg, med och utan synlig rullningslist."""
import asyncio, json
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JS = r"""([sel,k])=>{const s=document.querySelector(sel);const st=s.querySelector('.case-stage').getBoundingClientRect();
 const li=s.querySelectorAll('.cs')[k];
 const p=li.querySelector('p');const r=document.createRange();r.selectNodeContents(p);const rs=[...r.getClientRects()];const last=rs[rs.length-1];
 const cl=s.querySelector('.case-line').getBoundingClientRect();
 return {step:li.style.getPropertyValue('--i').trim(),lastBottom:Math.round(last.bottom),stageBottom:Math.round(st.bottom),vh:innerHeight,cw:document.documentElement.clientWidth,caseLineH:Math.round(cl.height)}}"""
async def main():
    out = []
    async with async_playwright() as p:
        for bars in (False, True):
            b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'] if bars else None)
            for w, h in [(390, 844), (375, 812)]:
                for sel, name, n in [('#case-horai', 'case-horai', 6), ('#case-calyx', 'case-calyx', 5)]:
                    for k in range(1, n + 1):
                        pg = await b.new_page(viewport={'width': w, 'height': h})
                        await pg.goto(URL + f"?preview={name}-0{k}"); await pg.wait_for_timeout(4000)
                        r = await pg.evaluate(JS, [sel, k-1]); r.update(bars=bars, w=w, mode=f"{name}-0{k}")
                        r['margin'] = min(r['stageBottom'], r['vh']) - r['lastBottom']
                        out.append(r); print(r, flush=True); await pg.close()
            await b.close()
    open('fit390.json', 'w').write(json.dumps(out, indent=1))
asyncio.run(main())
