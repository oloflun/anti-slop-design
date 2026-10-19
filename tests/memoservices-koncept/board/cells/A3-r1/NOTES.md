# A3-r1 · "Linsen II" · runda 3 + 3b

**Lane:** mörk film i gemener, där mosaiken är en lins över piren. De 28 brickorna är först fönster mot videon, sedan sidans kompass och därefter tjänsternas identitet genom resten av sidan.

**Auktoritet (TASTE § 1):** videon i första halvan (hero och fasad), därefter ytan: lime-bandet, ledgern och sidfoten. Grunden är `--ink` till och med tjänsterna, `--bakgrund` från och med kartläggningen och `--ink` i sidfoten.

## Runda 3b (leadens sex punkter)
1. **Hero:** fönsterrastret är 9×4 över hela bredden (cellstorleken räknas från bredden) och ligger bakom plattan. Plattan är 56 vw bred, centrerad och har opacity .9. De 28 brickorna sitter i kolumn 2–8, kolumn 1 och 9 är rena fönster, så fönster syns på båda sidor om texten. Vid ≤ 1023 px står rastret ovanför plattan, som tidigare.
2. **Tjänster:** 2×2-raden ligger i den sticky vänsterkolumnen under rubriken, i två rader (4 + 3, max 64 px per 2×2; på mobil 7 i en rad). Listan i högerkolumnen (kolumn 6–12) scrollar fritt, och inget lager ligger över texten. Den post vars text passerar 60 % av vyn lyser: 2×2:an får skala 1,12 och opacity 1, övriga .55. "Flera områden" tänder alla sju.
3. **Övergångarna är klara vid 45 %:** varje lagerövergång körs från att nästa sektions topp står vid 100 % av vyn tills den står vid 45 %. Sidfoten använder `clamp(top 45%)`, se avvikelserna. Ledgerns radtexter (om och insikter) reveal:ar vid `top 92%`. Markörerna landar sist i sina övergångar, och om-sektionen har tajtare luft (padding-top 10svh, rader på 18 px), så att fjärde raden redan visar text när dess markör landar. Uppmätt: när om-toppen står vid 39 % har alla fyra markörer landat och rad 4 är på väg in (opacity .6). Vid 51 % är markörerna fortfarande i luften.
4. **Kartläggning:** de samlade brickorna står kvar som en 2×2 på 24 vh i kolumn 6–7, till höger. Tre rutor är lime med 1,5 px ink-kontur och accentrutan är ink, med 7 brickor staplade per ruta. Lime-panelen växer ur 2×2:ans rektangel. Texten ligger i 7 kolumner (rubrik 1–5, text och knapp 3–5) med tyngdpunkten vid 44 % (mätt 0,440).
5. **`?preview=slut`:** `lenis.resize()` körs före hoppet. Lenis hade mätt sidan innan pin-spacern lades till och klämde därför "slut" mot en gammal gräns. Kroken landar nu längst ner, med sidfoten i vyn och app-ikonen bildad (läst som bild).
6. **Typsnitt:** Host Grotesk 400/600/700 ersätter Instrument Sans med samma roller och grader. Bricolage Grotesque är kvar som display. Knapparna och "Kontakta oss" mäts till `19px/700/"Host Grotesk"`.

## Typsnitt
| Roll | Familj | Vikt | Grad |
|---|---|---|---|
| Display (rubriker, tjänstenamn i listan, löpnummer) | Bricolage Grotesque, opsz 96 | 300, och 500 på det bärande ordet (KOMPETENS. / VÄXA / KONTAKTPERSON.) | `clamp(3rem, 7.5vw, 6.5rem)` med spärr +.012em och leading .95, begränsad av kolumnens container-enheter: hero 77 px (plattan är 56 vw), tjänster 68 px, kartläggning 104 px, om 93 px |
| Text | Host Grotesk | 400, 600, 700 | brödtext 17–18 px, kicker 13 px/700, knappar och hero-kicker 19 px/700 (stor text, så golvet är 3:1 mot brandröd) |

## Formationer (`#lager`, 28 brickor = 7 tjänster × 3 huvud + 1 accent)
| # | Sektion | Slot-mönster | Övergångsfönster | Ordning |
|---|---|---|---|---|
| F1 | Hero | `.hero-raster` 9×4 över hela bredden. Brickorna är ramar (2 px ink) på hålen i en ink-täckning (SVG-path, evenodd, 36 hål) | intro 1,4 s, fönstren öppnas rad för rad | — |
| F2 | Fasad (pin 260 vh) | `.kompass` 7×4 med 12 px-prickar nere till höger. Kolumnen för aktuell akt lyser | pin 0–30 %. Alla 36 hål växer ihop till full video | rad för rad |
| F3 | Tjänster | 2×2-raden i den sticky vänsterkolumnen | tjänsternas topp 100 → 45 % | rad för rad ur kompassen |
| F4 | Kartläggning | 2×2 på 24 vh (lime med kontur, ink-accent). Panelen växer ur den | 100 → 45 % (brickorna 0–60 %, panelen 55–100 %) | färg för färg |
| F5 | Om | 24 brickor i en 12 px-kolumn vid rubriken och 4 markörer i ledgern (röd ×3, lime) | 100 → 45 % | kolumnen uppifrån, markörerna sist |
| F6 | Insikter | en rad om 25 under INSIKTER och 3 kategorimarkörer (marin, brun, röd) | 100 → 45 % | raden från vänster, markörerna sist |
| F7 | Sidfot | app-ikonen 2×2 bredvid logotypen, 7 brickor per ruta (en från varje tjänst), röd ×3 och lime ×1 | `clamp(top 45%)`, sista triggern | tjänst för tjänst |

