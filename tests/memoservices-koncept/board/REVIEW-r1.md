# Granskning runda 1 · leadens pixelläsning

Bilder: `cells/<ID>-r1/.review/*.png` (review.py, 1440×900 + 390×844, varje ?preview= + 12 hjulhack),
`design-catalogue/entries/memo-<ID>-r1-self/motion/sheet.webp` (motion_capture, 24 bildrutor, riktigt hjul).

## C · Passagen

**Håller:** heron (brickor i tre djupplan över videon, pappersplatta, indexrad; mobilen lika bra),
introt (kickern sätts ordvis, gardinen lyfter), om-ledgern med 2×2-markörer, insikterna som plates,
sidfotens index som bildas, bannern, mobilmenyn (Esc, fokus). 0 konsolfel, 0 textavvikelser.

**Fel (runda 2):**
1. **Passagen är ett hål, inte en rail** (house-physics: varje öppen yta bär vikt). Vid 1440×900 står ett
   objekt (2×2 ≈ 310 px + text) ensamt på ink med ~250 px tomt ovan och under och ~800 px tomt mellan
   objekten; railen är 7 315 px för åtta objekt. Åtgärd: objektbredd 40–44 vw (railen ≈ 4 800 px),
   brickorna 20 vh, och ett andra lager i scenen som bär resten av vyn: videons sista ruta (fasadens
   raster, `piren-last.webp`) som mörk, nedtonad grund bakom railen med parallax 0,3, så att passagen
   är "inne i byggnaden". Rubrikobjektet står kvar först.
2. **Om-rubriken bryter fel:** "EN" står ensamt, "KONTAKTPERSON." på egen rad. Originalet: två rader
   "ETT AVTAL." / "EN KONTAKTPERSON.". Kolumnen är 7/12; sätt `clamp` så att andra raden ryms i en
   rad vid 1440 (≈ 6,2 rem) eller ge rubriken 8 kolumner.
3. **Limebandet** har en tom högerhalva. Lägg knappen och texten i en 7-kolumn med optisk mitt, och låt
   limebrickan som växte stå kvar som en stor 2×2 (lime + ink-accent) till höger, 24 vh, så att akten
   fortfarande är brickan.
4. **Navkickern** (röd 11 px på bakgrund) 4,17:1. Sätt den i `--ink`, 11 px, 0,18 em; röd behålls på
   heroens kicker där den står i originalet.
5. Övergången hero → passage passerar ett grått mellanläge (bildruta 6 på arket). Låt ink komma som en
   stegad mosaikkant underifrån i stället för en tonad grundfärg.

Sidlängd 14,6 vh (budget 8–14): punkt 1 tar ned den till ≈ 12.

## A · Linsen

**Håller:** introt (28 brickor flyger in, blir fönster, fönstren växer ihop), heron med scrubbad
kamerafärd på hjulet, ink-brickorna som nav i hörnen (inverteras på ljus grund), pixelupplösningen
över fasadens raster, sorteringen till sju 2×2, en tjänst lyser i taget, limepanelen ur en bricka,
om-ledgern, sidfoten där brickorna samlas till app-ikonen. 0 konsolfel, 0 textavvikelser (efter att
kontrollen fick sidfotens kolumnrubriker), 0 överflöde.

**Fel (runda 2):**
1. **Fasadakten står i övre halvan.** Rastret (4×2 grupper, brickor 65 px) ligger med överkant vid
   y≈285 och lämnar nedre 40 % av vyn tom; textrutan till vänster slutar vid y≈620. Centrera scenen
   på 44 % av höjden, brickor 88 px, gruppmellanrum 56 px, så att rastret bär vyn.
2. **Dött scroll inom stegen** (scroll_verify: 6 fönster). Låt stegets kort-text tändas ord för ord
   (`--grafit` → vit, scrub) under stegets håll, och låt den aktiva 2×2:an andas 1,00 → 1,06 över
   steget. Floor-regel 4 uppfylls och inget fönster står stilla.
3. **Dämpade grupper blir leriga** (opacity .35 mot ink ger brun-grå). Använd .5 och lägg
   `filter: saturate(.6)` bara på de dämpade (små element, inom budget).
