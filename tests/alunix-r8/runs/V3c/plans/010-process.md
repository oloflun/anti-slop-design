# 010 · Processakten "Ritningen" i V3c

> **Rättelse 2026-09-16 (arkitekten, efter R5).** Tre delar av den här planen är
> ersatta och står kvar nedan bara som historik:
> 1. **§ Målbild s-process-03 anger ett falskt mått.** Måttlinjen `#p-dim-gutter` som
>    planen ritar från x 226 till 270 är 44 units = 72 px = **4,5 rem**, inte 7 rem (arkets
>    skala 880 units = 1 440 px). Astra-granskningen R5 fynd 5. Rättad geometri: öppningen
>    flyttas till x 264 så att avståndet från 320-stationens hjälplinje (195,6) är 68,4 units
>    = 111,9 px ≈ 7 rem. Se `plans/020-arkets-geometri-och-utrop.md` § Target A.
> 2. **§ Copyutkast v0 (fråga och svar) är ersatt av copy v1** ur `PROCESS-UNDERLAG.md` § 3
>    (ett stycke per steg), Antons dom 2026-09-16. Se `plans/019-processakten-prosa-i-flodet.md`.
> 3. **Formen (sticky ark med absolut positionerade, korsfadade stegtexter) är ersatt** av
>    stegen som prosa i flödet med arket sticky bredvid (≥ 1280) eller ovanför (≤ 1279), och
>    fönster ankrade i stegens läge. Skäl: a11y F-03/F-05, Astra 8, leadens F-007 vid 390.
>    Se plan 019.
>
> Byggaren följer 019 och 020; den här filen läses för tokens, device-principer och
> banornas inventarium, inte för geometri eller copy.

- **Status**: SUPERSEDED av 019 och 020 (byggd i R5 som skriven; formen och copyn byts i R6)
- **Commit**: b2e1ecd (boardkopian `board/cells/V3c-r8/index.html`, 991 rader, identisk med `runs/V3c/index.html` vid dispatch)
- **Severity**: HIGH (Antons beställning 2026-09-15; H-02, H-06, H-28 till H-33 i `HELHET.md`)
- **Category**: Missed opportunity (ny akt) + Cohesion & tokens
- **Estimated scope**: 1 fil (`index.html`: ~90 rader CSS, ~120 rader markup, ~25 rader JS), 1 asset (`assets/demo-calyx-1440.webp`, finns i cellen)

Skriven av arkitekten. Byggaren har noll kontext utöver den här filen, `HELHET.md` § 3 och
`BRIEF.md`. Varje värde står här. Motorn `scroll/*.js` redigeras aldrig; `.sc-*` restylas
aldrig; ingen tredje live-iframe; F-011: ingen rörelsepreferens läses.

## Problem

Sidan beskriver processen med tre liggarrader (01 Design, 02 Utveckling, 03 System) i
`#giant-section`, `index.html:748-773`. Det är tjänsterna, inte hur ett projekt går till.
Referenserna gör det bättre: Highway Media har en lodrät tidslinje med fyra namngivna
faser (`shots/fasA/highway-1440/hw-goteborg-1440--s03.png`), Insign skriver löftena
(testadress, CMS) i klartext (`insign-1440--s01.png`), Hoy listar sex arbetsprinciper
(`hoy-webb-1440--s08.png`). V3c saknar en akt som svarar på kundens frågor om hur det går
till, och efter heron finns bara ett tvåspaltigt band (H-02) med två anatomier (H-06).

K3:s ritning (`board/cells/K3-r8/index.html:676-860`) har formen: en sektionsritning som
ritar sig ur `--sc-ps`, måttsatt med sanna tal, som sedan blir sidan. Den lånas som
**form** (kontur, måttlinje, hjälplinje, skraffering, utrop), aldrig som sida.

## Target

