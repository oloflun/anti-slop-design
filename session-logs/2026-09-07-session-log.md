# Session Log — 2026-09-07

## Session Summary

Anton underkände r6-boarden helt (ingen scrolleffekt syntes, K1:s fönster fel, K2 "för
mycket", K3 slop, kedjan läste noll referenser) och bad om fyra saker: en ärlig
rotorsaksanalys, ett feedbacksystem så domarna styr nästa bygge, två nya Sonnet-orkestrerade
K1/K2-körningar (r7) med bevisad kedjefyrning, och Higgsfield för K1:s kamera-in-i-fönster-akt.
Allt genomfördes: sex rundor × två koncept, ett referensgolv i hookarna, en per-session-
läkning av en tävlingsbugg i ledgern, och en FEEDBACK.md där Antons domar blir regler.
Dagens del (efter kompakteringen): boarden visade sig fortfarande inte animera — grundorsaken
var Windows' Animationseffekter fortfarande av, vilket Anton eskalerade till en permanent,
global regel ("rörelse spelas alltid upp, oavsett inställningar") efter att jag lagt fram
tillgänglighetsavvägningen rakt. Genomförd i hela kedjan (motorn, båda byggena, `a11y-audit`
globalt). Sedan en grundlig kedjerevision på Antons begäran: en verklig bugg i Stop-hookens
sessionsscoping hittades och bevisades (inte gissad), två route-gap-orsaker skildes åt, och
`Skill(design-catalog)` visade sig aldrig ha kallats i något av byggena — min egen
runda-1-prompt gav filvägar direkt i stället för att köra skillets query-steg.

## What Changed

### Files Created
- `tests/alunix-ab-r7/CHAIN-AUDIT-2026-09-07.md` — full kedjerevision: Stop-hookens
  sessions-scoping-bugg (bevisad genom att köra hooken själv med rätt miljö), route-gap-
  analysen för `imagegen-frontend-web` och `impeccable layout`, alla tolv rundors
  skill-anrop och referensläsningar regenererade direkt ur de råa loggarna, och § 5:s
  detaljerade steg-för-steg-genomgång av vad som faktiskt kallades i K1/K2.
- `design-catalogue/FEEDBACK.md` — F-011 (rörelse-alltid-regeln, Antons exakta citat och
  beslut) och F-012 (scrollrörelsen fungerar nu men ser hackig/billig ut, öppen orsak,
  överlämnad till nästa session). Filen fanns redan från tidigare i sessionen (F-001–F-010).
- `tests/alunix-ab-r7/monitor/B-K{1,2}-r{1..6}.md` + `summary.md` — regenererade från de
  råa `--include-hook-events`-loggarna för att svara på "vad laddades exakt".
- (Tidigare i sessionen, före kompakteringen: `plans/jag-vill-att-du-shimmering-sketch.md`,
  hela `tests/alunix-ab-r7/`-katalogen — `run.py`/`monitor.py`-omslag, `concepts.md`,
  `PROMPT.md`, `rounds/*.md`, `RAPPORT.md`, `board/*`, `higgsfield/LOG.md`,
  `runs/B/K1/`+`runs/B/K2/` — och `skills/design/scripts/serve.py`.)

### Files Modified
**Idag (efter kompakteringen), rörelse-alltid-regeln (F-011):**
- `skills/design/scripts/scroll/scrollcraft.js` — `reduce` hårdkodad till `false`, aldrig
  längre läst från `prefers-reduced-motion`.
- `skills/design/scripts/scroll/scrollcraft.css` — hela `@media (prefers-reduced-motion:
  reduce)`-blocket (transform/parallax/wipe-neutralisering) borttaget, inte bara tomt.
- `skills/design/SKILL.md` — § Motion omskriven till rörelse-alltid-regeln, gamla
  reservläges-regeln kvar som historik (struken); shipping-gate-raden uppdaterad.
- `skills/design/references/house-physics.md` — samma regel, två ställen (allmän Motion-
  punkt + Editorial-print "Shared reveal").
- `~/.agents/skills/a11y-audit/SKILL.md` — global standing override: flaggar inte längre
  avsaknad av reduced-motion-stöd, i något projekt skillet körs i.
- `~/.agents/skills/a11y-audit/references/principles.md` — motsvarande princip struken
  (annoterad, inte borttagen — provenance bevarad).
- `skills/design/scripts/board.py` — `protocol_version = "HTTP/1.1"` + `image/webp`-
  mimetype (samma fix som `serve.py`, aldrig portad till boarden — orsakade riktiga
  `net::ERR_CONNECTION_RESET` på K1:s hero-foto); reduced-motion-varningsbannern borttagen
  (missvisande nu när rörelsen alltid spelar).
- `hooks/design-stop.py` — exit-bar-kravet om en separat reduced-motion-skärmdump borttaget
  (fanns inget kvar att verifiera separat); `_is_reduced_shot` kvar som dokumenterat oanvänd.
- `tests/alunix-ab-r7/runs/B/K1/{scrollcraft.js,script.js,scrollcraft.css}` och
  `tests/alunix-ab-r7/board/cells/K1-2/{samma tre filer}` — samma `reduce=false`-patch och
  CSS-borttagning applicerad på det redan byggda K1.
- `tests/alunix-ab-r7/runs/B/K2/{scrollcraft.js,index.html,scrollcraft.css}` och
  `tests/alunix-ab-r7/board/cells/K2-2/{samma tre filer}` — samma patch; K2:s inline-skript
  hade dessutom en live `matchMedia`-listener och en egen `*{transition:none!important}`-
  CSS-killswitch, båda borttagna.
- `plans/2026-09-03-design-rework-v3.md` — "In Progress" uppdaterad tre gånger idag:
  motion-always-fixen klarmarkerad, kedjerevisionen klarmarkerad, F-012 (hackig rörelse)
  skriven som öppen post för nästa session.
- `scripts/sync-from-live.py` körd (inte redigerad) — mirrorade de sju skill-filerna +
  `.claude/hooks/design-stop.py` från vaultens live-kopia in i repot; drift bekräftat noll
  efteråt.

**Tidigare i sessionen (före kompakteringen), sammanfattat — se
`tests/alunix-ab-r7/RAPPORT.md` för fullständig detalj:**
- `hooks/design_hook_lib.py`, `design-gate.py`, `design-intent.py`, `design-vision-track.py`,
  `design-telemetry.py`, `design-session-start.py` — referensgolvet, per-session-läkning av
  en delad-tillstånd-race, ny `ref-read`-händelse, scroll-route-regel.
- `skills/design/references/component-routing.md` — scroll-routningsregeln.
- `skills/design/references/skill-orchestration.md` — § 12 "Delegated builds".
- `design-catalogue/TASTE.md` § 4.8 — rörelse som auktoritet inuti ett set-piece.
- `verify-design-system.py`, `tests/intent_corpus.jsonl` — nya kontroller för allt ovan.
- `.claude/launch.json` — `alunix-board-r7` (port 4625).
- `GOALS.md` — changelog för r7.

### Files Moved/Deleted
Inga. Den gamla, ofixade board-processen på port 4625 (PID 28732) lämnades medvetet igång på
Antons begäran ("Låt den gamla vara så jag kan se skillnaden") — den fixade versionen körs
parallellt på port 4626.

## Decisions Made

- **Rörelse spelas alltid upp, permanent, globalt (F-011):** Anton bad först om en fix för
  sin egen granskning ("vi behöver animera oavsett inställningar"). Jag lade fram
  avvägningen rakt — det är en medveten avvikelse från tillgänglighet för besökare med
  vestibulära besvär, inte en bugfix — och frågade om det gäller bara hans granskning eller
  den publicerade sajten för alla besökare, och om det ska vara projekt- eller systemomfattande.
  Svar: "B, och gör det till standard globalt som permanent override för all accessability
  audit." Beslutet gäller alltså `a11y-audit`-skillet globalt, inte bara Alunix. WCAG 2.3.1
  (blinkgräns) är opåverkad — en säkerhetsgräns, inte en preferens.
- **`board.py` får samma HTTP/1.1-fix som `serve.py`:** upptäcktes som en riktig, separat
  bugg (inte relaterad till reduced motion) under diagnosen av "scrollen fungerar inte" —
  boarden själv körde HTTP/1.0 och tappade WebP-svar under Chromium, exakt samma kända bugg
  som `serve.py` byggdes för att lösa åt cellernas egna byggen, men aldrig portad till boarden.
- **Stop-hookens sessions-scoping-bugg rapporteras men fixas inte än:** hittade och bevisade
  (körde hooken själv med rätt miljövariabel, jämförde mot faktiskt loggad data) att
  `scope_to_session()` faller tillbaka till att räkna alla sessioner när hook-subprocessen
  inte får samma `CLAUDE_CODE_SESSION_ID` som Bash-verktyget ser. Fixen (läs `session_id` ur
  event-JSON:en) är föreslagen men medvetet inte gjord — rör kärnmekanismen bakom hela
  referensgolvet, och jag ville lägga fram bevisen för Anton innan jag rör den igen.
- **`imagegen-frontend-web`-gapet bedöms som (troligen) korrekt, inte en bugg:** regeln
  triggar på vilken `<img>`-tagg som helst, men skillet är till för att GENERERA nya
  referensbilder, inte placera redan inköpt riktigt fotomaterial (allt K1/K2 använder).
  Rekommendation: precisera villkoret, inte tvinga fram anrop som skulle vara fel där.
- **`impeccable layout`-gapet är ett namnfel, plus en öppen miljöfråga:** skillets riktiga
  namn är `impeccable` (ett ord); routningstabellen har fel namn. Djupare, obesvarad fråga:
  är `impeccable` överhuvudtaget laddningsbart i den headless-miljö byggarna körs i?
- **`Skill(design-catalog)` kallades aldrig — ägt av min egen prompt, inte byggarna:**
  runda-1-prompten gav byggarna exakta filvägar att läsa direkt i stället för att instruera
  dem att köra `Skill(design-catalog)` (som internt kör `query.py --category/--register/
  --grammar` för att SÖKA fram kandidater). Jag hade redan valt entries själv i `concepts.md`
  och kringgick därmed skillets egen urvalsmekanism, inte bara verktygsanropet.

## Context & Discussion

- Anton bekräftade explicit: "Låt den gamla vara så jag kan se skillnaden" — den ofixade
  board-processen (port 4625) ska INTE dödas, den fixade versionen (port 4626) är parallell,
  inte en ersättning, tills han själv jämfört.
- Två `AskUserQuestion`-anrop gav "Tool result missing due to internal error" igen den här
  sessionen (samma mönster som redan står i USER.md, 2026-08-29) — löst genom att skriva
  frågorna i klartext direkt i svaret, precis som den befintliga regeln säger.
- Ett `Stop-Process`-anrop (för att döda en gammal python.exe som höll port 4625) blockerades
  av auto-mode-klassificeraren. Löst genom att helt undvika åtgärden — pekade Browser-panelen
  direkt på den redan körande processen i stället för att döda och starta om.
- Anton höll mig strikt till avgränsningen flera gånger: "Gör inget arbete själv, förbered
  för att lämna över till nästa agent" (diagnosfasen av scroll-buggen) följt senare av ett
  tydligt "Okej, då är det det vi behöver göra" som gav grönt ljus att implementera. Viktig
  läxa: skilj tydligt mellan "undersök och rapportera" och "bygg det" i samma tråd — Anton
  växlar läge explicit och förväntar sig att jag respekterar vilket läge som gäller just nu.
- Kedjerevisionen (på Antons uttryckliga begäran, "gräv vidare i ALLT som inte laddades")
  krävde att jag körde om `monitor.py` mot de råa, oroterade `--include-hook-events`-
  loggarna i stället för att lita på den delade `.impeccable`-ledgern, som visade sig vara
  opålitlig för sammanfattningar över tid (roterar/rensas, blandar sessioner). Detta är en
  metodologisk lärdom värd att bära vidare: **den delade ledgern är bra för mekaniska
  gate-beslut i nuet, inte som historisk sanning senare** — de råa per-runda-loggarna är det.
- Min tidigare gissning att två sessions-ID:n (`4521eca7`, `0468df01`) i ledgern var
  orelaterade vault-synk-processer var FEL — de är K2:s respektive K1:s riktiga sex-rundors
  byggsessioner. Rättad direkt i CHAIN-AUDIT-filen med källhänvisning (monitor.py:s egen
  matchningslogg) i stället för att låta felet stå.

## Open Threads

- **F-012, hackig/billig rörelse (Antons uttryckliga överlämning):** rörelsen spelar nu upp
  korrekt men "ser hackigt och billigt gjort ut". Orsak inte fastställd. Nästa session: slå
  fast vilken cell/akt, mät (frame-times i K1:s 100-rutors push-sekvens, `--sc-p`-
  kontinuitet, om någon smoothing-logik villkorad på `!reduce` oavsiktligt påverkades av
  dagens `reduce=false`-patch), skriv den härledda regeln som en ny FEEDBACK.md-post.
- **Stop-hookens sessions-scoping-fix, inte gjord:** `current_session_id()` bör läsa
  `event.get("session_id")` (finns i hook-payloaden, bekräftat via loggfynd) som primär
  källa i stället för bara miljövariabeln. Litet, additivt, men rör kärnmekanismen bakom
  referensgolvet — kräver Antons OK innan det görs.
- **`component-routing.md`, tre öppna rättningar:** `imagegen-frontend-web`-villkoret bör
  preciseras (inte trigga på riktiga foton); `"impeccable layout"` bör bytas till
  `"impeccable"`; Anton behöver svara om `impeccable` överhuvudtaget är laddningsbart för de
  headless-byggare som kör kedjan, annars bör hela fallback-regeln pekas om mot `design`.
- **`Skill(design-catalog)`:** ingen kodändring föreslagen än — Anton bad om en förklaring,
  inte en fix, men nästa runda-1-prompt (om fler r7-liknande körningar görs) bör faktiskt
  instruera byggaren att köra skillet (och dess `query.py`-urval) i stället för att
  orkestreraren väljer entries åt den i förväg.
- **Kling-omtagning (17,5 credits) för K1:s videoartefakter** och **K2:s driftkontrast**
  (3,35:1 i ett 90px-band) — båda oförändrat öppna sedan tidigare i sessionen, Antons beslut.
- **Antons jämförelse V3 vs V3b (r5-boarden, port 4623)** — flaggad i standup-briefen som
  öppen, inte rörd denna session.

## Cross-Project Handoffs

None this session.

## Current State After This Session

Rörelse-alltid är nu en levande, verifierad regel genom hela kedjan (motorn, båda r7-
byggena, `a11y-audit` globalt) — bekräftad fungerande i en riktig reduced-motion-webbläsare,
inte bara i teorin. `board.py` serverar nu tillförlitligt (HTTP/1.1, ingen bildtappning). En
grundlig, bevisdriven kedjerevision finns skriven (`CHAIN-AUDIT-2026-09-07.md`) med tre
konkreta, oimplementerade förslag väntande på Antons prioritering. Nästa session äger F-012
(varför rörelsen ser hackig ut) som det mest konkreta öppna arbetet, plus tre mindre
routningsfixar och Stop-hook-buggen om Anton ger klartecken.

<!-- session-state
date: 2026-09-07
type: design-system-infrastructure-and-accessibility-policy
files_created:
  - tests/alunix-ab-r7/CHAIN-AUDIT-2026-09-07.md
  - design-catalogue/FEEDBACK.md
  - tests/alunix-ab-r7/monitor/B-K1-r1.md
  - tests/alunix-ab-r7/monitor/B-K1-r2.md
  - tests/alunix-ab-r7/monitor/B-K1-r3.md
  - tests/alunix-ab-r7/monitor/B-K1-r4.md
  - tests/alunix-ab-r7/monitor/B-K1-r5.md
  - tests/alunix-ab-r7/monitor/B-K1-r6.md
  - tests/alunix-ab-r7/monitor/B-K2-r1.md
  - tests/alunix-ab-r7/monitor/B-K2-r2.md
  - tests/alunix-ab-r7/monitor/B-K2-r3.md
  - tests/alunix-ab-r7/monitor/B-K2-r4.md
  - tests/alunix-ab-r7/monitor/B-K2-r5.md
  - tests/alunix-ab-r7/monitor/B-K2-r6.md
files_modified:
  - skills/design/scripts/scroll/scrollcraft.js
  - skills/design/scripts/scroll/scrollcraft.css
  - skills/design/SKILL.md
  - skills/design/references/house-physics.md
  - skills/a11y-audit/SKILL.md
  - skills/a11y-audit/references/principles.md
  - skills/design/scripts/board.py
  - hooks/design-stop.py
  - tests/alunix-ab-r7/runs/B/K1/scrollcraft.js
  - tests/alunix-ab-r7/runs/B/K1/script.js
  - tests/alunix-ab-r7/runs/B/K1/scrollcraft.css
  - tests/alunix-ab-r7/runs/B/K2/scrollcraft.js
  - tests/alunix-ab-r7/runs/B/K2/index.html
  - tests/alunix-ab-r7/runs/B/K2/scrollcraft.css
  - tests/alunix-ab-r7/board/cells/K1-2/scrollcraft.js
  - tests/alunix-ab-r7/board/cells/K1-2/script.js
  - tests/alunix-ab-r7/board/cells/K1-2/scrollcraft.css
  - tests/alunix-ab-r7/board/cells/K2-2/scrollcraft.js
  - tests/alunix-ab-r7/board/cells/K2-2/index.html
  - tests/alunix-ab-r7/board/cells/K2-2/scrollcraft.css
  - plans/2026-09-03-design-rework-v3.md
decisions_made: 5
open_threads: 6
handoffs_pending: []
priority_changes: false
status_updated: true
goals_updated: yes
next_session_focus: "F-012: varfor scrollrorelsen ser hackig/billig ut trots korrekt rendering -- mata frame-times och --sc-p-kontinuitet i K1:s push-sekvens"
session-state -->
