# K1 Skymning, byggnoteringar

Arm B, koncept K1 enligt `concepts.md`. Ren HTML/CSS/JS i `index.html`, typsnitt från Google Fonts
(Newsreader 300/400 för rubrik, pris och adress; Schibsted Grotesk 400/500 för brödtext och etiketter).
Inga andra beroenden. Serveras från repo-roten på port 3101 så att ramen till `/sites/horai.html`
har samma origin.

## Målbild och referenser

Tier 2. Bilden är hela argumentet: ett foto av Stockholm i blå timmen bär första skärmen, rubriken
står i fotots mörka vattenband, exempelsajternas namn står som en rad i samma bild. Sedan hårt klipp
till vit grund, sedan mörkt igen.

Läst som bilder: `rogo/fold.webp`, `rogo/slices/02.webp`, `groupemontoni/fold.webp`.

- Från rogo lånas principen: ett skymningsfoto bär påstående och bevis i samma andetag, registret byter
  helt vid fållen (mörkt/foto till vitt/plant), varje påstående står bredvid en riktig skärmbild med
  bildsidan växlande. Inte lånat: logotypvägg, vit pillerknapp, annonsrad, cookiepanel.
- Från groupemontoni lånas: typen står rakt på fotot utan platta, mörkningen läggs bara i kanten där
  text står. Inte lånat: räknare i menyn, kortgrid, mosaik i flera färger.
- Inga färgkoder eller typsnitt från någon av dem. Paletten härleds ur skymningsfotot: vattnets
  blåsvarta (`--night`), fönstrens varma vita (`--light`), en enda kromatisk färg, fönsterbärnsten
  (`--amber`), som gör exakt två saker: understrykningen under `visitkort` och strecket under
  kontaktadressen vid hover. På vit grund används en mörkare variant (`--amber-ink`) för siffrorna
  01 till 03, så att den håller kontrast mot papperet.

## Beslut

- **Rubriken står nere till vänster, inte centrerad.** Fotots öppna band är vattnet i nedre vänstra
  hörnet (uppmätt medelluminans 31 av 255). Centrerat hade lagt texten över båten och de ljusa
  fasaderna.
- **Fönstret är ett fönster i Nationalmuseum**, längst till höger i bilden (87,6 % / 34,9 % av
  fotot, 7 % brett i 16:10). Där finns riktiga tända fönster, och det ligger långt från hotellet
  i mitten så att zoomvägen aldrig passerar dess skylt.
- **Hotellskylten är bortretuscherad** ur den vendrade kopian (en 60 x 32 px tegelremsa speglad in
  med mjuk kant). Vid första skärmen var den oläslig, men vid 35 % av zoomen blev den ett läsbart
  tredjepartsmärke i bilden.
- **Sajtnamnen** står i samma serif som rubriken, i lässtorlek, med en dämpad punkt mellan. Inga
  logotyper, ingen "trusted by"-text.
- **Toppbaren** är fast: logga vänster, adress höger, transparent över fotot, papper med hårlinje
  när det vita börjar, ljus igen över nattfotot. Under akt 3 visar den raden `Exempelsida: Hōrai,
  Asian fusion-koncept` i mitten (döljs under 640 px).
- **Tjänsterna** har korta underrader i byråröst utan kund- eller resultatpåståenden.
- **Paketen** är en typsatt liggare med hårlinjer, pris i displaygrad till höger. Inga kort.
- **Typsnitt.** Newsreader i vikt 300 för att målbilden vill ha en ljus serif som lägger sig i fotot
  utan att skrika. Sansen var först Instrument Sans; kedjans detektor flaggade den som överanvänd,
  så den byttes till Schibsted Grotesk, en nordisk tidningsgrotesk med ō-glyfen, utan att någon
  radbrytning ändrades (kontrollerat i `desk-fold`, `desk-ledger`, `desk-close`, `mob390-fold`).
- **Adressraden** i avslutet är `Alunix, webbyrå i Sverige. Skriv några rader om verksamheten, så
  hör vi av oss.` Ingen gatuadress, den finns inte i faktaunderlaget.
- **Mobil** (porträtt): fotot högerställs så att museet, kajen och vattnet syns; rubriken ligger
  kvar i vattnet. Raderna staplas under 760 px, liggaren blir en kolumn under 520 px.

## Akterna, vad som rör sig och hur det hänger i motivet

