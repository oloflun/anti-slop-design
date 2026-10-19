# Alunix r8, runda 2. Cell {{KONCEPT}}. Folden och signaturakten.

Samma session, samma cell. Nu bygger du `{{UT_MAPP}}/index.html` med **folden och
signaturakten kompletta**. Resten av sidan får vara markerade platshållarsektioner:
`<!-- R3 -->` med rätt höjd och rätt grund, **inga låtsaselement**, ingen lorem, inga tomma
ramar som ska "bli något sedan".

Underlaget är `{{UT_MAPP}}/BRIEF.md`, som du skrev i R1, och
`tests/alunix-r8/concepts-K4.md`. Där de säger emot varandra gäller målbilden i § 3 nedan,
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

**Delaren tippar.**

- Den pinnade akten: `data-sc-act="pin" data-sc-span="2.4" data-sc-dwell="0.22"`,
  cue `0 1 0 0`. Båda sajterna och rubriken är stagens **ground**, synliga från ps = 0.
  Ingen scroll-cue-text (gate 88).
- **Delaren går från 50 % till 100 % höger över akten, driven av `--sc-ps`.** Vid ps = 0
  står den mitt i ramen och de två sajterna delar bilden 50/50; vid ps = 1 fyller
  "efter"-ytan (Calyx) hela bilden. Talet som gör det heter `--split` i BRIEF.md § `?preview=`
  och räknas som delarens position i ramen: `--split: 50%` är folden, `--split: 0%` är det
  upplösta läget, `--split: 100%` är mallsidan i helbild. Samma rörelse, en enda konvention:
  **följ BRIEF.md:s teckenkonvention och skriv ut den i NOTES.md**, så att lead och arkitekt
  läser samma tal.
- `--split` beräknas ur `--sc-ps` plus pekarens offset och **publiceras som ett registrerat
  `<number>`** (`@property … syntax: "<number>"`) av samma slag som `sc-smooth.js`
  publicerar `--sc-ps`, så att CSS kan interpolera det. Ett osparsat tal stegar.
- **Dragbar med pekaren, på fin pekare:** `cursor: col-resize` under
  `@media (pointer: fine)`. Träffytan är 44 px bred och osynlig. Ingen handtagsknopp, ingen
  ikon, ingen "dra"-text (gate 88).
  - `pointerdown` tar över värdet direkt och 1:1, `pointermove` skriver det.
  - `pointerup` lämnar tillbaka det till scrollens värde genom en **kritiskt dämpad fjäder,
    damping 1.0**, seedad med pekarens hastighet vid släppet (**velocity-handoff**).
  - Rörelsen är **avbrytbar**: ett nytt `pointerdown` mitt i återgången tar vid i det läge
    och den hastighet fjädern hade. Den nollställer inte och den hoppar inte.
  - Det som målas är alltid fjäderns **utvärde**, aldrig pekarens råa x
    (`apple-design` § presentationsvärde).
  - Delaren snäpper aldrig tillbaka till 50 %. Släppet lämnas vidare till det värde scrollen
    äger.
- Längs samma tal degraderas "före"-halvan: rubrikhalvans `font-variation-settings`
  (`wght` 500 mot 200) och `letter-spacing` öppnar, och mallsidewrapperns `saturate()`
  faller. Allt tre läser `--sc-ps` via `--split`, aldrig rå `--sc-p`.
- Rubriken `Er hemsida är nutidens visitkort` är **en rad** tvärs över sömmen, tvåtons:
  `--ink-2` över "före", `--ink` över "efter". Den byter aldrig grad, aldrig snitt, aldrig
  radbrytning under akten.
- `will-change` sätts bara på delaren och på mallsidewrappern medan `0 < ps < 1`, aldrig i
  vila.
- Vänsterhalvan är `sites/before-ai-slop.html` **live i en `<iframe>`**, etiketterad
  `En typisk mallsida`. Högerhalvan är `sites/calyx.html` live. Ingen av dem karikeras,
  skakas eller faller isär.
- De första 0,10 av akten är författad tystnad: båda sajterna står helt stilla medan
  besökaren läser rubriken. Det ska stå i BRIEF.md så att `scroll_verify.py`:s `blankBands`
  inte larmar falskt.

**`?preview=`-lägen** (enligt BRIEF.md § `?preview=`-plan; alla fyra är obligatoriska):

| Läge | Tvingar |
|---|---|
| `?preview=before` | `--split: 100%`, delaren vid högerkanten, mallsidan fyller ramen |
| `?preview=split` | `--split: 50%`, baslinjen för folden, exakt 50/50 |
| **`?preview=after`** | **`--split: 0%`, det upplösta läget: "efter"-sidan fyller bilden.** Utan det kan F-007-kontrollen av skärm s3 inte köras |
| `?preview=mid` | `--split: 25%`, mitt i degraderingen; kontrollen att före-halvan tunnas och ändå är läsbar |

---

