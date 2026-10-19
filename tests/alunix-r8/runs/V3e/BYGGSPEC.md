# V3e · Katalogen · provarket — byggspec

Detta är en **ny visuell tappning av V3d**. Samma budskap, samma showcase, samma
copy ordagrant. Det som byts är registret, layouten och rörelsen.

Källan för copyn är `runs/V3d/index.html`. Copyn nedan är extraherad ordagrant
därifrån och får **inte** ändras, kortas eller skrivas om. Enda undantaget är
listan "BORT" längst ned.

---

## 1. Vad sidan säljer (läs detta först)

Alunix är en webbyrå. Budskapet: **första intrycket är digitalt, därför är design
hela jobbet.** Beviset är inte siffror eller kundcitat — det är tre *riktiga,
levande* exempelsajter som visas inbäddade i sidan, beskrivna punkt för punkt med
vad som gjordes och varför.

Det är sidans egentliga formproblem: **hur visar man tre främmande sajter inuti en
sida utan att ramen konkurrerar ut dem?** V3d löste det med mörk botten och
helskärmsifyllda inbäddningar, en i taget.

V3e löser det motsatt: **provarket**. En numrerad, linjerad katalog på papper, där
varje verk står som sig självt med sin egen identitet i behåll, etiketterat och
katalogiserat. Studions egen röst är typografisk och tyst. Färgen kommer från
verken, inte från ramen.

Om en detalj är oklar: välj det som gör att **arket** känns som ett tryckt
provark och **verken** känns levande. Aldrig tvärtom.

---

## 2. Register

| Roll | Värde |
|---|---|
| Papper (grund) | `oklch(0.968 0.003 260)` — svalt, nästan vitt. **Inte** cream/ivory. |
| Bläck | `oklch(0.17 0.012 265)` |
| Dämpat bläck | `oklch(0.46 0.010 265)` |
| Linje | `color-mix(in oklab, var(--ink) 22%, var(--paper))` |
| **Accent** (en, mättad) | `oklch(0.45 0.13 158)` — djup tryckfärgsgrön, som Pantone 350 |
| Accent på mörkt | `oklch(0.72 0.14 158)` |
| Mörk platta (för inversionen) | `oklch(0.19 0.012 265)` |

Accenten används **bara** till: katalognumren (01, 02, 03 …), den regel som
markerar aktuellt prov, och **ett** ord i display-skala på hela sidan
("visitkort" i h1). Ingen accent som fyllning på knappar, kort eller ytor.

**Förbjudet register** (husets egna spärrar, håll dig borta):
cream/ivory + överdimensionerad serif + kursivt ordbyte + terracotta i kombination ·
lila/indigo-accent · gradient-mesh · glasmorfism · tre lika feature-kort ·
centrerad hero med badge-rad · 8 px-radius på allt · dekorativ blob ·
hårlinjegrid som ren dekoration · em-dash i synlig text (noll tolerans) ·
beskrivande mikrotexter som berättar vad sektionen ska göra.

**En radius-skala för hela sidan: 0.** Allt är skarpt. Inga rundade hörn någonstans.

---

## 3. Typografi

Tre redan vendorerade filer i `assets/fonts/`. Inga nya hämtas.

| Fil | Roll i V3e |
|---|---|
| `geist-700-latin.woff2` | **Display.** Monumental. All rubriksättning. |
| `geist-mono-400-latin.woff2` | **Katalogapparaten.** Alla nummer, etiketter, bildtexter, mått, prisrader. |
| `public-sans-300-latin.woff2` | **Brödtext.** All löpande text. |

Skalan ska ha **ett stort språng**: display `clamp(3.2rem, 11vw, 11rem)`, body
`1.0625rem`, mono-etiketter `0.75rem` med `letter-spacing: 0.14em`. Inga
mellanstorlekar som suddar språnget.

Rubriker: `line-height: 0.92`, `letter-spacing: -0.03em`.

