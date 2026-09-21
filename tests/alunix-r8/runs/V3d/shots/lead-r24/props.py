"""R24 Fel 1: ar de numeriska custom properties REGISTRERADE?

Oregistrerad property -> getPropertyValue ger tokenstrommen
"clamp(0,calc((0.3214 - 0.2258) / 0.1613),1)", parseFloat ger NaN, och NaN
blir tyst 0 i varje filter. Kontrollen ska ge NaN mot trasigt lage och ett
tal mot lagat - darfor kors den mot bada.

Kontroll-varde: --x1 (px, oregistrerad ar RATT for en langd) maste ge ett tal
i BADA lagen. Den ar provet pa att matvagen sjalv fungerar: ger aven --x1 NaN
ar det lasaren som ar trasig, inte registreringen.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

READ = """() => {
  const num = (el, p) => {
    if (!el) return 'no-el';
    const raw = getComputedStyle(el).getPropertyValue(p);
    const v = parseFloat(raw);
    return {raw: raw.trim().slice(0, 70), val: isNaN(v) ? 'NaN' : v};
  };
  const ch = document.querySelector('.process-chapter');
  const caseEl = document.querySelector('.cases-chapter');
  const li = document.querySelector('.process-steps li');
  return {
    sc_ps: num(document.querySelector('#process'), '--sc-ps'),
    tx:    num(ch, '--tx'),
    cx:    num(caseEl, '--cx'),
    slit_p: num(li, '--slit-p'),
    x1_control: num(ch, '--x1')
  };
}"""


async def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "now"
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': 1920, 'height': 930})
        await pg.goto(URL)
        await pg.wait_for_timeout(2500)
        await pg.mouse.move(960, 465)
        rows = []
        # Malpunkter harledda ur elementen, inte hardkodade y:n: --cx och
        # --slit-p ar 0 utanfor sina egna akter, och en kontroll som bara ser
        # 0 matar ingenting. Varje property maste ses i ett lage dar den
        # faktiskt ar nollskild.
        targets = [0, 6880, 8200]
        for sel, frac in (('.process-steps li:nth-child(4)', 0.35),
                          ('.cases-chapter', 0.12),
                          ('.cases-chapter', 0.30)):
            y = await pg.evaluate(
                """([s, f]) => { const e = document.querySelector(s);
                     if (!e) return null;
                     const r = e.getBoundingClientRect();
                     return Math.round(r.top + window.scrollY + f * r.height
                                       - innerHeight * 0.5); }""", [sel, frac])
            if y is not None:
                targets.append(y)
        for target in targets:
            cur = await pg.evaluate("() => window.scrollY")
            step = 60 if target > cur else -60
            while (step > 0 and cur < target) or (step < 0 and cur > target):
                d = min(abs(step), abs(target - cur))
                await pg.mouse.wheel(0, d * (1 if step > 0 else -1))
                cur += d * (1 if step > 0 else -1)
                await pg.wait_for_timeout(2)
            await pg.wait_for_timeout(500)
            r = await pg.evaluate(READ)
            r['y'] = await pg.evaluate("() => window.scrollY")
            rows.append(r)
        await b.close()

    print(f"=== {tag} ===")
    for r in rows:
        print(f"y{r['y']:<6} sc_ps={r['sc_ps']['val']!s:<8} tx={r['tx']['val']!s:<8} "
              f"cx={r['cx']['val']!s:<8} slit_p={r['slit_p']['val']!s:<8} "
              f"| kontrol --x1={r['x1_control']['val']}")
    print()
    for key in ('tx', 'cx', 'slit_p'):
        vals = [r[key]['val'] for r in rows]
        if any(v == 'NaN' for v in vals):
            verdict = "NaN - OREGISTRERAD"
        elif any(v not in (0, 1) for v in vals if v != 'NaN'):
            verdict = "tal, och nollskilt i minst ett lage - registrerad"
        else:
            verdict = "tal men bara 0/1 - mattet ar svagt, se over malpunkterna"
        print(f"  {key:<8} {vals} -> {verdict}")
    print(f"  --x1     {[r['x1_control']['val'] for r in rows]} -> kontrol (px, ska vara tal i bada lagen)")
    print()
    print("  raw --tx:", rows[1]['tx']['raw'])
    open(f"props-{tag}.json", 'w').write(json.dumps(rows, indent=1))


asyncio.run(main())
