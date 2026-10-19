# Alunix r8, runda 2. Cell {{KONCEPT}}. Folden och signaturakten.

Samma session, samma cell. Nu bygger du `{{UT_MAPP}}/index.html` med **folden och
signaturakten kompletta**. Resten av sidan får vara markerade platshållarsektioner:
`<!-- R3 -->` med rätt höjd och rätt grund, **inga låtsaselement**, ingen lorem, inga tomma
ramar som ska "bli något sedan".

Underlaget är `{{UT_MAPP}}/BRIEF.md`, som du skrev i R1,
`tests/alunix-r8/concepts-K3.md` och SVG-specen i `{{UT_MAPP}}/assets/ASSETS.md`. Där de
säger emot varandra gäller målbilden i § 3 nedan, och avvikelsen får en rad i BRIEF.md
§ decision ledger med källa.

---

## 1. Motorn

Kopiera in, oförändrad, med `cp` eller `Copy-Item` (kopiering från skalet är tillåten och
är den avsedda vägen):

```
~/.claude/skills/design/scripts/scroll/scrollcraft.js   ->  {{UT_MAPP}}/scroll/
~/.claude/skills/design/scripts/scroll/scrollcraft.css  ->  {{UT_MAPP}}/scroll/
~/.claude/skills/design/scripts/scroll/sc-smooth.js     ->  {{UT_MAPP}}/scroll/
```

`sc-smooth.js` ligger bredvid motorn och laddas efter den. **Motorn redigeras aldrig.**
`.sc-*`-klasserna restylas aldrig (AB06). Stage-markupen tas ur motorns egen
`template.html`.

---

## 2. Signaturakten för {{KONCEPT}}, exakt

**Ritningen ritar sig, och blir sedan sidan.**

- Den pinnade akten: `data-sc-act="pin" data-sc-span="2.4" data-sc-dwell="0.35"`,
  cue `0 1 0 0`. Titelblocket är stagens **ground**, synligt från ps = 0. Ingen
  scroll-cue-text (gate 88).
- Ritningen är **en** `<svg>` med högst 60 `path`/`line`-element. Varje bana ritas med
  `stroke-dashoffset`, driven av `--sc-ps` genom `calc()` i CSS. Ingen per-frame
  JS-skrivning per bana.
- **Varje `--lN` registreras med `@property`:**

  ```css
  @property --l1 { syntax: "<number>"; inherits: false; initial-value: 0; }
  ```

  Detta är obligatoriskt och det är inte en detalj. Utan `syntax: "<number>"` är den lokala
  variabeln en osparsad token, interpoleras inte, och **ritningen stegar bana för bana** i
  stället för att flyta. Det är exakt F-012-felet, och `motion_probe` kommer att mäta det
  som `staircase > 0`.
- Ritordningen är en enda obruten hand: yttre kontur, hjälplinjer, måttlinjer, utrop.
  Ingenting tonar in ur intet; varje element startar i en linjeände som redan var synlig.
  Att scrolla uppåt suddar linjen i exakt omvänd ordning.
- Måttsiffrorna räknar upp till sina **sanna** värden (`320`, `768`, `1440`, `7 rem`,
  `96 px`, `16:9`, priserna) med motorns egen `count`. Ingen siffra som inte är ett
  verkligt mått eller pris.
- Öppningen som fylls är **samma rektangel** som konturen just ritade, inte en ny ruta
  ovanpå (F-010). Calyx monteras innanför konturen; bläcket ligger kvar som ram.
  Masken (`mask-position` eller `clip-path`) läser `--sc-ps`.
- `will-change: stroke-dashoffset` sätts **bara** medan `0 < ps < 1` och tas bort i vila.
- De första 0,12 av akten är författad tystnad: ett nästan tomt ark med bara titelblocket.
  Det ska stå i BRIEF.md så att `scroll_verify.py`:s `blankBands` inte larmar falskt.

