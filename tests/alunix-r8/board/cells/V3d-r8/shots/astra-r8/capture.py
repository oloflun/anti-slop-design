"""astra-r8: egna par-bilder. Målläget hämtas ur ett preview-/mätanrop i en separat sida och
nås sedan i en ren sida med mouse.wheel (aldrig scrollTo). En skärmbild per sida.
Argument: bredder att köra (default 1440 390 768), valfritt rad-id-filter efter '--'."""
import asyncio, json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from playwright.async_api import async_playwright

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/astra-r8"
REF = BASE / "tests/alunix-r8/runs/V3c/shots/fasA"

H1, W1 = "hoy-1440/", "hoy-390/"
ROWS = [
    ("P01", ("y", 0), H1 + "hoy-webb-1440--s00.png", W1 + "hoy-home-390--s00.png"),
    ("P02", ("preview", "back"), H1 + "hoy-home-1440--s00.png", W1 + "hoy-home-390--s00.png"),
] + [
    (f"P03-{n}", ("previewY", f"thesis-0{n}"), H1 + "hoy-home-1440--s01.png", W1 + "hoy-home-390--s01.png") for n in range(1, 6)
] + [
    ("P04-curtain", ("previewY", "curtain"), H1 + "hoy-home-1440--s03.png", W1 + "hoy-home-390--s03.png"),
    ("P04-chapter", ("previewY", "chapter"), H1 + "hoy-home-1440--s03.png", W1 + "hoy-home-390--s03.png"),
    ("P07", ("previewY", "process-01"), H1 + "hoy-home-1440--s03.png", W1 + "hoy-webb-390--s00.png"),
    ("P08", ("previewY", "process-02"), H1 + "hoy-webb-1440--s08.png", W1 + "hoy-webb-390--s08.png"),
    ("P09", ("previewY", "process-03"), H1 + "hoy-home-1440--s06.png", W1 + "hoy-home-390--s05.png"),
    ("P10", ("previewY", "process-04"), H1 + "hoy-home-1440--s07.png", W1 + "hoy-home-390--s06.png"),
    ("P11", ("previewY", "process-05"), H1 + "hoy-webb-1440--s07.png", W1 + "hoy-webb-390--s05.png"),
    ("P12", ("previewY", "process-06"), H1 + "hoy-webb-1440--s01.png", W1 + "hoy-webb-390--s01.png"),
    ("P13", ("previewY", "process-07"), H1 + "hoy-webb-1440--s10.png", W1 + "hoy-webb-390--s09.png"),
    ("P14", ("previewY", "cases"), H1 + "hoy-webb-1440--s04.png", W1 + "hoy-webb-390--s03.png"),
] + [
    (f"P17-{n}", ("previewY", f"case-calyx-0{n}"), H1 + "hoy-webb-1440--s02.png", W1 + "hoy-webb-390--s01.png") for n in (1, 3, 5)
] + [
    ("P18", ("previewY", "bridge"), H1 + "hoy-webb-1440--s03.png", W1 + "hoy-webb-390--s02.png"),
] + [
    (f"P19-{n}", ("previewY", f"case-horai-0{n}"), H1 + "hoy-home-1440--s02.png", W1 + "hoy-home-390--s02.png") for n in (1, 3, 6)
] + [
    ("P20", ("js", "scrollY+document.querySelector('#pris').getBoundingClientRect().top-innerHeight*0.5"), H1 + "hoy-home-1440--s08.png", "insign-390/insign-390--s10.png"),
    ("P15b", ("js", "document.documentElement.scrollHeight-2*innerHeight"), H1 + "hoy-home-1440--s08.png", "insign-390/insign-390--s10.png"),
    ("P15a", ("js", "document.documentElement.scrollHeight-innerHeight"), H1 + "hoy-home-1440--s09.png", "insign-390/insign-390--s10.png"),
]
ONLY768 = ("P03-", "P14", "P17-", "P18", "P19-")


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
        await pg.wait_for_timeout(3500)
        return await pg.evaluate("scrollY")
    await goto(pg, URL)
    await pg.wait_for_timeout(1500)
    return await pg.evaluate(arg)


async def settle_media(pg):
    await pg.evaluate("""Promise.all([...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight&&!i.complete}).map(i=>new Promise(res=>{i.onload=i.onerror=res;setTimeout(res,4000)})))""")
    for f in pg.frames[1:]:
        try:
            await f.wait_for_load_state("load", timeout=8000)
            await f.evaluate("""Promise.all([...document.images].filter(i=>{const r=i.getBoundingClientRect();return r.bottom>0&&r.top<innerHeight&&!i.complete}).map(i=>new Promise(res=>{i.onload=i.onerror=res;setTimeout(res,4000)})))""")
        except Exception:
            pass


async def wheel_to(pg, y, step=120):
    await pg.mouse.move(pg.viewport_size["width"] / 2, pg.viewport_size["height"] / 2)
    for _ in range(1200):
        cur = await pg.evaluate("scrollY")
        d = y - cur
        if abs(d) < 2: break
        await pg.mouse.wheel(0, max(-step, min(step, d)))
        await pg.wait_for_timeout(40)
    await pg.wait_for_timeout(2500)
    await settle_media(pg)
    await pg.wait_for_timeout(1200)
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
    args = sys.argv[1:]
    only = set(args[args.index("--") + 1:]) if "--" in args else set()
    widths = [int(a) for a in (args[:args.index("--")] if "--" in args else args)] or [1440, 390, 768]
    (OUT / "ours").mkdir(parents=True, exist_ok=True)
    logp = OUT / "positions.json"
    log = json.loads(logp.read_text()) if logp.exists() else {}
    dims = {1440: 900, 390: 844, 768: 1024}
    async with async_playwright() as p:
        br = await p.chromium.launch()
        for w in widths:
            h = dims[w]
            for rid, how, r1440, r390 in ROWS:
                if only and rid not in only: continue
                if w == 768 and not rid.startswith(ONLY768): continue
                ctx = await br.new_context(viewport={"width": w, "height": h})
                pg = await ctx.new_page()
                ours = OUT / "ours" / f"{rid}-{w}.png"
                if how[0] == "preview":
                    await goto(pg, URL + "?preview=" + how[1]); await pg.wait_for_timeout(2500); y = 0; ty = 0
                else:
                    ty = await target_y(pg, how)
                    await goto(pg, URL); await pg.wait_for_timeout(1500)
                    y = await wheel_to(pg, ty)
                hs = await pg.evaluate("document.documentElement.scrollWidth-innerWidth")
                log[f"{rid}-{w}"] = {"target": ty, "landed": y, "hscroll": hs}
                await pg.screenshot(path=str(ours))
                if w != 768:
                    ref = REF / (r1440 if w == 1440 else r390)
                    compose(ours, ref, OUT / f"{rid}-{w}.png", f"{rid}-{w}  scrollY {y:.0f}  |  V3d vänster, ref höger: {ref.name}")
                print(rid, w, ty, y, hs, flush=True)
                await ctx.close()
                logp.write_text(json.dumps(log, indent=1))
        await br.close()

asyncio.run(main())
