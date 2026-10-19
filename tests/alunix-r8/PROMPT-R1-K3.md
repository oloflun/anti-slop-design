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
catalogue-select: squarespace, aevi-wellness, beautiful, insign, mode
```

Primär post (13 poäng): **`squarespace`**. Övriga låsta: **`insign`**,
**`aevi-wellness`**, **`beautiful`**, och wildcard **`mode`** (utanför kategorin).
**Anti-referens, som ska läsas och sedan undvikas i varje detalj:**
`sites/before-ai-slop.html` (div-byggd låtsas-UI, gradientord, badge, pill, logotypvägg,
tre ikonkort).

Planens § 7.5 gissade `caractere-bois`, `hyperborea`, `wild`, `garden-eight` och
`tidvatten`. Ingen av dem föll ut, och orsakerna är mekaniska och kontrollerade i
`index.json` (arkitekten har skrivit ut dem i `tests/alunix-r8/concepts-K3.md`
§ catalogue-select). Skriptets rad vinner: **de fem posterna ovan är cellens låsta
referenser.** Du får läsa andra poster som jämförelse, men en post som inte är vald får
varken en rad i reference-locken eller en rad i "Vad jag måste slå".

**Avviker ditt resultat från raden ovan:** rapportera avvikelsen i BRIEF.md, ordagrant, med
skriptets hela utdata, och **följ sedan arkitektens rad**. Du byter aldrig referenser på egen
hand.

---

## 2. Referensgolvet du läser innan du skriver en rad i BRIEF.md

Läs med `Read`, aldrig med `cat`. Bilder läses som **pixlar**, inte som filnamn.

**Smak och återkoppling**
- `design-catalogue/TASTE.md`, hela.
- `design-catalogue/FEEDBACK.md`, **alla poster**. F-006 (glas), F-007 (målbild bild för
  bild), F-009 (orkestreraren äger assets), F-010 (fönstret i fasaden: innehållet maskas in
  i objektets verkliga öppning), F-011 (rörelse alltid), F-012 och F-014 (hackig rörelse,
  `--sc-ps`) styr den här cellen.

**Varje vald katalogpost**, under `design-catalogue/entries/<slug>/`
(`squarespace`, `insign`, `aevi-wellness`, `beautiful`, `mode`):
`entry.md` hela inklusive § Motion och § Reference lock, `extract/*-design-language.md`,
`fold.webp` och alla `slices/*.webp` **som bilder**. Tre rader digest per fil i
BRIEF.md § Lästa referenser: vad den gör, vad du tar, vad du lämnar.

**Anti-referensen:** `sites/before-ai-slop.html`, hela filen som text. Skriv i BRIEF.md
vilka fem drag i den du aktivt bygger bort.

**Kedjans referenser**, under `~/.claude/skills/design/references/`:
`reference-lock.md`, `scroll/devices.md`, `scroll/feel-and-fingerprint.md`, `scroll/pace.md`,
`motion-smoothness.md`, `performance.md`, `lift.md`.

**Registret:** `wiki/projects/_index/design-fingerprints.md`, alla rader. Fingerprint-gaten
är minst 4 av 6 skillnad mot **varje** rad, och K3 är ett nytt koncept: gaten gäller fullt
ut. Arkitekten har redan skrivit ut utfallet i `concepts-K3.md` § (4); du verifierar det.

**Cellens eget underlag:** `tests/alunix-r8/PRODUCT.md` (beviskassan och § absences),
`tests/alunix-r8/concepts-K3.md` (arkitektens målbildsgrind, hela, inklusive tokens,
typsnittskandidater, troplistan och gate 47/79-regeln),
`{{UT_MAPP}}/BRIEF.md` (skelettet du fyller), `{{UT_MAPP}}/assets/ASSETS.md` (SVG-specen för
ritningen och papperstexturen) och `credits.json`.

**De fem live-rubrikerna i kategorin** hämtar du själv med webbsök på
`digital byrå webbdesign Sverige`, tar de fem bästa träffarna, citerar varje `H1`
**ordagrant** med källdomän, och skriver in dem i BRIEF.md § Fem live-rubriker.
**Fabricera aldrig en rubrik.** Går sökningen inte att köra: skriv `[needs: live-rubriker]`
och gå vidare.

---

## 3. Målbilden för {{KONCEPT}}, bindande

Ordagrant ur planens § 7.5. Varje avvikelse kräver en rad i BRIEF.md § decision ledger med
källa.

#### K3 · "Ritningen" (nytt koncept 1)

**Idé.** Alunix ritar innan de bygger. Sidan är en teknisk ritning av en webbplats på kallt ritpapper: en dimensionerad sektionsritning av en sida (konturer, måttlinjer, utrop med **sanna** värden: 320/768/1440, `7 rem`, `96 px`, `16:9`, priserna) som ritar sig själv när man scrollar, och sedan *blir* det den ritade: den riktiga Calyx-sidan tonar in **innanför den ritade konturen** (F-010-principen: innehållet maskas in i objektets verkliga öppning, bläcket ligger kvar som ram). Noll fotografier (Hyperborea-precedens). Aldrig en falsk UI-mock (gate 79): ritningen har inga låtsasknappar eller låtsastext, bara konturer, måttlinjer och utrop.

**Auktoritet:** ytan (papper + bläck; TASTE §1 rad 3); typen medelstor; bilder inga; i set-piece-akten rörelsen. **Register:** modern clean (ämnet är precision). **Grammatik:** chaptered editorial (titelsida utan media; folio; kolofon-liknande *specifikation* som avslut). **Palett:** ett kallt ritpapper (oklch ~0.95, hue 230, låg chroma; *inte* cream, AB09-lärdomen), ett bläck (mörk petrol/ultramarin), Alunix-blått `#1E5E9C` (Tier 1-bevis) som enda accent, bara på måttsiffrorna i displayskala. **Typ:** en grotesk med teknisk karaktär i två snitt + en mono som register (måtten). Arkitekten kör brand.md-proceduren; **förbjudna**: reflex-listan och alla snitt som använts i r1–r7 (Geist, Inter, JetBrains Mono, Public Sans, Familjen Grotesk, Literata, Fragment Mono, Hanken Grotesk, Instrument Serif, Archivo, IBM Plex Mono, Figtree, Cardo, PT Mono, Cinzel, Vollkorn, Italiana).

**Nav:** en ritad *teckenförklaring* (legend) i marginalen, sticky, som är sidans index (varje rad = ett kapitel, en linje dras till kapitlet när det är aktivt). **Hero-device:** ritningen ritar sig (SVG `stroke-dashoffset` från `--sc-ps`, pinnad akt span 2.4 = toppen), måttsiffrorna räknar upp till sina sanna värden (`count`, bara riktiga tal). **Aktform:** pin (ritningen) → kinetic lines (kapitelrubrik "Vi bygger ert varumärke.") → reveal ×3 (en plate per exempelsajt: konturen ritas, sedan tonar den riktiga sajten in innanför konturen, bläcket blir ram; iframe monteras lazy) → flow+in (liggaren 01–03) → count+flow (specifikationen: paketen som stycklista med de sanna priserna) → close. ≥ 5 familjer, aldrig samma två i rad. **Avslut:** specifikationsbladet (priser, `Alla har rätt till bra design.`, en mailto) inom en ritad ram vars linjer dras in sist; sidan slutar stilla. **Signaturrörelse:** *ritningen blir sidan*: konturen ritas, fylls med den levande sajten, bläcket stannar som ram. Tell-someone: "det är sajten där man ser hemsidan ritas som en ritning och sen blir den på riktigt".

**Referenser (förväntade ur `select.py`):** `caractere-bois` (hårlinje-ritningar över foton: "designat innan byggt"), `hyperborea` (ritat identitetssystem, noll foton), `wild` (pixelritad silhuett som banner), `garden-eight` (ett typografiskt + ett skulpturalt moment), `tidvatten` (modern clean, två sanna siffror som set-piece). Anti-referens: `before-ai-slop` (div-byggd låtsas-UI).

**Målbildsgrind:** (1) auktoritet ytan; viker: typ (medel), foto (inget), färg (en accent på måtten). (2) troplistan: inga kort, inga badges, inget glas, ingen gradient, ingen spotlight; **ritning ≠ falsk UI** kontrolleras mot gate 47/79 bild för bild. (3) ett displayelement per skärm: ritningen (s1), kapitelrubriken (s2), en plate i taget (s3–5), priserna (s6), mailto (s7). (4) fingerprint: mot Hyperborea (grammatik delad → nav legend ≠ sticky header+edition strip · hero ritning ≠ SVG-sol · aktform ≠ · avslut specifikation ≠ kolofon · signatur ≠ → 5/6); mot r1 K4 Journal, r2 R2/R3/R4, r4 M2 (alla chaptered): ≥4/6 på nav/hero/akt/signatur; arkitekten skriver ut alla 36 rader.

*(Slut på målbilden. Två saker har hänt sedan den skrevs och båda gäller: `select.py` har
låst de fem posterna i § 1 i stället för den förväntade listan, och arkitekten har delat upp
skärmarna i elva i stället för sju, eftersom den pinnade akten är fyra granskningsbara vyer.
Båda står med källa i `concepts-K3.md`.)*

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
`{{UT_MAPP}}/assets/ASSETS.md`, inte av dig. K3 har noll fotografier: cellens medieplatser
är de tre levande sajterna plus det ritade systemet.

---

## 5. Invarianter i r8, gäller varje runda och varje fil du rör

1. **F-011, rörelsen spelar alltid.** Sidan har inget reservläge. Skriv aldrig
   `prefers-reduced-motion`, planera aldrig ett reducerat läge, beskriv aldrig ett i BRIEF.md.
   Ingen granskare i r8 flaggar frånvaron: den är beslutad (FEEDBACK.md F-011), inte
   förbisedd. Detta ersätter r7-formatets punkt om en reduced motion-plan.
2. **F-014, `--sc-ps` och ingenting annat.** Allt ögat ser förflytta sig läser `--sc-ps`:
   varje `stroke-dashoffset`, masken över öppningen, linjalens `scaleX`, marginalspaltens
   parallax. Rå `--sc-p` får bara driva cue-opacitet. `sc-smooth.js` kopieras in bredvid
   motorn (`scrollcraft.js` + `.css`). Motorn redigeras aldrig, `.sc-*`-klasserna restylas
   aldrig. Akten är inte klar förrän `staircase = 0`, `max_step <= 3 %`, bildtid p95
   <= 20 ms och noll frames > 33 ms, mätt i båda scrollriktningarna.
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
   kunder, omdömen, logotyper, team, kontor, år i branschen, antal projekt. Varje siffra i
   ritningen ska vara ett verkligt mått eller ett verkligt pris. Saknar du en uppgift: skriv
   `[needs: ...]` och gå vidare, fråga inte.
8. **Inga kort, badges, glas, spotlights** (TASTE § 5, F-006). Ett typsnittspar, roller som
   aldrig korsar. En accent som gör en sak.
9. **Gate 47 och gate 79, cellens känsligaste punkt.** Ritningen ritar **form**, aldrig
   **innehåll**. Tillåtet i SVG: konturer, måttlinjer med pilspetsar, hjälplinjer,
   snittmarkeringar, skrafferingar och utrop som anger ett mått eller namnet på en zon.
   Förbjudet: rektanglar som föreställer knappar, grå staplar som föreställer text, navrad,
   formulär, graf, sparkline, webbläsarram, flikrad, URL-fält, telefonbezel, eller en siffra
   som inte är ett verkligt mått. Kontrollen: varje `<rect>` och `<path>` ska kunna namnges
   som "kontur", "måttlinje", "hjälplinje", "skraffering" eller "utrop". Kan den inte det
   ska den bort.
10. **Fullständig output.** Trunkera aldrig, sammanfatta aldrig i stället för att leverera.
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
(THESIS / OWN-WORLD / STORY med elva skärmar / FIRST VIEWPORT / FORM) · motion-tes (focal,
continuity, feedback, budget) · feeling curve, en känsla per akt, aldrig två lika i rad ·
tell-someone-meningen · device-tabell med minst fem familjer, aldrig samma två i rad,
kolumnen "läser" ifylld per rad · Rejected-lista där varje kandidat besvarar
find-animation-opportunities fyra frågor (frekvens, syfte, hastighet, funktion) · delight-tes
i en mening (för K3: ritningen blir sidan) · tre persona-skisser (primär, kant, stress, med
situationella villkor) · asset-lock per medieplats (Asset role / Slot / Art direction /
Avoid) · fem live-rubriker ordagrant med källdomän · copy-plan som skiljer ordagranna
strängar från nya, inklusive legendens fem kapitelnamn och tjänsternas tre underrader (nya
går genom copy-gaten i R3) · prestandaplan (fonter som preloadas, iframes lazy, budgeten i
`performance.md` § 1) · `?preview=`-plan med vad varje läge tvingar · fingerprint, din cells
rad plus utfallet mot varje registerrad · och sist "Vad jag måste slå", en rad per låst
referens · samt § Lästa referenser med tre rader digest per läst fil.

**Skriv också in den författade tystnaden:** de första 0,12 av akt a1 är ett avsiktligt
nästan tomt ark med bara titelblocket, tystnaden före toppen och inte död scroll. Utan den
raden larmar `scroll_verify.py`:s `blankBands` falskt i R2.

**Ritningens ordning ska stå utskriven i BRIEF.md** innan du ritar något i R2: vilka
konturer, vilka hjälplinjer, vilka måttlinjer, vilka utrop, och i vilken ordning de dras.
Underlaget är SVG-specen i `{{UT_MAPP}}/assets/ASSETS.md`.

---

## 7. Kommande rundor, så att du planerar rätt

- **R2:** fold och signaturakt i `{{UT_MAPP}}/index.html`, motorn och `sc-smooth.js`
  kopierade, `?preview=`-lägen, egna körningar av `scroll_verify.py` och `motion_probe.py`.
- **R3:** hela sidan, copy-gaten i fem pass, `Skill(emil-design-eng)`,
  `Skill(review-animations)`, `Skill(a11y-audit)`, alla i din egen session.
- **R4 och framåt:** fixplaner från arkitekten, en fil per fynd, körda i nummerordning.

Avsluta rundan med en kort sammanfattning: vilka filer du läste (räkna dem), var BRIEF.md
ligger, vad som står som `[needs: ...]`, och dina öppna frågor.
