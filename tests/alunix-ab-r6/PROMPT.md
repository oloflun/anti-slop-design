# Uppdrag: en komplett landningssida för Alunix, koncept {{KONCEPT}}

Du bygger en färdig, scrollkoreograferad landningssida i ren HTML/CSS/JS för Alunix, en svensk
webbbyrå. Riktningen är låst till målbilden nedan. Bygg inga alternativa riktningar. Skriv bara
under `{{UT_MAPP}}`. Läs inte andra koncept, inte `tests/alunix-concepts*`, inte andra
byggmappar. Ingen commit.

## Vad du levererar (i `{{UT_MAPP}}`)

- `index.html` med all CSS och JS inuti eller i filer bredvid, utan externa beroenden utom
  typsnitt från Google Fonts (eller systemtypsnitt).
- `assets/` med alla bilder vendrade lokalt som WebP, längsta sida högst 2200 px. Hotlinka inte.
- `shots/` med dina egna skärmbilder (se Verifiering).
- `NOTES.md`: vilka beslut du tog och varför, akt för akt vad som rör sig och hur det hänger i
  motivet, fotokrediter, vilka skärmbilder du tittade på och vad du ändrade efter varje, kända
  brister.

## Alunix, fakta (inget annat får hittas på)

Alunix är en webbyrå i Sverige. Sidan säljer en tjänst: webbdesign. Byrån visar vad den kan
genom tre riktiga exempelsajter som ligger i samma repo och serveras live:

- `/sites/calyx.html`: florist i Stockholm. Rad att använda: `Exempelsida: Calyx, florist i Stockholm`
- `/sites/horai.html`: restaurang, Asian fusion. Rad: `Exempelsida: Hōrai, Asian fusion-koncept`
- `/sites/hyperborea.html`: konferens i Lund. Rad: `Exempelsida: Hyperborea, konferens i Lund`

Skärmbilder av dem: `tests/alunix-concepts-r3/build/assets/demo-{calyx,horai,hyperborea}.webp`
(kopiera in i `assets/`). Sajterna får visas live i `<iframe>` (samma origin när sidan serveras
från repo-roten, se Server nedan). Ramar ska vara användbara när de är öppna: transformera eller
tona aldrig själva ramelementet efter att det visats.

Logotyp: `tests/alunix-concepts-r3/build/assets/logo-white.svg` och `logo-black.svg` (kopiera in,
får läggas inline). Fotopool som får användas: `tests/alunix-concepts/_assets/*.webp`.

Dagens Alunix-register, som jämförelse och inte som lås: kall nästan-svart `#17181B`, blå
`#1E5E9C` bara för handling, Geist för rubrik, Inter för brödtext, JetBrains Mono för data.
Konceptet får avvika helt.

Röst: byråröst i vi-form, korta satser, fakta före adjektiv. Svenska. Ingen engelska behövs.

### Copy som ska användas ordagrant

- Rubrik: `Er hemsida är nutidens visitkort`
- Underrad: `Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten.`
- Tesrubrik: `VI BYGGER ERT VARUMÄRKE.`
- Rad: `Webbdesign, design och system. Allt på ett ställe.`
- Tjänster, numrerade 01–03: `Design`, `Utveckling`, `System` (skriv en kort underrad var, i
  byråröst, utan påståenden om kunder eller resultat)
- Paket, som egna rader:
  - `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.` → `26 900 kr`
  - `Paket med bokningssystem, betalning och kunddatabas.` → `38 900 kr`
  - `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera` → `Pris vid förfrågan`
- Prisrubrik: `Alla har rätt till bra design.`
- Kontakt: `kontakt@alunix.se` (som text och mailto; inget formulär som skickar någonstans)

### Förbjudet, bindande

- Inga påhittade tal, kunder, omdömen, citat, logotypväggar, stjärnor, "nöjda kunder".
  De tre exempelsajterna är de enda kunderna som får synas. Aldrig namnet Klova.
- Inga tankstreck (varken – eller —) i synlig text.
- Inget "jag". Inga foton som läses som "vårt kontor" eller "vårt team".
- Inga hexfärger eller typsnitt hämtade från någon annan färdig mall; allt härleds ur målbilden.

## Målbild för {{KONCEPT}}

Läs `tests/alunix-ab-r6/concepts.md`, avsnittet för {{KONCEPT}}, som den fullständiga målbilden.
Det är ditt brief. Tillåtet referensmaterial utöver det: de två katalogposter avsnittet namnger,
under `design-catalogue/entries/<slug>/` (`entry.md`, `fold.webp`, `shot.webp`, `slices/`). Titta
på bilderna. Låna principen, aldrig pixeln: inga av deras färgkoder eller typsnitt kopieras rakt av.
Läs inget annat under `design-catalogue/`.

## Scroll, krav

- Hela sidan är koreograferad, inte bara första skärmen. Minst fyra olika slags rörelser
  (till exempel: skalning kopplad till scroll, pinnad scen, avslöjande med klippmask,
  förskjutning i olika hastighet, radvis intoning, ett moment som styrs procentuellt av scroll).
  Aldrig samma slag två gånger i rad.
- En signaturrörelse som bara finns på den här sidan, beskriven i målbilden, och som hänger i
  sidans motiv. Den ska vara mjukt interpolerad och fungera i båda scrollriktningarna.
- Inget dött scrollavstånd (skärmhöjder där inget händer och inget nytt syns).
- `prefers-reduced-motion: reduce` tar bort resorna (skalning, förflyttning, parallax) men
  behåller allt innehåll synligt och i rätt ordning. Innehåll som börjar dolt måste ha en
  reserv som visar det om JavaScript inte kör eller om observatören aldrig fyrar.
- Inget horisontellt överflöde vid 320, 390, 768 och 1440 px bredd. Fungerar på mobil.

## Foton

`UNSPLASH_ACCESS_KEY` finns i din miljö (läs den från `os.environ`, skriv aldrig ut den).
API: `https://api.unsplash.com/search/photos?query=...&per_page=30&orientation=landscape` med
header `Authorization: Client-ID <nyckel>`. Innan du laddar ned en bild i full storlek: anropa
`GET /photos/<id>/download` (API-villkor). Hämta sedan `urls.raw` med `&w=2200&fm=webp&q=82`.
**Högst 12 API-anrop totalt.** Titta på kandidaterna (rendera ett kontaktark eller läs
miniatyrerna) innan du väljer; välj bilden efter hur mycket text den ska bära. Kreditera
fotografen med namn och länk i sidfoten och i `NOTES.md`.

## Server och verifiering

Playwright för Python och Chromium finns installerade. Starta en server från repo-roten på
din port: `python -m http.server {{PORT}}` (i bakgrunden), och öppna
`http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html`. Ramarna till `/sites/...` fungerar bara
när sidan serveras så.

Skjut och **titta på** minst: 1440×900 första skärm; hela sidan i 1440 efter en genomscroll
i 300 px-steg; 390×844 hela sidan; tre bilder mitt i signaturrörelsen; en bild med reduced
motion aktiverat. Läs konsolen efter fel. Mät horisontellt överflöde per element, inte bara
`scrollWidth`. Rätta det du ser, skjut om, och skriv i `NOTES.md` vilka bilder du läste.
En skärmbild du inte tittat på räknas inte.

Klart betyder: sidan laddar utan konsolfel, alla ramar visar sin sajt (dokumentet i ramen har en
`<title>`), inget överflöde, reduced motion visar allt, och `NOTES.md` är skriven.
