#!/usr/bin/env python3
"""browse.py -- writes design-catalogue/browse.html: every entry in rank order, one view at a
time, with the contact sheet, the reading, and a link to the original site.

Run index.py first. Open the HTML straight from disk or via scripts/serve.py.
Keys: ←/→ previous/next · o opens the original · / focuses the filter.
"""
import json
import re
from html import escape
from pathlib import Path

from index import parse_frontmatter  # same folder

ROOT = Path(__file__).resolve().parent.parent.parent
CAT = ROOT / "design-catalogue"


def body_html(md: str) -> str:
    out = []
    for line in md.splitlines():
        s = line.strip()
        if not s or s.startswith("<!--"):
            continue
        if s.startswith("## "):
            out.append(f"<h3>{escape(s[3:])}</h3>")
        elif s.startswith("- "):
            out.append(f"<li>{escape(s[2:])}</li>")
        else:
            out.append(f"<p>{escape(s)}</p>")
    # ponytail: adjacent <li> are not wrapped in <ul>; the CSS styles li as a list row anyway
    return "\n".join(out)


def main():
    index = json.loads((CAT / "index.json").read_text(encoding="utf-8"))
    items = []
    for e in index:
        d = CAT / "entries" / e["slug"]
        _fm, body = parse_frontmatter((d / "entry.md").read_text(encoding="utf-8"))
        img = next((f"entries/{e['slug']}/{p}" for p in ("motion/sheet.webp", "shot.webp", "fold.webp") if (d / p).exists()), "")
        items.append({k: e.get(k, "") for k in ("slug", "title", "url", "rank", "motion_floor", "showcase", "category", "category2",
                                                 "register", "grammar", "mode", "dna", "lane", "traits", "family")}
                     | {"img": img, "body": body_html(body)})
    data = json.dumps(items, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.replace("__DATA__", data).replace("__N__", str(len(items)))
    (CAT / "browse.html").write_text(html, encoding="utf-8")
    print(f"browse.py: wrote {len(items)} entries to design-catalogue/browse.html")


TEMPLATE = r"""<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><title>Referenskatalog · __N__ sidor</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{--ink:#111;--mute:#6b6b6b;--line:#e3e3e3;--bg:#fff;--acc:#0a7a46}
*{box-sizing:border-box}body{margin:0;font:14px/1.45 system-ui,sans-serif;color:var(--ink);background:var(--bg);display:grid;grid-template-columns:300px 1fr;height:100vh}
aside{border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0}
aside input{margin:10px;padding:8px 10px;border:1px solid var(--line);border-radius:6px;font:inherit}
#list{overflow:auto;flex:1}#list a{display:block;padding:7px 12px;text-decoration:none;color:inherit;border-bottom:1px solid var(--line)}
#list a.on{background:#f1f5f2}#list .r{color:var(--mute);font-variant-numeric:tabular-nums;display:inline-block;width:3.2em}
#list .f{float:right;color:var(--mute)}
main{overflow:auto;padding:18px 28px 60px}
header{display:flex;gap:16px;align-items:baseline;flex-wrap:wrap}header h1{margin:0;font-size:22px}
header .nav button{font:inherit;padding:6px 10px;border:1px solid var(--line);background:#fff;border-radius:6px;cursor:pointer}
.open{color:var(--acc);font-weight:600}
.meta{color:var(--mute);margin:6px 0 12px}.meta span{margin-right:12px}
.rank{display:inline-block;background:var(--ink);color:#fff;border-radius:4px;padding:1px 7px;font-weight:600;margin-right:8px}
img.sheet{max-width:100%;border:1px solid var(--line);display:block;margin:0 0 18px}
article{max-width:70ch}article h3{margin:18px 0 6px;font-size:15px}article li{margin:0 0 4px 1.2em}article p{margin:0 0 8px}
.lane{font-style:italic;color:#333}.dna{font-weight:600}
kbd{border:1px solid var(--line);border-radius:4px;padding:0 5px;color:var(--mute)}
@media (max-width:800px){body{grid-template-columns:1fr;height:auto}aside{max-height:35vh}}
</style></head><body>
<aside><input id="q" placeholder="filtrera (namn, familj, grammatik, register…)  /"><div id="list"></div></aside>
<main>
<header><div class="nav"><button id="prev">←</button> <button id="next">→</button></div><h1 id="title"></h1><a id="open" class="open" target="_blank" rel="noopener">Öppna originalet ↗ <kbd>o</kbd></a></header>
<div class="meta" id="meta"></div>
<img class="sheet" id="sheet" alt="">
<article id="body"></article>
</main>
<script>
const D=__DATA__;let view=D,i=0;
const $=s=>document.querySelector(s);
function tag(e){return e.rank?'#'+e.rank:'f'+e.motion_floor}
function render(){const e=view[i];if(!e)return;location.hash=e.slug;
 $('#title').innerHTML=(e.rank?'<span class="rank">#'+e.rank+'</span>':'')+e.title;
 $('#open').href=e.url;$('#open').style.display=e.url?'':'none';
 $('#meta').innerHTML=['floor '+e.motion_floor,e.showcase&&'showcase '+e.showcase,e.category+(e.category2?' / '+e.category2:''),e.register,e.grammar,e.mode,e.family].filter(Boolean).map(x=>'<span>'+x+'</span>').join('');
 $('#sheet').src=e.img;$('#sheet').style.display=e.img?'':'none';
 $('#body').innerHTML='<p class="dna">'+e.dna+'</p><p class="lane">'+e.lane+'</p>'+(e.traits&&e.traits.length?'<p>'+e.traits.join(' · ')+'</p>':'')+e.body;
 [...$('#list').children].forEach((a,k)=>{a.classList.toggle('on',k===i);if(k===i)a.scrollIntoView({block:'nearest'})});
 $('main').scrollTop=0}
function list(){$('#list').innerHTML=view.map((e,k)=>'<a href="#'+e.slug+'" data-k="'+k+'"><span class="r">'+tag(e)+'</span>'+e.title+'<span class="f">'+(e.showcase||'')+'</span></a>').join('');}
$('#list').onclick=ev=>{const a=ev.target.closest('a');if(!a)return;ev.preventDefault();i=+a.dataset.k;render()};
$('#q').oninput=()=>{const q=$('#q').value.toLowerCase();view=D.filter(e=>JSON.stringify([e.slug,e.title,e.family,e.grammar,e.register,e.category,e.category2,e.mode,e.dna,e.traits]).toLowerCase().includes(q));i=0;list();render()};
$('#prev').onclick=()=>{i=(i-1+view.length)%view.length;render()};$('#next').onclick=()=>{i=(i+1)%view.length;render()};
document.onkeydown=ev=>{if(ev.target.tagName==='INPUT'){if(ev.key==='Escape')ev.target.blur();return}
 if(ev.key==='ArrowLeft')$('#prev').click();else if(ev.key==='ArrowRight')$('#next').click();else if(ev.key==='o'&&view[i].url)window.open(view[i].url,'_blank');else if(ev.key==='/'){ev.preventDefault();$('#q').focus()}};
const h=decodeURIComponent(location.hash.slice(1));const k=D.findIndex(e=>e.slug===h);if(k>=0)i=k;list();render();
</script></body></html>"""


if __name__ == "__main__":
    main()
