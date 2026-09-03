# Session Log — 2026-09-03

## Session Summary
Design rework v3 planerades (icm-architect, egen läsning av alla externa repon) och genomfördes i sin helhet: hookarna fyrar bara i armade designsessioner, en tillgänglighetsskill med tre granskaragenter, reference lock + designkatalog (localhost, GitHub-repo som databas), Step 2b med scroll-grammatik och bake-off-board, visuell kritik som positiv port, nio uppdaterade emil-skills, och SlopMonster som hybrid i copy-kedjan. Varje tillägg A/B-testades blint mot baslinjen och bedömdes på pixlar; resultatet ligger i `tests/ab/*/verdict.md` och i loggboken "Design Rework v3" (artifact). Anton beslutade 1A (katalogen i GitHub-repo) och 2A (det som körs är kanoniskt, repot är spegel).

## What Changed

### Files Created
- `scripts/sync-from-live.py` — speglar vault-skills + super-intelligence-hookar in i repot; `--check` är verify-kontrollen "repo == live".
- `tests/intent_corpus.jsonl` (40 prompter), `tests/a11y/broken.html`, `tests/scroll/broken.html`, `tests/shotgun-smoke/`, `tests/ab/README.md` och `tests/ab/{02,03,05,06,07,08,09,10,11,K}*/` (byggen, skärmbilder, verdict.md).
- Vault-skills: `a11y-audit/` (SKILL, principles, report-template, tre skript), `design-catalog/`, `slopmonster/` (vendorad), åtta emil-skills (animate, review-animations, improve-animations, find-animation-opportunities, prototype, apple-design, animation-vocabulary, pick-ui-library).
- `design/references/`: `reference-lock.md`, `photo-sources.md`, `shotgun.md`, `scroll/{README,grammars,devices,feel-and-fingerprint}.md`, `verbs/critique.md`, `verbs/review.md`, `upstream/` (sju vendorer + MANIFEST + INDEX + slopmonster).
- `design/scripts/`: `board.py`, `scroll_verify.py`, `scroll/` (motorn byte-identisk).
- `~/.claude/agents/design-a11y-reviewer.md`, `design-critic.md`, `design-heuristics.md` (Sonnet, läs-bara).
- Vault: `wiki/projects/_index/design-fingerprints.md` (registret, seedat med sju sajter).
- Nytt repo `oloflun/design-catalog` (privat): Next.js på 127.0.0.1:4610, `catalog/<slug>/entry.md` + bilder, `scripts/{capture,describe,index,query,seed,from_image}.py`, `sync.sh`, `dev.cmd`.
- `~/.claude/plans/uppgift-design-rework-v3-validated-hammock.md` (planen) och `plans/2026-09-03-design-rework-v3.md` (projektkopia med status).

### Files Modified
- `super-intelligence/hooks/design-*.py` och `design_hook_lib.py` — classify()/arm()/armed(), villkorad route/verify/stop, gap = kod-starka craft-routes som varken laddats eller lästs, avsnitt 6 alltid, sessionsscope; `scripts/export-agents.mjs` läser vaultkopian; `skills/design` synkad.
- `verify-design-system.py` — 139 kontroller mot `super-intelligence/hooks` + `hooks.json`, corpus, arm/disarm, spegelkontroll, UTF-8.
- Vault `design/SKILL.md` (471 → 562 rader): AI-default-regel + generic-default-test, briefsäkring, läsbudget, Step 1b lock + katalog, Step 2b, Step 3 animate/pick-ui-library/a11y, Step 4 gates 1–91 + reveal-guard, Step 5 pass 9–12, verbtabell, exit bar, referensindex. Även `skill-orchestration.md` (v3-avsnitt), `gates.md` (89–91), `copy-gate.md` (SlopMonster-hybrid), `hallmark/SKILL.md` (disable-model-invocation), `polish/SKILL.md` (teach → init), `emil-design-eng` (uppströms body).
- `~/.carl/carl.json` DESIGN: recall 52 fraser + exclude 18. `~/.claude/settings.json`: frontend-design-pluginet av, `skillOverrides` super-intelligence:design = user-invocable-only. `.claude/launch.json`: design-catalog, shotgun-board.
- `anti-slop-design.md` (hubben, v3-avsnitt), `GOALS.md` (delmål 5–7 klara, positiva porten införd), `attribution/UPSTREAMS.md` (§6 emil, §7 SlopMonster), `.gitignore` (sync-skriptet spårat).

### Files Moved/Deleted
- Inget raderat. Backup före allt: `~/.agents/_backups/design-rework-v3-20260903-023344/`.

