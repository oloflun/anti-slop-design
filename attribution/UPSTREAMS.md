# Upstream Credits

The router skill in [`skills/design/SKILL.md`](../skills/design/SKILL.md) does not invent any visual rules. It selects and sequences existing Claude Code skills authored by other people. **All of the credit for the visual quality of the three demo sites belongs to the upstreams listed below.** This repo's only contribution is the routing layer that picks the right one for each task.

All five upstreams were verified live at the time of publishing (April 2026). Star counts are best-effort snapshots; check the repos for current numbers.

## The five composed skills

### 1. Impeccable — the engine

- **Repo:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- **Author:** [@pbakaus](https://github.com/pbakaus) (Philipp Bakaus, ex-Google, ex-Sencha)
- **License:** Apache 2.0
- **Stars at publish time:** ~29.2k
- **Description (from the repo):** "A design vocabulary with 23 commands and anti-pattern rules to help AI models create better frontend designs." Based on Anthropic's original `frontend-design` skill.
- **What the router uses it for:** Primary engine. Provides PRODUCT.md / DESIGN.md context loading, register detection (brand vs product), the brand register's *named reflex-reject font list* and *reflex-reject aesthetic lanes*, the second-order slop test, and 22 sub-commands (`craft`, `shape`, `polish`, `critique`, `audit`, `bolder`, `quieter`, `distill`, `harden`, `onboard`, `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive`, `clarify`, `adapt`, `optimize`, `live`, `extract`, `document`, `teach`).
- **Install:** `git clone https://github.com/pbakaus/impeccable ~/.agents/skills/impeccable` (or whatever your harness expects). See its README for the live-browser pin/unpin commands.

### 2. taste-skill — the anti-bias enforcer (and most of the specialist lanes)

- **Repo:** [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- **Author:** [@Leonxlnx](https://github.com/Leonxlnx)
- **License:** MIT
- **Stars at publish time:** ~18.4k
- **Description:** "Portable agent skills that upgrade AI-built interfaces with stronger layout, typography, motion, and spacing instead of generic-looking UIs."
- **Skills used by the router from this library:**
  - **`design-taste-frontend`** — the anti-bias enforcer. Bans Inter, gradient text, 3-column card layouts, oversized H1s, "Acme/Nexus/SmartFlow" placeholder names, and many other AI tells. Provides the Bento 2.0 architecture spec, the 5-card archetypes with named perpetual micro-animations, and a strict pre-flight checklist.
  - **`gpt-taste`** — Awwwards-tier with mandatory `<design_plan>`, AIDA structure, the 2-line H1 iron rule, gapless `grid-flow-dense` bento, GSAP ScrollTrigger choreography (pinning, scrubbing reveals, card stacking), and the meta-label ban.
  - **`high-end-visual-design`** — Apple/Linear-tier detail vocabulary (Double-Bezel nested architecture, button-in-button trailing icons, Variance Engine with Ethereal Glass / Editorial Luxury / Soft Structuralism archetypes, magnetic hover physics).
  - **`minimalist-ui`** — editorial workspace lane (warm monochrome, ultra-flat, muted pastels).
  - **`industrial-brutalist-ui`** — Swiss + tactical-terminal lane (for declassified-engineering tones, tactical telemetry surfaces).
- **Install:** clone the repo and either drop the individual skill folders into `~/.agents/skills/` or follow its README.

**Upgraded to v2 on 2026-07-27.** Upstream restructured the repo: v1 is preserved as `taste-skill-v1` (install name `design-taste-frontend-v1`), and each skill now lives in its own renamed directory (`taste-skill`, `brutalist-skill`, `minimalist-skill`, `gpt-tasteskill`, `soft-skill`, `redesign-skill`, `output-skill`) while keeping the same `name:` in frontmatter. Verified: `gpt-taste`, `minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design`, and `redesign-existing-projects` are **byte-identical** between v1 and v2 — only `design-taste-frontend` was rewritten (226 → 1206 lines).

What v2 adds, and where this router uses it:

- **Section 9.F production-test tells** → ported as gates 66–88 in [`production-tells.md`](../skills/design/references/production-tells.md). Roughly twenty empirically-derived micro-decoration signatures (hero version labels, numbered eyebrows, middle-dot chains, decorative status dots, `<br>`-broken italic headlines, rotated text, crosshair decoration, div-based fake product UI, fake version footers, performative-craftsman labels, locale/weather strips, pills on images, photo-credit captions, live-stock counters, hero decoration strips, floating corner sub-text, `border-t`+`border-b` rows, filled-track scoring bars, scroll cues) that Hallmark's gates 1–57 and impeccable's detector do **not** already catch.
- **Section 9.G em-dash ban** → gate 75. The strictest of the three em-dash rules in this system, and the one that wins.
- **Section 11 redesign protocol** → [`scope-discipline.md`](../skills/design/references/scope-discipline.md). Mode detection (greenfield / preserve / overhaul), audit-before-touching, preservation rules, modernisation levers in priority order, and the never-change-silently list.
- **Section 4.2 premium-consumer palette ban** → [`invention.md`](../skills/design/references/invention.md). A fourth calibration cluster with concrete banned hex families, extending impeccable's `cream-palette` prose into something checkable. Serif discipline from 4.1 folded in alongside.
- **Sections 0, 1, 2, 13** → [`process.md`](../skills/design/references/process.md). The one-line "design read", the three intensity dials, the brief→official-design-system map (Fluent / Material / Carbon / Polaris / Atlaskit / Primer / GOV.UK / USWDS / Radix / shadcn), and the out-of-scope boundary.

`design-taste-frontend` is now routed for page-scope landing, marketing, and portfolio surfaces — see [`component-routing.md`](../skills/design/references/component-routing.md). As with every other specialist, it supplies craft and structure only; at Tiers 0–2 it may not pick the palette.

### 3. Designpowers — the design-process layer

- **Repo:** [Owl-Listener/designpowers](https://github.com/Owl-Listener/designpowers)
- **Author:** [@Owl-Listener](https://github.com/Owl-Listener) (MC Dean)
- **License:** MIT
- **Stars at publish time:** ~175 (early; deserves more)
- **Description:** "An agent design team you control: 10 agents that run an inclusive design process while you direct."
- **What the router uses it for:** The taste-calibration step (`design-taste` for emotional target + craft standards + quality bar), `inspiration-scouting` for cross-domain references, and `motion-choreography` for animation discipline.
- **Note:** Designpowers is its own complete workflow system with 9 agents (design-lead, design-critic, motion-designer, accessibility-reviewer, design-scout, content-writer, design-strategist, heuristic-evaluator, inspiration-scout, asset-producer). The router only composes a few of its skills, but the whole system is worth running on its own merits — especially for accessibility-led projects.
- **Install:** see the repo README; provides drop-in installers.

### 4. design-extract / designlang — the URL → tokens utility

- **Repo:** [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract)
- **Author:** [@Manavarya09](https://github.com/Manavarya09)
- **License:** MIT
- **Stars at publish time:** ~2.8k
- **Description:** "Extracts any website's complete design system with one command, generating DTCG tokens, Tailwind configs, Figma variables, and more."
- **What the router uses it for:** The only skill that operates on existing sites instead of briefs. When I name a reference URL, `extract-design <url>` runs `npx designlang` and produces 8 output files (markdown design language, Tailwind config, CSS variables, shadcn theme, Figma variables, React/CSS-in-JS theme, W3C design tokens, visual HTML preview) plus a WCAG accessibility score.
- **Install:** `npm install -g designlang` plus the skill wrapper from the repo.

### 5. stitch-skills — the Google Stitch integration

- **Repo:** [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- **Author:** Google Labs Code
- **License:** Apache 2.0
- **Stars at publish time:** ~5.6k
- **Description:** "A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility with coding agents such as Antigravity, Gemini CLI, Claude Code, Cursor."
- **What the router uses it for:** Only loaded when I explicitly choose Stitch as my generation tool. Provides `stitch-design` (unified entry point), `stitch-design-taste` (Stitch's own anti-slop DESIGN.md generator), and `stitch-loop` (autonomous baton-passing build loop). The router treats Stitch as an alternative branch — if the Stitch MCP server is not connected, these skills don't load.
- **Install:** see the repo. Requires the Google Stitch MCP server.

## What this repo contributes on top

A single ~250-line master skill at `skills/design/SKILL.md` that:

1. **Detects the task type** and routes to one of 7 lanes (ground-up build / redesign / polish / reference-driven / component / direction-only / audit).
2. **Forces a *named* aesthetic lane** before any tokens are picked — the failure mode that ate every previous attempt.
3. **Runs both slop tests** (first-order category-reflex and second-order aesthetic-lane) as gates, not as suggestions.
4. **Layers the right specialist** from the five upstreams above, in the right order, every time.
5. **Enforces five hard bans** that override anything underneath: no Inter, no centered hero stack, no 3-col icon cards, no hero-metric template, no `#fff`/`#000`.

That's it. The router is a routing layer. Every word of visual taste it relies on comes from someone else's repo.

## How to support the upstreams

- **Star the repos.** That's how Claude Code skills get discovered.
- **File issues with examples** when their rules misfire. The taste-skill anti-bias list and Impeccable's reflex-reject aesthetic-lane list both update over time; the authors take real-world failure screenshots seriously.
- **Send PRs that add named aesthetic lanes** to Impeccable's brand register and reflex-reject list. The internet has more saturated aesthetic families than any one author can track.
- **Sponsor the authors directly** if you find their skills load-bearing. They're tracked under their GitHub handles above.

---

# Addendum — 2026-07-27 rebuild

The router was rebuilt around a brand-derivation gate and a hook chain. Three
upstreams were added and one was upgraded. The routing layer is still this
repo's only contribution; all visual rules come from the sources below.

## 6. Hallmark — the front door's spine

- **Repo:** [Nutlope/hallmark](https://github.com/Nutlope/hallmark)
- **Author:** [@Nutlope](https://github.com/Nutlope) (Hassan El Mghari)
- **License:** MIT
- **What the router uses it for:** Hallmark's `SKILL.md` structure became the
  front door — six cross-verb disciplines, scope check before anything else,
  pre-flight scan of existing code before asking the user anything, component
  branch, implementation safety rail, and the 57 numbered slop gates. All 105
  of its reference files are ported **byte-identical** into
  `skills/design/references/` and are the source of truth; nothing was
  abridged. `structure.md`'s six-axis fingerprint is kept and repurposed as a
  variety check *within* a locked brand.
- **What we changed:** its 20-theme catalog, 21 macrostructures and 50
  component archetypes are kept in full but **demoted to Tier 3**. Hallmark
  defaults to the catalog silently; this router reaches it only when there is
  no brand evidence at all, or when the user explicitly asks for a pick. Its
  `references/X.md` loads became `Skill(X)` invocations against the installed
  skill library.
- **Verify:** `python verify-design-system.py` diffs every ported file against
  upstream and fails the build on any content-bearing deletion.

## 7. marketingskills — stage 1 of the copy gate

- **Repo:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- **Author:** [@coreyhaines31](https://github.com/coreyhaines31)
- **What the router uses it for:** the `copywriting` skill runs on every
  user-facing string — page purpose, audience, offer, traffic context; headline
  formulas; `[Action Verb] + [What They Get] + [Qualifier]` CTAs; the five
  style principles; the bans on exclamation points, weak CTAs and buried value
  props.

## 8. humanizer — stage 2 of the copy gate

- **Repo:** [blader/humanizer](https://github.com/blader/humanizer)
- **Author:** [@blader](https://github.com/blader) (Siqi Chen)
- **What the router uses it for:** 33 AI-writing patterns removed after
  `copywriting` has settled structure — em dashes, "delve"/"tapestry",
  negative parallelism, forced rule-of-three, inflated significance,
  promotional adjectives, sycophancy, manufactured drama. Runs in embedded
  mode. Its core constraint is load-bearing: *"Preserve the information, not
  the shape"*, and never invent facts.
- **Applied in every language.** The tells are structural, not lexical, so
  Swedish copy gets the same guides with the equivalent resolved rather than
  skipped.

## 9. Anthropic's Claude Design system prompt

- **Source:** the system prompt of Anthropic's Claude Design product, supplied
  by the user.
- **What the router uses it for**, at full fidelity, each in its own reference:
  - **"Create design system"** → `brand-derivation.md` and the `brand-system`
    skill. This is the Tier 1 procedure — the VISUAL FOUNDATIONS and CONTENT
    FUNDAMENTALS interrogations, the logo-safety rules, the inventory
    discipline, the stop-on-inaccessible-resources rule, and the
    exact-values rule: *"If the kit says 5px, write 5px, not 4px."*
  - **"Frontend design"** → `invention.md`. Tier 3, ported verbatim.
  - **"Hi-fi design"** + workflow + question guidance → `process.md`.
  - **Output and content guidelines** → `scope-discipline.md`.
  - **"Wireframe"** → `wireframe.md`. **"Options"** → `options.md`.
    **"Handoff to Claude Code"** → `handoff.md`.
  - The preview and inspection tool docs → the `design-verify` skill.
- **The scoping line that validates the whole architecture:** its Frontend
  design guidance applies *"when designing frontend/UI work that is NOT
  governed by an existing brand or design system"*, and its Hi-fi design
  guidance calls building from scratch *"a LAST RESORT"*. Aesthetic invention
  is the fallback, not the default — Anthropic's own product agrees.
- **Deliberately not ported:** the Design Component runtime (`.dc.html`,
  `dc_write`, `<x-dc>`), the host-specific tools, and the **inline-styles-only**
  rule — that last one exists because their preview streams, and it would
  defeat the token system in a Next.js or Tailwind codebase. Full list with
  reasons in `skills/design/references/scope-discipline.md`.

## Upgrade: Impeccable v3 → v4.0.2

Impeccable (upstream #1) was upgraded. v4 solves the forced-theme problem
natively and states it directly:

> *"The brief wins. Honor pinned aesthetics, eras, materials, fonts, and
> palettes even when they conflict with a saturated-pattern warning.
> Redirecting a clear brief toward your taste is failure."*

> *"Established world: inherit it. A missing DESIGN.md does not erase a
> coherent identity already present in code; document that identity instead of
> inventing a replacement."*

It also supplies the mechanical layer this router enforces with: **68
deterministic detector rules**, four of which (`design-system-color`,
`design-system-font`, `design-system-font-size`, `design-system-radius`) check
a build against `DESIGN.md` directly. Those are what `design-gate.py` denies
on, so the contract is enforced by the upstream's own parser rather than a
reimplementation here.

**On the v4 "dice":** `scripts/concept-seed.mjs` deals challenger worlds from a
catalog that, per its own source comment, *"does not ship with the skill"* — it
resolves to a paid roll API, then degrades to assignment-only. It is disabled
in this setup outside the explicit no-reference lane, so no external world is
ever dealt.
