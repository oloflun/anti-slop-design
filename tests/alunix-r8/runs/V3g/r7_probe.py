#!/usr/bin/env python3
"""R7 probe: one instrument for the H1-H15 + MEDIUM measurements, run
against the pre-R7 copy (index.before-r7.html) and the fixed page, so the
before and after numbers come from the same code.

    python tests/alunix-r8/browser_lock.py -- python r7_probe.py URL OUT_DIR [--shots]

Headless only; the browser is always closed (try/finally).
"""
import json, os, sys, math
from playwright.sync_api import sync_playwright

URL, OUT = sys.argv[1], sys.argv[2]
SHOTS = "--shots" in sys.argv
os.makedirs(OUT, exist_ok=True)

JUMP = "async (y)=>{window.__lenis.scrollTo(y,{immediate:true,force:true});for(let i=0;i<3;i++)await new Promise(r=>requestAnimationFrame(r));}"

CONTRAST_JS = """
window.__lum = c => { const m=String(c||'rgb(0,0,0)').match(/[\\d.]+/g).map(Number); const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)}; return 0.2126*f(m[0])+0.7152*f(m[1])+0.0722*f(m[2]); };
window.__cr = (a,b) => { const x=__lum(a), y=__lum(b); return +( (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05) ).toFixed(2); };
"""


def wait_frames_loaded(pg, timeout=15000):
    # bring the showcase into the mount window, then wait for the active case
    pg.evaluate(JUMP, pg.evaluate("document.getElementById('exempelcase').getBoundingClientRect().top+scrollY-200"))
    try:
        pg.wait_for_function("window.__CASES && window.__CASES.calyx.loaded", timeout=timeout)
    except Exception:
        pass
    pg.wait_for_timeout(600)


def st_of(pg, sel):
    return pg.evaluate("""(sel)=>{const s=ScrollTrigger.getAll().find(t=>t.pin&&t.pin.matches(sel));return s?{start:s.start,end:s.end}:null}""", sel)


