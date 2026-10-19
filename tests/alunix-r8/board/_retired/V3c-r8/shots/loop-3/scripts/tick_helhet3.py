"""tick_helhet3.py: HELHET.md § 3 loop-3 pass. Flip each row's checkbox to the loop-3
verdict, append a '· loop 3' line after the row's '· loop 2' line, rewrite H-01, H-05 (a)
and H-19 with the measured reason, and add the loop-3 preamble."""
import re
from pathlib import Path

P = Path("C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3c/HELHET.md")
s = P.read_text(encoding="utf-8")
L3 = "  · loop 3 (2026-09-17), R8-läget `70214a22`: "
rows = {
 "H-01": ("[x]", "10 880 px = 12,09 vh vid 1440, 11 588 px = 13,73 vh vid 390 (`shots/loop-3/geom3.json`); heron 3 060 px = 28 %. **Raden omskriven** till kedjans budget 8 till 14 (`feel-and-fingerprint.md` § Pacing), som fas A citerade som 8 till 12 utan källa; bockad"),
 "H-02": ("[ ]", "bandet står (Q30); process, principer och avslut äger sina skärmar (`slices-1440/v3c-1440--s06.png` till `s12`); tes + jätterubrik samtidigt (`s03`)"),
 "H-03": ("[ ]", "två helbredds materialbyten (papper vid `#process` `s06`, foto vid avslutet `s11`/`s12`); tesen och priset spaltbreda. Q30"),
 "H-04": ("[x]", "`.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px (`geom3.json`, `slices-1440-fix/v3c-1440--s03.png`)"),
 "H-05": ("[x]", "1440: 162 px vid alla seams (3 060 → 3 222, 3 600 → 3 762, 4 150 → 4 312, 4 611 → 4 773; `geom3.json`); 390: 101 till 102 px (3 358 → 3 459, 4 055 → 4 157, 4 834 → 4 935, 5 497 → 5 599) och pris → papper är ett helbrett materialbyte (`slices-390-fix/v3c-390--s03.png` till `s07`). **(a) preciserad**: ≥ 160 px vid 1440, ≥ 96 px vid 390 (plan 032 B, loop 2)"),
 "H-06": ("[x]", "sex anatomier i följd, ingen två gånger i rad (`slices-1440-fix/…s03` till `slices-1440/…s12`)"),
 "H-07": ("[x]", "`.giant` 88 px, −3,52 px tracking, ordet 1 rect, 3 rader vid 1440; 33,6 px, 2 rader vid 390 (`geom3.json`, `preview/preview-1440-ledger.png`, `slices-390-fix/v3c-390--s05.png`)"),
 "H-08": ("[ ]", "`s03` tes + jätterubrik lika tunga (Q30); `slices-1440-fix/v3c-1440--s04.png`: Calyx dominerar liggaren; `s05`: Hōrai dominerar priset (Astra loop 3 bild 29, 30 överens). Öppen bara för s03"),
 "H-09": ("[x]", "`preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/v3c-1440-flip-11-100.png`: glyfen fyller kortets högra halva"),
 "H-10": ("[x]", "`flip-1440/v3c-1440-flip-05-045.png`, `-06-055.png`, `flip-390/…-05-045.png`: kortet med full höjd på kant, 4 px kant"),
 "H-11": ("[x]", "`slices-1440-fix/v3c-1440--s05.png`, `slices-390-fix/v3c-390--s06.png`: grafitplanet läser som material mot fotot"),
 "H-12": ("[x]", "`footer.close` 900 px = 100 svh, ensam i `slices-1440/v3c-1440--s12.png`; 844 px vid 390 (`s13`); mailto 98 px hög vid 1440 (`geom3.json`)"),
 "H-13": ("[x]", "R8 mätte 10,0 % (84 px) vid 390x844; `slices-390/v3c-390--s00.png`, `preview/preview-390-front.png`: ~85 px grund under underraden"),
 "H-14": ("[x]", "390: tes 2 870 → Calyx 3 459 → jätterubrik 4 157 → Hōrai 4 935 → pris 5 599 (`geom3.json`, `slices-390-fix/…s03` till `s07`)"),
 "H-15": ("[ ]", "prosan synlig från entrén (034 B, `process-1440/v3c-1440-life-01.png`), men entréskärmens högerspalt bär bara ett hörn av ramen tills konturen är hel (`slices-1440/v3c-1440--s06.png`, `process-390/v3c-390-life-01.png`; Astra loop 3 fix 6): plan 040"),
 "H-16": ("[x]", "`probe/scroll-verify-1440.txt`: 0 till 300 (0,0046) författad tystnad, 1 800 till 2 100 (0,0028) landad baksida + dwell, 1 500 till 1 800 (0,008) kortet på kant mot mörk grund (verktygsblindhet; `flip-1440/…-05`, `-06` visar rotationen), övriga 0,0107 till 0,0146; 390: 0 till 281 (0,0093) författad, 1 686 till 1 967 (0,0) landad baksida, 1 405 till 1 686 (0,0148)"),
 "H-17": ("[x]", "oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R8)"),
 "H-18": ("[x]", "oförändrat, 1 602 px; `flip-1440/` tolv ramar jämn rotation"),
 "H-19": ("[ ]", "44 % ger chroma 38 på träpanelen ((112,132,150) mot gråskalans (128,128,128)): tvätt (`drift2/d44-thesis.png`, `slices-1440/v3c-1440--s03.png`); 24 % ger chroma 21 (`drift2/d24-thesis.png`): kallt ljus; folden neutral vid alla styrkor (`drift2/drift2.json`). **Raden omskriven** på mellantonen (leadens R8-fynd 2); plan 038"),
 "H-20": ("[x]", "`preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`"),
 "H-21": ("[ ]", "cpu 4, 100:60: hero p95 89,5 ms ned (88 rutor), 54,0 upp (81); `#process` 285 ned (143), 461 upp (117); 20:120 hero 53,2 / 36,5, process 88,5 / 88,4. Kontrollen 18,2 till 18,5 ms med 0 till 2 rutor i varje körning (`probe/probe-log.txt`). Orsak mätt i `probe/ab/`: klippningen över en levande ram, plan 036"),
 "H-22": ("[ ]", "cpu 1, 100:60: hero ned 36,1 (19 rutor), upp 18,4 (5); `#process` ned 32,1 (14), upp 18,5 (4); `#giant-section` 128 (22); `.price`-fönstret 143,7 (16). A/B med ramarna förmonterade (`probe/ab/r3-*`, tre körningar): clip-path över levande Hōrai 101 till 187 ms, `mask-image` 65 till 72, ingen klippning 35 till 62. Plan 036"),
 "H-23": ("[x]", "`--sc-ps` max_step vid cpu 1: hero 1,41 ned / 1,38 upp, `#process` 0,78 / 1,42, `#giant-section` 2,82, `.price` 2,25, `footer.close` 2,74 (`probe/*/motion_probe.json`); R8:s 4,61 % uppåt inte reproducerad (1,38). cpu 4: hero 1,65 / 1,85, process 0,99 / 1,71"),
 "H-24": ("[ ]", "spårade: hero, `.plate-card`, `#process`, `#giant-section`, `.price`, `footer.close` (inga DEAD); `.giant` scale, `#threadFill`, `.close-rule`, `.thesis-figure`, `.horai-wrap:clip-path` oprobade. Verktygsskuld"),
 "H-25": ("[x]", "priset: tredje radens linje mitt i dragningen i `slices-1440-fix/v3c-1440--s05.png` mot hel i `process-1440/…life-00`; avslutets linje `s11`/`s12`; Calyx inset och Hōrai iris (`slices-1440-fix/`); jättens skala 0,92 → 1 oläsbar i tolv ramar (Astra loop 2 och 3): redundant mot ordscrubben på samma skärm, rapporteras, ingen plan"),
 "H-26": ("[x]", "grep `prefers-reduced-motion` 0; alla skivor tagna under `reduced_motion=\"reduce\"` visar allt innehåll"),
 "H-27": ("[ ]", "latchen backar aldrig men når inte 1 för PageDown (0,21), `scrollTo` (0) eller scrollbar (`latch_diag.json`; leadens R8-fynd 1): samplas bara vid scroll-händelser. Plan 035"),
 "H-28": ("[x]", "`#process` efter `.stagger`, före `#principer`, `data-sc-act=\"flow\"`, `--k1..--k7` ur `--sc-ps`; `data-on`:s av-villkor läser rå pps (Astra loop 3 fix 2, plan 039), raden håller i sak"),
 "H-29": ("[x]", "tolv banor + glyfen, alla namnbara (`preview_check.json` ids), `pathLength=\"1\"`"),
 "H-30": ("[ ]", "`?preview=process-02` vid 1440: `--k2` 0,19, `#p-dim-width` oritad; `process-01` vid 390: `--k1` 0,67, `#p-glyph` 0,59 (`preview_check.json`; Astra loop 3 bild 42/43/54/55): målscrollen räknas en gång före typsnitten, plan 037"),
 "H-31": ("[x]", "prosa v1 orörd, vi-form, noll tankstreck (grep), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`preview/preview-1440-process-02..07`)"),
 "H-32": ("[ ]", "cpu 1: `#process` 32,1 ned mot heron 36,1 (inte dyrare); cpu 4: 285 mot 89: akten kostar mer under strypning. Baren är H-21:s"),
 "H-33": ("[x]", "320 · 768 · 1440 i accent på skärm 03 till 05, `--hair-ink` vid 07 (`process-1440/v3c-1440-life-04.png` till `-11`)"),
 "H-34": ("[ ]", "hela sidan inte mätt i loop 3 (leadens grind); R8 mätte `.hero-headline` 17,71:1, `.hero-sub` 17,81:1, `.ledger-body p` 5,08:1 dämpat"),
 "H-35": ("[x]", "R8: `reflow.py` 320 + 200 % och åtta extra viewports rena; loop 3 `slices-390/` utan horisontell scroll; `geom3.json` mailto 44 px vid 390"),
}
assert len(rows) == 35

