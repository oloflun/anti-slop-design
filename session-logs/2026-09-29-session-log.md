# Session Log — 2026-09-29 (pågick 2026-09-24 till 2026-09-29)

## Session Summary
Designsystemet fick Inspo-MCP, UI-skills och GSAP+Lenis som standardmotor för all rörelse. En lokal
fork av Inspo innehåller nu också katalogens 97 poster, och det installerade pluginet byggdes om slankt
(9,7 MB i stället för 3,4 GB). Showcasen i Alunix V3g byggdes om över sju rundor till en mjuk pin med
en textruta som tonar mellan stegen och en förstoringslupp ur kundsajten. En Opus-granskning av hela
sidan gav 15 HIGH-fynd, som rättades i R7. R7b, som skulle rätta en regression i klicket, avbröts av
kontots sessionsgräns.

## What Changed

### Files Created
- `~/.agents/skills/design/references/inspo-mcp.md`: guide för Inspo-verktyget och den lokala forken.
- `~/.agents/skills/design/scripts/section_probe.py`: mäter varje sektion på hela sidan och fallerar
  vid iframe-omladdning, vid refresh under scroll och vid sektioner som blivit sämre än baslinjen.
- `~/.agents/skills/design/scripts/motion/` (vendor: GSAP 3.15.0, Lenis 1.3.26).
- `scripts/inspo_import.py`: katalogens poster som seedrader i Inspo-forken.
- `scripts/build-plugin.py`: bygger det slanka pluginet `dist/plugin/`.
- `tests/hooks/test_mcp_gsap_routes.py`: 8 tester.
- `tests/alunix-r8/{showcase_probe,click_scroll_probe,browser_lock}.py`, briefs `PROMPT-V3g-R1…R7b.md`.
- `tests/alunix-r8/runs/V3g/`: kopia av V3f, ombyggd. Innehåller `SHOWCASE-SPEC.md`, `EFFECTS.md`,
  `AUDIT.md`, `reviews/opus-*.md` och `RAPPORT.md`.
- `~/inspo` (lokal klon av Nutlope/inspo, branch `house`; ingen remote utöver upstream).
- Minnesfiler: `report-tool-stops`, `headless-browsers-only`, `track-every-requested-deliverable`,
  `model-order-enforced-in-builders`.

### Files Modified
- `~/.agents/skills/design/`: `SKILL.md` (Inspo i steg 1b; samma modellklass för subagenter),
  `reference-lock.md`, `motion.md`, `scroll/devices.md` (motorn och laststödjande regler),
  `skill-orchestration.md` (UI-skills-tabellen, bara headless), `component-routing.md` (GSAP-rutter).
- `hooks/design-vision-track.py`, `design-stop.py`, `hooks.json` (MCP-händelser i ledgern).
- `design-catalogue/FEEDBACK.md`: F-019 till F-022.
- `.claude-plugin/marketplace.json` (källan är nu `./dist/plugin`), `scripts/sync-from-live.py`,
  `.gitignore`, `verify-design-system.py` (ocommittad, delas med en annan sessions ändringar).
- `~/CLAUDE.md` § Delegering: subagenter körs på samma modellklass, Fable delegerar till Opus, ingen
  delegering till lägre klass utan Antons tillstånd.
- `~/.bashrc`: DeepSeek-raderna borttagna (säkerhetskopia `~/.bashrc.bak-deepseek-20260925`).
- `~/.claude.json`: MCP-servern `inspo` pekar nu på den lokala forken.
- `.claude/settings.local.json`: V3e/V3f-isoleringen borttagen (sparad som `settings.local.v3*.json`).

## Decisions Made
- **GSAP+Lenis är standardmotor för all rörelse (CARL design-012).** Scrollcraft behålls bara för
  sidor som redan är byggda på den. Antons order.
- **Inspo-forken är lokal och kräver ingen nyckel.** Våra rader ligger i en separat, gitignorerad
  fil så att upstream kan dras in utan konflikter.