**Gate 47 och gate 79, cellens känsligaste punkt.** Ritningen ritar **form**, aldrig
**innehåll**. Tillåtet i SVG: konturer, måttlinjer med pilspetsar, hjälplinjer,
snittmarkeringar, skrafferingar och utrop som anger ett mått eller namnet på en zon.
Förbjudet: rektanglar som föreställer knappar, grå staplar som föreställer text, navrad,
formulär, graf, sparkline, webbläsarram, flikrad, URL-fält, telefonbezel. Varje `<rect>` och
`<path>` ska kunna namnges som "kontur", "måttlinje", "hjälplinje", "skraffering" eller
"utrop". Kan den inte det ska den bort. Arkitektens F-007-kontroll läser folden som pixlar
och prickar av detta bild för bild.

**`?preview=`-lägen** (enligt BRIEF.md § `?preview=`-plan; alla fem är obligatoriska):

| Läge | Tvingar |
|---|---|
| `?preview=sheet` | `--sc-ps: 0` i akten: tomt ark, bara titelblocket |
| **`?preview=drawn`** | **Det ritade läget:** varje banas lokala `--lN` = 1, hela ritningen färdig, måttsiffrorna landade på sina sanna tal, men öppningen ännu **inte** fylld |
| `?preview=filled` | `--sc-ps: 1`: Calyx monterad i öppningen, konturen kvar som ram, siffrorna nedskalade |
| `?preview=mid` | `--sc-ps: 0.94`, siffrorna halvvägs i nedskalningen |
| `?preview=spec` | Avslutets ram fullt indragen |

---

## 3. Målbilden för {{KONCEPT}}, bindande

Ordagrant ur planens § 7.5.

#### K3 · "Ritningen" (nytt koncept 1)

**Idé.** Alunix ritar innan de bygger. Sidan är en teknisk ritning av en webbplats på kallt ritpapper: en dimensionerad sektionsritning av en sida (konturer, måttlinjer, utrop med **sanna** värden: 320/768/1440, `7 rem`, `96 px`, `16:9`, priserna) som ritar sig själv när man scrollar, och sedan *blir* det den ritade: den riktiga Calyx-sidan tonar in **innanför den ritade konturen** (F-010-principen: innehållet maskas in i objektets verkliga öppning, bläcket ligger kvar som ram). Noll fotografier (Hyperborea-precedens). Aldrig en falsk UI-mock (gate 79): ritningen har inga låtsasknappar eller låtsastext, bara konturer, måttlinjer och utrop.

**Auktoritet:** ytan (papper + bläck; TASTE §1 rad 3); typen medelstor; bilder inga; i set-piece-akten rörelsen. **Register:** modern clean (ämnet är precision). **Grammatik:** chaptered editorial (titelsida utan media; folio; kolofon-liknande *specifikation* som avslut). **Palett:** ett kallt ritpapper (oklch ~0.95, hue 230, låg chroma; *inte* cream, AB09-lärdomen), ett bläck (mörk petrol/ultramarin), Alunix-blått `#1E5E9C` (Tier 1-bevis) som enda accent, bara på måttsiffrorna i displayskala. **Typ:** en grotesk med teknisk karaktär i två snitt + en mono som register (måtten). Arkitekten kör brand.md-proceduren; **förbjudna**: reflex-listan och alla snitt som använts i r1–r7 (Geist, Inter, JetBrains Mono, Public Sans, Familjen Grotesk, Literata, Fragment Mono, Hanken Grotesk, Instrument Serif, Archivo, IBM Plex Mono, Figtree, Cardo, PT Mono, Cinzel, Vollkorn, Italiana).

