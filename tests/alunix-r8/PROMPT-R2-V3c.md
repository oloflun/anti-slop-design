# Alunix r8, runda 2. Cell {{KONCEPT}}. Folden och signaturakten.

Samma session, samma cell. Nu bygger du `{{UT_MAPP}}/index.html` med **folden och
signaturakten kompletta**. Resten av sidan får vara markerade platshållarsektioner:
`<!-- R3 -->` med rätt höjd och rätt grund, **inga låtsaselement**, ingen lorem, inga tomma
kort som ska "bli något sedan".

Underlaget är `{{UT_MAPP}}/BRIEF.md`, som du skrev i R1, och
`tests/alunix-r8/concepts-V3c.md`. Där de säger emot varandra gäller målbilden i § 3 nedan,
och avvikelsen får en rad i BRIEF.md § decision ledger med källa.

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

**Kortet vänds.**

- `section.hero` får `data-sc-act="pin" data-sc-span="2.2" data-sc-dwell="0.35"`.
  Rubriken, plåten och underraden är stagens **ground**, synliga från p = 0. Ingen
  scroll-cue-text (gate 88).
- `figure.hero-plate` behåller sin storlek (`width:min(100% − 2·rail, 56vh·16/9)`, 16:9,
  vänsteranknuten vid `--rail-x`) och får `perspective: 1600px`.
- Inuti:
  `.plate-card{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateY(calc(var(--flip,0) * -180deg))}`
  med två `.face` (`backface-visibility:hidden`, hairline `--frame-line`).
- **`--flip = smoothstep(0.12, 0.72, --sc-ps)`**, skrivet som `--flip` på `.plate-card` i
  sidans egen JS. Aldrig rå `--sc-p`. ps 0 till 0,12 stilla medan ljuspölen vandrar;
  0,12 till 0,72 vändningen kring Y-axeln; 0,72 till 1 baksidan i vila, dwell låter den
  landa. Båda scrollriktningarna.
- Vid 90 grader syns bara hårlinjen. Det är kontrollen på att kortet har en tjocklek och
  inte är två rektanglar som byter plats.
- `will-change: transform` sätts på `.plate-card` **bara** medan `0 < ps < 1` och tas bort i
  vila. `.giant`:s permanenta `will-change` tas bort.
- Framsidan är dagens innehåll (logo-dock och `#heroPoolImg`; `paintHeroPool` läser nu
  `--sc-ps`). Baksidan är svart med `ALUNIX` i Geist 700, kickern `Digital byrå` i Geist
  Mono 10,5 px, en hårlinje, raden `Design  Utveckling  System` i monoregister, och
  `Boka ett möte →` som typsatt länk med understrykning i accenten. Ingen tidsstämpel,
  ingen `2026 · SVERIGE`, ingen andra lede.

**`?preview=`-lägen** (enligt BRIEF.md § `?preview=`-plan, och de tre är obligatoriska):

| Läge | Tvingar |
|---|---|
| `?preview=back` | `--flip: 1` på `.plate-card`, kortbaksidan i vila |
| `?preview=front` | `--flip: 0`, baslinjen för folden |
| `?preview=mid` | `--flip: 0.5`, kontrollen att bara hårlinjen syns vid 90 grader |

---

## 3. Målbilden för {{KONCEPT}}, bindande

Ordagrant ur planens § 7.5.

#### V3c · Plåt i grunden · kortet vänds

*Iteration av V3b, inte nytt bygge: registrets V3-rad uppdateras till V3c; fingerprint-gaten (≥4/6) gäller K3/K4, inte V3c.* Grundkonceptet och estetiken är låsta: kontinuerlig svartvit grund (`k4-cabin-desk.webp`), R5-världen vänster (Geist, `#0b0c0e`/`#1e5e9c`), R6-världen höger (Public Sans, `#fdfbf4`), rubriken utanför platen i affischskala, Hyperborea-platen som bleeder, ordscrubben i liggaren, Calyx/Hōrai live.

**Heron blir en pinnad akt.** `section.hero` får `data-sc-act="pin" data-sc-span="2.2" data-sc-dwell="0.35"` (var `flow`), med motorns stage-markup från `template.html` (aldrig restylade `.sc-*`-klasser, AB06). Rubriken, platen och underraden är stagens *ground* (synliga från p = 0; "ground or greet" uppfyllt utan cue). Ingen scroll-cue-text (gate 88).

