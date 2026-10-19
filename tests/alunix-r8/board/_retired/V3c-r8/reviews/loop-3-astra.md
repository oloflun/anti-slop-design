fix

## persistence

Codex `gpt-6-astra` (`model_reasoning_effort=medium`) kördes av arkitekten 2026-09-17
13:11:14 till 13:19:28 (8 min 14 s, inom tio minuter, ett försök, exit 0, 313 993 tokens).
Prompt: `shots/loop-3/astra/astra3-prompt.txt` (HELHET.md i sin helhet,
femsektionskontraktet, 108 bilder i ordning ur `shots/loop-3/`: 13 + 14 helsidesskivor,
4 + 5 skivor med latchfixen injicerad, 12 + 12 previews, 12 + 12 flip-ramar, 12 + 12
processramar; invarianterna F-011, motorn, `--sc-ps`, gate 75, låst copy, `sites/*`,
ramarna orörda efter visning; de tre redan verifierade fynden K5 (latchen vägberoende), K6
(driften tvätt, mellantonen), K7 (bildtiden, klippningen över en levande ram) så att Astra
inte bränner budgeten på dem; de sex frågorna). Rå utdata: `shots/loop-3/astra/astra3-out.txt`.

Astra svarade `fix` med **sex** material_fixes och en H-radstabell för alla 35 rader.
Arkitekten verifierade varje fynd mot filen (`index.html` md5 `70214a22`,
`scroll/sc-smooth.js`) och mot mätningar i sidan (`shots/loop-3/preview_check.json`,
`latch_diag.json`): **sex av sex tagna**, varav två (fix 1, fix 4) redan låg i arkitektens
egna planer och utökas med Astras tillägg, och ett (fix 5) fick sin mätning av arkitekten
efter Astras bildläsning. Noll förkastade. Av tabellens 35 rader: överens på 29; sex
avvikelser med skäl i fidelity (H-01, H-05, H-16, H-25, H-30 i arkitektens favör med mätning,
H-15 i Astras).

Disposition `fix` står: grunden (heron, motorn, shimen, tokens, arket, bandet med levande
ramar) är sund; fynden är fyra lägesfel i sidans egen fil, ett previewfel och ett
entréfönster.

## fidelity

Koden gör vad BRIEF.md säger (aktsekvens, `?preview=`-lägena, device-tabellen) med de
avvikelser Astra fann och arkitekten bekräftade:

1. **Latchens aktobjekt dör vid resize** (`index.html:1679` cachar `R.act`; `sc-smooth.js:79`
   `collect()` skapar nya objekt, `:146` vid varje resize). Verifierat i källan: efter en
   resize före bandet läser latchen ett objekt vars `cur` aldrig uppdateras. Tillägg i plan
   035 (lös akten per tick ur `acts` via elementet). Tröskeln `t > R.v + 0.002` kan lämna
   `R.v` vid 0,998: exakt 1 skrivs (plan 035).
2. **`data-on` av på rå `pps − 0,03`** (`index.html:1708`): ett PageUp (800 px = 0,17 av
   aktens liv vid 1440) passerar hysteresen medan `--sc-ps` fortfarande ligger över `s` och
   banan ritar sig tillbaka: klipp, inte baklängesritning. Verifierat mot raden och mot
   025 B4:s egen kommentar (0,03 ≈ 135 px). Plan 039.
3. **Kortsidan byter på rå ps 0,44** (`index.html:1666`) medan `--flip` räknas ur `--sc-ps`
   (lerpad, och för heron dwell-remappad: `scrollcraft.js:835`, `dwell(0,44, 0,2)` = 0,452
   rå). `is-turning` (`:1660`) sätts på position inne i pinnen, inte på rörelse: vilande
   `will-change` när läsaren står stilla i pinnen. Verifierat. Plan 039.
4. **Driften på `:root`** (`index.html:1154`, `:1215` `data-sc-drift`; motorn skriver
   `--sc-canvas` på `docEl`, `scrollcraft.js:983`): Astra föreslår att sidan äger driften
   och skriver på `.ground`. Arkitekten hade samma kandidat (loop 2: 9,13 ms mot 0,24 ms
   per skrivning) men loop 3:s A/B i prisfönstret (cpu 1, `shots/loop-3/probe/ab/`) gav
   ingen mätbar skillnad med driften bortkopplad (35,1 → 40,8 / 35,4 ms; driften skrivs bara
   under de två övergångarna, inte i prisfönstret). Tagen som mätgrindad kodplan 041 (mäts i
   tesfönstret, behålls bara med vinst).
