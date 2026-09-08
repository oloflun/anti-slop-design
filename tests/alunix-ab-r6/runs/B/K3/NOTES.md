# K3 Konsolen, byggnoteringar

Sidan: `index.html` (all CSS och JS inuti). Kontroll: `python shoot.py <runda>` från denna mapp med
servern igång på 3103 från repo-roten. Skjuter allt som listas under Verifiering och skriver
konsol, ramtitlar, överflöde per element, reduced motion och no-JS till stdout.

## Beslut

**Lane.** "Ljus konsol i dagsljus": en yta man använder. Register modernt, rent, ljust.
Ingen grain, inga kickers, inga mono-etiketter. Apparaten är toppbaren med tre flikar och ett
glaskort som läser av riktig information.

**Referenslås.** Dominant: `bobbin` (glaskort över dokumentärt skrivbordsfoto som säger vad som
händer just nu; dragspel bredvid den skärm som visar just den funktionen). Detalj från
`customer-io`: produkten står i ett verkligt rum, en enda grotesk, en enda handlingsfärg.
Förkastat från båda: logotypväggar, trust-rader, pillerknappar, gult, regnbågsord.

**Typ.** En grotesk: Schibsted Grotesk (skandinavisk tidningsgrotesk, lugn, tabellsiffror
för procent och priser). Serif bara i rubrikens ord `visitkort`: Newsreader, roman, i accentblått.
Inga kursiver i rubriker.

**Färg.** Varmvit grund `oklch(0.985 0.006 80)`, kall bläcksvart `oklch(0.22 0.012 250)`,
blått `oklch(0.47 0.13 252)` (dagens Alunix-blå översatt till oklch) bara för handling och
aktuellt läge: aktiv flik, knappen, procenttalet, öppet spjäll. Levande punkt i grönt är det
enda andra kulörta. Alla toner är tokens; inga hexvärden från katalogposterna.

**Foto.** Annie Spratt, Unsplash `gdi9fJboJQU`, https://unsplash.com/@anniespratt.
Valdes ur ett kontaktark på 60 kandidater (två sökningar). Kriterier: dagsljus, ingen människa,
inget varumärke i bild, ett lugnt parti till höger. Bortvalda efter närmare titt: `iZ4QZFbQ2S8`
(Dell-logga synlig), `3zWXZyg_NXI` (mikrofon och böcker, läses som poddstudio), `0pXpp7jEZOo`
(för mörkt för det ljusa registret). Bilden ligger som `assets/hero-desk.webp`, 2200 px, 296 kB.
API-anrop totalt: 3 (två sökningar, ett download-anrop).

**Copy utöver det ordagranna.** Tre underrader för tjänsterna, en rad under paketrubriken, en
förklaring under mejlknappen, en mening efter `Alla har rätt till bra design.`. Inga tal, inga
kunder, inga citat. En rad om moms togs bort efter genomläsning eftersom den inte står i briefen.

## Akterna, vad som rör sig och hur det hänger i motivet

Motivet är konsolen: sidan är en yta som visar vad som händer, och kortet är instrumentet.

1. **Lugn.** Foto fullbredd med mjuk kant (mask nedåt, cremeslöja från vänster). Rubrik, underrad,
   två knappar. Glaskortet till höger: `Öppen just nu: Hōrai`, `Sektion: Entré`, `Läge: 0 %`,
   levande punkt, loggan i kortets övre kant. Rörelse: fotot skalas 1 till 1,09 och glider
   nedåt kopplat till scrollen (skalning kopplad till scroll).
2. **Övertagande, signaturen.** Scenen pinnas i 100 svh med raden `Exempelsida: Hōrai, Asian
   fusion-koncept` och ramen som fyller resten. Scenens höjd sätts till 100 svh + ramens
   scrollbara längd (1:1, tak 7000 px), så ett scrollat pixelsteg på sidan är ett steg i Hōrai.
   Ramens `scrollTop` interpoleras (lerp 0,22 per bildruta) mot målet, båda riktningarna.
   Kortet flyttar samtidigt från heroplatsen till scenens nedre högra hörn (interpolerad
   förskjutning med skala) och läser sektion och procent ur ramen varje bildruta. Scrollar
   besökaren inuti ramen med musen i stället flyttas sidan så att båda stämmer, så pinningen
   bryts aldrig. Hōrais egen `scroll-behavior: smooth` stängs av från föräldern så styrningen
   är direkt.
