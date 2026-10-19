
## Loop 4 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 4 av max 6

Kontrakt: `tests/alunix-r8/PROMPT-LOOP-V3c.md`, N = 4, RN = 10. Mål: R9-läget av
`runs/V3c/index.html` (md5 `909916d1`) på port 3090 (leadens angivelse; 4626 speglar).
`Skill(design)` anropad som första handling. Fångst i `shots/loop-4/`, allt vid 1440x900 och
390x844 med installerad Chrome, `reduced_motion="reduce"` (F-011), skivor med plain
`scrollTo` och 3 s väntan (035 byggd: ingen injicerad sampler), previews med
`wait_until="load"` + 2 s. Skript (kopierade till `shots/loop-4/scripts/`): `cap_loop4.sh`,
`slices4.py`, `previews4.py`, `geom4.py`, `frames.py`, `probes4.sh`, `motion_probe_dir.py`,
`motion_probe_ab.py`, `latch4.py`, `preview390.py`, `preview390b.py`, `mountshift.py`,
`shiftprobe.py`, `shiftprobe2.py`, `pricefix_ab.py`, `verify_astra4.py`,
`build_astra_prompt4.py`, `run_astra4.sh`, `tick_helhet4.py`, `patch_docs4.py`. Astra:
`shots/loop-4/astra/`. Rundan avbröts en gång av användningsgränsen efter att proben
startats i bakgrunden; proben hade gått klart (`probe/probe-log.txt` PROBES-DONE), inget
kördes om, md5 oförändrad, servrarna omstartade av lead.

### Steg 1, fångat och läst

Dokumenthöjd 10 880 px = 12,09 vh vid 1440 vid load, 10 582 px = 11,76 vh när prisblocket
målats; 11 588 / 11 326 px = 13,73 / 13,42 vh vid 390 (`geom4.json`, `mountshift.json`).

Läst som pixlar med `Read` (105 bilder):

- läst: `slices-1440/v3c-1440--s00.png` till `v3c-1440--s12.png` (13)
- läst: `slices-390/v3c-390--s00.png` till `v3c-390--s13.png` (14)
- läst: `preview/preview-1440-front|mid|back|ledger|bleed|process-01..07.png`, `preview-390-…` (24)
- läst: `flip-1440/v3c-1440-flip-00-000.png` till `v3c-1440-flip-11-100.png` (12)
- läst: `flip-390/v3c-390-flip-00-000.png` till `v3c-390-flip-11-100.png` (12)
- läst: `process-1440/v3c-1440-life-00.png` till `v3c-1440-life-11.png` (12)
- läst: `process-390/v3c-390-life-00.png` till `v3c-390-life-11.png` (12)
- läst: `astra-verify/calyx-rv0.png` (1); inte lästa som pixlar: `astra-verify/calyx-rv0.25|0.5|1.png`, `horai-rv*.png`, `drift-3580|3620.png` (talen i `verify_astra4.json`), `probe/*/frame-times.png`, `track-*.png`, `probe/sv-*/` (kontaktark)

**Geometri (`geom4.json`, `mountshift.json`):** 1440: hero 0 till 3 060 (28 %), `.panel-thesis`
3 222 + 378, `.panel-giant` 3 330 + 820 (offset 108), `.calyx-fig` 3 762 + 849, `.horai-fig`
4 312 + 1 325 (sträckt av `.price`), `.price` 4 773 + 864 (platshållare; 567 efter första
målningen), `#process` 5 637 + 3 796 (5 340 efter), `#principer` 9 433, `footer.close` 9 980 +
900; seams 162 px vid alla fyra; `.giant` 88 px, −3,52 px, ordet 1 rect, 3 rader; mailto 98 px
hög, 86,4 px; grunden vid tesen centrerad: träpanelen (720,180) (119,130,140) chroma 21,
`--sc-canvas` rgb(18,63,104); folden chroma 0. 390: tes 2 870 → Calyx 3 459 → jätterubrik
4 157 → Hōrai 4 935 → pris 5 599 → process 6 415 (6 152 efter); seams 101 till 102 px; `.giant`
33,6 px, 2 rader; folden 84 px = 10,0 % död grund; mailto 44 px.

