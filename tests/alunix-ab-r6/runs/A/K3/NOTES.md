# K3 Konsolen, byggnoteringar

Byggd 2026-09-05/06. Sidan: `index.html` (all CSS och JS inline), bilder i `assets/`,
skärmbilder i `shots/`. Ingen commit.

## Beslut

**Sidans logik.** En yta man använder. Produkten (de tre exempelsajterna) och fotot bär;
Alunix eget material är chrome runt dem. Ingen knapp i heron, ingen "trusted by", inga tal
utöver de som läses av i realtid.

**Palett** (härledd ur fotot: kall vit vägg, ljus ek, grönt oskärpa; blått bara för handling):

| Roll | Värde |
|---|---|
| Grund | `#F1F2EF` (blek, svagt grågrön vit, som frostat glas) |
| Panel | `#FFFFFF` |
| Bläck | `#16191E` |
| Dämpad text | `#555C65` |
| Linjer | `#D7DAD4` / `#C3C7C0` |
| Handling och aktuellt läge | `#1E5E9C` (dagens Alunix-blå, behållen; den var redan rätt jobb) |
| Blå tint (aktiv flik) | `#E3ECF6` |
| Glas | `rgba(255,255,255,.62)` + `backdrop-filter: blur(18px) saturate(1.3)` |

Inga färgkoder eller typsnitt från katalogposterna (Bobbin: gul/svart, GT Standard/Alpina;
Customer.io: teal-regnbåge, Saans). Från Bobbin lånas principen "ett litet glaskort som
namnger exakt det som händer just nu"; från Customer.io principen "produkten står i ett
fotograferat rum, inte på platt färg" (heron är rummet, ramen är produkten).

**Typ.** En grotesk: Schibsted Grotesk 400/500/600 för allt (chrome, brödtext, etiketter,
siffror med `tabular-nums` bara där tal står i kolumn). Serifinslaget finns bara i den stora
rubriken: Newsreader 400, `visitkort` i kursiv och blått. Ingen mono.

**Layout.** Toppbar som app-chrome (56 px, fast): logga, tre flikar `01 Design` /
`02 Utveckling` / `03 System`, en tom plats där kortet landar, adressen. Hero 100svh med
foto och glaskort till höger. Pinnad scen med Hōrai i full bredd. Tes + dragspel i vänster
spalt, klistrad rampanel i höger. Typsatt pristabell (max 1040 px). Fält + knapp för mejl.
Sidfot med fotokredit och länkar till exempelsidorna.

**Copy som skrevs utöver den låsta.** Tjänsternas underrader (inga kund- eller
resultatpåståenden), hero-hint `Scrolla för att provköra en av våra exempelsidor`,
scenradens `Din scroll styr sajten` / `Klar. Sajten går att använda med musen.`,
formulärets `Vad gäller det?` och `Öppna e-post` med förklaringen att texten blir ämnesrad.
Kortets rader är bara sektionsnamn och procent som läses av ur ramen.

## Akt för akt, vad som rör sig och varför

1. **Lugn (hero).** Fotot glider i 0,28 × scrollhastigheten (förskjutning i annan hastighet
   än texten) tills heron lämnat. Kortet visar `Öppen just nu: Hōrai / Sektion: Huset /
   Läge: 0 %`, läst ur den redan laddade Hōrai-ramen. Den blå punkten pulserar.
2. **Övertagande (pinnad scen).** Scenen är `position: sticky` i 100svh − toppbar, och
   sektionens höjd är scenhöjd + resa. Under resan mappas sidans scrollY till ramens
   `scrollTop` (samma origin, `/sites/horai.html`) med en utväxling på ~1,75 så att hela
   Hōrai tar ungefär fem skärmhöjder. Mappningen är en ren funktion av scrollY, så den går
   åt båda hållen; värdet lerpas (0,25/bildruta) för mjukhet. En osynlig sköld ligger över
   ramen medan den är pinnad så att hjulet går till sidan, inte in i ramen. Hōrais egen
   `scroll-behavior: smooth` stängs av i ramens dokument så att styrningen är exakt.
   Kortet läser ramens sektion (svenska etiketter per sektionsindex: Huset, Köksnotisen,
   Menyerna, Rätterna, Rummet, Bokning) och procent, och flyttar sig under herons sista
   del från sin heroplats till scenens nedre högra hörn. **Detta är signaturen:** besökaren
   provkör Hōrais egen scrollkoreografi (parallax, citatet som formas) inifrån Alunix sida.