---

## 4. Layouten, sektion för sektion

Åtta sektioner i denna ordning. Samma ordning som V3d.

**Ramen:** 12-kolumnsrutnät, `max-width: 1560px`, sidmarginal `clamp(20px, 5vw, 88px)`.
Allt står på rutnätet. Vertikal rytm: `clamp(72px, 9vw, 132px)` mellan sektioner,
satt **en gång** och återanvänd vid varje skarv.

### 4.1 `header.topline`
Tunn regel under. Vänster `ALUNIX` i mono, versaler, spärrad. Höger
`kontakt@alunix.se` i mono. Ingen bakgrund, ingen kant, ingen sticky-effekt.

### 4.2 `#hero` — monumentet
`h1` satt så stort att den **fyller första viewporten och skärs av nederkanten**.
Två rader: "Er hemsida är" / "nutidens visitkort". Ordet **visitkort** i accentfärg.

Under rubriken, i en smal spalt till höger om rutnätets kolumn 7–12: en liten
**provetikett** i mono, linjerad — detta är V3d:s visitkorts baksida, omgjord till
en tryckt etikett. Exakt fyra rader: `Alunix` / `Digital byrå` /
`Design · Utveckling · System` / `Boka ett möte` (länk till `#kontakt`).

Bakom/under: hero-bilden (`assets/demo-calyx-1440-color.webp` som första val,
annars den befintliga ljuspölsbilden från V3d:s assets om den finns) beskuren till
en liggande remsa i rutnätets nedre del. Bilden är ett **prov**, inte en fond — den
ska ha en tunn ram och en mono-bildtext, inte gå helskärm.

Ingen CTA-knapp i hero. Etiketten är ingången.

### 4.3 `#tes` — tesen, som numrerad utsaga
Fyra meningar, satta som en **numrerad lista** i mono + display, rad för rad, med
tunn linje mellan raderna. Varje rad tänds i tur och ordning när den passerar
mitten av viewporten. Ingen mörk platta, ingen bild i denna sektion.

Hyperborea-bilden hör inte här i V3e — den flyttar till prov 03 (se 4.5).

### 4.4 `#process` — registret
`Vår process:` i mono, sedan rubriken i display, sedan den låsta raden i brödtext.

De sju stegen som ett **linjerat register**: en rad per steg, `01`–`07` i mono i
accentfärg till vänster, stegets namn i display i mitten, beskrivningen i brödtext
till höger. Tunn linje mellan varje rad. Ingen SVG-ritning, inget sticky ark — det
är K3:s territorium ("Ritningen") och ska inte upprepas här.

Raden expanderar mjukt när den får fokus (steg-numret går från dämpat till
accent, linjen under raden drar ut från vänster). Det är rörelsens basnivå.

### 4.5 `#case` — provarket (sidans hjärta)
Kapitelstämpel `Exempelcase` i mono över en helbreddsregel.

Två prov. **Prov 01 Calyx**, **Prov 02 Hōrai**, **Prov 03 Hyperborea**.

Varje prov är ett **ark**:
- Överst en **etikettremsa** över hela bredden: `01` i mono accent, namnet i
  display, verksamheten i mono till höger (`Florist, Stockholm` /
  `Restaurang, Asian Fusion` / `Konferens, Lund`). Tunn regel under.
- Därunder, i rutnätet: **vänster kolumn 1–7** den levande inbäddningen i en tunn
  ram; **höger kolumn 8–12** en **bildtextslig ledger** — punkterna som numrerade
  rader, `01`–`05`/`06` i mono, titeln i display liten, texten i brödtext. Tunn
  linje mellan raderna.
- Prov 01 och 03: inbäddning vänster, ledger höger. Prov 02 (Hōrai): **spegelvänt**
  — ledger vänster, inbäddning höger. Spegelvändningen är den enda variationen
  tillåten i katalogen; allt annat hålls lika.

