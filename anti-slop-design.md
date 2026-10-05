---
title: Anti-Slop Design
type: project
status: active
project_slug: anti-slop-design
repo: C:\\Users\\Anton L\\anti-slop-design
updated: 2026-10-05
---

# Anti-Slop Design

## Nulage 2026-10-05

Alunix flik 7 (V3g R10, bara det Anton beställt) är live på https://alunix.se (308 till www) och https://www.alunix.se,
från det privata repot `oloflun/alunix-v3g` till Vercel-projektet `alunix`. Showcasens stegbilder är borttagna.
Boarden har flikarna 2, 6, 7, 8 (nytt koncept "Markören") och 9 (R10:s egna idéer). Designkedjan kräver nu
showcase-golvet och GSAP/Lenis-skills före första UI-skrivning (plugin 1.2.2). Domänflödet är skillen
`loopia-vercel-domain`. Öppet: Vercel-projektets Git-länk till `alunix-site`, Antons bedömning av flik 8/9,
push av `design-rework-v3`. Läs `HANDOFF-2026-10-05-ALUNIX-LIVE.md` först.

## Nulage 2026-10-01

Alunix V3f "Rutverket" (cellnät, GSAP+Lenis) är byggt och bedömt av Anton som bättre och mer unikt än V3d.
Processen, vad som bar, felen och en åttastegsplan för att föra in Inspo, UI-skills och GSAP+Lenis i designsystemet
står i `tests/alunix-r8/HANDOFF-V3f.md` (läs först). V3g:s showcase har copy i två stycken, utan rutor, och boardens
cell synkas efter varje bygge. Öppet: R7b-klickregressionen, Anton-besluten i `tests/alunix-r8/runs/V3g/AUDIT.md`
och push av `design-rework-v3` (opushad).

## Nulage 2026-09-22

Alunix V3d:s F1–F5 är åtgärdade, mätta och verifierade, och **sidan är publicerad**:
live på `https://alunix-three.vercel.app`, källan i det nya privata repot
`oloflun/alunix` med sidan självständig i roten (`index.html` byte-identisk med
cellen här, beroendena vendorerade på de absoluta sökvägar sidan redan frågar
efter). F3:s grundorsak var inte rubrikens egen ruta som förra sessionen antog —
`titelklipp.py` mätte `lost_px 0`, glyferna var hela — utan `.process-stick`,
arkets opaka sticky-plan, som täckte rubrikens sista rad eftersom stämpelrutan
hänger 133px nedanför kapitlets box.

**Ruttgapet — projektets egen mätpunkt 2 — är noll för sessionen.** `a11y-audit`
och `review-animations` laddades och kördes som procedur, med CARL-kontrollen mot
`tests/a11y/broken.html` först. a11y-passet gav ett HIGH-fynd som jag först
avskrev: `.process-kicker` mätte 7,38:1 i ett scrolläge men **3,64:1** i aktens
värsta, eftersom marken vandrar från accentblått till skiffer. Åtgärdat till
5,99:1. Full rapport i `tests/alunix-r8/runs/V3d/reviews/a11y-r24f.md`,
skuldbok i `.impeccable/a11y-debt.md`.

**Kvar:** F6/F7 (stora fyrkantiga block och den hårda vågräta skarven i
blå→ritning-övergången) är orörda; plan 067 § Verification är fortfarande
obetald; `<nav>`-landmärket saknas i sidhuvudet (två taggar, daterad skuld).
**`design-rework-v3` finns bara på den här disken — 29 commits före `origin/main`,
grenen finns inte på GitHub.** Det kräver Antons beslut; repot är publikt.

## 2026-09-20 — V3d byggd, nivan inte nadd

Alunix-landningssidans V3d-variant ar byggd med allt Anton bestallt (processtexten i vanster
spalt om ritningen, stampelruta i overgangen, Exempelcase nedskalat, prissektionen utan Young
Serif, egen kontaktsektion med formular). Antons dom 2026-09-20: punkterna ar gjorda men nivan
ar inte nadd. Overgangen blaa -> ritning, processektionernas tathet, case-overgangen och
case-ingressen ar underkanda. Plan 067 § Verification har aldrig korts.

