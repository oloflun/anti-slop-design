# 048 · V3d: den inverterade varianten. Processakten blir sju scener, avslutet får priset

- **Status**: TODO (V3d R1, en runda)
- **Commit**: `runs/V3d/index.html` md5 `864c38aa8dd4e81472d45ab2ad224529` (= V3c R13). V3c rörs aldrig.
- **Beställning**: Anton 2026-09-18, punkterna A till H. Detta är golvet, inte ett förslag.
- **Ordning**: visuellt först. Planens Steps följer A till H; tekniska följdfel lagas i samma
  runda och **ett djärvt drag backas aldrig för att laga ett fel** (`RAPPORT-LOOPEN.md` fel 5).
- **Estimated scope**: 1 fil. ~220 rader CSS (varav ~60 ersätter befintliga), 7 markup-omslag
  i `<li>`, ett `<g>`-omslag i arket, en flyttad `<section>`, ~40 rader JS i `measureAct`,
  `aimOnce` och `plansch`. **Ingen ny synlig sträng.** Ingen ny iframe, ingen ny asset.
- **Mätunderlag**: `NOTES.md` § Arkitekten (Playwright-mätning av nuläget vid sex bredder och
  läsningen av 12 + 45 + 55 skärmbilder). Jämförelsetabellen är `PARITET.md`.

## Problem

Sidan i V3d ser ut som V3c: processakten är en rullande paragraf (steg 0,44 till 0,54 viewport
höga, rubrik 31,7 px, nummer 12 px, brödtext 16 px bredvid ett ark på 826 px där Calyx fyller
37 % av ytan), priset står på ett grafitplan bredvid Hōrai, och adressen i avslutet är 86 px
utan referens. Loopen efter R6 lagade fel utan att ändra kompositionen. Den här planen ändrar
kompositionen och mäter målen i skärmbilder.

## Target, en rad per beställningspunkt

Alla mål mäts i skärmbild eller `getBoundingClientRect` på den byggda sidan. Inget mål är en
tidsgräns; prestanda är en grind (§ Verification C).

| | Synligt mål | 1440 | 390 |
|---|---|---|---|
| **A** | `section#pris` ligger direkt före `footer.close`, båda på det fasta skrivbordsfotot (`.ground`), noll px mellan dem; priset är avslutets rubrik | pris + adress i sidans två sista viewports | samma |
| **A** | kontrast över fotot (`contrast_over_media --url`, ljusaste 5 %) | brödtext ≥ 4,5:1, statement och priser ≥ 3:1 | samma |
| **B** | adressens font-size / glyfhöjd på `k` (stapelns topp till baslinjen, skärmbild) | **46 px / 32 till 35 px** (i dag 86,4 / ~62) | **28 px / 19 till 21 px** (i dag 32) |
| **C** | `#process` bakgrund utan parameter | `--c-drafting` = oklch(0,21 0,022 250) ≈ `#111922` | samma |
| **D** | `#giant-section` bakgrund / bläck | `--c-black` / `--c-paper`, kant `--frame-line` | samma |
| **E** | arkets renderade bredd | **≥ 1 100 px = 76 % vw**, förväntat 1 120 till 1 180 (i dag 826 = 57 %) | **≥ 358 px = 92 % vw** |
| **E** | Calyx-bildens synliga rektangel ÷ arkets rektangel | `?preview=process-05` ≥ 50 %, `-06`/`-07` **≥ 80 %** (i dag 37 %) | `-05` ≥ 50 %, `-06`/`-07` ≥ 55 % (i dag 36 %) |
| **E** | Calyx i pixlar vid `?preview=process-07` | ≥ 960x540 (i dag 505x284) | ≥ 330 px bred |
| **F** | varje steg äger ≥ 1 viewport: scroll mellan två bands landning | ≥ 900 px (band + 90svh ≈ 1 026) | steg + ark ≥ 844 |
| **F** | stegnummer (displaysiffra) font-size | **≥ 150 px** (clamp → 168) | **≥ 80 px** (86) |
| **F** | stegrubrik font-size | **≥ 48 px** (52) | **≥ 32 px** |
| **F** | brödtext i akten | 17 px, radavstånd 1,6, 78 % papper (9,95:1) | 16 px |
| **F** | rörelse, minst två lager, scrubbat i båda riktningarna | band-ticker + arkets ritning + siffra/rubrik-ljus + kamera (05 till 07) | ark + siffra/rubrik-ljus + kamera |
| **G** | inget hål där priset låg | vänster spalt vid Hōrai visar Calyx sticky, `blankBands` 0 i `.stagger` | staplat, inget glapp > 120 px |
| **G** | ljuset finns kvar | "Hur vi tänker" helbredd papper, Calyx live, bildtexterna, Calyx i färg i 05 till 07 | samma |
| **H** | varje rad i `PARITET.md` | "håller nivån" i en par-bild | samma |