**Nav:** en ritad *teckenförklaring* (legend) i marginalen, sticky, som är sidans index (varje rad = ett kapitel, en linje dras till kapitlet när det är aktivt). **Hero-device:** ritningen ritar sig (SVG `stroke-dashoffset` från `--sc-ps`, pinnad akt span 2.4 = toppen), måttsiffrorna räknar upp till sina sanna värden (`count`, bara riktiga tal). **Aktform:** pin (ritningen) → kinetic lines (kapitelrubrik "Vi bygger ert varumärke.") → reveal ×3 (en plate per exempelsajt: konturen ritas, sedan tonar den riktiga sajten in innanför konturen, bläcket blir ram; iframe monteras lazy) → flow+in (liggaren 01–03) → count+flow (specifikationen: paketen som stycklista med de sanna priserna) → close. ≥ 5 familjer, aldrig samma två i rad. **Avslut:** specifikationsbladet (priser, `Alla har rätt till bra design.`, en mailto) inom en ritad ram vars linjer dras in sist; sidan slutar stilla. **Signaturrörelse:** *ritningen blir sidan*: konturen ritas, fylls med den levande sajten, bläcket stannar som ram. Tell-someone: "det är sajten där man ser hemsidan ritas som en ritning och sen blir den på riktigt".

**Referenser (förväntade ur `select.py`):** `caractere-bois` (hårlinje-ritningar över foton: "designat innan byggt"), `hyperborea` (ritat identitetssystem, noll foton), `wild` (pixelritad silhuett som banner), `garden-eight` (ett typografiskt + ett skulpturalt moment), `tidvatten` (modern clean, två sanna siffror som set-piece). Anti-referens: `before-ai-slop` (div-byggd låtsas-UI).

**Målbildsgrind:** (1) auktoritet ytan; viker: typ (medel), foto (inget), färg (en accent på måtten). (2) troplistan: inga kort, inga badges, inget glas, ingen gradient, ingen spotlight; **ritning ≠ falsk UI** kontrolleras mot gate 47/79 bild för bild. (3) ett displayelement per skärm: ritningen (s1), kapitelrubriken (s2), en plate i taget (s3–5), priserna (s6), mailto (s7). (4) fingerprint: mot Hyperborea (grammatik delad → nav legend ≠ sticky header+edition strip · hero ritning ≠ SVG-sol · aktform ≠ · avslut specifikation ≠ kolofon · signatur ≠ → 5/6); mot r1 K4 Journal, r2 R2/R3/R4, r4 M2 (alla chaptered): ≥4/6 på nav/hero/akt/signatur; arkitekten skriver ut alla 36 rader.

**Låsta referenser** (ur `select.py`, samma rad som i R1): `squarespace` (primär), `insign`,
`aevi-wellness`, `beautiful`, `mode` (wildcard). Anti-referens att bygga bort i varje detalj:
`sites/before-ai-slop.html`.

---

## 4. Prestanda från första raden, inte som en efterhandsstädning

- `width` och `height` samt `decoding="async"` på **varje** `<img>`.
- `fetchpriority="high"` på LCP-elementets bild om folden har en.
- `<link rel="preload">` för displaysnittet och för monon; två variabla filer, tak 300 kB.
- Varje `<iframe>` får `loading="lazy"` **och** monteras via IntersectionObserver, aldrig
  fler än en igång samtidigt. Ramen transformeras eller tonas aldrig efter att den visats.
- `min-height: 100dvh`, aldrig `100vh`.
- Ingen `transition: all`. Ingen permanent `will-change`. Noll `box-shadow`, noll
  `backdrop-filter`, noll gradient, radie 0.
- Papperstexturen rastreras en gång och animeras aldrig.
- Budgeten står i `~/.claude/skills/design/references/performance.md` § 1 och i BRIEF.md
  § Prestandaplan.

---

## 5. Kör verifieringen själv innan du lämnar rundan

Från repo-roten, i din egen session:

```
python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .

python ~/.claude/skills/design/scripts/scroll_verify.py \
  --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --out {{UT_MAPP}}/shots/r2

python ~/.claude/skills/design/scripts/motion_probe.py \
  --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html \
  --track "section.drawing:--sc-p,section.drawing:--sc-ps,#outline-1:stroke-dashoffset" \
  --cpu 4 --out {{UT_MAPP}}/shots/r2
```

