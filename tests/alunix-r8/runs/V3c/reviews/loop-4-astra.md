fix

## persistence

Codex `gpt-6-astra` (`model_reasoning_effort=medium`) kördes av arkitekten 2026-09-17
18:09:06 till 18:17:51 (8 min 45 s, inom tio minuter, ett försök, exit 0, 316 744 tokens).
Prompt: `shots/loop-4/astra/astra4-prompt.txt` (HELHET.md i sin helhet med loop 3-raderna,
femsektionskontraktet, 99 bilder i ordning ur `shots/loop-4/`: 13 + 14 helsidesskivor med
plain `scrollTo` och 3 s väntan, 12 + 12 previews, 12 + 12 flip-ramar, 12 + 12 processramar;
loop 4:s probtabell med hero-dekompositionen och prisplatshållarens A/B; de fem redan
verifierade lägena K8 till K12; invarianterna F-011, motorn, `--sc-ps`, gate 75, låst copy,
`sites/*`, ramarna orörda efter visning; slutvillkoret utskrivet; de sex frågorna). Rå
utdata: `shots/loop-4/astra/astra4-out.txt`.

Astra svarade `fix` med **tre** material_fixes och en H-radstabell för alla 35 rader.
Arkitekten verifierade varje fynd mot filen (`index.html` md5 `909916d1`) och mot egna
mätningar i sidan (`shots/loop-4/astra-verify/verify_astra4.json`, `pricefix_ab.json`,
`mountshift.json`): **tre av tre tagna**, varav ett (fix 1) var arkitektens eget fynd C1 med
plan 042 redan skriven före Astra-passet, och två (fix 2, fix 3) är nya, båda reproducerade
med tal och bild efter Astras läsning. Noll förkastade. Av tabellens 35 rader: överens på
32; tre avvikelser med skäl i fidelity (H-16 och H-35 i arkitektens favör med mätning,
H-23 i Astras med precisering).

Disposition `fix` står. Slutvillkoret nås inte i runda 4: tre materiella fynd, varav två
funktionsfel i R9:s egen kod (036:s Calyx-öppning som aldrig klipper; prisblockets
platshållare som förskjuter allt under bandet) och ett kurvfel som 041 ärvde av motorn.

## fidelity

Koden gör vad BRIEF.md säger (aktsekvens, `?preview=`-lägena, device-tabellen) med de
avvikelser Astra fann och arkitekten bekräftade:

1. **Prisblockets platshållare** (`index.html:731`, `content-visibility:auto;
   contain-intrinsic-size:auto 760px`): 760 px mot blockets 463 px (1440) / 450 (390); sidan
   krymper 297 / 262 px första gången blocket målas, motorns akttoppar för `#process`,
   `#principer` och `footer.close` står kvar 297 px fel tills ett riktigt resize, och
   390-previews 01/02 formas i 1 av 3 laddningar. Verifierat före Astra (`mountshift.json`,
   `shiftprobe*.json`, `preview390*.json`, `pricefix_ab.json`: med platshållaren
   neutraliserad `engTop` = `realTop` och 6 av 6 previews formade). Astras tillägg: bild 77
   (`process-1440/v3c-1440-life-01.png`, tom högerspalt bredvid steg 01) är samma fel
   (motorn 0,091 mot sant 0,154), inte plan 040:s. **Plan 042** (skriven, utökad med 2b).
2. **Calyx-revealen är en no-op** (`index.html:677-678`): `.rv` flyttas ned och ramen upp
   lika mycket, men `.rv` klipper inte och wrapperns `overflow:clip` sitter på den
   stillastående boxen; ramens sammansatta position är wrapperns topp vid varje `--rv`.
   Mätt (`astra-verify/verify_astra4.json`, ramen monterad, `--rv` tvingad 0 / 0,25 / 0,5 /
   1): ramens top 40 px i alla fyra, wrapperbakgrund synlig 0,1 % i alla fyra
   (`calyx-rv0.png` visar hela Calyx); Hōrai i samma mätning 99,9 % → 31,8 % → 13,1 %
   svart (irisen fungerar). Loop 3:s A/B-recept hade samma fel, så "hela receptet 57,7 /
   53,0 ms" mätte en Calyx utan klippning. **Plan 043.**