5. **Previews siktar en gång, före typsnitten** (`index.html:1858`). Mätt av arkitekten
   efter Astras bildläsning (`preview_check.py`): 1440 process-02: `--sc-ps` 0,2566 mot
   `--e2` 0,3199, `--k2` 0,19, `#p-dim-width` oritad; 390 process-01: scrollY 6 723 → 6 461
   efter relayout, `--k1` 0,67, `#p-glyph` 0,59. Astra hade rätt om bild 42/43/54/55; R8:s
   kontroll mätte steg 01:s banor i alla lägen, inte steg N:s `--kN`. Plan 037.
6. **Processentrén**: högerspalten bär en toppkant och en högerkant tills konturen är
   hel (`#p-outline` över `--k1` 0 till 0,55, `index.html:945`). Verifierat i
   `slices-1440/v3c-1440--s06.png` och `process-390/v3c-390-life-01.png`. Plan 040 (kontur
   0 till 0,30, glyf 0,30 till 0,70).

Pixlarna, skärm för skärm (1440, `slices-1440/` och `slices-1440-fix/`): s00 till s02
matchar (kortet, kanten, baksidan med glyfen); **s03 avviker**: tes + jätterubrik lika
tunga (Q30), grunden blåtonad (K6, plan 038); **s04, s05 avviker i `scrollTo`-skivorna**
(ramarna helt klippta, K5, plan 035) och **matchar i fix-skivorna** (Calyx dominerar
liggaren, Hōrai dominerar priset: en auktoritet per skärm); s06 matchar delvis (priset som
plan, processentrén med ett hörn av ramen, plan 040); s07 till s10 matchar (arket
kumulativt, måtten i accent, Calyx maskad); s11 matchar (principerna i rail, papper → foto
helbrett); s12 matchar (avslutet ensamt, linjen dragen). 390 (`slices-390/`, `-fix/`): s00
matchar (10 % död grund); s01, s02 matchar; s03 matchar (seam 101 px, tesen); s04 till s06
matchar i fix-skivorna (Calyx, jätterubriken hel på två rader, Hōrai); s07 till s12
matchar; s13 matchar.

Astras H-radstabell mot arkitektens bockar (loop 3, HELHET § 3):

| H | Astra | Arkitekten | Dom |
|---|---|---|---|
| H-04, H-06, H-07, H-09 till H-14, H-17, H-18, H-20, H-23, H-26, H-29, H-31, H-33, H-35 | met | [x] | överens |
| H-02, H-03 | partial | [ ] | överens; Q30 |
| H-08 | partial (bild 28) | [ ] | överens; s03 är Q30, s04/s05 håller i fix-skivorna |
| H-19 | pending | [ ] omskriven på mellantonen | överens; plan 038 |
| H-21, H-22, H-32 | not met | [ ] | överens; plan 036 (klippningen över levande ram, mätt) |
| H-24, H-34 | unverified | [ ] | överens (verktygsskuld, leadens grind) |
| H-27 | partial | [ ] | överens; 035 |
| H-28 | mostly met | [x] med not | överens i sak: `data-on` av-villkoret är 039:s, raden håller (placering, `--sc-ps` för allt som rör sig) |
| H-01 | unverified | [x] omskriven | **avvikelse**: mätt 10 880 px = 12,09 vh (`geom3.json`); raden skrivs om till kedjans budget 8 till 14 (feel-and-fingerprint § Pacing), som fas A citerade fel som 8 till 12 |
| H-05 | partial (101 < 160) | [x] omskriven | **avvikelse**: (a) preciseras till ≥ 160 px vid 1440 och ≥ 96 px vid 390 (plan 032 B:s golv, loop 2); mätt 162 respektive 101 till 102 |
| H-15 | not met (entrén) | [ ] | **avvikelse mot loop 2-bedömningen**: Astra har rätt om entréskärmen (`s06`); plan 040 |
| H-16 | unverified | [x] | **avvikelse i metod**: loop 3 körde `scroll_verify` själv (`probe/scroll-verify-*.txt`) |
| H-25 | partial (jättens skala) | [x] | **avvikelse**: raden kräver en scroll-läst förändring per skärm, inte varje device: skärmen s4 bär ordscrubben, priset sina linjer, avslutet sin linje; jättens skala 0,92 → 1 är oläsbar i tolv ramar och rapporteras som redundant |
| H-30 | not established | [ ] | Astra hade rätt, mätt av arkitekten efter bildläsningen (fix 5); plan 037 |