1. **Stillhet.** Fotot, rubriken, underraden, sajtnamnen. En drift på 1,8 % i skalan över elva
   sekunder, som en kamera på stativ i vind. Driften fasas ut så fort scrollen börjar.
2. **Drag.** Scrollen driver en kontinuerlig inzoomning mot fönstret: skalan går exponentiellt
   (`S^smoothstep(p)`, konstant upplevd hastighet) och fönstrets punkt flyttas samtidigt till skärmens
   mitt. Scrollvärdet lerpas (0,14 per bildruta), så rörelsen är mjuk i båda riktningarna. Rubriken
   och underraden bleknar och blurrar (0 till 14 px) under de första 30 % av zoomen, utan att flytta
   sig. Sajtnamnen ligger kvar längst ned tills 80 %, sedan tonar de.
3. **Avslöjande.** När fönstret (skärmbilden av Hōrai, som vid liten storlek läses som ett tänt
   fönster) fyller skärmen byts det mot den riktiga ramen: `/sites/horai.html` i en fast, otransformerad
   `iframe` som aldrig tonas. Ramen hålls i 60 vh scroll. Mushjul över ramen vidarebefordras till
   sidan (samma origin), så att besökaren inte fastnar inne i Hōrai; länkar och hover i ramen fungerar.
   Med pekskärm (coarse pointer) visas skärmbilden i stället för ramen, eftersom touch skulle scrolla
   ramen och inte sidan. Den ordningen tillåter målbilden.
4. **Klarhet.** Hårt klipp: den vita huvuddelen börjar exakt där heroplanen slutar (320 vh), så
   bytet är ett klipp, inte ett glid. `VI BYGGER ERT VARUMÄRKE.` stiger in ord för ord (radvis
   intoning, 80 ms förskjutning). De tre raderna: skärmbilden glider in från sin sida, texten från
   motsatt håll, en gång, när de passerar.
5. **Räkning.** Hårlinjerna i liggaren dras från vänster i takt med scrollen (procentstyrt, tre
   linjer i följd), raderna tonar in efter varandra.
6. **Landning.** Nattfotot av samma stad öppnar sig från horisontlinjen: en klippmask
   (`clip-path: inset`) går från 50 % till 0 medan sektionen kommer in. Sedan står allt stilla.
   Inget tonar bort.

Rörelseslag i ordning: scrubbad skalning + fade/blur, hård klippning, radvis intoning, riktad
inglidning, procentstyrd linjedragning, klippmask. Aldrig samma slag två gånger i rad.

**Reduced motion** stänger av allt ovan: heron blir en vanlig 100 vh-sektion med fotot och fönstret
i bilden, ramen med Hōrai blir en egen 100 vh-sektion under den (med bildtext), inget är dolt, inga
resor. **Utan JavaScript** gäller samma statiska layout; ramen ligger i `<noscript>`. Alla intoningar
är dolda bara under `html.motion`, observatören har tröskel 0, och en reserv efter 3 s visar allt om
den aldrig fyrar.

## Foton

- Skymning: Rafael Peier, Unsplash, `ZP5J5M3Q9qg`, https://unsplash.com/@rafaelpeier
- Natt: Julian Terenzio, Unsplash, `5UDPVmIdXUo`, https://unsplash.com/@julianterenzio

Fyra API-anrop av tolv: två sökningar (`stockholm skyline blue hour`, `stockholm night waterfront
lights`, 60 kandidater, 52 unika), två `download`-registreringar. Kandidaterna renderades som
kontaktark (52 miniatyrer, sedan tio i större storlek) och valdes efter hur mycket text de bär:
skymningsfotot har ett stort mörkt vattenband nere till vänster och tända fönster till höger.
Nattfotot är samma stad, mörkare, med en lugn himmel för toppbaren. Båda hämtade med
`w=2200&fm=webp&q=82`. Exempelsajternas skärmbilder och loggan kopierade från r3-bygget.

## Skärmbilder jag tittade på, i ordning, och vad jag ändrade

Alla tagna med `shots/shoot.py` (Playwright, Chromium) mot `http://127.0.0.1:3101`.

