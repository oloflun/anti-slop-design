# 054 · V3d: tesbandet äger sin skärm, jättesektionen går, casen ersätter "Hur vi tänker"

- **Status**: TODO (V3d R7, en byggrunda, högst två fixrundor)
- **Beställning**: Anton 2026-09-19, punkterna 1 till 5. Detta är golvet, inte ett förslag.
- **Ordning**: visuellt först, punkterna i Antons ordning. Följdfel lagas i samma runda;
  **ett djärvt drag backas aldrig för att laga ett fel** (`runs/V3c/RAPPORT-LOOPEN.md` fel 5).
- **Copy**: alla synliga strängar står i `COPY-V3d-v0.md` (v0). Byggaren skriver in v0
  ordagrant; copy-agenten kör kedjan efteråt och rör bara strängar. Låst copy ur `PRODUCT.md`
  § Brand Commitments rörs aldrig.
- **Estimated scope**: 1 fil (`runs/V3d/index.html`). Bort: `.stagger` (markup 1650 till
  1748), `#principer` (1994 till 2020) och deras CSS (~300 rader). Nytt: ~260 rader CSS, 4
  sektioner markup, ~110 rader JS. Två live-iframes före och efter (ingen tredje), ingen ny
  asset, inga `sites/*`-ändringar.
- **Underlag, läst som bilder denna session**: nuläget i hjulscroll vid 1440 (19 skärmar) och
  390 (16 skärmar), `shots/lead-r6/sheet-d.png`, Calyx och Hōrai skrollade inuti en 840x760-ram
  (15 + 11 skärmar), referenserna hoy-1440 (23), highway-1440 + insign-1440 (22) och hoy-390
  (20) i kontaktark. Listan står i `NOTES.md` § Arkitekten R7.

## Problem

Tesen, sidans enda mättade färgblock, är en ruta på 651x720 px (45 % vw, 80 % vh) med en
rubrik på 64,8 px och ett stöd­stycke på 15,2 px bredvid en svart jätte. Den äger ingen skärm.
Jättesektionen ("VI BYGGER ERT VARUMÄRKE." med liggaren 01 till 03) delar skärm med Calyx och
tesen i fyra hjulskärmar av sex (nulägets `d-03` till `d-06`) och gör bandet till ett kollage.
"Hur vi tänker" är tre påståenden på papper där sidan borde visa arbetet. Calyx och Hōrai
syns bara som två stilla ramar bredvid varandra (`d-06`); ingen läsare får veta hur de
blev till. Copyn i processakten är 60 till 75 ord per steg i 17 px, och flera marginalrader
hänvisar till saker besökaren inte kan se ("radavståndet i liggaren", "revisionsfältet").

## Sidans nya ordning

| # | Sektion | Grund | Enhet i scroll (1440x900) | Rörelse (läser `--sc-ps`) |
|---|---|---|---|---|
| 1 | Hero, orörd | foto | 3,4 vh | kortvändningen, orörd |
| 2 | **Tesbandet**, `section.thesis` (ny, pinnad) | blått `--c-accent` | 5,5 vh | meningsbytet + Hyperborea + streckräknaren |
| 3 | **Ridån**: tesens stage lyfter av kapitelskärmen | blått över ritbordet | 1 vh (överlapp) | ren scroll, sticky kapitel |
| 4 | Processakten, orörd form, ny copy | ritbordet `--c-drafting` | ~9,8 vh | orörd |
| 5 | **Case-kapitlet** `section.cases-chapter` (ny) | papper `--bg` | 1 vh | rubrikens ordljus |
| 6 | **Case Calyx** `section.case--calyx` (ny, pinnad), text vänster, sajt höger | papper | 5,5 vh | sajtens scroll + textsteg + stegskenan |
| 7 | **Bryggan** `section.case-bridge` (ny) | svart plåt `--c-black` | 1 vh | delad reveal |
| 8 | **Case Hōrai** `section.case--horai` (ny, pinnad), sajt vänster, text höger | svart plåt | 6,4 vh | samma mekanik, spegelvänd |
| 9 | Priset, orört läge | foto + scrim | ~0,9 vh | hårlinjerna, orörda |
| 10 | Avslutet, orört | foto + scrim | ~0,3 vh | orörd |

Sidan växer från ~18,6 till ~34 viewports vid 1440 (uppskattat, se fråga Q6). Material i
följd: foto, blått, ritbordet, papper, svart plåt, foto. Två ljusa fält försvinner (papperet
i bandet och "Hur vi tänker"); papperet kommer tillbaka som case-kapitlet och Calyx-caset,
6,5 vh sammanhängande.

## Target, en rad per beställningspunkt

Alla mål mäts i skärmbild (Playwright `mouse.wheel`, aldrig `scrollTo`) eller
`getBoundingClientRect`/`getComputedStyle` på den byggda sidan. Inget mål är en tidsgräns;
prestanda är en grind (§ Verification C).

