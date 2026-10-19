"""tick_helhet2.py: append a '· loop 2' line after each row's '· loop 1' line in HELHET.md
section 3, flip the checkbox to the loop-2 verdict, rewrite H-07's floor with the
measurement, and update the section preamble."""
import re
from pathlib import Path

P = Path("C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3c/HELHET.md")
s = P.read_text(encoding="utf-8")

L2 = "  · loop 2 (2026-09-17), R7-läget `d30355da`: "
rows = {
 "H-01": ("[ ]", "10 880 px = 12,09 vh vid 1440 (0,09 över radens 12; inom feel-and-fingerprints 8 till 14), 11 521 px = 13,65 vh vid 390; heron 3 060 px = 28 % (`shots/loop-2/diag/diag3.json geom1440`, `slices-1440/`). Ingen plan: 017:s luft är H-05:s golv"),
 "H-02": ("[ ]", "bandet står (Q30 obesvarad); efter heron äger processakten, principerna och avslutet sina skärmar, bandet visar tes + jätterubrik samtidigt (`s03`)"),
 "H-03": ("[ ]", "två helbredds materialbyten (papper vid `#process`, foto vid avslutet); tesen och priset är spaltbreda (`s03`, `s05`). Q30"),
 "H-04": ("[x]", "`.panel-thesis` top 3 222, `.panel-giant` top 3 330: offset 108 px ≥ 96 (`diag3.json geom1440`, `s03`)"),
 "H-05": ("[ ]", "1440: 162 px luft vid alla fem seams (3 060 → 3 222, 3 600 → 3 762, 4 611 → 4 773, 4 266 → 4 428); 390: `gap` 84 px < 96 mellan panelerna (`s390-02`, `s390-03`, Astra loop 2 bild 18/20): plan 032 B"),
 "H-06": ("[x]", "sex anatomier i följd, ingen två gånger i rad (`s03` till `s12`)"),
 "H-07": ("[ ]", "96 px kapar det låsta ordet (`VARUMÄRK` / `E.`, `s03`, `preview-1440-ledger`): spalten är 555 px, ordet 601 px vid 96 px; 88 px vid −0,04em håller ordet helt (542 px, 1 rect, 3 rader vid 1280 och 1440, `diag3.json C_giant`, `synth3`). **Raden skrivs om av arkitekten:** golvet är ≥ 88 px vid 1440 och ordet aldrig delat; 96 px förutsätter en spalt ≥ 606 px, som bara Q30 ger (Q31). Plan 030"),
 "H-08": ("[ ]", "`s03` tes + jätterubrik lika tunga (Q30); `s04`/`s05` kan inte dömas: Calyx och Hōrai renderas som tomma plattor (ramarna vaknar inte, plan 027). Efter 027 läses balansen om"),
 "H-09": ("[x]", "A-glyfen fyller kortets högra halva i hårlinje, 60 % av höjden, ingen kollision med texten (`preview/preview-1440-back.png`, `preview-390-back.png`, `flip-1440/…-11-100.png`)"),
 "H-10": ("[x]", "oförändrat sedan loop 1 (span, fönster och skalparabel orörda); `flip-1440/…-05-045.png`, `flip-06-055.png` visar kortet med full höjd på kant"),
 "H-11": ("[x]", "`.price` `oklch(0.27 0.012 250)` (`diag3.json priceBg`), R7 mätte L-delta 12,16 och 14,54:1; läser som ett plan mot grunden (`s05`, `s390-06`)"),
 "H-12": ("[x]", "`footer.close` 900 px = 100 svh, ensam i sista skivan (`s12`, `s390-13`); mailto-raden 98 px hög, ~86 px teckenstorlek (`diag3.json geom1440 mailto`)"),
 "H-13": ("[ ]", "137 px = 16,3 % död grund under underraden vid 390 (`preview-390-front.png`, `s390-00`): plan 032 A"),
 "H-14": ("[x]", "390: tes 2 870 → Calyx 3 442 → jätterubrik/liggare 4 123 → Hōrai 4 884 → pris 5 531 (`diag3.json geom390`, `s390-03..06`)"),
 "H-15": ("[ ]", "processaktens entré: högerspalten tom tills arket nått in (`process-1440/v3c-1440-life-01.png`), och prosan tonar in (plan 034 B); efter 034 läses entrén om. Principernas 64ch-liggare står som mått, inte som öppen spalt (loop 1)"),
 "H-16": ("[x]", "`probe/scroll-verify-1440.txt`: 0 till 300 (0,0048) = författad tystnad ps 0 till 0,10, 1 800 till 2 100 (0,0043) = landad baksida + dwell; övriga band 0,0104 till 0,0146 över 0,01. 390: 1 686 till 1 967 (0,0) = landad baksida, 10 397 till 10 677 (0,0) = dokumentets sista viewport (maxscroll); övriga ≥ 0,0102"),
 "H-17": ("[x]", "oförändrat (span 3,4, dwell 0,2, fönster 0,10 till 0,78 orörda i R7)"),
 "H-18": ("[x]", "oförändrat, 1 602 px; `flip-1440/` tolv ramar jämn rotation"),
 "H-19": ("[x]", "mätbar: högermarginalens grundpixel (20,20,22) i folden mot (8,23,37) vid tesen, delta 15 (`diag3.json B_summary current-62`). Men hela fotot är blått (rännan (58,86,111) mot gråskalans (80,80,80), chroma 29, leadens R7-fynd): plan 029 sänker tonen till 40 % (delta 13, chroma 19, mätt) så att raden fortfarande håller"),
 "H-20": ("[x]", "R7 D: överhäng 100 px, 5 px före rubrikkanten; `preview/preview-1440-bleed.png`: plåtens högerkant står fri från `VI BYGGER`"),
 "H-21": ("[ ]", "cpu 4, 100:60: hero p95 817 ms ned (97 rutor), 107 ms upp (106); `#process` 480 ms ned, 392 upp; 20:120 hero 54 ms (454 av 1 037). Kontrollen 18,3 till 18,5 ms med 0 till 2 rutor (`probe/probe-log.txt`, maskinen brusig). Profileringen (`shots/loop-2/profile/`): stilomräkning 65 till 76 % av tasktiden; en `--sc-ps`-skrivning kostar 1,8 ms (hero), 2,1 (jätten), 2,2 till 2,6 (arket) i ren subträdsomräkning, shimen tvingar 1,7 till 4,6 omräkningar per frame. Plan 028 (mätt: cpu 1 hero 35,5 → 18,8 ms med batchad shim)"),
 "H-22": ("[ ]", "cpu 1, 100:60: hero ned p95 36,5 ms (31 rutor), upp 19,0 (10); `#process` ned 35,3 (16), upp 18,4 (3); staircase 0 överallt. Plan 028: målvärden hero ≤ 20, bandet ≤ 25, arket ≤ 20"),
 "H-23": ("[ ]", "hero `--sc-ps` max_step 1,41 till 2,04 % (båda riktningarna, båda kadenserna, cpu 1 och 4; R7:s 4,54 % uppåt inte reproducerad: 1,48 % cpu 1 upp), `#process` 0,22 till 1,77 %; `footer.close` mätt separat i loop 2 (`probe/footer-down-100*`), se NOTES § Loop 2. Öppen tills footern ligger under 3 % vid cpu 1"),
 "H-24": ("[ ]", "spårade: `section.hero:--sc-ps`, `.plate-card:transform`, `#process:--sc-ps`, `footer.close:--sc-ps` (inga DEAD); `.giant` scale, `#threadFill`, `.close-rule`, `.thesis-figure` oprobade (proben blind för ren `scale()`, README § Verktyg). Öppen som verktygsskuld"),
 "H-25": ("[ ]", "avslutet har sin linje (`footer` i `s11`/`s12`); priset står stilla (`process-1440/v3c-1440-life-00.png`, `s05`): plan 033; jätterubrikens skala 0,92 → 1 syns inte i tolv ramar (Astra loop 2): oförändrad, rapporteras"),
 "H-26": ("[x]", "grep `prefers-reduced-motion` i `index.html`: 0; alla skivor i loop 2 tagna under `reduced_motion=\"reduce\"` visar allt innehåll"),
 "H-27": ("[ ]", "ramarna transformeras inte, men wrapparnas reveal drivs av motorn ur rått `--sc-p` och reverserar vid scroll uppåt (`scrollcraft.js` rad 947-957; Astra loop 1 fix 8, uppskjuten till loop 2): plan 031 (sidans egen latch på det lerpade värdet)"),
 "H-28": ("[x]", "`#process` efter `.stagger`, före `#principer` och `footer.close`, `data-sc-act=\"flow\"`, `--k1..--k7` ur `--sc-ps` (rad 888-899); prosans reveal-attribut (rad 1230) är en separat defekt, plan 034 B"),
 "H-29": ("[x]", "tolv banor + glyfen, alla namnbara; `pathLength=\"1\"` (oförändrat sedan R6)"),
 "H-30": ("[ ]", "`?preview=process-0N` tappar steg 01: `--s1` mäts från det fastnade sticky-arket och hamnar över `--e1` (0,4847 > 0,2292 vid 1440, 0,4449 > 0,2510 vid 390), konturen och glyfen står med `stroke-dashoffset: 1px` i preview 02 till 07 (`diag/astra1-1440-process-05.png`, `astra1-390-process-05.png`; Astra loop 2 fix 1, verifierad): plan 034 A. Steg N+1 läcker inte längre (R7)"),
 "H-31": ("[x]", "prosa v1 orörd, vi-form, noll tankstreck (grep), talen 320 · 768 · 1440, 16:9, 7 rem, 96 px (`s07` till `s10`)"),
 "H-32": ("[ ]", "cpu 1: `#process` p95 35,3 ms ned mot heron 36,5 (inte längre dyrare); cpu 4: 480 mot 817 (brusigt). Baren är H-21:s; plan 028"),
 "H-33": ("[x]", "320 · 768 · 1440 i accent på skärm 02 till 05, `--hair-ink` vid 07 (`process-1440/…-life-04..11.png`, `preview-1440-process-02..07`)"),
 "H-34": ("[ ]", "hela sidan inte mätt i loop 2 (leadens grind); R7 mätte `.hero-headline` 17,7:1, `.price` 14,54:1, `.frame-cap` 17,77:1, kortet 17,5 till 19,6:1"),
 "H-35": ("[x]", "R7: `reflow.py` 320 + 200 % rent, sju extra viewports rena, träffytor ≥ 44 px (mailto 44 px vid 390/320); loop 2 `slices-390/` utan horisontell scroll. Plan 030 håller ordet i `overflow-wrap`-skyddet"),
}

