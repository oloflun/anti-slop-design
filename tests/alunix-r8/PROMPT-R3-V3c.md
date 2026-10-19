# Alunix r8, runda 3. Cell {{KONCEPT}}. Hela sidan.

Samma session, samma cell. Nu fyller du **alla** sektioner enligt `{{UT_MAPP}}/BRIEF.md` och
tar bort varje `<!-- R3 -->`-platshållare. Sedan kör du de fem stegen nedan i **din egen
session**, i den här ordningen, **namngivna i transkriptet**. Att de körs hos dig och inte
bara hos lead är hela poängen med rundan: det är luckan r7 lämnade och r8 stänger.

Signaturakten från R2 rörs bara om ett steg nedan hittar ett fel i den. Ordagrann
Alunix-copy rörs aldrig.

---

## 1. Sidan färdig

Sju skärmar enligt målbilden och BRIEF.md § direction contract, i ordning: heron som pinnad
akt (s1 till s3), tesen med Hyperborea-bleeden (s4), Calyx som ljus iframe med liggaren
(s5), prisblocket med Hōrai (s6), avslutet med mailto (s7).

Kolumnfördelningen är låst av målbilden: **vänster** blå tes, sedan Calyx, sedan pris;
**höger** jätterubrik och liggare, sedan Hōrai. `section.panel-open` och
`section.panel-services` finns inte. Inga kort, inga badges, inget glas, ingen spotlight.

Lyftet ur målbilden ska vara på plats: allt bespoke läser `--sc-ps`, `.giant` har ingen
permanent `will-change`, Geist 700 och Public Sans 300 preloadas, hero-bilden har
`decoding="async"` och `fetchpriority="high"`, iframes har `loading="lazy"` och
IO-montering, `content-visibility: auto` på `.price` och `.horai-wrap`, `text-wrap: balance`
på rubriker, `:focus-visible` med 2 px offset och minst 3:1 mot **båda** grunderna,
hårlinjerna på `--rail-x`-rastret, och 320 / 375 / 414 / 768 verifierade (kortet blir 4:5
under 640 px och vänds fortfarande).

Kirurgiska `Edit`-anrop, en sektion i taget. `Write` av hela filen bara om du skriver den
från noll, vilket du inte gör i den här rundan.

---

## 2. De fem stegen, i din egen session, namngivna i transkriptet

**Steg 1. `Skill(emil-design-eng)`.**
En Before/After/Why-tabell för **varje** övergång och varje rörelse på sidan, inte bara för
signaturakten. Sedan slow-motion-granskning av signaturakten: DevTools 10 %-hastighet
motsvaras här av `motion_probe.py --wheel 20:120`. Läs sparklinen som bild. Skriv tabellen i
NOTES.md.

**Steg 2. Copy-gaten, fem pass, vart och ett namngivet i transkriptet.**
Gäller **bara nya strängar**. Ordagrann copy ur § 4 nedan rörs inte, inte ett tecken.

1. **Pass 0, UX-copy:** varje sträng läses som gränssnittstext. Vad ska läsaren göra eller
   förstå av den raden.
2. **`Skill(copywriting)`.**
3. **`Skill(copy-editing)`:** sju svep plus loop-backs, som skillen beskriver dem.
4. **`Skill(humanizer-svenska)` på varje svensk sträng** och **`Skill(humanizer)` på varje
   engelsk**. Sidan är svensk; engelska strängar finns bara om du infört dem.
5. **Maskinellt plus hand:** `python ~/.agents/skills/slopmonster/tools/deslop.py --view` per
   sektion (engelsk detektering), **svenska tvillingar för hand** eftersom verktyget inte
   täcker svenska, och den **sexstegs manuella cleanse-listan**.

Noll tankstreck i synlig text. Tesrubriken är `VI BYGGER ERT VARUMÄRKE.` i versal form.

**Steg 3. `Skill(review-animations)`.**
Rapporten i sin helhet i transkriptet. **Standard 8 (reduced motion) gäller inte** i r8:
rörelsen spelar alltid (F-011). Flagga inte frånvaron, motivera den inte, bygg inget
reservläge.

**Steg 4. `Skill(a11y-audit)`.**
Åtta pass. Kör skripten mot din egen URL:

```
python ~/.claude/skills/a11y-audit/scripts/a11y_scan.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html
python ~/.claude/skills/a11y-audit/scripts/tab_walk.py  --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html
python ~/.claude/skills/a11y-audit/scripts/reflow.py    --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html
```

