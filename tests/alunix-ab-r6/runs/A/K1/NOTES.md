# K1 Skymning, byggnoteringar

Byggd 2026-09-05/06. Ren HTML/CSS/JS i `index.html`, `style.css`, `script.js`. Enda externa beroendet
är Google Fonts (Newsreader, Schibsted Grotesk). Alla bilder vendrade lokalt i `assets/`.

## Beslut och varför

**Fotot bär.** Julian Terenzios blå timme över Riddarholmen (Unsplash `5UDPVmIdXUo`) valdes av
tre kandidater efter kontaktark: det har en rad tydligt upplysta fönster i den ockrafärgade
fasaden strax vänster om mitten (zoommålet), ett stort öppet himmelsband för rubriken och mörkt
vatten längst ned för bevisraden. Philip Myrtorps nattbild av samma stad (`pFOeZMpdmFk`) tar
landningen: samma vy, senare på kvällen, som målbilden ber om. Aldrig dag, inget platt ljus.

**Färg härledd ur fotot.** Natten `#0b1424` är vattnet i skymningsbilden, mörkat. Den enda
kromatiska färgen är fönsterljuset, uppmätt i bilden till ungefär `rgb(255,220,144)` och satt
som `#f2c46b` på mörk grund. Den gör en enda sak: understrykningen under `visitkort`, det bärande
ordet. Kontaktraden är vit. Vitt är rent `#ffffff` för att klippet ska vara hårt. Ingen färgkod
eller typsnitt är taget från rogo eller groupemontoni; från dem lånades principen (ett filmiskt
skymningsfoto som bär serifrubrik, bevis i samma bild, hårt registerbyte till plan vit grund där
varje påstående står bredvid en riktig skärmbild), inte pixeln.

**Typ.** Newsreader i vikt 200/300 med optisk storlek för rubriker, priser och kontaktraden: lugn,
ljus i vikt, stor men luftig, precis som målbilden ber om. Schibsted Grotesk för brödtext, ett
skandinaviskt tidningsgrotesk som passar en svensk byrå. Ingen mono; siffrorna i prislistan står
i serifen med tabulära siffror.

**Ordmärket.** Målbilden vill ha ALUNIX i lugn serif i bilden och den vita SVG-loggan uppe till
vänster. Loggan ligger inline med `fill: currentColor` bredvid ordmärket i Newsreader-versaler i
toppbaren, som är transparent över fotot, så ordmärket står i bilden utan att konkurrera med
rubriken.

**Bevisraden** `Calyx · Hōrai · Hyperborea` står som textlänkar i vattnet längst ned på första
skärmen. Inga logotyper, ingen "trusted by". Den stannar kvar tills fönstret tar över.

**Ramen får användas.** Under resan har ramen `pointer-events: none` (man tittar in genom ett
fönster), när den fyller skärmen blir den klickbar och scrollbar. Ramelementet transformeras
aldrig och tonas aldrig: avslöjandet sker med `clip-path: inset()` på ett omslag med ramen i full
storlek därunder, och det som tonar är ett glödskikt och skärmbildsplåten ovanpå, inte ramen.
Plåten (`demo-horai.webp`) ligger kvar tills ramdokumentet rapporterar en `<title>`.

**Hårt klipp.** Den vita grunden ligger med `margin-top: -100vh` under den pinnade scenen och
glider in dold under den. När herons behållare tar slut sätts scenen `visibility: hidden` och
vitt står redan på plats. Utan JS eller med reduced motion finns ingen underlappning.

## Akt för akt, vad som rör sig och hur det hänger i motivet

1. **Stillhet.** Fotot, rubriken, underraden, bevisraden. Enda rörelsen är en svag andning i
   bilden (skala 1,000 till 1,018 över 38 s) med samma transform-origin som zoomen, så den är
   början på kamerarörelsen, inte en dekoration. Andningen dör ut under första fjärdedelen av
   resan.
2. **Drag.** Scrollen driver kameran: skalan går exponentiellt från 1 till 22 mot fönstret
   (0,457 in, 0,577 ned i bilden) medan bilden samtidigt förskjuts så att fönstret hamnar i
   skärmens mitt. Exponentiell interpolation ger konstant upplevd hastighet. Rubriken lämnar
   bilden genom att tona och blurra (0 till 14 px) under de första 30 procenten, aldrig genom att
   skjutas. Fönstret tänds när kameran börjar röra sig (rektangeln växer från 0 under de första
   8 procenten) så att fotots eget fönster är det som syns i stillhet. Bevisraden står kvar och
   tonar först vid 60 till 74 procent, när fönstret tagit över.
