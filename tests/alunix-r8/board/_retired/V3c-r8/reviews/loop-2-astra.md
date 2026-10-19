fix

## persistence

Codex `gpt-6-astra` (`model_reasoning_effort=medium`) kördes av arkitekten 2026-09-17 två
gånger. Första försöket 04:56:35 till 05:01:02 avbröts av Codex' egen användningsgräns
("You've hit your usage limit … try again at 8:06 AM", `scratch/astra2-err-attempt1.txt`,
ingen rapport, 237 544 tokens brända på inläsning) och redovisas som ett misslyckat pass, inte
som en rapport. Andra försöket 08:09:15 till 08:17:04 UTC+2 (7 min 49 s, inom tio minuter),
samma prompt och samma 99 bilder i ordning (`shots/loop-2/`: 13 + 14 helsidesskivor, 12 + 12
previews, 12 + 12 flip-ramar, 12 + 12 processramar), HELHET.md i sin helhet, femsektions-
kontraktet, invarianterna (F-011, motorn, `--sc-ps`, gate 75, låst copy, `sites/*`), de sex
frågorna, plus de fyra redan verifierade fynden K1 till K4 (ramarna vaknar inte, den blå
tvätten, det delade ordet, bildtidens attribution) så att Astra inte skulle bränna sin
budget på dem. Prompt och rå utdata: scratch `astra2-prompt.txt`, `astra2-out.txt`.

Astra svarade `fix` med tre material_fixes och en H-radstabell för alla 35 rader.
Arkitekten verifierade varje fynd mot filen (`index.html`, md5 `d30355da`) och sidan i
webbläsaren (scratch `verify_astra2.py`, `shots/loop-2/diag/astra1-*.png`): **tre av tre
tagna**, varav ett (fix 2) delvis: batchningen av shimens läsningar hade arkitekten redan
mätt oberoende (plan 028 A, samma mekanism), `--kN`-scopingen är en kandidat utan mätning
och går in som mätsteg i 028, och "frontier-only word updates" ersätts av 028 C
(gradientfront, mätt 2,10 → 0,84 ms). Noll förkastade. Av tabellens 35 rader: överens på
32; tre avvikelser med skäl i fidelity (H-07, H-16, H-23).

Disposition `fix` står: grunden (heron, motorn, shimen, tokens, arket) är sund; fynden är
tre kodfel i sidans egen fil.

## fidelity

Koden gör vad BRIEF.md säger (aktsekvens, `?preview=`-lägena, device-tabellen) med tre
avvikelser som Astra fann och arkitekten bekräftade i sidan:

1. **`--s1` mäts från ett fastnat sticky-element** (index.html:1547). Verifierat:
   `?preview=process-05` ger `--s1` 0,4847 mot `--e1` 0,2292 vid 1440 och 0,4449 mot 0,2510
   vid 390; `#p-outline` och `#p-glyph` har `stroke-dashoffset: 1px` (osynliga) i
   `process-03` och `process-05` vid båda bredderna (`astra1-1440-process-05.png`,
   `astra1-390-process-05.png`). Loop 2:s egna previews (`preview/preview-1440-process-*`)
   råkade fånga ett läge före `load`-mätningen, därför syntes ramen där; en färsk fångst
   visar felet. Astra hade rätt i sak för båda bredderna. Plan 034 A.
2. **Shimen tvingar omräkningar** (sc-smooth.js `tick()`, index.html:1445). Mätt av
   arkitekten före Astra: 1,7 till 4,6 omräkningar per frame mot 1,0 i kontrollen
   (`profile4.json`); batchad shim 1,2 till 1,4. Plan 028 A. `--kN`-scopingen: mätt att
   `.process-steps` display:none sänker en `#process`-skrivning 2,20 → 1,59 ms, men det är
   `--sc-ps`-arvet (inherits:true, nödvändigt) som invaliderar prosan, inte `--kN`; scopingen
   får ett mätsteg i 028, inget löfte.
3. **Prosan deltar i motorns reveal** (index.html:1230 `data-sc-in data-sc-stagger`).
   Verifierat: vid ramen `life-01` (390) är `li 01` opacity 0, `translateY(14px)`, `<ol>`
   opacity 0; li-topparna ligger 28 px lägre före revealen än efter, vilket förskjuter alla
   `--sN`/`--eN`. Vid 1440 fångas stycket mitt i toningen (`process-1440/v3c-1440-life-01.png`,
   bild 77, "Uppstart" utgråat). Plan 034 B.

Pixlarna, skärm för skärm (1440, `slices-1440/`): s00 till s02 matchar (kortet, kanten,
baksidan med glyfen); **s03 avviker**: `VARUMÄRK` / `E.` (K3, plan 030), tes + jätterubrik
lika tunga (Q30); **s04, s05 avviker**: Calyx beige platta, Hōrai svart platta (K1, plan
027), grunden blå (K2, plan 029); s06 matchar (priset som plan, processentrén); **s07
avviker delvis**: högerspalten tom tills arket når in, prosan tonar (plan 034 B); s08 till
s10 matchar (arket kumulativt, måtten i accent, Calyx maskad); s11 matchar (principerna i
rail, papper → foto helbrett); s12 matchar (avslutet ensamt, linjen dragen). 390
(`slices-390/`): s00 matchar utom H-13 (137 px död grund, plan 032 A); s01, s02 matchar
(kanten, baksidan); **s03 avviker**: 84 px slits mellan tesen och Calyx (Astra bild 18,
plan 032 B); **s04, s05 avviker**: Calyx-plattan tom (K1); s06 matchar (Hōrai vaken av en
slump i den fångsten, priset); s07 till s11 matchar (arket, stegen); s12, s13 matchar.