En ny full-bredd sektion `#process` på papper (`var(--bg)`), placerad **efter**
`</div><!-- .stagger -->` (`index.html:787`) och **före** `<footer class="close"`
(`index.html:801`), `data-sc-act="flow"` (heron är sidans enda `pin`). Sektionen är
300 svh hög; inne i den ligger ett ark (SVG, viewBox `0 0 880 495`, 16:9) som är
`position: sticky` mitt i viewporten och ritas i sju tillstånd medan sektionen passerar,
plus en vänsterspalt med stegindex, titel, kundfråga och svar, cued på `--sc-ps`.

### Målbild skärm för skärm, 1440x900

Arket: 880 x 495 px, x från 480 till 1360 (samma öppning som K3:s ritning), `top: 202px`
i vila (`(900 - 495) / 2`). Vänsterspalten: x från `--rail-x` (86) till 470, vertikalt
centrerad på arket. Aktens `--sc-ps` löper över sektionens synliga liv (3 600 px vid 900
vh: 2 700 höjd + 900). Arket är helt i vy och stilla från ps 0,19 till 0,81.

| Skärm | ps-fönster | Displayelement | Vad som ritas (banor, klass) | Sant mått som står | Text i vänsterspalten |
|---|---|---|---|---|---|
| s-process-01 Uppstart | 0,19 till 0,28 | arkets kontur | `#p-outline` (contour 1,5 px, medurs från övre vänstra hörnet), ordmärkets A-glyf som `#p-mark` (hairline-kontur, 36 units hög, x 24 y 24) | inget (författad tystnad) | `01` · Uppstart · fråga + svar |
| s-process-02 Planering | 0,28 till 0,37 | måttkedjan under arket | `#p-guides` (tre streckade lodräta hjälplinjer vid x 195,6 och 469,3 samt 24 = 320/1440, 768/1440 och marginalen av arkbredden), `#p-dim-width` (måttlinje y 470, x 0 till 880, pil i båda ändar), `#p-stations` (streck vid 195,6 och 469,3), måttsiffrorna `320` `768` `1440` i display 44 px | **320 · 768 · 1440** | `02` · Planering |
| s-process-03 Design | 0,37 till 0,46 | öppningens kontur | `#p-opening` (contour, rect x 270 y 96 w 538 h 303 = 16:9), `#p-dim-gutter` (måttlinje x 226 till 270, y 80) med utrop `7 rem`, `#p-lead-169` (ledare från hörnet 808,96 till 840,72) med utrop `16:9` | **16:9 · 7 rem** | `03` · Design |
| s-process-04 Utveckling | 0,46 till 0,55 | raddelningen | `#p-hatch` (skraffering i marginalzonen x 24 till 78, y 96 till 420, avslöjas med clip-path vänster till höger), `#p-ledgers` (tre streckade rader y 300, 358,7, 417,3 mellan x 78 och 226), `#p-dim-row` (lodrät måttlinje x 90, y 300 till 358,7) med utrop `96 px` | **96 px** | `04` · Utveckling |
| s-process-05 Innehåll | 0,55 till 0,64 | den fyllda öppningen | `<image href="assets/demo-calyx-1440.webp">` (gråskala via `filter` på ett 538 x 303-element, aldrig helskärm) inne i `<clipPath>` som öppningens rect; svep `clip-path: inset(0 0 calc((1 - var(--p-fill)) * 100%) 0)` | inget nytt | `05` · Innehåll |
| s-process-06 Lansering | 0,64 till 0,73 | arket som blev sidan | konturernas `stroke-width` faller 1,5 → 0,75 (`--p-thin`), hjälplinjer och skraffering tonar till 0,35 opacitet, måttsiffrorna skalas 44 → 12 px (`transform: scale`, `transform-box: fill-box`) och byter till `--hair-ink` | inget nytt | `06` · Lansering |
| s-process-07 Förvaltning | 0,73 till 0,81, håller till 1 | titelblockets revisionsfält | `#p-title` (tre rutade celler 60 x 18 vid x 24 y 447, hårlinje), `#p-rev` (första cellen får en hårlinjeskraffering avslöjad med clip-path) och utropet `A` (12 px, `--ink`) | inget nytt | `07` · Förvaltning |

