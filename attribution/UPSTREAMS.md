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