def desktop(pg, res, tag):
    vw, vh = pg.viewport_size["width"], pg.viewport_size["height"]
    r = {}
    pg.evaluate(CONTRAST_JS)
    r["title"] = pg.title()
    r["will_change_at_rest"] = pg.evaluate("Array.from(document.querySelectorAll('*')).filter(e=>getComputedStyle(e).willChange!=='auto').length")
    r["fetchpriority_high"] = pg.evaluate("Array.from(document.querySelectorAll('img[fetchpriority=high]')).map(i=>i.getAttribute('src').split('/').pop())")
    r["iframe_src_at_load"] = pg.evaluate("Array.from(document.querySelectorAll('iframe')).map(f=>[f.id,f.getAttribute('src')])")
    # H2 hero: band under the stage during the pin
    st = st_of(pg, '.hero-stage')
    if st:
        pg.evaluate(JUMP, (st["start"] + st["end"]) / 2)
        r["hero_mid_pin"] = pg.evaluate(f"(()=>{{const b=document.querySelector('.hero-stage').getBoundingClientRect();return {{top:Math.round(b.top),bottom:Math.round(b.bottom),band_px:Math.max(0,{vh}-Math.round(b.bottom))}}}})()")
        if SHOTS: pg.screenshot(path=f"{OUT}/{tag}-hero-pin.png")
        pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * 0.9)
        if SHOTS: pg.screenshot(path=f"{OUT}/{tag}-hero-pin-90.png")
    # H2 tes: headline under the topline during the pin
    st = st_of(pg, '.tes-top')
    if st:
        out = []
        for f in (0.1, 0.5, 0.95):
            pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * f)
            pg.wait_for_timeout(900 if f == 0.1 else 50)
            out.append(pg.evaluate("(()=>{const h=document.querySelector('.tes-top h2').getBoundingClientRect();const c=Array.from(document.querySelectorAll('.tes-top h2 .char, .tes-top h2 div div div')).map(e=>e.getBoundingClientRect().top);return {h2_top:Math.round(h.top),glyph_box_top:Math.round(c.length?Math.min(...c):h.top),under_topline_px:Math.max(0,48-Math.round(h.top))}})()"))
            if SHOTS and f == 0.5: pg.screenshot(path=f"{OUT}/{tag}-tes-pin.png")
        r["tes_pin"] = out
    # H5 / MED: links
    r["boka_links"] = pg.evaluate("Array.from(document.querySelectorAll('a')).filter(a=>/Boka ett m/.test(a.textContent)).map(a=>({href:a.getAttribute('href'),tabindex:a.getAttribute('tabindex'),h:Math.round(a.getBoundingClientRect().height)}))")
    # showcase
    wait_frames_loaded(pg)
    st = st_of(pg, '.showcase-stage')
    r["showcase_pinned"] = bool(st)
    if st:
        # H1 visible width fraction of the site
        pg.evaluate(JUMP, st["start"] + 10)
        pg.wait_for_timeout(300)
        r["h1_frame"] = pg.evaluate("""(()=>{const w=document.getElementById('showcaseFrameWrap').getBoundingClientRect();
          return Array.from(document.querySelectorAll('#showcaseFrameWrap iframe')).map(f=>{const m=new DOMMatrix(getComputedStyle(f).transform);const s=m.a||1;
            let sw=null;try{sw=f.contentDocument.documentElement.scrollWidth}catch(e){}
            return {id:f.id,css_w:f.offsetWidth,css_h:f.offsetHeight,scale:+s.toFixed(4),site_w:sw,wrap_w:Math.round(w.width),wrap_h:Math.round(w.height),
              visible_width_frac:+Math.min(1,w.width/((sw||f.offsetWidth)*s)).toFixed(3),visible_height_frac:+Math.min(1,w.height/(f.offsetHeight*s)).toFixed(3)}})})()""")
        # H4 contrast in the case head (text vs painted ground)
        r["h4_head_contrast"] = pg.evaluate("""(()=>{const out={};document.querySelectorAll('.showcase-head').forEach(h=>{if(getComputedStyle(h.closest('.showcase-panel')).display==='none'&&!h.offsetParent)return;
            const fill=h.firstElementChild&&h.firstElementChild.getAttribute('aria-hidden')==='true'?h.firstElementChild:h;const bg=getComputedStyle(fill).backgroundColor;
            const t=h.querySelector('h2'),c=h.querySelector('p.caption');out[t.id]={bg,name:__cr(getComputedStyle(t).color,bg),caption:c?__cr(getComputedStyle(c).color,bg):null,on_black:__cr(getComputedStyle(t).color,'rgb(0,0,0)')};});return out})()""")
        # H6 steps in the accessibility tree
        pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * 0.5)
        r["h6_steps_exposed"] = pg.evaluate("""(()=>Array.from(document.querySelectorAll('.showcase-panel')).map(p=>{const rows=Array.from(p.querySelectorAll('.showcase-row'));
            return {panel:p.id,rows:rows.length,exposed:rows.filter(x=>x.getAttribute('aria-hidden')!=='true'&&getComputedStyle(x).visibility!=='hidden').length}}))()""")
        r["will_change_mid_showcase"] = pg.evaluate("Array.from(document.querySelectorAll('*')).filter(e=>getComputedStyle(e).willChange!=='auto').length")
        # step screenshots, both cases, three steps
        if SHOTS:
            for case, steps in (("calyx", (0, 2, 4)), ("horai", (0, 2, 5))):
                if case == "horai":
                    pg.evaluate("document.querySelector('button.case-choice[data-case=horai]').click()")
                    try: pg.wait_for_function("window.__CASES.horai.loaded", timeout=15000)
                    except Exception: pass
                    pg.wait_for_timeout(2500)
                n = 5 if case == "calyx" else 6
                for k in steps:
                    p = (k + 0.8) / n if k else 0.1 / n
                    pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * p)
                    pg.wait_for_timeout(700)
                    pg.screenshot(path=f"{OUT}/{tag}-showcase-{case}-{k+1}.png")
            pg.evaluate("document.querySelector('button.case-choice[data-case=calyx]').click()")
            pg.wait_for_timeout(2500)
    # H7 tab walk from the top: stops inside frames and whether that frame is visible
    pg.evaluate(JUMP, 0)
    pg.wait_for_timeout(300)
    stops = []
    pg.evaluate("document.activeElement&&document.activeElement.blur()")
    for i in range(30):
        pg.keyboard.press("Tab")
        info = pg.evaluate("""(()=>{const a=document.activeElement;if(!a)return null;const o={tag:a.tagName,id:a.id,text:(a.textContent||a.getAttribute('aria-label')||'').trim().slice(0,30)};
          if(a.tagName==='IFRAME'){o.frame_opacity=getComputedStyle(a).opacity;try{const ia=a.contentDocument.activeElement;o.inner=ia?ia.tagName+':'+(ia.textContent||'').trim().slice(0,20):null;o.inner_scrollX=a.contentWindow.scrollX}catch(e){}}return o})()""")
        stops.append(info)
        if info and info["tag"] == "BODY": break
    r["h7_tab_stops"] = stops
    r["h7_frame_stops"] = sum(1 for s in stops if s and s["tag"] == "IFRAME")
    r["h7_hidden_frame_stops"] = sum(1 for s in stops if s and s["tag"] == "IFRAME" and float(s.get("frame_opacity", 1)) < 0.05)
    # MED: accessible names of the case buttons
    try:
        cdp = pg.context.new_cdp_session(pg)
        tree = cdp.send("Accessibility.getFullAXTree")["nodes"]
        r["button_names"] = [n.get("name", {}).get("value") for n in tree if n.get("role", {}).get("value") == "button" and not n.get("ignored")]
        r["tes_lines_in_tree"] = [n.get("name", {}).get("value") for n in tree if n.get("role", {}).get("value") in ("StaticText",) and "Skärmen möter" in (n.get("name", {}).get("value") or "")]
    except Exception as e:
        r["button_names"] = str(e)
    # H9 kontakt card: focus after the flip, link heights, ring clipping
    pg.evaluate(JUMP, pg.evaluate("document.getElementById('kontakt').getBoundingClientRect().top+scrollY-" + str(vh)))
    pg.wait_for_timeout(300)
    r["h9"] = pg.evaluate("""async ()=>{const f=document.getElementById('kontaktCardFront');if(window.__kontaktCardFlip)__kontaktCardFlip(false,{immediate:true});
        f.focus();f.click();await new Promise(r=>setTimeout(r,900));const a=document.activeElement;
        const face=document.getElementById('kontaktCardBack').getBoundingClientRect();
        const links=Array.from(document.querySelectorAll('#kontaktCardBack a')).map(l=>{const b=l.getBoundingClientRect();const cs=getComputedStyle(l);
          return {text:l.textContent.trim(),href:l.getAttribute('href'),h:Math.round(b.height),w:Math.round(b.width)}});
        return {active_after_flip:a.tagName+':'+(a.textContent||a.getAttribute('aria-label')||'').trim().slice(0,30),back_links:links,face_back_hit:!!document.getElementById('kontaktCardBackHit')}}""")
    if SHOTS:
        pg.evaluate(JUMP, pg.evaluate("document.getElementById('kontakt').getBoundingClientRect().top+scrollY-48"))
        pg.wait_for_timeout(1200)
        pg.screenshot(path=f"{OUT}/{tag}-kontakt.png")
        pg.keyboard.press("Tab") if False else None
    res[tag] = r


