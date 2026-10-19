# 045 · Processakten inverterad: ett läge i samma fil, som jämförelse mot papperet

- **Status**: TODO (R11, loop 5)
- **Commit**: R10-läget av `runs/V3c/index.html`, md5 `d3491b4a`
- **Severity**: ingen (detta är inte ett fynd). Antons beställning 2026-09-17: han vill se processakten inverterad och jämföra den mot papperet. Planen bygger jämförelseunderlaget, inte en dom.
- **Category**: Visuellt, jämförelseläge. Ingen H-rad öppnas eller stängs av den här planen; golvet är nått i loop 5 utan den.
- **Estimated scope**: 1 fil. Ett additivt CSS-block (~25 rader), en ny token i `:root`, en rad JS i `?preview=`-blocket. **Ingenting i den befintliga pappersvägen redigeras**, så pappersläget är bevisligt oförändrat: dess rader rörs inte.
- **Källor**: `index.html` rad 118 till 152 (`:root`, tokens), 873 till 935 (processaktens typografi och ritregister), 947 till 961 (`.p-live`, `.contour`, `#p-guides`), 968 till 985 (`#process`-blocket), 1028 till 1034 (`.principles`), 1312 (`<section id="process">`), 1497 (`<section id="principer">`), 1991 till 2007 (`?preview=`-parsningen). Mätningar: `shots/loop-5/contrast/` (pappersläget), `BRIEF.md` § Byggarens rader R1 rättelse 2 (accenten mot mörkt).

## Problem

Det finns inget. Akten på papper klarar sitt golv: H-28 till H-33 bockade i loop 5, kontrast
17,77:1 på alla strängar i akten vid 1440 (`contrast_over_media`, scrollY 5 400 och 8 000).
Uppgiften är att bygga **ett andra läge av samma akt** så att Anton kan lägga de två bredvid
varandra och välja. Planen ska därför inte "förbättra" något: den ska ge honom en ärlig
inversion av exakt samma sida.

## Target

`?process=invert` sätter `data-process="invert"` på rotelementet. Ett CSS-block inverterar
**enbart** `#process` och `#principer` genom att skriva om de tokens de redan läser. Ingen
markup dupliceras, inga banor dupliceras, inga fönster ändras, ingen copy ändras.

```css
/* :root, bredvid --c-graphite */
--c-accent-on-dark: <mätt värde, se steg 3>;

/* efter .principles-blocket, additivt */
:root[data-process="invert"] #process,
:root[data-process="invert"] .principles{
  --bg: var(--c-black);
  --ink: var(--c-paper);
  --c-line-on-paper: var(--hairline-dark);
  --c-accent: var(--c-accent-on-dark);
  /* OBS: --hair-ink är deklarerad på :root som
     color-mix(in srgb, var(--ink) 62%, var(--bg)) och substitueras DÄR,
     så den ärver INTE de omskrivna --ink/--bg. Den måste skrivas om här. */
  --hair-ink: color-mix(in srgb, var(--c-paper) 62%, var(--c-black));
}
/* De fyra hårdkodade bläcktonerna inne i de två sektionerna är rgba() och
   läser ingen token; de blir nära svarta mot mörkt om de lämnas. */
:root[data-process="invert"] #process .process-lead,
:root[data-process="invert"] #process .process-p,
:root[data-process="invert"] .principles .ledger-body p{
  color: color-mix(in srgb, var(--c-paper) 78%, var(--c-black));
}
:root[data-process="invert"] .principles .ledger-num{
  color: color-mix(in srgb, var(--c-paper) 62%, var(--c-black));
}
```

```js
/* i ?preview=-blocket, bredvid raden som sätter data-preview (rad ~2000) */
var proc = new URLSearchParams(location.search).get('process');
if (proc === 'invert') document.documentElement.setAttribute('data-process', 'invert');
```

Parametern är fristående från `preview`, så `?process=invert`,
`?preview=process-04` och `?process=invert&preview=process-04` alla fungerar.

**Varför tokens och inte en omskrivning per regel:** akten är redan byggd på fyra tokens.
`.contour` läser `--ink`, `.dimline`/`.guide`/`.leader`/`.leaddot`/`.callout`/`#p-hatch-pattern
line`/`.process-note` läser `--hair-ink`, `.measure` läser `color-mix(var(--c-accent),
var(--hair-ink) …)`, `.ledger`/`.ledger-row` läser `--c-line-on-paper`, och
`.process`/`.principles` sätter `background:var(--bg);color:var(--ink)`. Fyra omskrivna
tokens vänder alltså hela registret. De fyra `rgba(22,20,15,…)` ovan är de enda
undantagen och de är uppräknade.

