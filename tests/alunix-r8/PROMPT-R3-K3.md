# Alunix r8, runda 3. Cell {{KONCEPT}}. Hela sidan.

Samma session, samma cell. Nu fyller du **alla** sektioner enligt `{{UT_MAPP}}/BRIEF.md` och
tar bort varje `<!-- R3 -->`-platshållare. Sedan kör du de fem stegen nedan i **din egen
session**, i den här ordningen, **namngivna i transkriptet**. Att de körs hos dig och inte
bara hos lead är hela poängen med rundan: det är luckan r7 lämnade och r8 stänger.

Signaturakten från R2 rörs bara om ett steg nedan hittar ett fel i den. Ordagrann
Alunix-copy rörs aldrig.

---

## 1. Sidan färdig

Elva skärmar enligt BRIEF.md § direction contract, i aktordningen: pin (ritningen, s1 till
s4) → kinetic lines (kapitelrubriken `VI BYGGER ERT VARUMÄRKE.`, s5) → reveal ×3 (en plate
per exempelsajt, s6 till s8: konturen ritas, sedan monteras den riktiga sajten innanför
konturen och bläcket blir ram) → flow och in (liggaren 01–03, s9) → count och flow
(specifikationen med de sanna priserna, s10) → close (avslutet innanför den ritade ramen,
s11). Minst fem device-familjer, aldrig samma två i rad.

Navigationen är den ritade teckenförklaringen i marginalen: sticky, en rad per kapitel, med
en ledarlinje som dras till kapitlet när det blir aktivt. Ingen topprad, ingen CTA-knapp,
inget formulär. Kontakten är en mailto i löpande text i avslutet.

**Gate 47 och gate 79 gäller varje ny sektion, inte bara folden.** Ritningen ritar form,
aldrig innehåll: varje `<rect>` och `<path>` ska kunna namnges som kontur, måttlinje,
hjälplinje, skraffering eller utrop. Ingen låtsasknapp, ingen grå stapel som föreställer
text, ingen webbläsarram runt en exempelsajt. Varje siffra på arket är ett verkligt mått
eller ett verkligt pris.

Kirurgiska `Edit`-anrop, en sektion i taget.

---

## 2. De fem stegen, i din egen session, namngivna i transkriptet

**Steg 1. `Skill(emil-design-eng)`.**
En Before/After/Why-tabell för **varje** övergång och varje rörelse på sidan, inte bara för
signaturakten. Sedan slow-motion-granskning av signaturakten: DevTools 10 %-hastighet
motsvaras här av `motion_probe.py --wheel 20:120`. Läs sparklinen som bild. Skriv tabellen i
NOTES.md.

**Steg 2. Copy-gaten, fem pass, vart och ett namngivet i transkriptet.**
Gäller **bara nya strängar**: legendens kapitelnamn, tjänsternas tre underrader, utropens
zonnamn, bildtexterna. Ordagrann copy ur § 4 nedan rörs inte, inte ett tecken.

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
(legenden) vid 200 % zoom, överlevnad i forced-colors (en ritning som bara är stroke måste
fortfarande läsas), kontrast per grund (`contrast_over_media.py --url`), och en textalternativ
för ritningen: SVG:n är informativ, inte dekorativ, så den behöver en tillgänglig
beskrivning. `tab_walk.py` scrollar inte: läs `rect.top` och räkna inte offscreen-element som
dolda. `reflow.py` punkt (c) är ett mått på oavslöjat innehåll, inte på reducerad rörelse.

**Steg 5. Den mekaniska grinden.**

```
python ~/.claude/skills/design/scripts/preflight_taste.py {{UT_MAPP}}/index.html --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html
python ~/.claude/skills/design/scripts/perf_probe.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --cpu 4
node ~/.agents/skills/impeccable/scripts/detect.mjs --json {{UT_MAPP}}/index.html
```

Alla gröna, eller namngivna undantag i NOTES.md med skäl och källa. `perf_probe` körs vid
både 1440 och 390. Skriv in det mätta talet för skalet (HTML, SVG, två snitt, textur) och för
hela överföringen.

---

## 3. Skärmbilder

Vid **320, 375, 414, 768 och 1440**, plus `?preview=sheet`, `?preview=drawn`,
`?preview=filled`, `?preview=mid` och `?preview=spec`. **Läs varje bild själv, som pixlar.**
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
oförändrat. K3 har noll fotografier.

---

## 5. Målbilden för {{KONCEPT}}, fortfarande bindande

Ordagrant ur planens § 7.5.

#### K3 · "Ritningen" (nytt koncept 1)

**Idé.** Alunix ritar innan de bygger. Sidan är en teknisk ritning av en webbplats på kallt ritpapper: en dimensionerad sektionsritning av en sida (konturer, måttlinjer, utrop med **sanna** värden: 320/768/1440, `7 rem`, `96 px`, `16:9`, priserna) som ritar sig själv när man scrollar, och sedan *blir* det den ritade: den riktiga Calyx-sidan tonar in **innanför den ritade konturen** (F-010-principen: innehållet maskas in i objektets verkliga öppning, bläcket ligger kvar som ram). Noll fotografier (Hyperborea-precedens). Aldrig en falsk UI-mock (gate 79): ritningen har inga låtsasknappar eller låtsastext, bara konturer, måttlinjer och utrop.