## Tokens (gate 48: allt nytt i `:root`, aldrig inline-hex)

Lägg bredvid `--c-accent-on-dark` (rad 139):

```css
/* PLAN 048 C. Processaktens grund i V3d: ritbordet i mörker. Kall
   blåsvart, chroma 0,022 (grafiten har 0,012) - läser som ett eget
   material mot både fotot och jättens svarta plåt, blir aldrig en
   andra accent. Räknat: --c-paper 15,8:1, --c-accent-on-dark 4,67:1
   (44 px fet siffra, stor text, golv 3:1), 62 % papper 6,7:1,
   78 % papper 9,95:1. Mät om på pixel. */
--c-drafting:oklch(0.21 0.022 250);
/* PLAN 048 A. Scrimmen under pris och adress på skrivbordsfotot. */
--scrim-close:color-mix(in srgb, var(--c-black) 64%, transparent);
```

## Steps

### A · Priset flyttas ned till avslutets fotografiska grund

1. **Flytta markup.** Klipp hela `<section class="price panel-pad" id="pris" data-sc-act="flow">`
   (rad 1285 till 1303, inklusive kommentaren `<!-- s6 vänster. Priset ... -->`) ur
   `.col-left` och klistra in den **sist i `<main>`**, efter `</section>` för `#principer` (rad
   1573) och före `</main>` (rad 1589). `footer.close` ligger kvar utanför `<main>`
   (contentinfo-landmärket, se kommentaren rad 1576 till 1586). Innehållet i sektionen rörs
   inte ett tecken.
2. **Ta bort** `.price{order:5;}` i `@media (max-width:900px)` (rad 582): priset är inte längre
   ett flexbarn i `.stagger`.
3. **Ersätt** `.price{background:var(--c-graphite);...}` (rad 740 till 741) och
   `.price .statement{...}` (746 till 748):

```css
/* PLAN 048 A: priset är avslutets rubrik och står på samma fotografiska
   grund som adressen. Ingen egen yta: .ground syns igenom, scrimmen
   bär kontrasten (gate "type over media only on a plate or scrim"). */
.price{position:relative;isolation:isolate;background:none;color:var(--invert-ink);
  padding:clamp(120px,18svh,200px) var(--rail-x) 0;}
.price::before,.close::before{content:"";position:absolute;inset:0;z-index:-1;
  pointer-events:none;
  background:linear-gradient(90deg,var(--scrim-close) 0,var(--scrim-close) 58%,transparent 92%);}
.price .statement{font-family:var(--font);font-weight:300;
  font-size:clamp(2.75rem,6vw,6rem);line-height:1;letter-spacing:-.02em;
  max-width:14ch;text-wrap:balance;}
.price-ledger{margin-top:clamp(40px,6svh,64px);max-width:min(100%,1040px);}
.price-row .value{font-family:var(--font);font-weight:300;
  font-size:clamp(1.5rem,2.6vw,2.5rem);letter-spacing:-.01em;}
```

   `.price-row .value` ersätter befintlig deklaration (rad 767 till 768); `.price-ledger` får
   bara `margin-top` och `max-width` bytta (rad 754), resten står. `.price-row .label` blir
   `font-size:1.0625rem` (17 px). Vid `max-width:767px` blir scrimmen heltäckande:
   `.price::before,.close::before{background:var(--scrim-close);}`.
4. **Avslutet blir kortare** (rad 1135 till 1138): `min-height:100svh` bort; `padding:
   clamp(56px,8svh,96px) var(--rail-x) clamp(96px,16svh,180px)`; `justify-content:flex-start`;
   lägg `isolation:isolate`. Priset och adressen läses som en sammanhängande avslutning:
   statement, liggare, hårlinje, adress.