| | Synligt mål | 1440x900 | 390x844 |
|---|---|---|---|
| **1** | tesbandets blåa stage | **1440x900 = 100 % vw x 100 % vh** (i dag 651x720 = 45 % x 80 %) | 390x844, 100 % x 100 % |
| **1** | meningarnas font-size, **alla fem lika** (`.ts`, `getComputedStyle`) | **88 px** (i dag rubrik 64,8, stycke 15,2) | **35,5 px** (i dag 32 / 15,2) |
| **1** | varje mening äger rubrikplatsen i ett eget scrollintervall | 5 intervall om **810 px** (0,9 vh, längre än PageDown 787 px); i varje `?preview=thesis-0N` syns exakt en mening, noll glyfpixlar av någon annan | 5 intervall om 760 px |
| **1** | bytet i båda riktningarna | 12-ramssekvens ned och upp genom gränsen 2/3: utgående mening stiger ut genom rubrikradens överkant, inkommande stiger upp ur dess underkant, monotont båda vägarna | samma |
| **1** | "Vi hjälper er att synas på rätt sätt." i sekvensen | mening 4 av 5 | samma |
| **1** | texten i DOM:en | 5 element `.ts` i `.thesis-lines`, alla i tillgänglighetsträdet (axe/`innerText`), ingen `display:none`/`visibility:hidden`/`aria-hidden` | samma |
| **1** | Hyperborea-plåten | ≥ **36 % vw**, flush mot viewportens högerkant (gridbrott), gråskala till färg vid mening 3 | full bredd minus rail, under meningen |
| **1** | 0 delade ord i någon mening | 768/1024/1280/1440/1920 | 320/375/390 |
| **2** | jättesektionen borta | `#giant-section`, `.stagger`, `.col` = 0 träffar i DOM | samma |
| **2** | låst copy kvar | 16/16 rader ur `PRODUCT.md` § Brand Commitments finns i DOM:en ordagrant | samma |
| **2** | ridån | vid scrollY = tesens pinslut + 0,5 vh: övre halvan blått, undre halvan kapitelskärmen på ritbordet; kapitelrubrikens `top` **oförändrad (±1 px)** genom hela ridåns 900 px | samma, 844 px |
| **3** | copyn | varje sträng i `COPY-V3d-v0.md` kolumn v0 står i DOM:en ordagrant; processtycken ≤ 50 ord; noll tankstreck | samma |
| **4** | case-kapitlet | 100 % vh papper, rubrik **≥ 100 px** ensam på skärmen | ≥ 56 px |
| **4** | Calyx: sida för text / sajt | text **vänster**, sajtens ram **höger**, ramens högerkant = viewportens högerkant | sajt överst (sticky i stagen), text under |
| **4** | Calyx: ramens storlek | **≥ 58 % vw x ≥ 88 % vh** (≈ 835x790) | 390 x ≥ 50 % vh (≈ 420) |
| **4** | Calyx: sajten rullar i takt | i varje `?preview=case-calyx-0N` står ramens `contentWindow.scrollY` på stegets ankare **±2 px**, och ankarets sektion syns i ramens övre tredjedel; i en hjulsekvens (80 px/steg) är ramens scrollY monotont stigande ned och monotont fallande upp | samma |
| **4** | Calyx: textstegen | 5 steg, vart och ett ensamt i textplatsen i **810 px** scroll; steg N byter in samtidigt som sajten börjar röra sig mot sektion N och står färdigt när sajten landar | 760 px |
| **4** | Calyx: case-sektionens höjd | **5,5 vh** | 5,5 vh |
| **4** | bryggan | 100 % vh svart plåt, rubrik ≥ 72 px, inget annat än rubrik och ett stycke | ≥ 40 px |
| **4** | Hōrai: sida för text / sajt | sajtens ram **vänster**, flush mot viewportens vänsterkant, text **höger** | sajt överst, text under (samma som Calyx, se device-tabellen) |
| **4** | Hōrai: ramens storlek, takt, steg | som Calyx; 6 steg, **6,4 vh** | som Calyx |
| **4** | Hōrais egna scrollrörelser | husets ordljus och citatets skärpa spelar inne i ramen när sajten rullar (skärmbild vid `case-horai-02` och `-03`) | samma |
| **4** | iframe-budgeten | exakt **2** `iframe` i dokumentet, Calyx och Hōrai, en gång var | samma |
| **4** | priset efter Hōrai | `#pris` direkt efter `.case--horai`, på fotot, oförändrat | samma |
| **5** | materialrytm | inga två sektioner med samma grund kant i kant utan en sektionsgräns som syns; ljusbudget: ≥ 1 skiva om 900 px med > 50 % ljusa pixlar mellan processakten och priset (case-kapitlet) | samma |
| **5** | varje rad i `PARITET.md` | "håller nivån" i en par-bild | samma |

## Tokens

Inga nya färger. Nya ytor återanvänder befintliga tokens: tesen `--c-accent` (accentens
första av två förekomster, som i dag), case-kapitlet och Calyx `--bg`/`--ink` (papperet som
"Hur vi tänker" hade), bryggan och Hōrai `--c-black`/`--c-paper` med `--hairline-dark` (jättens
material, som därmed stannar på sidan). Brödtexten i casen `color-mix(in srgb, var(--ink)
80%, var(--bg))`: räknat ≥ 11:1 på papper och ≥ 12:1 på svart; mät om på pixel.

## Steps

### 1 · Tesbandet äger sin skärm, meningarna byter plats

1. **Markup.** Ersätt hela `<div class="stagger">…</div>` (rad 1650 till 1748, inklusive
   kommentaren ovanför) med en fristående sektion direkt efter `</section>` för heron:

```html
<!-- TES: en pinnad akt, en mening i taget i rubrikplatsen. INTE en rubrik
     med ett stödstycke bredvid en jätte. Alla meningar ligger i DOM:en. -->
<section class="thesis" id="tes" data-sc-act="pin" data-sc-span="5.5" aria-labelledby="tes-1">
  <div data-sc-stage class="thesis-stage">
    <div class="thesis-lines">
      <h2 class="ts" id="tes-1" style="--i:0">Det första intrycket är digitalt.</h2>
      <p class="ts" style="--i:1">Skärmen möter besökaren före texten.</p>
      <p class="ts" style="--i:2">Innan ett ord är läst bär layout och bild hela argumentet.</p>
      <p class="ts" style="--i:3">Vi hjälper er att synas på rätt sätt.</p>
      <p class="ts" style="--i:4">VI BYGGER ERT VARUMÄRKE.</p>
    </div>
    <div class="thesis-ticks" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
    <figure class="thesis-figure">
      <div class="thesis-photo-box"><img src="…demo-hyperborea.webp" …(orört) alt="(v0)"></div>
      <figcaption class="thesis-caption"><span class="cap-line">Exempelsida: Hyperborea, konferens i Lund</span></figcaption>
    </figure>
  </div>
</section>
```

   `data-sc-in` på `.thesis-text` försvinner med den gamla markupen (flödesrevealen får inte
   ligga i en pinnad stage). `img` behåller `src`, `width`, `height`, `loading`; `alt` enligt
   v0. Strängarna 2 och 3 är dagens `.thesis-support` delad i två element, ordagrant.
   Meningen "VI BYGGER ERT VARUMÄRKE." kommer från jättesektionen (se steg 2 och Q1).

2. **CSS.** Ersätt `.panel-thesis` till och med `.thesis-photo-box img` (rad 614 till 697)
   och tesens rader i `@media (max-width:900px)` (1559 till 1564) och `(max-width:640px)`
   (1581 till 1582):