**Nasta agent borjar i `tests/alunix-r8/runs/V3d/HANDOFF-2026-09-20.md`.** Rataranskriptet for
hela sessionen ligger i
`~/.claude/projects/C--Users-Anton-L-anti-slop-design/09682a1d-0752-4109-a0dc-1b4a1af7a4ac.jsonl`.

Blockerare: veckokvoten slut till 2026-09-23. *(Inaktuell: sessionen 2026-09-22 korde utan
kvotproblem, och F1–F5 ar atgardade. Texten star kvar som historik.)*

Canonical project hub. Read this first to orient; every section points at the document that carries the detail.

## 2026-09-10 — T2 klart, r8-testet genom R3, motion/perf-proberna kalibrerade

**Den bärande begränsningen från 2026-09-08 är löst.** Designsystemet är registrerat
som egen lokal marketplace och installerat direkt (10 hookar, byte-identiska med
repot) — sessioner laddar inte längre en inaktuell plugin-cache-kopia från
super-intelligence. `super-intelligence`s egen kopia (`b48f233`) är pushad efter en
sekretskanning.

**r8-testet (Alunix, tre koncept) har körts genom R3** med en headless Opus-lead
(`claude -p --resume`, återupptagen per fas/runda av den bevakande sessionen; byggare
och granskare som `Agent`-subagenter, inte terminal-teammates — se
`tests/alunix-r8/PROTOCOL.md` § "Valt läge 2026-09-09"). R3 var första gången
kvartetten (design-critic/heuristics/a11y/perf) och `codex-review` bevisades köra på
riktigt: en verklig `codex exec`-process (`gpt-5.5`, read-only, riktig
kontoanvändning), inte bara en rapport med rätt form. V3c (byggde hela sidan) ligger
närmast mål; K3 och K4 (fixrundor) är båda blockerade på var sin ersättningsplan efter
att arkitekten hittade följdfel i tidigare rundors fixar. Full status:
`tests/alunix-r8/STATUS.md`, kostnadsbild och beslut per runda:
`tests/alunix-r8/LEAD-REPORT.md`. Boarden (`localhost:4626`,
`.claude/launch.json`-posten `alunix-board-r8`) väntar på Antons egen granskning
innan R4 startas.

**Tre mätskript kalibrerade om eller lagade under samma test:**
`motion_probe.py`s `max_step`-gräns gäller nu bara det dämpade spelhuvudet `--sc-ps`
(en härledd `transform`-kurva rapporteras men grindar inte — en smoothsteppad kurva
toppar naturligt på ~4,4 %/ruta); `perf_probe.py` attribuerar en cells egen
resursvikt separat från vad dess `<iframe>`-exempelsajter drar in; `contrast_over_media.py`
var en engångsskript med hårdkodad port och gick inte att köra i r8 — nu ett riktigt
CLI. Fullt session-underlag: `session-logs/2026-09-10-session-log.md`.

## 2026-09-08 — designkedjan v4: mätlagret byggt, F-012 stängd, Higgsfield inkopplat

Efter r7 bad Anton om en full omarbetning: varje uppström läst i sin helhet med motiverade
uteslutningar, ett obligatoriskt katalog-först-steg, ett prestandalager, en lyft-procedur
som ersätter "kör polish", och ett Alunix-test med agent-team. Planen ligger i
`~/.claude/plans/trots-den-senaste-design-system-federated-raven.md` och är godkänd.
**Åtta av tretton infrastrukturuppgifter är klara, testet är inte startat.** Full
överlämning: [`HANDOFF-2026-09-08-designkedjan-v4.md`](HANDOFF-2026-09-08-designkedjan-v4.md).

**F-012 är stängd med mätning.** "Hackigt och billigt" var två fel, och F-011 orsakade
ingendera. Motorn dämpar bara video och pekare; `--sc-p` skrivs 1:1 från rå scrollposition,
så bespoke rörelse stegar med hjulet. Två fixturer med identisk bildfrekvens (16,7 ms p95)
skiljer sig med 18 trappsteg mot 0. V3b är dessutom genuint tung: 4,9 MB, 19 typsnittsfiler,
17 långa tasks under scroll, och en hero-bild hotlänkad från Unsplash i strid med Step 5b.
Åtgärd: [`scripts/scroll/sc-smooth.js`](skills/design/scripts/scroll/sc-smooth.js) publicerar
en lerpad `--sc-ps`. Regeln står i
[`references/motion-smoothness.md`](skills/design/references/motion-smoothness.md), posten som
F-013 i `design-catalogue/FEEDBACK.md`.

