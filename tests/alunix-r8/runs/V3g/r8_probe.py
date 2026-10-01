#!/usr/bin/env python3
"""R8 probe: the showcase without boxes, measured in every step of both cases.

    python tests/alunix-r8/browser_lock.py -- python r8_probe.py URL OUT_DIR [--shots] [--fault]

Per desktop viewport (1440x900, 1280x800, 1920x1080), per case, per step, at the
step's dwell point (75 % into its segment):
  clip      the active text block's scrollHeight > clientHeight, its bottom below
            the column's bottom, or below the viewport
  overlap   area of intersection between the text block and the visible loupe
  loupe     size, how far it breaks over the seam (px left of the column), gap
            to the text above it
  type      h3 / lede / second paragraph: size, line-height, colour, contrast
  surface   gap and background of every child of .showcase-rows (one surface)
Mobile 390x844: both paragraphs present, no row clipped, no boxes.
--fault injects `.showcase-row .showcase-lede{font-size:44px}` (the clip check
must fire), --fault-overlap moves the loupe 120 px up into the text (the overlap
check must fire): chain-discipline M3.
Headless only; the browser is always closed (try/finally).
"""
import json, os, sys
from playwright.sync_api import sync_playwright

URL, OUT = sys.argv[1], sys.argv[2]
SHOTS = "--shots" in sys.argv
FAULT = "--fault" in sys.argv
FAULT2 = "--fault-overlap" in sys.argv
os.makedirs(OUT, exist_ok=True)
FAULT_CSS = ".showcase-row .showcase-lede{font-size:44px !important}"
FAULT2_CSS = ".showcase-detail{overflow:visible !important}.showcase-figure{top:-120px !important;left:-48px !important}"  # R8b: text overlap AND iframe intersection must fire

