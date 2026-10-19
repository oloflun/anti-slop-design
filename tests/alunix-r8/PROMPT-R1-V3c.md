# Alunix r8, runda 1 av flera. Cell {{KONCEPT}}. Referenspaket, ingen HTML.

Du bygger, i flera rundor och i samma session, en färdig scrollkoreograferad landningssida i
ren HTML/CSS/JS för Alunix, en svensk webbyrå. Ett lead läser din leverans mellan varje runda
och skickar nästa rundas instruktion hit.

**I den här rundan skriver du ingen HTML, ingen CSS, ingen JS.** Leveransen är
`{{UT_MAPP}}/BRIEF.md`. Skelettet ligger redan där, skrivet av arkitekten: du fyller varje
fält som är märkt `[fylls i R1]` och rör inget annat i filen. Skriv bara under `{{UT_MAPP}}`.
Ingen commit.

**Första verktygsanropet i den här sessionen är `Skill(design)`. Inget annat före det.**
Kedjans hook nekar din första UI-skrivning i runda 2 tills referensgolvet nedan är läst i
den här sessionen. Det är avsiktligt och det går inte runt.

---

## 1. Kör katalogurvalet själv, innan du läser något annat

Kör detta i din egen session, som ditt andra verktygsanrop, från repo-roten:

```
python scripts/catalogue/select.py --brief {{UT_MAPP}}/BRIEF.md --k 4 --wildcard --explain
```

**Skälet, så att du inte hoppar över det:** `design-gate.py`:s referensgolv kräver en
`catalogue-select`-rad i **din egen** sessionsledger innan din första UI-skrivning i R2, och
golvet läser sedan varje vald slug och kräver `entry.md` + `fold.webp` + eventuell
`extract/*-design-language.md` per slug. Arkitektens körning ligger i en annan session och
räknas inte för dig. Skriptet är deterministiskt, så du ska få samma rad som arkitekten.

**Arkitektens låsta rad för {{KONCEPT}}:**

```
catalogue-select: oryzo-ai, dope-security, mattis-studio, monologue, planhat
```

Topprankad post (14 poäng): **`oryzo-ai`**. Övriga låsta: **`mattis-studio`**,
**`dope-security`**, **`monologue`**, och wildcard **`planhat`** (utanför kategorin).

Två saker gäller samtidigt och båda står i `{{UT_MAPP}}`-cellens `concepts-V3c.md`:
katalogens primära post är `oryzo-ai`, men enligt `reference-lock.md` Tier 0
("Primary = the locked system itself") är **primär riktning V3b själv**,
`tests/alunix-concepts-r5/cells/V3b-chain/index.html`. V3c är en iteration av den cellen,
inte ett nytt bygge. `garden-eight` och `squarespace` behåller sina rader som ribbor i
"Vad jag måste slå" med källan utskriven (planens § 7.5), men de är inte låsta referenser.

**Avviker ditt resultat från raden ovan:** rapportera avvikelsen i BRIEF.md, ordagrant, med
skriptets hela utdata, och **följ sedan arkitektens rad**. Du byter aldrig referenser på egen
hand.

---

## 2. Referensgolvet du läser innan du skriver en rad i BRIEF.md

Läs med `Read`, aldrig med `cat`. Bilder läses som **pixlar**, inte som filnamn.

**Smak och återkoppling**
- `design-catalogue/TASTE.md`, hela.
- `design-catalogue/FEEDBACK.md`, **alla poster**. F-006 (glas), F-007 (målbild bild för
  bild), F-009 (orkestreraren äger assets), F-010 (fönstret i fasaden), F-011 (rörelse
  alltid), F-012 och F-014 (hackig rörelse, `--sc-ps`) är de som styr den här cellen.

**Varje vald katalogpost**, under `design-catalogue/entries/<slug>/`
(`oryzo-ai`, `mattis-studio`, `dope-security`, `monologue`, `planhat`):
`entry.md` hela inklusive § Motion och § Reference lock, `extract/*-design-language.md`,
`fold.webp` och alla `slices/*.webp` **som bilder**. Tre rader digest per fil i
BRIEF.md § Lästa referenser: vad den gör, vad du tar, vad du lämnar.

**Kedjans referenser**, under `~/.claude/skills/design/references/`:
`reference-lock.md`, `scroll/devices.md`, `scroll/feel-and-fingerprint.md`, `scroll/pace.md`,
`motion-smoothness.md`, `performance.md`, `lift.md`.