### B · Adressen till en motiverad storlek

5. `.close-mailto` (rad 1142 till 1147): `font-size:clamp(1.75rem,3.2vw,3rem)` ger 46,1 px vid
   1440, 41 vid 1280, 32,8 vid 1024, 28 vid 768/390/320. **Motivering mot referenserna:** hoy
   sätter kapitelrubriker i ~46 px vid 1440 (hoy-home s06 "DIGITALA LÖSNINGAR") och sin kontakt
   i brödstorlek; insign-390 s10 avslutar med sin fråga i ~28 px. Adressen är en handling, inte
   en rubrik: den tar kapitelrubrikens storlek och lämnar displayskalan åt `Alla har rätt till
   bra design.` (86 px vid 1440, kvot 1,9). Understrykningen och `min-height:44px` står kvar.
   Vid 320 mäter strängen ~240 px: ryms utan brytning (gate 49).

### C · Processakten inverterad som standardläge

6. Skriv om 045:s block (rad 1047 till 1083) så att det gäller utan parameter och **bara**
   `#process`. `.principles` tas ur blocket och står kvar på papper (beslut G2):

```css
#process{
  --bg:var(--c-drafting); --ink:var(--c-paper);
  --c-line-on-paper:var(--hairline-dark);
  --c-accent:var(--c-accent-on-dark);
  --hair-ink:color-mix(in srgb, var(--c-paper) 62%, var(--c-drafting));}
#process .process-lead,#process .process-p{
  color:color-mix(in srgb, var(--c-paper) 78%, var(--c-drafting));}
#process .process-sheet .p-live{
  filter:grayscale(calc(1 - var(--k6))) contrast(1.05) brightness(0.6);}
```

   Ta bort JS-raden `if (proc === 'invert') ...` och `var proc = ...` (rad 2056 till 2060)
   med kommentar: `?process=` läses inte längre. `brightness(0.6)` är 046:s mätta värde mot
   svart; mät om mot `--c-drafting` med den större bilden (steg E) och skriv talet i NOTES.
   Lead dömer lampeffekten på par-bilden, inte på talet.

### D · Jättesektionen inverterad

7. `#giant-section` blir kortets baksida, samma material som `.face--back`:

```css
/* PLAN 048 D. Jätten på kortets material: svart plåt, papperets bläck,
   samma hårlinjekant som plåten i heron. Tokenbyte som i C. */
#giant-section{
  --bg:var(--c-black); --ink:var(--c-paper);
  --c-line-on-paper:var(--hairline-dark);
  border:1px solid var(--frame-line);}
#giant-section .giant-sub,#giant-section .ledger-body p{
  color:color-mix(in srgb, var(--c-paper) 72%, var(--c-black));}
#giant-section .ledger-num{
  color:color-mix(in srgb, var(--c-paper) 62%, var(--c-black));}
```

   `.panel-giant` läser redan `background:var(--bg);color:var(--ink)`; `.thread`,
   `.thread-fill`, `.ledger`, `.ledger-row` och ordscrubbens gradient läser `--ink`/`--bg`/
   `--c-line-on-paper` och vänder med tokens. Jätterubriken står kvar på `clamp(2.1rem,7.4vw -
   18px,5.5rem)` (plan 030); ingen storlek backas.

### E · Arket kraftigt större, Calyx fyller rutan

8. **Arkets storlek** (layout i F): vid ≥ 768 är arket sidans scen, `width:min(100%,
   calc((100svh - var(--band-h) - clamp(18px,3svh,32px)) * 880 / 495))`. Förväntat: 1440x900
   med `--band-h` 210 till 240 → 1 120 till 1 180 px (78 till 82 % vw), 1280x800 → ~980 (77 %),
   1024x768 → ~810 (79 %, bandet ~290), 768x1024 → 676 (88 %). Bandets höjd styrs av det längsta stycket
   (steg 03, ~430 tecken): 66 ch i 17 px ger 6 till 7 rader. **Krymp aldrig texten för att
   vinna arkyta**; vinn den på bandets spaltbredd.