# row rewrites
old01 = "**H-01** Dokumenthöjden vid 1440 är 8 till 12 vh, och ingen enskild akt tar mer än 45 % av dokumenthöjden."
new01 = "**H-01** Dokumenthöjden vid 1440 är 8 till 14 vh (kedjans budget, `scroll/feel-and-fingerprint.md` § Pacing; fas A skrev 12 utan källa, omskriven i loop 3), och ingen enskild akt tar mer än 45 % av dokumenthöjden."
assert old01 in s; s = s.replace(old01, new01)
old05 = "(a) kontinuerlig grund med minst 160 px luft,"
new05 = "(a) kontinuerlig grund med minst 160 px luft vid 1440 och minst 96 px vid 390 (plan 032 B, preciserad i loop 3),"
assert old05 in s; s = s.replace(old05, new05)
old19 = "**H-19** Grunddriften är mätbar: en grundpixel utanför panelerna skiljer minst 12 RGB-steg mellan heron (`#0b0c0e`) och tesbandet (`#123f68`-stoppet). (I dag är driften inte synlig i skivorna `v3c-1440--s04`, `s05`.)"
new19 = "**H-19** Grunddriften är ett kallt ljus, inte en tvätt, mätt på en mellantonspixel i grunden (träpanelen, gråskala L 110 till 140, t.ex. (720,180) vid 1440 med tesen centrerad): chroma (max − min) 12 till 24 vid tesbandet och ≤ 2 i folden. (Fas A:s golv, 12 RGB-steg på en nästan svart marginalpixel, var fel mätpunkt: `mix-blend-mode:color` skalar kulören med luminansen, så golvet tvingade en tvätt på mellantonerna; omskriven i loop 3 på leadens R8-fynd 2.)"
assert old19 in s; s = s.replace(old19, new19)