## Villkoren, Antons ord, som mätbara krav

**(a) Calyx-bilden i steg 05 får inte inverteras.** `.p-live` (rad 947 till 949) behåller
exakt `filter:grayscale(1) contrast(1.05)`. Ingen `invert()`, ingen
`mix-blend-mode`, ingen ny `filter` någonstans i blocket. Det är en riktig produktyta
(gate 47/79) och ska se ut som den sidan ser ut.

**(b) Kontrasten mäts om i det inverterade läget.** `contrast_over_media.py --url` på
`?process=invert` vid 1440 (scrollY 5 400, 6 500, 8 000) och 390 (7 000, 8 500): varje
brödtextsträng ≥ 4,5:1, varje rubrik ≥ 3:1. Hårlinjerna mäts separat (de är inte text):
`--hair-ink` mot den nya grunden ≥ 3:1, räknat på de två tokenvärdena.

**(c) Accenten byter värde med token.** `#1e5e9c` mot `#0b0c0e` är **2,93:1**, mätt och
utskrivet i `BRIEF.md` § Byggarens rader R1, rättelse 2. Den håller alltså inte.
`--c-accent-on-dark` väljs så att måttsiffrorna (`.measure`, 44 px, `#p-m320`, `#p-m768`,
`#p-m1440`) mäter **≥ 4,5:1** mot den valda grunden, i samma blå familj som `--c-accent`
(samma hue, högre ljushet), skriven som en token i `:root`. **Aldrig inline-hex** (gate 48),
**aldrig ett värde ur en demoterad skill** (gate 60). Ledgerraden skrivs i `BRIEF.md`
§ Byggarens rader, R11.

**(d) Grundväxlingen före och efter akten.** I pappersläget är `#process` sidans enda
helbredds materialbyte i mitten (H-03). Blir akten mörk försvinner det bytet, och det finns
inget sätt att behålla båda dess seams: prisplanet är `--c-graphite` (L ≈ 27) och
avslutsfotot är mörkt (L ≈ 8 till 15).

- `--bg: var(--c-black)` (L ≈ 8): pris → process behåller ett steg (Δ L ≈ 19, över H-11:s 12),
  process → avslut tappar sitt.
- `--bg: var(--c-graphite)` (L ≈ 27): pris → process tappar sitt helt (Δ L = 0),
  process → avslut behåller ett.

Bygg **`--c-black`**, alltså den första: den behåller växlingen mitt i dokumentet, där
läsaren är, och den som tappas (ritning → fotografi) bär ändå ett innehållsbyte.
**Mät båda kandidaterna** på pixel (en punkt i prisplanet, en i akten, en i avslutsfotot,
samma metod som H-11) och skriv in de fyra Δ L-talen i `NOTES.md` § R11, så att Anton ser
kostnaden i tal och inte bara i bild. Ingen kompensation byggs in: tesbandet, prisblocket
och avslutet rörs inte i den här planen. Om Anton väljer inverteringen är
grundväxlingen en egen plan i runda 6.

**(e) Båda lägena skjuts i samma sju steg.** Se Verification.

## Repo conventions to follow

- Motorn (`scroll/scrollcraft.js`, `scrollcraft.css`) och `scroll/sc-smooth.js` orörda.
- `sites/*.html` orörda.
- F-011: ingen `prefers-reduced-motion`, ingen statisk fallback.
- F-014: inget nytt som rör sig, alltså ingen ny `--sc-p`-läsare. Blocket är färg, inget annat.
- Låst copy (femton strängar) och de sju processtyckena orörda, ordagrant.
- Gate 75: inga tankstreck i synlig text (blocket lägger ingen text alls).
- Radie 0 står. Inga nya element, ingen ny geometri, inga nya banor.

## Steps

1. Lägg `--c-accent-on-dark` i `:root` bredvid `--c-graphite`, med ett mätt värde (steg 3).
2. Lägg det additiva CSS-blocket efter `.principles`-blocket (rad ~1034). Redigera ingen
   befintlig rad.
3. Mät accenten: räkna kontrasten för kandidatvärden mot `--c-black` tills ett värde i samma
   blå hue når ≥ 4,5:1, skriv talet i planens Verification-svar och i `NOTES.md` § R11.
4. Lägg JS-raden i `?preview=`-blocket, bredvid `data-preview`-raden.
5. Kör mätningarna i (b) och (d).
6. Skjut båda lägena enligt Verification.

## Boundaries

- **Ingen befintlig CSS- eller JS-rad utanför `?preview=`-blocket och `:root`-tokenlistan
  redigeras.** Blocket är additivt. Om en fix verkar kräva en ändring i pappersvägen:
  STOPPA och rapportera, för då är jämförelsen inte längre mellan samma sida i två lägen.
