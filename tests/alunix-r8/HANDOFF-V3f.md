# Handoff: V3f "Rutverket" och de fyra verktygen

Skriven 2026-09-24 av leaden (Opus). Körningen var en **isolerad testkörning**: designkedjan
(`design`-skillen, hookarna, katalogen) var avstängd. Allt designunderlag kom ur fyra källor:

1. **Inspo-MCP** (`mcp__inspo__*`): form, referenser, riktiga tokens.
2. **UI Skills-MCP** (`mcp__ui-skills__*`): hantverksregler.
3. **GSAP-skillsen** (`~/.agents/skills/gsap-*`, lokala, officiella).
4. **Lenis-skillen** (`~/.agents/skills/lenis/`, skriven i den här körningen ur primärkällor).

Antons dom efter R4: *"nästan perfekt på en gång och redan bättre och mer unikt än v3d"*.
Uppdraget till nästa agent är att **föra in de här verktygen i det fullständiga designsystemet**
så att nästa bygge får samma utfall *med* kedjan påslagen, inte trots att den var avstängd.

> **Rättelse 2026-10-02 (läs detta först).** Den första versionen av § 6 listade åtta
> integrationssteg som kvar att göra. Det var fel för sju av dem: en tidigare session
> (loggen `session-logs/2026-09-29-session-log.md`) hade redan fört in Inspo, GSAP+Lenis och
> ledgern i den körande designskillen, och jag skrev planen utan att ha läst den loggen.
> § 6 är omskriven mot det som faktiskt ligger på disk, kontrollerat fil för fil. § 7 säger
> vad som verkligen återstår, och § 8 vad som är incheckat och vad som är pushat.

Läs i den här ordningen:

| Fil | Vad |
|---|---|
| `HANDOFF-V3f.md` | Denna fil: processen, vad som bar, vad som föll, och integrationsplanen |
| `runs/V3f/KEDJA.md` | Varje MCP- och skill-anrop per runda, mätt ur transkripten, med leadens pixelkontroll per anrop |
| `runs/V3f/RAPPORT.md` | Byggarnas rapporter R1 till R5 med mätvärden |
| `runs/V3f/BYGGSPEC.md` | Kompositionsspecen (R1). Mallen för en spec som bär ett grepp |
| `runs/V3f/RORELSE-SPEC.md` | Rörelsespecen (R3). Mallen för en koreografi per sektion |
| `runs/V3f/RUNDA5-SPEC.md` | Antons R4-dom omsatt: läsbarhet, casevalet och kontakten |
| `INSPO-MCP-INSTRUKTION.md` | Inspo-verktygen och antimönstren (från V3e-körningen). Fortfarande giltig |
| `HANDOFF-V3e.md` | Varför V3e blev ett dokument. Kontrasten gör V3f begriplig |
| `chaintrace.py` | Spåraren som läser subagenternas transkript och listar kedjeanropen |

---

## 1. Vad som gjorde skillnad mot V3e

V3e och V3f hade samma copy, samma bildbank och samma modeller. V3e blev ett typografiskt
dokument (4,3 % bildyta, i praktiken två ytor), medan V3f blev en komposition (30 % bildyta,
fyra platta ytor plus rastrerade bildceller, ett objekt som vänds). Skillnaden låg i fem
beslut, i den här ordningen:

1. **Briefen till `recommend` var sidans formproblem, inte en stämning.** Så här löd den:
   levande kundsajter som bevis, tre verks identiteter på en sida med egen identitet,
   visitkortet som fysiskt objekt. Inga stilord.
2. **Sökningen var formulerad som form.** Sökningen *"client websites shown as huge full-bleed
   screens that dominate the page"* gav Aspen Search. Den andra sökningen, som var
   objektsformulerad, gav bara brus (lexikal rankning). Budgeten hölls på två sökningar.
