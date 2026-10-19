# Alunix r8, runda 3. Cell {{KONCEPT}}. Hela sidan.

Samma session, samma cell. Nu fyller du **alla** sektioner enligt `{{UT_MAPP}}/BRIEF.md` och
tar bort varje `<!-- R3 -->`-platshållare. Sedan kör du de fem stegen nedan i **din egen
session**, i den här ordningen, **namngivna i transkriptet**. Att de körs hos dig och inte
bara hos lead är hela poängen med rundan: det är luckan r7 lämnade och r8 stänger.

Signaturakten från R2 rörs bara om ett steg nedan hittar ett fel i den. Ordagrann
Alunix-copy rörs aldrig.

---

## 1. Sidan färdig

Nio skärmar enligt BRIEF.md § direction contract, i aktordningen: pin (delaren tippar, s1
till s3) → reveal per sida (skillnadsliggaren, s4: varje tal wipeas in från sin egen halva
mot hårlinjen) → flow och in (Hōrai och Hyperborea som full-bleed objekt, s5 och s6, ett i
taget, tillåtet först **efter** upplösningen) → kinetic lines (tjänsterna 01–03, s7) → count
(paketen, s8: `26 900` och `38 900` räknar, `Pris vid förfrågan` skrivs och räknar inte) →
reveal (avslutet, s9). Minst fem device-familjer, aldrig samma två i rad. Noll `pan`, noll
`drift`, noll `spotlight`, noll `magnet`, noll `scrub`: split stage förbjuder alla fem.

Ingen navbar. Delaren är chromen, och `kontakt@alunix.se` står som text i övre högra hörnet
av "efter"-halvan. Avslutet kollapsar till en kolumn.

**Skillnadsliggaren får bara innehålla tal som faktiskt är mätta ur de två filerna**, med
kommandot utskrivet i NOTES.md. Talen står i `{{UT_MAPP}}/BRIEF.md` § Skillnadsliggaren och
i `tests/alunix-r8/concepts-K4.md` § Mätning, ordagrant. Hittar du på ett tal faller cellen
på sitt eget argument.

Kirurgiska `Edit`-anrop, en sektion i taget.

---

## 2. De fem stegen, i din egen session, namngivna i transkriptet

**Steg 1. `Skill(emil-design-eng)`.**
En Before/After/Why-tabell för **varje** övergång och varje rörelse på sidan, inte bara för
signaturakten. Sedan slow-motion-granskning av signaturakten: DevTools 10 %-hastighet
motsvaras här av `motion_probe.py --wheel 20:120`. Läs sparklinen som bild. Granska särskilt
pekarhandoffen: fjäderns damping 1.0, avbrytbarheten, velocity-överlämningen och att delaren
aldrig snäpper till 50 %. Skriv tabellen i NOTES.md.

**Steg 2. Copy-gaten, fem pass, vart och ett namngivet i transkriptet.**
Gäller **bara nya strängar**: kickerna `Före` och `Efter`, skillnadsliggarens sex
radetiketter, bildtexterna, tjänsternas tre underrader och etiketten `En typisk mallsida`.
Ordagrann copy ur § 4 nedan rörs inte, inte ett tecken.

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
Etiketten på vänsterhalvan är ärlig och neutral: `En typisk mallsida`, aldrig ett skämt,
aldrig ett omdöme, aldrig ett kundnamn.

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
Obligatoriska fynd att adressera: `title` på **båda** `<iframe>`, fyra landmärken, sticky
chrome vid 200 % zoom, överlevnad i forced-colors, kontrast per grund
(`contrast_over_media.py --url`), och **delaren som kontroll**: den är dragbar, alltså
behöver den en tangentbordsväg och ett tillgängligt namn och värde. `tab_walk.py` scrollar
inte: läs `rect.top` och räkna inte offscreen-element som dolda. `reflow.py` punkt (c) är ett
mått på oavslöjat innehåll, inte på reducerad rörelse.

**Steg 5. Den mekaniska grinden.**

```
python ~/.claude/skills/design/scripts/preflight_taste.py {{UT_MAPP}}/index.html --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html
python ~/.claude/skills/design/scripts/perf_probe.py --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --cpu 4
node ~/.agents/skills/impeccable/scripts/detect.mjs --json {{UT_MAPP}}/index.html
```