Byt ut selektorerna mot dina faktiska namn, men `--track` måste innehålla aktens `--sc-p`,
aktens `--sc-ps` och **den ritade banans** `stroke-dashoffset`. Spåra dessutom en av de
registrerade `--lN` i en andra körning, så att du ser att den interpoleras och inte hoppar.
Kör `motion_probe` med både `--wheel 100:60` och `--wheel 20:120`.

**Läs kontaktarket och sparklinen som bilder**, inte som filnamn. `staircase` **måste vara
0** innan du lämnar rundan, och `max_step <= 3 %`, bildtid p95 <= 20 ms, noll frames
> 33 ms. Är den inte det: rätta rörelsen och mät om. En ritning som stegar bana för bana är
inte klar, hur rätt stillbilden än ser ut.

Skärmbilder: 1440 och 390, plus vart och ett av de fem `?preview=`-lägena. Läs varje bild
själv. `?preview=drawn` är den bild F-007-kontrollen prickar av mot gate 47/79.

---

## 6. Alunix, fakta (inget annat får hittas på)

Ordagrant ur `tests/alunix-ab-r7/PROMPT.md`.

Alunix är en webbyrå i Sverige. Sidan säljer en tjänst: webbdesign. Byrån visar vad den kan
genom tre riktiga exempelsajter som ligger i samma repo och serveras live:

- `/sites/calyx.html`: florist i Stockholm. Rad att använda: `Exempelsida: Calyx, florist i Stockholm`
- `/sites/horai.html`: restaurang, Asian fusion. Rad: `Exempelsida: Hōrai, Asian fusion-koncept`
- `/sites/hyperborea.html`: konferens i Lund. Rad: `Exempelsida: Hyperborea, konferens i Lund`

Skärmbilder av dem ligger i `{{UT_MAPP}}/assets/demo-{calyx,horai,hyperborea}.webp`. Sajterna
får visas live i `<iframe>` (samma origin när sidan serveras från repo-roten). Ramar ska vara
användbara när de är öppna: transformera eller tona aldrig själva ramelementet efter att det
visats.

Logotyp: `{{UT_MAPP}}/assets/logo-white.svg` och `logo-black.svg` (får läggas inline).

Dagens Alunix-register, som jämförelse och inte som lås: kall nästan-svart `#17181B`, blå
`#1E5E9C` bara för handling, Geist för rubrik, Inter för brödtext, JetBrains Mono för data.
Konceptet får avvika helt.

Röst: byråröst i vi-form, korta satser, fakta före adjektiv. Svenska.

### Copy som ska användas ordagrant (copy-gate: bevara, skriv inte om)