Övergångsorsaker: fönster som växer ihop, kompassen som lämnas rad för rad, samling till en 2×2 som blir bandet, delning till kolumn och markörer, samling till ikonen.

Mekanik: varje övergång är en tidslinje med `scrub: true` och en progress-proxy per bricka (`ease: "none"`). En `gsap.ticker`-funktion räknar om progress och levande slot-rektanglar till `transform` och opacity på `.b` och till färg och ram på det inre `i`. Vilan är en sinus på ±4 px (6–9 s) via `--dx/--dy` i CSS-`translate` på `i`, och den skrivs bara när värdet ändras. Pekaren lutar lagret 0,6 % via `quickTo` på `.flytt`. `will-change` sätts bara medan en övergång eller introt pågår.

## Signaturobjektets jobb
Fönster mot piren → kompass → tjänsternas identitet (lyser i lästakt) → 2×2:an som blir kartläggningens band → markörer och färgkolumn → app-ikonen.

## `?preview=`-krokar
`hero`, `fasad`, `tjanster` (första posten vid 60 %, övergången klar), `kartlaggning`, `om`, `insikter`, `slut`. Alla har lästs som skärmbild vid 1440 px. Dessutom har jag läst `tjanster` +12/+24/+36 hjulsteg, och övergången kartläggning → om steg för steg.

## Mätvärden (runda 3b, port 3104, headless)
- `verify_text.py`: **119 textnoder, 0 avvikelser**.
- `scroll_verify.py`: **deadScroll [], unrevealed [], cuesNeverFull []**. I `contrastUnderMedia` står samma tre poster som mäts fel som i runda 3: logolänken och "Kontakta oss" gömmer sin egen bricka, och kickern är 19 px/700 men mäts mot golvet för liten text.
- `contrast_over_media.py`, scroll 0 och 1200: **PASS**. Sämsta värden: kicker 3,24:1 (golv 3,0) och röda knappar 4,17:1.
- `motion_probe.py --track "#lager .b:transform" --cpu 1 --ticks 200`, tre körningar: p95 **16,8 / 16,8 / 33,3 ms**, staircase 0 i alla, dead false i alla. Bildrutor över 33 ms: 59 / 64 / 95. Förlusterna ligger i hero-pinnen (0–2000 px). När jag tog bort videon i ett test försvann de nästan helt, så kostnaden är videoavkodningen i headless utan GPU. Under mätningen körde maskinen cirka 45 andra Chrome- och Python-processer, troligen de parallella byggena. En all-intra-version och versioner med lägre upplösning (960/640) gav ingen säker förbättring och är borttagna. Sökningarna är begränsade till en per 50 ms.
- axe (`a11y_scan.py`, 1440 + 390): **0 överträdelser**, 1 ofullständig (färgkontrast över video).
- Konsolen: 0 fel och 0 svar ≥ 400 vid 1440/768/414/375/320 och för varje krok. Horisontellt överflöde: inget.
- Tangentbord: undermenyn öppnas med Enter, Tab går in i panelen och Esc stänger. Mobilmenyn byter mellan "Meny" och "Stäng menyn" och stängs med Esc.
- Kontaktark: `design-catalogue/entries/memo-A3-self/motion/sheet.webp` (24 rutor) är läst. Fönster syns på båda sidor om plattan, listan rullar fritt bredvid den sticky raden och 2×2:an bildas till höger i kartläggningen.

## Avvikelser och kända begränsningar
- **Sidfotens övergång:** den slutar vid `clamp(top 45%)` och inte vid `bottom bottom`. Det följer leadens regel att allt är klart vid 45 %, och `clamp` garanterar att övergången hinner bli klar på korta sidor. Det strider mot BRIEF-COMMON:s regel om `bottom bottom` för sista triggern.
- **Hela laddningen ligger i hero-pinnen:** se motion_probe ovan. Med riktig GPU-avkodning är det otestat.
- **Hand och JS där mallen inte räcker:** FÖRETAGET och JURIDISKT är skrivna i mallen, eftersom de är nycklar i `delat.json`. Logolänken har `aria-label="MemoServices"`. Koncernlänken, fetstilen i om-punkterna och det bärande ordet sätts av JS. Utan JS är texten komplett men har en enda vikt.
- **Mobil:** rastret står ovanför plattan och hero-pinnen startar vid `bottom bottom`, eftersom hero-sektionen är högre än vyn. Tjänsthuvudet är inte sticky där, så 2×2-raden rullar bort medan listan läses.
- **Hann inte:** en Teams-delning och mätning med riktig GPU.