## Decisions Made
- **Live är kanoniskt, repot spegel (2A):** vault `.agents/skills` + `super-intelligence/hooks` är källan; `sync-from-live.py` + verify-check. Skäl: det är de kopiorna som faktiskt körs (plugin-cache + junction); repot hade drivit tusen rader.
- **Katalogen i ett GitHub-repo, localhost först (1A):** innehåll bor i repon och läses live (chatt via GitHub-connector, Claude Code via git); Vercel + OAuth blir ett senare steg; `claude -p` ersätter API-nyckel.
- **Arm/disarm i hookarna:** en high-prompt eller Skill(design…) armar sessionen; allt nedströms är villkorat utom kontraktsgaten på låst DESIGN.md. Skäl: fem dokumenterade falska positiva på nakna nyckelord.
- **frontend-design inte som skill, två regler portade:** AB09 visade att paletten lämnade AI-defaulten men bygget tappade reveal-guarden; som skill blev den ett tredje direction-huvud.
- **designpowers: bara granskarna:** byggagenterna sätter direction (taste-profil, egen DESIGN.md-form); de tre granskarna som Sonnet-subagenter hittade 7/7 planterade + 9 verkliga fynd (AB04).
- **scroll-craft-motorn opt-in per grammatik, aldrig blint:** AB06 visade tre pinnade akter som scrollade bort när byggarens CSS skrev över `.sc-stage`; grammatik, känslokurva, fingerprint och scroll_verify tas in.
- **SlopMonster som hybrid:** kedjan skriver (svenska + gate 75), deslop.py grindar engelska strängar, fyra radkällor + never-invent-proof in i copy-gate; rival-cleanse valfri.
- **hallmark tystas (disable-model-invocation), inte avinstalleras;** super-intelligence:design blir user-invocable-only.

## Context & Discussion
- Antons skärmbilder (bake-off med stiltabbar och två motorer; katalogkort med DNA-rad, chips, image recipe, COPY BRIEF/COPY IMAGE PROMPT) blev förlagan för boarden och katalogen.
- Anton bad om frågor i klartext i chatten (AskUserQuestion föll), och att SlopMonster testas efter allt annat.
- Det inbyggda `/design` (Claude Design-canvas, Claude Code 2.1.234+) skuggas av den personliga `design`-skillen enligt dokumenterad namnregel; ingen konflikt.
- Två Hallmark-referensfiler (`custom-theme.md`, `macrostructures.md`) skiljer sig från uppströms HEAD för att uppströms ändrats; verify rapporterar 137/139 ärligt.
- Blinda one-shots ur samma v3-kedja gav två olika bra sidor (K1 med fotoupptakt, K2 typografisk med en trasig bild); en mellanversion tappade en briefsektion under referenslasten, vilket gav briefsäkring + läsbudget i SKILL.md.

## Open Threads
- Den nya hookkoden kör inte i sessioner förrän `super-intelligence` pushas (kräver Antons go-ahead) och plugin-cachen uppdateras med `claude plugin marketplace update` och `claude plugin update`. Tills dess fyrar den gamla Stop-rapporten (ROUTE GAP-larm) i varje session.
- `anti-slop-design` ligger committat på grenen `design-rework-v3` (inte main), opushat; merge till main är Antons beslut.
- Katalogens Vercel-steg (OAuth-app, tre env-värden, Actions-nyckel) enligt planens avsnitt 8b.
- CARL DESIGN-besluten för v3 är inte loggade i carl.json än; görs när hookarna är i drift.
- `BLOCKS.md` är på 22 000 tecken mot ett tak på 3 000; en separat städning (flytta lösta block äldre än tre månader till BLOCKS-RESOLVED.md) behövs, inte gjord här.
- `tests/ab/08-emil/runab/` och `tests/ab/smoke/` innehåller halvfärdiga run_ab-körningar (harmlösa); `run_ab.py` faller på helsides-screenshot i vissa fall.

## Cross-Project Handoffs
- super-intelligence: hookar + export-agents committade på `design-system-v2` (f6e8838); VERSION/CHANGELOG-bump och export-to-public görs i conclude-steget. Ingen separat handoff-fil.

## Current State After This Session
Designsystemet är i v3: tyst utanför designjobb, bevisat bättre än baslinjen på pixlar i tio A/B-tester, och dokumenterat i hubben, GOALS, loggboken och verdict-filerna. Nästa session bör börja med push av super-intelligence och cache-uppdatering så den nya kedjan faktiskt körs, sedan en riktig (icke-blind) designsession som kör Step 2b-bake-offen och Step 5-looparna skarpt.

<!-- session-state
date: 2026-09-03
type: infrastructure
files_created:
  - scripts/sync-from-live.py
  - tests/ab/README.md
  - plans/2026-09-03-design-rework-v3.md
files_modified:
  - verify-design-system.py
  - anti-slop-design.md
  - GOALS.md
decisions_made: 8
open_threads: 6
handoffs_pending:
  - target: super-intelligence
    topic: push hooks v3 + plugin cache update
priority_changes: true
status_updated: true
goals_updated: yes
next_session_focus: "Pusha super-intelligence och uppdatera plugin-cachen så hook v3 kör; kör en skarp designsession med bake-off och Step 5-looparna"
session-state -->