**Latchen (`latch4.json`):** hjul, PageDown, `scrollTo`, smooth `scrollTo` till 4 703: `--rv`
1 / 1; resize 1440 → 1280 före bandet, sedan hjul: 1 / 1; 0 skrivningar tre sekunder efter
landning. Skivorna: `rv calyx=1 horai=1` från s04/s06 (`capture-log.txt`), ramarna hela.

**Previews (`preview/preview_check4.json`):** 1440 process-01..07 formade 7 av 7 (`--sc-ps` =
`--eN` ± 0,0001, `data-on` 01..N). 390: 01 (ps 0,1894 mot `--e1` 0,2450) och 02 (0,2753 mot
0,3311) inte formade i fångsten; tre laddningar var (`preview390.json`): 01 formad 1 av 3, 02
1 av 3, 03 2 av 3.

**Loop 4:s huvudfynd, C1 (rotorsakat före Astra):** `.price{content-visibility:auto;
contain-intrinsic-size:auto 760px}` (rad 731) reserverar 760 px mot blockets 463 px vid 1440
(450 vid 390). Så länge blocket inte målats är `.price` 864 px, `.horai-fig` (`flex:1`) sträcks
till 1 325, bandet 2 577; när blocket når viewporten krymper allt 297 px (`.price` 567,
`.horai-wrap` 989, `.stagger` 2 280, `#process` 5 340, dokumentet 10 582), 262 px vid 390.
`shiftprobe.json` isolerar orsaken: ingen ändring vid montering, `is-asleep`,
`content-visibility:visible` på ramarna; bara när `.price` själv målas. Följder: (1)
layoutskifte i viewporten; (2) motorns `layout()` mäts vid load och resize, så `#process`,
`#principer` och `footer.close` räknar `--sc-p` ur toppar 297 px för höga tills ett riktigt
resize (`mountshift.json`: motorn 0,0134 mot sant 0,0767 vid scrollY 4 800; vid 390 rättar
inte ens ett syntetiskt resize, `scrollcraft.js` rad 1186); (3) 390-previews är ett race
mellan `aimOnce` och blockets första målning. A/B (`pricefix_ab.json`, platshållaren
neutraliserad efter load): docH 10 582 från load, motorns topp = DOM:ens, 390-previews 01/02
formade 6 av 6. R9:s "motorbunden gräns" (037) var sidans egen platshållare. Plan 042.

**`motion_probe.py`** (scratchkopia med `--start`, kontrollprotokollet; kontrollen gav 0 till
2 rutor > 33 ms i alla sju körningar, 18,2 till 18,4 ms p95):

