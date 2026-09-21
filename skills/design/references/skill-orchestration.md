# Skill orchestration

**The foundation document. Load when the job is anything larger than a single component.**

The system has ~40 design-capable skills across five packs plus two complete parallel pipelines. Most of them overlap. This file says which one owns which decision, in what order, and what each is forbidden from doing.

**The rule everything else serves:** *brand derives direction, skills supply craft, themes are the last resort.* A skill that arrives at a component and repaints it has violated the gate order, regardless of how good its taste is.

---

## 1. The seven phases

Every design job is some subset of these, in this order. Skipping forward is allowed; going backward means the earlier phase was wrong.

| # | Phase | Question it answers | Owner |
|---|---|---|---|
| 0 | **Classify** | What kind of job is this? | This file + `design-intent.py` |
| 1 | **Scope** | Component, page, surface, or whole system? | `SKILL.md` Step 0 |
| 2 | **Source** | Where does direction come from? | The tier gate |
| 3 | **Direction** | What is the visual language? | `brand-derivation` / `study` / `invention` |
| 4 | **Structure** | What is the page's shape and rhythm? | `verbs/redesign` · `macrostructures` · `structure` |
| 5 | **Craft** | How is each component executed? | `component-routing.md` |
| 6 | **Verify** | Did it actually work? | `design-verify` + detector + telemetry |

Phase 2 is the one that fails silently, and it is the reason this system exists.

---

## 2. Verb routing — Phase 0

The single largest gap in the pre-2026-07-28 system: it routed by *component* but never by *task type*. These are the verbs, their detection, and their owner.

| Verb | Fires on | Owner procedure | Notes |
|---|---|---|---|
| **build** | "build", "create", "make me a", "new page/site/landing" | Full flow, `SKILL.md` Steps 0–6 | Default when nothing else matches |
| **redesign** | "redesign", "rebuild", "gör om", "modernise", "refresh", "overhaul" | § 3 below — three-procedure sequence | Most collision-prone verb |
| **audit** | "audit", "review the design", "what's wrong with", "check this UI" | `verbs/audit.md` → then `design-review` if fixes wanted | **Read-only. Never edits.** |
| **polish** | "polish", "finishing touches", "tighten", "make it feel better", "polera" | `impeccable polish` → `emil-design-eng` for motion | Assumes direction is settled |
| **study** | A URL or screenshot supplied, "match this", "like this site" | `study.md` → `extract-design` for tokens | Tier 2. Borrow principle, never pixel |
| **explore** | "options", "variants", "show me some directions", "I don't know what I want" | `wireframe.md` → `options.md`, or `design-shotgun` | Low fidelity first |
| **system** | "design system", "brand kit", "tokens for the whole app" | `brand-system` → emits `{brand}-design` | Produces the Tier-0 artifact |
| **verify** | "check it", "does it look right", "screenshot it" | `design-verify` | Never edits |

**Ambiguity rule.** If two verbs both fire, take the one that changes more, and say which you took. *"Redesign the pricing page and polish the nav"* is a redesign job with a polish sub-task, not two jobs.

---

## 3. The redesign collision — resolved

Three procedures claim redesign. They are **complementary when sequenced** and destructive when picked arbitrarily. Run all three in this order:

### Step 1 — Mode detection · `scope-discipline.md` § Redesign protocol
*(source: taste-skill v2 §11)*

Decide **greenfield / preserve / overhaul** before anything else. Misclassifying here is the single biggest source of bad redesign output. Then: audit before touching (brand tokens, IA, content blocks, patterns to keep vs retire, **SEO baseline**), and note the never-change-silently list (URL structure, nav labels, form field names, logo, legal copy).

### Step 2 — Does brand evidence survive? · the tier gate
*(source: this repo + impeccable v4)*

- **preserve** → Tier 1. Derive from what exists.
- **overhaul** → Tier 1 if the mark and type survive; Tier 3 only if the identity itself is being replaced.
- A **partial rebrand** (new name, kept traits) is **preserve**, not greenfield. impeccable v4 calls this the *"Incomplete brand"* branch: *"preserve confirmed assets and recognizable traits, then help the user expand the system."*

impeccable's own rule governs the boundary: *"Refinement preserves; redesign replaces… Never split the difference into polish on the discarded look."*