3. **Släpp.** När ramen nått sitt slut släpper scenen. Kortet säger `Klar`, `100 %`, krymper
   och glider upp mot toppbaren över 0,45 skärmhöjd, tonar ut sista biten och ersätts av en
   liten chip i baren med samma information (kortet självt förflyttas, aldrig ramen).
4. **Sida vid sida.** `VI BYGGER ERT VARUMÄRKE.` avslöjas med klippmask från vänster; raden
   och de tre spjällen tonar in radvis med 90 ms förskjutning. Dragspelet är native `<details
   name>` (exklusivt, utan JS), och det öppna spjället styr vilken ram som visas i den klibbiga
   scenen till höger: Design ↔ Calyx, Utveckling ↔ Hōrai, System ↔ Hyperborea. Flikarna i
   toppbaren öppnar rätt spjäll och scrollar dit; aktiv flik markeras i blått. Chippen i baren
   läser nu av den öppna ramen i stället (sajt, sektion, procent).
5. **Villkor.** Typsatt tabell, tre rader, pris höger i displaystorlek. Hårlinjerna ritas från
   vänster (scaleX) med 120 ms förskjutning när raden kommer in.
6. **Avslut.** Mörk grund. `Skriv till oss`, ett riktigt textfält och knappen `Öppna mejl` som
   öppnar `mailto:kontakt@alunix.se?subject=<raden>`. Under: `Alla har rätt till bra design.`
   i lässtorlek. Formulär och sidotext tonar in radvis. Sidfot med logga, exempelsidor och
   fotokredit.

Rörelseslag i följd: skalning → pinnad scen med procentstyrd ram + interpolerad kortresa →
klippmask → radvis intoning → ritade linjer → radvis intoning. Inget slag två gånger i rad.

**Reduced motion.** Fotot står stilla, kortet ligger kvar i heroflödet, scenen är en vanlig
100 svh-ram utan pinning (Hōrai scrollas med musen, kortet läser ändå av den), inga
intoningar, inga klipp, chippen i baren visas utan övergång när heron passerats, punkten
pulserar inte. **Utan JS**: allt synligt, ingen opacitet 0, scenen 100 svh.
Intoningar har tröskel 0, avslöjar det som redan syns vid start och har en 2,5 s-reserv.

`?preview=<0..1>` landar mitt i signaturrörelsen för skärmbilder.

## Skärmbilder jag tittade på, och vad som ändrades

Rundor `r1` till `r5` i `shots/`. Filnamn `r<n>-<bredd>-<vad>.png`.

- **r1** (`1440-fold`, `1440-full`, tre `1440-scene-*`, `1440-release`, `390-full`,
  `1440-reduced-full`). Avslutssektionen var byggd som klibbig sidfot (`sticky; bottom:0`) och
  låg över varje skärm: rubriken och kortet syntes inte i första skärmen och kortet saknades i
  scenen. Tog bort tricket helt. Chippen flödade över vid 320 och 390 (mätt per element):
  ordmärket i baren döljs under 560 px, chippen visar bara procent under 420 px. Tipset
  `Scrolla: sidan i ramen följer med` syntes under reduced motion trots att inget pinnas:
  dolt där. `Klar` lämnade över till nästa ram för tidigt: bytet sker nu först när
  tjänstesektionen kommer in.
- **r2** (`1440-fold`, `1440-scene-0.5`, `1440-release`, `1440-full`, `390-full`, `390-fold`).
  Första skärmen rätt. Kortet fortfarande osynligt i scenen; mätte geometrin i webbläsaren:
  kortet stod på rätt plats (1084, 716) men målades under ramen. Orsak: `isolation: isolate`
  på heron gav det fixerade kortet en egen staplingskontext som ligger under den senare klibbiga
  scenen. Tog bort isoleringen. Släpp-bilden togs 0,7 skärmhöjd efter släpp, vilket redan är
  nästa akt; flyttade till 0,3.
