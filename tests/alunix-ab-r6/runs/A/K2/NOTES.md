# K2 Affischen. Anteckningar

Sidan: `index.html` (all CSS och JS inuti). Bilder i `assets/`, skärmbilder i `shots/`.
Server: `python -m http.server 3102` från repo-roten, sidan på
`http://127.0.0.1:3102/tests/alunix-ab-r6/runs/A/K2/index.html`.

## Beslut

**Register.** En tryckt affisch på salviapapper. Fem färger, inga fler:

| Roll | Värde |
|---|---|
| papper | `#CBD3C9` |
| bläck | `#1B1F1C` |
| vitt (bara plåtarnas grund) | `#F5F6F2` |
| hårlinje stark | `#A7B0A5` |
| hårlinje svag | `#BFC7BC` |

Ingen accentfärg. Länkar är bläck med understrykning vid hover. Avslutet inverterar: papper på bläck.
Hörnradie 2 px på plåtarna, annars 0. Inga skuggor, inga gradienter. Färgerna är härledda ur
målbilden (salvia, bläck, vitt, två gråa), inte tagna från någon katalogpost; springsummer har
celadon `#e5ebda` och plommon `#44394c`, vi ligger kallare och gråare.

**Typ.** Två typsnitt från Google Fonts.
- Archivo 900 (normal bredd) bara i affischskala: ordmärket, `VI BYGGER / ERT VARUMÄRKE.`,
  siffrorna 01 till 03 och `Alla har rätt till bra design.`. Affischskalan är ett enda token,
  `clamp(38px, 9.5vw, 170px)`, valt så att `ERT VARUMÄRKE.` fyller exakt en rad vid 1440
  (mätt: 9,64 em med spärrning −0,02 em). På telefon 12 vw, och där bryts `ERT / VARUMÄRKE.`
  på två rader.
- Familjen Grotesk 400/500/600 för allt annat: beskrivningsraden (22 px), löptext (17 px),
  små versaler med spärrning 0,14 em (12 px). Ingen rubrikstorlek däremellan.
- Ordmärket i heron är samma affischtoken förstorat med scroll-skalan (3,1× vid 1440×900,
  alltså 420 px). Så finns bara en poster-storlek i typsystemet; heron är den uppskalad.

**Layout.** Sidmarginal `clamp(20px, 2.4vw, 34px)`, tolv kolumner i uppslagen och liggaren.
Allt vänsterställt. Toppbaren är en tunn rad: liten SVG-logga och ordmärke i små versaler
vänster, riktig klocka (`Intl.DateTimeFormat`, `Europe/Stockholm`, tickar varje sekund) och
`Stockholm` som text, `kontakt@alunix.se` höger. Utan JS visas bara `Stockholm`, aldrig en
klocka som står stilla.

**Kopian.** All obligatorisk copy ordagrann. `Er hemsida är nutidens visitkort` och underraden
står på första skärmen som affischens lilla textblock nere till höger. Tjänsternas underrader,
i byråröst utan kundpåståenden: "Identitet, typografi och layout. Vi ritar sidan innan vi bygger
den." / "Handskriven kod utan tunga teman. Vi bygger det vi ritat." / "CMS, bokning, betalning
och kunddatabas. Vi kopplar ihop det ni behöver." Inga tankstreck i synlig text (kontrollerat
med sökning; "SEO-optimering" och "fusion-koncept" är bindestreck).

## Signaturrörelsen: fönstren i bokstäverna, papperet skjuts, blocket andas

Ordmärket är `ALU` / `NIX` på två rader, radhöjd 0,73 em så bokstäverna nästan rör varandra.
Varje rad är en inline-SVG med texten i bläck ovanpå en maskad bildgrupp. Masken är
bokstävernas *öppningar*: A:s räknare och öppningen under tvärstrecket, U:s kanal, X:s fyra
kilar. Öppningarna mäts i bläcket, inte gissas: bokstaven ritas på en canvas i 200 px,
och för varje pixelrad tas gapet mellan yttersta bläckstråken (för X även per kolumn).
Polygonerna dras 1,5 enheter in i bläcket så att inga springor uppstår, och klipps mot
bläckets yttermått så att öppna sidor (A:s fot, U:s topp) aldrig visar papper. Räknas om när
typsnittet laddat.

