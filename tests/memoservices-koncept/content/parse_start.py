"""parse_start.py <evidens> <content>: start page + shared chrome, verbatim."""
import json, sys
from pathlib import Path
ev, out = Path(sys.argv[1]), Path(sys.argv[2])
S = [l.strip() for l in (ev/"start.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
at = lambda s, frm=0: S.index(s, frm)
h = at("MEMOSERVICES AB · SKALA SMART. VÄX LÖNSAMT.")
start = {
 "kalla": "https://memoservices.se (hämtad 2026-10-11)",
 "meta": {"title": "MemoServices AB — Skala smart. Väx lönsamt.",
          "description": "Redovisning, skatt, HR, juridik, finans och operativ effektivisering, samlat hos oss. Rätt kompetens när du behöver den."},
 "hero": {"kicker": S[h], "rubrik_rader": [S[h+1], S[h+2]], "lead": S[h+3], "ingress": S[h+4],
          "knappar": [{"text": S[h+5], "till": "/tjanster"}, {"text": S[h+6], "till": "https://assess.memoservices.no", "extern": True}]},
}
t = at("TJÄNSTEOMRÅDEN")
start["tjansteomraden"] = {"kicker": S[t], "rubrik": S[t+1], "lank": {"text": S[t+2], "till": "/tjanster"},
                           "kort": "se tjanster.json: namn + kort_pa_startsidan + mosaik, länkar till /tjanster/<slug>",
                           "kortlank_text": "Läs mer →"}
f = at("Behöver du hjälp inom flera områden?")
start["tjansteomraden"]["flera_omraden"] = {"rubrik": S[f], "text": S[f+1], "lank": {"text": S[f+2], "till": "/kontakt"}}
k = at("KARTLÄGGNING")
start["kartlaggning"] = {"kicker": S[k], "rubrik": S[k+1], "text": S[k+2], "knapp": {"text": S[k+3], "till": "https://assess.memoservices.no", "extern": True}}
o = at("OM MEMOSERVICES AB")
start["om"] = {"ankare": "om", "kicker": S[o], "rubrik_rader": [S[o+1], S[o+2]], "text": S[o+3],
               "koncern": S[o+4], "koncern_lank": "https://www.memoservices.no",
               "punkter": S[o+5:o+9],
               "punkter_fetstil": ["En fast kontaktperson", "Sju tjänsteområden", "På plats i Göteborg", "Alla kan bli delägare"],
               "punkter_not": "Fetstilen är <strong> i originalets HTML. Punktmarkör: röd för de tre första, lime för den fjärde."}
assert start["om"]["punkter"][0].startswith("En fast kontaktperson") and start["om"]["punkter"][3].startswith("Alla kan"), start["om"]
i = at("INSIKTER"); j = at("Lindholmspiren 7, 417 56 Göteborg", i)
cards = S[i+2:j]; assert len(cards) == 9, cards
start["insikter"] = {"rubrik": S[i], "lank": {"text": S[i+1], "till": "https://memoservices.se/insikter", "extern": True},
  "artiklar": [{"kategori_datum": cards[n], "rubrik": cards[n+1], "utdrag": cards[n+2]} for n in (0, 3, 6)],
  "artikel_lankar": ["https://memoservices.se/insikter/3-ekonomiska-blind-spots-och-hur-ai-hjalper-dig-upptacka-dem-i-tid",
                     "https://memoservices.se/insikter/gir-2025-narmar-sig-gor-rapporteringen-enklare",
                     "https://memoservices.se/insikter/ny-kartlaggning-se-var-ditt-bolag-star"]}
shared = {
 "kalla": "header/footer på memoservices.se (hämtad 2026-10-11)",
 "nav": [["Tjänster","/tjanster"],["Insikter","https://memoservices.se/insikter"],["Om oss","/#om"],["Karriär","https://memoservices.se/karriar"],
         ["Kontakt","https://memoservices.se/kontakt"],["Gör en kartläggning ↗","https://assess.memoservices.no"]],
 "nav_knapp": ["Kontakta oss","https://memoservices.se/kontakt"],
 "footer": {"adress": "Lindholmspiren 7, 417 56 Göteborg", "epost": "hej@memoservices.se",
   "kolumner": {"TJÄNSTER": "de sju tjänsterna -> /tjanster/<slug>",
                "FÖRETAGET": [["Insikter","https://memoservices.se/insikter"],["Om oss","/#om"],["Karriär","https://memoservices.se/karriar"],["Kontakt","https://memoservices.se/kontakt"],["Gör en kartläggning ↗","https://assess.memoservices.no"]],
                "JURIDISKT": [["Integritetspolicy","https://memoservices.se/integritetspolicy"],["Cookies","https://memoservices.se/cookies"],["AI Act","https://memoservices.se/ai-forordningen"]]},
   "copyright": "© 2026 MemoServices AB", "koncernrad": "MemoServices AB är en del av MemoServices-koncernen", "koncernlank": ["www.memoservices.no ↗","https://www.memoservices.no"]},
 "kontaktperson": {"namn": "Linda Swartling", "titel": "VD, MemoServices AB", "epost": "linda.swartling@memoservices.se", "telefon": "076-328 51 71",
                   "kalla": "https://memoservices.se/kontakt"},
}
for k_, v in [("start.json", start), ("delat.json", shared)]:
    (out/k_).write_text(json.dumps(v, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(start, ensure_ascii=False, indent=1))