3. **Referenserna öppnades som fullsidor, inte miniatyrer.** `get_screen` ger URL:er till
   `full.1440.webp`. De hämtades med curl, konverterades och **lästes som bild**. Det var
   Aspens *fullsida*, inte heron, som visade greppet: hela sidan är ett enda rutnät av
   celler. Miniatyren visar bara 2×2-kvadranten.
4. **`get_design_system` gav riktiga tokens.** Det gav #0af474, radie 0, vikt 450, −4 %
   tracking och den flytande skalan 52→200 px, och de gick rakt in i specen. Inget gissades.
5. **Specen började med greppet i en mening:** *hela sidan är ETT kontinuerligt, hårt rutnät
   av celler … diagonalt motstående celler delar tema.* Därefter kom cellkartan per sektion
   och till sist spärrarna. V3e:s spec var 90 % spärrar och paritet.

## 2. Vad som var fel i processen (ärligt, också leadens egna fel)

| Fel | Vems | Följd | Lärdom att föra in |
|---|---|---|---|
| `compare` gav `sameRegister:false`, och leaden valde **en** referens | lead | Kompositionen vilade på Aspen ensam, vilket Anton påpekade | `compare` är ett **trianguleringsverktyg**: ta ett drag från varje referens som delar något, inte ett filter som väljer en. R3 rättade det i rörelsen (Cyphr, Exoape, Area17) |
| Specen sa "ALUNIX skuret av nederkanten" | lead | Ett ord utan underhäng tappade sina baslinjer och lästes som "AI UNIX" | Beskärning är bara tillåten där glyferna har något att förlora som inte bär läsningen (underhäng, en utfallande bokstavs sida). Aldrig baslinjen |
| Copy-diffen jämförde mängder, inte antal | byggare R1 | En duplicerad rubrik gick igenom | Diffen räknar förekomster (`Counter`). Infört R2 |
| Byggaren förklarade klippningen som "kerning" | byggare R4 | Fel diagnos. Den enda kontrollen som fångade det var leadens egen bild | Pixelgranskning av leaden är inte valfri. Husregel 8: misstänk mätningen, och här misstänk också förklaringen |
| Rutmönstermasken togs bort i R1 i stället för att lagas | byggare R1 | Cyphr-lånet försvann i tysthet och kom tillbaka först i R3 via GSAP grid-stagger | En borttagen specpunkt ska flaggas som avvikelse och stanna på listan |
| Inline-`grid-column` slog ut mobilens media queries | byggare R1 | Pris-bentot gick sönder vid 390 | Placering i klasser, aldrig inline |
| Lenis `respectReducedMotion` är `true` som standard | lenis-skillen (fynd) | Hade stängt av all rörelse för Anton, vars Windows kör med animationer av (se CARL design-beslut 2026-09-07) | Sätts uttryckligen i husets Lenis-init |
| Lenis `anchors` är `false` som standard | lenis-skillen (fynd) | Ankarlänkar slutar fungera utan att något syns | Sätts uttryckligen |
| Rubriker rörde sig medan de skulle läsas | lead (R3-spec) | "första intrycket hinner man knappt se" | R5-regeln: **varje rubrik står helt synlig under ≥ 40 vh**; rörelse bara före och efter |
| Tumnaglar gjorda av lågupplösta skärmbilder uppskalade till 140 vh | byggare R2, på leadens 30 %-golv | Suddigt och inzoomat. Bildytegolvet uppfylldes med en förstoring | Ett ytmått får aldrig uppfyllas genom att förstora samma bild. R5: skarpa, nytagna 2× bilder, utzoomade |

## 3. Verktygen, ett i taget: vad de är bra på och var de passar in

### 3.1 Inspo-MCP
- **Bra på:** form. Att hitta *en sida som redan har löst samma formproblem* och ge dess riktiga
  tokens och fold-för-fold-autopsi.