Om steg 07:s revisionsfält inte kan ritas som ren form (en cell, en skraffering, en
bokstav) stryks det och steg 07 ritar i stället en andra hårlinjeram 6 units utanför
konturen (`#p-frame2`), samma klass som `#p-outline`. Avvikelsen får en rad i ledgern.

### Målbild skärm för skärm, 390x844

Reducerad plansch som K3 (`K3-r8/index.html:389-476`): viewBox `0 0 320 640`, arket 342 px
brett (`--rail-x` 16 + 16), sticky `top: 12svh`. Kvar: kontur, öppning (272 x 153), en
måttlinje med kedjan 320 · 768 · 1440 som utrop under arket (34 px), 16:9-ledaren, Calyx-
bilden, titelblocket. Bort: hjälplinjer, skraffering, `7 rem`, `96 px`, `#p-stations`.
Texten (index, titel, fråga, svar) ligger **under** arket i flödet, en stegtext i taget,
cued på samma fönster. Sektionen 320 svh. Sju fönster som vid 1440 (arket helt i vy från
ps 0,17 till 0,83; fönstren skalas proportionellt: 01 0,17 till 0,26 … 07 0,71 till 0,83).

### Device-tabell för akten (F-014: allt som förflyttar sig läser `--sc-ps`)

| # | Vad | Device | Läser | Uttryck |
|---|---|---|---|---|
| 1 | arkets banor | bespoke `stroke-dashoffset` via `--p-l` per bana, `pathLength="1"` | `--sc-ps` | `--p-l: clamp(0, calc((var(--sc-ps) - start) / width), 1)`; `stroke-dasharray: 1px; stroke-dashoffset: calc((1 - var(--p-l)) * 1px)` (enheten `*1px` är obligatorisk, K3 rad 263-268) |
| 2 | skraffering, revisionsfält | `clip-path: inset(0 calc((1 - var(--p-l)) * 100%) 0 0)` | `--sc-ps` | samma fönsterform |
| 3 | utrop och måttsiffror, opacitet | `opacity: var(--p-t)` | `--sc-ps` (V3c:s regel, `index.html:38-41`, strängare än K3) | `--p-t: clamp(0, calc((var(--sc-ps) - start) / 0.02), 1)` |
| 4 | måttsiffrornas fall | `transform: scale(calc(1 - 0.7273 * var(--p-fall)))` (44 → 12 px), `transform-box: fill-box` | `--sc-ps` | `--p-fall: clamp(0, calc((var(--sc-ps) - 0.64) / 0.09), 1)` |
| 5 | konturens viktfall | `stroke-width: calc(var(--contour-line) - 0.75px * var(--p-thin))` | `--sc-ps` | `--p-thin` fönster 0,64 till 0,70 |
| 6 | Calyx-bilden | `clip-path: inset(0 0 calc((1 - var(--p-fill)) * 100%) 0)` på `<g>` runt `<image>` | `--sc-ps` | `--p-fill` fönster 0,55 till 0,64 |
| 7 | stegtexterna | opacitet per steg, in 0,02 och ut 0,02 vid fönstergränserna; steg 07 håller | `--sc-ps` | `opacity: min(clamp(0,(ps - start)/0.02,1), clamp(0,(end + 0.02 - ps)/0.02,1))`, sista steget bara in-klampen |
| 8 | arkets sticky-läge | ren CSS `position: sticky; top: 202px` inne i `#process` | ingen | ingen transform, ingen JS; det är sidans **enda** höjdmekanism för akten (`min-height: 300svh` på sektionen, aldrig `min-height` plus `contain-intrinsic-size`) |
| 9 | `will-change` | klass `.is-drawing` på `#process` medan `0 < ps < 1`, satt av den **befintliga** rAF-läsaren `readState` (`index.html:867-879`) som redan räknar heron ur `scrollY`: lägg till samma aritmetik för `#process` (`top`, `height`, liv = höjd + innerHeight) | `scrollY`, en gång per bildruta, ingen `getComputedStyle` | `.is-drawing .draw { will-change: stroke-dashoffset }` |

