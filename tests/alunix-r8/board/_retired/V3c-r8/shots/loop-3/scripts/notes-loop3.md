
## Loop 3 (arkitekten, 2026-09-17): helhetsloopen fas C, runda 3 av max 6

Kontrakt: `tests/alunix-r8/PROMPT-LOOP-V3c.md`, N = 3, RN = 9. Mål: R8-läget av
`runs/V3c/index.html` (md5 `70214a22`) på port 3090 (leadens angivelse; 4626 speglar).
`Skill(design)` anropad som första handling. Fångst i `shots/loop-3/`, allt vid 1440x900 och
390x844 med installerad Chrome, `reduced_motion="reduce"` (F-011), previews med
`wait_until="load"` + 1,5 s (loop 2:s verktygsfynd). Skript (kopierade till
`shots/loop-3/scripts/`): `cap_loop3.sh`, `previews3.py`, `latch_diag.py`, `drift_diag.py`,
`drift2.py`, `slices_fix.py`, `geom3.py`, `preview_check.py`, `probes3.sh`, `motion_probe_ab.py`
(`--pre`), `ab_band.sh` till `ab_band6.sh`, `build_astra_prompt3.py`, `tick_helhet3.py`,
`patch_docs3.py`. Astra: `shots/loop-3/astra/`. Rundan pausades av Codex användningsgräns
efter steg 1:s fångst och återupptogs på leadens order; md5 oförändrad, servrarna omstartade
av lead.

### Steg 1, fångat och läst

Dokumenthöjd 10 880 px = 12,09 vh vid 1440 (oförändrad sedan loop 2), 11 588 px = 13,73 vh
vid 390 (`geom3.json`).

Läst som pixlar med `Read` (117 bilder):

- läst: `slices-1440/v3c-1440--s00.png` till `v3c-1440--s12.png` (13)
- läst: `slices-390/v3c-390--s00.png` till `v3c-390--s13.png` (14)
- läst: `slices-1440-fix/v3c-1440--s03.png` till `v3c-1440--s06.png` (4, 035:s sampler injicerad)
- läst: `slices-390-fix/v3c-390--s03.png` till `v3c-390--s07.png` (5)
- läst: `preview/preview-1440-front|mid|back|ledger|bleed|process-01..07.png`, `preview-390-…` (24)
- läst: `flip-1440/v3c-1440-flip-00-000.png` till `v3c-1440-flip-11-100.png` (12)
- läst: `flip-390/v3c-390-flip-00-000.png` till `v3c-390-flip-11-100.png` (12)
- läst: `process-1440/v3c-1440-life-00.png` till `v3c-1440-life-11.png` (12)
- läst: `process-390/v3c-390-life-00.png` till `v3c-390-life-11.png` (12)
- läst: `drift/c44-thesis.png`, `c22-thesis.png`, `c16-thesis.png`, `c00-thesis.png`, `drift2/d24-thesis.png`, `d18-thesis.png` (6); inte lästa som pixlar: `drift/*-giant.png`, `*-fold.png`, `drift2/d*-fold.png`, `d*-giant.png`, `d44`/`d30`-bilderna (bara talen)
- läst: leadens `shots/r8-lead/frames-wait-4600.png`, `wheel-4700.png` (2); `shots/r8/calyx12-390-11.png` (1)
- inte läst som pixlar: `probe/*/frame-times.png`, `track-*.png`, `probe/sv-*/` (kontaktark), `probe/ab/**` (bara talen)

**Leadens två fynd, verifierade och rotorsakade:**

