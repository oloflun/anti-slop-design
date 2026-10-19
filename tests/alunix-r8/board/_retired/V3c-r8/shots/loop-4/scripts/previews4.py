"""previews4.py <out-dir> <base-url>: every ?preview= mode at 1440x900 and 390x844,
wait_until="load" + 2 s (R9 gate wording). Also logs --kN, --sc-ps and --e(N) per
process preview so H-30 is a number, not only a picture."""
import asyncio, sys, json
from pathlib import Path
from playwright.async_api import async_playwright
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
MODES = ["front", "mid", "back", "ledger", "bleed"] + [f"process-0{i}" for i in range(1, 8)]
JS = """(n) => {
  const p = document.getElementById('process'); const cs = getComputedStyle(p);
  const g = k => cs.getPropertyValue(k).trim();
  const off = id => { const e = document.getElementById(id); return e ? getComputedStyle(e).strokeDashoffset : null; };
  return {scrollY: scrollY, ps: g('--sc-ps'), k: g('--k'+n), s: g('--s'+n), e: g('--e'+n), sNext: g('--s'+(n+1)),
    outline: off('p-outline'), glyph: off('p-glyph'), dimw: off('p-dim-width'), stations: off('p-stations'),
    on: [...p.querySelectorAll('g[data-step][data-on]')].map(e => e.getAttribute('data-step')).join(',')};
}"""
async def main(out_dir, base):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for w, h, tag in ((1440, 900, "1440"), (390, 844, "390")):
            for m in MODES:
                pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce")
                await pg.goto(f"{base}?preview={m}", wait_until="load", timeout=60000)
                await pg.wait_for_timeout(2000)
                await pg.screenshot(path=str(out / f"preview-{tag}-{m}.png"))
                line = f"preview-{tag}-{m}.png"
                if m.startswith("process"):
                    n = int(m[-1]); r = await pg.evaluate(JS, n); res[f"{tag}-{m}"] = r
                    line += f"  k{n}={r['k']} ps={r['ps']} e{n}={r['e']} sNext={r['sNext']} outline={r['outline']} glyph={r['glyph']} on={r['on']}"
                print(line)
                await pg.close()
        await b.close()
    json.dump(res, open(out / "preview_check4.json", "w"), indent=1)
asyncio.run(main(sys.argv[1], sys.argv[2]))
