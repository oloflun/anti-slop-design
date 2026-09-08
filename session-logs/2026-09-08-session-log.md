# Session Log — 2026-09-08

## Session Summary

Planerade och byggde version 4 av designkedjan efter Antons missnöje med r7-utfallet: en
full genomgång av varje uppströmspaket där varje utelämnad skill motiveras ur filens eget
innehåll, ett obligatoriskt katalog-först-steg, ett prestandalager, en lyft-procedur, och
ett genereringslager med Higgsfield. Åtta av planens tretton infrastrukturuppgifter är
klara och verifierade, två delvis, tre orörda, och **hela Alunix r8-testet är inte
startat** — inget agent-team kördes och ingen designad sida producerades. Den öppna frågan
F-012 ("hackigt och billigt") stängdes med mätning i stället för hypotes och blev F-013.

## What Changed

### Files Created

- `skills/design/references/catalogue-first.md` — steg 0-proceduren: svep källorna,
  identifiera, extrahera, skriv posten, välj referenser mekaniskt, konsolidera, fingerprinta
- `skills/design/references/generation.md` — genereringslagret: modellrutt, kreditgrind,
  fallback-stege, vem som får generera, QA på rutnivå, provenance, en Never-lista
- `skills/design/references/performance.md` — budgeten (gate 93), laddning, rendering,
  rörelse, mätning, Never-lista
- `skills/design/references/motion-smoothness.md` — de två felen bakom "hackigt", regeln att
  bespoke rörelse läser `--sc-ps`, takt-avsnittet ur worldflight §7c
- `skills/design/references/lift.md` — sjupass-sekvensen som ersätter "kör polish"
- `skills/design/references/upstream/higgsfield/` — fyra vendorerade filer (scroll-scrub,
  scroll-scrub-asset-video, scroll-scrub-asset-css, game-textures) med F-011-annotering
- `skills/design/scripts/scroll/sc-smooth.js` — shimen som publicerar lerpad `--sc-ps`
- `skills/design/scripts/motion_probe.py` — mäter bildtid och värdekontinuitet
- `skills/design/scripts/perf_probe.py` — mäter budgeten
- `skills/design/scripts/preflight_taste.py` — taste-skillens mekaniska pre-flight
- `scripts/catalogue/select.py` — deterministiskt referensval, skriver `catalogue-select`
- `scripts/catalogue/sweep_raw.py` — omvänt index över `raw/` och `processed/`
- `scripts/catalogue/drift.py` — enum-, sektions- och extract-validering
- `tests/route_corpus.jsonl` — 20 routingfall
- `tests/hooks/test_reference_floor.py` — fem fall för referensgolvet
- `tests/hooks/test_generation_gate.py` — fyra fall för genereringsgrinden
- `tests/motion/{staircase,smooth}.html` + `sc-smooth.js` — rörelsefixturer
- `tests/perf/{heavy,clean}.html` + två PNG — prestandafixturer
- `tests/taste/bad.html` — taste-fixtur med planterade fel
- `tests/_shots/` — renderade skärmbilder av varje fixtur
- `HANDOFF-2026-09-08-designkedjan-v4.md` — överlämningen den här sessionen ombads skriva
- `C:\Users\Anton L\.claude\plans\trots-den-senaste-design-system-federated-raven.md` — planen

### Files Modified

- `hooks/design_hook_lib.py` — eventets sessions-id vinner över ärvd miljövariabel;
  `not_path` i routingmatchningen; `is_generation_tool`/`generation_fields`; `skill_status`
- `hooks/design-gate.py` — skärpt referensgolv (katalogval + per-slug-läsning + registret);
  genereringsgrind (budgetrad + `get_cost`-preflight)
- `hooks/design-vision-track.py` — `kind` per katalogfil; loggar genereringsanrop
- `hooks/design-stop.py` — genereringsavsnitt; gapet delas i tre hinkar
- `hooks/hooks.json` + `.claude/hooks/hooks.json` — två nya matchare för genereringsverktygen
- `verify-design-system.py` — lagade en krasch som fanns före sessionen; uppdaterade
  förväntningar för det skärpta golvet och F-011; divergensmedveten fidelitetskontroll;
  routingkorpusen inkopplad