- **Svagt:** rankningen är lexikal utan embedding-nyckel (`tip` säger det). Objekt- och
  stämningsfrågor ger brus. Rörelse finns inte i arkivet (statiska skärmbilder), så
  rörelselån måste läsas ur autopsiernas text ("checkerboard pixel-dissolve").
- **Arbetsflöde som bar** (budget: 1 recommend, 2 sökningar, 1 compare, 3 get_screen,
  1 design system, 2 JSX): `get_filters` → `recommend(formproblem)` → `search_screens` ×2 →
  `compare` → `get_screen` ×3, där fullsidan hämtas och läses som bild →
  `get_design_system` på den primära → `find_reference_components` + `get_reference_jsx` för
  sektioner som saknar form (pris: `tier-bento`).
- **Plats i systemet:** `reference-lock.md` nämner redan "Refero MCP when configured" som
  källa. Inspo ska in på samma rad, med **katalogen först** (SKILL.md steg 5 är oförändrat).
  Inspo är andra källan, före användarens URL. Instruktionen `INSPO-MCP-INSTRUKTION.md` ska
  flyttas till `~/.agents/skills/design/references/inspo-mcp.md` (**live först**, sedan
  speglas repot med `scripts/sync-from-live.py`, enligt GOALS delmål 5).
- **Tokens:** `get_design_system` levererar en DESIGN.md. Den passar direkt in i
  `design-md.md`-formatet som Tier 2-evidens. Lägg till i `reference-lock.md` att
  primärreferensens tokens ska hämtas, inte avläsas ur en bild.

### 3.2 UI Skills-MCP
- **Bra på:** hantverksregler som är billiga att lägga på efter att formen är bestämd:
  radie 0, 12→6→1-omkomposition (`elithrar/neo-industrial-design`), grid-först och 8 px-bas
  (`zeke/swiss-design`), easing och "animera bara transform/opacity" (`emil-design-eng`).
- **Fynd (V3e, bekräftat igen):** registret serverar samma text som flera av husets lokala
  skills (`emil-design-eng`, `impeccable`, `frontend-design`, `design-taste-frontend`). Att
  stänga av en lokal skill stänger inte av kunskapen.
- **Svagt:** `list_skills` utan `query` kraschar på storlek (114 kB). Beskrivningarna säger
  *vad* en skill är, inte *när* den passar. Dubbletter under olika konton.
- **Plats i systemet:** inte som ny källa för kunskap som redan finns lokalt. Använd den som
  **uppslag för hantverksskills som saknas lokalt**. I körningen var det `swiss-design` och
  `neo-industrial-design`, och båda gav mätbara regler. Förslag: en rad i
  `skill-orchestration.md` om att `ui-skills` frågas med `query` (aldrig tomt) efter att
  registret är låst, och att en hämtad skill som ändrar ett beslut loggas i beslutsliggaren.

### 3.3 GSAP (officiella skills, lokalt)
- **Bra på:** allt husets scrollcraft-motor inte gör. Scrubbade tidslinjer, pin, SplitText
  med masker, grid-stagger (`stagger:{grid, from:'random'}`, som bar Cyphrs
  rutupplösning), `matchMedia` per brytpunkt, `quickTo` för pekarstyrd lutning.
- **Skillsen som användes, i ordning:** `lenis` → `gsap-core` → `gsap-scrolltrigger` →
  `gsap-timeline` → `gsap-plugins` (SplitText) → `gsap-performance`, och i R5 `gsap-utils`.
  Alla laddades före första kodraden (verifierat i transkriptet med tidsstämplar).
- **Regler som visade sig bärande:** ScrollTriggers skapas i sidordning. scrub och
  toggleActions blandas aldrig. SplitText `type:'lines,words,chars'` med `mask:'lines'`,
  plus `white-space:nowrap` per ord, annars bryts ord mitt i. Masken behöver luft nedtill
  (padding-bottom med lika negativ marginal), annars kapas underhängen. `end:'bottom bottom'`
  för det sista elementet på sidan, annars når det aldrig progress 1.
