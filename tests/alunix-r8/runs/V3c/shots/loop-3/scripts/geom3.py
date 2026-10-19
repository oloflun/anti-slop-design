"""geom3.py: page geometry at 1440x900 and 390x844 for the HELHET ticks (H-01, H-04, H-05,
H-07, H-12, H-13, H-14) and for the probe start positions."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """() => {
  const q = s => document.querySelector(s);
  const box = s => { const e = q(s); if (!e) return null; const r = e.getBoundingClientRect();
    return {top: Math.round(r.top + scrollY), h: Math.round(r.height), left: Math.round(r.left), w: Math.round(r.width)}; };
  const sels = ['section.hero','.stagger','.panel-thesis','.calyx-fig','.panel-giant','.horai-fig','.price','#process','#principer','footer.close','.giant','.hero-sub','.card-cta','.hero-headline','.plate-card','.thesis-figure','.mailto, .close a[href^="mailto"]'];
  const o = {docH: document.documentElement.scrollHeight, vh: innerHeight, vw: innerWidth};
  for (const s of sels) o[s] = box(s);
  const g = q('.giant'); if (g) { const cs = getComputedStyle(g); o.giantFont = cs.fontSize; o.giantLS = cs.letterSpacing;
    const rng = document.createRange(); const tn = [...g.childNodes].filter(n => n.nodeType === 3 && /VARUM/.test(n.textContent))[0];
    if (tn) { const i = tn.textContent.indexOf('VARUM'); rng.setStart(tn, i); rng.setEnd(tn, tn.textContent.length); o.wordRects = rng.getClientRects().length; }
    o.giantLines = Math.round(g.getBoundingClientRect().height / parseFloat(cs.lineHeight)); }
  const sub = q('.hero-sub') || q('.card-cta');
  return o;
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for w, h in ((1440, 900), (390, 844)):
        p = b.new_page(viewport={"width": w, "height": h}, reduced_motion="reduce")
        p.goto(URL, wait_until="load"); p.wait_for_timeout(1500)
        out[f"{w}"] = p.evaluate(JS)
        p.close()
    b.close()
print(json.dumps(out, indent=1))
json.dump(out, open(sys.argv[1], "w"), indent=1)