## Runda 2 (samma dag, efter "underwhelming" och "för snarlika")

- **Inventering:** oanvända uppströms: impeccables dialar (bolder/delight/overdrive/typeset/colorize), scroll-crafts worlds.md, designpowers design-taste/inspiration-scouting/ui-composition/motion-choreography (+11 skills vendorade), designer-skills kompositionslagar (+26 vendorade), gpt-taste, imagegen. Sju spakar A/B-testade mot K1 + ett breddtest med fyra byggen under diversity contract; copy-jämförelsen renderad som sidor och fulltexter i loggboken.
- **Resultat:** fem av sju spakar (amplify, imagery pipeline, taste, gpt-taste, laws) ändrade inte banan: samma Unsplash-bukett, samma serif-över-foto. Rotorsak: fotopool på 19 bilder, registerdefault, house-physics-belöning för foto med typ över. Worlds-förordet in (med scrim-regel). Loopen (T17) rättar fel men lyfter inte intrycket. **Breddkontraktet gav fyra olika studior ur samma brief** (B2 och B4 rena; B1 ambitiös med tom remsa; B3 defaultnära) — in som default i Step 2b.
- **Kedjan ändrad:** kategoridefault sist på Tier 3; bake-off tilldelar tre register × tre grammatiker × tre världar med förbjudna syskondrag; fingerprint mot sessionens syskon; plansch/scrim-krav för typ över foto; `blankBands` i scroll_verify.py; shotgun.md fick "Diversity contract". Bevis: `tests/ab/compare-round2/`, `tests/ab/19-breadth/verdict.md`, `tests/ab/17-loop/verdict.md`.
- **Handpåläggning:** Unsplash API-nyckel (gratis) för riktig fotosökning; utan den konvergerar fotobyggen.
- **Avbrott:** sessionskvoten slog i mitt i runda 2 (nio agenter dog på 429); alla återupptogs efter reset utan förlorat arbete.

## Runda 3 (samma dag, copy-hybriden isolerad i två nya exempel)

Anton väntar fortfarande på Unsplash-nyckeln (ansökt). Han bekräftade att bredden är mycket
bättre, men höll fast vid att den gamla kedjans copy genomgående var bättre än SlopMonster rakt
av — problemet var att AB11 (kvist/florhuset) var det enda copy-exemplet, och det hade inte
körts mot de andra briefarna. Beställning: två helt nya, fristående exempel (inte en delad
jämförelse) som ställer den gamla kedjan mot den nya hybridkedjan (copy-gate.md:s Pass 1b +
svensk tell-lista, inte SlopMonster som fullständig ersättare — det beslutet stod redan fast
från AB11).

- **Två nya briefar**, medvetet olika register från allt tidigare (inget florist-, kvist- eller
  hantverksbrief återanvänt): `20-copy-hybrid-kajplats` (litet båtvarv, Fjällbacka, lokal
  tjänst) och `21-copy-hybrid-reglabok` (fakturerings-app för hantverkare, B2B-mjukvara).
- Fyra blinda Sonnet-agenter (en per brief x kedja), samma metod som alla tidigare A/B-test:
  ingen dialog, ingen research utanför briefen, bara Stage 1 (copywriting) + Stage 2
  (humanizer) för A, plus Pass 1b (radkälla) + svensk tell-lista för hand för B.
  Renderat till samma sidmall som AB11, skärmbildat, sida vid sida i
  `tests/ab/{20,21}-copy-hybrid-*/compare.png`.
- **Kajplats:** B vinner tydligt på heron — radkälla-disciplinen bytte ett generiskt löfte
  ("utan överraskningar") mot en fakta+rädsla-rad direkt ur briefen (14 platser, tak mot regn).
  Resten av sidan oavgjord.
- **Reglabok:** tvärtom. A:s hero ("inte vid köksbordet klockan tio") är den vassaste raden i
  hela testet; B ersatte den med en funktionslista plus en siffra, närmre SaaS-konventionen —
  precis den risk Anton varnade för. B:s äkta tillskott var en egen ärlighetsrubrik ("Vad
  Reglabok inte gör än") i stället för att gömma begränsningarna i ett stycke.
- **Slutsats:** hybriden är inte ett generellt lyft, den är två separata verktyg med olika
  träffsäkerhet. Radkälla-disciplinen (källa 1+2, fakta och rädsla) och
  ärlighets-tillägget (källa 3) håller streck. Källa 4 ("en rad som redan var bra") behöver
  väga tyngre i copy-gate.md så metoden inte skriver över ett redan starkt Stage 1-utkast —
  öppen post, se plans/2026-09-03-design-rework-v3.md.
- Full text (brief + A + B) och skärmbilder för båda i loggboken "Design Rework v3"
  (artifact), steg 14–15; verdict-filer: `tests/ab/20-copy-hybrid-kajplats/verdict.md`,
  `tests/ab/21-copy-hybrid-reglabok/verdict.md`.