### Step 3 — Execute the page shape · `verbs/redesign.md`
*(source: Hallmark, 269 lines)*

Owns what the other two do not: the **single-page vs multi-page scope split** (multi-page fires on a directory target and produces a locked `design.md`), section rhythm, component voice, and the non-destructive implementation rule.

**Precedence when they conflict:** mode detection (1) beats tier (2) beats page shape (3). A `preserve` mode with a Hallmark macrostructure that would discard the existing IA loses — mode wins.

**Do not also invoke** `redesign-existing-projects`. It is taste-skill v1's redesign skill and is byte-identical to content already covered by Step 1. Redundant, and its audit list is weaker.

---

## 4. The DESIGN.md problem

**Five things write a file called `DESIGN.md`, in three incompatible formats.** This is the most dangerous ambiguity in the stack because `design-gate.py` reads it to enforce the token contract.

| Writer | Format | Gate can enforce? |
|---|---|---|
| `impeccable document` | YAML frontmatter, Stitch schema (`colors`/`typography`/`rounded` as **maps**) + `.impeccable/design.json` sidecar | **Yes** — this is the canonical form |
| `brand-system` (ours) | Same, via `impeccable document` | Yes |
| `design-md` (Stitch) | **Prose only**, no frontmatter | **No** |
| `design-consultation` (gstack) | Prose + its own structure | **No** |
| Hallmark `design.md` | Lowercase, own format | Partially |

**The failure this creates:** `tier()` used to report `0-locked` on file existence alone. A prose-only `DESIGN.md` therefore announced *"TIER 0 — LOCKED, inherit the system, do not re-derive"* while the gate enforced **nothing** — verified empirically: a write with `#FF00FF` and Comic Sans passed silently. That is strictly worse than having no `DESIGN.md`, because the model skips derivation *and* gets no enforcement.

**Resolved:** the tier signal now distinguishes
- `0-locked` — frontmatter present and parseable → full mechanical enforcement
- `0-prose` — file exists, no parseable tokens → **authority without enforcement**. Read it and obey it as a human-authored contract, but know the gate is blind. Run `$impeccable document` to add frontmatter if mechanical enforcement is wanted.

**Rule:** only ever *write* `DESIGN.md` through `impeccable document` or `brand-system`. If another skill wrote one, treat it as a brief, not a contract, and convert it.

---

## 5. Direction skills — Phase 3

Exactly one of these sets direction. The rest may contribute craft vocabulary with their palettes overridden.

| Skill | Role | Allowed to set direction? |
|---|---|---|
| `brand-derivation.md` (ref) | Tier 1 — derive from the brand's own evidence | **Yes**, this is the default |
| `study.md` + `extract-design` | Tier 2 — extract DNA / tokens from a reference | **Yes**, recomposed not cloned |
| `invention.md` | Tier 3 — invent a named world | **Yes**, only when nothing to derive from |
| `impeccable new-work` | Tier 3 engine — 7 candidate directions from the audience's cultural world | **Yes** at Tier 3 |
| `design-taste-frontend` (v2) | Brief inference, intensity dials, design-system map, production tells | **Craft only.** Palette-locked at Tiers 0–2 |
| `gpt-taste` | Awwwards lane — AIDA, GSAP scrolltelling, 2-line H1 rule | **Craft only** |
| `high-end-visual-design` | Apple/Linear detail vocabulary | **Never** — hardcodes `#050505` / `#FDFBF7` |
| `minimalist-ui` | Editorial minimal lane | **Never** — hardcodes Notion's palette |
| `industrial-brutalist-ui` | Swiss + tactical terminal | **Never** — hardcodes `#E61919` as "the ONLY accent" |
| `ui-ux-pro-max` | 161 palettes, 57 font pairings, 99 UX rules, 25 chart types | **Craft + accessibility only.** Its palette library is a Tier-3 menu, never a Tier 0–2 source |
| `brandkit` | Brand-guideline *imagery* (boards, logo systems, decks) | No — produces assets, not the system |

The bottom three are gate 60: their hardcoded hex appearing in a Tier 0–2 build is a contract violation, logged as a `trap` event.

---

## 6. Craft skills — Phase 5

Routed mechanically by `component-routing.md`. Each supplies execution inside the settled direction.

