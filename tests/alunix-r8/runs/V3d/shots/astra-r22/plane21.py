"""astra-r21, R19-R21-specifikt: 20px-hjul BADA riktningarna genom tes -> ritning.
Per bildruta:
  - .tes-plane: position (far aldrig vara fixed), synlig rektangel efter clip-path, kontur-pa?
  - streck over text: elementsFromPoint pa planets fyra konturkanter OCH pa varje .seam i-linje;
    traff = textbarande nod (egen textnod, >=1 tecken) i stacken UTAN opakt element emellan
    den och konturen.
  - tva ark samtidigt: bade .tes-plane (kontur synlig, p-edge>0) och .process-sheet synliga.
Argument: bredd hojd.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

PROBE = r"""() => {
  function parseInset(cp, w, h){
    const m=/^inset\(([^)]+)\)/.exec(cp); if(!m) return null;
    const raw=m[1].trim().split(/\s+/);
    const val=(t,b)=>t.endsWith('%')?parseFloat(t)/100*b:parseFloat(t);
    let t,r,bo,l;
    if(raw.length===1){t=r=bo=l=val(raw[0],h);}
    else if(raw.length===2){t=bo=val(raw[0],h);r=l=val(raw[1],w);}
    else if(raw.length===3){t=val(raw[0],h);r=l=val(raw[1],w);bo=val(raw[2],h);}
    else {t=val(raw[0],h);r=val(raw[1],w);bo=val(raw[2],h);l=val(raw[3],w);}
    return {top:t,right:r,bottom:bo,left:l};
  }
  function hasOwnText(el){
    if(!el || el.nodeType!==1) return false;
    for(const n of el.childNodes) if(n.nodeType===3 && n.data.trim().length>0) return true;
    return false;
  }
  function opaque(el){
    const cs=getComputedStyle(el);
    const bg=cs.backgroundColor||'';
    const m=/rgba?\(([^)]+)\)/.exec(bg);
    if(!m) return false;
    const p=m[1].split(',').map(s=>parseFloat(s));
    return (p.length<4 || p[3]>=0.98);
  }
  const vw=innerWidth, vh=innerHeight;
  const plane=document.querySelector('.tes-plane');
  const out={y:scrollY, hits:[], plane:null, twoSheets:false, sheet:null};
  if(!plane) return out;
  const pcs=getComputedStyle(plane);
  const pr=plane.getBoundingClientRect();
  const ins=parseInset(pcs.clipPath, pr.width, pr.height)||{top:0,right:0,bottom:0,left:0};
  const V={left:pr.left+ins.left, right:pr.right-ins.right, top:pr.top+ins.top, bottom:pr.bottom-ins.bottom};
  // --tx och --p-edge ar OREGISTRERADE custom properties: getPropertyValue ger
  // token-strommen ("clamp(0,calc(...),1)"), inte det berakndade talet. Rakna
  // dem ur --sc-ps, som motorn skriver som ett rent tal.
  const chap=document.querySelector('.process-chapter');
  const cl=(v)=>Math.max(0,Math.min(1,v));
  const ps=chap?parseFloat(getComputedStyle(chap).getPropertyValue('--sc-ps')):NaN;
  const tx=isNaN(ps)?NaN:cl((ps-0.07)/0.29);
  const edgeOn=isNaN(tx)?0:cl((tx-0.6)/0.3);
  out.plane={pos:pcs.position, tx:tx, edge:edgeOn,
             vis:[Math.round(V.left),Math.round(V.top),Math.round(V.right),Math.round(V.bottom)],
             onScreen:(V.bottom>0 && V.top<vh && V.right>0 && V.left<vw && V.right>V.left && V.bottom>V.top)};
  const sh=document.querySelector('.process-sheet');
  if(sh){
    const sr=sh.getBoundingClientRect();
    out.sheet=[Math.round(sr.left),Math.round(sr.top),Math.round(sr.right),Math.round(sr.bottom)];
    out.twoSheets = out.plane.onScreen && edgeOn>0.05 && sr.bottom>0 && sr.top<vh && sr.height>40;
  }
  // .tes-plane och .seam har pointer-events:none och syns DARFOR aldrig i
  // elementsFromPoint (forsta forsoket gav 0 aven pa en trasig kontroll -
  // matte ingenting). Geometriskt prov i stallet: planets synliga rektangel
  // och varje .seam-linjes synliga rektangel mot varje LEVANDE textelements
  // rektangel. Traff = overlapp som inte doljs av ett opakt forfaderelement
  // (.step-band har egen background; .process-title/.process-locked har inte -
  // exakt den skillnad R20 pekade ut).
  function ancestorOpaqueCover(el, rect){
    let n=el, d=0;
    while(n && n.nodeType===1 && d<8){
      d++;
      // en forfader som SJALV innehaller planet malar UNDER planet och kan
      // darfor aldrig dolja det (R20: .step-band doljer, #process gor inte).
      if(n.contains(plane)){ n=n.parentElement; continue; }
      const cs=getComputedStyle(n); const m=/rgba?\(([^)]+)\)/.exec(cs.backgroundColor||'');
      if(m){ const p=m[1].split(',').map(parseFloat);
        if(p.length<4 || p[3]>=0.98){
          const r=n.getBoundingClientRect();
          if(r.left<=rect.left+0.5 && r.right>=rect.right-0.5 && r.top<=rect.top+0.5 && r.bottom>=rect.bottom-0.5) return true;
        } }
      n=n.parentElement;
    }
    return false;
  }
  const TEXTSEL='#process-title,.process-locked,.process-step-title,.process-p,.step-band p,.step-band h3,.step-num,.ts,h1,h2,h3';
  const targets=[];
  if(out.plane.onScreen && edgeOn>0.05){
    targets.push(['plane', {left:Math.max(0,V.left),right:Math.min(vw,V.right),top:Math.max(0,V.top),bottom:Math.min(vh,V.bottom)}]);
  }
  for(const li of document.querySelectorAll('.seam i')){
    const lcs=getComputedStyle(li); const lr=li.getBoundingClientRect();
    if(lr.width<=0||lr.height<=0) continue;
    const li2=parseInset(lcs.clipPath, lr.width, lr.height)||{top:0,right:0,bottom:0,left:0};
    const a={left:lr.left+li2.left,right:lr.right-li2.right,top:lr.top+li2.top,bottom:lr.bottom-li2.bottom};
    if(a.right<=a.left||a.bottom<=a.top) continue;
    if(a.bottom<0||a.top>vh||a.right<0||a.left>vw) continue;
    targets.push(['seam:'+(li.className||'')+'/'+(li.dataset.l||''), a]);
  }
  if(targets.length){
    for(const el of document.querySelectorAll(TEXTSEL)){
      const cs=getComputedStyle(el);
      if(parseFloat(cs.opacity)<0.05 || cs.visibility==='hidden' || cs.display==='none') continue;
      if(!(el.textContent||'').trim()) continue;
      let r=el.getBoundingClientRect();
      if(r.width<=0||r.height<=0) continue;
      // krymp mot forfaders clip-path (samma monster som r12:s sweep)
      let n=el, d=0;
      while(n && n.nodeType===1 && d<8){
        d++;
        const nr=n.getBoundingClientRect(); const ni=parseInset(getComputedStyle(n).clipPath, nr.width, nr.height);
        if(ni){ r={left:Math.max(r.left,nr.left+ni.left), right:Math.min(r.right,nr.right-ni.right),
                   top:Math.max(r.top,nr.top+ni.top), bottom:Math.min(r.bottom,nr.bottom-ni.bottom)}; }
        n=n.parentElement;
      }
      if(r.right<=r.left||r.bottom<=r.top) continue;
      if(r.bottom<=0||r.top>=vh) continue;
      for(const [nm,t] of targets){
        const ov={left:Math.max(r.left,t.left), right:Math.min(r.right,t.right),
                  top:Math.max(r.top,t.top), bottom:Math.min(r.bottom,t.bottom)};
        if(ov.right-ov.left<=1 || ov.bottom-ov.top<=1) continue;
        if(ancestorOpaqueCover(el, ov)) continue;
        out.hits.push({src:nm, tag:el.tagName, cls:(el.className||'').toString().slice(0,40),
                       txt:(el.textContent||'').trim().slice(0,30),
                       ov:[Math.round(ov.left),Math.round(ov.top),Math.round(ov.right),Math.round(ov.bottom)]});
      }
    }
  }
  return out;
}"""


async def main():
    w, h = int(sys.argv[1]), int(sys.argv[2])
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto(URL, wait_until='load'); await pg.wait_for_timeout(3000)
        # medvetet trasig kontroll: utan clip-path star planet kvar i full hojd
        # och maste da korsa levande text. En kontroll som inte upptacker DET
        # mater ingenting.
        if '--break' in sys.argv:
            await pg.add_style_tag(content='.tes-plane{clip-path:none!important;height:calc(var(--pl-h,0px) + var(--dn,0px) + 900px)!important;}')
            await pg.wait_for_timeout(400)
        await pg.mouse.move(w / 2, h / 2)
        y0 = await pg.evaluate("(()=>{const t=document.getElementById('tes');return t.getBoundingClientRect().top+scrollY+t.offsetHeight-2.2*innerHeight})()")
        y1 = await pg.evaluate("(()=>{const t=document.getElementById('process');return t.getBoundingClientRect().top+scrollY+3.2*innerHeight})()")
        # grovsteg dit
        while await pg.evaluate("scrollY") < y0 - 2:
            await pg.mouse.wheel(0, 240); await pg.wait_for_timeout(18)
        await pg.wait_for_timeout(900)
        frames = []
        for direction, sign, limit in (('down', 20, y1), ('up', -20, y0)):
            n = 0
            while n < 900:
                cur = await pg.evaluate("scrollY")
                if sign > 0 and cur >= limit: break
                if sign < 0 and cur <= limit: break
                await pg.mouse.wheel(0, sign); await pg.wait_for_timeout(35); n += 1
                v = await pg.evaluate(PROBE)
                v['dir'] = direction
                frames.append(v)
            await pg.wait_for_timeout(700)
        res = {
            'vp': [w, h], 'frames': len(frames),
            'fixed_seen': any(f['plane'] and f['plane']['pos'] == 'fixed' for f in frames),
            'positions': sorted({f['plane']['pos'] for f in frames if f['plane']}),
            'hits': sum(len(f['hits']) for f in frames),
            'hit_sample': [{'y': f['y'], 'dir': f['dir'], 'h': f['hits'][:3]} for f in frames if f['hits']][:8],
            'two_sheets_frames': sum(1 for f in frames if f['twoSheets']),
            'two_sheets_sample': [{'y': f['y'], 'dir': f['dir'], 'plane': f['plane']['vis'], 'sheet': f['sheet']}
                                  for f in frames if f['twoSheets']][:6],
            'edge_max': max([f['plane']['edge'] for f in frames if f['plane']] or [0]),
        }
        print(json.dumps(res, ensure_ascii=False, indent=1))
        open(f"plane21-{w}{'-break' if '--break' in sys.argv else ''}.json", 'w', encoding='utf-8').write(json.dumps({'summary': res, 'frames': frames}, ensure_ascii=False))
        await b.close()

asyncio.run(main())