3. **Avslöjande.** Vid 78 procent slutar fönstret följa fotot och öppnar sig till hela skärmen,
   fotot fortsätter mjukt till skala 27 och mörknar (75 procent natt) utanför. Glöden i fönstret
   tonar bort när rektangeln är ungefär en tiondel till en fjärdedel av skärmbredden, och rummet
   bakom visar sig vara Hōrais egen sida, live i ramen. Sedan 100vh scroll där ramen är hela
   skärmen, klickbar och scrollbar, med raden `Exempelsida: Hōrai, Asian fusion-koncept · Öppna
   sajten` nere till vänster. Toppbaren får en mörk halvgenomskinlig botten här så adressen inte
   läggs rakt över Hōrais knapp. Hela resan är en enda funktion av `scrollY`, så den går lika
   mjukt bakåt.
4. **Klarhet.** Hårt klipp till vitt. `VI BYGGER ERT VARUMÄRKE.` tonar in radvis (två rader med
   140 ms mellan), raden under följer. Sedan tre uppslag: Design bredvid Calyx, Utveckling bredvid
   Hōrai (bilden på vänster sida), System bredvid Hyperborea. Skärmbilden glider in från sin sida,
   texten från motsatt håll, en gång, när uppslaget passerat 82 procent av skärmhöjden. På mobil
   glider båda uppåt eftersom det inte finns någon sida att komma från.
5. **Räkning.** `Alla har rätt till bra design.` tonar in som rubrik, sedan tre rader där
   hårlinjen ritas från vänster (scaleX 0 till 1) och texten och priset avslöjas med klippmask:
   texten öppnar sig från vänster, priset från höger. Pris i stor grad till höger, ingen kortrad.
6. **Landning.** Nattbilden glider långsammare än texten medan sektionen kommer in (12vh
   förskjutning som når noll när sektionen fyller skärmen), sedan står allt stilla. Inget tonar
   bort. `kontakt@alunix.se` i stor grad som mailto, raden `Alunix, webbyrå i Sverige. Webbdesign,
   design och system.`, de tre exempelsidorna och fotokrediterna.

Rörelseslagen i ordning: skalning kopplad till scroll och klippmask som följer den (signatur),
tona och blurra, radvis intoning, sidoglid, ritad linje plus klippmask, parallax i annan
hastighet. Aldrig samma slag två gånger i rad.

**Reduced motion / utan JS.** Klassen `motion` sätts bara av JS när
`prefers-reduced-motion: reduce` inte gäller. Utan den är allt i CSS statiskt: fotot 100vh med
rubrik och bevisrad, sedan ramen som ett eget block på 100vh med bildtext, sedan vitt, allt
synligt i rätt ordning. Ingenting börjar dolt utan JS. Med JS finns dessutom en reserv som visar
allt som står i bild efter 6 s om ett avslöjande inte hunnit fyra, och en bild som inte laddat
första gången får ett andra försök.

## Fotokrediter

- Skymning (första skärmen): Julian Terenzio, Unsplash,
  https://unsplash.com/photos/a-view-of-a-city-at-night-from-across-the-water-5UDPVmIdXUo,
  https://unsplash.com/@julianterenzio
- Natt (landningen): Philip Myrtorp, Unsplash,
  https://unsplash.com/photos/a-night-view-of-a-city-with-a-bridge-and-a-body-of-water-pFOeZMpdmFk,
  https://unsplash.com/@philipmyr

API-anrop: 2 sökningar (`stockholm skyline blue hour`, `stockholm night waterfront lights`) och
2 `GET /photos/<id>/download`, totalt 4 av högst 12. Bilderna hämtades från `urls.raw` med
`&w=2200&fm=webp&q=82` (2200×1467 och 2200×1237) och fick lokala 1100 px-varianter till srcset.
Logotyp och skärmbilder kopierades från `tests/alunix-concepts-r3/build/assets/`.

## Skärmbilder jag läste och vad jag ändrade efter varje

Alla i `shots/`. Skjutna med `shots/shoot.py` mot `http://127.0.0.1:3101/...` (servern
`python -m http.server 3101` från repo-roten).

Omgång 1 (skrivbord 1440×900):
- `d-00-fold`: rubriken i himlen fungerar, bevisraden i vattnet fungerar. Fönstret syntes som en
  liten vit rektangel i fasaden redan i stillhet. → Fönstret tänds först när scrollen börjar och
  får ett varmt glödskikt tills rummet syns.
- `d-zoom-*`: resan går som tänkt; vid p=1,0 låg `kontakt@alunix.se` rakt över Hōrais
  RESERVATIONS-knapp. → Toppbaren får mörk botten medan ramen fyller skärmen.
- `d-cut`: "VARUMÄRKE" hade tappat prickarna över Ä, radens `overflow: hidden` med radhöjd 0,98
  klippte dem. → Tog bort overflow, lade padding-top på raden.