och **en gång mot `tests/a11y/broken.html`**, som kontroll att skripten faktiskt hittar fel.
Obligatoriska fynd att adressera: `title` på varje `<iframe>`, fyra landmärken, sticky chrome
vid 200 % zoom, överlevnad i forced-colors, och kontrast per grund
(`contrast_over_media.py --url`) eftersom sidan har två grunder. `tab_walk.py` scrollar inte:
läs `rect.top` och räkna inte offscreen-element som dolda. `reflow.py` punkt (c) är ett mått
på oavslöjat innehåll, inte på reducerad rörelse.

**Steg 5. Den mekaniska grinden.**

```
python ~/.claude/skills/design/scripts/preflight_taste.py {{UT_MAPP}}/index.html --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html
python ~/.claude/skills/design/scripts/perf_probe.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --cpu 4
node ~/.agents/skills/impeccable/scripts/detect.mjs --json {{UT_MAPP}}/index.html
```

Alla gröna, eller namngivna undantag i NOTES.md med skäl och källa. `perf_probe` körs vid
både 1440 och 390.

---

## 3. Skärmbilder

Vid **320, 375, 414, 768 och 1440**, båda world-grunderna (den mörka och papperet), plus
`?preview=front`, `?preview=mid` och `?preview=back`. **Läs varje bild själv, som pixlar.**
Dessutom **fem folds vid 1440 som kontaktark**. Allt i `{{UT_MAPP}}/shots/r3/`.

---

## 4. Alunix, fakta (inget annat får hittas på)

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

## 5. Målbilden för {{KONCEPT}}, fortfarande bindande

Ordagrant ur planens § 7.5.

#### V3c · Plåt i grunden · kortet vänds

*Iteration av V3b, inte nytt bygge: registrets V3-rad uppdateras till V3c; fingerprint-gaten (≥4/6) gäller K3/K4, inte V3c.* Grundkonceptet och estetiken är låsta: kontinuerlig svartvit grund (`k4-cabin-desk.webp`), R5-världen vänster (Geist, `#0b0c0e`/`#1e5e9c`), R6-världen höger (Public Sans, `#fdfbf4`), rubriken utanför platen i affischskala, Hyperborea-platen som bleeder, ordscrubben i liggaren, Calyx/Hōrai live.

**Heron blir en pinnad akt.** `section.hero` får `data-sc-act="pin" data-sc-span="2.2" data-sc-dwell="0.35"` (var `flow`), med motorns stage-markup från `template.html` (aldrig restylade `.sc-*`-klasser, AB06). Rubriken, platen och underraden är stagens *ground* (synliga från p = 0; "ground or greet" uppfyllt utan cue). Ingen scroll-cue-text (gate 88).

**Kortet.** `figure.hero-plate` (samma storlek: `width:min(100% − 2·rail, 56vh·16/9)`, 16:9, vänsteranknuten vid `--rail-x`) får `perspective: 1600px`. Inuti: `.plate-card{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateY(calc(var(--flip,0) * -180deg))}` med två `.face` (`backface-visibility:hidden`, hairline `--frame-line`). **Framsidan** = dagens innehåll (logo-dock + `#heroPoolImg`; ljuspölen vandrar vidare, nu på `--sc-ps`). **Baksidan** (`transform:rotateY(180deg)`, `background:var(--c-black)`): `ALUNIX` i Geist 700, `clamp(3.2rem, 9cqw, 7.5rem)`, `line-height:.9`, uppercase (displayskala ≥ 5× body, TASTE §2.4); under: `Digital byrå` som kicker (Geist Mono 10.5 px, .22 em; en av sidans ≤ 4 monoetiketter); hairline; raden `Design  Utveckling  System` i samma monoregister (samma ordning som liggaren 01–03, så att de två listorna inte motsäger varandra; **öppen fråga till Anton**: hans meddelande listade "utveckling, design, system", är ordningen avsiktlig?); `Boka ett möte →` som typsatt länk (Geist 700, understruken i accent). **Ingen tidsstämpel, ingen `2026 · SVERIGE`, ingen lede** (underraden under platen bär redan leden; två leder i folden vore dubbelt).

**Koreografin på `--sc-ps`** (aldrig rå `--sc-p`): `flip = smoothstep(0.12, 0.72, ps)` i sidans JS (skrivs som `--flip` på `.plate-card`); p 0–0,12 stilla, ljuspölen vandrar; 0,12–0,72 vändningen (Y-axeln, som ett visitkort man vänder med handen; vid 90° syns bara hairlinen, det är ärligt); 0,72–1 baksidan i vila, dwell låter den landa. `will-change:transform` sätts på `.plate-card` bara medan `0 < ps < 1` och tas bort i vila. Båda riktningarna. `?preview=back` tvingar `--flip:1`. Rubriken står kvar hela tiden (stagens ground); underraden också.