## 3. Målbilden för {{KONCEPT}}, bindande

Ordagrant ur planens § 7.5.

#### K4 · "Före/Efter" (nytt koncept 2)

**Idé.** Alunix argument är tvåsidigt: sidan ni har mot sidan ni kunde ha. Split stage: vänster halva = **en typisk mallsida** (kedjans egen `sites/before-ai-slop.html`, live, ärligt etiketterad `En typisk mallsida`; aldrig en påhittad kund), höger halva = Calyx live. Delaren *är* sidans chrome (grammatikens egen form). Scrollen tippar balansen: delaren går från 50 % till 100 % höger över en pinnad akt medan vänstersidan tappar mättnad, skärpa och typvikt; vid p = 1 fyller "efter" bilden och avslutet kollapsar till en kolumn.

**Auktoritet:** produkten (de två sajterna som objekt; TASTE §1 rad 4): typen nästan tyst (kickers `Före` / `Efter`, två av ≤ 4 monoetiketter; rubriken `Er hemsida är nutidens visitkort` i lässtorlek+ tvärs över delaren, tvåtons: dämpad över "före", bläck över "efter", paper.design-principen), ytan flat. **Register:** modern clean. **Grammatik:** split stage (förbjuder full-bleed *före* upplösningen, centrerad copy, symmetriskt avslut). **Palett:** ett papper (varmvitt eller kallt, arkitekten väljer mot K3 så att de två nya cellerna inte delar temperatur), ett bläck, Alunix-blått som enda accent **bara på delaren**. **Typ:** en grotesk (ej använd förut, ej på reflex-listan) + mono som register.

**Nav:** ingen bar; delaren är chromen; `kontakt@alunix.se` som text i övre högra hörnet av "efter"-halvan. **Hero-device:** två levande sajter i 50/50 split under en enradig tvåtons-rubrik. **Aktform:** pin (balansen tippar, span 2.4, toppen) → reveal per sida (skillnaderna: en liggare med **sanna, mätta** skillnader mellan de två filerna — `measure.py`-utfall: antal accentfärger, kort med skugga, displaykontrast ×, hairlines, riktiga foton: data som textur med sanna tal, TASTE §4.9) → efter upplösningen: Hōrai och Hyperborea som full-bleed objekt i tur och ordning (tillåtet efter kollapsen) → flow (liggaren 01–03) → flow (paketen) → close. **Avslut:** kollapsen till en kolumn: "efter"-sidan fyller, rubriken `Alla har rätt till bra design.` i displayskala, mailto. **Signaturrörelse:** delaren är scrollstyrd **och** dragbar med pekaren (fin pekare: `cursor: col-resize`; apple-design: avbrytbar, presentationsvärde, velocity-handoff, spring damping 1.0), och "före"-sidans typ *degraderas* av delaren (letter-spacing lossnar, vikt tunnas, mättnad faller) i takt med `--sc-ps`. Ingen handtagsknopp, ingen ikon, ingen "dra"-text (gate 88). Tell-someone: "det är sajten där den dåliga hemsidan bokstavligen trycks ut ur bild av den bra".

**Referenser (förväntade):** `paper` (tvåtons-rubrik), `dovetail` (split, noll accent, hårlinjer), `future-fur` (två-upp split med ordmärke tvärs över), `harkcap` (hover-reveal), `mode` (bara tvåspaltsrytmen; korten avvisas). Anti-referens: `before-ai-slop` som *innehåll* på vänstersidan är avsiktligt och etiketterat.

**Målbildsgrind:** (1) auktoritet produkten; viker: typ (tyst), färg (accent bara på delaren), foto (inga egna). (2) troplistan: inga kort/badges/glas/spotlight; **jämförelseslider-klichén** neutraliseras av att delaren är sidans enda linje, inget handtag, och att "före" är ärligt märkt. (3) ett displayelement per skärm: de två sajterna (s1), skillnadsliggaren (s2), Hōrai (s3), Hyperborea (s4), priserna (s5), slutrubriken (s6). (4) fingerprint mot r1 K2 Tjänsteledger och r2 R5 (split stage): nav delare ≠ sticky rail/konsolram · hero två live-sajter ≠ grotesk-fråga/ordmärke i ram · aktform ≠ · avslut kollaps ≠ · signatur ≠ → ≥4/6; mot Tidvatten (två tal som möts): annan mekanism och grammatik; alla 36 rader skrivs ut.

**Låsta referenser** (ur `select.py`, samma rad som i R1): `paper` (primär), `gocanopy`,
`harkcap`, `mode`, `customer-io` (wildcard). `sites/before-ai-slop.html` är **innehåll** i
vänsterhalvan, inte en anti-referens att undvika.

---

## 4. Prestanda från första raden, inte som en efterhandsstädning

- `width` och `height` samt `decoding="async"` på **varje** `<img>`; båda `<iframe>` får
  `width` och `height` så att inget lager hoppar.