def mobile(pg, res, tag):
    vw, vh = pg.viewport_size["width"], pg.viewport_size["height"]
    r = {}
    r["footer_link"] = pg.evaluate("Array.from(document.querySelectorAll('.footer-strip a')).map(a=>({text:a.textContent.trim(),lines:a.getClientRects().length,h:Math.round(a.getBoundingClientRect().height)}))")
    r["hero_boka_href"] = pg.evaluate("(document.querySelector('.card-cta')||{}).getAttribute && document.querySelector('.card-cta').getAttribute('href')")
    wait_frames_loaded(pg)
    r["frame"] = pg.evaluate("""(()=>{const w=document.getElementById('showcaseFrameWrap').getBoundingClientRect();
        return Array.from(document.querySelectorAll('#showcaseFrameWrap iframe')).map(f=>{const m=new DOMMatrix(getComputedStyle(f).transform);const s=m.a||1;let sw=null;try{sw=f.contentDocument.documentElement.scrollWidth}catch(e){}
        return {id:f.id,css_w:f.offsetWidth,css_h:f.offsetHeight,scale:+s.toFixed(4),site_w:sw,wrap_w:Math.round(w.width),wrap_h:Math.round(w.height),visible_width_frac:+Math.min(1,w.width/((sw||f.offsetWidth)*s)).toFixed(3)}})})()""")
    # H14: tap Hoerai, then walk the rows and check the site follows + h3 visibility
    pg.evaluate("document.querySelector('button.case-choice[data-case=horai]').scrollIntoView({block:'center'})")
    pg.wait_for_timeout(300)
    pg.evaluate("document.querySelector('button.case-choice[data-case=horai]').click()")
    pg.wait_for_timeout(150)
    r["frame_blank_after_tap"] = pg.evaluate("""(()=>{const H=window.__CASES.horai;const p=H.poster;return {loaded:H.loaded,poster_shown:!!p&&getComputedStyle(p).display!=='none',iframe_opacity:getComputedStyle(H.iframe).opacity}})()""")
    try: pg.wait_for_function("window.__CASES.horai.loaded", timeout=15000)
    except Exception: pass
    pg.wait_for_timeout(2500)
    r["h14"] = pg.evaluate("""async ()=>{const H=window.__CASES.horai;const rows=Array.from(document.querySelectorAll('#showcase-horai .showcase-row'));
        const cell=document.querySelector('.showcase-embed-cell');const fb=48+cell.offsetHeight;const vh=innerHeight;
        const J=async y=>{window.__lenis.scrollTo(y,{immediate:true,force:true});for(let i=0;i<2;i++)await new Promise(r=>requestAnimationFrame(r));};
        const out=[];
        for(let i=0;i<rows.length;i++){const top=rows[i].getBoundingClientRect().top+scrollY;await J(top-(fb+24));await new Promise(r=>setTimeout(r,900));
          out.push({row:i,pending:H.pendingRow,site_y:Math.round(H.w?H.w.scrollY:-1),want:H.y?H.y[i]:null});}
        // h3 visibility while each row is the active one
        const first=rows[0].getBoundingClientRect().top+scrollY-vh, last=rows[rows.length-1].getBoundingClientRect().bottom+scrollY;
        const act={},vis={};
        for(let y=first;y<last;y+=20){await J(y);const k=H.pendingRow;act[k]=(act[k]||0)+20;const h=rows[k].querySelector('h3').getBoundingClientRect();
          if(h.top>=fb-1&&h.bottom<=vh+1)vis[k]=(vis[k]||0)+20;}
        const per=rows.map((_,k)=>({row:k,active_px:act[k]||0,h3_visible_px:vis[k]||0}));
        return {frame_bottom:fb,rows:out,visibility:per}}""")
    if SHOTS:
        rows = pg.evaluate("Array.from(document.querySelectorAll('#showcase-horai .showcase-row')).map(r=>r.getBoundingClientRect().top+scrollY)")
        fb = pg.evaluate("48+document.querySelector('.showcase-embed-cell').offsetHeight")
        for k in (0, 2, 5):
            pg.evaluate(JUMP, rows[k] - (fb + 24)); pg.wait_for_timeout(1200)
            pg.screenshot(path=f"{OUT}/{tag}-showcase-horai-{k+1}.png")
        pg.evaluate("document.querySelector('button.case-choice[data-case=calyx]').click()"); pg.wait_for_timeout(2500)
        rows = pg.evaluate("Array.from(document.querySelectorAll('#showcase-calyx .showcase-row')).map(r=>r.getBoundingClientRect().top+scrollY)")
        for k in (0, 2, 4):
            pg.evaluate(JUMP, rows[k] - (fb + 24)); pg.wait_for_timeout(1200)
            pg.screenshot(path=f"{OUT}/{tag}-showcase-calyx-{k+1}.png")
        pg.evaluate(JUMP, 0); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/{tag}-hero.png")
        pg.evaluate(JUMP, pg.evaluate("document.getElementById('tes').getBoundingClientRect().top+scrollY-48")); pg.wait_for_timeout(1200); pg.screenshot(path=f"{OUT}/{tag}-tes.png")
        pg.evaluate(JUMP, pg.evaluate("document.getElementById('kontakt').getBoundingClientRect().top+scrollY")); pg.wait_for_timeout(1500)
        pg.evaluate(JUMP, pg.evaluate("document.getElementById('kontakt').getBoundingClientRect().top+scrollY+document.getElementById('kontakt').offsetHeight*0.35")); pg.wait_for_timeout(1200)
        pg.screenshot(path=f"{OUT}/{tag}-kontakt.png")
        pg.evaluate(JUMP, 1e6); pg.wait_for_timeout(800); pg.screenshot(path=f"{OUT}/{tag}-footer.png")
    r["kontakt_links"] = pg.evaluate("Array.from(document.querySelectorAll('#kontaktCardBack a')).map(l=>({text:l.textContent.trim(),h:Math.round(l.getBoundingClientRect().height)}))")
    res[tag] = r