- `d-white-4`: landningens text stod centrerad på sidan i stället för i vänsterspalten (auto-
  marginaler på `.wrap` som flex-barn i kolumn). → `.land > .wrap { width: 100% }`. Mörkningen
  under kontaktraden var för svag mot de upplysta fasaderna. → Starkare gradient längst ned.

Omgång 2 (mobil 390/320/768, reduced motion):
- `m390-fold`: glöden syntes som en gul lapp i fasaden i stillhet på mobil. → Samma åtgärd som
  ovan (fönstret tänds vid scroll), bekräftat i omgång 3.
- `m390-white-0`: tesen bröt till tre rader med `ERT` ensamt. → Mindre grad på mobil så
  `ERT VARUMÄRKE.` får plats på en rad.
- `rm-full`: två skärmbilder visades som trasiga med alt-text; konsolen visade
  `ERR_CONNECTION_RESET` från `python -m http.server`, som tappar anslutningar under parallell
  last (även `curl` parallellt gav bara 4 av 8 svar). → Lade in ett andra försök på bilder som
  fallerar, och lät skärmbildsskriptet fylla samma URL:er från disk via Playwright-route så att
  verifieringen mäter sidan, inte testservern. Servern på 3101 körs fortfarande för ramarna.

Omgång 3:
- `d-zoom-4-p100` och `d-hold-late`: hela skärmen suddig och mörk, toppbaren hopklämd åt vänster.
  Orsak: toppbaren fick klassen `frame`, som också är ramelementets klass, och ärvde `height: 100%`
  och `display: block`. → Bytte klassnamn till `overframe`. Bekräftat rätt i omgång 4.
- `d-end`: sista skärmen står stilla, kontaktrad, exempelsidor och krediter läsbara.
- `m390-white-0`: tesen på två rader. `m390-white-2`, `m390-white-3`: prislistan i en spalt, pris
  under texten, fungerar.
- `rm-full`: de tre skärmbilderna i uppslagen syntes som tomma ramar eftersom de laddas lazy och
  helsidesbilden togs utan genomscroll. → Skriptet scrollar igenom före helsidesbilden; alla sex
  bilder rapporterar `complete` i omgång 4. Ingen ändring i sidan behövdes.

Omgång 4 (slutlig): `d-00-fold`, `d-zoom-0-p22` (fönstret tänt, litet), `d-zoom-1-p50`,
`d-zoom-2-p72`, `d-zoom-3-p90` (fönstret öppnar sig), `d-zoom-4-p100` (ramen hela skärmen,
bildtext, toppbar med botten), `d-cut-1`, `d-cut`, `d-cut+400`, `d-white-0` till `d-white-4`,
`d-end`, `d-full`, `m390-fold`, `m390-zoom-p50`, `m390-zoom-p90`, `m390-white-0` till `-3`,
`m390-full`, `m320-fold`, `m320-full`, `m768-fold`, `m768-full`, `rm-fold`, `rm-frame`, `rm-full`.

Mätt i sista omgången: inga konsolfel från sidan (enda posten är Hōrais egen varning om Tailwinds
CDN inuti ramen), ramdokumentets titel `Hōrai — A Three-Sister Restaurant, Stockholm`, inget
horisontellt överflöde per element vid 320, 390, 768 och 1440 (element som klipps av en
`overflow: hidden`-förälder, alltså det skalade fotot inne i scenen, räknas inte),
`scrollWidth` lika med viewportbredden överallt, alla sex bilder laddade.

## Kända brister

- Helsidesbilderna (`*-full.png`) visar heron som ett stort mörkt block: en pinnad scen kan inte
  fångas i en helsidesbild. Läs skärmhöjdsbilderna för den delen.
- Vid skala 22 till 27 är fotot uppförstorat långt förbi sin upplösning. Det läses som oskärpa
  utanför fönstret och mörkas, men ett foto med högre upplösning skulle ge en renare avslutning.
- Fönstret i fotot är högt och smalt, ramen är 16:9. Rektangeln som tänds är därför något bredare
  än fönstret den ligger på.
- Under det sista hundratalet vh, när ramen fyller skärmen, händer inget nytt på Alunixsidan;
  det är där Hōrai får användas. Scrollhjulet över ramen scrollar Hōrai, och sidan fortsätter när
  ramen nått sitt slut (webbläsarens scrollkedja).
- `python -m http.server` tappar anslutningar under parallell last; sidan har ett andra försök
  för bilder, men en riktig server behövs för en riktig driftsättning.
- Toppbaren över ramen täcker Hōrais övre 60 px medan ramen är hela skärmen (även i det statiska
  läget, där den får samma mörka botten när ramblocket ligger under den, kontrollerat i `rm-frame`).