Bakom masken ligger de tre exempelsajternas skärmbilder staplade lodrätt, zoomade 1,6× så att
fönstren visar något man känner igen (Calyx blommor, Hōrais tallrik, Hyperboreas orange).
Rad två har samma stapel förskjuten en radhöjd, så bilden är kontinuerlig genom hela blocket.

Heron är en pinnad scen, 320 vh lång. Scrollen mappas till p i [0, 1], mjukt interpolerad
(0,16 per bildruta mot målet) och fungerar i båda riktningarna:
- 0 till 0,06: stillhet. Bara klockan går.
- 0,06 till 0,58: **bytet**. Bildstapeln glider uppåt bakom den stilla masken med två
  övergångar och vila emellan (Calyx håller, byter till Hōrai, håller, byter till Hyperborea,
  håller). Raden `Exempelsida: …` under ordmärket byts vid varje övergångs mitt.
- 0,58 till 1: **andningen**. Blocket skalas från 3,1× till 1× (transform-origin uppe till
  vänster), radhöjden går från krossad till normal, raderna glider isär till 0,04 em, och
  raderna byter innehåll: ordmärket glider en bit uppåt och tonar bort, `VI BYGGER` /
  `ERT VARUMÄRKE.` kommer underifrån i sin slutstorlek och tonar in. Klippet per rad är en
  `clip-path` som i slutet öppnar sig 0,45 em uppåt så att Ä:s prickar inte skärs av.
  Samtidigt tonar affischens lilla textblock och sajtraden ut, och ledraden `Tre exempelsidor`
  tonar in på sajtradens plats. Blocket glider ned till lodrät mitt i den kvarvarande ytan.
  Vid p = 1 lossnar scenen exakt, och rubriken följer med i flödet som nästa akts rubrik.

## Akt för akt: vad som rör sig och hur det hänger i motivet

1. **Tyngd.** Affischen, klockan tickar, Calyx syns i A, U och X. Inget annat rör sig.
2. **Byte.** Bilden bakom masken glider (procentuellt styrt av scroll, pinnad scen). Som ett
   ark som skjuts under en stans.
3. **Andning.** Skalning kopplad till scroll och radbyte (samma pinnade scen; brief:et
   kopplar de två till samma scroll). Det krossade blocket öppnar sig till rubriken.
4. **Bevis.** Tre uppslag under varandra, växelvis 1–10 och 3–13 i kolumnraster. Varje
   uppslag glider in en gång från sin sida (plåten och bildtexten, 48 px, olika fördröjning).
   Skärmbilden är svartvit och går till färg i en enda övergång kopplad till scrollen när
   plåten passerar mitten (`grayscale(1−q)`, q över ett band på 24 vh runt 62 % av höjden).
   När q når 1 låses den: skärmbilden tonar bort och den levande ramen under den blir synlig
   och användbar. Ramen själv transformeras eller tonas aldrig; bara bilden ovanpå. Pil som
   länk (`Öppna i nytt fönster →`) öppnar sajten i ny flik.
5. **Lista.** Tjänsterna 01–03 som liggare med hårlinjer, siffran i affischtoken. Raderna dras
   fram radvis med en klippmask vänster till höger (120 ms förskjutning per rad). Det
   dokumentära fotot (svartvitt, litet, till höger om rubriken) går i annan hastighet än
   texten (translateY ±48 px över en skärmhöjd). Ingen parallax på text.
6. **Pris.** Tre rader i samma liggare, pris höger. Radvis intoning: raden tonar in och priset
   glider in 28 px från höger (140 ms per rad). Annan rörelse än akt 5:s klippmask.