**Auktoritet:** ytan (papper + bläck; TASTE §1 rad 3); typen medelstor; bilder inga; i set-piece-akten rörelsen. **Register:** modern clean (ämnet är precision). **Grammatik:** chaptered editorial (titelsida utan media; folio; kolofon-liknande *specifikation* som avslut). **Palett:** ett kallt ritpapper (oklch ~0.95, hue 230, låg chroma; *inte* cream, AB09-lärdomen), ett bläck (mörk petrol/ultramarin), Alunix-blått `#1E5E9C` (Tier 1-bevis) som enda accent, bara på måttsiffrorna i displayskala. **Typ:** en grotesk med teknisk karaktär i två snitt + en mono som register (måtten). Arkitekten kör brand.md-proceduren; **förbjudna**: reflex-listan och alla snitt som använts i r1–r7 (Geist, Inter, JetBrains Mono, Public Sans, Familjen Grotesk, Literata, Fragment Mono, Hanken Grotesk, Instrument Serif, Archivo, IBM Plex Mono, Figtree, Cardo, PT Mono, Cinzel, Vollkorn, Italiana).

**Nav:** en ritad *teckenförklaring* (legend) i marginalen, sticky, som är sidans index (varje rad = ett kapitel, en linje dras till kapitlet när det är aktivt). **Hero-device:** ritningen ritar sig (SVG `stroke-dashoffset` från `--sc-ps`, pinnad akt span 2.4 = toppen), måttsiffrorna räknar upp till sina sanna värden (`count`, bara riktiga tal). **Aktform:** pin (ritningen) → kinetic lines (kapitelrubrik "Vi bygger ert varumärke.") → reveal ×3 (en plate per exempelsajt: konturen ritas, sedan tonar den riktiga sajten in innanför konturen, bläcket blir ram; iframe monteras lazy) → flow+in (liggaren 01–03) → count+flow (specifikationen: paketen som stycklista med de sanna priserna) → close. ≥ 5 familjer, aldrig samma två i rad. **Avslut:** specifikationsbladet (priser, `Alla har rätt till bra design.`, en mailto) inom en ritad ram vars linjer dras in sist; sidan slutar stilla. **Signaturrörelse:** *ritningen blir sidan*: konturen ritas, fylls med den levande sajten, bläcket stannar som ram. Tell-someone: "det är sajten där man ser hemsidan ritas som en ritning och sen blir den på riktigt".

**Referenser (förväntade ur `select.py`):** `caractere-bois` (hårlinje-ritningar över foton: "designat innan byggt"), `hyperborea` (ritat identitetssystem, noll foton), `wild` (pixelritad silhuett som banner), `garden-eight` (ett typografiskt + ett skulpturalt moment), `tidvatten` (modern clean, två sanna siffror som set-piece). Anti-referens: `before-ai-slop` (div-byggd låtsas-UI).

**Målbildsgrind:** (1) auktoritet ytan; viker: typ (medel), foto (inget), färg (en accent på måtten). (2) troplistan: inga kort, inga badges, inget glas, ingen gradient, ingen spotlight; **ritning ≠ falsk UI** kontrolleras mot gate 47/79 bild för bild. (3) ett displayelement per skärm: ritningen (s1), kapitelrubriken (s2), en plate i taget (s3–5), priserna (s6), mailto (s7). (4) fingerprint: mot Hyperborea (grammatik delad → nav legend ≠ sticky header+edition strip · hero ritning ≠ SVG-sol · aktform ≠ · avslut specifikation ≠ kolofon · signatur ≠ → 5/6); mot r1 K4 Journal, r2 R2/R3/R4, r4 M2 (alla chaptered): ≥4/6 på nav/hero/akt/signatur; arkitekten skriver ut alla 36 rader.

**Låsta referenser:** `squarespace` (primär), `insign`, `aevi-wellness`, `beautiful`,
`mode` (wildcard). Anti-referens att bygga bort: `sites/before-ai-slop.html`.

---

## 6. Invarianter i r8

1. **F-011, rörelsen spelar alltid.** Skriv aldrig `prefers-reduced-motion`, bygg aldrig ett
   reservläge, beskriv aldrig ett. `Skill(review-animations)` standard 8 gäller inte.
2. **F-014, `--sc-ps`.** Allt ögat ser förflytta sig läser `--sc-ps`. Rå `--sc-p` bara för
   cue-opacitet. Varje `--lN` är registrerad med `@property syntax: "<number>"`, annars
   stegar ritningen bana för bana. Motorn redigeras aldrig, `.sc-*` restylas aldrig,
   `sc-smooth.js` ligger kvar. `staircase = 0`, `max_step <= 3 %` på spelhuvudet `--sc-ps`
   (på härledda spår rapporteras talet men grindar inte, Q22 avgjord 2026-09-10), p95 <= 20 ms,
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
   Varje siffra på arket är ett verkligt mått eller pris.
8. **Fullständig output.** Trunkera aldrig. Måste du pausa: `[PAUSED — sektion X av Y]` som
   sista rad, fortsätt i nästa tur. Rapporterna i steg 1 till 5 skrivs ut i sin helhet, inte
   sammanfattade.

---

## 7. Leverans

- `{{UT_MAPP}}/index.html`, hela sidan, noll platshållare kvar.
- `{{UT_MAPP}}/shots/r3/` med alla breddar, `?preview=`-lägena och kontaktarket med fem
  folds.
- `{{UT_MAPP}}/NOTES.md` § R3, i denna ordning: Before/After/Why-tabellen, copy-gatens fem
  pass med vad varje pass ändrade, `review-animations`-rapporten, a11y-rapporten med
  körningarna mot både din URL och `tests/a11y/broken.html`, probe-utfallen
  (`preflight_taste`, `perf_probe` vid 1440 och 390, `detect.mjs`) med namngivna undantag
  där något inte är grönt, och den uppdaterade rollistan över varje ritad `<rect>` och
  `<path>`.