- **Licens:** GSAP 3.13+ är fri inklusive SplitText. Vendoras lokalt
  (`assets/vendor/`, 3.15.0), aldrig CDN i runtime.

### 3.4 Lenis
- **Kopplingen (den enda):** `new Lenis({autoRaf:false, anchors:true,
  respectReducedMotion:false, lerp:0.075, wheelMultiplier:0.6})` (husets tempo efter F-020;
  V3f byggdes med `lerp:0.1` före domen), `gsap.ticker.add(t => lenis.raf(t*1000))`,
  `gsap.ticker.lagSmoothing(0)`, `lenis.on('scroll', ScrollTrigger.update)`. Ingen
  `scrollerProxy`, eftersom Lenis rullar den riktiga sidan. Ingen `scroll-behavior:smooth`.
- **Samspel med iframes:** Lenis egen CSS sätter `pointer-events:none` på iframes under
  smooth-scroll. För scrollstyrda inbäddningar (showcasen) är det önskat. För inbäddningar som
  användaren ska rulla i, sätt `data-lenis-prevent`.
- **Samspel med husets verifiering:** `window.__lenis` exponeras, och alla hopptester går via
  `lenis.scrollTo(el, {immediate:true})`. Ett `window.scrollTo` bredvid Lenis ger
  mellantillstånd som ser ut som buggar.

### 3.5 GSAP+Lenis mot husets scrollcraft
Scrollcraft (`~/.agents/skills/design/scripts/scroll/`) är husets motor: "copy, never edit",
sex tokens, `--sc-p` per akt. V3d byggdes på den, och dess signatur (kortet vänds, pinnade
case) krävde tusentals rader egen kod runt motorn (`latchTick`, `measureCase`, hopp-shims).
V3f gör mer rörelse med mindre egen kod: runda 3 ersatte den egna loopen helt.

**Beslutet är redan fattat (Antons order, CARL design-012):** GSAP+Lenis är husets
standardmotor för all rörelse. Scrollcraft behålls bara för sidor som redan är byggda på den.
Min första rekommendation ("andra motor bredvid scrollcraft") var alltså svagare än det som
gäller. Lenis-initen med husets tre avvikelser från standard (`autoRaf:false`, `anchors:true`,
`respectReducedMotion:false`) står som kodblock i `references/scroll/devices.md` rad 44.
**Blanda aldrig motorerna på samma sida.** Två scrollägare är samma fel som två RAF-loopar.

## 4. Husregler som den här körningen bekräftade eller skärpte

- **Rörelse spelar alltid (F-011)**, men **rubriker står stilla när de läses** (ny, R5).
  Formuleras i `motion.md`: "varje rubrik ≥ 40 vh helt synlig, oklippt, orörlig".
- **Fail toward visible (CARL design 10):** varje reveal behöver en väg till synligt vid
  hopp, vid maxscroll och när triggern aldrig fyrar. Kontaktkortet vänder sig självt vid
  progress 0,7. Kontrollen `max_scroll_residual_check()` i `runs/V3f/verify_motion.py` är
  mallen.
- **Leadens pixelgranskning är en egen kontroll, inte en uppföljning.** Varje runda i V3f
  hittade fel som byggarens egen verifiering hade godkänt. Stegen
  (`lead_motion_capture.py` i den här mappen) ska in i `skill-orchestration.md` § 12
  som leadens del:
  1. Riktig hjulscroll (`page.mouse.wheel` i steg om 4×120 px).
  2. En bild per ~halv viewport, sammanställd till ett kontaktark.
  3. Introt vid 60, 150, 250 och 400 ms.
  4. Slutläget vid maxscroll på varje bredd.
- **Skärmfångst kan falla på miljön.** "Unable to capture screenshot" vid 390 berodde på
  att boardfliken laddade samma sida parallellt. Isolerat gick fångsten på 0,08–0,57 s.
  Lägg in omförsök (3×) i fångstskript innan felet tolkas som en regression.