**Kortet.** `figure.hero-plate` (samma storlek: `width:min(100% − 2·rail, 56vh·16/9)`, 16:9, vänsteranknuten vid `--rail-x`) får `perspective: 1600px`. Inuti: `.plate-card{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateY(calc(var(--flip,0) * -180deg))}` med två `.face` (`backface-visibility:hidden`, hairline `--frame-line`). **Framsidan** = dagens innehåll (logo-dock + `#heroPoolImg`; ljuspölen vandrar vidare, nu på `--sc-ps`). **Baksidan** (`transform:rotateY(180deg)`, `background:var(--c-black)`): `ALUNIX` i Geist 700, `clamp(3.2rem, 9cqw, 7.5rem)`, `line-height:.9`, uppercase (displayskala ≥ 5× body, TASTE §2.4); under: `Digital byrå` som kicker (Geist Mono 10.5 px, .22 em; en av sidans ≤ 4 monoetiketter); hairline; raden `Design  Utveckling  System` i samma monoregister (samma ordning som liggaren 01–03, så att de två listorna inte motsäger varandra; **öppen fråga till Anton**: hans meddelande listade "utveckling, design, system", är ordningen avsiktlig?); `Boka ett möte →` som typsatt länk (Geist 700, understruken i accent). **Ingen tidsstämpel, ingen `2026 · SVERIGE`, ingen lede** (underraden under platen bär redan leden; två leder i folden vore dubbelt).

**Koreografin på `--sc-ps`** (aldrig rå `--sc-p`): `flip = smoothstep(0.12, 0.72, ps)` i sidans JS (skrivs som `--flip` på `.plate-card`); p 0–0,12 stilla, ljuspölen vandrar; 0,12–0,72 vändningen (Y-axeln, som ett visitkort man vänder med handen; vid 90° syns bara hairlinen, det är ärligt); 0,72–1 baksidan i vila, dwell låter den landa. `will-change:transform` sätts på `.plate-card` bara medan `0 < ps < 1` och tas bort i vila. Båda riktningarna. `?preview=back` tvingar `--flip:1`. Rubriken står kvar hela tiden (stagens ground); underraden också.

**Under heron.** `section.panel-open` (svarta konsolkortet) **tas bort**; dess innehåll bor nu på kortets baksida. `section.panel-services` (Tjänster, tre lika kolumner 01–03) **tas bort** som dubblett av liggaren (och gate 3-familj). Ny kolumnfördelning, materialväxling i båda spalterna (TASTE §4.5): **vänster** = blå tes (Hyperborea-bleed) → Calyx (ljus iframe) → **pris** (mörk); **höger** = jätterubrik + liggare (papper) → Hōrai (mörk iframe). `calyx-wrap` behåller `flex:1`. Arkitekten läser kolumnvikten som pixlar (squint: ingen kolumn får bära mindre vikt än sin bredd) och får flytta priset tillbaka till höger om vänster blir för tung.

**Lyftet i V3c (utan att ändra konceptet):** allt bespoke (`paintMotion`, `paintHeroPool`, ordscrubben) läser `--sc-ps`; `.giant`:s permanenta `will-change` bort; preload av Geist 700 + Public Sans 300; `decoding="async"` + `fetchpriority="high"` på hero-bilden; `loading="lazy"` + IO-montering på iframes; `content-visibility:auto` på `.price`/`.horai-wrap`; `text-wrap: balance` på rubriker; hover/focus på de tre länkarna (`:focus-visible` 2 px offset ≥ 3:1 mot båda grunderna); hairlinerna på `--rail-x`-rastret; 320/375/414/768 verifierade (kortet blir 4:5 under 640 px som idag och vänds fortfarande); copy-gaten bara på de ändrade strängarna (ordagrann copy bevaras).

**Vad referenserna gör som V3c måste slå** (låses via `select.py`; förväntat: `garden-eight`, `mattis-studio`, `squarespace`, ev. `creative-giants`): Garden Eight: *ett typografiskt moment, ett skulpturalt moment, åtskilda av tystnad* → V3c:s hero får bara rubrik + kort + en rad, inget mer. Mattis: konsolkortet med hörnmarkeringar är platt → V3c:s kort är ett *fysiskt* kort som vänds. Squarespace: svarta/vita band med ett statistikblock → V3c:s inversioner ska vara lika rena, utan kort.