Registrerade lokaler, i `<style>` (K3 rad 100-104, samma namnrymd fast prefixet `--p-`):

```css
@property --p-l    { syntax: "<number>"; inherits: false; initial-value: 0; }
@property --p-t    { syntax: "<number>"; inherits: false; initial-value: 0; }
@property --p-thin { syntax: "<number>"; inherits: false; initial-value: 0; }
@property --p-fill { syntax: "<number>"; inherits: false; initial-value: 0; }
@property --p-fall { syntax: "<number>"; inherits: false; initial-value: 0; }
```

Utan registrering är värdet en sträng och ritningen stegar (F-013). `--sc-ps` registreras
redan av `scroll/sc-smooth.js` med `inherits: true` (F-014:s efterspel), så barnen ärver.

### Copyutkast v0

Vi-form, korta satser, noll tankstreck (även U+2010 till U+2015), inga tal utöver 320 · 768
· 1440, 16:9, 7 rem, 96 px. Inspirationens roll: Highway Medias fasordning (uppstart,
design och utveckling, innehåll, lansering) ger stegens ordning; Insigns testadress och
redigerbara CMS ger svaren i 03 och 04; Hoys WCAG-princip ger svaret i 02. Lånade som
princip, aldrig som mening. Copy-gaten (fem pass, `humanizer-svenska` sist) körs av en
copy-agent senare; det här är ärligt, inte putsat. Inga tider, inga villkor, inga tal.

| # | Titel | Kundens fråga | Vårt svar |
|---|---|---|---|
| 01 | Uppstart | Vad behöver ni av oss i början? | Ett samtal om verksamheten och vad sidan ska göra för er. Material tar vi emot efter hand. |
| 02 | Planering | Hur vet vi att sidan fungerar på mobilen? | Vi ritar den för tre bredder från början, 320, 768 och 1440, och bygger sedan i den ordningen. |
| 03 | Design | Får vi se förslaget innan ni bygger? | Ja. Förslaget ligger på en testadress som ni öppnar i er egen webbläsare, och ni godkänner innan vi bygger vidare. |
| 04 | Utveckling | Vem äger koden, kan vi ändra själva? | Koden är er. Texter och bilder ändrar ni själva i ett CMS. Resten sköter vi. |
| 05 | Innehåll | Vem skriver texterna och tar bilderna? | Ni kan er verksamhet. Vi sätter text och bild på plats i strukturen och säger till när något saknas. |
| 06 | Lansering | Vad testas innan sidan går live, får vi en genomgång? | Vi går igenom sidan tillsammans på testadressen innan den flyttas till er adress. |
| 07 | Förvaltning | Vad händer efter lansering, finns ni kvar? | Vi finns kvar. En sida är ett levande dokument, och ändringar går samma väg som bygget. |

Liggarens tre underrader (`index.html:755`, `762`, `769`), omskrivna så att de pekar in i
processen (rubrikerna `Design`, `Utveckling`, `System` är låst copy och rörs inte):

| Rad | Nu | v0 |
|---|---|---|
| 01 Design | Identitet och formspråk, hämtat ur den verksamhet sajten ska visa. | Identitet och formspråk, hämtat ur er verksamhet. Ni ser det på en testadress innan vi bygger. |
| 02 Utveckling | Byggt i kod från grunden. Snabbt att ladda, enkelt att bygga vidare på. | Byggt i kod från grunden, för tre bredder. Koden är er. |
| 03 System | Lager, bokningar och medlemskap, på samma tekniska nivå som sajterna. | Lager, bokningar och medlemskap, kopplade innan lansering och skötta efter den. |

Strängen `Så går det till` som kicker ovanför arket, `.kicker-sans` (Public Sans 600, 11 px,
inte mono). Stegindexen `01` till `07` i `.ledger-num` (mono, femte etikettfamiljen, T-7).
Titlarna i `--f-display` 700, `clamp(1.4rem, 2.2vw, 2rem)`, versaler som liggarens h3.
Frågan i `--font` 600, 16 px, `--ink`. Svaret i `--font` 300, 16 px, `rgba(22,20,15,.78)`.