```css
/* PLAN 054 1. Tesbandet: pinnad akt, 5,5 vh. INTE en ruta på 45 % vw. */
.thesis{position:relative;z-index:2;}
.thesis-stage{background:var(--c-accent);color:var(--c-white);
  display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.62fr);
  grid-template-rows:minmax(0,1fr) auto;column-gap:clamp(24px,4vw,64px);
  padding:clamp(72px,12svh,120px) 0 clamp(28px,5svh,48px) var(--rail-x);
  border-bottom:1px solid var(--frame-line);overflow:clip;}
.thesis-lines{grid-column:1;grid-row:1;align-self:center;display:grid;min-width:0;}
.ts{grid-area:1/1;align-self:start;min-width:0;
  font-family:var(--f-display);font-weight:700;
  font-size:clamp(2rem,5vw + 1rem,6rem);line-height:.98;letter-spacing:-.02em;
  text-transform:uppercase;text-wrap:balance;overflow-wrap:normal;hyphens:manual;}
/* Bytet: rubrikradens överkant och underkant är en springa. Utgående
   mening stiger ut genom överkanten, inkommande stiger upp ur
   underkanten. --in/--out läser --sc-ps (F-014), linjärt över --f. */
.js .ts{--a:calc(var(--i) / 5);--b:calc((var(--i) + 1) / 5);--f:.04;
  --in:clamp(0,calc((var(--sc-ps,0) - var(--a) + var(--f) / 2) / var(--f)),1);
  --out:clamp(0,calc((var(--sc-ps,0) - var(--b) + var(--f) / 2) / var(--f)),1);
  clip-path:inset(calc(var(--out) * 100%) 0 calc((1 - var(--in)) * 100%) 0);
  transform:translateY(calc((1 - var(--in)) * .55em - var(--out) * .55em));
  letter-spacing:calc(-.02em + (1 - var(--in)) * .06em);}
.js .ts:first-child{--in:1;}
.js .ts:last-child{--out:0;}
/* Lager 3: fem streck, det aktiva i fullt papper. Inga siffror (PRODUCT.md). */
.thesis-ticks{grid-column:1;grid-row:2;display:flex;gap:10px;margin-top:clamp(20px,3svh,32px);}
.thesis-ticks i{width:32px;height:2px;background:color-mix(in srgb,var(--c-white) 38%,var(--c-accent));}
/* :nth-child(N) får background var(--c-white) när --sc-ps ligger i dess intervall:
   background:color-mix(in srgb,var(--c-white) calc(38% + 62% * var(--on)),var(--c-accent))
   med --on = clamp(0, 1 - abs((var(--sc-ps) - (N - .5) / 5) * 10) + 1, 1) skrivet ut per N. */
.thesis-figure{grid-column:2;grid-row:1 / span 2;align-self:end;min-width:0;margin:0;}
.thesis-photo-box{position:relative;aspect-ratio:16/10;overflow:clip;
  border:1px solid var(--frame-line);border-right:0;}
/* Lager 2: färgen kommer med mening 3 ("layout och bild"), beskärningen drar åt. */
.thesis-photo-box img{width:100%;height:100%;object-fit:cover;
  filter:grayscale(calc(1 - clamp(0,calc((var(--sc-ps,0) - .4) / .2),1))) contrast(1.05);
  transform:scale(calc(1 + .06 * var(--sc-ps,0)));transform-origin:70% 40%;}
.thesis-caption{margin-top:12px;padding-right:var(--rail-x);}
.thesis-caption .cap-line{/* orörd deklaration från rad 663 till 665 */}
@media (max-width:767px){
  .thesis-stage{grid-template-columns:minmax(0,1fr);grid-template-rows:auto auto auto;
    padding:clamp(56px,9svh,80px) var(--rail-x) clamp(20px,3svh,32px);row-gap:16px;}
  .thesis-lines{align-self:start;min-height:calc(7 * .98 * clamp(2rem,5vw + 1rem,6rem));}
  .thesis-figure{grid-column:1;grid-row:3;}
  .thesis-photo-box{border-right:1px solid var(--frame-line);}
  .thesis-caption{padding-right:0;}
}
```

   `.thesis-lines` får vid < 768 en min-höjd lika med sju rader, så att den längsta meningen
   (mening 3, 57 tecken) aldrig flyttar plåten när den byter in. Vid ≥ 768 centreras raderna
   i sin rad och plåten står bottenställd; den längsta meningen tar 5 rader à 86 px = 430 px
   i en spalt på ~790 px.

3. **Drift.** `.thesis` ersätter `.panel-thesis` i `thesisEl` (JS rad 2289). `giantEl` finns
   inte längre: skriv om `driftColor()` (rad 2116 till 2130) till två ben som bara läser
   tesen, **svart → `--c-accent-deep` över t 0 till 0,35, `--c-accent-deep` → svart över t
   0,65 till 1**, och ta bort `giantTop`, `giantH`, `driftHand` (rad 2292, 2303, 2309) och
   `DRIFT_STOPS[2]`. Grunden syns bara i heron och i priset; priset ska stå på fotots
   neutrala ton som heron, inte i blått.

### 2 · Jättesektionen bort, ridån från tesen till ritningen

4. **Vad som bor i jättesektionen och är låst** (`PRODUCT.md` § Brand Commitments):
   - `VI BYGGER ERT VARUMÄRKE.` → **mening 5 i tesens sekvens** (steg 1). Skäl:
     `PRODUCT.md` § Product Purpose kallar raden ordagrant "Tesrubriken". Den hör hemma i
     tesbandet, och den avslutar sekvensen som svar på "Vi hjälper er att synas på rätt
     sätt." Samma storlek som de andra meningarna, som Anton beställt.
   - `Webbdesign, design och system. Allt på ett ställe.` → **kapitelskärmen** i processakten,
     som stycke direkt under "Från samtal till lanserad sida." (steg 6). Skäl: raden säger
     vad som kommer ur samma ställe; kapitelskärmen inleder just hur det görs.
   - `Design`, `Utveckling`, `System`: finns redan kvar på kortets baksida (`.card-services`,
     rad 1631) och i `.sr-only` (rad 1643). Inget flyttas.
   - Olåst och borta med sektionen: numreringen 01 till 03 och tjänsternas tre underrader.
     Samma innehåll bärs av processstegen 03 Design och 04 Utveckling (bokning, betalning,
     kunddatabas). Se Q2.