lines = s.split("\n")
out = []
i = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r"^- \[( |x)\] \*\*(H-\d\d)\*\*", ln)
    if m and m.group(2) in rows:
        state, text = rows[m.group(2)]
        ln = "- " + state + ln[5:]
        if m.group(2) == "H-07":
            ln = ("- [ ] **H-07** Jätterubriken `VI BYGGER ERT VARUMÄRKE.` mäter minst 88 px teckenstorlek vid 1440 (5,5 gånger brödtexten) och det låsta ordet står alltid helt på en rad. "
                  "(Skrevs i fas A som 96 px mot en antagen 640 px-spalt; den faktiska spalten är 555 px och 96 px kapar ordet. 96 px förutsätter Q30:s helbredd, Q31. Hoys kapitelavdelare mäter 100 till 132 px i full bredd.)")
        out.append(ln)
        # copy following continuation lines until next row/blank
        j = i + 1
        while j < len(lines) and lines[j].startswith("  ·"):
            out.append(lines[j]); j += 1
        out.append(L2 + text)
        i = j
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)

pre_old = "**Loop 1 (arkitekten, 2026-09-17), R6-läget `424cdd46`:**"
pre_new = ("**Loop 2 (arkitekten, 2026-09-17), R7-läget `d30355da`:** 18 av 35 bockade, 17 öppna. Varje rad bär en "
           "`· loop 2`-rad med bild eller tal ur `shots/loop-2/`. Öppna rader med plan i R8: H-05 (390, 032 B), H-07 (030), "
           "H-08 (027, sedan Q30), H-13 (032 A), H-15 (034), H-21/H-22/H-32 (028), H-23 (028, footern), H-25 (033), H-27 (031), "
           "H-30 (034). Öppna utan plan: H-01 (0,09 vh över), H-02/H-03 (Q30), H-24 (verktygsskuld), H-34 (leadens grind).\n\n" + pre_old)
assert pre_old in s2
s2 = s2.replace(pre_old, pre_new, 1)
P.write_text(s2, encoding="utf-8")
n2 = s2.count("· loop 2 (2026-09-17)")
print("loop-2 lines:", n2, "ticked:", sum(1 for st, _ in rows.values() if st == "[x]"))