1. **Latchen är vägberoende** (`latch_diag.json`, 1440x900, scrollY 4 703 = `.horai-fig`
   `--sc-ps` 0,58): hjul 100 px / 60 ms `--rv` Hōrai 0,979 / Calyx 1 (10 skrivningar);
   PageDown 0,207 / 1 (1 skrivning); `window.scrollTo` **0 / 0**; smooth `scrollTo` **0 / 0**.
   Orsak: `readState` (rad 1671 till 1685) samplar `act.cur` bara ur `schedule()` (scroll- och
   resize-händelser, rad 1716 till 1718); shimen lerpar ~30 bildrutor efter sista händelsen
   utan att någon samplar. `R.from`/`R.to` stämmer mot flow-spannet (iris öppen vid p 0,55,
   figuren centrerad vid 0,68); `R.sel` matchar rätt akt. Med en rAF-sampler som kör medan
   någon reveal < 1 och akten lerpar (injicerad): 0,9998 / 1, 0,9995 / 1, 1 / 0,9988, 1 / 0,9988.
   `scrollTo`-skivorna `slices-1440/…s04`, `s05` visar därför ramarna **helt klippta** (rå grund
   där de ska stå), inte sovande; `slices-1440-fix/` visar dem hela. Plan 035.
2. **Grunddriften vid 44 %** (`drift2/drift2.json`, tesen centrerad, mellantonspixlar):
   träpanelen (720,180) gråskala (128,128,128); 44 % (112,132,150) chroma **38**; 30 % 26;
   24 % **21**; 18 % 16; marginalen (1420,850) delta fold → tes 11 / 8 / 7 / 5. Folden neutral
   (chroma 0 till 1) vid alla styrkor. `d44-thesis.png`: träet är blått (tvätt);
   `d24-thesis.png`: gråskalefoto i kallt ljus; `d18`: nästan neutralt. Dom mot TASTE § 4.4:
   24 %. H-19:s golv (12 steg på en L 20-pixel) var fel mätpunkt: `mix-blend-mode:color`
   skalar kulören med luminansen, så golvet tvingade tvätten. H-19 omskriven på mellantonen
   (chroma 12 till 24 vid tesen, ≤ 2 i folden). Plan 038.

**`motion_probe.py`** (scratchkopia med `--start`, kontrollprotokollet; kontrollen gav 0 till
2 rutor > 33 ms i alla tio körningar, 18,2 till 18,5 ms p95, "aldrig helt tyst"):

| Körning | cpu | hjul | riktning | spår | p95 ms | > 33 ms | max_step | staircase |
|---|---|---|---|---|---|---|---|---|
| hero-down-100 | 4 | 100:60 | ned | `section.hero:--sc-ps` / `.plate-card:transform` | 89,5 | 88 | 1,65 % / 2,48 % | 0 / 0 |
| hero-up-100 | 4 | 100:60 | upp | samma | 54,0 | 81 | 1,85 % / 2,72 % | 0 / 0 |
| hero-down-20 | 4 | 20:120 | ned | samma | 53,2 | 418 | 0,36 % / 0,41 % | 0 / 0 |
| hero-up-20 | 4 | 20:120 | upp | samma | 36,5 | 289 | 0,34 % / 0,41 % | 0 / 0 |
| proc-down-100 | 4 | 100:60 | ned | `#process:--sc-ps` | 285,1 | 143 | 0,99 % | 0 |
| proc-up-100 | 4 | 100:60 | upp | samma | 460,7 | 117 | 1,71 % | 0 |
| proc-down-20 | 4 | 20:120 | ned | samma | 88,5 | 747 | 0,23 % | 0 |
| proc-up-20 | 4 | 20:120 | upp | samma | 88,4 | 701 | 1,20 % | 0 |
| hero-down-100-cpu1 | 1 | 100:60 | ned | hero | 36,1 | 19 | 1,41 % / 2,01 % | 0 / 0 |
| hero-up-100-cpu1 | 1 | 100:60 | upp | hero | 18,4 | 5 | 1,38 % / 2,20 % | 0 / 0 |
| proc-down-100-cpu1 | 1 | 100:60 | ned | process | 32,1 | 14 | 0,78 % | 0 |
| proc-up-100-cpu1 | 1 | 100:60 | upp | process | 18,5 | 4 | 1,42 % | 0 |
| giant-down-100-cpu1 (2 700, 28 ticks) | 1 | 100:60 | ned | `#giant-section:--sc-ps` | 128,1 | 22 | 2,82 % | 0 |
| price-down-100-cpu1 (3 873, 18) | 1 | 100:60 | ned | `.price:--sc-ps` | 143,7 | 16 | 2,25 % | 0 |
| footer-down-100-cpu1 (8 500, 18) | 1 | 100:60 | ned | `footer.close:--sc-ps` | 18,4 | 5 | 2,74 % | 0 |
| kontroll (10 körningar) | 4 / 1 | 100:60 | ned | `#act:--sc-ps` / `#card:transform` | 18,2 till 18,5 | 0 till 2 | 1,35 till 1,51 % | 0 |