### Token-tabellen

| Token | Värde | Roll | Källa |
|---|---|---|---|
| `--hair-ink` | `color-mix(in srgb, var(--ink) 62%, var(--bg))` | hjälplinjer, måttlinjer, skraffering, ledare, fallna måttsiffror | planens § Designbeslut; 62 % är sidans dämpade bläck (`index.html:572`) |
| `--contour-hair` | `.75px` | den enda hårlinjebredden i arket | K3 `--hair` |
| `--contour-line` | `1.5px` | konturer (ark, öppning, titelblock) | K3 `--contour` |
| `--contour-dash` | `4 3` | den enda streckformen | K3 `--dash` |
| måttsiffror | `var(--c-accent)` | de sanna måtten 320 · 768 · 1440, 7 rem, 96 px, 16:9 | **avvikelse från planens `var(--ink)`**: Anton lättar tvåförekomstlåset (2026-09-15); accentens tredje roll är "ett blått moment per skärm i akten, alltid ett sant tal". Kontrast `#1e5e9c` på `#fdfbf4` 6,46:1. Rad i decision ledger, Q26. Säger Anton nej: `var(--ink)` och tabellen ovan gäller oförändrad |
| utrop (`7 rem`, `96 px`, `16:9`, `A`) | `--hair-ink`, 12 px, `--f-mono`? **nej**: `.kicker-sans` 11 px | monobudgeten (fyra familjer + stegindex) tål inte fler; utropen sätts i Public Sans 600 | planens § Designbeslut |
| papper | `var(--bg)` | aktens grund, samma som `#giant-section` | finns |
| bläck | `var(--ink)` | konturer, titlar, frågor | finns |

Inga inline-hex (gate 48), inga demoterade skills hex (gate 60). Radie 0. Ingen skugga.

### Fingerprint-delta

V3c:s registerrad (`concepts-V3c.md` § (4)) ändras i två celler:

- **Aktform:** "7 screens, 1 pinned act (span 2.2) plus 6 flow acts" → "8 screens, 1 pinned
  act (span 3.4, dwell 0.2) plus a 3 svh sticky drawn process act and 6 flow acts, ~8.7 vh".
- **Signatur:** oförändrad (kortet vänds). Processarket är en **sekundär** signatur lånad
  som form ur K3 och skrivs in i cellen "Act-sequence shape", inte i "Signature move":
  två signaturer är ingen (`feel-and-fingerprint.md` § The peak).

K3:s egen rad (ritningen som blir sidan) står kvar i registret; V3c:s ark blir aldrig sidan
(Calyx maskas in som bild, inte som live-ram), vilket är skillnaden som håller raderna isär.

### Vad i HELHET.md § 3 akten måste uppfylla

H-02, H-05, H-06, H-08, H-15, H-21, H-22, H-23, H-24, H-25, H-26, H-28, H-29, H-30, H-31,
H-32, H-33, H-34, H-35.

## Repo conventions to follow

- Custom properties i `:root` (`index.html:119-155`); nya tokens läggs efter `--body-r5`.
- Fönsteruttryck i CSS ur `--sc-ps`, aldrig i JS per bildruta: exemplar `.plate-card`
  (`index.html:285-296`) och `.panel-giant { --scrub: clamp(...) }` (`index.html:522`).
- `will-change` bara via klass vid gränsövergång: exemplar `.hero.is-turning .plate-card`
  (`index.html:299`) och `readState` (`index.html:867-879`).
- Iframes: ingen tredje. Kommentaren vid `index.html:889-890` gäller.
- `?preview=`: exemplar `MODES` (`index.html:966-976`); nya lägen `process-01` … `process-07`
  sätter `window.__scFreezeMotion = true`, skriver `--sc-ps` på `#process` till fönstrets
  mittvärde (01: 0,235 · 02: 0,325 · 03: 0,415 · 04: 0,505 · 05: 0,595 · 06: 0,685 · 07: 0,90)
  som inline-stil, och `scrollIntoView({block:'start'})` på `#process` följt av en
  `scrollBy(0, mitt * liv)` så att arket faktiskt står sticky i bilden.