**Tre nya mätskript, alla bevisade i båda riktningarna** — `motion_probe.py`, `perf_probe.py`
och `preflight_taste.py`. Principen är ny och gäller nu generellt: en kontroll som bara kan
avfyra är lika värdelös som en som aldrig gör det, så varje skript prövas mot en trasig
fixtur som måste falla **och** mot ett känt-gott bygge som måste hålla tyst. Den regeln fångade
tre egna fel samma dag, bland dem att `motion_probe` godkände ett kort som inte rörde sig alls.

**Referensgolvet kräver nu ett mekaniskt katalogval.** `scripts/catalogue/select.py` väljer
referenser deterministiskt ur hela katalogen och skriver raden golvet läser, så ett bygge inte
kan gå vidare på referenser någon mindes. Routingen pekar bara på laddbara skills igen:
fallback-namnet hade aldrig gått att ladda.

**Higgsfield är inkopplat och mätt** — se
[`references/generation.md`](skills/design/references/generation.md). MCP:n kör, skillsen
levererar procedur, och varje anrop loggas med modell och kostnad. `sync_agents` körs aldrig:
den laddar upp Antons egna skills till Higgsfields marknadsplats.

**Bärande begränsning just nu:** hookarna i sessionerna är inaktuella plugin-cache-kopior från
super-intelligence, så allt hook-arbete är bevisat men inte i drift. Det är T2 i planen och det
blockerar r8.

## 2026-09-07 — motion-always policy (F-011), a real HTTP/1.0 board bug, and a chain audit

The r7 Alunix board still showed no scroll motion when Anton judged it — root cause was
Windows' Animationseffekter still off (same condition as F-001), which sets
`prefers-reduced-motion: reduce` in every browser on the machine at once. Anton escalated
past "fix my own review" to a permanent, global rule after the accessibility tradeoff was
laid out plainly: **motion always plays now, everywhere this system builds, regardless of
`prefers-reduced-motion` or any other browser/OS setting** (`design-catalogue/FEEDBACK.md`
F-011). Applied through the whole chain — the vendored engine
([`scripts/scroll/scrollcraft.js`](skills/design/scripts/scroll/scrollcraft.js)/`.css`),
both r7 builds, and `a11y-audit` globally (it no longer flags missing reduced-motion
support, anywhere it runs — not just here). WCAG 2.3.1's flash-rate limit is untouched;
that one is a safety floor, not a preference. Separately, a real bug: `scripts/board.py`
was still on HTTP/1.0 and dropped WebP under Chromium — the exact bug `serve.py` was built
to fix for the cell builders, never ported to the board itself. Fixed alongside.

On request, a full chain audit followed
([`tests/alunix-ab-r7/CHAIN-AUDIT-2026-09-07.md`](tests/alunix-ab-r7/CHAIN-AUDIT-2026-09-07.md)):
a real session-scoping bug in `design-stop.py`'s reports (counts every session in the shared
ledger when the hook subprocess doesn't see the same `CLAUDE_CODE_SESSION_ID` the Bash tool
does — proposed fix: read the event payload's own `session_id`, not proposed as done), the
route-gap split into two distinct causes (`imagegen-frontend-web` fires on any `<img>` tag
regardless of whether generation is needed; `"impeccable layout"` is simply the wrong skill
name — the real skill is `impeccable`, and it's unclear it even loads in the builders'
environment), and `Skill(design-catalog)` never once invoked in either r7 build — the
orchestrator's own round-1 prompt handed builders file paths directly instead of the
skill's own `query.py` search. New open item: F-012, motion now renders but "looks janky and
cheap" — cause not yet established, explicitly handed to the next session.

## What it is

A Claude Code **design system**. It writes no visual rules of its own beyond one addition — it sequences other people's work (impeccable, Hallmark, taste-skill, Anthropic's Claude Design prompt, copywriting, humanizer) and enforces that they do not overwrite the client's brand on the way through.

**The one rule everything serves:**

> **Brand derives direction. Skills supply craft. Themes are the last resort.**

Every failure this system was built to fix came from inverting that — a specialist skill set the visual direction and the brand got repainted in the skill author's palette.

## 2026-09-04/05 Alunix bake-off: the chain run on a real client project, five rounds

