import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for w,h in [(1920,930),(1920,1080),(1440,900)]:
            pg=await b.new_page(viewport={'width':w,'height':h})
            await pg.goto("http://localhost:3090/tests/alunix-r8/runs/V3d/index.html?preview=process-06"); await pg.wait_for_timeout(4000)
            r=await pg.evaluate("""(()=>{const s=document.querySelector('.process-stick');const k=[...s.querySelectorAll('*')].map(e=>e.getBoundingClientRect()).filter(r=>r.width>200).sort((a,b)=>b.width*b.height-a.width*a.height)[0];const r=s.getBoundingClientRect();return {stick:[Math.round(r.left),Math.round(r.width),Math.round(r.height)],inner:k?[Math.round(k.left),Math.round(k.width),Math.round(k.height)]:null,vw:innerWidth}})()""")
            print(w,h,r, round(r['stick'][1]/w*100,1))
            await pg.close()
        await b.close()
asyncio.run(main())
