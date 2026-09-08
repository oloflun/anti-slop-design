# K1 Skymning, byggnoter

Bygge B/K1, 2026-09-06. Sidan: `index.html` (all CSS och JS inline), `assets/`, `shots/`.
Öppnas via `http://127.0.0.1:3101/tests/alunix-ab-r6/runs/B/K1/index.html` från repo-roten,
annars visar ramen mot `/sites/horai.html` ingenting.

## Beslut

**Fotot bär.** Ett foto av Stockholm i blå timmen (Riddarholmen sett från Söder, tända fönster
längs kajen, vatten i förgrunden) fyller första skärmen. Himlen är ett mörkt, jämnt band i övre
40 procent, där rubriken står. Husraden med tända fönster ligger i nedre halvan och ger
signaturrörelsen ett mål.

**Register härlett ur fotot, inte ur mallen.** Mörk grund `#0b1220` är vattnet i fotot,
en aning mörkare. Vit text `#f4f2ec` är fönsterljuset avmättat. Den enda kromatiska färgen är
bärnsten `#e6b567`, samplad från fönstren, och den gör en sak: understrykningen under
`visitkort` (och samma linje under kontaktadressen i landningen, som är samma tecken igen).
Dagens Alunix-blå används inte; den skulle konkurrera med himlen.

**Typ.** Cormorant Garamond 300 för rubriker, ordmärket och priserna: ljus i vikt, stor, luftig.
Schibsted Grotesk 400/500 för brödtext och tesrubriken (skandinavisk tidningsgrotesk, valdes i
stället för Instrument Sans som projektets krok flaggade som överanvänd). Tesrubriken
`VI BYGGER ERT VARUMÄRKE.` är den enda tunga raden på sidan och sätts därför i grotesken.

**Lån från katalogen, princip och inte pixel.**
- `rogo`: ett skymningsfoto bär rubriken, bevis i samma bildruta, sedan ett hårt byte till vit
  grund där varje påstående står bredvid en riktig skärmbild, sidan växlar vänster/höger.
  Inga av rogos färgkoder eller typsnitt. Rogos logotypvägg ersätts av tre textnamn.
- `groupemontoni`: ordmärket i serif direkt i bilden utan platta, mjuk mörkning bara i kanten
  där text står. Inga räknare, ingen mosaik.

**Bevisraden.** `Calyx · Hōrai · Hyperborea` som textnamn längst ned i första skärmen med en
liten etikett `Tre exempelsidor, byggda av oss` så att raden inte läses som "trusted by".
Namnen länkar till sajterna.

**Ramen är användbar men fångar inte scrollen.** Hōrai ligger live i en `<iframe>` som fyller
skärmen efter zoomen. Ramen har `pointer-events: none` tills besökaren klickar `Prova sidan`
i radens nederkant (blir `Klar` när den är på). Utan det spärret hade hjulet fastnat inne i
Hōrais egen scrollkoreografi. Ramen transformeras eller tonas aldrig; den är ett vanligt
element i flödet som pinnas med `position: sticky` under en skärmhöjd.

**Ingen knapp i heron.** Kontaktadressen är en typsatt länk i toppbaren och i landningen.
Inget formulär, bara `mailto:`.

## Akterna, vad som rör sig och hur det hänger i motivet

1. **Stillhet.** Fotot, ordmärket ALUNIX i spärrad serif, rubriken, underraden, bevisraden.
   Enda rörelsen är en svag drift i fotot (CSS-keyframe, skala 1 till 1,035 över 26 s, fram och
   tillbaka). Fönstret som kameran ska in i syns redan här som ett litet varmt fönster i
   fasaden: det är Hōrais skärmbild i 60×37 px med en bärnstenston lagd över.
2. **Drag (signaturrörelsen, scrollstyrd i procent).** Scrollen driver en kontinuerlig
   inzoomning mot fönstret. Fotot skalas exponentiellt från 1 till 24 gånger runt fönstrets
   punkt (49 % x, 59 % y i bilden), samtidigt som punkten glider till skärmens mitt. Fönstret
   ritas i skärmrymd utan transform så att skärmbilden är skarp när den fyller skärmen.
   Rubriken lämnar bilden genom att tona och blurra (opacity och `filter: blur`, ingen
   förskjutning). Bevisraden stannar kvar längst ned tills fönstret nästan tar över. Allt är
   `smoothstep`-interpolerat mot scrollpositionen och fungerar i båda riktningarna.