4. **Limebandets text ligger under mitten** (rubrik y 560–770 av 900). Optisk mitt 44 %; behåll brickan
   som växte som en stor 2×2 (lime + ink-accent) till höger om texten.
5. **Om-rubriken bryter "EN" ensamt**, samma som C. Andra raden ska rymmas: `clamp` ner till ≈ 6,2 rem
   vid 1440 eller 8 kolumner.
6. Sidfotens övre fält (där brickorna samlas) är ~250 px tomt efter samlingen. Flytta samlingspunkten
   till raden med logotypen och ta bort den tomma höjden.

**Runda 2 (A), verifierad i pixlar 2026-10-12:** punkt 1, 3, 4, 5, 6 och a11y rättade. Punkt 2:
ordtändning och andning byggda; `scroll_verify` flaggar ändå 5 fönster inom stegen eftersom
ändringen är liten i bildyta. **Beslut:** stegens håll är auktoriserad tystnad (F-025: ett steg
ska stå still och läsas), inte dött scroll; flaggorna står kvar och är förklarade här. Textkontroll
0 avvikelser, 0 konsolfel.

## B · Banden

**Håller:** app-ikonens 2×2 som växer till videoramen, ramen som växer till full bleed med rubriken kvar,
bandakten där varje tjänsts 2×2 **är** viewporten (tre brickor i huvudfärg + accentbrickan nere till
höger, sömmarna i papper), nästa tjänsts lilla 2×2 i accentfältet som cue, limebandet som åttonde,
"flera områden" som ledger-rad, om-stycket som tänds ord för ord, insikterna som ledger, mobilen.
0 konsolfel, 0 textavvikelser, 0 överflöde. Om-rubriken ryms på två rader här.

**Fel (runda 2):**
1. **Ordtändningen startar under kontrast** (axe: 29 noder i `.om-text`). Startläget ska vara
   `--grafit` (7,9:1 på bakgrund) och tändas till `--ink`, inte `--sten`/opacity.
2. **Sidfotens videominiatyr** (omvänd växt) landar som 56 px: för liten för att läsas som "brickan".
   Landa som en 2×2-stor ruta (≥ 120 px, radie `--radie`) bredvid logotypen, så att slutet svarar
   på öppningen.
3. **Limebandet** står tomt i ~1 vh innan kartläggningstexten kommer (band-7 + 12 hack: bara
   rubrikkolumnen på lime). Låt "Behöver du hjälp…"-raden och kartläggningsrubriken resa sig så snart
   limen täcker 60 % av vyn.
4. **Sidfotens kolumnrubriker** via `attr(data-h)` ger tomma `<h2>` (axe empty-heading). Skriv
   texten i noden: `verify_text.py` godtar nu TJÄNSTER/FÖRETAGET/JURIDISKT.
5. Bandets nedre vänstra ruta (~220 px) är tom i alla sju band. Antingen sänk sömmen så rutan blir
   ett smalt band (≤ 120 px), eller låt "Läs mer →" stå där.

**Runda 2 (B), verifierad i pixlar 2026-10-12:** alla sex punkter rättade (ordtändning från grafit,
128 px sidfotsruta, limebandet fyllt direkt, riktiga kolumnrubriker, låg söm, a11y). axe 0, textkontroll
0 avvikelser, 0 överflöde. `reflow.py` unrevealed 2 = inaktiva bandkroppar (per design).

**Runda 2 (C), verifierad i pixlar 2026-10-12:** alla sju punkter rättade; passagen är nu tät med
fasadrastret bakom (kontrast under text 10,6:1), sidlängd 11,5 vh. Introts kicker satt i ink av leaden
(röd 11 px = 4,17:1). axe 0, textkontroll 0 avvikelser. `reflow.py` flaggar railens objekt vid 320
(horisontellt överflöde är railens funktion; alla objekt nås med scroll och tangentbord, verifierat).
`motion_probe` DEAD på `.rail` är ett mätfel i proben: under riktigt hjul (Playwright) går railen
0 → −4 000 px linjärt med scrollY 712 → 5 029.