5. **Ta bort** `#giant-section` och allt som bara tjänar den: CSS rad 879 till 1026
   (`.panel-giant`, `.giant`, `.giant-sub`, `#giant-section`, `.ledger-wrap`, `.thread*`,
   `.ledger`, `.ledger-row`, `.ledger-body`, `.is-scrubbed …`, `@container`); **men behåll
   `.ledger-num`** (rad 994 till 995) eller flytta dess två kvarvarande deklarationer in i
   `#process .ledger-num`: stegens siffror använder klassen. Greppa varje borttagen selektor
   efter kvarvarande användare innan den raderas. JS: `giant`/`is-scrubbed` (rad 2531 till
   2534), `?preview=ledger` och `?preview=bleed` (rad 2558 till 2573). CSS för `.stagger`,
   `.col*`, `.calyx-fig`, `.horai-fig`, `.calyx-wrap`, `.horai-wrap` (rad 567 till 602,
   713 till 735, 737 till 738, 766 till 783, 820 till 821, 1029 till 1031, 1554 till 1558).
   `.frame-wrap`, `.frame-wrap iframe`, `.frame-wrap.is-asleep`, `.frame-wrap.frame-poster`,
   `.frame-cap` och `:focus-within` står kvar (casen använder dem).
6. **Ridån.** Kapitelskärmen blir stående medan tesens stage lyfter av den. Inget skrivs
   per bildruta; det är ren scroll.
   - Markup: omslut `.process-chapter` (rad 1769 till 1774) i `<div class="chapter-hold">`.
     Lägg `<p class="process-locked">Webbdesign, design och system. Allt på ett ställe.</p>`
     efter `h2#process-title`, före `.process-lead`.
   - CSS (ersätter `.process-chapter` rad 1053 till 1055):

```css
/* PLAN 054 2. Ridån: #process ligger en skärm in under tesen. Kapitlet är
   sticky i sin hållare, så det står still medan tesens blå stage glider
   upp av det. INTE ett nytt blått block, INTE en korsfadning. */
#process{position:relative;z-index:1;margin-top:-100svh;}
.chapter-hold{height:calc(200svh + 40svh);}
.process-chapter{position:sticky;top:0;height:100svh;display:flex;
  flex-direction:column;justify-content:center;padding-block:clamp(72px,12svh,120px);}
.process-locked{font-family:var(--font);font-weight:300;
  font-size:clamp(1.25rem,1.6vw,1.5rem);line-height:1.4;max-width:34ch;
  margin-top:clamp(20px,3svh,32px);padding-inline:var(--rail-x);}
```

   Räkning: hållarens överkant = tesens underkant - 100svh = exakt den scrollY där tesens
   pin släpper. Kapitlet börjar klibba i samma ögonblick som stagen börjar lämna, står still
   i 1 vh medan stagen lyfter, och sedan 0,4 vh ensamt innan band 01 kommer. Tesens
   `border-bottom` (`--frame-line`) är ridåns kant.
   - `measureAct` mäter om `processTop` och ankarna (oförändrad kod); `--s1..--e7` flyttas
     med. `?preview=process-0N` ska landa som i dag: kontrollera alla sju vid 1440 och 390.

### 3 · Copyn, enklare och tydligare

7. Skriv in varje sträng i `COPY-V3d-v0.md` där status är **förenklad** eller **ny**, med
   `Edit` per sträng, och sätt `<!-- copy v0, 054 -->` före varje ändrat element. Rör inga
   strängar med status **låst** eller **oförändrad**. SVG-texterna i arket (`320`, `768`,
   `1440`, `7 rem`, `16:9`, `96 px`, `A`) är mått och rörs inte.

### 4 · Case-kapitlet, Calyx, bryggan, Hōrai

