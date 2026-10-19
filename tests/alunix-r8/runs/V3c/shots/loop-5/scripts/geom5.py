"""geom4.py <out.json>: page geometry at 1440x900 and 390x844 for the HELHET ticks
(H-01, H-04, H-05, H-07, H-12, H-13, H-14, H-20, H-35) on the R9 state, plus the
drift chroma on the mid-tone (H-19) and the fold's dead ground (H-13)."""
import json, sys, io
from playwright.sync_api import sync_playwright
from PIL import Image
URL = "http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """() => {
  const q = s => document.querySelector(s);
  const box = s => { const e = q(s); if (!e) return null; const r = e.getBoundingClientRect();
    return {top: Math.round(r.top + scrollY), h: Math.round(r.height), left: Math.round(r.left), w: Math.round(r.width), bottom: Math.round(r.bottom + scrollY)}; };
  const sels = ['section.hero','.stagger','.panel-thesis','.calyx-fig','.panel-giant','.horai-fig','.price','#process','#principer','footer.close','.giant','.hero-sub','.card-cta','.hero-headline','.plate-card','.thesis-figure','.close a[href^="mailto"]','.calyx-wrap','.horai-wrap','.rv'];
  const o = {docH: document.documentElement.scrollHeight, vh: innerHeight, vw: innerWidth, vhRatio: +(document.documentElement.scrollHeight/innerHeight).toFixed(2)};
  for (const s of sels) o[s] = box(s);
  const g = q('.giant'); if (g) { const cs = getComputedStyle(g); o.giantFont = cs.fontSize; o.giantLS = cs.letterSpacing;
    const rng = document.createRange(); const tn = [...g.childNodes].filter(n => n.nodeType === 3 && /VARUM/.test(n.textContent))[0];
    if (tn) { const i = tn.textContent.indexOf('VARUM'); rng.setStart(tn, i); rng.setEnd(tn, tn.textContent.length); o.wordRects = rng.getClientRects().length; }
    o.giantLines = Math.round(g.getBoundingClientRect().height / parseFloat(cs.lineHeight)); }
  const m = q('.close a[href^="mailto"]'); if (m) { o.mailtoFont = getComputedStyle(m).fontSize; }
  o.bodyFont = getComputedStyle(document.body).fontSize;
  o.scrollW = document.documentElement.scrollWidth;
  o.rvClip = q('.horai-wrap') ? getComputedStyle(q('.horai-wrap')).clipPath : null;
  o.hasClipFrame = !!document.querySelector('.frame-wrap[style*=clip-path]');
  return o;
}"""
def ch(p): return max(p) - min(p)
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for w, h in ((1440, 900), (390, 844)):
        p = b.new_page(viewport={"width": w, "height": h}, reduced_motion="reduce")
        p.goto(URL, wait_until="load"); p.wait_for_timeout(1500)
        o = p.evaluate(JS)
        if w == 1440:
            # H-19: mid-tone drift on the wood at the thesis centred, and the fold
            img = Image.open(io.BytesIO(p.screenshot())).convert("RGB")
            o["fold_px"] = {f"{x},{y}": (img.getpixel((x, y)), ch(img.getpixel((x, y)))) for x, y in ((1300,700),(1420,850),(1200,450),(720,180))}
            yT = p.evaluate("() => { const t = document.querySelector('.panel-thesis').getBoundingClientRect(); return Math.round(t.top + scrollY + t.height/2 - innerHeight/2); }")
            p.evaluate("y => scrollTo(0,y)", yT); p.wait_for_timeout(1200)
            img = Image.open(io.BytesIO(p.screenshot())).convert("RGB")
            o["thesis_y"] = yT
            o["thesis_px"] = {f"{x},{y}": (img.getpixel((x, y)), ch(img.getpixel((x, y)))) for x, y in ((300,180),(720,180),(1000,180),(1420,850),(1300,100))}
            o["canvas"] = p.evaluate("getComputedStyle(document.querySelector('.ground')).getPropertyValue('--sc-canvas')")
            # H-20: bleed at --sc-ps 1 for the thesis figure
            p.evaluate("y => scrollTo(0,y)", yT + 600); p.wait_for_timeout(1500)
            o["thesisFigAtLater"] = p.evaluate("() => { const f = document.querySelector('.thesis-figure'); const g = document.querySelector('.giant'); const r = f.getBoundingClientRect(); const gr = g.getBoundingClientRect(); const w = document.querySelector('.panel-thesis').getBoundingClientRect(); return {figRight: Math.round(r.right), panelRight: Math.round(w.right), overhang: Math.round(r.right - w.right), giantLeft: Math.round(gr.left), transform: getComputedStyle(f).transform}; }")
        else:
            # H-13: dead ground under the sub-line at 390 fold
            o["deadFold"] = p.evaluate("() => { const s = document.querySelector('.hero-sub') || document.querySelector('.card-cta'); const r = s.getBoundingClientRect(); return {subBottom: Math.round(r.bottom), dead: Math.round(innerHeight - r.bottom), pct: +((innerHeight - r.bottom)/innerHeight*100).toFixed(1)}; }")
        out[str(w)] = o
        p.close()
    b.close()
print(json.dumps(out, indent=1))
json.dump(out, open(sys.argv[1], "w"), indent=1)
