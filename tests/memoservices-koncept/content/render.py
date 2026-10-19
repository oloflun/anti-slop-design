"""Fyller en cell-mall med ordagrant innehåll ur content/*.json.

    python render.py <template.html> <out.html>

Mallspråk (medvetet litet):
  {{hero.kicker}}            värde ur start.json / delat.json / tjanster.json / ny-text.json
  {{#tjanster}} ... {{/tjanster}}   upprepar blocket per tjänst; inuti: {{.namn}} {{.slug}} {{.mosaik.huvudfarg}} {{@index}} {{@n}}
  {{#om.punkter}} ... {{/om.punkter}}  lista av strängar: {{.}} ; parallell lista med samma index: {{^om.punkter_fetstil}}
  {{#insikter.artiklar}} ... {{/insikter.artiklar}}  inuti även {{^insikter.artikel_lankar}} (parallell lista)
Allt annat i mallen lämnas som det är. Texten kommer alltså aldrig från byggarens hand.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
def load(n): return json.loads((HERE / n).read_text(encoding="utf-8"))
START, DELAT, TJ, NY = load("start.json"), load("delat.json"), load("tjanster.json"), load("ny-text.json")
ROOT = {**START, "delat": DELAT, "tjanster": TJ["tjanster"], "oversikt": TJ["oversikt"], "ny": NY}

def get(ctx, path):
    cur = ctx
    for part in path.split("."):
        if part == "": continue
        if isinstance(cur, list): cur = cur[int(part)]
        else: cur = cur[part]
    return cur

LOOP = re.compile(r"\{\{#([\w.]+)\}\}(.*?)\{\{/\1\}\}", re.S)
VAR = re.compile(r"\{\{(\.?[\w.]*|@index|@n|\^[\w.]+)\}\}")

def render(tpl, ctx, item=None, index=None):
    def loop(m):
        items = get(ctx, m.group(1))
        return "".join(render(m.group(2), ctx, it, i) for i, it in enumerate(items))
    tpl = LOOP.sub(loop, tpl)
    def var(m):
        key = m.group(1)
        if key == "@index": return str(index)
        if key == "@n": return f"{index+1:02d}"
        if key.startswith("^"):               # parallell lista, samma index
            return str(get(ctx, key[1:])[index])
        if key == ".": return str(item)
        if key.startswith("."): return str(get(item, key[1:]))
        return str(get(ctx, key))
    return VAR.sub(var, tpl)

if __name__ == "__main__":
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    html = render(src.read_text(encoding="utf-8"), ROOT)
    assert "{{" not in html, "ofylld platshållare kvar: " + html[html.index("{{"):html.index("{{")+60]
    out.write_text(html, encoding="utf-8")
    print("skrev", out, len(html.splitlines()), "rader")