Anton's own agency site, Alunix, run through the full v3 chain as a real build instead of
a blind test. `tests/alunix-concepts-r3/` (R5+R6 combined per Anton's mosaic, six pixel
rounds) → `-r4/` (three remixes: M1 continuous ground, M2 chaptered pinned stage, M3
gallery rail, one `design-critic` pass) → `-r5/` (three variants of the winning M1, a
polish round on the winner, `V3-baseline` frozen for reference). `board.py` rewritten
mid-session (single full-width pane, rating drawer, `--fallback-root` so cells can
reference `/sites/...` and other repo-absolute paths) — that fix now lives in the live
skill and is mirrored here.

**What this proved and what it didn't.** The reference-lock, feeling-curve and fingerprint
mechanics held up on a real multi-round client job, not just a one-shot test. What it did
**not** prove: route gap never reached zero (see GOALS.md's changelog, 2026-09-04/05) —
`emil-design-eng`, `imagegen-frontend-web` and `impeccable layout` were named every session
without ever loading, on a build that never needed an animation library, generated imagery,
or a component system. Worth a session to decide whether that is a real gap or a router
false-positive class the intent corpus doesn't cover yet.

## 2026-09-03 rework (v3): quiet hooks, an accessibility skill, a bake-off, a catalog

Plan: `~/.claude/plans/uppgift-design-rework-v3-validated-hammock.md`. Run log with every
A/B, screenshot and verdict: the "Design Rework v3" artifact (claude.ai/code/artifacts) and
[`tests/ab/`](tests/ab/) (one `verdict.md` per addition). Decisions by Anton: the catalog's
database is a GitHub repo (1A); **the live copies are canonical and this repo is a mirror**
(2A, [`scripts/sync-from-live.py`](scripts/sync-from-live.py), verify check "repo == live").

- **Hooks stop over-triggering.** `design-intent.py` classifies prompts high/medium/none
  (verb + UI object, negative guards for hook/skill/CARL/investigate talk, project signal);
  a `high` prompt or a `Skill(design…)` call **arms** the session (`.impeccable/.armed`), and
  route/verify/stop act only when armed (contract gate on a locked DESIGN.md always). The
  Stop gap now counts only code-strong craft routes that were neither loaded nor read
  (`skill-read` event); framework skills never count; section 6 always prints. 40-prompt
  corpus in `tests/intent_corpus.jsonl`; `verify-design-system.py` is 139 checks against
  `super-intelligence/hooks` + `hooks.json`. CARL DESIGN recall narrowed to phrases + exclude.
- **`a11y-audit`** (new skill, eight passes, three Playwright scripts proven on
  `tests/a11y/broken.html`, principle catalog from Interfaces, designpowers,
  inclusive-design-skills, designer-skills) and three read-only Sonnet reviewer agents
  (`design-critic`, `design-a11y-reviewer`, `design-heuristics`) reconciled by
  accessibility > usability > brief > personas.
- **Reference lock + decision ledger** (Refero's method) in Step 1b at every tier;
  gates 89–91; `photo-sources.md` corrects the Unsplash licence note.
- **Step 2b:** page grammar, feeling curve, fingerprint gate (vault registry
  `wiki/projects/_index/design-fingerprints.md`), scroll devices on the vendored
  scroll-craft engine, `scroll_verify.py`; then the **bake-off board** (`scripts/board.py`,
  `references/shotgun.md`): directions × engines, the user picks, `approved.json`.
- **Visual critique** (`verbs/critique.md`, seven dimensions on pixels) and the review
  orchestrator (`verbs/review.md`) behind the `audit` verb.
- **Design catalog** `oloflun/design-catalog` (localhost-first, repo as database,
  `Skill(design-catalog)`) seeded with the seven example sites; Step 1b starts there.
- **Emil Kowalski skills refreshed** (nine), `hallmark` no longer auto-invokes,
  `frontend-design` plugin off (two rules ported into the craft floor),
  `super-intelligence:design` user-invocable-only, `polish` dependency fixed.
- **Not adopted, with evidence:** frontend-design as a skill (AB09: escaped the cream
  default but lost the reveal guard and three anatomies); designpowers' build agents
  (set direction); Refero MCP (optional, unconfigured); kie.ai video generation.

## 2026-08-01 rework: registers replace the house style, exit bar goes mechanical

Full rationale: [`plans/2026-07-31-what-actually-made-the-difference.md`](plans/2026-07-31-what-actually-made-the-difference.md).

Archaeology across three prior sessions established that the 2026-07-28 v2 rework
(below) fixed v1's mechanical failures — hooks not firing reliably, specialist skills
repainting brands — but never asked why v1's *output* had been good. Craft that lived
resident in one dense context became 120 on-demand reference files; the step that named
an aesthetic lane before writing code disappeared; every quality gate stayed negative,
so a flat, on-palette, thoroughly generic page passed all 88 of them untouched.

- **`SKILL.md` "The craft floor"** — a resident (not routed) section: name the lane
  before code; a **register table** — editorial print / cinematic dark / illustrated
  dark / modern clean / warm photographic / historical art — picked from the business,
  not from which example happens to exist on disk; house physics with exact values;
  a composition contract; an apparatus budget; "a muted tone needs a value per
  ground"; "reduced motion removes motion, not content."
- **[`house-physics.md`](skills/design/references/house-physics.md)** (new) —
  structural invariants true in every register, then a per-register inventory with
  exact values pulled from real page source, not memory.
- **[`sites/`](sites/)** — six worked examples now, not three: `calyx.html` /
  `horai.html` / `hyperborea.html` (editorial print / cinematic dark / illustrated
  dark, from the original v1 build) plus `tidvatten.html` (modern clean),
  `vintergatan.html` (editorial print, a second exemplar), `vinterspelen.html`
  (historical art — built with **no worked example on disk to copy**, the hardest
  test of whether the register table teaches derivation rather than imitation), and
  `klova/` (warm photographic, vendored from a real client project — its README
  explains why it correctly breaks nearly every "invariant" the earlier system
  would have forced on it).
- **`design-stop.py`** — the Stop hook now **blocks** ending a design session when UI
  edits exist that no rendered image was Read afterward (capped at 2 blocks/session,
  then degrades to advisory). This is the mechanical version of the instruction that
  made the difference in the Snajp session — "iterate until you honestly beat the
  references, verified on pixels" — previously only enforced when a user retyped it
  as an explicit goal.
- **`design-session-start.py`**, **`design-vision-track.py`** (new hooks) — session
  state that never cleared before now clears on `SessionStart`; a `PostToolUse` hook
  on `Read` logs when a render actually enters context, feeding the block above.
- **`design-verify-gate.py`** — inverted from "prefer read_page over screenshot, two
  rounds max" to "judge from pixels, iterate until a full pass finds nothing."
- **[`scripts/contrast.py`](skills/design/scripts/contrast.py) /
  [`contrast_over_media.py`](skills/design/scripts/contrast_over_media.py)** (new) —
  both were wrong on their first real run, in ways that would have passed a broken
  page: one only parsed `rgb()` against Tailwind 4's `oklch()` output, the other
  measured text-over-photo against the page background instead of the rendered
  plate with the text hidden.

Verified with three blind one-shot builds from fresh subagents — no iteration, no
dialogue — all of which the author judged to clear the reference bar on the first
attempt. `verify-design-system.py` 80/80. Applied to `alunix-site` (a new scroll-driven
set-piece) and `klova-hamnkrog` (a design audit, 8 fixes, both committed).

**Not yet done:** `install.mjs`/`upgrade.mjs` in `super-intelligence` don't wire the
two new hooks into `settings.json` for existing installs yet — `deployTemplate()`/`wf()`
skip writes when the destination already exists, so this needs an explicit additive
merge. `super-intelligence` 0.4.5 has the file sync committed locally, not pushed.

## 2026-07-28 rework (superseded above, kept for history)

## How it decides — four layers, in order

| Layer | Question | Detail |
|---|---|---|
| **1. Verb** | What kind of job is this? | 8 verbs (EN + SV): build · redesign · audit · polish · study · explore · system · verify. Re-fires when the verb *changes*, not once per session. → [`skill-orchestration.md`](skills/design/references/skill-orchestration.md) §2 |
| **2. Gate** | Where does direction come from? | Tier 0-locked / 0-prose / 1-derive / 2-reference / 3-invent. First tier with evidence wins. → [`brand-derivation.md`](skills/design/references/brand-derivation.md), [`invention.md`](skills/design/references/invention.md) |
| **3. Mode** | Marketing or product? | Persuade/Read/Experience use the marketing stack; Operate (dashboards, admin, tables, editors) uses a different register on the *same tokens*. → [`product-surfaces.md`](skills/design/references/product-surfaces.md) |
| **4. Component** | Which craft skill for this file? | Signal-matched routing table, parsed by the hooks. → [`component-routing.md`](skills/design/references/component-routing.md) |

## The hook chain

Enforcement lives at **edit boundaries**, not turn boundaries — the original system injected guidance once per prompt and drifted across a sixty-tool-call build turn.

```
UserPromptSubmit    design-intent.py        verb + tier + this project's locked tokens
PreToolUse  write   design-gate.py          DENY contract violations before they land
PreToolUse  browser design-verify-gate.py   inspection discipline before the first look
PostToolUse write   design-route.py         name the right skill for what was written
PostToolUse Skill   design-telemetry.py     attribute every skill call to its component
Stop                design-stop.py          deep detector pass + session report
```

Source: [`.claude/hooks/`](.claude/hooks/) (vendored) · live at `~/.claude/hooks/` · shipped in `super-intelligence/hooks/`.

**The load-bearing limitation:** hooks inject text and deny writes. They **cannot load a skill** — only the model calls `Skill()`. Every route is therefore a *suggestion*, which is why the route-vs-invocation gap is measured rather than assumed. `design-gate.py` is the one hard enforcement point.

## Invariants that bite if broken

- **Only write `DESIGN.md` through `impeccable document` or `brand-system`.** Five skills write a file by that name in three incompatible formats. A prose-only one used to make the system announce *"TIER 0 — LOCKED"* while enforcing nothing (`#FF00FF` + Comic Sans passed silently). Now reported honestly as `0-prose`.
- **`minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design` may never set direction** — each hardcodes a full palette. Gate 60 treats their hex in a Tier 0–2 build as a contract violation, logged as a `trap` event.
- **Redesign needs all three procedures, in order:** mode detection → tier gate → page shape. Mode beats tier beats page shape.
- **Marketing references do not load on product surfaces** — hero enrichment, macrostructures, the six-axis fingerprint, gates 66–88.
- **A local addition inherits its surface.** It never re-runs the gate and never starts a second identity (gate 65).
- **Don't mix pipelines.** gstack and Stitch are complete parallel workflows that write their own `DESIGN.md`; pick one lane per project.

## Document map

**Entry points**
- [`skills/design/SKILL.md`](skills/design/SKILL.md) — the front door. Dispatcher only; ~240 lines.
- [`ROUTER.md`](ROUTER.md) — plain-English explainer of the architecture.
- [`README.md`](README.md) — public-facing, includes the v1→v2 rebuild rationale and demo sites.

**Foundation**
- [`skill-orchestration.md`](skills/design/references/skill-orchestration.md) — **the foundation doc.** 7 phases, verb routing, full skill catalog with each skill's role and boundary, 9 known collisions and their resolutions, the parallel pipelines. Read for any job larger than one component.
- [`product-surfaces.md`](skills/design/references/product-surfaces.md) — Operate mode.

**The gate**
- [`brand-derivation.md`](skills/design/references/brand-derivation.md) — Tier 1. VISUAL/CONTENT FOUNDATIONS interrogations, logo safety, the exact-values rule.
- [`invention.md`](skills/design/references/invention.md) — Tier 3, plus the four AI palette-calibration clusters.
- [`study.md`](skills/design/references/study.md) — Tier 2.

**Rules**
- [`gates.md`](skills/design/references/gates.md) — index. 1–57 Hallmark · 58–65 ours · 66–88 production tells · mechanical detector mapping.
- [`slop-test.md`](skills/design/references/slop-test.md) — gates 1–57, ported verbatim.
- [`production-tells.md`](skills/design/references/production-tells.md) — gates 66–88, micro-decoration signatures.
- [`scope-discipline.md`](skills/design/references/scope-discipline.md) — targeted-change rule, inheritance checklist, **redesign protocol**.

**Process**
- [`process.md`](skills/design/references/process.md) — working method, question calibration, intensity dials, official-design-system map.
- [`copy-gate.md`](skills/design/references/copy-gate.md) — copywriting → humanizer, every language.
- [`options.md`](skills/design/references/options.md) · [`wireframe.md`](skills/design/references/wireframe.md) · [`handoff.md`](skills/design/references/handoff.md)

**Sibling skills**
- `skills/design-verify/` — batched browser inspection.
- `skills/brand-system/` — builds a full system, emits `{brand}-design` as an installable skill.

**Meta**
- [`attribution/UPSTREAMS.md`](attribution/UPSTREAMS.md) — every upstream, what it provides, what we changed.
- [`verify-design-system.py`](verify-design-system.py) — 79 mechanical checks. Run after any change.
- [`AUDIT.md`](AUDIT.md) — **stale.** The pre-rebuild 32-skill audit; superseded by `skill-orchestration.md`. Kept for history.

## Verification

```bash
python verify-design-system.py
```

79 checks: install, settings wiring, routing table, reference fidelity against upstream, contract enforcement, verb routing, prose-only false-lock, product-vs-marketing routing, false positives, kill switch.

Not covered — model behaviour, provable only by a real build's telemetry report: gate-order judgment, inheritance, the targeted-change rule, copy quality.

## Status

**This repo is the plugin now (since 2026-09-04).** The design skills (`design`,
`a11y-audit`, `brand-system`, `design-catalog`, `design-verify`), the design hooks, and the
three reviewer agents moved out of `super-intelligence` into this standalone
`anti-slop-design` plugin — `super-intelligence` no longer ships or wires any of it. The
vault's `.agents/skills/design` (and `a11y-audit`) is the live/canonical copy;
`skills/design/` and `skills/a11y-audit/` here are the mirror, kept in sync with
[`scripts/sync-from-live.py`](scripts/sync-from-live.py) (run manually after editing the
live copy — not automatic, easy to forget).

Design system rebuilt 2026-08-01 (registers + mechanical exit bar), reworked again
2026-09-03 (hooks, `a11y-audit`, reference lock, catalog), and again 2026-09-06/07 (r7:
reference floor + per-session ledger fix + motion-always policy, F-011/F-012 above).

**Open:** **`design-rework-v3` är opushat — 29 commits, allt septemberarbete inklusive
hela V3d, finns bara på den här disken; grenen finns inte på `origin`.** F6/F7 är
orörda (stora fyrkantiga block och den hårda vågräta skarven i blå→ritning).
Plan 067 § Verification är obetald. `<nav>`-landmärket saknas i sidhuvudet på
V3d-sidan (två taggar, daterad skuld i `.impeccable/a11y-debt.md` till
2026-12-20). `skills/design/scripts/contrast.py` har en hårdkodad URL
(`localhost:3055`) och kan inte pekas på en sida — a11y-audit föreskriver den och
den kunde därför inte köras som avsett. `memory/BLOCKS.md` är 25 293 tecken mot
sin egen `limit: 3000`. `oloflun/alunix` har en kvarvarande juli-prototyp i
`app/`/`components/`/`lib/` — den byggs inte och publiceras inte, men radering
kräver Antons ord. Sedan tidigare: katalogens Vercel + GitHub OAuth-steg; två
Hallmark-referensfiler (`custom-theme.md`, `macrostructures.md`) skiljer sig från
upstream HEAD därför att upstream flyttat (fidelity-kontrollen rapporterar det
ärligt); huruvida `impeccable` laddas alls i den headless byggmiljön (se F-011
ovan); Stop-hookens sessions-scopningsfix (föreslagen, inte gjord).

## Related

- Session logs: `session-logs/` · Plans: `plans/`

## Relevanta källor

- [[sources/2025-07-21-the-game-hormozi-12-persuasion-hacks]] — Hormozis 12 övertalningstrick för sälj och copy (captured: 2025-07-21)
- [[sources/2026-05-05-the-game-hormozi-5-things-before-starting]] — fem strukturella fördelar innan man startar ett bolag (captured: 2026-05-05)
- [[sources/2026-08-24-skit-om-ai-9-exponera-foretaget-i-tider-av-ai]] — Skit om AI #9: synlighet i AI-eran — teknisk SEO före AI-tjänster (captured: 2026-08-24)
- [[sources/2026-09-02-startup-ideas-5-github-repos-goldmine]] — Fem repos: anti-slop, AI-CRM, Video Use, SkillSpector, Phone Harness (captured: 2026-09-02)