- Kickers som inte är mono: `.kicker-sans` (`index.html:423-424`).
- Kommentar i källan som namnger slop-defaulten som ersätts: `<!-- PROCESS: ett ritat ark i sju tillstånd, INTE fyra ikonkort eller en tidslinje med punkter -->`.

## Steps

1. Lägg tokens i `:root` efter `index.html:142`: `--hair-ink`, `--contour-hair`,
   `--contour-line`, `--contour-dash`. Lägg de fem `@property`-raderna ovan direkt efter
   `:root`-blocket.
2. Skriv sektionen efter `index.html:787`:
   `<section id="process" class="process on-paper" data-sc-act="flow" aria-labelledby="process-title">`
   med (a) `<p class="kicker-sans process-kicker">Så går det till</p>` och `<h2 id="process-title" class="process-title">` … (välj titelsträng ur copyutkastet, låst copy rörs inte), (b) `<div class="process-stage">` som är `position: sticky; top: 202px; height: 495px` vid ≥ 900 px bredd, med `<ol class="process-steps">` (sju `<li data-step="01">` med index, titel, fråga, svar) till vänster och `<svg class="process-sheet" viewBox="0 0 880 495">` till höger. Sektionen `min-height: 300svh; padding-block: 0`.
3. Rita banorna i ordningen i målbildstabellen. Varje bana: en av klasserna `contour`,
   `dimline`, `guide`, `leader`, `hatch`, `callout` (kopiera K3:s klassregler, byt tokens
   till `--ink`, `--hair-ink`, `--contour-*`), `pathLength="1"` på allt som ritas med dash,
   `id` per bana, `--p-l`-fönster per `id` i CSS. Räkna banorna: ≤ 60.
4. Måttsiffrorna som `<text class="measure">` i `--f-display` 700, 44 px, `fill: var(--c-accent)`,
   `font-variant-numeric: tabular-nums`, `transform-box: fill-box`, `transform-origin` per
   siffra (320 och 768: `50% 100%`, 1440: `100% 100%`).
5. Calyx: `<clipPath id="p-open"><rect x="270" y="96" width="538" height="303"/></clipPath>`,
   `<g clip-path="url(#p-open)" class="p-live"><image href="assets/demo-calyx-1440.webp" x="270" y="96" width="538" height="303" preserveAspectRatio="xMidYMin slice"/></g>`,
   `.p-live { clip-path: inset(0 0 calc((1 - var(--p-fill)) * 100%) 0); filter: grayscale(1) contrast(1.05); }`
   (filtret ligger på ett 538 x 303-element, aldrig över halva viewporten).
   `<image>` får `width`/`height` så ingen CLS uppstår.
6. Stegtexterna: `.process-steps li { position: absolute; inset: 0; opacity: ...; }` med
   fönstren i device-tabellen rad 7; `li[data-step="07"]` håller. Ingen `transition`.
7. `readState` (`index.html:867-879`): mät `#process` som heron (`top`, `height`), räkna
   `ps = (scrollY + innerHeight - top) / (height + innerHeight)` klampat 0 till 1, toggla
   `process.classList.toggle('is-drawing', ps > 0.0005 && ps < 0.9995)`. `.is-drawing .draw { will-change: stroke-dashoffset }`.
8. `?preview=process-0N` enligt konventionsraden ovan. Lägg de sju i `MODES`-blockets
   grannskap utan att röra `front/mid/back`.
9. Mobil (`@media (max-width: 899px)`): viewBox byts i JS till `0 0 320 640` (attribut, inte
   CSS, K3 rad 1101-1124), `display: none` på `#p-guides, #p-hatch, #p-ledgers, #p-dim-row, #p-dim-gutter, #p-stations` och deras utrop; `d: path(...)` för `#p-outline` (`M0.5 0.5 H319.5 V639.5 H0.5 Z`), `#p-opening` (`M24 150 H296 V303 H24 Z`), `#p-dim-width` (`M0 505 H320`); måttsiffrorna 34 px med x 48 / 145 / 304, y 480; texterna under arket i flödet.