- Matchar inte rad 947 till 949, 968 till 985, 1028 till 1034 eller 1991 till 2007: STOPPA.
- Inverteringen får inte nå `.stagger`, `.price`, `section.hero`, `footer.close` eller någon
  ram. Selektorn är `#process` och `.principles`, ingenting annat.
- Ingen ny `filter`, ingen `invert()`, ingen `mix-blend-mode` någonstans.

## Verification

- **Mekaniskt:**
  - `?process=invert` ensam, `?preview=process-0N` ensam och de två kombinerade laddar utan
    konsolfel; i kombinationen är `--sc-ps` = `--eN` ± 0,0001 för alla sju steg vid 1440 och
    390 (samma mätning som `shots/loop-5/scripts/previews4.py` gör i dag).
  - Utan `?process=` är `data-process` inte satt och sidan är byte-identisk med R10 i
    render: `getComputedStyle` på `.process`, `.process-p`, `.ledger-body p`, `.measure`,
    `.contour` ger samma värden som före ändringen (skriv ut båda uppsättningarna).
  - `a11y_scan` 0 och `reflow.py` rent i **båda** lägena.
  - `grep` `prefers-reduced-motion` 0; inline-hex-räkningen oförändrad (12) plus noll nya.
- **Skärmbilder, det Anton ska jämföra:**
  - `shots/r11/papper/`: `?preview=process-01` till `-07` vid 1440 och 390 (14 bilder), plus
    hela sidan i skivor vid 1440 och 390.
  - `shots/r11/invert/`: `?process=invert&preview=process-01` till `-07` vid 1440 och 390
    (14 bilder), plus hela sidan i skivor vid 1440 och 390 med `?process=invert`.
  - Samma filnamn i båda mapparna, så att lead kan lägga dem parvis sida vid sida.
- **Mätvärden att skriva i `NOTES.md` § R11:** accentens kontrast, varje strängs kontrast i
  invert-läget (b), de fyra Δ L-talen i (d), och `--c-accent-on-dark`s värde.
- **Done when:** båda lägena finns, båda är mätta, och ingen rad i pappersvägen är ändrad.

## Vad jag själv ser i pixlarna, för och emot

Underlag åt Anton, läst ur `shots/loop-5/` denna runda. Det är inte en dom.

**För inverteringen.** Registret är en teknisk ritning, och konvention för en ritning som
*arbetsdokument* är ljusa linjer mot mörkt; papperet är konvention för den *tryckta*
ritningen. Sidans värld är mörk och fotografisk i båda ändar (`slices-1440/…s00` till `s02`
och `s11`), och pappersakten är i dag dokumentets enda ljusa parti: `#process` plus
`#principer` är 4 342 px av 10 582, alltså **41 % av sidan**. En inversion gör sidan till en
sammanhållen mörk värld och tar bort den största tonala utflykten. A-glyfen i arkets hörn
(`process-1440/v3c-1440-life-02.png`) och måttsiffrorna (`…life-06.png`) får mer närvaro mot
mörkt än mot papper.

**Emot inverteringen.** Tre saker, alla läsbara i bilderna:

1. **Växlingen försvinner.** H-03 räknar helbredds materialbyten och sidan har två: papper
   vid `#process` och foto vid avslutet. Inverteringen tar bort det första (villkor d), och
   kvar blir ett. Det är den enda H-rad den här planen rör, och den rör den åt fel håll.
2. **Anatomivarianten försvinner.** H-06 vilar på att prisliggaren (grafitplan), processarket
   (papper) och avslutet (foto) läser som tre material i följd (`slices-1440/…s05`, `s06`,
   `s10`, `s11`). Mörkt ark efter mörkt prisplan gör tre anatomier till två.
3. **Sju stycken brödtext.** Akten bär sju stycken om ~90 ord i `Public Sans 300` på 16 px
   (`process-1440/…life-06.png`). Ljus text i vikt 300 på mörk grund blommar; kontrasttalet
   kan vara godkänt och raden ändå bli tyngre att läsa än pappersraden. Copyn är låst, så
   byggaren kan inte korta den, och planen tillåter ingen viktändring. Det här är min
   starkaste reservation och den syns bäst om Anton läser ett helt steg i båda lägena, inte
   bara tittar på dem.

En fjärde sak, mindre: Calyx-bilden i öppningen (villkor a) förblir en ljus rektangel. På
papper läser den som "ritningen blev sida" (`preview-1440-process-07.png`); på mörk grund
blir samma rektangel ett hål i arket. Det går inte att mäta i förväg, och det är just
därför bilderna ska ställas bredvid varandra.