**Motion and interaction:** `emil-design-eng` (easing, springs, transform-origin, `:active` — the default for anything that moves) · `animated-navigation` (nav-specific interaction model) · `vercel-react-view-transitions` (route/state transitions) · `slideshow` (carousel mechanics).

**Framework correctness:** `next-best-practices` · `vercel-react-best-practices` (performance) · `vercel-composition-patterns` · `react-components` (component structure) · `shadcn-ui` (primitives) · `vercel-react-native-skills` (RN only — state N/A explicitly on web).

**Content surfaces:** `dataviz` (charts — its palette derives from the locked accent, never its own placeholders) · `imagegen-frontend-web` / `imagegen-frontend-mobile` (real imagery, not CSS scenery) · `image-to-code` (image → implementation).

**Copy:** `copywriting` → `humanizer`, in that order, on every user-facing string, every language. `copy-editing` for existing copy. `cro` when the goal is explicitly conversion.

**Accessibility:** `ui-ux-pro-max` (99 UX guidelines) · `web-design-guidelines` (Vercel interface guidelines, review-only).

---

## 7. Verify skills — Phase 6

| Skill | Scope | Edits? |
|---|---|---|
| `design-verify` (ours) | Batched browser inspection, four breakpoints, console + network, storage safety | No |
| `impeccable detect` | 68 deterministic rules incl. the four `design-system-*` contract checks | No |
| `verbs/audit.md` | Severity-graded slop findings, stamp-lies detection, `design.md` drift | **No — never edits** |
| `design-review` (gstack) | Visual QA that *fixes* issues, atomic commits, before/after screenshots | **Yes** |
| `polish` / `impeccable polish` | Final alignment, spacing, consistency pass | Yes |
| `tauri-react-visual-verify` | Tauri/React app UI in a plain browser | No |
| `qa` (gstack) | Functional QA of a web app | Yes |
| `ios-design-review` / `ios-qa` | iOS on real hardware | Varies |

**Order:** `design-verify` (see it) → `impeccable detect` (mechanical) → `verbs/audit.md` (judgment, read-only) → *then* `design-review` or `polish` if fixes are wanted. Auditing and fixing in one pass is how findings get rationalised away mid-edit.

**`polish` has a stale dependency** — it instructs `/teach-impeccable`, which is impeccable **v3** terminology (`teach` aliased `init`; v4 renamed it). Use `$impeccable init` instead, or `impeccable polish` directly.

---

## 8. The parallel pipelines

Two complete alternative workflows exist. They are **not** wired into this router, and mixing them mid-job produces incoherent output. Pick one lane per project.

### gstack design pipeline
`design-consultation` (→ its own DESIGN.md) → `design-shotgun` (variants + comparison board) → `design-html` (production Pretext HTML/CSS) → `design-review` (visual QA + fixes). Plan-stage variant: `plan-design-review`.

**When to prefer it:** the user explicitly invokes a `/design-*` gstack command, or wants the comparison-board review loop with structured feedback collection. It has real strengths this router lacks — a genuine variant board and an iterative fix-and-recommit loop.

**When not to:** any project already carrying an `impeccable`-schema `DESIGN.md`. `design-consultation` will offer to overwrite it in a format the gate cannot read.

### Stitch pipeline
`enhance-prompt` → `stitch-design` → `stitch-design-taste` / `design-md` (DESIGN.md) → `react-components` (Vite/React output) → `remotion` (walkthrough video). Requires the Stitch MCP.

**When to prefer it:** the user is working in Google Stitch. Otherwise irrelevant.

**Boundary:** both pipelines produce a `DESIGN.md` this router's gate cannot enforce. If a project has been through either, convert with `$impeccable document` before relying on the contract gate.

---

## 9. Known collisions and their resolutions