3. **Avslöjande (pinnad scen).** När fönstret fyller skärmen är spåret slut, den fasta heron
   döljs och exakt under den ligger den levande ramen med Hōrai, pinnad en skärmhöjd. Bytet
   från skärmbild till levande sida sker på samma pixel. Toppbaren viker undan här, eftersom
   Hōrai har en egen toppbar.
4. **Klarhet (glid in från sidan, en gång).** Hårt klipp till vit grund.
   `VI BYGGER ERT VARUMÄRKE.` stort. Tre rader: Design bredvid Calyx, Utveckling bredvid
   Hōrai, System bredvid Hyperborea, bildsidan växlar. Skärmbilden glider in från sin sida
   och texten från motsatt håll när raden passerar 22 % av skärmen (IntersectionObserver,
   en gång).
5. **Räkning (radvis intoning).** `Alla har rätt till bra design.` i serif, tre rader med
   hårlinjer, pris till höger i stor serifgrad. Raderna tonar in med 140 ms förskjutning
   per rad. Inga kort.
6. **Landning (förskjutning i olika hastighet).** Mörk grund, ett andra foto av samma stad
   nu i natt (Mariaberget, tända fönster, mörk husmassa). Fotot rör sig långsammare än
   texten tills sektionen fyller skärmen, sedan står allt stilla. `kontakt@alunix.se` i stor
   serifgrad med bärnstenslinjen under. Sista skärmen hålls stilla; inget tonar bort.

Sekvens av rörelseslag: scrollstyrd zoom → pinnad scen → glid från sidan → radvis intoning →
parallax. Inget slag två gånger i rad. Ingen skärmhöjd utan att något nytt syns: heron har
3,8 skärmhöjder scroll och zoomen pågår genom 0,04 till 0,90 av dem, resten är fönstret
fullt innan klippet.

**Reduced motion.** Heron blir ett vanligt block på en skärmhöjd utan zoom och utan drift,
fönstret döljs, rubriken står kvar, ramen ligger i flödet utan pinning, raderna och priserna
visas utan förskjutning, landningen utan parallax. **Utan JavaScript** gäller samma sak:
alla `.js`-beroende regler faller bort, innehåll som annars börjar dolt är synligt.
Observatören har dessutom en reserv som efter 2,5 s visar allt som redan ligger i skärmen.

## Foton

Fyra Unsplash-anrop av tolv tillåtna: två sökningar (`stockholm skyline blue hour`,
`stockholm night waterfront lights`) och två registreringar via `/photos/<id>/download`
före nedladdning av `urls.raw` med `w=2200&fm=webp&q=82`. Alla 60 kandidater renderades
till två kontaktark; sex kandidater hämtades i 1000 px och bedömdes mot kravet: mörkt
band för rubriken, upplyst fönsterparti att zooma mot, vatten i förgrunden, aldrig dag.

- `assets/dusk.webp`, 2200×1467: Julian Terenzio, https://unsplash.com/@julianterenzio,
  https://unsplash.com/photos/5UDPVmIdXUo
- `assets/night.webp`, 2200×1467: Adnan Tokgöz, https://unsplash.com/@adnantokgoz,
  https://unsplash.com/photos/POH0WhC1j3U

Krediterade i sidfoten med namn och länk. Skärmbilderna `demo-*.webp` och loggorna
kopierade från `tests/alunix-concepts-r3/build/assets/`.

## Skärmbilder jag läste och vad jag ändrade

Alla bilder ligger i `shots/`. Skriptet `shots/shoot.py` tar dem (Playwright, Chromium).

**Omgång 1** (1440 fold, zoom p25/50/72/90/100, tre ramlägen, hel sida, 390 hel, reduced).
- Heron var tom: `dusk.webp` fick `ERR_CONNECTION_RESET`. Se Kända brister; löst för
  verifieringen genom att låta Playwright fylla `assets/*` från disk, sidan oförändrad.