7. **Avslut.** Bläckarket trycks över papperet: `clip-path: inset(0 R 0 0)` där R går från
   100 % till 0 kopplat till scrollen när arket kommer in, som en vals som drar bläck över
   arket. Inne i arket: `Alla har rätt till bra design.` i affischskala, sedan kontaktadressen
   som vanlig länk i lässtorlek, sedan sidfoten i 11 px. Sidan slutar på minsta typen.

Rörelseslag i följd: pinnad procentstyrd bildglidning → skalning och radbyte → engångsglidning
och scrollkopplad färg → klippmask radvis och foto i annan hastighet → radvis intoning →
scrollkopplad klippmask. Aldrig samma slag två gånger i rad.

**Reduced motion.** `.rm` sätts från `matchMedia`. Heron släpper pinningen, ordmärket står i
sin hero-storlek med Calyx i fönstren, `VI BYGGER / ERT VARUMÄRKE.` ligger som en vanlig
rubrik i flödet först i Bevis-akten, uppslagen visar ramarna direkt (skärmbilden döljs),
liggarens rader står framme, fotot står stilla, bläckarket är oklippt. Alla transitions av.

**Utan JS.** `html.js` saknas: allt dolt är synligt. Raderna ligger i flödet, rubriken visas
statiskt, skärmbilderna ligger i färg ovanpå ramarna, liggare och priser är synliga,
avslutet oklippt. Fönstren i bokstäverna kräver JS (masken byggs ur den renderade glyfen),
så utan JS är ordmärket helt i bläck.

## Foto

- `assets/desk-daylight.webp`: Annie Spratt, Unsplash,
  <https://unsplash.com/photos/Rjp8UxEIJ38>, fotograf <https://unsplash.com/@anniespratt>.
  Hämtad med `w=2200`, konverterad till svartvitt lokalt (2200×1649). Krediterad i sidfoten.
  Vald ur ett kontaktark med 30 kandidater på sökningen "designer desk daylight documentary":
  dagsljus genom persienner, ett litet träbord, lampa, modellskepp. Inga skärmar, ingen
  människa, läses som ett rum och inte som "vårt kontor".
- API-anrop: 2 av 12 (en sökning, ett `download`-anrop). Bildfilen hämtades från
  `images.unsplash.com`.
- `assets/demo-{calyx,horai,hyperborea}.webp` och `logo-black.svg`, `logo-white.svg` kopierade
  från `tests/alunix-concepts-r3/build/assets/`.

## Referenser, lånat som princip

- springsummer: fem färger utan accent, krossad radhöjd i affischskala, klockan och staden
  som typsatt text, arrow-glyfer som enda styrning, ingen mellanstorlek på rubriker.
- indoek: fotot står inne i ordmärkets bokstäver. Vi gör det i öppningarna i stället för i
  en rektangel bakom ordet, och bilden byts genom att glida bakom masken.
Inga färgkoder eller typsnitt kopierade.

## Skärmbilder jag tittade på, och vad jag ändrade efter varje

1. `desktop-fold.png` (första bygget). Fönstren låg fel: hullen räknades ur canvas-måtten och
   hamnade utanför glyfen (band ovanför U, springor vid X). Två prickar syntes till höger om
   NIX: Ä:s prickar i den dolda rubrikraden stack upp ovanför radklippet. Sajtraden låg långt
   från blocket. → Byggde om masken ur pixelskanning av bläcket, lade en extra förskjutning på
   den inkommande raden, flyttade sajtraden till direkt under blocket.
2. `desktop-full.png` (första). Skrivbordsfotot var uttänjt till ett stående band: `height`-
   attributet gällde när CSS bara satte bredd. → `img{height:auto}`.
3. `desktop-fold.png` (andra). Blocket försvann: `BASE` odefinierad efter omskrivningen.
   → Rättade konstanten.
4. `desktop-fold.png` (tredje). Polygonernas över- och underkanter var sneda (vänster- och
   högerpunkter hade olika y), A:s fot visade en springa under baslinjen, sajtraden låg
   ovanpå det skalade blocket (layouthöjden var oskalad), affischens textblock hamnade till
   vänster. → Raka kanter med gemensam y, klipp mot bläckets yttermått, blockets layouthöjd
   sätts till den synliga höjden, textblocket i kolumn 2.
