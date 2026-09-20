"""astra-r5: egna par-bilder. Positionen hämtas ur ett preview-/mätanrop i en separat sida,
och nås sedan i en ren sida med mouse.wheel (aldrig scrollTo). En skärmbild per sida."""
import asyncio, json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from playwright.async_api import async_playwright

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/astra-r5"
REF = BASE / "tests/alunix-r8/runs/V3c/shots/fasA"

# id, how to find target y, ref1440, ref390
ROWS = [
    ("P01", ("y", 0), "hoy-1440/hoy-webb-1440--s00.png", "hoy-390/hoy-home-390--s00.png"),
    ("P02", ("preview", "back"), "hoy-1440/hoy-home-1440--s00.png", "hoy-390/hoy-home-390--s00.png"),
    ("P03", ("js", "(()=>{const r=document.querySelector('.panel-thesis').getBoundingClientRect();return scrollY+r.top-innerHeight*0.12})()"), "hoy-1440/hoy-home-1440--s01.png", "hoy-390/hoy-home-390--s01.png"),
    ("P04", ("previewY", "ledger"), "hoy-1440/hoy-webb-1440--s03.png", "hoy-390/hoy-webb-390--s02.png"),
    ("P05", ("js", "(()=>{const r=document.querySelector('.horai-fig').getBoundingClientRect();return scrollY+r.top+r.height/2-innerHeight/2})()"), "insign-1440/insign-1440--s04.png", "insign-390/insign-390--s07.png"),
    ("P06", ("js", "scrollY+document.querySelector('#process').getBoundingClientRect().top"), "hoy-1440/hoy-home-1440--s03.png", "hoy-390/hoy-home-390--s03.png"),
    ("P07", ("previewY", "process-01"), "hoy-1440/hoy-home-1440--s03.png", "hoy-390/hoy-webb-390--s00.png"),
    ("P08", ("previewY", "process-02"), "hoy-1440/hoy-webb-1440--s08.png", "hoy-390/hoy-webb-390--s08.png"),
    ("P09", ("previewY", "process-03"), "hoy-1440/hoy-home-1440--s06.png", "hoy-390/hoy-home-390--s05.png"),
    ("P10", ("previewY", "process-04"), "hoy-1440/hoy-home-1440--s07.png", "hoy-390/hoy-home-390--s06.png"),
    ("P11", ("previewY", "process-05"), "hoy-1440/hoy-webb-1440--s07.png", "hoy-390/hoy-webb-390--s05.png"),
    ("P12", ("previewY", "process-06"), "hoy-1440/hoy-webb-1440--s01.png", "hoy-390/hoy-webb-390--s01.png"),
    ("P13", ("previewY", "process-07"), "hoy-1440/hoy-webb-1440--s10.png", "hoy-390/hoy-webb-390--s09.png"),
    ("P14", ("js", "(()=>{const r=document.querySelector('#principer').getBoundingClientRect();return scrollY+r.top+r.height/2-innerHeight/2})()"), "hoy-1440/hoy-webb-1440--s04.png", "hoy-390/hoy-webb-390--s02.png"),
    ("P15b", ("js", "document.documentElement.scrollHeight-2*innerHeight"), "hoy-1440/hoy-home-1440--s08.png", "insign-390/insign-390--s10.png"),
    ("P15a", ("js", "document.documentElement.scrollHeight-innerHeight"), "hoy-1440/hoy-home-1440--s09.png", "insign-390/insign-390--s10.png"),
]


async def goto(pg, url):
    for a in range(6):
        try:
            await pg.goto(url, wait_until="load", timeout=30000); return
        except Exception:
            if a == 5: raise


async def target_y(pg, how):
    kind, arg = how
    if kind == "y": return arg
    if kind == "previewY":
        await goto(pg, URL + "?preview=" + arg)
        await pg.wait_for_timeout(2500)
        return await pg.evaluate("scrollY")
    await goto(pg, URL)
    await pg.wait_for_timeout(1200)
    return await pg.evaluate(arg)


async def wheel_to(pg, y):
    await pg.mouse.move(pg.viewport_size["width"] / 2, pg.viewport_size["height"] / 2)
    for _ in range(400):
        cur = await pg.evaluate("scrollY")
        d = y - cur
        if abs(d) < 2: break
        await pg.mouse.wheel(0, max(-120, min(120, d)))
        await pg.wait_for_timeout(45)
    await pg.wait_for_timeout(2500)
    # vänta tills bilder i viewporten är laddade
    await pg.evaluate("""Promise.all([...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight&&!i.complete}).map(i=>new Promise(res=>{i.onload=i.onerror=res;setTimeout(res,4000)})))""")
    await pg.wait_for_timeout(800)
    return await pg.evaluate("scrollY")


def compose(ours, ref, out, label):
    a = Image.open(ours).convert("RGB"); b = Image.open(ref).convert("RGB")
    h = min(a.height, b.height)
    a = a.resize((int(a.width * h / a.height), h)); b = b.resize((int(b.width * h / b.height), h))
    s = Image.new("RGB", (a.width + 24 + b.width, h + 26), "white")
    s.paste(a, (0, 0)); s.paste(b, (a.width + 24, 0))
    try: f = ImageFont.truetype("arial.ttf", 14)
    except Exception: f = None
    ImageDraw.Draw(s).text((4, h + 5), label, fill="black", font=f)
    s.save(out)


async def main():
    only = set(sys.argv[1:])
    (OUT / "ours").mkdir(parents=True, exist_ok=True)
    log = {}
    async with async_playwright() as p:
        br = await p.chromium.launch()
        for w, h in [(1440, 900), (390, 844)]:
            for rid, how, r1440, r390 in ROWS:
                if only and rid not in only: continue
                ctx = await br.new_context(viewport={"width": w, "height": h})
                pg = await ctx.new_page()
                ours = OUT / "ours" / f"{rid}-{w}.png"
                if how[0] == "preview":
                    await goto(pg, URL + "?preview=" + how[1]); await pg.wait_for_timeout(2500); y = 0
                else:
                    ty = await target_y(pg, how)
                    await goto(pg, URL); await pg.wait_for_timeout(1500)
                    y = await wheel_to(pg, ty)
                    log[f"{rid}-{w}"] = {"target": ty, "landed": y}
                await pg.screenshot(path=str(ours))
                ref = REF / (r1440 if w == 1440 else r390)
                compose(ours, ref, OUT / f"{rid}-{w}.png", f"{rid}-{w}  scrollY {y:.0f}  |  V3d vänster, ref höger: {ref.name}")
                print(rid, w, y, flush=True)
                await ctx.close()
        await br.close()
    (OUT / "positions.json").write_text(json.dumps(log, indent=1))

asyncio.run(main())
