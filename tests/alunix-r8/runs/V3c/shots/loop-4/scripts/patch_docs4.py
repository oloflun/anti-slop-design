"""patch_docs4.py: README § R10 and BRIEF § Arkitektens rader, loop 4."""
from pathlib import Path
CELL = Path("C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3c")
P = CELL / "plans/README.md"; s = P.read_text(encoding="utf-8")
anchor = "## R9 (helhetsloopen runda 3), i ordning (sju planer; taket är åtta)"
assert anchor in s
new = """## R10 (helhetsloopen runda 4), i ordning (tre planer; taket är åtta)

Skrivna av arkitekten 2026-09-17 mot R9-läget av `runs/V3c/index.html` (md5 `909916d1`);
matchar raderna inte när byggaren öppnar filen, stoppar byggaren. Ordningen är kontraktets:
funktion → states → flöde/hierarki → visuellt → kod. Källor: `HELHET.md` § 3 (loop 4-raderna),
`NOTES.md` § Loop 4, `reviews/loop-4-astra.md` (tre fynd, alla tagna), arkitektens egna
mätningar i `shots/loop-4/`.

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 042 | Prisblockets platshållare (760 px mot 463) krymper sidan 297 px vid första målningen; motorns akttoppar under bandet står kvar fel; 390-previews ett race | HIGH | 1, funktion | arkitektens C1 = Astra loop 4 fix 1; `shots/loop-4/mountshift.json`, `shiftprobe*.json`, `preview390*.json`, `pricefix_ab.json`, `probe/ab/price-*`, `giant-*`; `process-1440/v3c-1440-life-01.png` |
| 043 | Calyx-revealen har ingen öppning: `.rv` klipper inte, ramen står hel vid varje `--rv` | HIGH | 2, funktion / states | Astra loop 4 fix 2; `shots/loop-4/astra-verify/verify_astra4.json`, `calyx-rv0.png` |
| 044 | Driftens överlämning tes → jätte hoppar blå → papper i en bildruta vid 3 600 | MEDIUM | 3, visuellt | Astra loop 4 fix 3; `astra-verify/verify_astra4.json`, `drift-3580.png`, `drift-3620.png` |

042 först: H-15, H-30 och bildtiden i bandet mäts mot den konstanta dokumenthöjden, och 043:s
Calyx-fönster ligger i samma band. 043 mäts före och efter i Calyx-fönstret (2 862 + 20 ticks)
med tre körningar och median, som 036. 044 är oberoende och en fyraradersändring.

**Utanför R10:** Q30/Q31 (bandets omkomposition och 96 px; H-02/H-03/H-08 s03, väntar på
Anton), H-21/H-22/H-32 (bildtiden vid cpu 4 och i bandet: arkitektoniskt golv redovisat i
NOTES § Loop 4, pinnen ensam 18,4 ms; det som är kvar i filen är 042), H-23 (3,12 / 3,52 % i
fönster där ramarna monteras; mäts om efter 042), H-24 (verktygsskuld: `.rv:transform` läses
DEAD för ren `scale()`), H-34 (leadens grind; folden 7/7 mätt), jättens skala 0,92 → 1,
sidvikten (476 kB), a11y-skulden, `sites/calyx.html`:s nav vid 390 (referenssajten).

**Verktygsfynd loop 4:** `frames.py life` och `slices4.py` laddar vid scrollY 0 och hoppar,
så prisblocket målas först när fönstret passerar det: alla fångster efter 5 340 (1440) står
på den krympta sidan medan motorns toppar står på den ursprungliga; kickern i `s06` vid y 18
i stället för 237 är den skillnaden, inte en ny geometri. `motion_probe.py --start` scrollar
direkt till startpositionen, så ett fönster med start ≥ 1 920 får 036 B:s montering i sin
första bildruta (tesfönstret 142 ms); 036:s mätningar förmonterade av det skälet.
`.horai-wrap .rv:transform` läses DEAD (ren `scale()`, atan2-blindheten, README § Verktyg);
`.horai-wrap:--rv` spåras i stället.

"""
s = s.replace(anchor, new + anchor)
P.write_text(s, encoding="utf-8"); print("README ok")
B = CELL / "BRIEF.md"; b = B.read_text(encoding="utf-8")
anchor2 = "## Direction contract"
assert anchor2 in b
rows = """### Arkitektens rader, helhetsloopen runda 4 (2026-09-17)

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Prisblockets platshållare** | `content-visibility:auto; contain-intrinsic-size:auto 760px` bort från `.price` (plan 042): dokumenthöjden konstant från load, motorns akttoppar = DOM:ens utan resize | `shots/loop-4/mountshift.json` (docH 10 880 → 10 582, `#process` 5 637 → 5 340 vid första målningen; motorn kvar på 5 637), `pricefix_ab.json` (390-previews 01/02: 1 av 3 → 3 av 3), `probe/ab/` (pris 53,0 → 35,3, jätte 94,1 → 81,7 ms median) | gate 93 (CLS), H-30, H-15; performance.md: en platshållare som inte matchar innehållet är ett skifte, inte ett skydd | R9:s "motorbunden gräns" (037) var sidans egen: platshållaren är 297 px högre än blocket; Astra loop 4 fix 1, funnen oberoende av arkitekten (C1) |
| **Calyx-öppningen** | `.calyx-wrap .rv{overflow:clip}` och riktningen uppifrån (`translateY((rv − 1)·100%)` på `.rv`, `(1 − rv)·100%` på ramen) (plan 043) | `shots/loop-4/astra-verify/verify_astra4.json`: ramens top 40 px vid `--rv` 0 / 0,25 / 0,5 / 1, wrapperbakgrund 0,1 % synlig i alla fyra; `calyx-rv0.png` | PRODUCT.md: reveal en gång på wrappern; F-002: målet tyst i vila och tänds vid scroll; 036:s egen regel (innehållet pixelstilla, identitet vid 1) | Astra loop 4 fix 2: 036 A:s Calyx-halva var en no-op (wrapperns klipp sitter på den stillastående boxen); loop 3:s A/B mätte samma no-op |
| **Driftens överlämning** | leg 2 räknas från överlämningen: `k = smooth((g − gH) / 0,35)` med `gH` = jättens råa progress när tesen når 1, mätt i `measureAct` (plan 044) | `astra-verify/verify_astra4.json`: `--sc-canvas` rgb(18,63,104) vid 3 600, rgb(244,242,238) vid 3 620; träet chroma 21 → 2 | gate 94 (kontinuitet), H-19 (kallt ljus utan klipp); TASTE § 4.5 (materialbyte, inte hopp) | Astra loop 4 fix 3; motorns egen loop gjorde samma hopp i R7/R8, 041 ärvde kurvan |
| **Bildtiden, golvet** | H-21/H-22/H-32 redovisas som arkitektoniskt golv utanför cellen (de två levande ramarnas montering och målning, motorns läsning) med talen; det som är kvar i filen är 042 | `probe/ab/hero-pin18-*` (pinnen ensam 18,4 ms = kontrollen, tre körningar), `hero-mount-*` (förmonterad 89,4), `hero-pricefix-*` (64,7); loop 2:s profilering | F-013 regel 2: mät före ändring; gate 93 | Herofönstrets försämring mot R8 (36 → 78 ms) är 036 B:s tidigare montering i fönstret, inte 035:s sampler |
| **H-23 återöppnad** | `--sc-ps` max_step 3,12 % (jätten) och 3,52 % (tesfönstret) vid cpu 1 i fönster där ramarna monteras och sidan lägger om 297 px; mäts om efter 042, ingen egen plan | `probe/giant-down-100-cpu1/`, `thesis-down-100-cpu1/`, `probe/ab/giant-fix-*` (2,86 till 3,13) | gate 94 punkt 2 | loop 2: korta flow-akter stegar när bildtiden faller |
| **Skivfångsten** | plain `scrollTo` med 3 s väntan är loopens skivfångst från loop 4 (035 byggd: `--rv` 1 / 1 i alla skivor); `slices_fix.py` pensioneras | `shots/loop-4/capture-log.txt` (`rv calyx=1 horai=1` från s04/s06) | Verktyget mäter den väg sidan täcker | K5 stängd |
"""
b = b.replace(anchor2, rows + anchor2)
B.write_text(b, encoding="utf-8"); print("BRIEF ok")