**Under heron.** `section.panel-open` (svarta konsolkortet) **tas bort**; dess innehåll bor nu på kortets baksida. `section.panel-services` (Tjänster, tre lika kolumner 01–03) **tas bort** som dubblett av liggaren (och gate 3-familj). Ny kolumnfördelning, materialväxling i båda spalterna (TASTE §4.5): **vänster** = blå tes (Hyperborea-bleed) → Calyx (ljus iframe) → **pris** (mörk); **höger** = jätterubrik + liggare (papper) → Hōrai (mörk iframe). `calyx-wrap` behåller `flex:1`. Arkitekten läser kolumnvikten som pixlar (squint: ingen kolumn får bära mindre vikt än sin bredd) och får flytta priset tillbaka till höger om vänster blir för tung.

**Lyftet i V3c (utan att ändra konceptet):** allt bespoke (`paintMotion`, `paintHeroPool`, ordscrubben) läser `--sc-ps`; `.giant`:s permanenta `will-change` bort; preload av Geist 700 + Public Sans 300; `decoding="async"` + `fetchpriority="high"` på hero-bilden; `loading="lazy"` + IO-montering på iframes; `content-visibility:auto` på `.price`/`.horai-wrap`; `text-wrap: balance` på rubriker; hover/focus på de tre länkarna (`:focus-visible` 2 px offset ≥ 3:1 mot båda grunderna); hairlinerna på `--rail-x`-rastret; 320/375/414/768 verifierade (kortet blir 4:5 under 640 px som idag och vänds fortfarande); copy-gaten bara på de ändrade strängarna (ordagrann copy bevaras).

**Vad referenserna gör som V3c måste slå** (låses via `select.py`; förväntat: `garden-eight`, `mattis-studio`, `squarespace`, ev. `creative-giants`): Garden Eight: *ett typografiskt moment, ett skulpturalt moment, åtskilda av tystnad* → V3c:s hero får bara rubrik + kort + en rad, inget mer. Mattis: konsolkortet med hörnmarkeringar är platt → V3c:s kort är ett *fysiskt* kort som vänds. Squarespace: svarta/vita band med ett statistikblock → V3c:s inversioner ska vara lika rena, utan kort.

**Låsta referenser:** `oryzo-ai` (primär i katalogen), `mattis-studio`, `dope-security`,
`monologue`, `planhat` (wildcard). Primär riktning enligt `reference-lock.md` Tier 0 är V3b
själv.

---

## 6. Invarianter i r8

1. **F-011, rörelsen spelar alltid.** Skriv aldrig `prefers-reduced-motion`, bygg aldrig ett
   reservläge, beskriv aldrig ett. `Skill(review-animations)` standard 8 gäller inte.
2. **F-014, `--sc-ps`.** Allt ögat ser förflytta sig läser `--sc-ps`. Rå `--sc-p` bara för
   cue-opacitet. Motorn redigeras aldrig, `.sc-*` restylas aldrig, `sc-smooth.js` ligger
   kvar. `staircase = 0`, `max_step <= 3 %` på spelhuvudet `--sc-ps` (på härledda spår som
   `transform` rapporteras talet men grindar inte, Q22 avgjord 2026-09-10), p95 <= 20 ms,
   noll frames > 33 ms, båda riktningarna. Spåra aldrig rått `--sc-p`.
3. **UI-filer författas bara med `Write` eller `Edit`.** `design-gate.py` nekar `cat >`,
   heredoc, `tee`, `sed -i`, `Set-Content`/`Out-File` och inline-skript i en armad session;
   nekandet syns i ledgern som `gate-deny` med signalen `shell-write`. Kopiering med `cp`
   eller `Copy-Item` är tillåten.
4. **Servern** är `serve.py` på `{{PORT}}` från repo-roten, aldrig `http.server`.
5. **Ingen generering.** Higgsfield är spärrat på din argv och har 0 krediter (free plan,
   mätt av lead 2026-09-09). Saknas material: `[needs asset: ...]` i NOTES.md och vidare.
6. **Noll tankstreck i synlig text.** Ordagrann copy ändras aldrig. Tesrubriken är versal.
7. **Inga kort, badges, glas, spotlights.** Inga påhittade fakta (`PRODUCT.md` § absences).
8. **Fullständig output.** Trunkera aldrig. Måste du pausa: `[PAUSED — sektion X av Y]` som
   sista rad, fortsätt i nästa tur. Rapporterna i steg 1 till 5 skrivs ut i sin helhet, inte
   sammanfattade.