9. **Kameran.** Omslut allt ritat utom `#p-outline` i en ny `<g id="p-cam">` direkt efter
   `</defs>`. `#p-outline` flyttas ut ur `g[data-step="01"]` till en egen
   `<g data-step="01" id="p-frame">` FÖRE `#p-cam` (den ramen skalas aldrig, "rutan" står);
   `#p-glyph` stannar i `#p-cam` i en `g` utan `data-step` (den döljs redan av sin
   snäppopacitet tills `--k1` ≥ 0,30). `sheetGroups` indexeras per `data-step`: läs **alla**
   grupper per steg (`querySelectorAll('g[data-step="01"]')`) och växla `data-on` på varje,
   annars tappas den ena gruppen. Paint-ordningen inne i `#p-cam` är oförändrad (05 först).

```css
/* PLAN 048 E. Kameran: ritningen skjuts in mot öppningen när materialet
   kommer (05) och när ritningen blir sida (06). Ramen #p-frame står
   still; bara innehållet rör sig. Läser --k5/--k6 (F-014 via --sc-ps). */
#process{--cam:clamp(0, 0.35 * var(--k5) + 0.65 * var(--k6), 1);}
#p-cam{transform-box:view-box;transform-origin:533px 247.5px;
  transform:translate(calc(-93px * var(--cam)),0) scale(calc(1 + 0.5 * var(--cam)));}
```

   533 / 247,5 är öppningens mitt ((264+802)/2, (96+399)/2); −93 flyttar den till arkets mitt
   (440). Vid `--cam` = 1 är öppningen 807x455 av 880x495 = **84 %** av arkets yta; vid
   `?preview=process-05` (`--cam` 0,35) 632x356 = **52 %**. Allt utanför öppningen skjuts ut ur
   arket och klipps av `<svg>`:s egen overflow; det är avsikten (06:s not: "Ritningen och
   sidan är samma sak").
10. **Mobilens plansch blir 320x300** (i dag 320x360), så att öppningen tar mer av ytan.
    I `@media (max-width:767px)` (ersätter `max-width:1279px`, rad 1088):

```css
#p-outline{d:path("M0.5 0.5 H319.5 V299.5 H0.5 Z");}
#p-opening{d:path("M16 68 H304 V230 H16 Z");}
#p-open-rect,#p-live-img{x:16px;y:68px;width:288px;height:162px;}
#p-dim-width{d:path("M0 286 H320");}
#p-lead-169{d:path("M304 68 L296 60 H200");}
#p-dot-169{cx:304px;cy:68px;}
#p-title{d:path("M208 16 H304 V52 H208 Z M208 28 H304 M208 40 H304");}
#p-rev{x:208px;y:16px;width:96px;height:12px;}
#p-cam{transform-origin:160px 149px;transform:scale(calc(1 + 0.08 * var(--cam)));}
.process-sheet{aspect-ratio:320/300;}
```

    Och i JS (`plansch`, rad 2178 till 2189): `matchMedia('(max-width: 767px)')`, viewBox
    `'0 0 320 300'`, `MOBILE_TEXT` mobilvärden: `p-m320` [71, 276], `p-m768` [171, 276],
    `p-m1440` [304, 276], `p-c-169` [196, 64], `p-c-rev` [256, 26]. Skrivbordsvärdena i
    `MOBILE_TEXT` rörs inte. Öppningen 288x162 av 320x300 = 48,6 %, med kameran 1,08 = 56,7 %.
    **Kontroll:** inga två av `#p-glyph`, `#p-title`, `#p-c-169`, `#p-m320`, `#p-m768`,
    `#p-m1440`, `#p-opening` får ha överlappande `getBBox()` vid 390 (skriv ut dem).

### F · Varje fas en scen

Formen, i en mening: **arket är en sticky scen i nederkanten av skärmen, stegtexten står i ett
sticky band ovanför, och varje nytt band stiger upp bakom arkets överkant och skjuter det förra
ut ur bild.** Texten ligger kvar i flödet i `<ol>`-ordning (PageDown, skärmläsare, plan 019:s
a11y-skäl), men varje steg äger sin skärm.

11. **Markup, sju `Edit`.** I varje `<li data-step="0N">`: omslut barnen med
    `<div class="step-band">…</div>`, och ge `<span class="ledger-num">` attributet
    `aria-hidden="true"` (`<ol>` bär ordningen för skärmläsaren). Ingen text ändras.
12. **Kapitelskärmen** (hoy-home s03): `.process{padding-block:clamp(120px,22svh,240px) 0}`,
    `.process-title{font-size:clamp(2.75rem,7.2vw,7.5rem);line-height:.95;max-width:14ch;
    letter-spacing:-.03em}` (104 px vid 1440), `.process-lead{font-size:1.0625rem;
    margin-bottom:clamp(96px,16svh,180px)}`, och `.process-grid{margin-top:0}`.
13. **Scenen, ≥ 768** (ersätter `.process-grid`, `.process-steps`, `.process-steps li`,
    `.process-step-title`, `.process-p`, `.process-note`, `.process-stick`, `.process-sheet` på
    rad 887 till 908):

```css
/* PLAN 048 F. INTE en rullande paragraf bredvid ett litet ark: en scen
   per steg. --band-h skrivs av measureAct (högsta .step-band), fallback
   nedan. */
#process{--band-h:clamp(200px,24svh,240px);}
.process-grid{display:grid;grid-template-columns:minmax(0,1fr);}
.process-stick{grid-area:1/1;align-self:start;position:sticky;
  top:var(--band-h);margin-top:var(--band-h);height:calc(100svh - var(--band-h));
  z-index:2;background:var(--bg);display:flex;align-items:center;justify-content:center;
  padding:clamp(6px,1svh,12px) var(--rail-x) clamp(12px,2svh,20px);}
.process-sheet{display:block;height:auto;max-width:none;aspect-ratio:880/495;
  width:min(100%,calc((100svh - var(--band-h) - clamp(18px,3svh,32px)) * 880 / 495));}
.process-steps{grid-area:1/1;z-index:1;list-style:none;margin:0;padding:0;}
/* Kodan: arket står kvar färdigt i en skärm efter att band 07 lämnat. */
.process-steps::after{content:"";display:block;height:calc(100svh - var(--band-h));}
.process-steps li{min-height:calc(var(--band-h) + 90svh);padding:0;}
.step-band{position:sticky;top:0;height:var(--band-h);background:var(--bg);
  display:grid;grid-template-columns:auto max-content minmax(0,42rem);
  column-gap:clamp(24px,3vw,56px);align-items:start;
  padding:clamp(20px,3svh,32px) var(--rail-x) clamp(12px,2svh,20px);
  border-bottom:1px solid var(--c-line-on-paper);}
#process .ledger-num{font-family:var(--f-display);font-weight:700;
  font-size:clamp(5rem,11.7vw,10.5rem);line-height:.8;letter-spacing:-.04em;
  font-variant-numeric:tabular-nums;padding:0;}
.process-step-title{font-family:var(--f-display);font-weight:700;
  font-size:clamp(2rem,3.6vw,3.25rem);line-height:.95;letter-spacing:-.02em;
  text-transform:uppercase;color:var(--ink);}
.process-p{font-family:var(--font);font-weight:300;font-size:1.0625rem;
  line-height:1.6;max-width:66ch;}
.process-note{font-weight:600;font-size:13px;color:var(--hair-ink);
  max-width:28ch;margin-top:.8rem;}
@media (max-width:1023px) and (min-width:768px){
  .step-band{grid-template-columns:auto minmax(0,1fr);row-gap:16px;}
  .step-band .process-p{grid-column:1 / -1;}
}
```

    `.process-note` står i andra spalten under rubriken: flytta den i markup? **Nej.** Placera
    med grid: `.step-band > .process-step-title{grid-column:2}`, `.step-band >
    .process-note{grid-column:2;grid-row:2}`, `.step-band > .process-p{grid-column:3;
    grid-row:1 / span 2}`, siffran `grid-row:1 / span 2`. DOM-ordningen (nummer, rubrik,
    stycke, not) är oförändrad.

    Varför ticker-effekten uppstår av sig själv: bandet för steg N är sticky i sitt eget `<li>`.
    När `<li>` N+1 når bandets underkant ligger dess band direkt under band N och under arkets
    ogenomskinliga scen (z-index 2); de två banden rör sig upp tillsammans, N ut ur bild, N+1
    fram ur arkets överkant. Det är ren scroll, pixelbundet, i båda riktningarna, utan en
    enda skrivning per bildruta. Sticky-intervallet per steg är 90svh (810 px vid 900) och
    alltså längre än Chromes PageDown (787 px vid 900): PageDown kan inte hoppa över ett steg.

14. **Siffran och rubriken tänds med steget** (lager 2, läser `--kN` alltså `--sc-ps`):

```css
.process-steps li[data-step="01"]{--k:var(--k1);}
/* ... 02 till 07 likadant ... */
#process .step-band .ledger-num{
  color:color-mix(in srgb, var(--ink) calc(62% + 38% * var(--k)), var(--bg));
  letter-spacing:calc(0.04em - 0.08em * var(--k));
  transform:translateY(calc((1 - var(--k)) * 0.08em));}
#process .step-band .process-step-title{
  --edge:calc(var(--k) * 130%);
  background-image:linear-gradient(100deg,var(--ink) 0 calc(var(--edge) - 12%),
    color-mix(in srgb,var(--ink) 62%,var(--bg)) calc(var(--edge) + 12%) 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;}
```

    Båda ändarna är läsbara (62 % papper mot `--c-drafting` = 6,7:1). Ingen `opacity` på text.
15. **Mobilen, < 768.** Arket sticky överst som i dag (`.process-stick{order:-1;position:
    sticky;top:0;z-index:2;background:var(--bg);padding-block:12px;width:min(100% - 2 *
    var(--rail-x),560px);justify-self:center}`), stegen i flödet under det, `.step-band`
    **inte** sticky (`position:static;height:auto;display:block;border:0`), `.process-steps
    li{min-height:calc(100svh - var(--sheet-h));padding-block:clamp(24px,4svh,40px)}` med
    `--sheet-h` skrivet av `measureAct` (arkets `getBoundingClientRect().height`),
    `.process-steps::after{display:none}`, `.process-steps` behåller sin bottenpadding
    `clamp(160px,22vh,220px)`. Siffran `font-size:clamp(4.5rem,22vw,6rem)` (86 px vid 390),
    rubriken `2rem`. `.process-steps{width:min(100%,560px)}` och `justify-self:center`.
16. **JS, `measureAct`** (rad 1827 till 1881):
    - brytpunkten `(max-width:1279px)` → `(max-width:767px)`, på alla tre ställen (rad 1844,
      2097, 2180);
    - **först** (≥ 768): `bandH = max(.step-band.scrollHeight)` över de sju, avrundat uppåt,
      skrivet som `--band-h` på `#process` (skrivs bara om det ändrats); vid < 768 skrivs
      `--sheet-h` i stället;
    - **sedan** li-rektanglarna (de beror på `--band-h`);
    - ankare vid ≥ 768: `s1 = (y0 + 0.5 * vh) / life`, `sN = (y0 + vh) / life` för N ≥ 2,
      `eN = (y0 + 1.6 * vh) / life`. Alltså: steget ritar under de första 60 % av sitt
      sticky-intervall och står färdigt de sista 30 %. Mobilformlerna står kvar som de är.
    - `aimOnce` (rad 2103 till 2105): vid ≥ 768 `target = stepAnchors[pi].y0 + 0.6 * vh`
      (ger `--sc-ps` = `eN` per konstruktion); mobil oförändrad.

### G · Balansen efter flytten

17. **Bandet där priset låg.** Vänsterspalten tappar 729 px vid 1440 (priset 567 + gap 162).
    I stället för ett hål hålls **Calyx sticky** i vänsterspalten medan jätten och Hōrai
    passerar till höger: `.calyx-fig{flex:none;position:sticky;top:clamp(24px,5svh,48px);}`
    (ersätter `.calyx-fig{flex:1;}`, rad 654). `.calyx-wrap` behåller `min-height:90dvh`. Ramen
    transformeras eller tonas inte av detta (sticky är ingen transform; PRODUCT.md håller). Vid
    `max-width:900px`: `.calyx-fig{position:static}`. Resultat vid Hōrai-skärmen: två levande
    sajter sida vid sida, som insign-1440 s04 (två arbeten, 94 % vw tillsammans).
18. **Var ljuset finns kvar** (beslutet, motiverat i § Beslut G nedan): "Hur vi tänker" står
    kvar på papper, helbredd, som sidans enda helbredds tonala inversion; bildtexterna under
    ramarna står kvar på papper; Calyx live bär ljus i stagger-bandet; Calyx får färg i
    05 till 07. "Hur vi tänker" väger upp sin högra halva: `.principles` blir en tvåspaltig
    grid ≥ 900 (`grid-template-columns:minmax(0,5fr) minmax(0,7fr)`), kickern "Hur vi tänker"
    sätts i displaystorlek i vänsterspalten (`font-family:var(--f-display);font-weight:700;
    font-size:clamp(2.25rem,4.4vw,4.25rem);letter-spacing:-.02em;text-transform:none`, samma
    text, samma element), liggaren i högerspalten med `h3` i `clamp(1.25rem,1.8vw,1.6rem)` och
    brödtext 17 px. Det är hoy-webb s04:s form: rubrik vänster, text höger, papper i full bredd.

### H · Jämförelsen

19. Skjut skivor och par-bilder enligt `PARITET.md` och laga det som inte håller nivån i samma
    runda (se `PROMPT-V3d-R1.md` § 3).

## Device-tabell

| Bredd | Stagger-bandet | Processakten | Arket (förväntat) | Avslutet |
|---|---|---|---|---|
| **1440x900** | två spalter; Calyx sticky vänster, jätten svart + Hōrai höger | band 210 till 240 px sticky överst, scen under; kod en skärm | 1 120 till 1 180 bred (78 till 82 %) | statement 86 px, priser 37 px, adress 46 px |
| **1280x800** | som 1440 | band ~210 | ~980 (77 %) | 77 / 33 / 41 |
| **1024x768** | två spalter (brytpunkten är 900) | band 3 spalter, stycket ~445 px brett, band ~290 | ~810 (79 %) | 61 / 27 / 33 |
| **768x1024** | staplat (≤ 900): tes, Calyx, jätten, Hōrai | band 2 rader (siffra + rubrik / stycke), ~320 | 676x380 (88 %) | 46 / 24 / 28 |
| **390x844** | staplat | mobil: plansch 320x300 sticky överst, stegen under | 358x336 (92 %) | 44 / 24 / 28 |
| **320x568** | staplat | mobil | 288x270 (90 %) | 44 / 24 / 28 |

200 % zoom vid 1440 = 720 css-px: mobilvägen. Noll horisontell scroll 320 till 1440, mätt på
elementens rektanglar (gate 34), inte på `scrollWidth`.

## `?preview=`

- `process-01` till `-07`: siktar på `eN` enligt steg 16. Vid ≥ 768 visar bilden band N överst
  med siffran full ton och rubriken tänd, och arket i steg N:s formade läge; `-05` visar
  kameran på 0,35, `-06` och `-07` på 1. Mobil: som i dag. `--sc-ps` = `--eN` ± 0,0001 vid 1440
  och 390, tre laddningar per läge vid 390.
- `front`, `mid`, `back`, `ledger`, `bleed`: oförändrade. `ledger` visar nu den svarta jätten.
- `?process=invert` läses inte längre (akten är inverterad utan parameter).

## Beslut G, med skäl i pixlar

1. **Priset lämnar ett hål på 729 px vid 1440; det fylls med en hållning, inte med en ny
   yta.** Tre kandidater prövades mot mätningen: (a) Calyx `flex:1` som i dag skulle sträcka
   ramen till 1 578 px höjd på 651 bredd (kvot 2,4, en porträttremsa av en liggande sajt);
   (b) att flytta Hōrai till vänster lämnar samma hål till höger; (c) Calyx sticky: ramen
   behåller sina 849 px och står i bild genom hela högerspaltens passage. (c) valt: noll ny
   yta, noll ny text, och bandet blir två levande sajter bredvid varandra.
2. **"Hur vi tänker" förblir papper.** Med processen på `--c-drafting` (≈ 7 till 8 viewports
   vid 1440) och jätten på svart är det enda helbredda ljusa fältet mellan heron och avslutet
   annars borta, och sidan läses som en massa. Papperet står direkt efter aktens kod och före
   avslutets foto: mörk ritning, papper, fotografi, alltså tre material i följd (H-03, H-06).
   045 inverterade principerna tillsammans med akten; beställningen C gäller processakten,
   inte principerna.
3. **Tre mörka material, inte ett.** Fotot (neutralt grått, L ~0,15 till 0,35 efter
   `brightness(.5)`), jättens svarta plåt (`#0b0c0e`, med `--frame-line` som heronkortet) och
   ritbordet (`--c-drafting`, kall blåsvart). De ligger aldrig kant i kant utan en ram eller ett
   foto emellan, och de läser som tre ytor, inte en.
4. **Ljusbudget, mätt av byggaren:** helsidesbilden vid 1440 i skivor om 900 px; per skiva
   andelen pixlar med relativ luminans > 0,5. Förväntat: ingen följd av fler än fyra skivor
   under 3 %, och "Hur vi tänker" > 50 %. Lead dömer på strippen och par-bilderna, inte på
   talet.

## Repo conventions

- Motorn `scroll/scrollcraft.js`, `scrollcraft.css`, `scroll/sc-smooth.js` och `sites/*` orörda.
  `@property`-registreringen av `--sc-ps` (i shimen) orörd; inga nya `@property`.
- F-011: ingen `prefers-reduced-motion`, ingen statisk fallback. F-014: allt som rör sig läser
  `--sc-ps` via `--kN`/`--cam`; rå `--sc-p` driver ingenting.
- Låst copy ordagrant (PRODUCT.md § Brand Commitments), de sju processtyckena och noterna
  ordagrant. Ingen ny synlig sträng. Gate 75: noll tankstreck.
- Gate 47/79: Calyx i arket är en riktig produktyta. Ingen tredje iframe.
- Radie 0. Inga skuggor. Accenten `#1e5e9c` fortfarande exakt två förekomster (tesen, "Boka ett
  möte"); `--c-accent-on-dark` på måttsiffrorna är samma roll mot en annan grund (045).

## Boundaries (STOPPA och skriv i NOTES)

- En ändring skulle kräva att en låst sträng ändras eller flyttas ut ur sin sektion.
- Kameran eller bandet kräver JS per bildruta för att fungera.
- `sheetGroups`-ändringen gör att en grupp aldrig får `data-on` (kontrollera alla sju steg
  vid 1440 och 390 med `?preview=`).

## Verification

**A. Synligt, det som avgör.** `PARITET.md`: skivor vid 1440 och 390, par-bild per rad, och
varje rad bedömd "håller nivån" eller lagad. Plus tabellen ovan, rad för rad, med uppmätt värde.

**B. Mätt.**
- E: `getBoundingClientRect` på `#processSheet` och på `#p-live-img` (klippt mot
  `#p-open-rect`, alltså skärningen av de två rektanglarna) vid `?preview=process-05/06/07`,
  1440 och 390. Kvoten skriven.
- F: `getComputedStyle` font-size på `#process .ledger-num`, `.process-step-title`,
  `.process-p`; li-höjder; tolvstegs ramsekvens genom steg 03 till 04 vid 1440, **ned och upp**,
  med siffrans `color` och bandens `top` utskrivna per ram (monotont i båda riktningarna).
- B: glyfhöjden på `k` i `kontakt@alunix.se` ur skärmbilden (kolumnskanning av den första
  glyfens bläck), 1440 och 390.
- A/C/D: `contrast_over_media.py --url` på prisets och adressens strängar (scroll till
  `#pris` och till dokumentets slut), på akten (`?preview=process-02` och `-06`) och på jätten
  (`?preview=ledger`), 1440 och 390. Brödtext ≥ 4,5:1, stor text ≥ 3:1.
- G: ljusbudgeten per skiva (§ Beslut G punkt 4); `scroll_verify` `blankBands` i `.stagger`
  = 0. `blankBands` inne i `#process` i helsidesfångsten är en artefakt av den sticky scenen
  (fångsten visar scenen en gång); de redovisas och döms på skivorna.

**C. Grinden (inte målet).** `scroll_verify` 1440 och 390; `motion_probe` med
kontrollprotokollet (`tests/motion/smooth.html` ren först), `#process:--sc-ps` ned och upp,
cpu 1 och 4, staircase 0, `max_step` ≤ 3 % på `--sc-ps`; `a11y_scan` + `reflow` vid 390 och
768; `tab_walk`; noll horisontell scroll 320 till 1440; grep: `prefers-reduced-motion` 0,
U+2012 till U+2015 0 i synlig text, inline-hex utanför `:root` inte fler än före (arkitektens räkning: 16 i CSS utan kommentarer, 8 i markup/JS).

**Done when:** varje målrad ovan har ett uppmätt värde som når målet, varje rad i `PARITET.md`
håller nivån i sin par-bild, och grinden är ren eller varje avvikelse namngiven med skäl.
