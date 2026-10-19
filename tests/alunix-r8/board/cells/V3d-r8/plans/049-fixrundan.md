# 049 · V3d R2: fixrundan. Astras åtta material_fixes, lead tar alla åtta

- **Status**: TODO (V3d R2, en runda, den enda planerade)
- **Beställning**: `tests/alunix-r8/runs/V3d/reviews/r1-astra.md` § material_fixes, verifierade av lead mot
  pixlarna. Ordning: 1 och 2 (funktionsfel) → 3, 4, 5 → 7 → 6, 8.
- **Bindande**: ingen fix löses genom att backa ett djärvt drag från R1 (arket, siffrorna,
  rubrikerna mindre, eller scenen bort). Låst copy 15/15 ordagrant. Noll tankstreck. F-011/F-014.
  Motorn, `scroll/*.js`, `scrollcraft.css`, `sites/*` orörda. Ingen tredje iframe. Inline-hex
  ökar inte.

## Fix 1 · P13. Steg 07 ritar inget vid 1440

**Problem (Astra).** `g[data-step="07"]` ligger inuti `#p-cam`. Vid `--cam` 1 ger transformen
(translate −93px, scale 1,5, ursprung 533/247,5) x′ = 533 + 1,5·(x−533) − 93. För `p-title`
(x 24..84, y 439..493): x′ = −323,5..−233,5, y′ = 534,75..615,75 — helt utanför viewBox
0..880/0..495. Revisionsfältet finns, men syns aldrig.

**Target (Astras Expected).** Vid `?preview=process-07` ligger `#p-title`s rect innanför
`.process-sheet`s rect, och 07 skiljer sig synligt från 06.

**Fix.** Flytta `<g data-step="07">` ut ur `#p-cam`, som syskon direkt efter
`</g><!-- /#p-cam -->`, före `</svg>`. Ramen `#p-frame` gör redan exakt detta för steg 01
(motiverat i R1: "rutan skalas aldrig"); revisionsfältet får samma behandling — ett ark-fast
element, aldrig kameraskalat.

## Fix 2 · P07/P08. Arket täcker stegtexten på mobil

**Problem (Astra), mätt.** `.process-stick` ärver skrivbordsregelns `margin-top:var(--band-h)`
(202,56 px vid 390) och båda `.process-stick`/`.process-steps` står kvar i `grid-area:1/1`.
R1:s mobilblock (`@media max-width:767px`) nollade `height` och `padding-inline` (samma fynd,
lagat R1) men inte `margin-top`/`grid-area`. Stick landar 202,56 px för lågt, över
`.process-p` (idag 548 över 506..724).

**Target.** Vid `?preview=process-01..07`, 390: stick har `top:0` bokstavligen (ingen
kvarvarande margin), och överlappar aldrig `.process-p`.

**Fix.** I `@media (max-width:767px)`: `.process-stick{margin-top:0;grid-area:auto;}` och
`.process-steps{grid-area:auto;}` — separata rader i stället för överlappande grid-celler
(`.process-grid` är redan `grid-template-columns:1fr` där, så auto-placering ger två rader).

## Fix 3 · P11/P12. Den mjölkiga hinnan

**Problem.** `.process-sheet .p-live{filter:…brightness(0.6)}` (den aktiva, C-inverterade
regeln) tar taket för varje vitt vid 153/255 och gråtonar pappershuvudet och den ljusa
bottengradienten — hela steg 06/07, inte bara ritfasen.

**Target (Astras Expected).** Vid `process-06`: p95-luminans ≥ 220, pappershuvudet
≥ (225,222,214). Dämpningen hör bara till ritfasen (05).

**Fix.** `brightness(calc(0.6 + 0.4 * var(--k6)))` — vid k6=0 (steg 05) oförändrat 0,6; vid
k6=1 (steg 06 färdig) full ton 1,0.

## Fix 4 · P11/P12. Kameran lämnar kapade utrop och en guide över produkten

