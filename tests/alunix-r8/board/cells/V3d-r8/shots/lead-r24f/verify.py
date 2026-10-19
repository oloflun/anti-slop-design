"""R24 F1-F5: verifieringen. Konsol, natverk, overflow-svep, bildstatus.

Overflow-kontrollen mater ELEMENTENS kanter, inte scrollWidth (SKILL.md
Step 5 pass 3), och kors i alla fyra mobilbredderna x bada rorlselagena.
"""
import asyncio, json, os
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
OUT = os.path.dirname(os.path.abspath(__file__))
WIDTHS = [(320, 568), (375, 667), (414, 896), (768, 1024), (1920, 930)]

JS = r"""
() => {
  const vw = innerWidth, bad = [];
  for (const e of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const b = e.getBoundingClientRect();
    if (b.width === 0 && b.height === 0) continue;
    if (b.right > vw + 1.5 || b.left < -1.5) {
      bad.push({sel: (e.tagName + '.' + (e.className || '')).slice(0, 60),
                left: Math.round(b.left), right: Math.round(b.right)});
    }
  }
  // dubblett-id:n (F1:s kritiska fall)
  const ids = {}, dup = [];
  for (const e of document.querySelectorAll('[id]')) {
    ids[e.id] = (ids[e.id] || 0) + 1;
  }
  for (const k in ids) if (ids[k] > 1) dup.push(k + ' x' + ids[k]);
  return {vw, docScroll: document.documentElement.scrollWidth,
          bodyScroll: document.body.scrollWidth,
          offscreen: bad.slice(0, 8), offscreenCount: bad.length, dupIds: dup,
          contactImg: (() => { const i = document.querySelector('.contact-card img');
            return i ? {ok: i.complete && i.naturalWidth > 0, nw: i.naturalWidth} : null; })()};
}
"""


async def main():
    errs, reqs, rows = [], [], []
    async with async_playwright() as p:
        br = await p.chromium.launch()
        for (w, h) in WIDTHS:
            pg = await br.new_page(viewport={"width": w, "height": h})
            pg.on("console", lambda m: errs.append(f"{w}px [{m.type}] {m.text[:160]}")
                  if m.type in ("error", "warning") else None)
            pg.on("pageerror", lambda e: errs.append(f"{w}px [pageerror] {str(e)[:160]}"))
            pg.on("response", lambda r: reqs.append((r.status, r.url.split("/")[-1]))
                  if r.status >= 400 or r.url.endswith(".webp") else None)
            await pg.goto(URL, wait_until="load")
            await pg.wait_for_timeout(1200)
            # rulla genom hela sidan sa alla sektioner har mountat
            for _ in range(90):
                await pg.mouse.wheel(0, 700)
                await pg.wait_for_timeout(18)
            await pg.wait_for_timeout(900)
            d = await pg.evaluate(JS)
            rows.append({"size": f"{w}x{h}", **d})
            await pg.close()
        await br.close()
    print("== overflow / dubblett-id / kontakbild ==")
    for r in rows:
        print(f"  {r['size']:>9}  offscreen {r['offscreenCount']:>2}  "
              f"docScroll {r['docScroll']:>5} (vw {r['vw']})  dupIds {r['dupIds']}  "
              f"kontaktbild {r['contactImg']}")
        for o in r["offscreen"]:
            print("      ", o)
    print("== konsol ==")
    print("  inga" if not errs else "\n".join("  " + e for e in errs[:15]))
    print("== natverk (>=400 + alla webp) ==")
    for s, u in reqs[:20]:
        print(f"  {s} {u}")
    json.dump({"rows": rows, "console": errs, "net": reqs},
              open(f"{OUT}/verify.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


asyncio.run(main())