JUMP = "async (y)=>{window.__lenis.scrollTo(y,{immediate:true,force:true});for(let i=0;i<3;i++)await new Promise(r=>requestAnimationFrame(r));}"
HELPERS = """
window.__lum = c => { const m=String(c||'rgb(0,0,0)').match(/[\\d.]+/g).map(Number); const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)}; return 0.2126*f(m[0])+0.7152*f(m[1])+0.0722*f(m[2]); };
window.__cr = (a,b) => { const x=__lum(a), y=__lum(b); return +((Math.max(x,y)+0.05)/(Math.min(x,y)+0.05)).toFixed(2); };
"""
MEASURE = """(key)=>{
  const P=document.getElementById('showcase-'+key), side=document.querySelector('.showcase-side').getBoundingClientRect();
  const embed=document.querySelector('.showcase-embed-cell').getBoundingClientRect();
  const rows=P.querySelector('.showcase-rows'), bg=getComputedStyle(rows).backgroundColor;
  const texts=[...P.querySelectorAll('.showcase-row-text')];
  const act=texts.findIndex(t=>+getComputedStyle(t.querySelector('h3')).opacity>0.9);
  const t=texts[act]; if(!t) return {act:-1};
  const tr=t.getBoundingClientRect();
  const figs=[...P.querySelectorAll('.showcase-figure')];
  const fig=figs.find(f=>+getComputedStyle(f).opacity>0.5);
  // R8b: the loupe is clipped by .showcase-detail (overflow:hidden); its visible rect is the intersection
  const det=P.querySelector('.showcase-detail'), dr=det.getBoundingClientRect();
  const shown=fig&&getComputedStyle(fig).display!=='none';
  const raw=shown?fig.getBoundingClientRect():null;
  const clips=/hidden|clip/.test(getComputedStyle(det).overflowX+getComputedStyle(det).overflowY);
  const fr=raw&&!clips?raw:raw?{left:Math.max(raw.left,dr.left),right:Math.min(raw.right,dr.right),top:Math.max(raw.top,dr.top),bottom:Math.min(raw.bottom,dr.bottom),get width(){return this.right-this.left},get height(){return this.bottom-this.top}}:null;
  const wrap=document.getElementById('showcaseFrameWrap').getBoundingClientRect();
  const ix=(a,b)=>Math.max(0,Math.min(a.right,b.right)-Math.max(a.left,b.left))*Math.max(0,Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top));
  const inter=fr?Math.max(0,Math.min(tr.right,fr.right)-Math.max(tr.left,fr.left))*Math.max(0,Math.min(tr.bottom,fr.bottom)-Math.max(tr.top,fr.top)):0;
  // also against every text block (the tallest step governs the layout)
  const interAll=fr?Math.max(...texts.map(x=>{const r=x.getBoundingClientRect();return Math.max(0,Math.min(r.right,fr.right)-Math.max(r.left,fr.left))*Math.max(0,Math.min(r.bottom,fr.bottom)-Math.max(r.top,fr.top))})):0;
  const st=el=>{const c=getComputedStyle(el);return {px:+parseFloat(c.fontSize).toFixed(2),lh:+(parseFloat(c.lineHeight)/parseFloat(c.fontSize)).toFixed(2),color:c.color,cr:__cr(c.color,bg),w:Math.round(el.getBoundingClientRect().width),lines:Math.round(el.getBoundingClientRect().height/parseFloat(c.lineHeight))}};
  const h3=t.querySelector('h3'), lede=t.querySelector('.showcase-lede'), more=t.querySelector('.showcase-more');
  const ch=(el)=>{const s=document.createElement('span');s.textContent='0';s.style.cssText='position:absolute;visibility:hidden;font:inherit';el.appendChild(s);const w=s.getBoundingClientRect().width;s.remove();return w;};
  const kids=[...rows.children].map(c=>({cls:c.className,bg:getComputedStyle(c).backgroundColor,border:getComputedStyle(c).borderTopWidth}));
  const steps=P.querySelector('.showcase-steps');
  return {act, counter:(P.querySelector('.showcase-counter')||{}).textContent,
    fill:(P.querySelector('.showcase-track-fill')||{style:{}}).style.transform,
    rows_gap:getComputedStyle(rows).rowGap, rows_bg:bg, kids,
    text:{top:Math.round(tr.top),bottom:Math.round(tr.bottom),sh:t.scrollHeight,chh:t.clientHeight,
      row_sh:t.parentElement.scrollHeight,row_ch:t.parentElement.clientHeight,
      steps_sh:steps.scrollHeight,steps_ch:steps.clientHeight},
    column:{top:Math.round(side.top),bottom:Math.round(side.bottom),left:Math.round(side.left),vh:innerHeight},
    clip:(t.scrollHeight>t.clientHeight+1)||(tr.bottom>side.bottom+0.5)||(tr.bottom>innerHeight+0.5),
    // steps_sh may exceed steps_ch by the y:12 of the invisible (opacity 0) steps; reported, not a clip
    band_h:Math.round(dr.height), loupe_hidden:!!fig&&!shown,
    loupe:fr?{w:Math.round(fr.width),h:Math.round(fr.height),left:Math.round(fr.left),bottom:Math.round(fr.bottom),
      breakout_px:Math.round(side.left-fr.left),gap_to_text:Math.round(fr.top-tr.bottom),
      gap_to_tallest:Math.round(fr.top-Math.max(...texts.map(x=>x.getBoundingClientRect().bottom))),
      over_embed_px:Math.round(Math.max(0,embed.right-fr.left)),
      iframe_intersection_px2:Math.round(ix(fr,wrap)), detail_iframe_intersection_px2:Math.round(ix(dr,wrap)),
      flush:{left:Math.round(fr.left-side.left),right:Math.round(side.right-fr.right),bottom:Math.round(side.bottom-fr.bottom)},
      fx_fy:[getComputedStyle(fig).getPropertyValue('--fx').trim(),getComputedStyle(fig).getPropertyValue('--fy').trim()],
      border:getComputedStyle(fig).borderTopWidth,shadow:getComputedStyle(fig).boxShadow,
      nat:(()=>{const i=fig.querySelector('.color-layer');return i?[i.naturalWidth,i.naturalHeight]:null})()}:null,
    overlap_px2:Math.round(inter), overlap_any_step_px2:Math.round(interAll),
    type:{h3:st(h3),lede:lede?st(lede):null,more:more?st(more):null,
      lede_ch:lede?+(lede.getBoundingClientRect().width/ch(lede)).toFixed(1):null,
      more_ch:more?+(more.getBoundingClientRect().width/ch(more)).toFixed(1):null,
      gap_h3_lede:lede?Math.round(lede.getBoundingClientRect().top-h3.getBoundingClientRect().bottom):null,
      gap_lede_more:more?Math.round(more.getBoundingClientRect().top-lede.getBoundingClientRect().bottom):null}};
}"""