def short(pg, res, tag):
    """H10: 768x432 (200 % zoom of 1536x864): is any step text clipped?"""
    wait_frames_loaded(pg)
    st = st_of(pg, '.showcase-stage')
    r = {"pinned": bool(st)}
    if st:
        worst = []
        for f in (0.1, 0.5, 0.9):
            pg.evaluate(JUMP, st["start"] + (st["end"] - st["start"]) * f)
            pg.wait_for_timeout(400)
            worst.append(pg.evaluate("""(()=>{const side=document.querySelector('.showcase-side').getBoundingClientRect();
               const vis=Array.from(document.querySelectorAll('.showcase-panel:not([style*="none"]) .showcase-row-text')).filter(e=>+getComputedStyle(e).opacity>0.5);
               const sd=document.querySelector('.showcase-side');return {side_overflow:sd.scrollHeight-sd.clientHeight,text:vis.map(e=>Math.round(e.getBoundingClientRect().bottom-Math.min(side.bottom,innerHeight)))}})()"""))
        r["text_bottom_minus_panel_bottom"] = worst
    else:
        r["rows_clipped"] = pg.evaluate("""(()=>Array.from(document.querySelectorAll('#showcase-calyx .showcase-row-text')).map(e=>{const b=e.getBoundingClientRect(),p=e.closest('.showcase-row').getBoundingClientRect();return Math.round(b.bottom-p.bottom)}))()""")
    if SHOTS:
        pg.evaluate(JUMP, pg.evaluate("document.getElementById('showcase').getBoundingClientRect().top+scrollY+300")); pg.wait_for_timeout(1200)
        pg.screenshot(path=f"{OUT}/{tag}-showcase.png")
    res[tag] = r


res = {"url": URL}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    try:
        for tag, vp, fn, touch in (("d1440", (1440, 900), desktop, False), ("m390", (390, 844), mobile, True), ("s768x432", (768, 432), short, False)):
            ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]}, has_touch=touch)
            pg = ctx.new_page()
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2500)
            try:
                fn(pg, res, tag)
            except Exception as e:
                res[tag + "_error"] = repr(e)
            res[tag + "_pageerrors"] = errs
            ctx.close()
    finally:
        b.close()
with open(os.path.join(OUT, "r7_probe.json"), "w", encoding="utf-8") as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
print(json.dumps(res, ensure_ascii=False)[:6000])