(Den första footer-körningen spårade också `.price` från 8 500, alltså efter aktens slut:
`.price` 16,0 % / staircase 1 där är probens första adoption, inte sidans; körningen om från
3 873 gav 2,25 % / 0 och står i tabellen.) Läsning: staircase 0 på varje spår i varje
körning; `--sc-ps` max_step ≤ 3 % överallt vid cpu 1 (H-23 bockad); R8:s 4,61 % uppåt inte
reproducerad (1,38 %). Bildtidsbaren faller vid cpu 4 överallt och vid cpu 1 i heron nedåt
(36,1), arket nedåt (32,1) och framför allt i bandet (128 / 144).

**A/B-ablation av bandet** (`probe/ab/`, cpu 1, prisfönstret 3 873 + 18 ticks om inget
annat sägs, `motion_probe_ab.py --pre` = JS efter `load` + 5 s):

| variant | p95 ms per körning |
|---|---|
| som byggd (ramen monteras i fönstret) | 109 / 127 |
| förmonterad, `clip-path: circle()` över levande Hōrai | 202 / 303 / 187 / 139 / 101 |
| förmonterad, `clip-path: inset()` | 124 / 214 |
| förmonterad, `will-change: clip-path` | 71 / 142 |
| förmonterad, `contain: paint` | 183 / 164 |
| förmonterad, `mask-image: radial-gradient` | 86 / 65 / 70 / 68 / 72 |
| förmonterad, ramen `visibility:hidden` under klippningen | 139 / 157 |
| förmonterad, ingen klippning (`--rv` 1) | 35 / 35 / 36 / 62 |
| förmonterad, ingen klippning, `data-sc-drift` bort | 41 / 35 |
| förmonterad, **iris som transform** (inre box `border-radius:50%` `scale(t)`, ramen `scale(1/t)`) | **35,6 / 46,7** |
| förmonterad, samma utan kontraskalning | 125 / 138 |
| förmonterad, uppdragning som `translateY` på inre box utan kontratransform | 98 / 119 |
| iris som transform, **utan** förmontering | 48,7 / 35,6 |
| jättefönstret (2 700 + 28): som byggd | 123 / 208 |
| jättefönstret: hela receptet utan förmontering | 121 / 88,5 |
| jättefönstret: hela receptet med förmontering | 57,7 / 53,0 |

Slutsats, mätt: en `clip-path` eller `mask` på en wrapper med en monterad iframe är
bandets bildtid (70 till 300 ms), oavsett form; en transform på en inre box med ramen
kontratransformerad kostar inget utöver det omonterade fallet; monteringen av de två
sajterna kostar ~40 till 60 ms i jättefönstret; driften på `:root` ger ingen mätbar skillnad
i prisfönstret (den skrivs bara i övergångarna). Plan 036 (A receptet, B monteringen i
heroens svans), 041 mätgrindad.

**`scroll_verify.py`** (`probe/scroll-verify-1440.txt`, `-390.txt`): 1440 deadScroll åtta band:
0 till 300 (0,0046) och 1 800 till 2 100 (0,0028) författade; 1 500 till 1 800 (0,008) kortet på
kant mot mörk grund (verktygsblindhet, `flip-1440/…-05`, `-06`); 900 till 1 200, 5 700 till
6 000, 6 300 till 6 600, 6 900 till 7 200, 8 100 till 8 400 (0,0107 till 0,0146) över 0,01.
blankBands 900 till 3 222 (pinnen). 390: 0 till 281 (0,0093) författad, 1 405 till 1 686 (0,0148),
1 686 till 1 967 (0,0) landad baksida; blankBands sex: pinnen, 3 330 till 4 031 (Calyx), 4 803
till 5 473 (Hōrai), 5 484 till 6 221 (priset), 6 403 till 6 919 (processentrén), 10 398 till 10 910
(avslutets foto). Calyx/Hōrai-banden är K5 (verktyget scrollar med `scrollTo`, latchen når
inte 1), inte sovande ramar. cuesNeverFull, unrevealed, contrastUnderMedia tomma vid båda.