**Registret:** `wiki/projects/_index/design-fingerprints.md`, alla rader.

**Cellens eget underlag:** `tests/alunix-r8/PRODUCT.md` (beviskassan och § absences),
`tests/alunix-r8/concepts-V3c.md` (arkitektens målbildsgrind, hela),
`{{UT_MAPP}}/BRIEF.md` (skelettet du fyller), `{{UT_MAPP}}/assets/ASSETS.md` och
`credits.json`.

**Föregående cell, som utgångspunkt och inte som mall:**
`tests/alunix-concepts-r5/cells/V3b-chain/index.html`, hela. V3c ärver dess värld.

**De fem live-rubrikerna i kategorin** hämtar du själv med webbsök på
`digital byrå webbdesign Sverige`, tar de fem bästa träffarna, citerar varje `H1`
**ordagrant** med källdomän, och skriver in dem i BRIEF.md § Fem live-rubriker.
**Fabricera aldrig en rubrik.** Går sökningen inte att köra: skriv `[needs: live-rubriker]`
och gå vidare.

---

## 3. Målbilden för {{KONCEPT}}, bindande

Ordagrant ur planens § 7.5. Varje avvikelse kräver en rad i BRIEF.md § decision ledger med
källa. Text mellan bakåtcitattecken är kod eller ordagrann copy.

#### V3c · Plåt i grunden · kortet vänds

*Iteration av V3b, inte nytt bygge: registrets V3-rad uppdateras till V3c; fingerprint-gaten (≥4/6) gäller K3/K4, inte V3c.* Grundkonceptet och estetiken är låsta: kontinuerlig svartvit grund (`k4-cabin-desk.webp`), R5-världen vänster (Geist, `#0b0c0e`/`#1e5e9c`), R6-världen höger (Public Sans, `#fdfbf4`), rubriken utanför platen i affischskala, Hyperborea-platen som bleeder, ordscrubben i liggaren, Calyx/Hōrai live.

**Heron blir en pinnad akt.** `section.hero` får `data-sc-act="pin" data-sc-span="2.2" data-sc-dwell="0.35"` (var `flow`), med motorns stage-markup från `template.html` (aldrig restylade `.sc-*`-klasser, AB06). Rubriken, platen och underraden är stagens *ground* (synliga från p = 0; "ground or greet" uppfyllt utan cue). Ingen scroll-cue-text (gate 88).

**Kortet.** `figure.hero-plate` (samma storlek: `width:min(100% − 2·rail, 56vh·16/9)`, 16:9, vänsteranknuten vid `--rail-x`) får `perspective: 1600px`. Inuti: `.plate-card{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateY(calc(var(--flip,0) * -180deg))}` med två `.face` (`backface-visibility:hidden`, hairline `--frame-line`). **Framsidan** = dagens innehåll (logo-dock + `#heroPoolImg`; ljuspölen vandrar vidare, nu på `--sc-ps`). **Baksidan** (`transform:rotateY(180deg)`, `background:var(--c-black)`): `ALUNIX` i Geist 700, `clamp(3.2rem, 9cqw, 7.5rem)`, `line-height:.9`, uppercase (displayskala ≥ 5× body, TASTE §2.4); under: `Digital byrå` som kicker (Geist Mono 10.5 px, .22 em; en av sidans ≤ 4 monoetiketter); hairline; raden `Design  Utveckling  System` i samma monoregister (samma ordning som liggaren 01–03, så att de två listorna inte motsäger varandra; **öppen fråga till Anton**: hans meddelande listade "utveckling, design, system", är ordningen avsiktlig?); `Boka ett möte →` som typsatt länk (Geist 700, understruken i accent). **Ingen tidsstämpel, ingen `2026 · SVERIGE`, ingen lede** (underraden under platen bär redan leden; två leder i folden vore dubbelt).

**Koreografin på `--sc-ps`** (aldrig rå `--sc-p`): `flip = smoothstep(0.12, 0.72, ps)` i sidans JS (skrivs som `--flip` på `.plate-card`); p 0–0,12 stilla, ljuspölen vandrar; 0,12–0,72 vändningen (Y-axeln, som ett visitkort man vänder med handen; vid 90° syns bara hairlinen, det är ärligt); 0,72–1 baksidan i vila, dwell låter den landa. `will-change:transform` sätts på `.plate-card` bara medan `0 < ps < 1` och tas bort i vila. Båda riktningarna. `?preview=back` tvingar `--flip:1`. Rubriken står kvar hela tiden (stagens ground); underraden också.