- **r3** (`1440-scene-0.15`, `1440-scene-0.85`, `1440-release`, `1440-reduced-full`).
  Kortet ligger i scenens hörn med `Huset 15 %` respektive `Rummet 85 %`. Chippen säger
  `Hōrai Klar 100 %` vid släpp med kortet synligt mitt i resan. Reduced motion visar hela
  sidan i rätt ordning på 3807 px.
- **r4** (`1440-services-system`, `768-fold`, `390-services`, `390-terms`, `390-scene`).
  System öppet visar Hyperborea, aktiv flik blå, chip `Hyperborea Entré 0 %`. 768 håller.
  390: dragspel och ram staplade, tabellen läsbar med pris under texten. Scenraden bröt på två
  rader i 44 px fast höjd: `min-height` i stället. Tab-vandringen visade att textfältet
  saknade synlig fokusring (bara kantfärg): la till `:focus-visible`-ring. Detektorn flaggade
  `transition: width` på kortets mätare: bytte till `transform: scaleX`.
- **r5** (`1440-fold`, `1440-scene-0.5`, `390-fold` lästa; hela sviten körd). Rent.

**Mätningar (r5).** Konsol: inga fel från sidan; enbart Tailwinds CDN-varning från
exempelsajterna själva. Alla fyra ramar visar sin sajt med `<title>`. Överflöde per element
vid 320/390/768/1440 i båda rörelselägena: inget, utom heroens bild som skalas 1,09 inuti
en `overflow: clip`-behållare (scrollWidth = viewport i alla fall). Kontrast mot den renderade
plåten med texten dold, ljusaste 5 % under varje sträng: rubrik 16,2:1, `visitkort` 6,5:1,
underrad 8,0:1, kortets etiketter 4,7:1 som lägst. `scroll_verify.py`: inget dött scrollavstånd,
inga cues som inte når full opacitet, inget oavslöjat; det enda `blankBand` är den pinnade
scenen i helsidesbilden, som är väntat för en pinnad akt. Tvåvägssynk testad: scroll inuti
ramen till 3500 flyttade sidan till 4187 och kortet till `Menyerna 47 %`; scroll tillbaka gav 5 %.

## Fotokrediter

- Hero: Annie Spratt, Unsplash, https://unsplash.com/photos/gdi9fJboJQU. Kredit i sidfoten.
- Exempelsajternas egna bilder tillhör respektive exempelsajt och visas bara genom ramarna.
- `demo-*.webp` kopierades in i `assets/` enligt uppdraget men används inte: ramarna är live.

## Kända brister

- Den pinnade scenen syns som ett tomt band i statiska helsidesbilder (7000 px). I webbläsaren
  är det Hōrai som scrollas. Vill man korta resan sänks taket i `sizeScene()`.
- Kortet täcker ett litet hörn av Hōrai under pinningen (`pointer-events: none`, så klick går
  igenom, men innehållet därunder skyms).
- Inuti ramen på 390 px visar exempelsajterna sitt eget mobilläge vid 358 px bredd: Calyx
  navigering kolliderar och Hōrais ingress går utanför ramens kant. Det är sajternas egna
  brytpunkter, inte den här sidans överflöde.
- `<details name>` för exklusivt dragspel kräver Chromium 120+/Safari 17.2+/Firefox 130+.
  I äldre webbläsare kan flera spjäll stå öppna samtidigt; ramen följer det senast öppnade.
- Kopiepassen `copywriting`, `copy-editing` och `humanizer-svenska` kördes inte som skills;
  de få egna raderna lästes för hand mot deras regler (inga tankstreck, inga tal, inga
  påståenden om kunder).
- Fingerprintraden lades inte till i valvets register eftersom uppdraget bara tillåter skrivning
  under den här mappen.
