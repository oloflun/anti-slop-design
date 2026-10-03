# V4 · R1 · ett helt nytt koncept för Alunix

Koncept {{KONCEPT}}, ut-mapp `{{UT_MAPP}}` (skapa den), port {{PORT}}.

**Modell:** Opus. Starta inga subagenter, gör hela uppdraget själv (`~/CLAUDE.md` § Delegering).
**Webbläsare:** bara headless, en i taget, via `tests/alunix-r8/browser_lock.py` (vänta på låset,
ta det aldrig från någon annan). Server: `python skills/design/scripts/serve.py --port {{PORT}}
--root .` från repo-roten.
**Push:** aldrig. Commit: nej, leaden committar.

## Beställningen

Anton, 2026-10-03, ordagrant: "skapa 8, ett helt nytt koncept för sidan som tar inspiration
från helt nya källor och implementerar de nya designmekanismerna från Gsap och Lenis".

Det här är alltså inte en variant av V3c–V3g. Det är en ny riktning för samma byrå och samma
fakta. Anton har beställt **ett** koncept, så bake-offen (2b punkt 5) hoppas över. Allt annat i
kedjan körs fullt ut.

## Kedjan, utan genvägar

Ladda Skill(design) och gå igenom Step 0–6. `design-gate` spärrar första UI-filen tills
referensgolvet är läst. Det omfattar, sedan 2026-10-03:
- TASTE.md, FEEDBACK.md (F-001 till F-027 är bindande) och reference-lock.md;
- en katalogvalsrad från `scripts/catalogue/select.py` med de valda posterna lästa (entry.md
  och fold som bild);
- `references/scroll/` README, grammars, devices och feel-and-fingerprint, plus
  `showcase-floor.md` och `journeys/era-residence.md`;
- fingerprint-registret (`wiki/projects/_index/design-fingerprints.md` i valvet);
- två rörelseark med `motion_floor: 2`, lästa som bild;
- Skill(lenis), Skill(gsap-core), Skill(gsap-scrolltrigger), plus gsap-timeline,
  gsap-plugins och gsap-performance när du använder dem.

**Helt nya källor.** Följande har redan använts för Alunix och får varken vara dominant
referens eller lån: aspensearch-com, cyphr-studio, exoape-com, area17-com, planhat,
era-residence (läs resan som mall för hur en resa byggs, men låna inte dess form),
collabcapitolium, forgeautomotive-co, filmbot och huehaus. Välj bland övriga poster med
`motion_floor: 2`:

    grep -l "motion_floor: 2" design-catalogue/entries/*/entry.md

Läs minst tre rörelseark och skriv reference-lock (en dominant, minst två lån, F-024). Säg för
varje källa vilket drag du tar: intro, övergångar, signaturobjekt, typ och media.

**Fingerprint-gaten.** Konceptet ska skilja sig på minst 4 av 6 dimensioner mot **varje** rad i
registret, även Alunix-raderna r1–r7, och mot V3f/V3g (rutverket: split-studio cellgrid, kort som
vänds). Räkna ut det rad för rad i `{{UT_MAPP}}/BRIEF.md`. Om planen inte klarar gaten ändrar du
planen, aldrig registret.

## Fakta och copy

Allt sakinnehåll kommer från `tests/alunix-r8/PRODUCT.md`. Låst copy står kvar ordagrant. Det
som saknas där får inte uppfinnas: inga kunder, resultat, siffror eller svarstider.

Sidan ska täcka samma frågor som V3g R9:
- vad byrån gör;
- den digitala första kontakten (tesen);
- processen i sju steg;
- de två levande exempelsajterna Calyx och Hōrai i `<iframe>` från `/sites/`, en ram som
  visats transformeras eller tonas aldrig;
- de tre paketen beskrivna utan priser. Läs de godkända beskrivningarna i
  `tests/alunix-r8/runs/V3g/index.html`, sök `pkg-desc`. Använd dem, och lägg till raden "Vi
  lämnar pris efter första samtalet.";
- kontakt via `kontakt@alunix.se`, med en etikett som säger att det är mejl.

Varje sträng går genom Skill(copywriting), sedan Skill(copy-editing) och sist
Skill(humanizer-svenska). Inga riktiga person- eller platsnamn utom Stockholm.

Bilder: bara material som redan finns i repot (exempelsajternas bilder under `sites/`,
`tests/alunix-r8/runs/V3g/assets/`, `tests/alunix-concepts-r3/build/assets/`) eller i katalogens
poster. Ingen generering, ingen hotlänk.

## Golvet som ska nås (showcase-floor.md § 2, alla sju)

1. Intro och hero är ett skott: något följer med över övergången.
2. Varje sektionsbyte har en materiell orsak. Minst tre olika orsaker, aldrig samma två gånger
   i rad, och var och en hämtad ur byråns eget material (webbsidor, rutnät, skärmar, kort,
   typ). Inga 14 px-tonningar som enda övergång.
3. Ett signaturobjekt återkommer och förändras genom sidan.
4. Text i läsfart: SplitText med radmasker. Minst ett påstående styrs av scrollen. Varje
   rubrik står hel och stilla ≥ 40 vh.
5. Typ och media delar ram minst en gång.
6. Husets utjämning: Lenis `lerp .075`, `wheelMultiplier .6`, `respectReducedMotion: false`,
   `anchors: true`, gsap.ticker som enda RAF, `lagSmoothing(500, 33)`, `scrub: true` överallt.
7. Ingen grind.

Motorn är den länkade GSAP 3.15 + Lenis 1.3.26 (`references/scroll/toolchain.md`):
- statisk HTML med importmap;
- aldrig CDN vid körning, aldrig `npm install`, aldrig en kopia;
- import bara via de centrala `gsap.js` / `smooth-scroll.js`.

En pin skapas en gång och dödas aldrig. En iframe i en pinnad scen får en egen `pinSpacer` och
anropar aldrig `refresh()` från sin `load`. Varje animerad egenskap har en ägare (F-027).

## Mät innan du säger klart

Kör allt headless genom låset och läs varje bild själv:
- `section_probe.py` på hela sidan, sparad till `{{UT_MAPP}}/shots/section-probe.json`: alla
  sektioner p95 ≤ 20 ms, en laddning per iframe, 0 refresh.
- Hjulvandring 1440×900, 768×1024 och 390×844 (och 320×640 för kontakten).
- Sidans eget rörelseark: `MOTION_FRAMES=40 python scripts/catalogue/motion_capture.py --url
  http://127.0.0.1:{{PORT}}/tests/alunix-r8/runs/V4/index.html --slug alunix-v4-self --redo`.
  Lägg det bredvid dina floor-2-ark och gå regel för regel genom § 2 i `{{UT_MAPP}}/NOTES.md`.
- `skills/design/scripts/a11y_scan.py`, och textavstånd (WCAG 1.4.12) i 1440 och 390. Ingen
  text får bli oläsbar eller klippas.
- `microtext_scan.py --names` på sidan: 0 träffar.

Lämna:
- `{{UT_MAPP}}/index.html`
- `{{UT_MAPP}}/BRIEF.md` (känslokurva, topp, signaturdrag, fingerprint-räkning)
- `{{UT_MAPP}}/NOTES.md` (referenslås, beslutslogg, golvet regel för regel, mätvärden,
  föreslagen registerrad)