Inbäddningarna finns redan i V3d och pekar på:
- Calyx: `/sites/calyx.html`, `title="Exempelsida: Calyx, florist i Stockholm"`
- Hōrai: `/sites/horai.html`, `title="Exempelsida: Hōrai, Asian fusion-koncept"`
- Hyperborea: `/tests/alunix-concepts-r3/build/` — **kontrollera den faktiska
  sökvägen i `runs/V3d/index.html` och återanvänd den exakt.** Hyperborea visas i
  V3e som ett **prov med bild**, inte som inbäddning, eftersom V3d bara bäddar in
  Calyx och Hōrai. Använd Hyperborea-bilden (`alt`: "Startsidan för Hyperborea, en
  konferens i Lund") och ge prov 03 dess tre rubriker ur copyn nedan.

Inbäddningarna ska ha `loading="lazy"` och `title` ordagrant som ovan.

### 4.6 `#pris` — inversionen
Detta är sidans **enda tonala inversion**: en mörk platta
(`oklch(0.19 0.012 265)`) med ljus text, satt innanför pappersarket så att
arket syns runt om. Motiverad: det är sidans enda känsloutrop i en katalog av
linjerade rader.

Rubriken `Alla har rätt till bra design.` i display på den mörka plattan.
Ingressen under. Sedan de tre raderna som ett **linjerat register** i mono/pris —
tjänsten till vänster, priset till höger, tunn linje mellan. Priset i mono, i
display-storlek relativt raden (priset är radens största tal).

### 4.7 `#kontakt`
Tillbaka på papper. Rubrik + underrad. Formuläret som **linjerade fält** (endast
underlinje, ingen ruta), etiketter i mono. Knappen `Skicka` som **skarp rektangel**
med 1px bläckkant, ingen fyllning, ingen radie.

`.contact-status` med `role="status"` och `aria-live="polite"` ska finnas och vara
tom i markup, precis som i V3d.

Provetiketten från hero (visitkortets framsida) upprepas här som ett litet
linjerat block, `aria-hidden="true"`.

### 4.8 `footer.close`
En helbreddsregel överst. En rad i mono: mejladressen.

---

## 5. Riktlinjer för text (gäller kopian i §6)
- Allt innehåll sätts "på svenska", aldrig kursivt för betoning i display.
- `01`–`07` och `01`–`06` i processtegen och ledger-punkterna är **provets egna
  numrering**, inte dekorativa eyebrows. De bär ordning och får därför finnas.
- Inga versala etiketter ovanpå bilder. Bildtexten står under bilden.

---

## 6. Copyn — källan är filen, inte detta dokument

**Läs `runs/V3d/index.html` och återanvänd varje synlig sträng ordagrant.**
Filen är facit. Kommentarerna i V3d:s HTML pekar på `COPY-V3d-*.md`, men flera av
dem är stale (R24 ändrade två strängar utan att kopysfilen uppdaterades) — lita
därför **bara** på HTML:en.

Extrahera texten mekaniskt (t.ex. med BeautifulSoup på `runs/V3d/index.html`),
behåll ordningen, och sätt in den i V3e:s markup. Ändra inget. Nedan är ankarna
och de strängar som är extra känsliga.

### 6.1 `<head>`
- `<title>`: `Alunix · webbyrå i Sverige`
- meta description: `Alunix är en webbbyrå i Sverige. Vi skapar skräddarsydda webbplatser.`

### 6.2 Rubriker (exakt)
| Sektion | Sträng |
|---|---|
| h1 (hero) | `Er hemsida är nutidens visitkort` |
| tes 1 | `Det första intrycket är digitalt.` |
| tes 2 | `Skärmen möter besökaren före texten.` |
| tes 3 | `Innan ett ord är läst bär layout och bild hela argumentet.` |
| tes 4 | `Vi hjälper er att synas på rätt sätt.` |
| process-kicker | `Vår process:` |
| process-rubrik | `Från samtal till lanserad sida.` |
| process-underrad | `Webbdesign, design och system. Allt på ett ställe.` |
| case-kapitel | `Exempelcase` |
| pris-rubrik | `Alla har rätt till bra design.` |
| kontakt-rubrik | `Berätta om er verksamhet.` |
| kontakt-underrad | `Så berättar vi vad vi kan göra för er.` |

De fyra tesmeningarna sätts i V3e som fyra **egna rader**, en per `<li>`. I V3d
tänds de i sekvens — behåll den sekvensen.

### 6.3 Sidans visitkortsetikett (V3d:s kortbaksida, fyra rader)
`Alunix` · `Digital byrå` · `Design` `Utveckling` `System` · `Boka ett möte`

`Boka ett möte` är en länk till `#kontakt`. Dessutom finns i V3d en
skärmläsarkopia (`.sr-only`), behåll den ordagrant:
`Alunix. Digital byrå. Design, utveckling, system. Boka ett möte: kontakt@alunix.se.`

### 6.4 Processtegen — sju rader, `01`–`07`
Namnen: `Uppstart` · `Planering` · `Design` · `Utveckling` · `Innehåll` · `Lansering` · `Förvaltning`.
Beskrivningarna hämtas ordagrant ur `runs/V3d/index.html`
(`.process-step-title` + respektive stycke). Ändra inget, korta inget.

### 6.5 Proven — ledger-punkterna
**Prov 01 Calyx** — `Calyx`, `Florist, Stockholm`. Fem punkter:
`Fotot bär rubriken` · `En serif för allt man läser` · `Färgen finns redan i bilderna` ·
`Utbudet som prislista` · `Ett mejl räcker`

**Prov 02 Hōrai** — `Hōrai`, `Restaurang, Asian Fusion`. Sex punkter:
`Namnet står en gång` · `Stycket tänds i er takt` · `En mening som saktar in` ·
`Priset står större än namnet` · `Rummet före bokningen` · `Knappen fanns där hela tiden`

**Prov 03 Hyperborea** — `Hyperborea`, `Konferens, Lund`. Tre punkter:
`Fotot bär rubriken` · `En serif för allt man läser` · `Färgen finns redan i bilderna`

> **Kontrollera prov 03 mot filen.** V3d bäddar bara in Calyx och Hōrai; Hyperborea
> förekommer hos V3d som *bild* i tesen. De tre punkterna ovan är Hyperboreas egna
> rader ur `concepts.md`. Om `runs/V3d/index.html` inte innehåller dem: hämta dem
> ordagrant ur `runs/V3d/concepts.md` (sök på `Hyperborea`), och om de inte finns
> där heller, **uteslut prov 03** och säg det i din rapport. Hitta aldrig på text.

### 6.6 Priset — tre rader, ordagrant
1. `Standardpaket. Webbplats med CMS för egna ändringar och en första SEO-optimering.` → `26 900 kr`
2. `Paket med bokningssystem, betalning och kunddatabas.` → `38 900 kr`
3. `Helt skräddarsydda lösningar för produktkataloger, specialbyggda system med mera` → `Pris vid förfrågan`

I rad 1 är ordet `SEO‑optimering` bundet med **U+2011 non-breaking hyphen**
(`SEO&#8209;optimering`), inte ett vanligt bindestreck. Behåll det exakt.

Ingressen över raderna hämtas ordagrant ur filen.

### 6.7 Kontakten
Etiketter: `Namn` · `Verksamhet` · `Vad ni behöver`. Knapp: `Skicka`.
Sektionsrubrik + underrad enligt 6.2.

### 6.8 Footern
`Eller mejla oss direkt på kontakt@alunix.se` — mailto-länk. Strängen ändrades i
R24; den gamla formen (`Eller mejla kontakt@alunix.se`) står kvar i kopysfilen och
är fel. HTML:en gäller.

### 6.9 Bilder och inbäddningar — återanvänd exakt
| Vad | Sökväg | alt / title |
|---|---|---|
| Hero-bild (ljuspölen) | `/tests/alunix-concepts-r3/build/assets/k1-stage-pool.webp` | `En ljuspöl faller diagonalt över ett mörkt scentyg` |
| Hyperborea-bild | `/tests/alunix-concepts-r3/build/assets/demo-hyperborea.webp` | `Startsidan för Hyperborea, en konferens i Lund` |
| Calyx-inbäddning | `/sites/calyx.html` (V3d använder `data-src`) | `Exempelsida: Calyx, florist i Stockholm` |
| Hōrai-inbäddning | `/sites/horai.html` (V3d använder `data-src`) | `Exempelsida: Hōrai, Asian fusion-koncept` |

Bilderna ligger kvar där de ligger — kopiera inte in dem i cellen. De serveras från
repo-roten via `--fallback-root`, precis som för V3d.

---

## 7. BORT — det som inte längre passar

Dessa delar av V3d **ska inte** finnas i V3e:

1. **Det vändbara visitkortet.** Ersätts av provetiketten (§4.2). Copyn behålls,
   ­180°-rotationen tas bort.
2. **Det självritande ritningsarket (SVG).** K3 äger "Ritningen"; V3e upprepar den
   inte. Processen blir ett linjerat register i stället.
3. **Den mörka grafitgrunden `#0b0c0e` och den blå accented `#1e5e9c`.** Hela
   registerbytet. Behåll **en** tonal inversion (§4.6), inte en mörk sida.
4. **Helskärmsifyllda, scroll-pinnade inbäddningar.** Proven blir ark i ett ark.
5. **Alla interna spår i kommentarer:** `PLAN 0XX`, `R-nummer`, `F-0XX`,
   `Astra rNN`, `Target N`, `gate NN`, `TASTE §N`, `C-8`, mätvärden
   (`958 px stilla baksida`, `3,64:1`, `--tx-a 0,2258`), `COPY-V3d-*.md`-hänvisningar,
   och filhuvudet som felaktigt säger `cell V3c`. Kommentarer i V3e ska förklara
   **varför**, inte hänvisa till rundor.
6. **`data-preview`- och `?preview=`-mekaniken** om den inte behövs för rörelsen —
   den är testinfrastruktur. Om du behåller en motsvarighet, namnge den för vad den
   gör i V3e.
7. **Den beskrivande mikrotexten**, om någon finns. Ingen text får berätta vad
   sektionen strax ska göra.

---

## 8. Rörelse

Rörelsen spelar **alltid** upp — ingen `prefers-reduced-motion`-gata, inget statiskt
reservdokument. Detta är husets regel (F-011) och gäller även här.

En delad reveal (rader och ark tonar in när de passerar mitten) plus **en**
signatur-set-piece med minst två koordinerade lager. Set-piece i V3e: när
`#case`-kapitlet öppnar sig **rätar arkets linjer ut sig samtidigt som proven
glider in i sina rutor** — rutnätsreglerna ritas ut från vänster medan proven
sätter sig. Två lager, en rörelse.

Dämpad rörelse läser scrollprogressen, aldrig rå `--sc-p` för `transform`,
`clip-path`, `object-position`, `mask-position` eller `background-position`.

---

## 9. Vad du ska lämna in

1. `runs/V3e/index.html` — hela sidan, en fil.
2. `runs/V3e/RAPPORT.md` — kort: vad du byggde, vilka strängar du hämtade varifrån,
   vad du uteslöt och varför, vad du är osäker på.

**Skriv ingen UI-kod förrän du läst `runs/V3d/index.html` och förstått hur den
hanterar scrollprogress, iframe-laddning och bildservering.** Återanvänd dess
mekanismer där de är bra; byt bara det visuella.

Fråga inte om lov för detaljer — välj, bygg, och skriv valet i rapporten.