| Körning | cpu | hjul | riktning | spår | p95 ms | > 33 ms | max_step `--sc-ps` | staircase |
|---|---|---|---|---|---|---|---|---|
| hero-down-100 | 4 | 100:60 | ned | hero | 333,8 | 96 | 1,72 % | 0 |
| hero-up-100 | 4 | 100:60 | upp | hero | 79,7 | 91 | 1,86 % | 0 |
| hero-down-20 | 4 | 20:120 | ned | hero | 53,0 | 459 | 0,36 % | 0 |
| hero-up-20 | 4 | 20:120 | upp | hero | 52,7 | 438 | 0,58 % | 0 |
| proc-down-100 | 4 | 100:60 | ned | `#process` | 326,9 | 138 | 1,10 % | 0 |
| proc-up-100 | 4 | 100:60 | upp | `#process` | 474,6 | 131 | 1,06 % | 0 |
| proc-down-20 | 4 | 20:120 | ned | `#process` | 86,0 | 837 | 0,20 % | 0 |
| proc-up-20 | 4 | 20:120 | upp | `#process` | 215,7 | 793 | 0,24 % | 0 |
| giant-down-100 (2 700 + 28) | 4 | 100:60 | ned | `#giant-section` | 462,0 | 88 | 3,36 % | 0 |
| price-down-100 (3 873 + 18) | 4 | 100:60 | ned | `.price` | 875,9 | 62 | 2,84 % | 0 |
| hero-down-100-cpu1 (tre körningar) | 1 | 100:60 | ned | hero | 53,6 / 78,2 / 82,2 | 35 / 38 / 41 | 1,38 till 1,55 % | 0 |
| hero-up-100-cpu1 | 1 | 100:60 | upp | hero | 35,4 | 19 | 1,37 % | 0 |
| proc-down-100-cpu1 | 1 | 100:60 | ned | `#process` | 18,2 | 7 | 0,70 % | 0 |
| proc-up-100-cpu1 | 1 | 100:60 | upp | `#process` | 18,2 | 3 | 0,70 % | 0 |
| giant-down-100-cpu1 | 1 | 100:60 | ned | `#giant-section` | 101,6 | 28 | **3,12 %** | 0 |
| price-down-100-cpu1 | 1 | 100:60 | ned | `.price` | 40,4 | 12 | 1,78 % | 0 |
| thesis-down-100-cpu1 (2 322 + 18; ramarna monteras i fönstrets första bildruta) | 1 | 100:60 | ned | `.panel-thesis` | 142,4 | 33 | **3,52 %** | 0 |
| footer-down-100-cpu1 (8 500 + 18) | 1 | 100:60 | ned | `footer.close` | 18,3 | 1 | 2,70 % | 0 |
| horai-rv-cpu1 (3 873 + 24) | 1 | 100:60 | ned | `.horai-wrap:--rv` / `.rv:transform` | 35,5 | 13 | 5,41 % (härledd, rapporteras) / DEAD (ren `scale()`, probens blindhet) | 0 |
| kontroll (sju körningar) | 4 / 1 | 100:60 | ned | `#act:--sc-ps` / `#card:transform` | 18,2 till 18,4 | 0 till 2 | 1,26 till 1,51 % | 0 |

Läsning mot R8 (loop 3): heron nedåt cpu 1 36,1 → 78,2 (median), uppåt 18,4 → 35,4;
`#process` 32,1 → 18,2 / 18,5 → 18,2; jätten 128 → 101,6; priset 143,7 → 40,4 (036:s mål ≤ 50
nått). Staircase 0 i alla körningar, båda riktningarna, båda kadenserna.

**Dekomposition av herofönstret** (`probe/ab/hero-*`, cpu 1, 100:60, tre körningar, median):
pinnen ensam (18 ticks, 0 till 1 800, före monteringen vid hero cur 0,80 ≈ 1 920) **18,4 /
18,4 / 18,4 ms** med 2 till 4 rutor: kontrollens nivå. 40 ticks som byggd 78,2; förmonterad 5 s
före hjulet 89,4; förmonterad + platshållaren neutraliserad 102,6; platshållaren neutraliserad
64,7. Slutsats: latchTick per bildruta kostar inget mätbart i pinnen; herofönstrets kostnad
ligger i 1 800 till 4 000 (de två levande ramarna monteras, laddar och målar sina sidor,
bandet kommer in), och försämringen mot R8 är 036 B (monteringen flyttad från 2 860 till
1 920, in i fönstret). Förmontering flyttar inte kostnaden bort: sajterna renderar ändå.
Arkitektoniskt golv utanför cellen (ramarnas egen målning, motorns läsning), redovisat med
talen i HELHET H-21/H-22/H-32.

**A/B prisplatshållaren** (`probe/ab/price-*`, `giant-*`, cpu 1, tre körningar): prisfönstret
som byggd 35,7 / 53,0 / 53,4 (median 53,0) mot neutraliserad 35,2 / 35,3 / 35,6 (35,3);
jättefönstret 98,4 / 94,1 / 88,5 (94,1) mot 81,7 / 70,9 / 106,6 (81,7). Omlayouten på 297 px
sker annars mitt i fönstret.