Svar på frågorna 1 till 4, sammanfattat: sidan hänger ihop som en sida genom rail,
typografi, foto, grafit och ritspråk; det som fortfarande läser som skarvar är bandets
entré (tes + jätterubrik, Q30) och processentrén (040). Rytmen: inga slitsar under 96 px
kvar vid någon bredd; balansen per skärm håller i fix-skivorna utom s03 (Q30). Rörelsen:
kortet kontinuerligt (bild 61 till 84), arket kumulativt (87 till 94, 101 till 105), priset
och avslutets linje läsbara, jättens skala oläsbar; previews 01/02 inte formade (037).

## ceiling

- insign: allt läsbart vid varje offset; V3c:s ramar står klippta för tangentbords- och
  scrollbar-läsaren tills 035.
- highwaymedia: sekvensens skelett läses tidigare; V3c:s entré bär ett hörn av ramen tills
  040.
- hoy: en auktoritet per kapitel; bandets entré har två (Q30).
- K3: en stabil kumulativ ritning; V3c:s previews 01/02 är inte formade (037).

## material_fixes

1. **Latchen samplar lerpen tills den landat, aktobjektet löses per tick, exakt 1**
   (`index.html:1671-1685`, `:1679`, `:1684`). Mål: `--rv` ≥ 0,99 på båda wrapparna efter
   hjul, PageDown, `scrollTo` och resize; noll skrivningar efter landning. **Plan 035.**
2. **Revealen klipper aldrig en levande ram** (`index.html:657-658`, `:1735-1790`). Mätt
   loop 3 (cpu 1, prisfönstret 3 873 till 5 673, ramarna förmonterade): clip-path över levande
   Hōrai p95 139 till 303 ms; `mask-image` 65 till 86; ingen klippning 35. Mål: p95 ≤ 40 ms i
   prisfönstret med ramarna förmonterade. Mekanismen mätt (`probe/ab/r4-iris-*`, `r5-*`): irisen som `border-radius:50%` + `scale(--rv)` på en inre box med ramen kontraskalad ger 35,6 / 46,7 ms (förmonterad) och 48,7 / 35,6 (utan förmontering). **Plan 036.**
3. **Previews siktar om efter `load` och `fonts.ready`** (`index.html:1858-1868`). Mål:
   `--kN` = 1 och `--sc-ps` < `--s(N+1)` i alla 14 lägen. **Plan 037.**
4. **Kortsidan, `is-turning` och `data-on` av läser shimens `cur`** (`index.html:1660`,
   `:1666`, `:1708`). Mål: `inert` växlar i samma bildruta som `--flip` passerar 0,5;
   `is-turning` borta inom 40 bildrutor efter sista scroll-händelsen; PageUp i akten ritar
   baklänges utan klipp. **Plan 039.**
5. **Konturen hel medan steg 01 läses** (`index.html:945`, `:952`). Mål: `#p-outline`
   dashoffset 0 när `.process-grid`:s överkant står på 60 % av viewporthöjden. **Plan 040.**
6. **Driften skrivs på `.ground` av sidan, mätgrindad** (`index.html:1154`, `:1215`,
   `:1511`). Mål: `.panel-thesis`-fönstret cpu 1 p95 ≥ 3 ms bättre, annars återställs.
   **Plan 041.**

## keep

Tvåspaltsbandets offset och luft (i väntan på Q30), 88 px och ordet helt, mobilordningen,
grafitplanet, wrapparnas sömn, reveal en gång på wrappern, ramarna orörda efter visning,
kortets fulla höjd på kant, baksidans glyf, prosan synlig, gridankaret (034 A), den
kumulativa ritningen, måtten i accent, prisliggarens linjer, avslutet ensamt på fotot,
`--sc-ps`-kontraktet (staircase 0 i alla loop 3-körningar, båda riktningarna, båda
kadenserna, cpu 1 och 4). Inga nya element eller färger föreslogs av Astra; arkitekten
föreslår inga heller (038 ändrar en alfa, inte en färg).