Alla gröna, eller namngivna undantag i NOTES.md med skäl och källa. `perf_probe` körs vid
både 1440 och 390. Skriv in den faktiska överföringen med båda ramarna monterade. Överstiger
den 2,5 MB: degradera **vänsterramen** till en skärmbild och behåll högerramen live, aldrig
tvärtom, och skriv en rad i decision ledger. Mät också bildtid p95 med och utan
`saturate()`-filtret vid 4× CPU och skriv båda talen; skiljer de sig mer än 3 ms byts filtret
mot en opak varm övertoning i `--paper` med stigande `opacity`.

---

## 3. Skärmbilder

Vid **320, 375, 414, 768 och 1440**, plus `?preview=before`, `?preview=split`,
`?preview=after` och `?preview=mid`. **Läs varje bild själv, som pixlar.** Dessutom **fem
folds vid 1440 som kontaktark**. Allt i `{{UT_MAPP}}/shots/r3/`.

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
oförändrat. K4 har noll egna fotografier och noll genererat material.

---

## 5. Målbilden för {{KONCEPT}}, fortfarande bindande

Ordagrant ur planens § 7.5.

#### K4 · "Före/Efter" (nytt koncept 2)

**Idé.** Alunix argument är tvåsidigt: sidan ni har mot sidan ni kunde ha. Split stage: vänster halva = **en typisk mallsida** (kedjans egen `sites/before-ai-slop.html`, live, ärligt etiketterad `En typisk mallsida`; aldrig en påhittad kund), höger halva = Calyx live. Delaren *är* sidans chrome (grammatikens egen form). Scrollen tippar balansen: delaren går från 50 % till 100 % höger över en pinnad akt medan vänstersidan tappar mättnad, skärpa och typvikt; vid p = 1 fyller "efter" bilden och avslutet kollapsar till en kolumn.

**Auktoritet:** produkten (de två sajterna som objekt; TASTE §1 rad 4): typen nästan tyst (kickers `Före` / `Efter`, två av ≤ 4 monoetiketter; rubriken `Er hemsida är nutidens visitkort` i lässtorlek+ tvärs över delaren, tvåtons: dämpad över "före", bläck över "efter", paper.design-principen), ytan flat. **Register:** modern clean. **Grammatik:** split stage (förbjuder full-bleed *före* upplösningen, centrerad copy, symmetriskt avslut). **Palett:** ett papper (varmvitt eller kallt, arkitekten väljer mot K3 så att de två nya cellerna inte delar temperatur), ett bläck, Alunix-blått som enda accent **bara på delaren**. **Typ:** en grotesk (ej använd förut, ej på reflex-listan) + mono som register.

**Nav:** ingen bar; delaren är chromen; `kontakt@alunix.se` som text i övre högra hörnet av "efter"-halvan. **Hero-device:** två levande sajter i 50/50 split under en enradig tvåtons-rubrik. **Aktform:** pin (balansen tippar, span 2.4, toppen) → reveal per sida (skillnaderna: en liggare med **sanna, mätta** skillnader mellan de två filerna — `measure.py`-utfall: antal accentfärger, kort med skugga, displaykontrast ×, hairlines, riktiga foton: data som textur med sanna tal, TASTE §4.9) → efter upplösningen: Hōrai och Hyperborea som full-bleed objekt i tur och ordning (tillåtet efter kollapsen) → flow (liggaren 01–03) → flow (paketen) → close. **Avslut:** kollapsen till en kolumn: "efter"-sidan fyller, rubriken `Alla har rätt till bra design.` i displayskala, mailto. **Signaturrörelse:** delaren är scrollstyrd **och** dragbar med pekaren (fin pekare: `cursor: col-resize`; apple-design: avbrytbar, presentationsvärde, velocity-handoff, spring damping 1.0), och "före"-sidans typ *degraderas* av delaren (letter-spacing lossnar, vikt tunnas, mättnad faller) i takt med `--sc-ps`. Ingen handtagsknopp, ingen ikon, ingen "dra"-text (gate 88). Tell-someone: "det är sajten där den dåliga hemsidan bokstavligen trycks ut ur bild av den bra".

**Referenser (förväntade):** `paper` (tvåtons-rubrik), `dovetail` (split, noll accent, hårlinjer), `future-fur` (två-upp split med ordmärke tvärs över), `harkcap` (hover-reveal), `mode` (bara tvåspaltsrytmen; korten avvisas). Anti-referens: `before-ai-slop` som *innehåll* på vänstersidan är avsiktligt och etiketterat.