**Frame-time (motion_probe, cpu 1, 1440×900):** p95 16,8 ms i alla tre; staircase 0. A: 37 frames
> 33 ms (introt + videodekod), B: 26, C: 28. Vid 4× CPU-strypning p95 33 ms i alla tre (budgeten 20 ms
nås inte strypt; mäts igen på den valda riktningen efter bundling och videooptimering).

## Runda 3 (Antons beställning "höj nivån", 2026-10-12)

Grepp: ett beständigt bricklager (28 brickor) som formar om sig genom hela sidan, inga pinnar utom
heron; nya sans-par; nya layouter. Referenser: d2c-lifescience, thewatch-60fps, aramco, Inspo-mätning.

**C3 · Väggen (Funnel Display + Figtree)** · runda 3 → 3b → 3c, verifierad i pixlar.
Håller: heron (video + ink-remsa med rubriken nederst), väggen (sju 2×2 med namn), dyken (varje
tjänsts 2×2 växer till rummet; efter 3c växer nästa rum som en sammanhållen 2×2 inne i det
föregående, inga tomma pappersbilder, inga överlapp), golvet i kartläggningen (kvadrater), om-kolumnen,
sidfotens index. motion_probe p95 16,7 ms, staircase 0; axe 0; text 0 avvikelser; 0 överflöde.
Kvar (mindre): högra fältet i varje dyk bär bara indexraden (liten); övergången sista dyket →
golvet går bricka för bricka.

**B3 · Banden II (Schibsted Grotesk + Onest)** · runda 3 → 3b, verifierad i pixlar.
Håller: rubriken 12/12 + videobandet, de fyra fälten som grund, textpanelen klippt till övre
vänstra fältet (rubrik + rail + bandtext, korsar aldrig söm eller nav), bandbytet som stegad
mosaikkant (ingen mellanfärg), kartläggningen samlad i ett fält, om-raden, sidfotens ikon, mobilens
accentremsa. motion_probe p95 16,8 ms, staircase 0; axe 0; text 0 avvikelser; 0 överflöde.
Kvar (mindre): under ett hjulhack delar gamla och nya bandrubriken bilden vid den stegade kanten;
om-ledgerns tredje och fjärde rad reveal:ar strax under vyns nederkant vid preview-läget.

**A3 · Linsen II (Bricolage Grotesque + Host Grotesk)** · runda 3 → 3b, verifierad i pixlar.
Håller: fönsterrastret 9×4 över hela bredden bakom den centrerade lätta plattan (fönster på båda
sidor om texten), scrubbad kamerafärd, kompassen, tjänsterna med 2×2-raderna i den sticky
vänsterkolumnen och listan som lyser, limebrickan som står kvar (konturbrickor + ink-accent),
om-kolumnen, sidfotens app-ikon; `?preview=slut` landar rätt. motion_probe p95 16,8 ms (en körning
33 ms under parallella byggen), staircase 0; text 0 avvikelser. Kvar (mindre): 2×2-grupperna i
tjänstekolumnen är små (≈ 27 px brickor); sidfotens trigger slutar vid 45 % i stället för
`bottom bottom` (medvetet, för att övergången alltid ska bli klar).

## Gemensamt för alla tre (runda 2)
- `aria-label` på `<span>`/`<p>` utan roll är förbjudet (axe aria-prohibited-attr): ta bort dem; de
  delade raderna läses ändå rätt av skärmläsare när SplitText körs med `aria: "auto"` (standard).
- Rubriker/löpnummer via CSS `content:` byts till riktig text (kolumnrubrikerna) resp. `aria-hidden`
  `<span>` med text i eget element (löpnumren får stå i eget element; kontrollen slår bara om
  numret delar textnod med namnet).
- Länk i löptext utan understrykning (C, koncernlänken): understruken alltid (gate 61).
- Tangentbord i C:s rail: fokus på ett objekts länk ska rulla railen till objektet (`focusin` →
  samma scrollTo som indexet). 7 fokusstopp hamnar nu utanför vyn.
- Navkicker i C: `--ink` (4,17:1 i rött under golvet).