**Låsta referenser** (ur `select.py`, samma rad som i R1): `oryzo-ai` (primär i katalogen),
`mattis-studio`, `dope-security`, `monologue`, `planhat` (wildcard). Primär riktning enligt
`reference-lock.md` Tier 0 är V3b själv,
`tests/alunix-concepts-r5/cells/V3b-chain/index.html`.

---

## 4. Prestanda från första raden, inte som en efterhandsstädning

- `width` och `height` samt `decoding="async"` på **varje** `<img>`.
- `fetchpriority="high"` på LCP-bilden (hero-bildens framsida).
- `<link rel="preload">` för displaysnittet (Geist 700) och Public Sans 300.
- Varje `<iframe>` får `loading="lazy"` **och** monteras via IntersectionObserver.
  Ramen transformeras eller tonas aldrig efter att den visats.
- `min-height: 100dvh`, aldrig `100vh`.
- Ingen `transition: all`. Ingen permanent `will-change`. Noll `box-shadow`.
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
  --track "section.hero:--sc-p,section.hero:--sc-ps,.plate-card:transform" \
  --cpu 4 --out {{UT_MAPP}}/shots/r2
```

Har du döpt akten eller det roterande elementet till något annat: byt ut selektorerna, men
`--track` måste innehålla aktens `--sc-p`, aktens `--sc-ps` och det rörliga elementets
`transform`. Kör `motion_probe` med både `--wheel 100:60` och `--wheel 20:120`.

**Läs kontaktarket och sparklinen som bilder**, inte som filnamn. `staircase` **måste vara
0** innan du lämnar rundan, och `max_step <= 3 %`, bildtid p95 <= 20 ms, noll frames
> 33 ms. Är den inte det: rätta rörelsen och mät om. En akt som stegar är inte klar,
oavsett hur den ser ut på en stillbild.

Skärmbilder: 1440 och 390, plus vart och ett av de tre `?preview=`-lägena. Läs varje bild
själv.

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
oförändrat.

---

## 7. Invarianter i r8

1. **F-011, rörelsen spelar alltid.** Skriv aldrig `prefers-reduced-motion`, bygg aldrig ett
   reservläge, beskriv aldrig ett. Frånvaron är beslutad (FEEDBACK.md F-011) och ingen
   granskare i r8 flaggar den.
2. **F-014, `--sc-ps`.** Allt ögat ser förflytta sig läser `--sc-ps`. Rå `--sc-p` får bara
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
   (`PRODUCT.md` § absences).
8. **Fullständig output.** Trunkera aldrig. Måste du pausa: `[PAUSED — sektion X av Y]` som
   sista rad, fortsätt i nästa tur.

---

## 8. Leverans

- `{{UT_MAPP}}/index.html` med folden och signaturakten kompletta, resten som markerade
  `<!-- R3 -->`-platshållare med rätt höjd och grund.
- `{{UT_MAPP}}/scroll/` med motorn och `sc-smooth.js`, oförändrade.
- `{{UT_MAPP}}/shots/r2/` med skärmbilder, kontaktark och sparklines.
- `{{UT_MAPP}}/NOTES.md` § R2: vad som avviker från målbilden och varför, med källa; de
  mätta talen ur `motion_probe` (`staircase`, `max_step`, p95, frames > 33 ms) för båda
  hjulhastigheterna och båda riktningarna; vad du läste i kontaktarket och sparklinen.


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

**Två rader i V3c:s takavsnitt är inte takrader.** `garden-eight` och `squarespace` kommer ur
planens paragraf 7.5-förväntan, som `select.py` ersatte, och ingen av dem lästes i cellens
session. Takraderna gäller de fem låsta sluggarna och bara dem: `oryzo-ai`, `dope-security`,
`mattis-studio`, `monologue`, `planhat`. Kritikern skriver "slår" för de fem. Behåll de två
villkoren som text under en egen rubrik "Ärvda villkor från V3b" om du vill ha dem kvar, men
de räknas aldrig som referenser och de får inget "slår".