**`scroll_verify.py`** (`probe/scroll-verify-1440.txt`, `-390.txt`): 1440 deadScroll 0 till 300
(0,0052) författad, 600 till 900 (0,0088) kortet på kant (verktygsblindhet), 1 800 till 2 100
(0,0005) landad baksida + dwell, 1 500 till 1 800 (0,0124), 5 700 till 6 000, 6 600 till 7 200,
8 100 till 8 400 (0,0115 till 0,0147); `cuesNeverFull`, `unrevealed`, `contrastUnderMedia`
tomma; blankBands 900 till 3 222 (pinnen). 390: 0 till 281 (0,0055), 1 124 till 1 405 (0,008),
1 686 till 1 967 (0,0); blankBands pinnen, 3 330 till 4 031 (Calyx), 4 803 till 5 473 (Hōrai),
5 484 till 6 221 (priset), 6 403 till 6 919 (processentrén), 10 398 till 10 910 (avslutets foto):
64x36-nedskalningen av hela ramar och platta plan; `slices-390/…s04`, `s06` visar ramarna hela.

**Kontrast (arkitektens egen läsning, H-34 är leadens grind):** `contrast_over_media.py --url`
folden 1440: 7 av 7 godkända, sämsta 16,20:1 (`a.topline-contact`), hero-rubriken 17,71:1,
underraden 17,82:1, kortets fyra strängar 18,79 till 21,00:1.

**Grep:** `prefers-reduced-motion` 0; U+2012 till U+2015 i synlig text 0; `data-sc-drift=` 0
attribut (en kommentarträff, rad 1568); `clip-path` 0 på ramwrapparna; sidan 135 795 B egen
vikt (R9:s `perf_probe` 476 kB inkl. resurser); låst copy 15/15 (10 distinkta strängar,
räkningar identiska med R8: 1, 1, 1, 4, 5, 2, 1, 1, 1, 2).

### Steg 3, egna fynd ur pixlarna och talen (före Astra)

| # | Fynd | Bild / tal | Dom | Plan |
|---|---|---|---|---|
| C1 | Prisblockets platshållare 297 / 262 px högre än blocket: layoutskifte, motorns toppar stale, 390-previews ett race | `mountshift.json`, `shiftprobe*.json`, `preview390*.json`, `pricefix_ab.json`; `slices-1440/…s06` (kickern vid y 18, inte 237) | rotorsakat; R9:s "motorbunden gräns" var sidans | 042 |
| C2 | Herofönstrets bildtid 36 → 78 ms mot R8 är 036 B:s montering i fönstret, inte latchen: pinnen ensam 18,4 | `probe/ab/hero-pin18-*`, `hero-mount-*` | golv redovisat | ingen |
| C3 | `--sc-ps` max_step 3,12 % (jätten) och 3,52 % (tesfönstret) vid cpu 1 | `probe/giant-down-100-cpu1/`, `thesis-down-100-cpu1/` | H-23 återöppnad, bildtidens följd | mäts efter 042 |
| C4 | Ramarna hela i alla plain `scrollTo`-skivor; latchen 1 / 1 på fyra scrollsätt + resize | `capture-log.txt`, `latch4.json`, `slices-1440/…s04`, `s05` | 035 håller; H-27:s latchdel bockad | ingen |
| C5 | Hōrais iris genuint cirkulär, tallriken stilla; `--rv` 0,9487 i `s05` är rätt värde för aktens 0,49 | `slices-1440/…s05`, `verify_astra4.json` horai | 036 A Hōrai håller | ingen |
| C6 | Processentrén: konturen hel och glyfen påbörjad i `s06` och `life-02`; `life-01` tom högerspalt | `slices-1440/…s06`, `process-1440/…life-01`, `-02` | 040 håller där motorn stämmer; `life-01` är C1 | 042 |
| C7 | Previews 1440 7 av 7 formade, steg N+1 läcker inte; 390 01/02/03 intermittenta | `preview_check4.json`, `preview390.json` | 037 håller vid 1440; 390 är C1 | 042 |
| C8 | Grunden vid tesen kallt ljus (chroma 21), folden neutral | `geom4.json`, `slices-1440/…s03` | 038/041 håller | ingen |
| C9 | Kortvändningen kontinuerlig i tolv ramar vid båda bredderna, kanten 4 px, baksidans glyf | `flip-1440/`, `flip-390/` | H-09, H-10, H-18 står | ingen |
| C10 | Arket kumulativt 01 till 07, måtten i accent, revisionsfältet vid 07 | `process-1440/…life-03..11`, `process-390/…life-03..10`, previews 02..07 | H-29, H-31, H-33 står | ingen |
| C11 | Avslutet ensamt, linjen dragen; principerna i rail; papper → foto helbrett | `slices-1440/…s11`, `s12`, `slices-390/…s12`, `s13` | H-12 står | ingen |
| C12 | Seams 162 / 101 px, offset 108, 88 px helt ord, folden 10 % | `geom4.json`, `slices-390/…s00`, `s05` | H-04, H-05, H-07, H-13 står | ingen |