5. `sig-20/35/70/85/100.png`. Bytet fungerar, Hōrai och Hyperborea passerar. Ä:s prickar
   klipptes i slutet; slutläget var topptungt med tom nedre halva; ledraden nere till höger.
   → `clip-path` som öppnar uppåt i slutet, blocket glider till lodrät mitt, ledraden tar
   sajtradens plats.
6. `walk-spread1.png`, `walk-tjanster.png`, `walk-paket.png`, `walk-end.png`. Liggarna och
   uppslagen hade tappat sidmarginalen (`padding`-kortformen i sektionsregeln slog ut
   `.wrap`). Prisets startförskjutning 28 px gav horisontellt överflöde. Tjänste-rubriken
   och raden satt i olika rader i rastret. → `padding-top/bottom` i stället för kortform,
   `overflow-x:clip` på prislistan, rubrik och rad i en gemensam cell.
7. `mobile-fold.png`, `mobile-full.png`. Tom mitt i heron på telefon (scenen var 100 vh
   medan blocket är breddbegränsat). → Scenen får auto-höjd under 900 px; bredden ensam styr
   ordmärkets storlek.
8. `reduced-fold.png`. Ordmärket var litet (SVG-bredden sattes i affischtoken utan skalning).
   → I reduced motion sätts SVG:n direkt i hero-storlek.
9. `sig-75.png`. Mitt i andningen kolliderade fragment av ALU, VI BYGGER och NIX i samma yta:
   rullningen på full radhöjd blev rörig med två rader. → Kortare glidning (0,4 radhöjd) med
   korstoning: ordmärket tonar bort, rubriken tonar in. `sig-70/80/90.png` och
   `mobile-sig-35/90.png` bekräftar att övergången är ren.
10. `nojs-fold.png`, `nojs-full.png`. Allt innehåll synligt i rätt ordning, klockan visar bara
    `Stockholm`. Inga ändringar.
11. `desktop-full-after-scroll.png`, `walk-spread2.png`, `walk-kontakt.png`. Uppslagen låser
    till levande ramar i färg efter passagen, bläckarket är fullt tryckt vid sidans slut.

Sista körningar: konsolen tom i desktop, mobil och reduced motion (se nedan om
utvecklingsservern), `scrollWidth` lika med viewporten och inget element utanför vid 320, 390,
768 och 1440 (mätt per element med `getBoundingClientRect`, klippande förfäder inräknade, i
400 px-steg genom hela sidan), alla tre ramar rapporterar sin `<title>`.

## Kända brister

- **Utvecklingsservern släpper ibland anslutningar.** `python -m http.server` på Windows ger
  då och då `ERR_CONNECTION_RESET` på en av webp-filerna vid sidladdning, oavsett hur få
  anrop som går samtidigt (testat: staplade bildladdningar, lata skärmbilder). Sidan har en
  omhämtning på `img` och SVG-`image` (upp till tre försök) som i praktiken alltid räddar
  bilden, men webbläsaren loggar det första felet i konsolen. På en vanlig server händer det
  inte. Det syns i vissa körningar som ett `Failed to load resource`, aldrig som ett JS-fel.
- Fönstren i bokstäverna finns bara med JS. Utan JS står ordmärket helt i bläck.
- Ramarna fångar hjulscroll när pekaren står över dem. Det är avsett (ramarna ska vara
  användbara) men kan överraska när man scrollar förbi ett öppet uppslag.
- På telefon bryts `ERT VARUMÄRKE.` på två rader, så rad två i andningen växer till dubbel
  höjd medan rad ett förblir en. Det ser avsiktligt ut men är en följd av bredden.
- Hel-sida-skärmbilder av sidan visar heron som tom yta (pinnad scen fotograferad ur sitt
  läge); det är ett artefakt av fullsidesfotografering, inte av sidan.
- De första 6 % av heron (13 vh) är avsiktlig stillhet, bara klockan går.