| Collision | Resolution |
|---|---|
| `hallmark` skill vs this `design` skill | All 105 Hallmark references are ported byte-identical into `references/`. The installed `hallmark` skill is **redundant and competes for auto-invocation** on the same triggers. Prefer `design`; invoke `hallmark` only by explicit name. *Flagged for the user — narrowing its description or uninstalling is their call.* |
| 3× redesign | § 3, sequenced |
| 5× DESIGN.md writers | § 4, `impeccable document` is canonical |
| `redesign-existing-projects` vs taste-skill §11 | Same upstream author; §11 supersedes. Do not run both |
| `design-review` (gstack) vs `verbs/audit.md` | audit is read-only judgment; design-review is fix-and-commit. Audit first |
| `polish` vs `impeccable polish` | Prefer `impeccable polish` — `polish` has the stale `/teach-impeccable` dependency |
| `ui-ux-pro-max` palettes vs the tier gate | Its 161 palettes are a **Tier-3 menu only** |
| `webpage-builder` | **Project-locked** to the project-a-next Swedish B2B design system. Never fire outside that project |
| `design-md` vs `brand-system` | Both emit DESIGN.md; `design-md` is Stitch-only and prose-only. **Demoted to Stitch-import (2026-09-09):** its only sanctioned job is turning a Stitch export into a brief. It never writes the contract file — run `$impeccable document` afterwards to produce the canonical `DESIGN.md` the gate can read (§ 4) |

---

## 10. Product surfaces are a mode, not an exclusion

Dashboards, admin panels, settings, data tables, forms, and editors appear inside corporate sites constantly. They are **in scope, in a different mode** — see [`product-surfaces.md`](product-surfaces.md).

The distinction that matters:

- **The gate does not change.** Product surfaces derive colour, type, and radius from the same brand. A locked project's dashboard shares its landing page's tokens. Gate 65 (second identity) applies across the seam.
- **The register does change.** Marketing taste does not transfer. `impeccable`'s Operate mode and its `reference/operate.md` are the authority: one font family, fixed rem scale, Restrained colour floor, accent for state only, 150–250ms motion that conveys state, no page-load choreography, density and familiarity over expression.
- **Different references load.** `hero-enrichment`, `macrostructures`, `structure`'s six-axis fingerprint and `production-tells` (gates 66–88) are marketing-composition references and are **not** loaded on a product surface. A version label in a product header is legitimate build metadata, not a tell.

Detection is automatic — `component-routing.md`'s `product` rule fires on dashboard/admin/settings/table/editor paths and on signals like `<DataTable`, `useReactTable`, `<CommandDialog`, `aria-sort`, `<Sidebar`. No user input required.

**Hand off the engine, keep the design.** For a serious data grid (TanStack, AG Grid), a code editor (Monaco, CodeMirror), an enterprise context with an official system (Fluent, Carbon, Atlaskit, Polaris), or native mobile (Apple HIG, Material) — use the right tool for the mechanism, themed to the locked tokens. The router still owns the tokens, the mode declaration, the eight-state discipline, and verification. Handing off the grid engine is correct; applying landing-page taste to a data grid is not.

## 11. What is genuinely out of scope

`ab-testing` · `seo-audit` · `programmatic-seo` · `site-architecture` · `competitors` · `popups` · `free-tools` · `directory-submissions` · `sales-enablement` · `churn-prevention` · `community-marketing` — marketing skills that may *inform* a page's content but never its visual direction.

Realtime collaborative UI (presence, cursors, operational transforms) is a different problem class; say so rather than treating it as a styling job.

## 12. Delegated builds — briefing a build agent (2026-09-06, from the r6 post-mortem)

A build delegated to a fresh agent (headless `claude -p`, or an Agent-tool subagent) fails
in one specific way: it reads the brief as a spec to implement, skips every reference the
brief did not name, and ships a one-shot. r6 (2026-09-06) produced six such builds. The
rules below are the fix, and the reference floor in `design-gate.py` enforces the first one.

**The brief never goes below the floor.** A brief may narrow *which* catalogue entries to
study, never the floor itself: `design-catalogue/TASTE.md`, `design-catalogue/FEEDBACK.md`,
`references/reference-lock.md`, each named entry's `entry.md` + `fold.webp` + `slices/` +
`extract/<site>-DESIGN.md`, and on a scroll brief `references/scroll/README.md`,
`grammars.md`, `devices.md`, `feel-and-fingerprint.md` + `house-physics.md` Motion. Never
write "read nothing else" about `design-catalogue/` or `references/`. List the floor files
in the brief explicitly, in reading order.

**Rounds, not one-shot (Persuade/Experience surfaces).**
1. *Reference digest, no HTML.* Deliverable `BRIEF.md`: three lines per floor file (what it
   says, what is taken, what is rejected), the reference lock, the named authority
   (TASTE.md § 1) and what steps down for it, the feeling curve, the device table
   (≥4 families), the fingerprint against every sibling and registry row, the `?preview=`
   plan. The orchestrator reads it against the files before round 2 begins.