- **Skyddade effekter och en regressionsgrind.** Varje körning har en `EFFECTS.md`, och
  `section_probe` körs på hela sidan. Orsaken var att tesrubriken försämrades av en omladdningsloop
  i iframen, utan att någon ändrat den.
- **Pluginet byggs slankt.** Källan `.` kopierade hela repot, 3,4 GB per version.
- **Samma modellklass för subagenter.** Antons regeländring efter att en Opus-byggare lämnat 85 % av
  arbetet till Sonnet.

## Context & Discussion
- Anton underkände i ordning: rubrikens storlek i rutan (F-019), att scrollen gick för fort (F-020),
  regressionen i tesrubriken (F-021) och de gröna strecken i stegskalan (F-022). Stegskalan var
  leadens egen spec och godkändes av leaden själv.
- Synliga webbläsarfönster (headed) staplades på skärmen och kraschade maskinen. All verifiering
  körs nu headless, en i taget, med lås och en vakt som stänger synliga fönster.
- Disken nådde 201 MB ledigt och RAM tog slut. Den största källan var cognee-backfillen och
  plugin-cachen. Cognee rörs inte, enligt Antons order.

## Open Threads
- **R7b är inte klar.** Klicket på Hōrai startar i tre av fem körningar först efter 1,5–2,5 s,
  eftersom Hōrai laddas vid klicket. Kör om `PROMPT-V3g-R7b.md` med Opus och `R8_NO_SUBAGENTS=1`,
  och verifiera sedan med `click_scroll_probe` fem gånger.
- **R7:s visuella rättningar är inte granskade i pixlar av leaden:** iframen i full bredd,
  tesrubriken och kontrasten. Det görs efter R7b.
- **Sex beslut väntar på Anton:** casebyte inne i pinnen, ankarlänkar i topplisten, en gemensam
  reveal-profil, prisets storlek och momsrad, kontaktens tomma cell, och en riktig bokningslänk
  (se `AUDIT.md`).
- **`verify-design-system.py`** har mina ocommittade kontroller ovanpå en annan sessions ändringar.
- **Katalogens frontmatter-parser** delar trait-värden vid kommatecken (42 av 97 poster). Det finns
  ett förslag som separat uppgift.
- `design-rework-v3` är opushad, och push kräver Antons klartecken.

## Cross-Project Handoffs
None this session. CLAUDE.md-regeln gäller globalt och är redan skriven i källfilen.

## Current State After This Session
V3g har en mjuk och verifierad showcase (p95 16,8–18 ms i alla sektioner), och Opus-granskningens
HIGH-fynd är rättade i R7. Klickregressionen och leadens pixelgranskning av R7 återstår. Designsystemet
och pluginet 1.1.0 är aktiva lokalt.

<!-- session-state
date: 2026-09-29
type: design-system + design-iteration
files_created:
  - C:/Users/Anton L/.agents/skills/design/references/inspo-mcp.md
  - C:/Users/Anton L/.agents/skills/design/scripts/section_probe.py
  - C:/Users/Anton L/anti-slop-design/scripts/build-plugin.py
  - C:/Users/Anton L/anti-slop-design/scripts/inspo_import.py
  - C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3g/AUDIT.md
  - C:/Users/Anton L/inspo/packages/db/src/house-screens.json
files_modified:
  - C:/Users/Anton L/.agents/skills/design/references/scroll/devices.md
  - C:/Users/Anton L/.agents/skills/design/references/motion.md
  - C:/Users/Anton L/anti-slop-design/hooks/design-vision-track.py
  - C:/Users/Anton L/anti-slop-design/design-catalogue/FEEDBACK.md
  - C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3g/index.html
  - C:/Users/Anton L/CLAUDE.md
decisions_made: 5
open_threads: 6
handoffs_pending: []
priority_changes: true
status_updated: false
goals_updated: "skipped -- tidsbrist vid avbrott; målbilden (AUDIT.md-beslutet) oförändrad"
next_session_focus: "Kör om R7b (klickregressionen), granska R7 i pixlar, ta Antons sex beslut ur AUDIT.md"
session-state -->
