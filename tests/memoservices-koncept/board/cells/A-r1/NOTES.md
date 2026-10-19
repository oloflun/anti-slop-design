# A-r1 · "Linsen"

**Lane:** mörk film, mosaiken som lins över piren. Filmic one-shot, register modern clean.

**Auktoritet (TASTE § 1):** videon. Typen viker: Archivo Black bara på rubrikerna (vit på opak
ink-platta i heron), allt annat Arimo. Grund `--ink` till och med fasadakten, sedan lime och
`--bakgrund` (en tonal inversion där fasaden lämnar över), ink igen i sidfoten.

Filer: `template.html` (platshållare + inline CSS), `index.html` (renderad med `render.py`),
`main.js` (all rörelse; importerar bara `/gsap.js` och `/smooth-scroll.js`).

## Akterna

| # | Akt | Enhet | Spann | Övergångsorsak in |
|---|---|---|---|---|
| 0 | Intro | tidslinje (kinetic): 28 brickor flyger in (`msIn` = `.34,1.56,.64,1`, slumpad stagger .6), blir fönster (SVG-clipPath, 28 rects), tonas till .18 och fönstren växer ihop (1,4 s `power3.inOut`); h1 reser sig ur radmasker under sista tredjedelen | ~3,5 s; scroll/hjul/tangent under introt spelar klart det i 4× takt | (laddning) |
| 1 | Hero | pin + scrub: `piren-scrub.mp4` som Blob efter load, `currentTime` drivs av hjulet (>1/24 s, aldrig under `seeking`); plattan står still 0–40 %, driver −30 % 40–80 %, sista rutan som bild 74 %, pixelblock-dissolve 81–98 % | 300 vh | fönster som växer ihop |
| 2 | Fasaden | pin + scrub: 28 brickor i heromosaikens läge sorterar sig (x/y + `backgroundColor`) till sju 2×2; rubrik (SplitText lines i tidslinjen) + länk; sju steg à 0,095 (≈47,5 vh) där aktiv 2×2 = full färg, skala 1,15, övriga .35, namn + kort + "Läs mer →" till vänster; åttonde steget "flera områden" med alla sju tända; utgång 94,5–100 %: de sju drar sig mot radens axel | 500 vh (400 vh < 900 px bredd) | pixelblock-dissolve: 8×5 ink-brickor över videons sista ruta, fogarna visar fasaden, plattan lämnar uppåt |
| 3 | Kartläggning | scrub (clip): limeytan växer från en bricka mitt på radens axel (`inset(... round)` → 0), `power2.in` | 120 vh | panel som växer ur axeln |
| 4 | Om (`id="om"`) | scrub (stegad kant) + reveal: papperets överkant är en polygon i brickans enhet (bredd = bricka + fog, höjder 0/8/16/24 px) som planas ut; rubrik i radmasker, ledger-markörer .25 → 1 (stagger 90 ms) | kant: top bottom → top 12 % | mosaikkant |
| 5 | Insikter | flow+in: ledger-rader 14 px / 620 ms, stagger 60 ms; hover: raden lyfter 1 px, brickan 1,1 | flöde | (flöde) |
| 6 | Slut | scrub, sista triggern `end: 'bottom bottom'`: 28 små brickor spridda över sidfotens överdel samlas till app-ikonens 2×2 (tre papper, lime nere till höger) och den röda botten slår ut | sidfotens höjd | brickorna samlas |

Enhetsföljd: kinetic → pin/scrub → pin/scrub → clip-scrub → reveal → flow+in → scrub.
Övergångsorsaker: fönster växer ihop · pixelblock-dissolve · panel ur axeln · mosaikkant · brickorna samlas (fem, ingen upprepad).
Pekare (bara `(hover:hover) and (pointer:fine)`, `gsap.quickTo`): magnet på "Se tjänsterna", tilt 6° på de sju 2×2 (på ett inre lager, så skala/opacitet förblir fasadtidslinjens).

**Det tysta före peaken (avsiktligt):** heron står still i rubriken 0–40 % av sin pin (120 vh)
medan bara videon rör sig. När videon inte kan spelas (headless utan h264) syns postern, och det
spannet kan läsas som dött scroll. Det är den tystnad briefen beställer före akt 2.

## Signaturobjektet: brickan, fem jobb

1. Heromosaiken (28 brickor, facit + brun, sten, grafit, så alla sju huvudfärger finns).
2. Fönstret: varje bricka är ett hål i linsen mot piren.
3. Fasadens raster: ink-brickorna i upplösningen, med fasaden i fogarna.
4. Sorteringen: samma 28 brickor blir de sju tjänsternas 2×2 (signaturrörelsen).
5. Ytan och kanten: limen växer ur en bricka, papperets kant stegas i brickans enhet,
   och i sidfoten samlas brickorna till app-ikonen.

Tjänstens 2×2 finns också i Tjänster-panelen, mobilmenyn, ledger-markörerna och sidfotens TJÄNSTER.

## `?preview=`-krokar

`hero` · `fasad` (sorterad, rubrik inne) · `tjanster` (Redovisning tänd) · `kartlaggning`
(limen fullvuxen) · `om` · `insikter` · `slut`. Varje krok: `ScrollTrigger.refresh()` +
`lenis.resize()`, introt till slut, sedan `lenis.scrollTo(y, {immediate:true})`.
`window.__previewTargets()` ger målen i px. Kontrollerat 1440×900, 768×1024 och 390×844: varje
krok landar exakt (scrollY = mål).

## Runda 2 (leadens sju punkter)