## 5. Skill-kedjan: hur den bevakades

- `tests/alunix-r8/chaintrace.py <lead-session-id>` läser
  `~/.claude/projects/<slug>/<session>/subagents/agent-*.jsonl` (också subagenter på djup
  2, som skill-skrivaren startade) och listar varje `mcp__inspo__*`, `mcp__ui-skills__*`
  och `Skill`-anrop med tid och argument. Det är **transkriptet, inte byggarens rapport**, som
  räknas. I V3f stämde rapporterna med transkripten i varje runda.
- Byggarna fick kedjan föreskriven *med ordning och tidpunkt* ("före första CSS-raden").
  Varje runda har en tabell i `KEDJA.md` med kolumnen *leadens kontroll i pixlar*: vad anropet
  ledde till och om det syns.
- Förslag till systemet: `design-stop.py` § ROUTE GAP räknar i dag Skill-anrop.
  MCP-anropen syns inte där. Utöka ledgern (`.impeccable/design-session.jsonl`) med en
  `mcp`-händelse för `mcp__inspo__*` och `mcp__ui-skills__*` (PostToolUse-matchare), så att
  `chaintrace.py` blir onödig i drift.

## 6. Läget i designsystemet, kontrollerat 2026-10-02

Kontrollerat mot de körande filerna under `~/.agents/skills/design/` (live) och repospegeln
`skills/design/`. Där ett steg står som gjort har jag hittat raden, inte antagit den.

| # | Steg i den ursprungliga planen | Läge | Belägg |
|---|---|---|---|
| 1 | `references/inspo-mcp.md` med formproblem-brief, fullsidan som bild, `compare`, tokens | **Gjort** | filen finns (13 Inspo-träffar). Rad 24–26: flödet. Rad 40–45: "`compare` triangulates; it never picks a winner". Rad 46–51: `get_screen` ger `full.1440.webp` som ska läsas som bild |
| 2 | Inspo i `reference-lock.md`, primärens tokens hämtas | **Gjort** | `reference-lock.md` rad 129–131: Inspo som andra källa, tokens via `get_design_system` |
| 3 | `SKILL.md` steg 5: Inspo när katalogen saknar formen | **Gjort** | `SKILL.md` rad 336 och 594 |
| 4 | GSAP+Lenis i `scroll/devices.md` | **Gjort, och starkare än planen** | 40 träffar. Lenis-init rad 44 med `lerp:0.075`, `wheelMultiplier:0.6` och de tre avvikelserna. CARL design-012: standardmotor |
| 5 | `motion.md`: läsregel, fail toward visible | **Gjort** | rad 318 (rubrik ≥ 40 vh, rörelse bara före och efter), rad 324 (fail toward visible med självfullbordan), rad 341 (godkända effekter skyddas). `end:'bottom bottom'` för sidans sista element: **ej kontrollerat** |
| 6 | `skill-orchestration.md`: leadens pixelgranskning, UI-skills | **Gjort** | rad 206 (UI Skills-registret), rad 302–316 (riktig hjulscroll, bild per halv viewport, kontaktark, bara headless) |
| 7 | MCP-händelse i ledgern | **Kodad, ej provad separat** | `hooks/design-vision-track.py` rad 32 och 175, `design-stop.py` rad 47. Stop-hooken i den här sessionen räknade skill-laddningar och flaggade `lenis`, `gsap-core` och `gsap-scrolltrigger` som saknade, så rutterna fungerar. Ett provbygge som visar en `mcp`-rad i `design-report-*.md` är inte gjort |
| 8 | A/B-körning med kedjan på | **Inte gjord** | se § 7 punkt C |

Vad som däremot **inte** syns i referensfilerna (letade i de körande kopiorna): domarna
F-023 till F-026 som regler. De ligger i `design-catalogue/FEEDBACK.md`, som steg 1b läser
ovillkorat, så de verkar redan, men de står inte i `references/`. Detaljer i § 7 punkt B.