10. Liggarens tre underrader (`index.html:755`, `762`, `769`) byts till v0-strängarna.
11. Uppdatera rubrikkommentaren (`index.html:4-7`) med den åttonde skärmen och
    `BRIEF.md` § decision ledger med raderna: akten, tokens, accentens tredje roll (T-2),
    monobudgeten (T-7), sticky-arket som page-authored höjdmekanism (inte motorns pin).

## Boundaries

- Rör inte `section.hero` (span och fönster ändras i egen plan, 011, ur `HELHET.md` § 2).
- Rör inte `.stagger`, `.panel-thesis`, `.frame-fig`, `.price`, `footer.close`.
- Ingen tredje `<iframe>`; ingen `background-attachment`; ingen `filter` på något större än
  öppningen; ingen `transition` på något som läser `--sc-ps`.
- Ingen text i SVG som är innehåll: bara utrop som anger ett mått eller ett zonnamn, och
  bokstaven `A` i revisionsfältet. Frågor och svar är HTML.
- Inga nya typsnittsfiler. Ingen mono utöver stegindexen.
- Om koden vid `index.html:787` eller `:867-879` inte matchar radhänvisningarna (byggaren R4
  kör parallellt), STOPPA och rapportera i NOTES.md i stället för att gissa.

## Verification

- **Mekaniskt:** `python ~/.claude/skills/design/scripts/serve.py --port 3301 --root .`;
  `motion_probe.py --url … --cpu 4 --track "#process:--sc-ps,#p-outline:stroke-dashoffset,#p-opening:stroke-dashoffset" --wheel 100:60` och `--wheel 20:120`, kontrollen `tests/motion/smooth.html` först och ren: staircase 0, p95 ≤ 20 ms, 0 rutor > 33 ms (H-21, H-32); `scroll_verify.py` vid 1440 och 390: inga nya `deadScroll`-band i akten (H-16), `blankBands` inget band inne i `#process`; `perf_probe.py --cpu 4`: CLS ≤ 0,05 vid 390, sidans egen vikt +≤ 120 kB (webp:en); `detect.mjs --json`; `preflight_taste.py`; `a11y_scan.py` 0 violations (SVG:n `role="img"` med `<title>` och `<desc>`, stegen som `<ol>`); grep `index.html` för `prefers-reduced-motion` = 0 träffar, för U+2013/U+2014 = 0 träffar, för `#[0-9a-f]{6}` i nya rader = 0 träffar.
- **Skärmbilder:** `?preview=process-01` … `07` vid 1440 och 390, lästa som bilder; F-007 bild för bild mot målbildstabellen: rätt banor synliga per steg, rätt sant mått, ett displayelement per skärm; tolvstegs ramsekvens genom `#process`s liv (som `shots/fasA/v3c-giant/`) utan hopp, utan omkastning, utan stopp.
- **Feel check:** scrolla akten kallt med hjulet i båda riktningarna. Linjen ska följa handen som en penna (uppåt suddar den i omvänd ordning). Arket står stilla medan sektionen passerar; ingenting "poppar". Måttsiffrorna landar på hela tal och glider aldrig. Vid 10 % uppspelning i DevTools: inga banor ritas samtidigt som en annan; varje fönster börjar där det föregående slutade. Ingen reduced-motion-kontroll (F-011): rörelsen ska spela med Windows "Animationseffekter" av.
- **Copy:** femton låsta strängar ordagranna (diff mot `PRODUCT.md`-listan), noll tankstreck, inga tal utöver de sex sanna måtten; v0-strängarna markerade `<!-- copy v0, copy-gate i R6 -->` i källan.
- **Done when:** de sju previewbilderna matchar tabellen, proben är grön med kontrollen ren, `scroll_verify` har inga nya band, H-28 till H-33 bockade i `HELHET.md`.
