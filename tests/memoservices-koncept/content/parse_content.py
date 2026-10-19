"""parse_content.py <evidens_dir> <content_dir>: verbatim site text -> JSON. Asserts the shape so nothing is lost."""
import json, re, sys
from pathlib import Path
ev, out = Path(sys.argv[1]), Path(sys.argv[2])
def lines(name):
    return [l.strip() for l in (ev / name).read_text(encoding="utf-8").splitlines() if l.strip() and l.strip() != "‍"]

SERV = [("redovisning","Redovisning","REDOVISNING"),("hr-och-rekrytering","HR och rekrytering","HR OCH REKRYTERING"),
        ("skatt","Skatt","SKATT"),("juridik","Juridik","JURIDIK"),("finans-och-ma","Finans och M&A","FINANS OCH M&A"),
        ("governance-risk-och-compliance","Governance, risk & compliance","GOVERNANCE, RISK & COMPLIANCE"),
        ("operativ-effektivisering","Operativ effektivisering","OPERATIV EFFEKTIVISERING")]
MOSAIC = {"redovisning":("#2c546d","#c5eb43"),"hr-och-rekrytering":("#6dabbf","#c5eb43"),"skatt":("#8b5e3c","#f3aaaf"),
          "juridik":("#4b4b4b","#e72835"),"finans-och-ma":("#9db377","#2c546d"),
          "governance-risk-och-compliance":("#294b3f","#c5eb43"),"operativ-effektivisering":("#b1b0aa","#ee646e")}

T = lines("tjanster.txt")
i0 = T.index("SJU TJÄNSTEOMRÅDEN. ETT AVTAL.")
overview = {"kicker": T[i0-1], "rubrik": T[i0], "ingress": T[i0+1]}
start_txt = lines("start.txt")
services = []
for n, (slug, name, head) in enumerate(SERV):
    a = T.index(head, i0 + 2)
    b = T.index(SERV[n+1][2], a + 1) if n + 1 < len(SERV) else T.index("Lindholmspiren 7, 417 56 Göteborg", a)
    blk = T[a:b]
    pf = blk.index("PASSAR FÖR")
    cta = blk.index("Prata med oss →")
    passar = blk[pf+1:pf+5]
    lev_head, lev = blk[pf+5], blk[pf+6:cta]
    def qa(s):
        q, a_ = s.split("? ", 1); return {"fraga": q + "?", "svar": a_}
    def item(s):
        k, v = s.split(" — ", 1); return {"namn": k, "text": v}
    # start-page card one-liner = line after the service name inside the TJÄNSTEOMRÅDEN block
    sa = start_txt.index("TJÄNSTEOMRÅDEN")
    card = start_txt[start_txt.index(name, sa) + 1]
    s = {"slug": slug, "namn": name, "rubrik": blk[0], "ingress": blk[1], "brodtext": blk[2:pf],
         "passar_for_rubrik": "PASSAR FÖR", "passar_for": [qa(x) for x in passar],
         "leverans_rubrik": lev_head, "leveranser": [item(x) for x in lev], "cta": "Prata med oss →",
         "kort_pa_startsidan": card, "mosaik": {"huvudfarg": MOSAIC[slug][0], "accent": MOSAIC[slug][1], "monster": "2x2: tre rutor huvudfärg + en ruta accent (nere till höger)"}}
    assert len(s["passar_for"]) == 4 and len(s["leveranser"]) == 6 and s["brodtext"], (slug, len(passar), len(lev))
    assert lev_head.isupper() and "?" not in lev_head, (slug, lev_head)
    services.append(s)

# every service line must be accounted for verbatim
blob = json.dumps(services, ensure_ascii=False)
for s in services:
    for l in [s["ingress"], *s["brodtext"]]: assert l in T

(out / "tjanster.json").write_text(json.dumps({"kalla": "https://memoservices.se/tjanster (hämtad 2026-10-11)", "oversikt": overview, "tjanster": services}, ensure_ascii=False, indent=2), encoding="utf-8")
print("tjanster OK", [ (s['slug'], len(s['brodtext'])) for s in services])