def st_of(pg):
    return pg.evaluate("(()=>{const s=ScrollTrigger.getAll().find(t=>t.pin&&t.pin.matches('.showcase-stage'));return s?{start:s.start,end:s.end}:null})()")


def goto(pg):
    errs = []
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until="load")
    if FAULT:
        pg.add_style_tag(content=FAULT_CSS)
    if FAULT2:
        pg.add_style_tag(content=FAULT2_CSS)
    pg.wait_for_timeout(1500)
    pg.evaluate(HELPERS)
    pg.evaluate(JUMP, pg.evaluate("document.getElementById('exempelcase').getBoundingClientRect().top+scrollY-200"))
    try:
        pg.wait_for_function("window.__CASES && window.__CASES.calyx.loaded", timeout=20000)
    except Exception:
        pass
    pg.wait_for_timeout(700)
    return errs


def desktop(b, w, h, res):
    pg = b.new_page(viewport={"width": w, "height": h})
    errs = goto(pg)
    tag = f"{w}x{h}"
    out = {}
    for key, n in (("calyx", 5), ("horai", 6)):
        if key == "horai":
            pg.click('.case-choice[data-case="horai"]')
            pg.wait_for_timeout(2600)
            try:
                pg.wait_for_function("window.__CASES.horai.loaded", timeout=20000)
            except Exception:
                pass
            pg.wait_for_timeout(900)
            pg.evaluate(HELPERS)
        st = st_of(pg)
        steps = []
        for k in range(n):
            pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * ((k + 0.75) / n))
            pg.wait_for_timeout(450)
            m = pg.evaluate(MEASURE, key)
            steps.append(m)
            if SHOTS and k in (0, 2):
                pg.screenshot(path=f"{OUT}/{key}-{tag}-steg{k+1}.png")
        if SHOTS and w == 1440 and key == "calyx":
            # crossfade midpoint into step 3: lede ~half in, second paragraph lagging
            for frac, name in ((0.15 + 0.15 * 0.45, "mitt"), (0.15 + 0.15 * 0.25, "tidig")):
                pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * ((2 + frac) / n))
                pg.wait_for_timeout(450)
                ops = pg.evaluate("""()=>{const t=[...document.querySelectorAll('#showcase-calyx .showcase-row-text')][2];
                    const o=e=>+(+getComputedStyle(e).opacity).toFixed(2);return {h3:o(t.querySelector('h3')),lede:o(t.querySelector('.showcase-lede')),more:o(t.querySelector('.showcase-more'))}}""")
                out.setdefault("crossfade_into_step3", {})[name] = ops
                pg.screenshot(path=f"{OUT}/calyx-{tag}-overtoning-{name}.png")
        out[key] = steps
    # desktop -> mobile resize: matchMedia must revert the step parts to visible
    pg.set_viewport_size({"width": 390, "height": 844})
    pg.wait_for_timeout(900)
    out["after_resize_to_390_min_part_opacity"] = pg.evaluate("Math.min(...[...document.querySelectorAll('#showcase-horai .showcase-row-text > *, #showcase-calyx .showcase-row-text > *')].map(e=>+getComputedStyle(e).opacity))")
    out["overflow_px"] = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
    out["console_errors"] = errs
    res[tag] = out
    pg.close()


