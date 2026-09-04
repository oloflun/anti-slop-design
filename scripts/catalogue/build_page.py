#!/usr/bin/env python3
"""build_page.py -> sites/catalogue.html

One static page, no framework. Embeds index.json + each entry's body sections
(brief, reference lock, image recipe, motion) so the page works from the cloud with
no server: category chips with counts, cards (fold thumbnail, DNA line, chips),
detail panel with COPY BRIEF / COPY REFERENCE LOCK / COPY IMAGE PROMPT.
Image paths are relative to sites/ (../design-catalogue/entries/<slug>/fold.webp).
Run index.py first.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CAT = ROOT / "design-catalogue"
OUT = ROOT / "sites" / "catalogue.html"

SECTIONS = ["Why it works", "What to borrow (principle)", "What to leave", "Signature move",
            "Motion", "Brief", "Image recipe", "Photo search", "Reference lock"]


def body_sections(md: str) -> dict:
    body = md.split("\n---\n", 2)[-1] if md.startswith("---") else md
    out = {}
    parts = re.split(r"^## +", body, flags=re.M)
    for part in parts[1:]:
        title, _, text = part.partition("\n")
        out[title.strip()] = text.strip()
    return out


def main():
    index = json.loads((CAT / "index.json").read_text(encoding="utf-8"))
    cats = json.loads((CAT / "categories.json").read_text(encoding="utf-8"))
    entries = []
    for e in index:
        md = (CAT / "entries" / e["slug"] / "entry.md").read_text(encoding="utf-8")
        secs = body_sections(md)
        d = CAT / "entries" / e["slug"]
        e = dict(e)
        e["img"] = f"../design-catalogue/entries/{e['slug']}/" + ("fold.webp" if (d / "fold.webp").exists() else "shot.webp")
        e["full"] = f"../design-catalogue/entries/{e['slug']}/shot.webp" if (d / "shot.webp").exists() else e["img"]
        e["sections"] = {k: secs.get(k, "") for k in SECTIONS}
        e["has_extract"] = (d / "extract").exists()
        entries.append(e)

    data = json.dumps({"entries": entries, "categories": cats}, ensure_ascii=False)
    n = len(entries)

    page = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Design catalogue · anti-slop-design</title>
<style>
:root{--bg:#F4F2EC;--bg2:#EAE7DF;--ink:#16171A;--ink2:#5C5F66;--line:#D6D2C8;--acc:#1E5E9C;--chip:#E3E0D7}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 Inter,system-ui,sans-serif}
header{padding:40px 32px 20px;max-width:1480px;margin:0 auto}
h1{font:600 28px/1.1 Inter,system-ui,sans-serif;letter-spacing:-.02em;margin:0 0 6px}
.sub{color:var(--ink2);font-size:13px;font-family:ui-monospace,Consolas,monospace;letter-spacing:.08em;text-transform:uppercase}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 0}
.chip{border:1px solid var(--line);background:transparent;padding:6px 12px;border-radius:999px;font:12px ui-monospace,Consolas,monospace;letter-spacing:.06em;text-transform:uppercase;cursor:pointer;color:var(--ink)}
.chip[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.chip b{font-weight:500;opacity:.6;margin-left:6px}
main{max-width:1480px;margin:0 auto;padding:12px 32px 80px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px}
.card{background:#fff;border:1px solid var(--line);border-radius:6px;overflow:hidden;cursor:pointer;display:flex;flex-direction:column}
.card:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.card img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top;background:var(--bg2)}
.card .b{padding:12px 14px 14px}
.card h2{font:600 15px/1.2 Inter,system-ui,sans-serif;margin:0 0 4px}
.card .dna{color:var(--ink2);font-size:12px;margin:0 0 8px}
.card .t{display:flex;flex-wrap:wrap;gap:4px}.card .t span{background:var(--chip);border-radius:3px;padding:2px 6px;font-size:11px}
.card .m{margin-top:8px;font:11px ui-monospace,Consolas,monospace;color:var(--ink2);letter-spacing:.06em;text-transform:uppercase;display:flex;justify-content:space-between}
dialog{border:0;border-radius:8px;padding:0;max-width:1100px;width:calc(100% - 40px);max-height:calc(100vh - 40px);background:var(--bg);color:var(--ink)}
dialog::backdrop{background:rgba(20,20,20,.55)}
.dl{display:grid;grid-template-columns:1.1fr 1fr;gap:0}
.dl img{width:100%;display:block;object-fit:cover;object-position:top;max-height:calc(100vh - 40px)}
.dr{padding:28px 28px 32px;overflow:auto;max-height:calc(100vh - 40px)}
.dr h2{margin:0 0 4px;font:600 22px/1.1 Inter,system-ui,sans-serif}
.dr .meta{font:11px ui-monospace,Consolas,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--ink2);margin-bottom:14px}
.dr h3{font:600 11px ui-monospace,Consolas,monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);margin:18px 0 6px;padding-top:12px;border-top:1px solid var(--line)}
.dr p,.dr pre{white-space:pre-wrap;font:13px/1.5 Inter,system-ui,sans-serif;margin:0}
.btns{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0}
.btn{border:1px solid var(--ink);background:transparent;padding:8px 12px;border-radius:4px;font:600 12px Inter,system-ui,sans-serif;cursor:pointer;color:var(--ink)}
.btn:hover{background:var(--ink);color:var(--bg)}
.pal{display:flex;gap:4px;margin:6px 0}.pal i{width:22px;height:22px;border-radius:3px;border:1px solid rgba(0,0,0,.1)}
.empty{grid-column:1/-1;color:var(--ink2);padding:40px 0}
@media (max-width:820px){.dl{grid-template-columns:1fr}.dl img{max-height:40vh}}
</style></head><body>
<header><h1>Design catalogue</h1><div class="sub">__N__ references · anti-slop-design · read as pixels, borrow as principle</div>
<div class="chips" id="chips"></div></header>
<main id="grid"></main>
<dialog id="dlg"><div class="dl"><img id="dimg" alt=""><div class="dr">
<h2 id="dtitle"></h2><div class="meta" id="dmeta"></div><div class="pal" id="dpal"></div>
<div class="btns"><button class="btn" data-copy="Brief">Copy brief</button><button class="btn" data-copy="Reference lock">Copy reference lock</button><button class="btn" data-copy="Image recipe">Copy image prompt</button><a class="btn" id="dopen" target="_blank" rel="noopener">Open site</a><button class="btn" id="dclose">Close</button></div>
<div id="dsecs"></div></div></div></dialog>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const grid=document.getElementById('grid'),chips=document.getElementById('chips'),dlg=document.getElementById('dlg');
let active='all';
const esc=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function renderChips(){
  const all=[{category:'all',count:D.entries.length}].concat(D.categories);
  chips.innerHTML=all.map(c=>`<button class="chip" aria-pressed="${c.category===active}" data-c="${esc(c.category)}">${esc(c.category)}<b>${c.count}</b></button>`).join('');
}
function renderGrid(){
  const list=D.entries.filter(e=>active==='all'||e.category===active||e.category2===active);
  grid.innerHTML=list.length?list.map((e,i)=>`<article class="card" tabindex="0" data-slug="${esc(e.slug)}">
   <img src="${esc(e.img)}" alt="${esc(e.title)} fold" loading="lazy">
   <div class="b"><h2>${esc(e.title)}</h2><p class="dna">${esc(e.dna||e.lane)}</p>
   <div class="t">${(e.traits||[]).slice(0,5).map(t=>`<span>${esc(t)}</span>`).join('')}${(e.traits||[]).length>5?`<span>+${e.traits.length-5}</span>`:''}</div>
   <div class="m"><span>${esc(e.category)}${e.category2?' · '+esc(e.category2):''}</span><span>${String(i+1).padStart(2,'0')} / ${list.length}${e.has_extract?' · ext':''}</span></div></div></article>`).join('')
   :'<p class="empty">No entries in this category yet.</p>';
}
function open(slug){
  const e=D.entries.find(x=>x.slug===slug);if(!e)return;
  document.getElementById('dimg').src=e.full;document.getElementById('dtitle').textContent=e.title;
  document.getElementById('dmeta').textContent=[e.category,e.category2,e.register,e.grammar,e.mode,e.origin,'extract '+e.extract].filter(Boolean).join(' · ');
  document.getElementById('dpal').innerHTML=(e.palette||[]).map(c=>`<i style="background:${esc(c)}" title="${esc(c)}"></i>`).join('');
  const o=document.getElementById('dopen');if(e.url&&e.url.startsWith('http')){o.href=e.url;o.hidden=false}else{o.hidden=true}
  document.getElementById('dsecs').innerHTML=Object.entries(e.sections).filter(([k,v])=>v).map(([k,v])=>`<h3>${esc(k)}</h3><p>${esc(v)}</p>`).join('');
  dlg.querySelectorAll('[data-copy]').forEach(b=>b.onclick=()=>{navigator.clipboard.writeText(e.sections[b.dataset.copy]||'');b.textContent='Copied';setTimeout(()=>b.textContent=b.dataset.copy==='Brief'?'Copy brief':b.dataset.copy==='Reference lock'?'Copy reference lock':'Copy image prompt',1200)});
  dlg.showModal();
}
chips.addEventListener('click',ev=>{const b=ev.target.closest('.chip');if(!b)return;active=b.dataset.c;renderChips();renderGrid()});
grid.addEventListener('click',ev=>{const c=ev.target.closest('.card');if(c)open(c.dataset.slug)});
grid.addEventListener('keydown',ev=>{const c=ev.target.closest('.card');if(c&&(ev.key==='Enter'||ev.key===' ')){ev.preventDefault();open(c.dataset.slug)}});
document.getElementById('dclose').onclick=()=>dlg.close();
dlg.addEventListener('click',ev=>{if(ev.target===dlg)dlg.close()});
renderChips();renderGrid();
</script></body></html>"""
    page = page.replace("__N__", str(n)).replace("__DATA__", data.replace("</", "<\\/"))
    OUT.write_text(page, encoding="utf-8")
    print(f"build_page.py: {n} entries -> {OUT}")


if __name__ == "__main__":
    main()