- Rubrik: `Er hemsida är nutidens visitkort`
- Underrad: `Vi skapar skräddarsydda webbplatser som hjälper er att exponera verksamheten.`
- Tesrubrik: `VI BYGGER ERT VARUMÄRKE.`
- Rad: `Webbdesign, design och system. Allt på ett ställe.`
- Tjänster, numrerade 01–03: `Design`, `Utveckling`, `System` (en kort underrad var, i
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
- Inga egna Unsplash-anrop och ingen egen server: allt material ligger i `assets/`, och servern
  är `python ~/.agents/skills/design/scripts/serve.py --port {{PORT}}` från repo-roten (från
  runda 2).

**r8-preciseringen:** serverns sökväg är
`~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .`; allt annat gäller
oförändrat. K3 har noll fotografier.

---

## 7. Invarianter i r8

1. **F-011, rörelsen spelar alltid.** Skriv aldrig `prefers-reduced-motion`, bygg aldrig ett
   reservläge, beskriv aldrig ett. Frånvaron är beslutad (FEEDBACK.md F-011) och ingen
   granskare i r8 flaggar den.
2. **F-014, `--sc-ps`.** Allt ögat ser förflytta sig läser `--sc-ps`: varje
   `stroke-dashoffset`, masken över öppningen, linjalens `scaleX`. Rå `--sc-p` får bara
   driva cue-opacitet. `sc-smooth.js` kopieras in bredvid motorn; motorn redigeras aldrig,
   `.sc-*` restylas aldrig. Akten är inte klar förrän `staircase = 0`, `max_step <= 3 %`,
   p95 <= 20 ms och noll frames > 33 ms.
3. **UI-filer författas bara med `Write` eller `Edit`.** `design-gate.py` nekar `cat >`,
   heredoc, `tee`, `sed -i`, `Set-Content`/`Out-File` och inline-skript i en armad session,
   och nekandet syns i ledgern som `gate-deny` med signalen `shell-write`. Att **kopiera**
   motorn med `cp` eller `Copy-Item` är tillåtet.
4. **Servern** är `serve.py` på `{{PORT}}` från repo-roten, aldrig `http.server`, aldrig en
   egen server.
5. **Ingen generering.** Higgsfield är spärrat på din argv och har 0 krediter (free plan,
   mätt av lead 2026-09-09). Saknas material: `[needs asset: ...]` i NOTES.md och vidare.
6. **Noll tankstreck i synlig text.** Ordagrann Alunix-copy ändras aldrig. Tesrubriken är
   `VI BYGGER ERT VARUMÄRKE.` i versal form.
7. **Inga kort, badges, glas, spotlights** (TASTE § 5, F-006). Inga påhittade fakta
   (`PRODUCT.md` § absences). Varje siffra på arket är ett verkligt mått eller pris.
8. **Fullständig output.** Trunkera aldrig. Måste du pausa: `[PAUSED — sektion X av Y]` som
   sista rad, fortsätt i nästa tur.

---

## 8. Leverans

- `{{UT_MAPP}}/index.html` med folden och signaturakten kompletta, resten som markerade
  `<!-- R3 -->`-platshållare med rätt höjd och grund.
- `{{UT_MAPP}}/scroll/` med motorn och `sc-smooth.js`, oförändrade.
- `{{UT_MAPP}}/shots/r2/` med skärmbilder, kontaktark och sparklines.
- `{{UT_MAPP}}/NOTES.md` § R2: vad som avviker från målbilden och varför, med källa; listan
  över varje ritad `<rect>` och `<path>` med sin roll (kontur, måttlinje, hjälplinje,
  skraffering, utrop); de mätta talen ur `motion_probe` för båda hjulhastigheterna och båda
  riktningarna; vad du läste i kontaktarket och sparklinen.


## Tillägg från lead efter R1-granskningen (2026-09-10)

**Skrivvägen.** Varje filskrivning i den här rundan går genom `Write` eller `Edit`, aldrig
genom skalet. `.md`-undantaget i `design-gate.py` gäller inte prosa du författar: R1 avslutades
med ett `cat >>`-heredoc mot en brief, och samma klass av skrivning är det som plattade ut
svenska diakriter till ASCII i fas 0-skeletten. Lead har rättat 127 rader för hand. R2 är
rundan som skriver kod, så vägen stängs här.

**`NOTES.md` är en leverabel, inte en möjlighet.** Skriv `{{UT_MAPP}}/NOTES.md` med rubriken
`## R2` och en rad per beslut: datum, beslut, källa (F-post, TASTE-paragraf, katalogpost eller
planens paragraf). Kravet stod bara villkorligt i R1-prompten, vilket var arkitektens lucka och
inte byggarens fel. Det är ovillkorligt nu.

**Takraderna ska bära sitt belägg.** Varje rad i `{{UT_MAPP}}/BRIEF.md` under "Vad jag måste
slå" ska namnge den slice eller den rad i referensens `entry.md` som påståendet vilar på.
Belägget finns redan i briefens egen paragraf "Lästa referenser"; det ska flyttas upp så att
raden går att verifiera där den läses. Skälet är mätt: lead läste referensernas folds som
pixlar och tre påståenden gick inte att belägga ur folden ensam. Arkitekten har sedan belagt
alla tre ur respektive `entry.md`, så ingen rad ska strykas, men pekaren ska stå i raden.
En rad utan pekare stryks ur låset i fas 2.