**Målbildsgrind:** (1) auktoritet produkten; viker: typ (tyst), färg (accent bara på delaren), foto (inga egna). (2) troplistan: inga kort/badges/glas/spotlight; **jämförelseslider-klichén** neutraliseras av att delaren är sidans enda linje, inget handtag, och att "före" är ärligt märkt. (3) ett displayelement per skärm: de två sajterna (s1), skillnadsliggaren (s2), Hōrai (s3), Hyperborea (s4), priserna (s5), slutrubriken (s6). (4) fingerprint mot r1 K2 Tjänsteledger och r2 R5 (split stage): nav delare ≠ sticky rail/konsolram · hero två live-sajter ≠ grotesk-fråga/ordmärke i ram · aktform ≠ · avslut kollaps ≠ · signatur ≠ → ≥4/6; mot Tidvatten (två tal som möts): annan mekanism och grammatik; alla 36 rader skrivs ut.

**Låsta referenser:** `paper` (primär), `gocanopy`, `harkcap`, `mode`, `customer-io`
(wildcard). `sites/before-ai-slop.html` är **innehåll** i vänsterhalvan, inte en
anti-referens att undvika.

---

## 6. Invarianter i r8

1. **F-011, rörelsen spelar alltid.** Skriv aldrig `prefers-reduced-motion`, bygg aldrig ett
   reservläge, beskriv aldrig ett. `Skill(review-animations)` standard 8 gäller inte.
2. **F-014, `--sc-ps`.** Allt ögat ser förflytta sig läser `--sc-ps` via `--split`, som är
   ett registrerat `<number>`. Rå `--sc-p` bara för cue-opacitet. Motorn redigeras aldrig,
   `.sc-*` restylas aldrig, `sc-smooth.js` ligger kvar. `staircase = 0`, `max_step <= 3 %`
   på spelhuvudet `--sc-ps` (på härledda spår rapporteras talet men grindar inte, Q22 avgjord
   2026-09-10), p95 <= 20 ms, noll frames > 33 ms, båda riktningarna. Spåra aldrig rått `--sc-p`.
3. **UI-filer författas bara med `Write` eller `Edit`.** `design-gate.py` nekar `cat >`,
   heredoc, `tee`, `sed -i`, `Set-Content`/`Out-File` och inline-skript i en armad session;
   nekandet syns i ledgern som `gate-deny` med signalen `shell-write`. Kopiering med `cp`
   eller `Copy-Item` är tillåten.
4. **Servern** är `serve.py` på `{{PORT}}` från repo-roten, aldrig `http.server`.
5. **Ingen generering.** Higgsfield är spärrat på din argv och har 0 krediter (free plan,
   mätt av lead 2026-09-09). Saknas material: `[needs asset: ...]` i NOTES.md och vidare.
6. **Noll tankstreck i synlig text.** Ordagrann copy ändras aldrig. Tesrubriken är versal.
7. **Inga kort, badges, glas, spotlights.** Inga påhittade fakta (`PRODUCT.md` § absences).
   Accenten `#1E5E9C` finns bara på delaren.
8. **Vänsterhalvan är ärlig, inte en karikatyr.** Den skakas inte, faller inte isär, får inga
   glidande element och beskrivs aldrig som en verklig kund. Sidans enda kritik är mätta tal.
9. **Fullständig output.** Trunkera aldrig. Måste du pausa: `[PAUSED — sektion X av Y]` som
   sista rad, fortsätt i nästa tur. Rapporterna i steg 1 till 5 skrivs ut i sin helhet, inte
   sammanfattade.

---

## 7. Leverans

- `{{UT_MAPP}}/index.html`, hela sidan, noll platshållare kvar.
- `{{UT_MAPP}}/shots/r3/` med alla breddar, `?preview=`-lägena och kontaktarket med fem
  folds.
- `{{UT_MAPP}}/NOTES.md` § R3, i denna ordning: Before/After/Why-tabellen inklusive
  pekarhandoffen, copy-gatens fem pass med vad varje pass ändrade,
  `review-animations`-rapporten, a11y-rapporten med körningarna mot både din URL och
  `tests/a11y/broken.html`, och probe-utfallen (`preflight_taste`, `perf_probe` vid 1440 och
  390 med den faktiska överföringen, `detect.mjs`, samt frame p95 med och utan filtret) med
  namngivna undantag där något inte är grönt.