---

## 7. Leverans

- `{{UT_MAPP}}/index.html`, hela sidan, noll platshållare kvar.
- `{{UT_MAPP}}/shots/r3/` med alla breddar, båda grunderna, `?preview=`-lägena och
  kontaktarket med fem folds.
- `{{UT_MAPP}}/NOTES.md` § R3, i denna ordning: Before/After/Why-tabellen, copy-gatens fem
  pass med vad varje pass ändrade, `review-animations`-rapporten, a11y-rapporten med
  körningarna mot både din URL och `tests/a11y/broken.html`, och probe-utfallen
  (`preflight_taste`, `perf_probe` vid 1440 och 390, `detect.mjs`) med namngivna undantag
  där något inte är grönt.

## Tillägg från lead efter R2:s F-007-kontroll (2026-09-10)

**Pilen efter `Boka ett möte` tas bort.** Gate 97 i `production-tells.md` förbjuder ett
pilsuffix på en länk eller knapp som default och tillåter det bara när decision ledger bär en
rad för det: en namngiven källa som gör det, och ett skäl specifikt för det här uppdraget.
V3c:s brief har ingen sådan rad, ingen låst referens gör det, och affordansen bärs redan av
den typsatta understrykningen i accenten som målbilden själv föreskriver. Målbilden skrev
strängen med pil som ett förbiseende, inte som ett argument, så grinden vinner.

Målvärde: strängen blir `Boka ett möte`, Geist 700, understruken i `#1e5e9c`, och `:active`
och `:focus-visible` är oförändrade. Strängen står inte i `PRODUCT.md` § Låst copy, så ingen
ordagrann Alunix-rad rörs.

## Tillägg från bevakaren (2026-09-10)

1. **Typsnitten är nu vendorade.** Under hela R2 laddades Geist 700, Geist Mono 400 och
   Public Sans 300 över nätet från Google Fonts (`[needs asset]`-kommentaren på rad 68).
   Bevakaren har hämtat latin-subsetet till `{{UT_MAPP}}/assets/fonts/`
   (`geist-700-latin.woff2`, `geist-mono-400-latin.woff2`, `public-sans-300-latin.woff2`,
   se `assets/ASSETS.md` rad 11–13). Du gör bytet: ta bort `preconnect`- och Google
   Fonts-länkarna, skriv tre `@font-face` med `font-display: swap`, `unicode-range` för latin
   och metrikmatchad fallback per familj, och `preload` för Geist 700 och Public Sans 300
   (§ 1 kräver det). Bekräfta först i transkriptet att de tre filerna svarar 200 på din port.
   Varje mätning och skärmbild från R2 tas om i den här rundan, folden och signaturakten
   inräknade.
2. **Copy-gaten gäller R2:s strängar också.** Steg 2 säger "bara nya strängar"; R2:s strängar
   passerade aldrig gaten (route-gapet lead mätte: 1 per cell), så de räknas som nya. Ordagrann
   copy ur § 4 rörs fortfarande inte.
3. **Bildtid i vändningsakten vid 4× CPU.** Bevakarens mätning 2026-09-10 gav 6 till 14 rutor
   > 33 ms, alla under flippen, p95 upp till 33 ms. Värden var brusig, så talet är osäkert.
   Mätprotokoll: kör först
   `python ~/.claude/skills/design/scripts/motion_probe.py --url http://127.0.0.1:{{PORT}}/tests/motion/smooth.html --cpu 4 --track "#act:--sc-ps,#card:transform"`
   som kontroll; ger kontrollen någon ruta > 33 ms är fönstret brusigt, vänta en minut och
   kör om. Först när kontrollen är noll mäter du sidan:
   `--track "section.hero:--sc-ps,.plate-card:transform" --cpu 4 --wheel 100:60` och sedan
   `--wheel 20:120`. Faller sidan på rutor > 33 ms när kontrollen är ren, är det flippens
   kostnad per ruta: ta bort varje `box-shadow`, `filter` och `backdrop-filter` som ritas
   om under `0 < ps < 1`, ge kortet `contain: paint` och `will-change: transform` bara i det
   fönstret, och mät om. Skriv båda talen (kontroll och sida) i NOTES.md § R3.
4. `max_step` på `.plate-card:transform` är inte längre ett fel (Q22). Platta inte ut
   easingen.
