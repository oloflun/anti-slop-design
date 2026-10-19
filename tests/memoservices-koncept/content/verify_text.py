"""Kontroll enligt BESTALLNING § 2.5: varje synlig textnod på den renderade sidan finns
ordagrant i content/*.json (eller är ny text ur ny-text.json). Körs med JavaScript AV så att
SplitText inte har delat upp orden. 0 avvikelser krävs.

    python verify_text.py <url> [--allow "extra sträng" ...]
Bevis mot trasig variant: --inject "Påhittad mening" lägger till ett stycke och måste ge 1 avvikelse.
"""
import json, re, sys, argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
def strings(o, acc):
    if isinstance(o, str): acc.add(norm(o))
    elif isinstance(o, dict): [strings(v, acc) for v in o.values()]
    elif isinstance(o, list): [strings(v, acc) for v in o]
    return acc
def norm(s): return re.sub(r"\s+", " ", s.replace("\u00a0", " ").replace("\u200d", "")).strip()

ALLOWED = set()
for n in ("start.json", "delat.json", "tjanster.json", "ny-text.json"):
    strings(json.loads((HERE / n).read_text(encoding="utf-8")), ALLOWED)
for k in json.loads((HERE / "delat.json").read_text(encoding="utf-8"))["footer"]["kolumner"]:
    ALLOWED.add(norm(k))  # TJÄNSTER / FÖRETAGET / JURIDISKT är rubriker i originalet, lagrade som nycklar
ALLOWED.discard("")

ap = argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--allow", action="append", default=[]); ap.add_argument("--inject", default=None)
a = ap.parse_args()
for s in a.allow: ALLOWED.add(norm(s))

JS = r"""
() => {
  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const el = n.parentElement;
    if (!el || ['SCRIPT','STYLE','NOSCRIPT','TEMPLATE'].includes(el.tagName)) continue;
    const t = n.textContent.replace(/\s+/g,' ').trim();
    if (!t) continue;
    // närmaste blockförälder: dess hela text används som alternativ (täcker <strong> i en mening)
    let p = el; while (p && getComputedStyle(p).display.startsWith('inline')) p = p.parentElement;
    out.push({t, parent: (p||el).textContent.replace(/\s+/g,' ').trim(), tag: el.tagName, cls: el.className});
  }
  return out;
}"""
with sync_playwright() as pw:
    b = pw.chromium.launch(); ctx = b.new_context(java_script_enabled=False); pg = ctx.new_page()
    pg.goto(a.url, wait_until="load")
    if a.inject:
        ctx2 = b.new_context(java_script_enabled=True); pg2 = ctx2.new_page(); pg2.goto(a.url); pg2.evaluate("t=>{const p=document.createElement('p');p.textContent=t;document.body.appendChild(p)}", a.inject); nodes = pg2.evaluate(JS)
    else:
        nodes = pg.evaluate(JS)
    b.close()
def ok(x):
    t = norm(x["t"])
    if re.fullmatch(r"\d{1,3}", t): return True   # löpnummer (01–07) i eget element är inte copy
    return t in ALLOWED or norm(x["parent"]) in ALLOWED
bad = [x for x in nodes if not ok(x)]
for x in bad: print("AVVIKELSE", x["tag"], x["cls"], "|", x["t"][:120])
print(f"{len(nodes)} textnoder, {len(bad)} avvikelser")
sys.exit(1 if bad else 0)