- `fetchpriority="high"` på LCP-elementets bild om folden har en.
- `<link rel="preload">` för displaysnittet och för monon; två variabla `.woff2`, tak 300 kB.
- **Vänsterramen** (`before-ai-slop.html`, liten och utan externa resurser) monteras eagerly,
  eftersom den är folden. **Högerramen** (`calyx.html`, med externa bilder) monteras via
  IntersectionObserver med `loading="lazy"`. Ramarna transformeras eller tonas aldrig efter
  att de visats; `saturate()` ligger på **wrappern**, inte på ramen, och det är sidans enda
  `filter`.
- `min-height: 100dvh`, aldrig `100vh`.
- Ingen `transition: all`. Ingen permanent `will-change`. Noll `box-shadow`, noll
  `backdrop-filter`, noll gradient, radie 0 i K4:s eget lager.
- Budgeten står i `~/.claude/skills/design/references/performance.md` § 1 och i BRIEF.md
  § Prestandaplan. Överstiger den mätta överföringen 2,5 MB: degradera **vänsterramen** till
  en skärmbild och behåll högerramen live, aldrig tvärtom.

---

## 5. Kör verifieringen själv innan du lämnar rundan

Från repo-roten, i din egen session:

```
python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .

python ~/.claude/skills/design/scripts/scroll_verify.py \
  --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html --out {{UT_MAPP}}/shots/r2

python ~/.claude/skills/design/scripts/motion_probe.py \
  --url http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html \
  --track "section.split:--sc-p,section.split:--sc-ps,.divider:transform" \
  --cpu 4 --out {{UT_MAPP}}/shots/r2
```

Byt ut selektorerna mot dina faktiska namn, men `--track` måste innehålla aktens `--sc-p`,
aktens `--sc-ps` och **delarens** `transform`. Spåra dessutom `--split` i en andra körning,
så att du ser att det registrerade talet interpoleras och inte hoppar. Kör `motion_probe`
med både `--wheel 100:60` och `--wheel 20:120`.

**Läs kontaktarket och sparklinen som bilder**, inte som filnamn. `staircase` **måste vara
0** innan du lämnar rundan, och `max_step <= 3 %`, bildtid p95 <= 20 ms, noll frames
> 33 ms. Är den inte det: rätta rörelsen och mät om.

**Pekarhandoffen mäts också**, eftersom `motion_probe` bara driver hjulet: dra delaren,
släpp, och kontrollera i din egen körning att återgången är kontinuerlig, att ett nytt grepp
mitt i återgången tar vid utan hopp, och att den aldrig snäpper till 50 %. Skriv utfallet i
NOTES.md.

Skärmbilder: 1440 och 390, plus vart och ett av de fyra `?preview=`-lägena. Läs varje bild
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
oförändrat. K4 har noll egna fotografier och noll genererat material.

---

## 7. Invarianter i r8

1. **F-011, rörelsen spelar alltid.** Skriv aldrig `prefers-reduced-motion`, bygg aldrig ett
   reservläge, beskriv aldrig ett. Frånvaron är beslutad (FEEDBACK.md F-011) och ingen
   granskare i r8 flaggar den.
2. **F-014, `--sc-ps`.** Allt ögat ser förflytta sig läser `--sc-ps`: clip-gränsen, delarens
   `translateX`, rubrikhalvans vikt och tracking, wrapperns `saturate()`. Rå `--sc-p` får
   bara driva cue-opacitet. `sc-smooth.js` kopieras in bredvid motorn; motorn redigeras
   aldrig, `.sc-*` restylas aldrig. Akten är inte klar förrän `staircase = 0`,
   `max_step <= 3 %`, p95 <= 20 ms och noll frames > 33 ms.
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
   (`PRODUCT.md` § absences). Accenten `#1E5E9C` finns bara på delaren.
8. **Vänsterhalvan är ärlig, inte en karikatyr.** Etiketten är `En typisk mallsida`. Sidans
   enda kritik är mätta tal.
9. **Fullständig output.** Trunkera aldrig. Måste du pausa: `[PAUSED — sektion X av Y]` som
   sista rad, fortsätt i nästa tur.

---

## 8. Leverans

- `{{UT_MAPP}}/index.html` med folden och signaturakten kompletta, resten som markerade
  `<!-- R3 -->`-platshållare med rätt höjd och grund.
- `{{UT_MAPP}}/scroll/` med motorn och `sc-smooth.js`, oförändrade.
- `{{UT_MAPP}}/shots/r2/` med skärmbilder, kontaktark och sparklines.
- `{{UT_MAPP}}/NOTES.md` § R2: vad som avviker från målbilden och varför, med källa;
  `--split`-konventionen utskriven; de mätta talen ur `motion_probe` för båda
  hjulhastigheterna och båda riktningarna; utfallet av pekarhandoffen (avbrytbarhet,
  velocity, ingen snäpp till 50 %); vad du läste i kontaktarket och sparklinen.


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