- 23 filer under `skills/design/references/` — F-011-saneringen
- `skills/design-verify/SKILL.md`, `skills/a11y-audit/SKILL.md`,
  `skills/a11y-audit/scripts/{reflow,a11y_scan,tab_walk}.py` — F-011, omdöpta nycklar,
  `load`-fallback vid `networkidle`
- `skills/design/scripts/scroll_verify.py` — `--reduced-motion` borttagen
- `skills/design/references/assets.md` — regel 5 vänd; nytt avsnitt om kodning för scrub
- `skills/design/SKILL.md` — referensindexet får fem nya rader
- `skills/design-catalog/SKILL.md`, `design-catalogue/SCHEMA.md` — rätt serve-kommando och
  uppmätta designlang-flaggor
- `design-catalogue/FEEDBACK.md` — F-013 tillagd, F-012 stängd
- 25 filer under `design-catalogue/entries/` — mode-enum, sektionsnamn, `## Motion`, extract
- `tests/a11y/broken.html` — ett preferensoberoende oavslöjat element tillagt
- `scripts/catalogue/capture.py` — slug-validering
- `C:\Users\Anton L\.claude\settings.json` — fyra Higgsfield-skills avstängda

### Files Moved/Deleted

- `design-catalogue/entries/scroll_verify_out/` → `tests/_archive/scroll_verify_out/`
  (13 spårade PNG, flyttade i stället för raderade)
- Tre tomma skräpkataloger borttagna: `entries/--help`, `entries/-h`, och samma två i
  repo-roten. Alla ospårade och tomma; kontrollerade före borttagning.

## Decisions Made

- **Higgsfield körs via MCP:n, inte via skillsens CLI.** Skillsen anropar en egen binär med
  egen OAuth-inloggning och kan inte köra mot MCP-servern. Avgörande skäl: `get_cost` finns
  bara på MCP-sidan, och ingen av de åtta skillsen nämner kostnadskontroll överhuvudtaget.
  Skillsen bidrar med procedur och modellrutt.
- **`sync_agents` körs aldrig av kedjan.** Den installerar inget; den laddar upp Antons egna
  skills och en syntetiserad personlighetsfil till Higgsfields marknadsplats. Utåtriktad
  publicering av privat material är Antons beslut, inte ett kedjesteg.
- **Fyra Higgsfield-skills avstängda, inte raderade**, så `npx skills add` fortsätter
  uppdatera dem. Grunden är innehåll: `websites` bygger och deployar React på Cloudflare,
  `soul-id` kräver ansiktsfoton, `marketplace-cards` genererar påstående- och
  rekommendationspaneler, `product-photoshoot` förutsätter en produkt.