**Problem.** Från `--k5` skjuts måttkedja/ledare/utrop in i kameran utan att tona bort —
"16:9", "96 PX", "7 REM", "1440" kapas av arkets kant. `#p-guides` (tre lodräta hjälplinjer,
x 195,6/469,3/24, y 20..410) korsar öppningen (x 264..802) och tonar bara mot `--k6`, aldrig
mot `--k5` — synlig genom hela steg 05.

**Target (Astras Expected).** Vid `process-05/06/07` och i hjulsekvenser mellan dem: ingen
etikett eller ledare kapas av arkets kant, ingen streckad linje korsar Calyx.

**Fix.**
```css
#process{--cam-fade:calc(1 - clamp(0, var(--cam) * 4, 1));}
#p-c-gutter,#p-c-169,#p-c-row{opacity:calc(var(--p-t) * var(--cam-fade));}
#p-dim-gutter,#p-dim-row,#p-lead-169,#p-dim-width{
  opacity:calc(clamp(0,calc(var(--p-l) * 9999),1) * var(--cam-fade));}
```
`.measure`s befintliga opacitetsformel multipliceras med `var(--cam-fade)` (samma rad, inte en
konkurrerande regel — annars vinner ingen deterministiskt). `#p-guides` bryts ut ur den
delade `#p-guides,#p-ledgers,#p-hatch`-regeln (`#p-ledgers`/`#p-hatch` ligger i marginalzonen,
x 24..78/78..226, korsar aldrig öppningen x 264..802 — de behåller sin regel oförändrad) till
`opacity:calc((1 - var(--k5)) * (1 - 0.65 * var(--k6)))`. Alla formler är multiplikativa
tillägg till befintlig snäpp-opacitet (`--p-l`/`--p-t`), aldrig en ersättning — annars poppar
en linje till full ton innan den hunnit ritas klart om kameran redan rört sig.

## Fix 5 · P-genomgående. Tickerspringan visar glyffragment ("--")

**Problem, uppmätt live (Playwright, scrollY 11700, 1440).** `.step-band` är `position:sticky`
i sin egen `<li>`. När steg N:s `<li>` närmar sig sitt slut trycker sticky-mekaniken (helt
enligt spec) ut bandet uppåt förbi `top:0` i takt med att `<li>`:s underkant närmar sig —
band 06 uppmätt vid `top:-32,47px`, synlig del ends `bottom:183,5px`. Steg 07:s `<li>` börjar
exakt där (`top:183,5px`) men har INTE nått sin egen sticky-tröskel än (`top` blir 0 först vid
`li07.top<0`), så bandet står kvar i normalt flöde, synligt från 183,5px. Arket
(`.process-stick`) börjar först vid `top:216px` (`var(--band-h)`). Det lämnar en 32,5 px
spalt (183,5 till 216) där steg 07:s redan-monterade text (dämpad, `--k7`≈0) syns rakt av,
innan arket hunnit täcka den. Verifierat: `--s7` (0,8185) är matematiskt exakt det `--sc-ps`
där `li07.top` korsar 0 (samma formel som `sN=(y0+vh)/life` för N≥2) — spalten existerar
exakt i fönstret `[s7 − band_h/life, s7]`.

**Target (Astras Expected).** Inget bildruteläge mellan två band visar ett partiellt glyf
från nästa band.

**Fix.** JS (`measureAct`, samma pass som redan skriver `--band-h`): skriv även
`process.style.setProperty('--life', life.toFixed(2))` (en gång per mätning, inget nytt per
bildruta). CSS: varje `li[data-step="0N"]` (N 2–7) får utöver `--k` även `--s:var(--sN)`
(utökning av de sju redan existerande reglerna). En ny, delad regel:
```css
@media (min-width:768px){
  .process-steps li:not([data-step="01"]) .step-band{
    --slit-start:calc(var(--s) - var(--band-h) / var(--life));
    --slit-p:clamp(0, calc((var(--sc-ps,0) - var(--slit-start)) / (var(--s) - var(--slit-start))), 1);
    clip-path:inset(calc((1 - var(--slit-p)) * 100%) 0 0 0);
  }
}
```
Bandet är helt osynligt (clip 100 %) tills `--sc-ps` når `--slit-start` (`sN` minus arkets
egen höjd i liv-enheter), växer sedan linjärt till helt synligt exakt vid `sN` (där bandet per
konstruktion blir riktigt sticky). Ren funktion av `--sc-ps`, reversibel i båda riktningar,
F-014 hållen. Skopad till ≥768 där ticker-mekaniken över huvud taget finns (mobil har
`position:static`, ingen sticky-krock).

