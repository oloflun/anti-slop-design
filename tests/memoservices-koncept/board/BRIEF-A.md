# Riktning A · "Linsen" · mosaiken som fönster mot piren

Cell: `tests/memoservices-koncept/board/cells/A-r1/` · port 3101 · `?preview=` krokar: `hero`,
`fasad`, `tjanster`, `kartlaggning`, `om`, `insikter`, `slut`.

**Lane (en fras):** mörk film, mosaiken som lins över piren.
**Register:** modern clean. **Grammatik:** filmic one-shot (en linjär rörelse, inga synliga sömmar,
en ingång). **Auktoritet (TASTE § 1):** videon. Typen viker: Archivo Black bara på rubrikerna, vit på
ink-platta; allt annat Arimo i vikt 400.
**Tell-someone:** "sajten där kontorsbyggnadens fönster blev de sju tjänsterna."
**Grund:** `--ink` från toppen till och med tjänsteakten (sidans mörka halva), sedan `--bakgrund`
från kartläggningen (lime) och framåt. En tonal inversion, exakt där videons fasad lämnar över.

## Känslokurvan (en rad per akt, känslan först, orsaken sedan)

| # | Akt | Känsla | Vad på skärmen |
|---|---|---|---|
| 0 | Intro → hero | Igenkänning | 25 brickor flyger in och bildar deras mosaik på svart; brickorna blir fönster: piren syns genom dem |
| 1 | Hero | Rymd | fönstren växer ihop, hela viewporten är piren, rubriken står still |
| 2 | Fasaden (toppen) | Insikt | kameran är inne i glasfasaden; fönsterrastret får färg, sju 2×2 sorterar sig ur det, var och en lyser i tur med sitt namn |
| 3 | Flera områden + Kartläggning | Lättnad | limeytan växer ur brickornas axel och sidan blir ljus |
| 4 | Om | Förtroende | två rader rubrik på papper, fyra punkter som ledger, en ruta per punkt tänds |
| 5 | Insikter | Kontinuitet | tre rader, kategorins brickfärg som markör |
| 6 | Slut | Svar på öppningen | brickorna samlas till app-ikonens 2×2 bredvid logotypen i sidfoten |

Peaken är akt 2 (störst spann, tystast före: hero-rubriken står still i 40 vh innan kameran går in i fasaden). Det tysta före peaken är avsiktligt och ska nämnas i NOTES.md så att `scroll_verify` inte läser det som dött scroll.

## Akterna i detalj

**Intro → hero (regel 1, ett tag).** Sidan laddar på `--ink`. Logotypen står uppe till vänster i en ink-bricka (se Nav). 25 brickor (facit-layouten + brun och sten, § 4) tweenas in från slumpade positioner utanför vyn till mosaikens läge mitt i högra halvan av vyn, `ease: CustomEase` med översving (originalets `cubic-bezier(.34,1.56,.64,1)` som `"back.out(1.6)"`-liknande kurva), stagger `{grid:[5,7], from:'random', amount:.6}`, 1,1 s. Sedan blir varje bricka ett fönster: videon ligger full-bleed under en ink-täckning som är en inline-SVG med `<mask>` där 25 `<rect rx>` är hålen; brickornas färg tonas till en tunn tint (opacity .18) och rects växer (`attr: {x,y,width,height,rx:0}`) tills hålen täcker hela SVG:n, 1,4 s, `power3.inOut`. Hero-rubriken reser sig ur sina radmasker (SplitText lines) **under** den sista tredjedelen av växten, så att intro och hero är ett tag. Vid vila: inget förhandsvisar fasad-akten.

**Hero (akt 1, pin, spann 300 vh, scrub: true).** `piren-scrub.mp4`: videons `currentTime` drivs av en scrubbad tween på ett vanligt objekt (`{t:0}` → `{t:video.duration}`) som skriver `video.currentTime` i `onUpdate` bara när skillnaden > 1/24 s och videon inte `seeking`; videon laddas som Blob efter första målning (performance.md § 1). Kameraturen är alltså hjulet. Vänster kolumn: ink-platta (opak, 46 % bredd på desktop, full bredd på mobil) med kicker (originalets, röd), rubrikens två rader, lead, ingress, de två knapparna (röd fylld + konturknapp, radie `--radie`, magnet på den röda). Rubriken står still i minst 40 vh (de första 40 % av pinnen gör plattan inget). Därefter driver plattan långsamt uppåt (yPercent −30) medan videon fortsätter, och fönsterrastret i fasaden närmar sig.