1. `desk-fold.png` (första körningen): fotot laddade inte, alt-texten stod i bilden. Zoomfönstret
   hamnade nere till höger i stället för i mitten. Klippet till vitt skedde vid 220 vh i stället för
   320 vh. `VARUMÄRKE.` bröts mitt i ordet.
   Ändrat: plattans centrering flyttades från `transform` till `translate`-egenskapen så att
   zoomtransformen inte skrev över den; klippet räknas nu på spårhöjden; max-bredden på tesrubriken
   togs bort; efter kontroll med `curl` visade sig bildfelet vara serverns (Pythons `http.server`
   återställer anslutningar under samtidig last, 2 av 16 parallella hämtningar kom tillbaka
   trunkerade). Ramen till Hōrai skapas därför i JavaScript först när skymningsfotot har laddat, så
   att dess tio parallella anrop inte tävlar med fotot; en bild som felar hämtas om en gång.
2. `desk-zoom-0.35/0.7/0.92.png`: fönstret centrerat och skalan rätt. Vid 0,35 var hotellskylten
   läsbar; retuscherad. Vid 0,7 var fönstrets skärmbild avhuggen i nederkanten: trunkerad
   överföring från servern, borta efter omordningen ovan.
3. `desk-hold.png`, `desk-precut.png`, `desk-cut.png`: ramen fyller skärmen otransformerad, radens
   etikett i toppbaren fick text-skugga för läsbarhet över Hōrais ljusa parti; klippet landar på den
   vita tesskärmen.
4. `desk-full.png` efter genomscroll i 300 px-steg: alla rader avslöjade (0 oavslöjade element),
   inget överflöde. Det mörka bandet överst i helsidesbilden är heroplanens spår, som en fixerad hero
   alltid ger i en helsidesfångst.
5. `desk-ledger.png`, `desk-close.png`: liggaren ritad, priser i displaygrad. `Skriv till oss` låg
   över en ljus fasad; mörkningen i nederkanten gjordes djupare (78 % höjd, 0,92 i botten).
6. `mob390-fold.png`, `mob390-full.png`, `mob320-full.png`, `tab768-full.png`: högerställd beskärning
   visar museet och fönstret; vid 320 bröts `VARUMÄRKE.` igen eftersom clamp-minimum låg på 44 px;
   sänkt till 32 px. Inget överflöde per element vid 320, 390, 768, 1440.
7. `desk-reduced-full.png`, `desk-reduced-frame.png`: allt innehåll synligt i rätt ordning, ramen
   som egen sektion med bildtext, inga rörelser (`motion`-klassen sätts inte).
8. `desk-zoom-reverse-0.55.png`: efter att ha passerat klippet och scrollat tillbaka står heron mitt
   i zoomen med bleknad rubrik, ramen släckt, huvuddelen dold. Båda riktningarna fungerar.
9. `desk-nojs-full.png`: JavaScript av, allt i flödet och synligt; ramen i `<noscript>` laddar
   (ostylad eftersom även Hōrais eget JavaScript är avstängt i den kontexten).

Granskningspass efter bygget: `emil-design-eng` (alla transitions namnger sina egenskaper, intoningar
med stark ease-out, inget skalas in från noll, scrubben är avbrytbar per bildruta, reduced motion tar
bort resor men inte innehåll: inga ändringar) och `humanizer-svenska` på de fem egna strängarna (inga
fynd; brieftexten är ordagrann och rörs inte).

Slutkontroll: konsolen fri från fel från sidan själv (den enda raden är Tailwinds CDN-varning inifrån
Hōrais ram), ramens dokument har `<title>` `Hōrai — A Three-Sister Restaurant, Stockholm`, inget
element utanför visningsbredden, inga tankstreck och inget "jag" i synlig text.

## Kända brister

- Under akt 3 kan ramen inte scrollas med mushjulet; hjulet driver Alunix-sidan så att besökaren
  inte fastnar. Klick, hover och tangentbord i ramen fungerar. Med pekskärm visas skärmbilden.
- Zoomen skalar fotot upp till omkring 15 gånger; mellan 5 och 12 gånger är fasaden mjuk. Det läses
  som kamerans resa, men det är en 2200 px-bild som bär den.
- Helsidesfångster visar heroplanens spår som ett mörkt band (320 vh) eftersom heron är fixerad.
- Pythons `http.server` trunkerar ibland svar under parallell last. Sidan skjuter upp ramen och
  hämtar om felade bilder, men en trunkerad bild som inte ger felhändelse kan inte upptäckas.
- I Hōrais ram ligger Alunix toppbar över Hōrais egen toppbar; loggan och adressen läses ändå.