**Under heron.** `section.panel-open` (svarta konsolkortet) **tas bort**; dess innehåll bor nu på kortets baksida. `section.panel-services` (Tjänster, tre lika kolumner 01–03) **tas bort** som dubblett av liggaren (och gate 3-familj). Ny kolumnfördelning, materialväxling i båda spalterna (TASTE §4.5): **vänster** = blå tes (Hyperborea-bleed) → Calyx (ljus iframe) → **pris** (mörk); **höger** = jätterubrik + liggare (papper) → Hōrai (mörk iframe). `calyx-wrap` behåller `flex:1`. Arkitekten läser kolumnvikten som pixlar (squint: ingen kolumn får bära mindre vikt än sin bredd) och får flytta priset tillbaka till höger om vänster blir för tung.

**Lyftet i V3c (utan att ändra konceptet):** allt bespoke (`paintMotion`, `paintHeroPool`, ordscrubben) läser `--sc-ps`; `.giant`:s permanenta `will-change` bort; preload av Geist 700 + Public Sans 300; `decoding="async"` + `fetchpriority="high"` på hero-bilden; `loading="lazy"` + IO-montering på iframes; `content-visibility:auto` på `.price`/`.horai-wrap`; `text-wrap: balance` på rubriker; hover/focus på de tre länkarna (`:focus-visible` 2 px offset ≥ 3:1 mot båda grunderna); hairlinerna på `--rail-x`-rastret; 320/375/414/768 verifierade (kortet blir 4:5 under 640 px som idag och vänds fortfarande); copy-gaten bara på de ändrade strängarna (ordagrann copy bevaras).

**Vad referenserna gör som V3c måste slå** (låses via `select.py`; förväntat: `garden-eight`, `mattis-studio`, `squarespace`, ev. `creative-giants`): Garden Eight: *ett typografiskt moment, ett skulpturalt moment, åtskilda av tystnad* → V3c:s hero får bara rubrik + kort + en rad, inget mer. Mattis: konsolkortet med hörnmarkeringar är platt → V3c:s kort är ett *fysiskt* kort som vänds. Squarespace: svarta/vita band med ett statistikblock → V3c:s inversioner ska vara lika rena, utan kort.

*(Slut på målbilden. `select.py` har sedan dess körts och låst de fem posterna i § 1;
`garden-eight` och `squarespace` står kvar som ribbor, `creative-giants` faller helt.)*

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

**Två r8-preciseringar till blocket ovan, och bara två:** serverns sökväg i r8 är
`~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .` (skillen flyttade;
allt annat i raden gäller oförändrat), och materialet vendoras av lead enligt
`{{UT_MAPP}}/assets/ASSETS.md`, inte av dig.

---

## 5. Invarianter i r8, gäller varje runda och varje fil du rör

1. **F-011, rörelsen spelar alltid.** Sidan har inget reservläge. Skriv aldrig
   `prefers-reduced-motion`, planera aldrig ett reducerat läge, beskriv aldrig ett i BRIEF.md.
   Ingen granskare i r8 flaggar frånvaron: den är beslutad (FEEDBACK.md F-011), inte
   förbisedd. Detta ersätter r7-formatets punkt om en reduced motion-plan.
2. **F-014, `--sc-ps` och ingenting annat.** Allt ögat ser förflytta sig läser `--sc-ps`.
   Rå `--sc-p` får bara driva cue-opacitet. `sc-smooth.js` kopieras in bredvid motorn
   (`scrollcraft.js` + `.css`). Motorn redigeras aldrig, `.sc-*`-klasserna restylas aldrig.
   Akten är inte klar förrän `staircase = 0`, `max_step <= 3 %`, bildtid p95 <= 20 ms och
   noll frames > 33 ms, mätt i båda scrollriktningarna. Device-tabellens kolumn "läser" ska
   ange `--sc-ps`, `--sc-p` eller "motorns egen" per rad.
3. **UI-filer författas bara med `Write` eller `Edit`.** `.html`, `.css` och `.js` skrivs
   aldrig från skalet. `design-gate.py` nekar `cat >`, heredoc, `tee`, `sed -i`,
   `Set-Content`/`Out-File` och inline-skript som skriver filen i en armad session, och
   nekandet hamnar i ledgern som `gate-deny` med signalen `shell-write`. Att **kopiera**
   motorn med `cp` eller `Copy-Item` är tillåtet, och det är den vägen du kopierar den.