## 7. Vad som verkligen återstår, i ordning

**A. Distribution. Tre luckor, och det är den viktigaste.** Reglerna finns lokalt men
verktygen de pekar på finns inte hos någon annan installation.
1. **Pluginet.** Det installerade pluginet (`anti-slop-design` 1.1.0, cachen under
   `~/.claude/plugins/cache/anti-slop-design/`) och `dist/plugin/skills/` innehåller bara fem
   skills: `a11y-audit`, `brand-system`, `design`, `design-catalog`, `design-verify`. `lenis`
   och de åtta `gsap-*`-skillsen finns bara globalt i `~/.agents/skills/`. En molnsession, chatten
   eller en annan maskin får `devices.md` som säger "ladda `lenis`" men inte skillen.
2. **`super-intelligence`-paketet.** Där ligger `lenis` (version 0.11.0, incheckad 47d5528).
   De åtta `gsap-*`-skillsen (`gsap-core`, `-frameworks`, `-performance`, `-plugins`, `-react`,
   `-scrolltrigger`, `-timeline`, `-utils`) finns inte i paketet. Kopiera dem från
   `~/.agents/skills/`, bumpa `VERSION` och `CHANGELOG.md`, kör `node scripts/export-to-public.mjs`
   och läs rapporten (fixa källan om grinden flaggar något, lägg aldrig till ett undantag).
3. **Inspo-forken är lokal.** `~/inspo` (branch `house`, 97 katalogposter ur `house-screens.json`) och
   `~/.claude.json` pekar `inspo`-servern dit. `inspo-mcp.md` beskriver forken. Ingen annan
   installation har den; den hostade upstreamservern fungerar men saknar husets poster.
   Bestäm om forken ska dokumenteras som maskinlokal eller paketeras.

   Gör det som ett beslut för Anton först: vilken av `anti-slop-design`-pluginet och
   `super-intelligence` ska äga skillsen? Designskillsen flyttades 2026-09-04 till det egna
   pluginet, så `lenis` och `gsap-*` passar där. Bygg om det med
   `python scripts/build-plugin.py`, bumpa pluginversionen, uppdatera den lokala marketplacen
   och kör `claude plugin update <namn>@<marketplace>` (kontrollera namnen med
   `claude plugin marketplace list`).

**B. Domarna in i `references/`.** `FEEDBACK.md` läses ovillkorat, men en regel som bara bor
där hittas sent. Kontrollera först om de redan finns (grep), lägg annars in:
- F-023 (case- och processtext i två stycken, orsaken före valet, bortval som alternativ som fanns,
  tre skillspass) i `copy.md` eller `copy-gate.md`.
- F-024 (en dominerande referens och minst två dokumenterade lån) i `reference-lock.md`. `inspo-mcp.md`
  rad 40 täcker triangulering men inte kravet på dokumenterade lån i låset.
- F-025 andra halvan (ett ytmått får aldrig uppfyllas genom att förstora en lågupplöst bild, nya
  skarpa bilder i 2× skala) i `imagery-kit.md` eller `layout-and-space.md`.
- F-026 (varje sektion bär ett grepp som går att säga i en mening) i `invention.md` eller
  `component-cookbook.md`.

**C. A/B-körningen (det som avgör delmål 8 i `GOALS.md`).** Kör samma brief och copy
(`tests/alunix-r8/runs/V3d/index.html` är copyfacit) med kedjan påslagen som arm B mot V3f som arm A.
Husets uppställning (CARL design-beslut 2026-09-06): separata `claude -p`-processer, inte
Agent-verktygets subagenter. Launcher: `tests/alunix-ab-r6/run.py`; kontrollera först om
`tests/alunix-ab-r7/` redan innehåller en liknande körning. Utlägget är två Opus-byggen, så fråga
Anton. Frågan att besvara: når ett bygge med Inspo, UI-skills och GSAP+Lenis V3f:s nivå på
första försöket, utan de sex rundor V3f behövde? Kontrollera efteråt vilken modell som faktiskt
byggde (`modelUsage`), enligt `~/CLAUDE.md` § Delegering.