**Etikett: "Exempelcase".** Skäl: Calyx och Hōrai är Alunix egna exempelsajter;
"Kundcase" påstår en kund som inte finns (`PRODUCT.md` § absences, "Kunder utöver de tre
exempelsajterna"). "Exempelcase" delar förledet med de låsta bildtexterna
("Exempelsida: …"), så etiketten och bildtexten säger samma sak. Casetexternas första steg
säger dessutom uttryckligen att sajten är ett exempel vi byggt för en tänkt verksamhet.

**Iframe-mekaniken: levande ram, skrollad inifrån med `contentWindow.scrollTo`.** Vägt mot en
lång skärmbild i en mask:

| | Levande ram, `scrollTo` | Lång skärmbild, `translateY` |
|---|---|---|
| Beviset | sajten kör på riktigt: Hōrais ordljus och citatskärpa och Calyx reveals spelar i takt (`PRODUCT.md` princip 1, "Beviset ska gå att använda") | en bild av sajten; Hōrais egna rörelser syns aldrig |
| Lås | ramen transformeras aldrig; dokumentet inuti skrollar (samma som en läsare som skrollar i den) | inget lås berört |
| Kostnad | ramens eget dokument layoutar/målar när det skrollar; två ramar finns redan i dag, sövs utanför 40 % | en transform på en stor bild, billigast |
| Tillförlitlighet | same-origin, synkron; risker: Hōrais `scroll-behavior:smooth` (lös: `behavior:'instant'`), Tailwind-CDN:ns omlayout efter load (lös: `ResizeObserver` i ramens dokument), ramen ej laddad vid snabb scroll (lös: `frame-poster` finns redan, montering tidigareläggs) | nya assets (två helsidesbilder, ~1 till 2 MB), måste tas om vid varje sajtändring |

Valt: levande ram. Blir det ramens kostnad som faller i grinden (§ Boundaries) stoppar
byggaren och skriver i NOTES; skärmbildsvägen är lead:s beslut, inte en tyst reträtt.

**Bandets nya roll.** Bandet (`.stagger`) upphör. Tesbandet står ensamt och behåller
Hyperborea som sin bild, som i dag en stillbild (ingen ram). Calyx- och Hōrai-ramarna flyttar
in i casen: fortfarande exakt två live-iframes. Sidan visar Hyperborea en gång, Hōrai en gång.
Calyx syns två gånger i följd, i arkets steg 05 till 07 som bild och direkt efter i caset som
levande sajt; det är övergången, inte en upprepning: processaktens sista not säger att
"ritningen finns kvar som ram runt den färdiga sidan", case-kapitlet säger "Så blev
ritningen en sida", och Calyx-caset öppnar samma sajt i full storlek.

8. **Markup, fyra sektioner** efter `</section>` för `#process` och före `#pris`; hela
   `#principer` (rad 1994 till 2020) tas bort:

```html
<!-- CASE-KAPITEL: en rubrik som äger skärmen på papper. INTE ett kortrutnät med case. -->
<section class="cases-chapter" id="case" data-sc-act="flow" aria-labelledby="case-title">
  <p class="kicker-sans">Exempelcase</p>
  <h2 id="case-title" class="cases-title">Så blev ritningen en sida.</h2>
  <p class="cases-lead">(v0)</p>
</section>

<!-- CASE CALYX: text vänster, sajten höger och skrollad i takt. INTE en stilla
     skärmbild bredvid en punktlista. -->
<section class="case case--calyx on-paper" id="case-calyx" data-sc-act="pin"
         data-sc-span="5.5" aria-labelledby="calyx-title">
  <div data-sc-stage class="case-stage">
    <div class="case-text">
      <p class="kicker-sans">Exempelcase</p>
      <h2 id="calyx-title" class="case-title">Calyx</h2>
      <ol class="case-steps">
        <li class="cs" style="--i:0"><h3>(v0)</h3><p>(v0)</p></li>
        … fem li, --i 0 till 4, text ur COPY-V3d-v0 …
      </ol>
      <div class="case-rail" aria-hidden="true"><span>(h3 1)</span>…<span>(h3 5)</span></div>
    </div>
    <figure class="frame-fig case-fig">
      <div class="frame-wrap case-wrap calyx-wrap frame-poster">
        <iframe data-src="/sites/calyx.html" loading="lazy" inert
                title="Exempelsida: Calyx, florist i Stockholm"></iframe>
      </div>
      <figcaption class="frame-cap">Exempelsida: Calyx, florist i Stockholm</figcaption>
    </figure>
  </div>
</section>

<!-- BRYGGA: en mening på svart plåt mellan två sajter. INTE en tredje ram. -->
<section class="case-bridge" data-sc-act="flow" aria-labelledby="bridge-title">
  <h2 id="bridge-title" class="bridge-title" data-sc-in>(v0)</h2>
  <p class="bridge-p" data-sc-in>(v0)</p>
</section>

<!-- CASE HŌRAI: spegelvänt, sajten vänster, texten höger. -->
<section class="case case--horai" id="case-horai" data-sc-act="pin" data-sc-span="6.4"
         aria-labelledby="horai-title"> … samma anatomi, sex li, .case-fig FÖRE .case-text i
  DOM:en, ramen /sites/horai.html med title "Exempelsida: Hōrai, Asian fusion-koncept" … </section>
```

   `.rv`-omslaget runt ramen tas bort (ingen reveal på casens ramar: stagen själv glider in,
   och en ram får aldrig klippas med clip-path, plan 036). `.calyx-wrap`/`.horai-wrap` står
   kvar enbart som krokar för `frame-poster`-bilden (rad 820 till 821). `id="projekt"` flyttar
   till `#case`.

9. **CSS för casen** (nytt block efter `.frame-cap`):

```css
/* PLAN 054 4. Casen: pinnad stage, text och sajt delar skärmen 5/7.
   Ramen möter viewportens kant (gridbrottet). */
.case--calyx{--bg:var(--bg);--ink:var(--ink);}
.case--horai{--bg:var(--c-black);--ink:var(--c-paper);--c-line-on-paper:var(--hairline-dark);}
.case-stage{background:var(--bg);color:var(--ink);display:grid;
  grid-template-columns:minmax(0,5fr) minmax(0,7fr);column-gap:clamp(24px,4vw,64px);
  padding-block:clamp(24px,4svh,40px);}
.case--calyx .case-text{grid-column:1;padding-left:var(--rail-x);}
.case--calyx .case-fig{grid-column:2;}
.case--horai .case-fig{grid-column:1;grid-row:1;}
.case--horai .case-text{grid-column:2;grid-row:1;padding-right:var(--rail-x);}
.case--horai .case-stage{grid-template-columns:minmax(0,7fr) minmax(0,5fr);}
.case-fig{min-width:0;display:flex;flex-direction:column;}
.case-wrap{flex:1;min-height:0;border:1px solid var(--c-line-on-paper);}
.case--calyx .case-wrap{border-right:0;}
.case--horai .case-wrap{border-left:0;}
.case-text{display:flex;flex-direction:column;justify-content:center;min-width:0;}
.case-title{font-family:var(--f-display);font-weight:700;
  font-size:clamp(3.5rem,7.2vw,7.5rem);line-height:.95;letter-spacing:-.03em;margin-top:12px;}
.case-steps{list-style:none;margin:clamp(28px,5svh,48px) 0 0;padding:0;display:grid;}
.cs{grid-area:1/1;min-width:0;}
.cs h3{font-family:var(--f-display);font-weight:700;font-size:clamp(1.5rem,2.2vw,2rem);
  line-height:1.05;letter-spacing:-.01em;text-transform:uppercase;}
.cs p{font-size:clamp(1.0625rem,1.4vw,1.25rem);line-height:1.55;max-width:36ch;margin-top:.7rem;
  color:color-mix(in srgb,var(--ink) 80%,var(--bg));}
/* Samma springa som tesen, N ur sektionen (Calyx 5, Hōrai 6). */
.case--calyx{--n:5;} .case--horai{--n:6;}
.js .cs{--a:calc(var(--i) / var(--n));--b:calc((var(--i) + 1) / var(--n));--f:.04;
  /* --in, --out, clip-path, transform, letter-spacing exakt som .js .ts */}
.js .cs:first-child{--in:1;} .js .cs:last-child{--out:0;}
/* Stegskenan: stegens rubriker i 13 px, det aktiva i fullt bläck, en
   hårlinje fylls i takt med --sc-ps. Lager 3. */
.case-rail{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:clamp(28px,5svh,48px);
  padding-top:12px;border-top:1px solid var(--c-line-on-paper);
  font-size:13px;font-weight:600;letter-spacing:.04em;}
.case-rail span{color:color-mix(in srgb,var(--ink) calc(62% + 38% * var(--on,0)),var(--bg));}
/* --on per span: samma formel som .thesis-ticks, N ur --n, skrivet per nth-child. */
```

   Stagens höjd är motorns 100svh (`[data-sc-stage]{height:100svh}` rad 327 gäller redan).
   `.case-wrap` fyller figuren under bildtexten: vid 1440x900 ≈ 835 x 790.

10. **CSS för kapitlet och bryggan:**

```css
.cases-chapter{background:var(--bg);color:var(--ink);min-height:100svh;display:flex;
  flex-direction:column;justify-content:center;padding:clamp(72px,12svh,120px) var(--rail-x);}
.cases-title{/* = .process-title (rad 1056 till 1059): 3,5rem till 7,5rem */}
.cases-title{--edge:calc(var(--sc-ps,0) * 260%);background-image:linear-gradient(100deg,
  var(--ink) 0 calc(var(--edge) - 12%),color-mix(in srgb,var(--ink) 62%,var(--bg)) calc(var(--edge) + 12%) 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;}
.cases-lead{font-size:1.25rem;line-height:1.5;max-width:44ch;margin-top:clamp(20px,3svh,32px);
  color:color-mix(in srgb,var(--ink) 80%,var(--bg));}
.case-bridge{background:var(--c-black);color:var(--c-paper);min-height:100svh;display:grid;
  place-content:center;padding:clamp(72px,12svh,120px) var(--rail-x);
  border-top:1px solid var(--frame-line);}
.bridge-title{font-family:var(--f-display);font-weight:700;
  font-size:clamp(2.5rem,5vw + .5rem,5.5rem);line-height:.98;letter-spacing:-.02em;max-width:18ch;}
.bridge-p{font-size:1.25rem;line-height:1.5;max-width:44ch;margin-top:clamp(20px,3svh,32px);
  color:color-mix(in srgb,var(--c-paper) 80%,var(--c-black));}
```

   Kapitelrubrikens ordljus läser kapitlets egna flödes-`--sc-ps` (0,5 när rubriken står i
   mitten): fronten har passerat hela rubriken vid ~0,5, båda ändarna läsbara (62 % bläck ≥
   6:1 på papper).

11. **JS: montering.** I `latchTick` (rad 2172): byt villkoret `heroAct.cur >= 0.80` mot att
    processakten har nått steg 05: flytta monteringen in i `if (process){…}`-grenen efter
    `procAct` är hittad, `if (!framesMounted && stepAnchors[4] && procAct.cur >= stepAnchors[4].s)`.
    Två levande sajter ska inte starta under tesens meningsbyte. Observern (rad 2490 till
    2506) står kvar oförändrad: den observerar `.frame-wrap` och söver utanför 40 %.
    Ta bort `reveals` (rad 2085 till 2089 och slingan 2217 till 2227) och `measureFrames`
    (rad 2384 till 2396); `@property --rv` (rad 761) och `.rv`-reglerna går med.

12. **JS: sajten rullar i takt.** Nytt, efter `measureAct`:

```js
/* PLAN 054 4. Casens ramar skrollas INIFRÅN, ur aktens LERPADE värde (cur),
   i latchTick. Ramen själv transformeras aldrig (PRODUCT.md). Ankarna mäts
   i ramens dokument (same-origin) vid load och vid varje storleksändring
   där, aldrig per bildruta. */
var CASES = [
  { el: document.getElementById('case-calyx'), anchors: [
      ['top', 0], ['#studio', 0], ['#studio + section', 0], ['#index', 0], ['#commission', 0] ] },
  { el: document.getElementById('case-horai'), anchors: [
      ['top', 0], ['#hero-section + section', 0.30], ['#quote-section', -0.40],
      ['#quote-section + section', 0], ['#reservations', -1], ['#reservations', 0] ] }
].filter(function(C){ return C.el; });
/* Andra talet: förskjutning i ramhöjder. 0,30 = husets stycke står en tredjedel
   ned så ordljuset spelar; -0,40 = citatets eget "formade läge" (horai.html rad
   481); -1 = rummet (sektionen före bokningen) står i ramen. Mätt vid bygget,
   justeras mot skärmbild, skrivs i NOTES. */
function measureCase(C){
  var f = C.el.querySelector('iframe'), w = f && f.contentWindow, d = f && f.contentDocument;
  if (!d || !d.documentElement) return;
  var ih = w.innerHeight, max = d.documentElement.scrollHeight - ih;
  C.f = f; C.w = w; C.y = C.anchors.map(function(a){
    var t = a[0] === 'top' ? 0 : (d.querySelector(a[0]) || {}).offsetTop || 0;
    return Math.max(0, Math.min(max, Math.round(t + a[1] * ih)));
  });
}
function caseY(C, p){
  var n = C.y.length, k = Math.min(n - 1, Math.floor(p * n)), t = p * n - k;
  if (k === 0) return C.y[0];
  var u = Math.min(1, t / 0.45); u = u * u * (3 - 2 * u);   /* resa 45 %, stå 55 % */
  return C.y[k - 1] + (C.y[k] - C.y[k - 1]) * u;
}
```

   - Koppling: i `mountFrame` (rad 2458), efter `f.src = s`, lägg en `load`-lyssnare som
     letar upp sitt `CASES`-objekt, kör `measureCase` och sätter
     `new f.contentWindow.ResizeObserver(function(){ measureCase(C); }).observe(f.contentDocument.documentElement)`.
     Även `resize` på fönstret kör `measureCase` för varje ärende.
   - I `latchTick`, efter reveals-slingans plats: för varje `C` med `C.y`: `act =
     findAct(acts, C.el)`; `y = caseY(C, act.cur)`; om `Math.abs(y - C.last) >= 0.5`:
     `C.w.scrollTo({ top: y, left: 0, behavior: 'instant' }); C.last = y`. Om aktens
     `--sc-p` och `cur` skiljer > 0,0005: `again = true` (samma mönster som processen,
     rad 2213 till 2214). **Ingen `getComputedStyle`, ingen `scrollHeight`-läsning per
     bildruta.**
   - Steg N:s text byter in vid p = N/n, samma ögonblick som `caseY` börjar resan mot
     ankare N; sajten landar vid p = (N + 0,45)/n, långt innan steget byter ut.

13. **Mobilen, < 768.** Samma pinnade akt; stagen staplas med sajten överst:

```css
@media (max-width:767px){
  .case-stage,.case--horai .case-stage{grid-template-columns:minmax(0,1fr);
    grid-template-rows:52svh minmax(0,1fr);padding:0 0 clamp(16px,3svh,24px);}
  .case .case-fig{grid-column:1;grid-row:1;}
  .case .case-text{grid-column:1;grid-row:2;justify-content:flex-start;
    padding:clamp(16px,3svh,24px) var(--rail-x) 0;}
  .case-wrap,.case--calyx .case-wrap,.case--horai .case-wrap{border:0;
    border-bottom:1px solid var(--c-line-on-paper);}
  .case-text > .kicker-sans{display:none;}
  .case-title{font-size:clamp(2rem,9vw,2.5rem);margin-top:0;}
  .case-steps{margin-top:14px;}
  .cs h3{font-size:1.375rem;} .cs p{font-size:1rem;max-width:none;}
  .case-rail{display:none;}
}
```

   **Skäl, sajten ovanför texten på båda casen:** vid 390 finns ingen sida att spegla;
   ögat läser uppifrån, och texten är sajtens bildtext för det som syns just då. Spegeln
   bärs av grunden (papper mot svart plåt) och av ordningen i DOM:en, inte av en
   spegelvänd stapel som skulle lägga Hōrais text ovanför en ram texten ännu inte
   beskrivit. Kickern och skenan döljs under 768 (de upprepar rubriken och stegens
   rubriker; ytan behövs för stycket). Casestyckena är ≤ 40 ord (COPY-V3d-v0), vilket ger
   ≤ 9 rader i 16 px vid 320 och ryms under en ram på 52svh vid 320x568.

### 5 · Balans och övergångar

14. **Övergångarna, en i taget, och vad som bär dem:**
    - hero → tes: heronts pin släpper, den blå stagen stiger in i full bredd. Pin följer på
      pin; avsteg från "aldrig samma familj två gånger i rad" (devices.md), namngivet: tesens
      meningsbyte är Antons beställning, och materialbytet foto → blått plus heronts 160 px
      luft före (`.stagger`s padding-top försvinner, ersätts av `.thesis{margin-top:
      clamp(160px,18vh,200px)}` på fotots grund) gör gränsen läsbar.
    - tes → process: ridån (steg 6).
    - process → case-kapitel: arkets sista bild är Calyx i färg; sedan papper med "Så blev
      ritningen en sida." Hård materialgräns ritbordet → papper, som hoy (hoy-home s03 → s04).
    - Calyx → brygga: papper → svart plåt, hård gräns med `--frame-line` överst.
    - brygga → Hōrai: samma svarta plåt; Hōrais ram glider in från vänster kant med stagen.
    - Hōrai → pris: svart plåt → foto med scrim, orört prisblock.
15. **Tre sektionsanatomier till** (utöver hero, process, pris): pinnad helbredd med
    bytande rad (tes), kapitel i centrerad spalt (case-kapitel, brygga), delad diptyk med
    ram mot kanten (casen). Ingen anatomi två gånger i rad utom kapitlet och Calyx-caset,
    som skiljs av pin mot flöde.
16. **Ingen ny accent.** `#1e5e9c` fortfarande exakt två förekomster (tesen, "Boka ett
    möte"). Monobudgeten: jättens siffror försvinner, kvar är tre av fyra (kortets kicker,
    kortets tjänsterad, tesens bildtext).

## Device-tabell

| Bredd | Tesbandet | Ridån | Case-kapitel / brygga | Casen |
|---|---|---|---|---|
| **1440x900** | stage 1440x900; meningar 88 px i spalt ~790 px, ≤ 5 rader; Hyperborea ~40 % vw flush höger, färg från mening 3; streck under raderna | kapitlet står, blått lyfter 900 px | 104 / 88 px rubrik | text 5/12 (~500 px, h2 104 px, steg 32 px + 20 px); ram 7/12 ≈ 835x790 flush mot kanten |
| **1280x800** | 80 px, ≤ 5 rader | 800 px | 92 / 80 px | ram ≈ 740x700 |
| **1024x768** | 67 px, ≤ 5 rader; plåt ~36 % vw | 768 px | 74 / 67 px | ram ≈ 590x670 (Calyx byter till sin smala layout, väntat) |
| **768x1024** | 54 px; staplad under 768 gäller inte, 768 är två spalter: plåt 0,62fr ≈ 280 px | 1024 px | 56 / 54 px | två spalter: text ~290 px, steg 17 px; ram ≈ 430x960 |
| **390x844** | 35,5 px, raderna överst (min 7 rader), plåt 344 px bred under, bildtext under plåten | 844 px | 56 / 40 px | ram 390x439 överst, text under: h2 35 px, steg 22 + 16 px |
| **320x568** | 32 px, plåt 288 px | 568 px | 56 / 40 px | ram 320x295, text under ≤ 9 rader |

Noll horisontell scroll 320 till 1920, mätt på elementens rektanglar (gate 34). Vid 200 %
zoom på 1440 (720 css-px) gäller 768-raden. Hōrai vid 390 har ett eget känt överflöde i
`sites/horai.html` (r3 fix 7, rörs aldrig); det syns som en kapad underrubrik inne i ramen.

## `?preview=`

Varje läge sätter `window.__scFreezeMotion = true` (befintligt, rad 2544). En gemensam
`aimPin(el, p)`: `target = elTop + p * (el.offsetHeight - innerHeight)`, samma settle-slinga
och driftlyssnare som `aimPreview` (rad 2621 till 2659), klar när aktens `--sc-ps` = p ±
0,002. Casen väntar dessutom in ramens `load` + `measureCase` och kör `kickLatch()` så att
ramen hinner skrollas.

| Läge | p | Visar |
|---|---|---|
| `thesis-01` … `thesis-05` | (N - 0,5)/5 | mening N ensam i rubrikplatsen |
| `curtain` | tesens pinslut + 0,5 vh (scrollY) | halvt blått, halvt kapitel |
| `chapter` | kapitlet sticky, blått borta | kapitelskärmen ensam |
| `cases` | `#case` centrerad, `--sc-ps` 0,5 | case-kapitlet med rubriken tänd |
| `case-calyx-01` … `-05` | (N - 1 + 0,8)/5 | steg N, sajten landad på ankare N |
| `bridge` | `.case-bridge` centrerad | bryggan |
| `case-horai-01` … `-06` | (N - 1 + 0,8)/6 | steg N, sajten landad på ankare N |
| `front`, `mid`, `back`, `process-01` … `-07` | oförändrade | som i dag |

`ledger` och `bleed` tas bort (deras mål finns inte längre).

## Repo conventions

- Motorn `scroll/scrollcraft.js`, `scrollcraft.css`, `scroll/sc-smooth.js` och `sites/*`
  orörda. Inga nya `@property`.
- F-011: ingen `prefers-reduced-motion`, ingen statisk fallback. F-014: allt som rör sig
  läser `--sc-ps` (CSS) eller shimens `cur` (JS); rå `--sc-p` driver ingenting.
- No-JS: `.js`-grindarna gör att meningarna och casestegen utan skript står staplade men
  överlagrade i samma cell. Lägg `.no-js .ts,.no-js .cs{grid-area:auto;}` så de staplas i
  flödet och alla syns (reveal faller mot synligt).
- Låst copy ordagrant. Gate 75: noll tankstreck (U+2010 till U+2015, U+2212). Radie 0,
  inga skuggor. Gate 47: ramarna är riktiga sajter, ingen ritad webbläsarkrom.

## Boundaries (STOPPA och skriv i NOTES)

- En låst sträng skulle behöva ändras.
- Ramens synk kräver en läsning av `getComputedStyle` eller `scrollHeight` per bildruta.
- `motion_probe` på `#case-calyx:--sc-ps` eller `#case-horai:--sc-ps` ger `staircase` > 0,
  eller bildrutor > 33 ms fler än dubbla processaktens värde i samma körning (cpu 1).
  Då beslutar lead om skärmbildsvägen; byggaren byter inte själv.
- Ridån gör att någon `?preview=process-0N` inte längre landar på `--eN`.

## Verification

**A. Synligt, det som avgör.** `PARITET.md`: par-bilder vid 1440 och 390 för varje rad,
lästa som bilder, varje rad "håller nivån" eller lagad i samma runda. Plus Target-tabellen
rad för rad med uppmätt värde. Lead läser själv par-bilderna för P03, P04, P14, P17 till
P20 bredvid referensen innan runda räknas klar.

**B. Mätt.**
- 1: `getComputedStyle(.ts).fontSize` för alla fem vid 320/390/768/1024/1280/1440/1920
  (identiska per bredd); ordbrytningsskriptet (R3:s) på `.ts`, `.case-title`, `.cs h3`,
  `.cases-title`, `.bridge-title`; hjulsekvens 80 px/steg genom hela tesen, ned och upp,
  kontaktark, med `--in`/`--out` per mening utskrivna per ram.
- 2: grep `giant-section|stagger|principer` = 0 i markup; 16 låsta strängar ordagrant i
  `document.body.innerText`; ridån: kapitelrubrikens `top` var 50:e px genom ridån.
- 4: vid varje `case-*-0N`: `C.w.scrollY` mot `C.y[N-1]`; hjulsekvens 80 px/steg genom båda
  casen, ramens `scrollY` utskriven per ram, monoton båda riktningarna; skärmbild per ram,
  kontaktark; `document.querySelectorAll('iframe').length === 2`.
- 5: ljusbudgeten per skiva om 900 px vid 1440 (andel pixlar med relativ luminans > 0,5),
  som i plan 048 § Beslut G punkt 4.
- Kontrast: `contrast_over_media.py --url` på tesen (thesis-03), kapitlet, casestegen (båda
  grunderna), bryggan, priset; `background-clip:text` läses med pixelmetoden (NOTES R1).

**C. Grinden (inte målet).** `scroll_verify` 1440 och 390; `motion_probe` med kontroll-
protokollet på `#tes`, `#process`, `#case-calyx`, `#case-horai` ned och upp, cpu 1 och 4,
wheel 100:60 och 20:120, `staircase 0`, `max_step` ≤ 3 %; `a11y_scan` + `reflow` vid 390 och
768; `tab_walk`; grep `prefers-reduced-motion` 0; inline-hex utanför `:root` inte fler än
före (CSS 16, markup/JS 2).

**Done when:** varje målrad har ett uppmätt värde som når målet, varje rad i `PARITET.md`
håller nivån i sin par-bild, grinden är ren eller varje avvikelse namngiven, och copy-agenten
har fått `COPY-V3d-v0.md` som underlag.

## Frågor till Anton (bygget stoppar inte; antagandet gäller tills svar)

| # | Fråga | Antagande |
|---|---|---|
| Q1 | `VI BYGGER ERT VARUMÄRKE.` bodde i jättesektionen. Får den bli femte och sista meningen i tesens sekvens (PRODUCT.md kallar den "Tesrubriken")? Alternativet är kapitelskärmen i processakten. | Mening 5 i tesen |
| Q2 | Tjänsterna numrerade 01 till 03 med underrader (PRODUCT.md § Product Purpose) försvinner med sektionen; namnen står kvar på kortets baksida. Ska numreringen synas någonstans igen? | Nej; processtegen 03 och 04 bär innehållet |
| Q3 | Etiketten "Exempelcase". Håller den, eller föredrar du "Så arbetade vi"? | "Exempelcase" |
| Q4 | Casetexterna är dikt om vår egen process för två tänkta verksamheter och säger det i första steget. Är tonen rätt, och får vi säga "en tänkt florist"? | Ja |
| Q5 | "Hur vi tänker" försvinner helt, även "Vi visar innan vi påstår" och "Sidan ska fungera för alla". Saknar du någon av dem? | Ingen flyttas |
| Q6 | Sidan blir ~34 viewports lång vid 1440 (i dag ~18,6). Casen står för ~12 av dem. Ok, eller ska Hōrai kortas till fem steg? | Ok |
| Q7 | Ramarna förblir `inert` (ingen klick i sajterna); de rullar bara i takt med sidan. Räcker det som "levande"? | Ja |
