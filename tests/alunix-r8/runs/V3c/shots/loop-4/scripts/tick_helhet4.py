"""tick_helhet4.py: HELHET.md § 3 loop-4 pass on the R9 state (md5 909916d1). Flip each
row's checkbox to the loop-4 verdict, append a '· loop 4' line after the row's '· loop 3'
line, and add the loop-4 preamble. Probe-dependent rows read PROBE below (filled after
probes4.sh)."""
import re, json
from pathlib import Path
P = Path("C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3c/HELHET.md")
s = P.read_text(encoding="utf-8")
L4 = "  · loop 4 (2026-09-17), R9-läget `909916d1`: "
PROBE = json.load(open(Path(__file__).with_name("probe4_rows.json"), encoding="utf-8"))
rows = {
 "H-01": ("[x]", "10 880 px = 12,09 vh vid 1440 vid load, 10 582 px = 11,76 vh när prisblocket målats (plan 042: platshållaren 760 px är 297 px högre än blocket); 11 588 / 11 326 px = 13,73 / 13,42 vh vid 390 (`shots/loop-4/geom4.json`, `mountshift.json`); heron 3 060 px = 28 till 29 %. Inom 8 till 14 i båda lägena; bockad, dokumenthöjden blir konstant med 042"),
 "H-02": ("[ ]", "bandet står (Q30, väntar på Anton); process, principer och avslut äger sina skärmar (`slices-1440/v3c-1440--s06.png` till `s12`); tes + jätterubrik samtidigt (`s03`)"),
 "H-03": ("[ ]", "två helbredds materialbyten (papper vid `#process` `s05`/`s06`, foto vid avslutet `s11`/`s12`); tesen och priset spaltbreda. Q30, väntar på Anton"),
 "H-04": ("[x]", "`.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px (`geom4.json`, `slices-1440/v3c-1440--s03.png`)"),
 "H-05": ("[x]", "1440: 162 px vid alla seams (3 060 → 3 222, 3 600 → 3 762, 4 150 → 4 312, 4 611 → 4 773; `geom4.json`); pris → papper helbrett vid 5 340 (efter första målningen) / 5 637 (före), plan 042 gör det till ett värde; 390: 101 till 102 px (`slices-390/v3c-390--s03.png` till `s07`)"),
 "H-06": ("[x]", "sex anatomier i följd, ingen två gånger i rad (`slices-1440/…s03` till `s12`)"),
 "H-07": ("[x]", "`.giant` 88 px, −3,52 px tracking, ordet 1 rect, 3 rader vid 1440; 33,6 px, 2 rader vid 390 (`geom4.json`, `preview/preview-1440-ledger.png`, `slices-390/v3c-390--s05.png`)"),
 "H-08": ("[ ]", "`s03` tes + jätterubrik lika tunga (Q30, väntar på Anton); `slices-1440/v3c-1440--s04.png`: Calyx dominerar liggaren; `s05`: Hōrai dominerar priset, båda ramarna hela i vanliga `scrollTo`-skivor (035). Öppen bara för s03"),
 "H-09": ("[x]", "`preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/v3c-1440-flip-11-100.png`: glyfen fyller kortets högra halva"),
 "H-10": ("[x]", "`flip-1440/v3c-1440-flip-05-045.png`, `-06-055.png`, `flip-390/…-05-045.png`: kortet med full höjd på kant, 4 px kant"),
 "H-11": ("[x]", "`slices-1440/v3c-1440--s05.png`, `slices-390/v3c-390--s06.png`: grafitplanet `oklch(0.27 0.012 250)` läser som material mot fotot (`preview390.json` priceBg)"),
 "H-12": ("[x]", "`footer.close` 900 px = 100 svh, ensam i `slices-1440/v3c-1440--s12.png`; 844 px vid 390 (`s13`); mailto 98 px hög, 86,4 px teckenstorlek vid 1440 (`geom4.json`)"),
 "H-13": ("[x]", "84 px = 10,0 % död grund under underraden vid 390x844 (`geom4.json deadFold`; `slices-390/v3c-390--s00.png`, `preview/preview-390-front.png`)"),
 "H-14": ("[x]", "390: tes 2 870 → Calyx 3 459 → jätterubrik 4 157 → Hōrai 4 935 → pris 5 599 (`geom4.json`, `slices-390/…s03` till `s07`)"),
 "H-15": ("[ ]", "konturen hel medan steg 01 läses där motorns topp stämmer (040): `slices-1440/v3c-1440--s06.png`, `process-1440/v3c-1440-life-02.png`, `process-390/v3c-390-life-01.png`; men `process-1440/v3c-1440-life-01.png` (Astra loop 4 bild 77): steg 01 läsbart nere till vänster, högerspalten tom, för att motorn räknar `#process` från 5 637 medan DOM:en står på 5 340 efter prisblockets första målning (`--sc-p` 0,091 mot sant 0,154; `mountshift.json`). Plan 042, inte 040"),
 "H-16": ("[x]", PROBE["H-16"]),
 "H-17": ("[x]", "oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R9); statiska svansen 393 px"),
 "H-18": ("[x]", "oförändrat, 1 602 px; `flip-1440/` och `flip-390/` tolv ramar jämn rotation"),
 "H-19": ("[ ]", "mätpunkterna håller: träpanelen (720,180) vid tesen centrerad (119,130,140), chroma 21; folden chroma 0 (`geom4.json thesis_px`, `fold_px`); `slices-1440/v3c-1440--s03.png`: kallt ljus. Men överlämningen tes → jätte hoppar: `--sc-canvas` rgb(18,63,104) vid scrollY 3 600, rgb(244,242,238) vid 3 620, träet chroma 21 → 2 på 20 px (`astra-verify/verify_astra4.json`, `drift-3580.png`, `drift-3620.png`; Astra loop 4 fix 3): ljuset släcks i ett steg i stället för att tona. Plan 044"),
 "H-20": ("[x]", "`preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`; `.thesis-figure` transform translateX 86,5 px vid `--sc-ps` ≈ 0,95, 100 px vid 1 (R7 D), spåret levande (`geom4.json thesisFigAtLater`)"),
 "H-21": ("[ ]", PROBE["H-21"]),
 "H-22": ("[ ]", PROBE["H-22"]),
 "H-23": ("[x]", PROBE["H-23"]),
 "H-24": ("[ ]", "spårade: hero, `.plate-card`, `#process`, `#giant-section`, `.price`, `.panel-thesis`, `footer.close`, `.horai-wrap:--rv` och `.horai-wrap .rv:transform` (inga DEAD); `.giant` scale, `#threadFill`, `.close-rule`, `.thesis-figure` oprobade (proben blind för ren `scale()`). Verktygsskuld, oförändrad"),
 "H-25": ("[x]", "priset: liggarens tredje linje mitt i dragningen i `slices-1440/v3c-1440--s05.png` mot hel i `process-1440/v3c-1440-life-00.png`; avslutets linje `s11`/`s12`; Hōrai iris (`--rv` 0,9487 i `s05`) och ordscrubben på s4; Calyx-revealen sker inte (043) men skärmen s4 bär ordscrubben, så raden håller per skärm; jättens skala 0,92 → 1 oläsbar i tolv ramar (rapporterad, redundant mot ordscrubben)"),
 "H-26": ("[x]", "grep `prefers-reduced-motion` 0; alla skivor tagna under `reduced_motion=\"reduce\"` visar allt innehåll"),
 "H-27": ("[ ]", "latchen: `shots/loop-4/latch4.json`: hjul, PageDown, `scrollTo` och smooth `scrollTo` till scrollY 4 703 ger `--rv` 1 / 1 på båda wrapparna; resize 1440 → 1280 före bandet, sedan hjul: 1 / 1; noll `--rv`-skrivningar tre sekunder efter landning; ingen transform på ramen efter visning (identitet vid `--rv` 1). Men Calyx-wrapperns reveal sker aldrig: `.rv` klipper inte, ramen står på wrapperns topp vid `--rv` 0 / 0,25 / 0,5 / 1, wrapperbakgrund synlig 0,1 % i alla fyra (`astra-verify/verify_astra4.json`, `calyx-rv0.png`; Hōrai 99,9 → 31,8 → 13,1 % svart, irisen fungerar; Astra loop 4 fix 2). Plan 043"),
 "H-28": ("[x]", "`#process` efter `.stagger`, före `#principer`, `data-sc-act=\"flow\"`, `--k1..--k7` ur `--sc-ps`; `data-on` av läser shimens `cur` (039)"),
 "H-29": ("[x]", "tolv banor + glyfen, alla namnbara, `pathLength=\"1\"` (oförändrat sedan R6; `preview/preview-1440-process-07.png`)"),
 "H-30": ("[ ]", "1440: `?preview=process-01..07` formade 7 av 7 (`preview/preview_check4.json`: `--sc-ps` = `--eN` ± 0,0001, `on` = 01..N, steg N+1 läcker inte; `preview-1440-process-01..07.png`). 390: 01 och 02 formas i 1 av 3 laddningar, 03 i 2 av 3 (`preview390.json`, `pricefix_ab.json` A): motorns cachade topp för `#process` (6 415) mot den verkliga (6 152) är prisblockets platshållare, inte motorn; med platshållaren bort formas 01 och 02 i 3 av 3 (`pricefix_ab.json` B). Plan 042"),
 "H-31": ("[x]", "prosa v1 orörd, vi-form, noll tankstreck (grep U+2012 till U+2015: 0), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`preview/preview-1440-process-02..07`)"),
 "H-32": ("[ ]", PROBE["H-32"]),
 "H-33": ("[x]", "320 · 768 · 1440 i accent på skärm 03 till 05, `--hair-ink` vid 06 och 07 (`process-1440/v3c-1440-life-04.png` till `-10`, `preview-1440-process-06`, `-07`)"),
 "H-34": ("[ ]", PROBE["H-34"]),
 "H-35": ("[x]", "R9: `reflow.py` 320 + 200 % och åtta extra viewports rena; loop 4 `slices-390/` utan horisontell scroll, `geom4.json scrollW` = 390 / 1440; mailto 44 px hög vid 390"),
}
assert len(rows) == 35
n = 0
for hid, (box, text) in rows.items():
    m = re.search(r"^- \[[ x]\] \*\*%s\*\*" % hid, s, re.M)
    assert m, hid
    s = s[:m.start()] + "- %s **%s**" % (box, hid) + s[m.end():]
    i = s.find("  · loop 3 (", m.start())
    j = s.find("\n", i)
    nxt = s.find("\n- [", m.start())
    assert i > 0 and (nxt < 0 or i < nxt), hid
    s = s[:j+1] + L4 + text + "\n" + s[j+1:]
    n += 1
assert n == 35
pre_anchor = "**Loop 3 (arkitekten, 2026-09-17), R8-läget `70214a22`:**"
assert pre_anchor in s
pre = PROBE["preamble"] + "\n\n"
s = s.replace(pre_anchor, pre + pre_anchor)
P.write_text(s, encoding="utf-8")
x = len(re.findall(r"^- \[x\] \*\*H-", s, re.M)); o = len(re.findall(r"^- \[ \] \*\*H-", s, re.M))
print("ticked", x, "open", o)