**D. Verifiering som saknas.**
1. Ett provbygge där Inspo anropas, och kontroll att en `mcp`-rad syns i `design-report-*.md`.
2. `end:'bottom bottom'` för sidans sista pinnade element: kontrollera att regeln står i `motion.md`.
3. `runs/V3f/verify_motion.py` kraschar när 12+ sidor öppnas i en webbläsare. Starta en ny
   webbläsare per kontroll.
4. Bildrutetiming (p95 33 ms för V3f, 16,8 ms för V3g:s showcase) är mätt headless. Mät i en
   riktig webbläsare på Antons maskin innan siffran räknas som bevis.

**E. Beslut som bara Anton kan ta.**
1. Hōrai steg 1 i V3g-showcasen: bandet visar mitten av ett stort H över suddigt bröd. Annan
   detalj, eller inget band i det steget?
2. Calyx vid 1280×800: bandet döljs eftersom första steget är längst, så kolumnen slutar i vit yta.
3. Copy-diffen flaggar `ALUNIX` (topplist + footer) och `kontakt@alunix.se` (topplist + kort) som
   dubbletter i V3f. Acceptera som ordmärke respektive navigation, eller ta bort en av varje.
4. De sex besluten i `tests/alunix-r8/runs/V3g/AUDIT.md` och R7b-klickregressionen i V3g
   (`PROMPT-V3g-R7b.md`: Hōrai startar först efter 1,5–2,5 s i tre av fem körningar).
5. Vilket repo som äger `lenis`- och `gsap-*`-skillsen (se A).

**F. Städning och rutin.**
1. **Boardkopian.** Boarden läser `board/cells/<V>-r8/`, en kopia, inte `runs/<V>/`. Byggarna skriver
   till `runs/`, så previewen visade en gammal V3g tills jag synkade den 2026-10-01. Gör
   synken till sista steget i varje byggorder, eller skriv `sync_board_cell.py` som kopierar
   `index.html` och `assets/` och verifierar med `cmp`. Raden finns i vaultens `MEMORY.md`.
2. Ospårade scratch-filer i repots rot som inte är mina och inte raderats: `.scratch_fakta.md`,
   `.scratch_mal.md`, `plane21-*.json`, `.shots/`, `.claude/settings.local.json.bak`. Fråga Anton
   innan något tas bort (förstörelseskyddet i `/conclude`).
3. Skärmbilderna under `runs/V3f/shots/` och `runs/V3g/shots/` (ca 1 GB) är medvetet inte
   incheckade. Bestäm om de ska ligga utanför git eller i en arkivmapp.

## 8. Pushläge och vad som är incheckat (kontrollerat 2026-10-02)

Inget är pushat, och push kräver Antons uttryckliga go-ahead varje gång (global regel).

| Repo och gren | Läge | Det som rör den här handoffen |
|---|---|---|
| `anti-slop-design`, `design-rework-v3` | **Ingen uppströmsgren, har aldrig pushats.** Remote: `origin` = `github.com/oloflun/anti-slop-design`. Alla incheckningar är lokala | `623e261` (session 2026-10-01: V3f, handoff, V3g R8, F-023–F-026, plan). Tidigare `b96c250` (designkedjan v5, V3g-showcase). Plugin 1.1.0: `19b616e`, `1cf73b8` |
| `super-intelligence`, `design-system-v2` | 20 incheckningar före `origin/design-system-v2` | `47d5528`: `lenis` 0.11.0. Inga `gsap-*`-skills i paketet |
| `super-intelligence-public`, `main` | 1 lokal incheckning, inte pushad | `48f2d83`: tre filer som ändrats av andra sessioner (`hooks/brief-context.py` och två principles-skills), inte Lenis. Dessutom andra väntande ändringar i arbetsträdet (bl.a. borttagna `design-*.py`-hookar) som inte är mina och inte stagade |
| Installerat plugin (lokalt) | `anti-slop-design` 1.1.0 från den lokala marketplacen | Behöver ingen push för att fungera lokalt. Bara `design/`-skillen och fyra till ingår, inte `lenis`/`gsap-*` |
| Vaulten (`oloflun/anton-vault`) | `VaultAutoSync` var 15:e minut | `MEMORY.md` och `MEMORY-FULL.md` uppdaterade |

