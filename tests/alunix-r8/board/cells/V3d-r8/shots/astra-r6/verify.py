"""astra-r6: kontroll av r5:s fyra material_fixes. Hjul (mouse.wheel) överallt utom preview-mätningar."""
import asyncio, json
from PIL import Image
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"


async def wheel(pg, y):
    for _ in range(600):
        d = y - await pg.evaluate("scrollY")
        if abs(d) < 2: break
        await pg.mouse.wheel(0, max(-120, min(120, d))); await pg.wait_for_timeout(40)
    await pg.wait_for_timeout(1100)

EXIT = r"""(()=>{const lis=[...document.querySelectorAll('.process-steps > li')];const li=lis[lis.length-1];const band=li.querySelector('.step-band')||li;const r=band.getBoundingClientRect();const st=document.querySelector('.process-stick').getBoundingClientRect();
const kids=[...band.querySelectorAll('*')].filter(e=>e.children.length==0&&e.textContent.trim()).map(e=>{const b=e.getBoundingClientRect();return [e.textContent.trim().slice(0,14),Math.round(b.top),Math.round(b.bottom)]});
return {y:scrollY,band:[Math.round(r.top),Math.round(r.bottom)],stickTop:Math.round(st.top),stickBottom:Math.round(st.bottom),cut:kids.filter(k=>k[1]<Math.round(st.top)&&k[2]>Math.round(st.top)).map(k=>k[0]),kids}})()"""
SHEET = r"""(()=>{const R=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.left),Math.round(b.top),Math.round(b.right),Math.round(b.bottom)]};const cs=(s,p)=>{const e=document.querySelector(s);return e?getComputedStyle(e)[p]:null};
return {y:scrollY,sheet:R('.process-sheet'),live:R('.process-sheet .p-live'),glyph:R('#p-glyph'),glyphOp:cs('#p-glyph','opacity'),rev:R('#p-rev'),revOp:cs('#p-rev','opacity'),title:R('#p-title'),crev:R('#p-c-rev'),crevOp:cs('#p-c-rev','opacity'),camfade:getComputedStyle(document.querySelector('#process')).getPropertyValue('--cam-fade')}})()"""
GIANT = r"""(()=>{const h=document.querySelector('#giant-section h2.giant');const b=h.getBoundingClientRect();const head=document.querySelector('.giant-head').getBoundingClientRect();const plate=document.querySelector('#giant-section').getBoundingClientRect();
const split=[];const lines=new Set();const tw=document.createTreeWalker(h,NodeFilter.SHOW_TEXT);let t;while((t=tw.nextNode())){const re=/\S+/g;let m;while((m=re.exec(t.data))){const r=document.createRange();r.setStart(t,m.index);r.setEnd(t,m.index+m[0].length);const tops=new Set([...r.getClientRects()].map(x=>Math.round(x.top)));tops.forEach(v=>lines.add(v));if(tops.size>1)split.push(m[0])}}
return {y:scrollY,fs:getComputedStyle(h).fontSize,h2:[Math.round(b.left),Math.round(b.top),Math.round(b.right),Math.round(b.bottom)],lines:lines.size,split,headH:Math.round(head.height),headPct:+(head.height/innerHeight*100).toFixed(1),plate:[Math.round(plate.left),Math.round(plate.top),Math.round(plate.width)],inVp:b.top>=0&&b.bottom<=innerHeight&&b.left>=0&&b.right<=innerWidth,scrub:getComputedStyle(h).getPropertyValue('--scrub')}})()"""


async def main():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        # 1. utgångssekvens 1440, 40 px
        pg = await b.new_page(viewport={"width": 1440, "height": 900}); await pg.goto(URL, wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(720, 450)
        ims = []; out['exit'] = []
        for y in range(13760, 14480, 40):
            await wheel(pg, y); f = f"exit-{y}.png"; await pg.screenshot(path=f); ims.append(Image.open(f)); out['exit'].append(await pg.evaluate(EXIT))
        tw, th, cols = 432, 270, 6
        S = Image.new('RGB', (cols * (tw + 6), ((len(ims) + cols - 1) // cols) * (th + 6)), 'white')
        for k, im in enumerate(ims): S.paste(im.convert('RGB').resize((tw, th)), ((k % cols) * (tw + 6), (k // cols) * (th + 6)))
        S.save("strip-exit-1440.png"); await pg.close()
        # 2. steg 05/06/07 vid 390 och 768
        out['sheet'] = {}
        for w, h in [(390, 844), (768, 1024)]:
            for m in ["process-05", "process-06", "process-07"]:
                pg = await b.new_page(viewport={"width": w, "height": h}); await pg.goto(URL + "?preview=" + m, wait_until="load"); await pg.wait_for_timeout(2500)
                ty = await pg.evaluate("scrollY"); out['sheet'][f"{w}-{m}-preview"] = await pg.evaluate(SHEET); await pg.close()
                pg = await b.new_page(viewport={"width": w, "height": h}); await pg.goto(URL, wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(w / 2, h / 2)
                await wheel(pg, ty); await pg.wait_for_timeout(1500)
                out['sheet'][f"{w}-{m}-wheel"] = await pg.evaluate(SHEET); await pg.screenshot(path=f"steg-{w}-{m}.png"); await pg.close()
        # 3. jätten
        out['giant'] = {}
        for w in [768, 1024, 1280, 1440, 1920]:
            pg = await b.new_page(viewport={"width": w, "height": 900}); await pg.goto(URL + "?preview=ledger", wait_until="load"); await pg.wait_for_timeout(2500)
            ty = await pg.evaluate("scrollY"); out['giant'][f"{w}-preview"] = await pg.evaluate(GIANT); await pg.close()
            pg = await b.new_page(viewport={"width": w, "height": 900}); await pg.goto(URL, wait_until="load"); await pg.wait_for_timeout(1500); await pg.mouse.move(w / 2, 450)
            out['giant'][f"{w}-top-scrub0"] = await pg.evaluate(GIANT)
            await wheel(pg, ty); await pg.wait_for_timeout(1500)
            out['giant'][f"{w}-wheel"] = await pg.evaluate(GIANT); await pg.screenshot(path=f"giant-{w}.png"); await pg.close()
        await b.close()
    open("verify.json", "w").write(json.dumps(out, indent=1))

asyncio.run(main())