def mobile(b, res):
    pg = b.new_page(viewport={"width": 390, "height": 844})
    errs = goto(pg)
    pg.evaluate(HELPERS)
    y0 = pg.evaluate("document.querySelector('#showcase-calyx .showcase-rows').getBoundingClientRect().top+scrollY")
    pg.evaluate(JUMP, y0 - 520)
    pg.wait_for_timeout(900)
    r = pg.evaluate("""()=>{
      const rows=[...document.querySelectorAll('#showcase-calyx .showcase-row')];
      const box=document.querySelector('#showcase-calyx .showcase-rows');
      return {gap:getComputedStyle(box).rowGap,
        rows:rows.map(r=>{const t=r.querySelector('.showcase-row-text');const L=r.querySelector('.showcase-lede'),M=r.querySelector('.showcase-more');
          const bg=getComputedStyle(r).backgroundColor;
          return {bg, clip:r.scrollHeight>r.clientHeight+1||t.scrollHeight>t.clientHeight+1, lede_px:L&&parseFloat(getComputedStyle(L).fontSize), more_px:M&&parseFloat(getComputedStyle(M).fontSize),
            h3_px:parseFloat(getComputedStyle(r.querySelector('h3')).fontSize), lede_cr:L&&__cr(getComputedStyle(L).color,bg), more_cr:M&&__cr(getComputedStyle(M).color,bg)}})}}""")
    if SHOTS:
        pg.screenshot(path=f"{OUT}/calyx-390x844-rader.png")
    pg.evaluate(JUMP, y0 + 600)
    pg.wait_for_timeout(900)
    if SHOTS:
        pg.screenshot(path=f"{OUT}/calyx-390x844-rader-2.png")
    pg.click('.case-choice[data-case="horai"]')
    pg.wait_for_timeout(3000)
    y1 = pg.evaluate("document.querySelector('#showcase-horai .showcase-rows').getBoundingClientRect().top+scrollY")
    pg.evaluate(JUMP, y1 - 520)
    pg.wait_for_timeout(900)
    r["horai"] = pg.evaluate("""()=>[...document.querySelectorAll('#showcase-horai .showcase-row')].map(r=>{const bg=getComputedStyle(r).backgroundColor;const L=r.querySelector('.showcase-lede'),M=r.querySelector('.showcase-more');
       return {bg,clip:r.scrollHeight>r.clientHeight+1,lede_cr:__cr(getComputedStyle(L).color,bg),more_cr:__cr(getComputedStyle(M).color,bg)}})""")
    if SHOTS:
        pg.screenshot(path=f"{OUT}/horai-390x844-rader.png")
    r["overflow_px"] = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
    r["console_errors"] = errs
    res["390x844"] = r
    pg.close()


def summary(res):
    rows = []
    for tag, d in res.items():
        if tag == "390x844":
            continue
        for key in ("calyx", "horai"):
            for i, s in enumerate(d.get(key, [])):
                if s.get("act", -1) < 0:
                    rows.append(f"{tag} {key} {i+1}: NO ACTIVE STEP"); continue
                lp = s["loupe"] or {}
                rows.append(f"{tag} {key} steg{i+1}: act={s['act']+1} {s['counter']} clip={s['clip']} overlap={s['overlap_px2']}/{s['overlap_any_step_px2']} "
                            f"band_h={s.get('band_h')} hidden={s.get('loupe_hidden')} iframe_x={lp.get('iframe_intersection_px2')} flush={lp.get('flush')} "
                            f"text {s['text']['top']}-{s['text']['bottom']} col_bottom={s['column']['bottom']} "
                            f"loupe {lp.get('w')}x{lp.get('h')} breakout={lp.get('breakout_px')} gap={lp.get('gap_to_tallest')} "
                            f"h3={s['type']['h3']['px']} lede={s['type']['lede']['px']}/{s['type']['lede']['lh']} ({s['type']['lede_ch']}ch) "
                            f"more={s['type']['more']['px']}/{s['type']['more']['lh']} cr={s['type']['more']['cr']} ({s['type']['more_ch']}ch)")
    return rows


res = {}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    try:
        for (w, h) in ((1440, 900), (1280, 800), (1920, 1080)):
            desktop(b, w, h, res)
        mobile(b, res)
    finally:
        b.close()
name = "r8-probe-fault.json" if FAULT else ("r8-probe-fault-overlap.json" if FAULT2 else "r8-probe.json")
with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
for line in summary(res):
    print(line)
print("mobile:", json.dumps(res.get("390x844"), ensure_ascii=False)[:1500])
for tag in res:
    if tag != "390x844":
        print(tag, "resize->390 min opacity", res[tag].get("after_resize_to_390_min_part_opacity"), "overflow", res[tag].get("overflow_px"), "errors", res[tag].get("console_errors"), "xfade", res[tag].get("crossfade_into_step3"))