- Fönstret låg mitt i ordet `visitkort` vid start och lästes som en tumnagel, inte ett
  fönster. Ändrade: rubriken på två rader och högre upp, startskala 24 i stället för 16
  (fönstret 60×37 px), bärnstenston över fönstret som tonar bort under zoomen.
- Klippet var inte hårt: efter zoomen fanns en tom mörk skärmhöjd innan ramen gled in.
  Ändrade: ramsektionen börjar exakt där spåret slutar (`margin-top: -100vh`), heron döljs
  på samma scrollposition.
- Toppbarens `kontakt@alunix.se` låg över Hōrais `Reservations`. Ändrade: toppbaren viker
  undan medan ramen fyller skärmen.

**Omgång 2** (samma uppsättning).
- Underraden låg på husfasadernas ljusa del. Ändrade: textblocket 8 vh från toppen,
  mörkningen i övre kanten sträcker sig till 56 % med en mellanstopp.
- Toppbaren kom tillbaka en skärmhöjd för tidigt (villkoret slutade vid pinningens slut,
  inte vid det vita). Ändrade villkoret till "tills det vita ligger under toppbaren".
- Raderna i akt 4 hade smal bildkolumn. Ändrade till 5/7 med bilden i den breda.

**Omgång 3.**
- Vid p=90 var skärmbilden i fönstret suddig: Chromium rastrerar det skalade lagret i
  startupplösning. Ändrade: fönstret ligger utanför det skalade omslaget och får läge och
  storlek i skärmrymd från JS, utan transform. Skarp genom hela zoomen och pixelexakt mot
  den levande ramen vid klippet.
- Toppbarens undanvikning gäller nu även vid reduced motion (det är inte rörelse).

**Slutkörning** (`final-*`): 1440 fold, zoom p25/50/72/90/100, ramen vid tre lägen, hel
sida 1440 efter genomscroll i 300 px-steg, 390 fold och hel sida, 320 hel sida, reduced
motion fold och hel sida. Tittade på: fold, p50, p72, p90, frame1, m390 fold, reduced fold
och de tre helsidorna.

Mätningar i slutkörningen:
- Konsol: inga fel från sidan. En varning från ramen: Hōrai-sidan laddar
  `cdn.tailwindcss.com`, det är dess egen sak.
- Horisontellt överflöde per element (element inuti klippande föräldrar undantagna):
  inget vid 320, 390, 768, 1440.
- Ramen: dokumentet har `<title>` (Hōrai-sidans egen titel, som innehåller ett tankstreck; det är dess text, inte min).
- Typsnitt laddade: Cormorant Garamond 300/400, Schibsted Grotesk 400/500.
- Inga tankstreck, inget "jag", inget Klova i synlig text.

## Kända brister

- **Loopback på den här maskinen bryter ibland anslutningen för filer över ungefär
  128 kB**, oavsett server (python `http.server`, HTTP/1.1, Node). Curl och Hōrai-sidan
  själv går fint; sidorna i `sites/` laddar sina bilder från Unsplash. Sidan har en
  omladdning per bild vid fel som skyddsnät, och verifieringen fyller `assets/` från disk.
  I en riktig miljö är det inget problem, men om sidan öppnas lokalt utan skriptet kan
  heron i undantagsfall behöva en omladdning.
- Fotot är 24 gånger uppskalat i zoomens sista tredjedel och därför mjukt runt fönstret.
  Fönstret täcker då nästan hela skärmen, så det syns bara i kanterna, men det syns.
- Helsidesskärmbilderna visar tomma mörka fält där den fasta heron och den pinnade ramen
  ligger; det är så helsidesbilder ser ut med `position: fixed` och `sticky`, inte döda
  skärmhöjder i verkligheten.
- Skärmbilden i fönstret är desktopversionen av Hōrai. På mobil (stående) visar den levande
  ramen mobilversionen, så det finns ett litet språng i layout vid klippet, även om motivet
  (samma foto, samma ordmärke) är detsamma.
- `Prova sidan` är en `<button>` som ser ut som en typsatt länk. Det är det enda
  knappelementet på sidan och det finns för att ramen ska vara användbar utan att fånga
  scrollen.