Astras H-radstabell mot arkitektens bockar (loop 2, HELHET § 3):

| H | Astra | Arkitekten | Dom |
|---|---|---|---|
| H-01, H-04, H-06, H-09 till H-12, H-14, H-17, H-18, H-20, H-26, H-28, H-29, H-31, H-33, H-35 | met | [x] (H-01 [ ]: 12,09 vh, 0,09 över raden) | överens; H-01 är arkitektens strängare läsning av sitt eget tal |
| H-02, H-03 | open / partial | [ ] | överens; Q30 |
| H-05 | partial, mobilen 84 px | [ ] | **tagen**: 032 B (gap 96 till 120 px) |
| H-07 | "numeric threshold met at 96, composition fails" | [ ] omskriven till 88 px + ordet helt | **avvikelse**: 96 px kan inte hålla ordet i en 555 px-spalt (mätt 601 px); raden skrevs om med mätningen, Q31 till Anton |
| H-08, H-13, H-15 | not met / partial | [ ] | överens (027, 032 A, 034) |
| H-16 | "accepted R7 evidence" | [x] | **avvikelse i metod**: loop 2 körde `scroll_verify` själv (`probe/scroll-verify-*.txt`), banden förklarade i raden |
| H-19 | numeric met, aesthetic fails | [x] med 029 | överens i sak: raden håller som tal, 029 tar intensiteten |
| H-21, H-22, H-32 | not met | [ ] | överens; 028 med mätta målvärden |
| H-23 | "upward 4,54 % (R7)" | [ ] | **avvikelse**: R7:s 4,54 % reproducerades inte (1,48 % cpu 1 uppåt); det som står över 3 % är footern och priset vid cpu 4 (5,79 / 16,41 %), 2,80 % vid cpu 1: bildtidens följd |
| H-24, H-34 | unverified / partial | [ ] | överens |
| H-25 | partial (priset, jättens skala) | [ ] | överens: 033 för priset; skalan rapporteras |
| H-27 | partial (latch) | [ ] | **tagen**: 031 (loop 1 sköt den hit) |
| H-30 | not met | [ ] | överens: 034 A |

Svar på frågorna 1 till 4, sammanfattat: sidan hänger ihop bättre än i R6 (offseten,
grafitplanet, papperskontinuiteten, avslutet), men balansen i bandet kan inte dömas förrän
ramarna renderar (K1); rytmen bryts av de tomma plattorna, av 84 px-slitsarna vid 390 och av
processentréns tomma högersida med tonande prosa; rörelsen: kortet kontinuerligt (bild 52
till 75), arket kumulativt i verklig scroll (78 till 84) men inte i previews (fix 1),
avslutets linje läsbar som rörelse, jätterubrikens skala inte läsbar i tolv ramar.

## ceiling

- insign: allt innehåll läsbart vid varje offset; V3c:s processprosa tonar in (034 B) och
  ramarna står tomma (027) tills R8.
- highwaymedia: sekvensen läses som framsteg innan detaljerna; V3c:s entré dröjer tills
  arkets ram etablerats (034 A rättar ankaret, 025 B:s ankomst står).
- hoy: en auktoritet per kapitel; bandet behöver sina levande bevis tillbaka (027) innan
  balansen kan dömas, och Q30 avgör resten.
- K3: en stabil kumulativ ritning; V3c:s previews tappar steg 01 (034 A).

## material_fixes

1. **Stegens ankare oberoende av sticky-läget** (index.html:1547, 1566-1567, 1780): `--s1`
   ur gridets överkant, inte ur det fastnade arkets rect. Mål: `--s(N) < --e(N)` för alla N
   i alla sju previews vid 1440 och 390; `#p-outline`/`#p-glyph` `stroke-dashoffset 0px` i
   preview 02 till 07; samma `--s1` före och efter `resize` mitt i akten. **Plan 034 A.**
2. **Prosan utan reveal** (index.html:1230): `data-sc-in`/`data-sc-stagger` bort från
   `<ol class="process-steps">`. Mål: `li` opacity 1 och transform none vid varje offset;
   li-topparna vid `load` = efter 2 s. **Plan 034 B.**
3. **Shimen batchar och `--sc-p` ärvs inte** (sc-smooth.js `tick()`, registrering): läs
   `--sc-p` ur inline-stilen, skriv alla `--sc-ps` efter alla läsningar; `CSS.registerProperty
   --sc-p inherits:false`. Mål: RecalcStyleCount ≤ 1,4 per frame (mätt 1,2 till 1,4), cpu 1
   hero p95 ≤ 20 ms (mätt 18,8). `--kN`-scopingen som mätsteg. **Plan 028 A, B (+ E).**

## keep

Kortet som fysiskt objekt med sin landning, baksidans balans med glyfen, tvåspaltsbandets
offset (i väntan på Q30), mobilordningen, grafitplanet, de återhållna bildtexterna, arkets
kumulativa ritspråk och pappersflödet in i principerna, avslutet ensamt på sista skärmen,
`--sc-ps`-kontraktet (staircase 0 i alla loop 2-körningar, båda riktningarna, båda
kadenserna, cpu 1 och 4). Inga nya element eller färger behövs för de tre fixarna; Astra
föreslog inga heller.