3. **Driftens överlämning hoppar** (`index.html:1598`): leg 2 räknar `smooth(g / 0,35)` från
   jättens egen start, som ligger 108 px efter tesen; när tesen når 1 (scrollY 3 600 vid
   1440) är `g` 0,68 och leg 2 redan på 1. Mätt: `--sc-canvas` rgb(18,63,104) vid 3 600,
   rgb(244,242,238) vid 3 620; träpanelen chroma 21 → 2 på 20 px scroll (`verify_astra4.json`,
   `drift-3580.png`, `drift-3620.png`). Motorns egen loop gjorde samma sak i R7/R8 (041
   reproducerade troget). **Plan 044.**

Astras kodläsning i övrigt, bekräftad: `latchTick` fortsätter bara medan heron, akten
eller en ofärdig reveal lerpar, läser inline-egenskaper och cachade tal, inga
`getComputedStyle`/`getBoundingClientRect` per bildruta; pinnen ensam mäter 18,4 ms p95
(kontrollens tal) i tre körningar (`probe/ab/hero-pin18-*`), så per-bildruta-samplern är inte
herofönstrets kostnad. `aimPreview` har generations-id och begränsad settle-slinga,
lyssnarna är preview-skopade; Hōrais kvadrat (0,552 × diagonalen > 0,5) täcker wrappern och
kontraskalan tar ut sig. Ingen av dessa är ett fynd.

Pixlarna, skärm för skärm (1440, `slices-1440/`): s00 till s02 matchar (kortet, kanten,
baksidan med glyfen); **s03 avviker** (tes + jätterubrik lika tunga, Q30, väntar på Anton;
grunden kallt ljus, inte tvätt, 038 håller); s04 matchar (Calyx hel, dominerar liggaren;
ramen hel i en vanlig `scrollTo`-skiva, 035 håller); s05 matchar (Hōrai dominerar priset,
`--rv` 0,9487, prisliggarens tredje linje mitt i dragningen); s06 matchar delvis
(processentrén med hel kontur och påbörjad glyf, 040 håller; men kickern står vid y 18 för
att sidan redan krympt 297 px, plan 042); s07 till s10 matchar (arket kumulativt, måtten i
accent, Calyx maskad); s11 matchar (principerna i rail, papper → foto helbrett); s12
matchar (avslutet ensamt, linjen dragen). 390 (`slices-390/`): s00 matchar (10 % död
grund); s01, s02 matchar; s03 matchar (seam 101 px, tesen); s04 matchar (Calyx hel; Calyx
egna nav över ordmärket är referenssajtens, rapporterat i R9); s05 matchar (jätterubriken
hel på två rader, liggaren); s06 matchar (Hōrai hel, priset); s07 till s12 matchar; s13
matchar.

Astras H-radstabell mot arkitektens bockar (loop 4, HELHET § 3):

| H | Astra | Arkitekten | Dom |
|---|---|---|---|
| H-01, H-04 till H-07, H-09 till H-14, H-17, H-18, H-20, H-26, H-28, H-29, H-31, H-33 | met | [x] | överens |
| H-02, H-03, H-08 (s03) | waiting for owner | [ ] Q30 | överens; räknas inte som öppna fynd |
| H-15 | not met (bild 77) | [ ] | överens i sak, orsaken är 042 (motorns stale topp), inte 040:s fönster |
| H-19 | met at samples, handoff fails | [ ] | överens; plan 044 |
| H-21, H-22, H-32 | not met | [ ] | överens; se tabellen i NOTES § Loop 4 för vad som är golv och vad som är kvar i filen (042) |
| H-23 | not met numerically (giant 3,12 %, thesis 3,52 %) | [ ] | **avvikelse, Astras favör med precisering**: loop 3 bockade H-23 på cpu 1-tal ≤ 2,82 %; loop 4 mäter 3,12 % (jätten) och 3,52 % (tesfönstret, där ramarna monteras vid fönstrets start). Raden öppnas igen som bildtidens följd (korta flow-akter stegar när bildtiden faller, loop 2), inte som ett fönsterfel; ingen egen plan, 042 mäts mot den |
| H-24, H-34 | unverified | [ ] | överens (verktygsskuld; leadens grind, folden mätt 7/7 av arkitekten) |
| H-25 | partial (Calyx) | [x] med not | överens i sak: raden gäller per skärm (s4 bär ordscrubben, s5 prisliggaren, s6 irisen); Calyx-revealen är 043:s |
| H-27 | partial (Calyx) | [ ] | överens; plan 043 |
| H-30 | not met | [ ] | överens; plan 042 (inte motorn) |
| H-16 | met on supplied probe | [x] | **avvikelse i metod**: loop 4 körde `scroll_verify` själv (`probe/scroll-verify-*.txt`) |
| H-35 | supported, not rerun | [x] | **avvikelse i metod**: `geom4.json scrollW` = vw vid båda bredderna, skivorna utan horisontell scroll; reflow.py är R9:s |