1. Fasadscenen (textruta + raster) centreras på 44 % (nedre utfyllnad = övre + 12vh); brickor 88 px vid 1440 (krymper så att textkolumnen behåller ~330 px), gruppmellanrum 56 px.
2. Korttexten tänds ord för ord (grafit → vit, scrubbat över stegets håll) och den aktiva 2×2:an andas 1,00 → 1,06 (på tilt-lagret). **deadScroll är inte 0:** 1440: 5 fönster (diff 0,005–0,014), 390: 9 fönster, alla i fasadpinnen. Ordfyllningen och andningen rör för små ytor för verktygets tröskel på 1,5 % av hela bilden. Det som skulle räcka är en rörelse med stor yta inom stegen (t.ex. att rastret panorerar sidledes längs fasaden ~35 px per 300 px scroll), men det är en ny designändring och inte gjord.
3. Dämpade grupper: opacity .5 + `filter: saturate(.6)`, bara på de dämpade.
4. Kartläggningsblocket har sin tyngdpunkt på 44 % när limen är fullvuxen (mätt: kicker y 178, knapp y 620 av 900). Den vuxna brickan står kvar som en 2×2 på 24vh till höger (tre lime med hårlinje, ink-accent).
5. Om-rubriken har 8 kolumner; "EN KONTAKTPERSON." ryms på en rad vid 1440 (och på mobil, 7,4vw).
6. Sidfoten: övre fältet borta (80 px), brickorna sprids över hela sidfoten och samlas på logotypraden.
7. SplitText delar rubriken själv (h1/h2 får aria-label, inga span). Ordsplitten på korttexten använder `aria:"none"`. 0 element med aria-label utanför länkar, knappar och rubriker.

## Mätvärden (port 3101, headless Chrome)

- **Textkontroll** (`verify_text.py`, runda 2): 113 textnoder, 0 avvikelser (kolumnrubrikerna godtas nu av skriptet).
- **Konsol/nätverk:** 0 fel, 0 varningar, 0 svar ≥ 400 i alla körningar (preview × 7, fem bredder).
- **Horisontellt överflöde** (elementgränser, steg om 430 px genom hela sidan): 0 vid 320, 375,
  414, 768 och 1440. Inga tvåradiga knappar eller navlänkar.
- **contrast_over_media.py:** PASS, 13 strängar i folden. Kickern (röd, 19 px fet) 4,10:1 och de
  röda knapparna 4,17:1 mot golvet 3,0 (stor text).
- **scroll_verify.py 1440:** unrevealed 0, cuesNeverFull 0. deadScroll: 6 fönster, alla inne i
  fasadpinnen (5100–7500, diff 0,004–0,013). Det är lässtoppen inom ett tjänstesteg (briefen vill
  ha ett hållet steg per tjänst, F-025 kräver att texten står still ≥ 40 vh, och stegen på 47,5 vh (427 px) är
  längre än verktygets fönster på 300 px). Hero→fasad (tidigare 0,0001) och fasadens svans
  (tidigare 0,0) är åtgärdade med fograstret och utgången mot axeln. contrastUnderMedia listar
  "Kontakta oss" 1,0 (en mätartefakt: verktyget döljer hela knappen inklusive den röda ytan och
  mäter videon under) och kickern 4,1 mot verktygets golv på 4,5 (det sätter stor text först vid
  24 px; enligt WCAG är 19 px fet stor text, golv 3,0). 390×844: samma bild, deadScroll bara i
  fasadstegen.
- **blankBands** i den statiska helsidesbilden: pin-spacers och scrubbade akter (förväntat för en
  pinnad sida i en bild utan scroll).

## Avvikelser från briefen (medvetna)

- Hela navraden får plats först från 1080 px, så under 1080 px visas logotyp + `{{ny.meny}}` (briefen
  säger < 768). Annars bryts navlänkarna på två rader vid 768–1079. "Kontakta oss"-brickan visas från 600 px.
- Fasadstegen är 0,095 av 500 vh ≈ 47,5 vh, inte 55 vh, så att åttonde steget och utgången
  ryms i 500 vh.
- Ingen tonad grundfärg ink → papper under limeväxten: den gav en grå mellanton. Limen täcker
  ink helt, och papperet kommer med om-avsnittets stegade kant.
- Logotyplänkens `aria-label` är `{{meta.title}}` (ordagrant innehåll, men inte ur ny-text.json,
  som saknar ett företagsnamn).
- Koncernlänken i om-avsnittet och `<strong>` i om-punkterna sätts av `main.js` (mallspråket kan inte
  dela en sträng). Utan JS står texten kvar hel, bara utan länk och fetstil.
- Kategorifärgen på insiktsraderna går på radens plats (1 marin, 2 brun, 3 brandröd), inte på texten.

## Det jag inte hann

- Lässtoppen i fasadstegen är kvar som deadScroll (se ovan). Om det ska bort helt krävs en
  kontinuerlig storyta i varje steg (till exempel att den aktiva tjänstens färg blir ett band),
  vilket är ett designbeslut för nästa runda.
- `section_probe.py` och `perf_probe.py` (bildfrekvens per akt) är inte körda.
- Ingen a11y-audit utöver tangentbordstestet (Tjänster-panelen: Enter öppnar, Tab går in i
  panelen och vidare till "Insikter", Esc stänger och fokus går tillbaka till knappen; mobilmenyn:
  fokus på "Stäng menyn", Esc stänger, Lenis stoppas; fokus på en 2×2 i fasaden scrollar till dess
  steg).