2. *Fold + set-piece only.* Screenshots in both motion modes (`reduced_motion`
   `no-preference` and `reduce`), read as pixels by the orchestrator, and compared:
   under F-011 they must match.
3. *The whole page*, plus `emil-design-eng` on transitions and the copy gate on own strings.
4. *Orchestrator findings + the reviewer trio* → 5. *Fixes*, until a full pass is clean.

**The target-picture gate (the orchestrator's own brief).** Before a concept is briefed:
(1) name one authority and list what steps down for it; (2) test it against TASTE.md § 5's
rejected list and the AI-trope list — glass card with telemetry, dashboard over a photo,
badge rows, gradient pill, three equal cards, spotlight cursors; (3) one display-scale
element per screen; (4) fingerprint ≥4/6 against earlier rounds. Write the gate out, filled
in, in the concept file. r6-K3 (glass card) would have fallen on (2); r6-K2 on (1) and (3).

**Infrastructure is the orchestrator's job.** Ship the photo pack (sourced, credited,
vendored) and any generated motion material with the brief; point the agent at
`scripts/serve.py`; the builder makes no Unsplash calls and writes no server.

**Judge in motion mode — now a regression test.** The orchestrator captures every round
with `reduced_motion="no-preference"` *and* `"reduce"`, reads both, and the two sets must
be **identical**. Before F-011 the point was to label which mode an image showed, because
a reviewer whose OS had animations off saw only the fallback (r6: that is what happened,
and nobody noticed for a whole round). There is no fallback any more, so a difference
between the two sets is not a labelling problem — it is a reduced-motion branch that has
crept back into the build, and it fails the round. `shoot.py`, `measure.py` and
`shoot_slices.py` default to `"reduce"` for exactly this reason: the hostile setting is
the one worth photographing.

## 2026-09-03 rework (v3) — what changed in the orchestration

**New phases.** Step 1b now ends with a reference lock and a decision ledger (`reference-lock.md`), sourced first from the design catalog (`~/design-catalog`, `Skill(design-catalog)`). Step 2b (Persuade/Experience only) picks a page grammar, writes the feeling curve, runs the fingerprint gate against the vault registry, chooses scroll devices from the vendored scroll-craft engine, and runs the bake-off board (`shotgun.md`, `scripts/board.py`) before Step 4. Step 5 gained four passes: `a11y-audit`, `verbs/critique.md`, `review-animations` + `scroll_verify.py`, and the three reviewer subagents (`design-critic`, `design-a11y-reviewer`, `design-heuristics`) reconciled by accessibility > usability > brief > personas.

**New skills in the catalog.** `a11y-audit` (eight passes, three scripts, principle catalog from Interfaces, designpowers, inclusive-design-skills, designer-skills), `design-catalog` (add/query references), `animate` / `review-animations` / `improve-animations` / `find-animation-opportunities` / `prototype` / `apple-design` / `animation-vocabulary` / `pick-ui-library` (Emil Kowalski, refreshed 2026-09-03; `emil-design-eng` keeps the local trigger description).

**Boundaries that changed.** `hallmark` no longer auto-invokes (`disable-model-invocation`); `frontend-design` is not loaded (two of its rules live in the craft floor); `super-intelligence:design` is user-invocable-only so only the vault `design` competes for auto-invocation. The `audit` verb is now `verbs/review.md` (one ranked table, cap 15, escalation triggers always HIGH, Block/Approve); `verbs/audit.md` stays the slop audit inside it.

**Collisions resolved.** Refero's anti-slop tells 4/7/8 became gates 89–91; its "calm editorial serif" tell is our editorial-print register, so that register now needs two departures from the default look. designpowers' build agents are not adopted (they set direction); its reviewers are, as read-only Sonnet subagents. scroll-craft's engine is never edited per project; its `count` device is only for real numbers; video scrub is opt-in (ffmpeg).

**Hooks.** Arm/disarm: `design-intent.py` classifies prompts high/medium/none; per-edit and Stop hooks act only in an armed session (or on a 0-locked contract); the Stop report's gap counts only code-strong craft routes that were neither loaded nor read. Evidence: `tests/ab/*/verdict.md` and `tests/intent_corpus.jsonl` in `anti-slop-design`.