**Previews** (`preview_check.json`, `load` + 2 s): 1440 process-01 `--k1` 1 (formad); 1440
process-02 `--sc-ps` 0,2566 mot `--e2` 0,3199, `--k2` **0,19**, `#p-dim-width` oritad; 390
process-01 scrollY 6 723 → 6 461 efter relayout, `--k1` **0,67**, `#p-glyph` 0,59; 390
process-02 formad. Målscrollen räknas en gång före typsnitten (rad 1858). Plan 037.

**Grep:** `prefers-reduced-motion` 0; tankstreck i synlig text 0 (R8:s grep står, inget ändrat);
låst copy 15/15 (md5 oförändrad sedan R8:s kontroll).

### Steg 3, egna fynd ur pixlarna (före Astra)

| # | Fynd | Bild / tal | Dom | Plan |
|---|---|---|---|---|
| C1 | Ramarna helt klippta i `scrollTo`-skivorna, hela i fix-skivorna | `slices-1440/…s04`, `s05` mot `slices-1440-fix/…s04`, `s05`; `latch_diag.json` | leadens fynd 1, rotorsak: sampling bara per scroll-händelse | 035 |
| C2 | Grunden blåtonad bakom tesen och jätten | `slices-1440/…s03`, `s04`; `drift2/d44-thesis.png` mot `d24-thesis.png` | leadens fynd 2; H-19:s mätpunkt fel, omskriven | 038 |
| C3 | Bandets bildtid är klippningen över en levande ram | `probe/ab/` (sex omgångar) | mätt; transformreceptet 35 till 47 ms | 036 |
| C4 | Previews 01 (390) och 02 (1440) inte formade | `preview_check.json`; `preview-390-process-01.png`, `preview-1440-process-02.png` | verifierat efter Astras bildläsning | 037 |
| C5 | Processentrén: högerspalten bär ett hörn av ramen | `slices-1440/…s06`, `process-390/…life-01` | H-15 öppen (Astra fix 6) | 040 |
| C6 | Bandets balans med levande ramar: Calyx dominerar liggaren, Hōrai priset | `slices-1440-fix/…s04`, `s05` | H-08 håller för s04/s05; s03 är Q30 | ingen |
| C7 | Jätterubriken 88 px hel på tre rader (1440), två rader (390) | `preview-1440-ledger.png`, `slices-390-fix/…s05`, `geom3.json` | 030 verifierad, H-07 bockad | ingen |
| C8 | Folden 390: ~85 px grund under underraden | `slices-390/…s00`, `preview-390-front.png` | 032 A verifierad, H-13 bockad | ingen |
| C9 | Seams 162 px vid 1440, 101 till 102 px vid 390; pris → papper helbrett | `geom3.json`, `slices-390-fix/…s03` till `s07` | H-05 bockad, (a) preciserad | ingen |
| C10 | Prisliggarens linjer mitt i dragningen, avslutets linje | `slices-1440-fix/…s05`, `process-1440/…life-00`, `s11`/`s12` | 033, 015 verifierade; H-25 bockad | ingen |
| C11 | Kortvändningen kontinuerlig i tolv ramar vid båda bredderna, kanten 4 px | `flip-1440/`, `flip-390/` | H-10, H-18 står | ingen |
| C12 | Arket kumulativt 01 till 07, tonbytet vid 06, revisionsfältet vid 07 | `process-1440/…life-02..11`, `process-390/…life-02..10` | H-29, H-31, H-33 står | ingen |
| C13 | Avslutet ensamt på sista skärmen, mailto 98 px | `slices-1440/…s12`, `slices-390/…s13`, `geom3.json` | H-12 står | ingen |
| C14 | Jättens skala 0,92 → 1 oläsbar i tolv ramar | Astra loop 2 och 3; ingen `giant`-ramsekvens i loop 3 | redundant mot ordscrubben; rapporteras, ingen plan | ingen |
| C15 | `scroll_verify`:s blankBands vid Calyx/Hōrai är K5, inte sovande ramar | `probe/scroll-verify-390.txt` mot `slices-390-fix/` | verktygsfynd | README § Verktygsfynd |