Skillen `lenis` och de åtta `gsap-*` är **live** och används av alla lokala sessioner nu
(`~/.agents/skills/` är kopplad till `~/.claude/skills/`). Det som saknas är bara distributionen.

## 9. Läget för bygget (V3f efter R6, V3g efter R8b)

**Byggt och verifierat i pixlar av leaden:**
- Rubrikerna står stilla och hela i ≥ 40 vh.
- Väljaren visar två skarpa, utzoomade case med hover.
- Valet låser in besökaren i en pinnad showcase. Den levande sajten scrollas genom sina ankare
  (V3d:s `measureCase`/`caseY`, porterade), och en liggare fäller ut texten på andra sidan.
- Kontakten är "kortet lämnas över": heron speglad, kortet vänds av besökaren och vänder sig
  självt vid 0,7.

**Öppet:**
1. Copy-diffen flaggar två dubbletter som specen införde: `ALUNIX` (topplist + footer) och
   `kontakt@alunix.se` (topplist + kort). Beslut för Anton: acceptera som ordmärke respektive
   navigation, eller ta bort en av varje.
2. `verify_motion.py` kraschar när den körs som en enda webbläsare med 12+ sidor. Den bör
   stänga sidor och starta en ny webbläsare per kontroll. Sidan själv läcker inte (se
   `KEDJA.md` R6).
3. Byggarens bildrutetiming (p95 33 ms) är mätt headless. Mät i en riktig webbläsare på
   Antons maskin innan den räknas.
4. Showcasen väljer Calyx som förval. Om besökaren aldrig väljer ser hen aldrig Hōrai. Det är
   Antons avsikt ("vissa kommer scrolla tillbaka upp"), men värt att mäta i verklig
   användning.

**Rundor och kostnad:** R1–R2 komposition, R3–R4 rörelse, R5–R6 läsbarhet, casevalet och
kontakten. Sex rundor, alla med leadens pixelgranskning mellan dem. Varje runda hittade fel som
byggarens egen verifiering hade godkänt, i R4 och R6 också fel som leaden rättade själv.

**V3g efter R8 och R8b (2026-09-29 till 2026-10-01):**
- Showcasens högerkolumn är en sammanhängande yta utan rutor. Stegen har rubrik, ingress och
  brödstycke. Copyn står i `runs/V3g/COPY-R8.md` och har gått genom copywriting, copy-editing och
  humanizer-svenska. Luppen är ett band i kolumnens bredd som aldrig rör sajten och döljs under
  160 px höjd.
- Uppmätt: ingen text klipps i något steg vid 1280, 1440, 1920 och 390. Showcasens p95 är 16,8 ms
  mot baslinjens 18,2 ms. 0 px överflöd och 0 konsolfel.
- Byggaren flaggade själv ett stort H som läses dåligt i bandet (Hōrai steg 1). Se § 7 E.
- `section_probe` föll i 2 av 4 körningar på `#exempelcase`, en sektion ingen rörde. Samma probe
  föll på den oförändrade sidan i en av sina körningar. Orsaken är Calyx-iframens första rendering
  (känd monteringskostnad från R7), inte R8.
- Boardens V3g-cell synkades 2026-10-01 och är byte-lik `runs/V3g/index.html`.