## Fix 6 · P03/P04. Tesen och jätten äger inte sina viewports

### P04, jätten
**Problem.** Den svarta plåten delar alltid skärmen med den blå tesplåten eller Calyx-ramen —
ingen skärm där den står ensam.

**Target.** Ett intervall i `.stagger` där plåten fyller ≥ 80 % vw utan att den blå panelen
eller en ram syns bredvid.

**Beslut, motiverat.** Två oberoende, additiva ändringar, den minsta kombination som ger
resultatet utan att röra `.calyx-fig`s sticky-mekanik (R1) eller Hōrai-parningen (P05, redan
"håller nivån"):
1. **Fördröj Calyx-rutans start** i `.col-left` (extra `margin-top` på `.calyx-fig`, ~600px):
   ger jätten sin första `~600px` av scroll HELT ensam i viewporten (Calyx-rutan har då
   ännu inte nått sin egen positon, bara tesen — som redan hunnit rulla bort — syns i
   col-left). Calyx kommer ikapp och parar med Hōrai precis som i R1, bara något senare.
2. **Ett bleed på `#giant-section`**, skopat `≥901px`, som läser jättens EGNA `--sc-ps`
   (samma mönster som `.thesis-figure`s redan existerande bleed): negativ `margin-left` +
   motsvarande breddökning, 0 tidigt i akten (undviker att kollidera med tesens svans, som
   fortfarande syns de första ~15 % av jättens akt) och full vid `--sc-ps` ≥ 0,5. Fullt bleed
   räknat att ge ≥ 80 % vw vid 1440 (se § Beslut nedan för talen).

### P03, tesen
**Problem, uppmätt.** Hyperborea-bilden 297 px = 20,6 % vw. `.thesis-grid`s
`minmax(28ch,.6fr)` ger text 270 px och bild bara 249 px vid 1440 — 28ch är STÖRRE än vad
`.6fr` ensam skulle ge, så minimum vinner och äter bildens spalt (motsatsen till den avsedda
0,6/1,5-fördelningen).

**Target.** Hyperborea ≥ 40 % vw i tesintervallet. Calyx och Hōrai ska fortfarande stå sida
vid sida (P05 rörs inte).

**Geometrisk gräns, uppmätt och redovisad, inte gissad.** Bildens bleed är redan idag mätt
till att sluta 7,6 px före jättens rubrik (`789px` höger kant mot rubrikens `796,8px` — samma
"5 px marginal" som filens egen kommentar om plan 017 D dokumenterar). Med textspalten
krympt till sitt minsta rimliga mått (14ch ≈ 135px, kortare gör rubriken oläslig i två-tre
ord per rad) ger den maximala säkra bredden (utan att kliva in i jättens rubrik) **530 px =
36,8 % vw** — under 40, men en nästan dubblering från 20,6 %. Byggt mot det uppmätta taket,
inte mot en gissning; talet efter bygget står i NOTES och jämförs mot 40 igen efter mätning.

**Fix.** `.thesis-grid{grid-template-columns:minmax(14ch,.5fr) 1.5fr}` (text från 28ch);
`.thesis-figure{margin-right:calc(-1 * var(--pad-i) - <uppmätt tal>px)}` (räknat mot den
uppmätta 789px-gränsen, se § Beslut); `transform:translateX(...)` behåller samma form men
omräknad så maxläget (ps=1) inte skjuter förbi 789px.

## Fix 7 · Steg 04, 06, 07 är inte egna scener

**Problem.** Vid 390 döljer mobilblocket (`#p-guides,#p-hatch,#p-ledgers,#p-dim-row,#p-c-row`)
ALLA steg 04:s tillägg — bandet byter text, arket ritar ingenting. Vid 1440 är 06 och 07
pixel-identiska (löst av Fix 1: revisionsfältet gör 07 synligt skilt). Kodan
(`.process-steps::after`, en tom `100svh - band-h` hög spacer efter listan) håller kvar det
FÄRDIGA arket en extra skärm utan att något förändras — tre visningar av samma bild i rad.

