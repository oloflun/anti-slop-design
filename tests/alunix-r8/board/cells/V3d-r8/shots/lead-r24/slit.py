"""R24: var ar --slit-p nollskild? Diagnos for Fel 1:s tackning och Fel 3.

--slit-p klipper stegtextens slot. Den deklareras per li och lacker pa
--slit-start/--s/--e, som JS skriver. En kontroll som bara ser 0 matar
ingenting - det har skriptet hittar fonstret dar den faktiskt ror sig.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

READ = """() => {
  const ch = document.querySelector('.process-chapter');
  const out = {tx: parseFloat(getComputedStyle(ch).getPropertyValue('--tx')),
               y: window.scrollY, bands: []};
  /* --slit-p deklareras pa .step-band (rad ~1459), INTE pa li - att lasa den
     ur li ger det ÄRVDA initialvardet 0 och matar ingenting. */
  document.querySelectorAll('.process-steps li').forEach((li, i) => {
    const cs = getComputedStyle(li.querySelector('.step-band') || li);
    const f = p => { const v = parseFloat(cs.getPropertyValue(p)); return v !== v ? 'NaN' : +v.toFixed(3); };
    out.bands.push({i: i + 1, slit_p: f('--slit-p'),
                    slit_start: f('--slit-start'), s: f('--s'), e: f('--e')});
  });
  return out;
}"""


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': 1920, 'height': 930})
        await pg.goto(URL)
        await pg.wait_for_timeout(2500)
        await pg.mouse.move(960, 465)
        proc_top = await pg.evaluate(
            "() => { const e = document.getElementById('process');"
            " return e.getBoundingClientRect().top + window.scrollY; }")
        proc_h = await pg.evaluate("() => document.getElementById('process').offsetHeight")
        rows = []
        cur = 0
        for frac in (0.35, 0.45, 0.55, 0.65, 0.75, 0.85):
            target = int(proc_top + frac * proc_h)
            while cur < target:
                d = min(200, target - cur)
                await pg.mouse.wheel(0, d); cur += d
                await pg.wait_for_timeout(3)
            await pg.wait_for_timeout(450)
            r = await pg.evaluate(READ)
            rows.append(r)
        await b.close()

    for r in rows:
        live = [f"{x['i']}:{x['slit_p']}" for x in r['bands']
                if isinstance(x['slit_p'], float) and 0 < x['slit_p'] < 1]
        zero = [str(x['i']) for x in r['bands'] if x['slit_p'] == 0]
        one = [str(x['i']) for x in r['bands'] if x['slit_p'] == 1]
        print(f"y{r['y']:<7} tx={r['tx']:<8.3f} 0<slit<1: {live or '-'}")
        print(f"          =0: {','.join(zero) or '-'}   =1: {','.join(one) or '-'}")
    print()
    b0 = rows[0]['bands'][0]
    print("rad 1 vid forsta provet:", b0)
    anymid = any(isinstance(x['slit_p'], float) and 0 < x['slit_p'] < 1
                 for r in rows for x in r['bands'])
    print("\n--slit-p sedd nollskild (<1, >0) i minst ett lage:", anymid)
    open("slit-probe.json", 'w').write(json.dumps(rows, indent=1))


asyncio.run(main())