**Fasaden (akt 2, pin, spann 500 vh, scrub: true).** Orsak för övergången från heron: *pixelblock-dissolve* (Davide Cattaneo, Huehaus): ett raster av ink-brickor (8×5, samma enhet som mosaiken) täcker vyn i slumpad stagger medan videon står på sin sista ruta (fasadens raster). Under rastret ligger akt 2:s scen: samma ink-grund med 7 × (2×2) = 28 brickor som först är en oordnad spridning (de 25 hero-brickorna plus tre), och som på scrollen **sorterar sig till sju 2×2-grupper** på en rad/ett 4×2-raster (desktop) eller 2 kolumner (mobil), varje grupp med tre brickor i huvudfärgen och accentbrickan nere till höger. Det är SPEC:ens signaturrörelse: "sju områden, ett avtal" i form. Mekanik: Flip eller en per-bricka `.to({x,y})` i samma scrubbade tidslinje; brickor som byter färg gör det via `backgroundColor` i samma tween.
När grupperna är på plats: rubriken "DET DU BEHÖVER FÖR ATT VÄXA" (SplitText lines, vit) och
kickern. Sedan **lyser en tjänst i taget** (floor-regel 4): den aktiva 2×2:an står i full färg
och skalas 1,15, dess namn (Archivo Black) + `kort_pa_startsidan` + "Läs mer →" tonas in i en
textruta till vänster; de övriga sex dämpas till opacity .35. Sju steg, 55 vh var. Tidslinjen som
drivs av `.progress(p)` ska vara exakt 1 lång (`tl.set({}, {}, 1)`), och varje steg ska fungera
vid hopp och vid scroll tillbaka. Efter sjunde: "Behöver du hjälp inom flera områden?" + text +
"Kontakta oss →" tonas in som åttonde steg med alla sju lysande. Hela listan finns också som
vanlig HTML under scenen för tangentbord och JS-av (den är scenen; `gsap.set` döljer inget i CSS).

**Flera områden → Kartläggning (akt 3, flow).** Orsak: *panel som växer ur axeln*: en lime-yta
(`--lime`) växer från en bricka i mitten av raden till full bredd (clip-path inset scrub, 120 vh),
och sidans grund byter till `--bakgrund`. På limeytan: kicker, rubriken "HUR REDO ÄR DITT BOLAG…"
(ink, SplitText lines), texten, knappen "Starta kartläggningen ↗" (ink fylld, vit text).

**Om (akt 4, flow + reveal, `id="om"`).** Orsak: *mosaikkant*: papperets överkant mot limen är
en stegad kant i brickans enhet (clip-path polygon som animeras upp 24 → 0 px i steg). Kicker,
rubriken i två rader (vänster, 7 kolumner), texten + koncernraden; till höger de fyra punkterna som
ledger med hårlinjer (ingen kortruta), varje rad med en liten 2×2 som markör: tre brickor i
`--brand-rod` och accent `--lime` för de tre första, inverterat för den fjärde (originalet har röd
punkt ×3, lime ×1). Markören tänds (opacity .25 → 1, stagger 90 ms) när raden kommer in.
`<strong>` på fetstilsdelen enligt originalet.

**Insikter (akt 5, flow+in).** Rubrik "INSIKTER" + länken; tre artiklar som **ledger-rader**
(hårlinje under varje; inga kort): kategori·datum vänster, rubrik stor (Arimo 700, inte display),
utdrag i 52 ch, en bricka i kategorins färg (Redovisning marin, Skatt brun, Nyhet brandröd)
längst till vänster. Hover: raden lyfter 1 px och brickan skalar 1,1.

**Slut (akt 6).** Sidfot på `--ink`. Orsak: *brickorna samlas*: 25 små brickor som ligger spridda
över sidfotens övre del drar ihop sig till en 2×2 (röd, lime nere till höger, app-ikonen) bredvid
logotypen när sidfoten når viewporten (scrub, sista triggern `end: 'bottom bottom'`). Dörr in,
fönster ut. Kolumnerna TJÄNSTER (med 2×2 per tjänst), FÖRETAGET, JURIDISKT; copyright; koncernraden.
Konceptbannern är sidfotens allra sista rad i `--sand` på ink.

## Nav

Ingen full bar. Två **ink-brickor** fästa i övre hörnen (fixed, radie `--radie`, 8 px marginal):
vänster brickan bär logotypen och de fem länkarna i rad (Arimo 500, vit); höger brickan är
"Kontakta oss" (brandröd). Under heron är brickorna ink på video; när sidan blir ljus inverteras
de till `--bakgrund` med ink-text (en `[data-ground]`-trigger per sektion byter tema, som Era).
"Tjänster" i vänsterbrickan är en länk **och** en knapp (`aria-expanded`) som fäller ut brickan
nedåt till en panel med sju rader: 2×2 + namn, tangentbord, Esc stänger. Mobil (< 768): vänster
brickan är logotyp + `{{ny.meny}}`; menyn täcker vyn på `--ink` med alla poster + de sju
tjänsterna + "Kontakta oss".

## Enheter (≥ 4 familjer, aldrig samma två i rad)

intro-tidslinje → scrub (hero) → pin+scrub (fasad) → reveal/clip (lime växer) → reveal (mosaikkant) + flow+in (om, insikter) → scrub (slut). Pekare: magnet på "Se tjänsterna", tilt 6° på de sju 2×2 i fasadakten (hover:hover).

## Övergångsorsaker (≥ 3, aldrig samma två i rad)

fönster som växer ihop (intro→hero) · pixelblock-dissolve (hero→fasad) · panel ur axeln (fasad→lime) · mosaikkant (lime→om) · brickorna samlas (→slut).

## Vad som skiljer A från B och C (fingerprint)

Grammatik filmic · nav = två brickor i hörnen · hero = mosaik-fönster som växer till video, scrubbad kameratur · aktform: 2 pinnar (hero 300 vh + fasad 500 vh), ~11 vh totalt · slut = brickorna samlas till app-ikonen · signatur = fasadens raster sorterar sig till sju tjänster.