**Target.** Varje steg ändrar arket synligt, också vid 390. Kodan går bort, eller blir en
egen scen.

**Fix.**
1. Mobil viewBox (320×300, satt av `plansch()`): ge `#p-hatch`/`#p-dim-row`/`#p-c-row` egna
   mobilkoordinater i stället för att dölja dem — en liten skrafferad remsa i planschens
   vänstermarginal (samma roll som skrivbordsversionen: raddelningen), t.ex.
   `x=8,y=56,width=8,height=162` för hatchen. `#p-guides`/`#p-ledgers` (marginalzonens
   hjälplinjer) förblir dolda: deras skrivbordsposition har ingen meningsfull mobil
   motsvarighet utan att kollidera med öppningen på en 320 px bred plansch.
2. Kodan (`.process-steps::after`) tas bort (fix 1 gör 07 till en riktig, skild scen; en extra
   viloskärm av samma bild tillför inget nu).

## Fix 8 · Mobil och kroppstextsskala

| Mål | Nu | Fix |
|---|---|---|
| `.hero-headline` ≥ 46 px vid 390 | ~35 px (`min(clamp(2.2rem,9cqw,…), …)` — `9cqw` faller tillbaka mot viewport utan container-förfader, men 2.2rem-golvet vinner ändå vid 390) | Höj golvet: `clamp(2.2rem,…)` → `clamp(2.875rem,…)` (46 px), rör inget annat i uttrycket |
| `.principles .ledger--plain .ledger-body p` 20 px vid ≥ 900 | 17 px (R1) | Ny regel i den befintliga `@media (min-width:900px)`-blocket: `font-size:1.25rem` |
| `.principles > .kicker-sans` ≥ 32 px vid 390 | 11 px (ärver `.kicker-sans` — displayregeln finns bara i `@media (min-width:900px)`) | Ny basregel (utanför media-blocket): `font-size:2rem`; 900+-blockets egen `clamp(2.25rem,…)` vinner ändå vid desktop (samma specificitet, senare regel, medievillkoret gör det ömsesidigt uteslutande) |
| Mobilt ark 92 % vw (358 px) i stället för 88 % (343 px) | `.process-stick{width:min(100% - 2*var(--rail-x),560px)}` (`--rail-x`=23,4px vid 390) | `width:min(100% - 32px,560px)` — 16 px eget inset, 390−32=358 |

## Boundaries

- Motorn, `scroll/*.js`, `scrollcraft.css`, `sites/*`: orörda.
- Ingen ny `@property`. Ingen ny iframe.
- `--sc-ps`/`--kN`/`--cam` är den enda motorn för allt som rör sig (F-014); `--life` är en
  mätt konstant (skriven en gång per `measureAct`, inte per bildruta) — samma kategori som
  redan existerande `--band-h`/`--sheet-h`, inte ett nytt per-frame-skrivningsmönster.
- Låst copy rörs inte. Ingen ny synlig sträng.

## Verification

Se `PROMPT-V3d-R1.md`s grind (scroll_verify, motion_probe med kontroll, contrast_over_media,
a11y_scan, reflow, horisontell scroll, grep) plus rundans egna krav: par-bilder om **en skärm
per sida** (aldrig ihopsydda), hjulscrollsekvenser (`mouse.wheel`, inte `scrollTo`) genom hela
processakten vid 1440 och 390 var 150:e px. Varje fix mäts mot sitt Expected med skript;
kamerans transform läses ur beräknad `transform` och appliceras för hand på rektanglarna,
`getBoundingClientRect` under navigering litas inte på för det.

**Done when:** alla åtta fixar mätta mot sitt Expected (P03 mot det uppmätta, redovisade
taket om 40 % inte nås), alla PARITET-rader håller nivån i par-bilder vid 1440 och 390,
grinden ren eller varje avvikelse namngiven.