4. **Servern.** `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .`
   från repo-roten. Aldrig `python -m http.server`, aldrig en egen server, aldrig en annan
   port.
5. **Ingen generering.** Higgsfields genereringsverktyg är spärrade på din argv och kontot
   har dessutom 0 krediter (free plan, mätt av lead 2026-09-09). r8 kör med noll genererat
   material. Saknas ett material: skriv `[needs asset: ...]` i BRIEF.md respektive NOTES.md
   och gå vidare. Fråga inte, vänta inte, ersätt inte med en platshållarbild.
6. **Noll tankstreck i synlig text**, varken `–` eller `—`. Ordagrann Alunix-copy ändras
   aldrig, inte ett tecken. Tesrubriken är `VI BYGGER ERT VARUMÄRKE.` i versal form.
7. **Inga påhittade fakta.** `PRODUCT.md` § absences listar vad som aldrig får finnas:
   kunder, omdömen, logotyper, team, kontor, år i branschen, antal projekt. Saknar du en
   uppgift: skriv `[needs: ...]` och gå vidare, fråga inte.
8. **Inga kort, badges, glas, spotlights** (TASTE § 5, F-006). Ett typsnittspar, roller som
   aldrig korsar. En accent som gör en sak.
9. **Fullständig output.** Trunkera aldrig, sammanfatta aldrig i stället för att leverera.
   Måste du pausa: skriv `[PAUSED — sektion X av Y]` som sista rad och fortsätt i nästa tur.

---

## 6. Vad BRIEF.md ska innehålla

Skelettet i `{{UT_MAPP}}/BRIEF.md` har rubrikerna i rätt ordning och de låsta värdena redan
ifyllda. Fyll varje `[fylls i R1]` och lämna resten orört. I ordning:

catalogue-select-raden (din egen körning, ordagrant) · Design Read i en mening (lane +
register + grammatik) · dial-deklaration (variance / motion / density 1 till 10, en mening
per siffra) · reference lock, sju fält, media strategy som enum · decision ledger med de
obligatoriska raderna palett, typ, nav, hero-device, aktform, avslut och Memorable detail,
var och en med Area | Decision | Source | Source rule | Why · direction contract
(THESIS / OWN-WORLD / STORY / FIRST VIEWPORT / FORM) · motion-tes (focal, continuity,
feedback, budget) · feeling curve, en känsla per akt, aldrig två lika i rad · tell-someone-
meningen · device-tabell med minst fyra familjer, aldrig samma två i rad, kolumnen "läser"
ifylld per rad · Rejected-lista där varje kandidat besvarar find-animation-opportunities
fyra frågor (frekvens, syfte, hastighet, funktion) · delight-tes i en mening (för V3c:
kortet vänds) · tre persona-skisser (primär, kant, stress, med situationella villkor) ·
asset-lock per medieplats (Asset role / Slot / Art direction / Avoid) · fem live-rubriker
ordagrant med källdomän · copy-plan som skiljer ordagranna strängar från nya (nya går genom
copy-gaten i R3) · prestandaplan (LCP-bilden, fonter som preloadas, iframes lazy, budgeten i
`performance.md` § 1) · `?preview=`-plan med vad varje läge tvingar · fingerprint, din cells
rad plus utfallet mot varje registerrad · och sist "Vad jag måste slå", en rad per låst
referens · samt § Lästa referenser med tre rader digest per läst fil.

**Skriv också in den författade tystnaden** (vilka delar av akten som är avsiktligt stilla)
så att `scroll_verify.py`:s `blankBands` inte larmar falskt i R2.

---

## 7. Kommande rundor, så att du planerar rätt

- **R2:** fold och signaturakt i `{{UT_MAPP}}/index.html`, motorn och `sc-smooth.js`
  kopierade, `?preview=`-lägen, egna körningar av `scroll_verify.py` och `motion_probe.py`.
- **R3:** hela sidan, copy-gaten i fem pass, `Skill(emil-design-eng)`,
  `Skill(review-animations)`, `Skill(a11y-audit)`, alla i din egen session.
- **R4 och framåt:** fixplaner från arkitekten, en fil per fynd, körda i nummerordning.

Avsluta rundan med en kort sammanfattning: vilka filer du läste (räkna dem), var BRIEF.md
ligger, vad som står som `[needs: ...]`, och dina öppna frågor.