3. **Släpp.** När ramen nått sitt slut släpper scenen. Över de följande 280 px
   interpoleras kortet (position, storlek, hörnradie) till platsen i toppbaren och blir en
   chip som säger `Hōrai · Klar`; skölden tas bort så ramen går att klicka i medan den
   scrollar ut. Procentuellt scrollstyrt, båda riktningar.
4. **Sida vid sida.** `VI BYGGER` / `ERT VARUMÄRKE.` tonas in radvis (IntersectionObserver,
   en gång). Rampanelen avslöjas med klippmask underifrån (`clip-path: inset`). Dragspelet är
   native `<details name="tjanst">`, alltid ett öppet, och det öppna spjället byter ram:
   Design ↔ Calyx, Utveckling ↔ Hōrai, System ↔ Hyperborea. Ramarna byts med `hidden`,
   aldrig med transform eller opacitet, och laddas första gången de öppnas. Flikarna i
   toppbaren öppnar rätt spjäll och scrollar dit; aktiv flik = öppet spjäll medan akten är
   på skärmen. Chipen säger `Öppen just nu: <sajt>`.
5. **Villkor.** Tabellens hårlinjer ritas (scaleX) och raderna tonas rad för rad styrt av
   hur långt tabellen kommit in i rutan (`--p` på sektionen, kontinuerligt, inte
   engångsutlöst), så att akt 4 och 5 inte använder samma slags rörelse.
6. **Avslut.** Rubrik, fält och knapp tonas in en gång. Knappen öppnar
   `mailto:kontakt@alunix.se?subject=<det man skrivit>`. `Alla har rätt till bra design.` står
   i lässtorlek under adressraden.

Rörelseslag som används, i ordning: parallax → pinnad scen med procentuell styrning →
morf/procentuell resa → radvis intoning + klippmask → kontinuerligt scrollritade linjer →
engångsintoning. Inget slag två gånger i rad.

**Reduced motion.** Ingen parallax, ingen pinning (scenen är en vanlig 100svh-ram som
används med musen), inga intoningar (allt synligt direkt), tabellen ritad, kortet hoppar
mellan sina lägen utan interpolation, punkten pulserar inte.

**Utan JavaScript.** Ingen `.js`-klass → alla `[data-reveal]` synliga, tabellen ritad, kortet
dolt (det har inget att läsa), Hōrai-ramen och Calyx-ramen har `src` i HTML, skärmbilderna
ligger bakom ramarna som reserv. Kontrollerat med JS avstängt (`1440-nojs-full.png`).

## Foto

