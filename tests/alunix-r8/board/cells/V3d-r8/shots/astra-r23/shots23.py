"""astra-r23: en skarmbild per sida. Varje lage nas med mouse.wheel i en ren sida."""
import asyncio, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = Path(r"C:\Users\Anton L\anti-slop-design\tests\alunix-r8\runs\V3d\shots\astra-r23")

SHOTS = {
 1920: [("A01",6400,""),("A02",6467,"t0"),("A03",6560,""),("A04",6616,"t1"),
        ("A05",6720,""),("A06",6764,"t2"),("A07",6800,""),("A08",6880,""),
        ("A09",6912,"t3"),("A10",7000,""),("A11",7061,"t4"),("A12",7160,""),
        ("A13",7280,""),("A14",7440,""),("A15",7600,""),("A16",7700,"kapitelskarm"),
        ("A17",8000,""),
        ("C01",16250,"infor case"),("C02",16527,"case-kapitel"),("C03",16850,""),
        ("C04",17150,""),("C05",17436,"calyx topp"),("C06",18084,"calyx-01"),
        ("P01",29400,""),("P02",29668,"pris")],
 390:  [("A01",5800,""),("A02",5869,"t0"),("A03",5960,""),("A04",6004,"t1"),
        ("A05",6080,""),("A06",6138,"t2"),("A07",6200,""),("A08",6273,"t3"),
        ("A09",6360,""),("A10",6408,"t4"),("A11",6520,""),("A12",6700,""),
        ("A13",6900,""),("A14",7050,"kapitelskarm"),("A15",7300,""),
        ("C01",12000,"infor case"),("C02",12241,"case-kapitel"),("C03",12500,""),
        ("C04",12800,""),("C05",13085,"calyx topp"),("C06",13692,"calyx-01"),
        ("P01",23950,""),("P02",24189,"pris")],
}
DIMS = {1920:930, 390:844}

async def goto(pg,url):
    for a in range(6):
        try:
            await pg.goto(url, wait_until="load", timeout=40000); return
        except Exception:
            if a==5: raise

async def settle(pg):
    await pg.evaluate("""Promise.all([...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight&&!i.complete}).map(i=>new Promise(res=>{i.onload=i.onerror=res;setTimeout(res,4000)})))""")
    for f in pg.frames[1:]:
        try:
            await f.wait_for_load_state("load", timeout=8000)
        except Exception: pass

async def wheel_to(pg,y,step=140):
    await pg.mouse.move(pg.viewport_size["width"]/2, pg.viewport_size["height"]/2)
    for _ in range(1500):
        cur = await pg.evaluate("scrollY")
        d = y-cur
        if abs(d)<2: break
        await pg.mouse.wheel(0, max(-step,min(step,d)))
        await pg.wait_for_timeout(22)
    await pg.wait_for_timeout(2200)
    await settle(pg)
    await pg.wait_for_timeout(1000)
    return await pg.evaluate("scrollY")

async def main():
    log = {}
    async with async_playwright() as p:
        br = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w in (1920,390):
            h = DIMS[w]
            for rid,ty,note in SHOTS[w]:
                ctx = await br.new_context(viewport={"width":w,"height":h})
                pg = await ctx.new_page()
                await goto(pg,URL)
                await pg.wait_for_timeout(1400)
                y = await wheel_to(pg,ty)
                hs = await pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
                path = OUT/f"{rid}-{w}.png"
                await pg.screenshot(path=str(path))
                log[f"{rid}-{w}"] = {"target":ty,"landed":y,"note":note,"hscroll":hs}
                print(rid,w,ty,y,hs,note,flush=True)
                await ctx.close()
                (OUT/"shots23.json").write_text(json.dumps(log,indent=1,ensure_ascii=False))
        await br.close()

asyncio.run(main())