n = 0
for hid, (box, text) in rows.items():
    m = re.search(r"^- \[[ x]\] \*\*%s\*\*" % hid, s, re.M)
    assert m, hid
    s = s[:m.start()] + "- %s **%s**" % (box, hid) + s[m.end():]
    # the row's loop-2 line: first '  · loop 2' after the row start
    i = s.find("  · loop 2 (", m.start())
    j = s.find("\n", i)
    nxt = s.find("\n- [", m.start())
    assert i > 0 and (nxt < 0 or i < nxt), hid
    s = s[:j+1] + L3 + text + "\n" + s[j+1:]
    n += 1
assert n == 35

pre_anchor = "**Loop 2 (arkitekten, 2026-09-17), R7-läget `d30355da`:**"
assert pre_anchor in s
pre = ("**Loop 3 (arkitekten, 2026-09-17), R8-läget `70214a22`:** 23 av 35 bockade, 12 öppna. Varje rad bär en `· loop 3`-rad med bild eller tal ur `shots/loop-3/`. Öppna rader med plan i R9: H-15 (040), H-19 (038), H-21/H-22/H-32 (036, 041), H-27 (035), H-30 (037). Öppna utan plan: H-02/H-03/H-08 (Q30), H-24 (verktygsskuld), H-34 (leadens grind). Omskrivna rader i loop 3, med skäl i raden: H-01 (kedjans budget 8 till 14 med källa), H-05 (a) (390-golvet 96 px), H-19 (mellantonen i stället för svärtan).\n\n")
s = s.replace(pre_anchor, pre + pre_anchor)
P.write_text(s, encoding="utf-8")
x = len(re.findall(r"^- \[x\] \*\*H-", s, re.M)); o = len(re.findall(r"^- \[ \] \*\*H-", s, re.M))
print("ticked", x, "open", o)
