"""preview390b.py: where do the 263 px go at 390 in ?preview=process-01? Compare the
boxes of every act in normal mode vs preview mode, plus the engine's cached tops, 3 s
after load; three loads of the preview to catch both outcomes."""
import json, sys
from playwright.sync_api import sync_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
JS = """() => {
  const q = s => document.querySelector(s);
  const box = s => { const e = q(s); if (!e) return null; const r = e.getBoundingClientRect(); return [Math.round(r.top + scrollY), Math.round(r.height)]; };
  const o = {scrollY: scrollY, docH: document.documentElement.scrollHeight, vh: innerHeight};
  for (const s of ['section.hero', '.hero-stage, .hero > *', '.stagger', '.panel-thesis', '.calyx-fig', '.calyx-wrap', '.panel-giant', '.horai-fig', '.horai-wrap', '.price', '#process', '#principer', 'footer.close']) o[s] = box(s);
  o.calyxAsleep = q('.calyx-wrap').classList.contains('is-asleep'); o.horaiAsleep = q('.horai-wrap').classList.contains('is-asleep');
  o.calyxSrc = !!q('.calyx-wrap iframe').src; o.horaiSrc = !!q('.horai-wrap iframe').src;
  const inst = (window.ScrollCraft && window.ScrollCraft.instances && window.ScrollCraft.instances[0]) || null;
  try { o.engine = inst.acts.map(a => [a.el.id || a.el.className, Math.round(a.top), Math.round(a.h || a.height || 0)]); } catch(e) { o.engine = String(e); }
  const p = q('#process'); const cs = getComputedStyle(p);
  o.ps = cs.getPropertyValue('--sc-ps'); o.e1 = cs.getPropertyValue('--e1'); o.rawP = p.style.getPropertyValue('--sc-p');
  return o;
}"""
out = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(3000)
    out["normal"] = pg.evaluate(JS); pg.close()
    pg = b.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(1500); pg.evaluate("scrollTo(0, 6461)"); pg.wait_for_timeout(3000)
    out["normal_scrolled_6461"] = pg.evaluate(JS); pg.close()
    for rep in range(3):
        pg = b.new_page(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
        pg.goto(URL + "?preview=process-01", wait_until="load"); pg.wait_for_timeout(3000)
        out[f"preview01_{rep}"] = pg.evaluate(JS); pg.close()
    b.close()
for k, v in out.items():
    print(k, json.dumps({kk: vv for kk, vv in v.items() if kk in ('scrollY', 'docH', 'section.hero', '.stagger', '.calyx-wrap', '.horai-wrap', '.price', '#process', 'calyxAsleep', 'horaiAsleep', 'calyxSrc', 'horaiSrc', 'ps', 'e1')}))
    print("   engine:", v.get("engine"))
json.dump(out, open(sys.argv[1], "w"), indent=1)