- Hero: TheStandingDesk via Unsplash, https://unsplash.com/photos/qMUr7Iq1Il4
  (fotograf: https://unsplash.com/@thestandingdesk). Vald för det lugna väggpartiet till
  höger, ingen människa, dagsljus, ingen "kontorsbild". Nedladdningsanropet gjordes enligt
  API-villkoren; hämtad som `w=2200&fm=webp&q=82` → `assets/hero-desk.webp` (2200×1236).
- API-anrop totalt: 3 (två sökningar, ett download-anrop).
- Sökningar: `desk natural light plant laptop documentary`, `workspace window light warm`.
  Kontaktark av 60 miniatyrer renderades och lästes; fyra kandidater hämtades i 960 px
  och jämfördes (Yen Vu, TheStandingDesk, Daniel Hansen, Annie Spratt). Yen Vus bild var
  mer dokumentär men hade en röd lampa som slogs mot den blå accenten och ett rörigt
  vänsterparti under rubriken.
- Exempelsajternas skärmbilder och loggan kopierade från `tests/alunix-concepts-r3/build/assets/`.

## Skärmbilder jag tittade på, och vad som ändrades efter varje

Alla i `shots/`. Verifieringsskript: `shots/verify.py` (huvudkörning: 1440×900, 390×844,
1440 med reduced motion, 320 och 768 för överflöde; genomscroll i 300 px-steg, per-elements
överflödesmätning, ramtitlar, konsol) och `shots/verify2.py` (morfbilder, flik 3, återscroll,
utan JS).

1. **Första körningen, `1440-fold.png`.** Heron visade ingen bild: `hero-desk.webp` och
   `demo-calyx.webp` fick `ERR_CONNECTION_RESET` från `python -m http.server`. Curl fick
   filerna felfritt; Chromium tappade de större svaren från HTTP/1.0-servern och hängde vid
   omladdning. Åtgärd: `shots/serve.py`, samma statiska server från repo-roten på port 3103
   men HTTP/1.1 med keep-alive. Därefter laddade bilden varje gång (4/4).
2. **`1440-release.png` (första).** Kortet mitt i morfen var en tom grå pill med båda
   innehållen halvt synliga ovanpå varandra. Ändrade korstoningen så att hela kortet
   lämnar över till chipen tidigt (t 0–0,25) och pillen som reser bär raden `Hōrai · Klar`.
   Kontrollerat i `1440-morph-0/1/2.png` (remsa: `_crop-morph-strip.png`).
3. **`1440-build.png` (första).** Rampanelen var tom: klippmasken låg på det observerade
   elementet och IntersectionObserver fyrade aldrig. Flyttade masken till barnet
   `.panel-plate` och lät omslaget vara oklippt. Panelen avslöjas nu (`1440-build.png`,
   `1440-build-tab2.png`, `1440-build-tab3.png`).
4. **Skiljetecken med luft** (`Exempelsida :  Hōrai ,`): global `font-feature-settings:
   "tnum"` gjorde kommatecken tabulära i Schibsted. Tog bort den globalt, satte
   `font-variant-numeric: tabular-nums` bara på kortets värden, priserna och fliksiffrorna.
5. **Överflöde vid 390 (första körningen).** Dragspelet stack ut 3 px: rampanelens
   bildtext (`white-space: nowrap`) gav gridkolumnen en min-bredd. `minmax(0,1fr)` på
   gridet, `min-width: 0` på bildtexten. Sedan: 0 element utanför vid 320, 390, 768, 1440,
   i varje 600 px-steg genom hela sidan.
6. **`390-sig-1.png`.** Mobilkortet bröt `Öppen just nu` på två rader. Etiketten döljs på
   mobil; raden är `ALUNIX ● Hōrai   Menyerna 50 %`. Hero-hinten låg över mörk oskärpa;
   slöjan på mobil gjordes tätare kring textblocket. Rampanelens bildtext får radbrytas på
   mobil i stället för att klippas med ellips. Kontrollerat i `390-fold.png`.
7. **`1440-sig-0/1/2.png`** (18 %, 50 %, 82 % in i resan): kortet läser Köksnotisen /
   Menyerna / Rummet, ramens `scrollTop` följer (1342 / 3724 / 6108 px), Hōrais eget
   citat formas mitt i bild. Återscroll till 72 % pinnar om och läser `Rätterna`.
8. **`rm-fold.png`, `rm-full.png`** (reduced motion): samma första skärm, scenen är en
   vanlig ram, allt innehåll synligt i rätt ordning, sidan 3893 px hög.
9. **`1440-full.png`, `390-full.png`** efter genomscroll i 300 px-steg: alla akter
   synliga; det klistrade och fasta (toppbar, scen) ritas på sin sista plats i
   helsidesbilder, vilket ger en ljus tom yta där scenen står. Det är en artefakt i
   helsidesfångsten, inte i sidan. Beskurna delar jag läste: `_crop-1440-bottom.png`,
   `_crop-390-top.png`, `_crop-390-bottom.png`, `_crop-rm-mid.png`, `_crop-nojs-top.png`.
10. **`1440-terms-entering.png`, `1440-end.png`, `390-after-release.png`.** Tabellen ritad,
    formuläret och sidfoten på plats, chipen i mobilens toppbar.

Slutläge: konsolen utan fel (enda posterna är Tailwind-CDN-varningen inifrån Hōrais egen
sida), alla ramar som visats har `<title>` i sitt dokument (Hōrai i scenen; Calyx, Hōrai,
Hyperborea i panelen när de öppnats), inget överflöde, reduced motion visar allt, inga
tankstreck och inget "jag" i synlig text.

## Kända brister

- Skärmbilderna togs mot `shots/serve.py` (HTTP/1.1), inte mot `python -m http.server`,
  eftersom den senare tappade bildsvar till Chromium på den här maskinen. Sidan i sig är
  identisk oavsett server.
- Under den pinnade scenen går det inte att klicka i Hōrai (skölden tar hjulet). Det är
  avsiktligt och sägs i scenraden; efter släpp är ramen klickbar.
- Kortet ligger över Hōrais nedre högra hörn under resan. Det är ett HUD och läser av
  ramen, men det skymmer en liten del av sajten.
- Hōrais egen toppbar kolliderar (`HŌRAI` mot `RESERVATIONS`) vid 390 px inne i ramen.
  Det är exempelsidans responsivitet, inte den här sidans, och ändras inte här.
- Rampanelens klippmaskavslöjande sker medan Calyx-ramen redan är synlig bakom masken.
  Det är en engångsreveal före användning; efter det rörs varken ram eller omslag.
- Mobilens chip byter till `Calyx` så snart dragspelet är i bild, vilket på 390 px sker
  strax efter släppet; `Hōrai · Klar` syns därför bara kort där.
- Webbtypsnitten hämtas från Google Fonts; utan nät faller sidan till systemtypsnitt.