Squint 5 px per 1440-skärm: s00 rubriken ok; s01 kortet på kant ok; s02 baksidan ok; s03 tes +
jätterubrik lika tunga (Q30); s04 Calyx dominerar ok; s05 Hōrai dominerar, priset underordnat
ok; s06 priset + processentré med hel kontur ok; s07 till s10 arket ok; s11 principerna ok;
s12 adressen ok.

### Steg 2, Astra

`codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` med 99 `-i`-bilder och loop 4:s
probtabell i prompten, ett försök 18:09:06 till 18:17:51 (8 min 45 s, exit 0, 316 744 tokens).
Astra: `fix`, tre material_fixes, H-tabell för alla 35 rader. Verifierad rapport:
`reviews/loop-4-astra.md` (`check_reviewer_report.py`: contract held).

| Astra-fynd | Verifierat mot | Dom | Var |
|---|---|---|---|
| 1. Prisplatshållaren (rad 731) | = C1; Astras tillägg bild 77 (`life-01`) som samma fel | tagen (redan plan) | 042 |
| 2. Calyx-revealen är en no-op (rad 677-678: `.rv` klipper inte) | `astra-verify/verify_astra4.json`: ramens top 40 px och wrapperbakgrund 0,1 % synlig vid `--rv` 0 / 0,25 / 0,5 / 1; `calyx-rv0.png`; Hōrai 99,9 → 13,1 % svart | tagen | 043 |
| 3. Driftens överlämning hoppar (rad 1598) | `verify_astra4.json`: `--sc-canvas` blå vid 3 600, papper vid 3 620, träet chroma 21 → 2 | tagen | 044 |
| H-15 "not met, bild 77" | `mountshift.json` (motorn 0,091 mot sant 0,154 i `life-01`) | överens, orsak 042 | HELHET |
| H-23 "not met numerically" | `probe/giant-down-100-cpu1/`, `thesis-…` | Astra har rätt, raden återöppnad | HELHET |
| H-16, H-35 "unverified" | `probe/scroll-verify-*.txt`, `geom4.json scrollW` | körda, bockade | HELHET |
| `latchTick`, `aimPreview`, `.rv`-geometrin: inga fynd | `probe/ab/hero-pin18-*` | överens | ingen |

Inga nya element eller färger föreslogs.

### Slutvillkoret

Nås inte i runda 4: Astra `fix` med tre material_fixes; HELHET § 3 22 av 35 bockade (Q30-raderna
H-02/H-03/H-08 väntar på Anton; H-15/H-30 → 042, H-27 → 043, H-19 → 044; H-21/H-22/H-23/H-32
bildtidens golv, redovisat; H-24 verktygsskuld; H-34 leadens grind); smoothness-grinden röd
vid cpu 4 i båda riktningarna (staircase 0, bildtiden inte).

### Planer till R10 (tre, README § R10): 042, 043, 044

Byggarprompten `tests/alunix-r8/PROMPT-R10-V3c-loop.md` skriven med `{{KONCEPT}}`, `{{UT_MAPP}}`,
`{{PORT}}`, grinden ur R9 § 2 (utökad med geometrikontrollen, CLS bredvid R9:s 0,000, 390-previews
tre laddningar, Calyx-fönstret och driftsekvensen), invarianterna ur R9 § 3. HELHET.md § 3 bockad
rad för rad (22 av 35; H-23 återöppnad), BRIEF § Arkitektens rader loop 4 (sex rader), README §
R10. Q30 och Q31 obesvarade: bandet står, 88 px står; ingen plan staplar om bandet. Inga nya
frågor.