Squint 5 px per 1440-skärm (fix-skivor för bandet): s00 rubriken ok; s01 kortet på kant ok;
s02 baksidan ok; s03 tes + jätterubrik lika tunga (Q30); s04 Calyx dominerar ok; s05 Hōrai
dominerar, priset underordnat ok; s06 priset + processentré med ett hörn av ramen (040);
s07 till s10 arket ok; s11 principerna ok; s12 adressen ok.

### Steg 2, Astra

`codex exec -m gpt-6-astra -c model_reasoning_effort="medium"` med 108 `-i`-bilder, ett
försök 13:11:14 till 13:19:28 (8 min 14 s, exit 0, 313 993 tokens). Astra: `fix`, sex
material_fixes, H-tabell för alla 35 rader. Verifierad rapport: `reviews/loop-3-astra.md`
(`check_reviewer_report.py`: contract held).

| Astra-fynd | Verifierat mot | Dom | Var |
|---|---|---|---|
| 1. Latchens aktobjekt dör vid resize; exakt 1 | `sc-smooth.js` 79, 146; `index.html` 1679, 1684 | tagen (tillägg) | 035 |
| 2. `data-on` av på rå `pps − 0,03` klipper vid stort hopp uppåt | `index.html` 1708; 025 B4 | tagen | 039 |
| 3. Kortsidan byter på rå ps 0,44; `is-turning` på position, inte rörelse | `index.html` 1660, 1666; `scrollcraft.js` 835 | tagen | 039 |
| 4. Driften på `:root` → `.ground` | loop 2 `synth3`; loop 3 `probe/ab/` (ingen vinst i prisfönstret) | tagen som mätgrindad | 041 |
| 5. Previews siktar en gång före typsnitten | `preview_check.json` (mätt efter bildläsningen) | tagen | 037 |
| 6. Processentrén bär bara ett streck | `slices-1440/…s06`, `process-390/…life-01` | tagen | 040 |
| H-01 "unverified" | `geom3.json` 12,09 vh | raden omskriven till kedjans budget med källa, bockad | HELHET |
| H-05 "101 < 160" | `geom3.json`, 032 B | (a) preciserad per bredd, bockad | HELHET |
| H-16 "unverified" | `probe/scroll-verify-*.txt` | körd, bockad | HELHET |
| H-25 "jättens skala" | tolv ramar | raden gäller per skärm, inte per device; bockad, skalan rapporterad | HELHET |
| H-15 "not met" | `s06` | Astra har rätt; loop 2:s bock tas tillbaka | 040 |

### Planer till R9 (sju, README § R9): 035, 036, 037, 039, 040, 038, 041

Byggarprompten `tests/alunix-r8/PROMPT-R9-V3c-loop.md` skriven med `{{KONCEPT}}`, `{{UT_MAPP}}`,
`{{PORT}}`, grinden ur R8 § 2 (utökad med latchtabellen, previews i båda riktningarna,
PageUp-kontrollen, `clip-path`-greppet), invarianterna ur R8 § 3. HELHET.md § 3 bockad rad
för rad (23 av 35; H-01, H-05 (a), H-19 omskrivna med skäl i raden), BRIEF § Arkitektens
rader loop 3 (nio rader), README § R9. Q30 och Q31 obesvarade: bandet står, 88 px står; ingen
plan staplar om bandet. Inga nya frågor.