Svar på frågorna 1 till 4, sammanfattat: sidan hänger ihop som en sida (foto, glyf,
ritning, typografi); det som läser som skarv är bandets entré (Q30) och processentréns
tomma högerspalt i en fångst som redan passerat prisblocket (042). Rytmen: seams 162 / 101
px håller. Balansen per skärm håller utom s03 (Q30). Rörelsen: kortet kontinuerligt (bild
52 till 75), arket kumulativt, priset och avslutets linjer läsbara; previews 1440 7 av 7;
390 01/02/03 intermittenta (042); Calyx-revealen sker inte (043); driften hoppar (044).

## ceiling

- insign: allt läsbart vid varje offset; V3c:s ritning ligger 297 px efter prosan för en läsare som inte ändrat fönsterstorlek (042).
- highwaymedia: sekvensens skelett läses tidigare än V3c:s entré i `life-01` (042).
- hoy: en auktoritet per kapitel; bandets entré har två (Q30).
- K3: en stabil kumulativ ritning; V3c:s 390-previews är ett race (042).

## material_fixes

1. **Prisblockets platshållare bort** (`index.html:731`). Mål: dokumenthöjden lika vid load
   och i bandet (10 582 / 11 326); motorns topp för `#process` = DOM:ens utan resize;
   `?preview=process-01..07` vid 390 formade 21 av 21 laddningar; ritningen i fas med
   prosan i `life-01`. **Plan 042.**
2. **Calyx-öppningen klipper och kommer uppifrån** (`index.html:677-678`). Mål:
   wrapperbakgrund synlig ≈ 100 / 50 / 0 % vid `--rv` 0 / 0,5 / 1, innehållet pixelstilla,
   identitet vid 1. **Plan 043.**
3. **Driftens leg 2 räknas från överlämningen** (`index.html:1598`, `measureAct`). Mål:
   `--sc-canvas` monotont från blå mot papper från scrollY 3 600, inget steg > 40 per kanal
   per 20 px, samma värden uppåt. **Plan 044.**

## keep

Tvåspaltsbandets offset och luft (Q30), 88 px och ordet helt, mobilordningen, grafitplanet,
wrapparnas sömn via `f.closest('.frame-wrap')`, den vägoberoende latchen med exakt 1 och
aktobjekt per tick (035), Hōrais kvadratiska iris med kontraskalad ram (036 A), monteringen i
heroens svans (036 B), `aimPreview` med generations-id (037), lägena ur shimens `cur` (039),
konturen hel på entrén (040), 24 % (038), driften skriven på `.ground` av sidan med
stoppen ur `:root` (041), kortets fulla höjd på kant, baksidans glyf, prosan synlig,
gridankaret, den kumulativa ritningen, måtten i accent, prisliggarens linjer, avslutet
ensamt på fotot, `--sc-ps`-kontraktet (staircase 0 i alla loop 4-körningar, båda
riktningarna, båda kadenserna, cpu 1 och 4). Inga nya element eller färger föreslogs av
Astra; arkitekten föreslår inga heller.