- **T2 skrevs om efter mätning.** Planens ursprungliga steg ("exportera hookarna till
  super-intelligence") hade återskapat en dubblering som togs bort medvetet 2026-09-04.
  Rätt riktning är den omvända: aktivera det här repot som plugin och ta bort de gamla
  designhookarna ur super-intelligences publicerade commit.
- **Sektionsanatomi i `preflight_taste.py` är en not, inte ett fel.** Att klassificera en
  sektions anatomi är en bedömning, och skriptets kontrakt är "räknat, aldrig bedömt". Den
  fällde referensbygget på fel grund.
- **En prob som kan godkänna en död sida är sämre än ingen prob.** `motion_probe` fick en
  `DEAD`-kontroll efter att den godkände ett kort som inte rörde sig alls.
- **`layout`-passet kördes inte på fixturerna.** De är instrument, inte produktytor; ett
  spacing- och hierarkipass på dem vore teater.

## Context & Discussion

- Anton bad uttryckligen om Opus-agenter för allt arbete i den här uppgiften, vilket
  åsidosätter CLAUDE.md:s standardregel om Sonnet-underagenter.
- Mitt under planeringen: **"läs de faktiska skillsen innan du utesluter något,
  beskrivningarna reflekterar inte alltid innehållet rättvist"**. Sex Opus-agenter läste
  därefter varje fil i varje uppström i sin helhet. Det gav fynd som beskrivningar aldrig
  hade gett, till exempel att `visual-catalog-matcher` (beskriven som "leverantörsfoton,
  lagerhyllor") innehåller exakt den tvåpass-procedur katalogen saknar för att identifiera
  en sajt ur en skärmbild.
- Higgsfield-uppdraget kom som ett separat meddelande efter att planen godkänts.
- Sessionen upptäckte att kedjans egen referenssida `sites/calyx.html` bryter mot gate 75
  tolv gånger och överflödar horisontellt vid 320 px. Båda är äkta fynd mot projektets egen
  måttstock. En separat uppgift är föreslagen för tankstrecken.
- Katalogen visade sig vara **helt svept** redan, tvärtemot planens antagande om en
  obearbetad råfil.

## Open Threads

- **T2, driftsättningen, blockerar allt hook-arbete.** Hookarna som kör i sessionerna är
  inaktuella plugin-cache-kopior från super-intelligence. Allt hook-arbete är korrekt i
  repot och bevisat med fixturer men inte i drift. Nästa steg kräver Anton: registrera
  `anti-slop-design` som marketplace och aktivera pluginet, och ta bort designhookarna ur
  super-intelligences publicerade commit.
- **Hela Alunix r8-testet är inte startat.** Ingen `tests/alunix-r8/`, inget agent-team,
  inga celler, ingen board. Prompterna finns i planens §8 men är aldrig använda.
- **Portlistorna i planens §2.4 och §2.5 är den stora återstående biten**, ungefär hundra
  namngivna portar från uppströmspaketen in i kedjans referensfiler.
- **T8, fingerprint-registret, har noll av 29 Alunix-rader.** Utan dem kan fingerprint-gaten
  inte skydda mot att ett nytt koncept liknar ett gammalt.
- **T10, granskarkontraktet:** tre agentfiler saknar dispositionsordet och den fjärde,
  `design-perf-reviewer`, finns inte.
- **T4, T11 och `scaffold_entry.py`** är orörda.
- `/review-animations` kan bara Anton köra. Kommandot mot shimen är
  `/review-animations skills/design/scripts/scroll/sc-smooth.js`.
- `sites/calyx.html` har tolv tankstreck och överflödar vid 320 px. Uppgift föreslagen för
  det första; det andra är inte adresserat.

## Cross-Project Handoffs

Ingen till ett annat projekt. Överlämningen den här sessionen ombads skriva är
`HANDOFF-2026-09-08-designkedjan-v4.md` i repo-roten och riktar sig till nästa session i
det här projektet.

## Current State After This Session

Kedjan har fått sitt mätlager: referensgolvet kräver ett mekaniskt katalogval, routingen
pekar bara på laddbara skills, och tre nya mätskript är bevisade i båda riktningarna.
`verify-design-system.py` går igenom med 191 kontroller mot tidigare 80, och den nådde inte
ens slutet innan sessionen började. Det som saknas är dels driftsättningen (T2), som gör
allt hook-arbete verkningslöst tills den är gjord, dels själva testet: **ingenting av det
som byggdes har ännu producerat en designad sida**, vilket var hela poängen. Nästa session
bör börja med T2 och därefter T8, eftersom båda blockerar r8.

<!-- session-state
date: 2026-09-08
type: infrastructure
files_created:
  - skills/design/references/catalogue-first.md
  - skills/design/references/generation.md
  - skills/design/references/performance.md
  - skills/design/references/motion-smoothness.md
  - skills/design/references/lift.md
  - skills/design/scripts/scroll/sc-smooth.js
  - skills/design/scripts/motion_probe.py
  - skills/design/scripts/perf_probe.py
  - skills/design/scripts/preflight_taste.py
  - scripts/catalogue/select.py
  - scripts/catalogue/sweep_raw.py
  - scripts/catalogue/drift.py
  - tests/route_corpus.jsonl
  - tests/hooks/test_reference_floor.py
  - tests/hooks/test_generation_gate.py
  - HANDOFF-2026-09-08-designkedjan-v4.md
files_modified:
  - hooks/design_hook_lib.py
  - hooks/design-gate.py
  - hooks/design-vision-track.py
  - hooks/design-stop.py
  - hooks/hooks.json
  - verify-design-system.py
  - design-catalogue/FEEDBACK.md
  - skills/design/SKILL.md
  - skills/design/references/assets.md
  - skills/a11y-audit/scripts/reflow.py
decisions_made: 7
open_threads: 8
handoffs_pending: []
priority_changes: true
status_updated: false
goals_updated: yes
next_session_focus: "T2: aktivera anti-slop-design som plugin och ta bort de gamla designhookarna ur super-intelligence, sedan T8 fingerprint-registret — båda blockerar r8-testet"
session-state -->
