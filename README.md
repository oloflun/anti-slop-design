# Anti-Slop Design — one router, the right skills, every time

> Three landing pages, three aesthetic lanes, **one master skill** routing the right specialists from a stack of 32 audited Claude Code design skills. Built in ~20 minutes in a single Claude Code session, Opus 4.7. The work that the upstreams do is excellent; this repo's only contribution is making sure the right one fires for each task.

[**→ Live demos**](#the-proof--three-sites)  ·  [**The router (300 lines)**](skills/design/SKILL.md)  ·  [**Full audit of 32 skills**](AUDIT.md)  ·  [**Credits to every upstream**](attribution/UPSTREAMS.md)

---

## The problem in one image

<table>
<tr>
<td align="center"><sub><b>What every AI coding tool ships by default</b></sub></td>
</tr>
<tr>
<td><img src="shots/before-ai-slop-desktop.png" alt="Generic AI SaaS landing — Inter, pill nav, gradient text, chart card with metric grid, 3 icon-title cards, big-number row, gradient hero" width="900"></td>
</tr>
</table>

Inter, sticky pill nav, gradient text, chart card on the right, 4-column metric grid with tiny captions, 3-column "feature" cards with icon + title + body, big-number row, gradient CTA. Familiar? It should be. Every AI tool produces this. Every AI tool produces *exactly* this.

The problem isn't that the skills to do better don't exist — they do, and they're brilliant — it's that the model can't reliably pick the right one from 30+ overlapping descriptions, and even when it does, it doesn't compose them in the right order, and even when it does *that*, the model still falls back to base AI taste at the first ambiguity. Premium skills installed; AI-slop shipped.

This repo's answer: one **master router skill** that detects the task, names an aesthetic lane, runs slop tests, layers the right specialist, blocks the bans, and forces a polish pass. Type `design` and it fires.

## The proof — three sites

Each was produced through the router in this repo, from a single prompt, in a different aesthetic lane. Each lives behind a `/` URL on the deployed showcase. **None of them could be confused for the page above.**

| Site | Aesthetic lane | Specialists the router fired | Demo |
|---|---|---|---|
| **Calyx** — Stockholm botanical atelier | Editorial luxury minimalism (cream + charcoal + layered botanical photography, Cardo italic display) | Impeccable + high-end-visual-design (Editorial Luxury archetype) | [Live](https://anti-slop-design.vercel.app/calyx) · [Source](sites/calyx.html) |
| **Hyperborea Summit MMXXVI** — speculative-futurist conference | Drenched dark navy + amber, bilingual EN/SV/JP, illustrated SVG sun-disc speaker portraits | Impeccable + gpt-taste (AIDA scrolltelling) + design-taste-frontend (perpetual micro-motion) | [Live](https://anti-slop-design.vercel.app/hyperborea) · [Source](sites/hyperborea.html) |
| **Hōrai** — a three-sister restaurant, Stockholm | Drenched warm (rice-paper cream + lacquer red, monumental Cinzel display, literary Vollkorn body, large food photography for a high-end Asian-fusion dining room) | Impeccable + designpowers/design-taste | [Live](https://anti-slop-design.vercel.app/horai) · [Source](sites/horai.html) |

### Screenshots

<table>
<tr>
<td align="center" width="33%"><sub><b>Calyx</b> — editorial luxury</sub></td>
<td align="center" width="33%"><sub><b>Hyperborea</b> — speculative-futurist</sub></td>
<td align="center" width="33%"><sub><b>Hōrai</b> — drenched warm</sub></td>
</tr>
<tr>
<td><img src="shots/calyx-desktop.png" alt="Calyx — botanical photography hero with italic editorial overlay"></td>
<td><img src="shots/hyperborea-desktop.png" alt="Hyperborea — drenched dark navy with amber rising sun, italic Italiana display headline"></td>
<td><img src="shots/horai-desktop.png" alt="Hōrai — rice-paper cream warm-drench restaurant landing with Cinzel display headline and atmospheric food photography"></td>
</tr>
<tr>
<td><img src="shots/calyx-mobile.png" alt="Calyx mobile" width="300"></td>
<td><img src="shots/hyperborea-mobile.png" alt="Hyperborea mobile" width="300"></td>
<td><img src="shots/horai-mobile.png" alt="Hōrai mobile" width="300"></td>
</tr>
</table>

## v2 — the rebuild (2026-07-27)

The version above shipped three good sites and then failed in real use. Three reasons, all root causes rather than tuning problems.

**It fired once per turn, not once per edit.** Guidance arrived at the top of a prompt; design decisions happen sixty tool calls later. It held at the start of a session and drifted after.

**It was a table of contents, not a procedure** — six hops from brief to any actual taste content, and no method at the front door, so the model improvised one.

**Its own specialists overwrote the brand.** `minimalist-ui` hardcodes Notion's palette; `industrial-brutalist-ui` declares `#E61919` "the ONLY accent color"; `high-end-visual-design` ships three fixed archetypes. Routing to those *as direction-setters* is how a client's identity became someone else's house style.

### The rule now

> **Brand derives direction. Skills supply craft. Themes are the last resort.**

### The verb

Classified first, because the wrong *procedure* costs more than the wrong component skill. Eight verbs (English + Swedish), each routed to its owner: **build · redesign · audit · polish · study · explore · system · verify**. Re-fires when the verb changes, not once per session.

Redesign is the contested one — three procedures claim it, and they work only in sequence: mode detection → tier gate → page shape. Precedence in [`skill-orchestration.md`](skills/design/references/skill-orchestration.md).

### The gate

First tier with evidence wins; lower tiers never run.

| Tier | Condition | Invention |
|---|---|---|
| **0 · Locked** | `DESIGN.md` **with token frontmatter** → inherit; gate enforces mechanically | None |
| **0 · Prose** | `DESIGN.md` without parseable tokens → authority, but the gate is **blind** | None |
| **1 · Derive** | Logo, brand hex, deployed site, tailwind colours → derive from that evidence | Extension only |
| **2 · Reference** | A URL or screenshot → study it, borrow principle not pixel | Recomposition |
| **3 · Invent** | Genuinely nothing, or "wing it" → invent. Themes live here | Full |

Tier 0-prose exists because five skills write `DESIGN.md` in three incompatible formats. Reporting `0-locked` on file existence alone made the system claim *"LOCKED, inherit"* while enforcing nothing — `#FF00FF` and Comic Sans passed silently. Write `DESIGN.md` only through `impeccable document` or `brand-system`.

### The mode

Marketing or product, detected automatically. Dashboards, admin, settings, tables and editors route to **Operate mode** — same tokens, different register (one font family, Restrained colour, 150–250ms state-only motion, density over expression). Marketing references don't load there. See [`product-surfaces.md`](skills/design/references/product-surfaces.md).

### The hooks

```
UserPromptSubmit    design-intent.py        gate order + this project's locked tokens
PreToolUse  write   design-gate.py          DENY contract violations before they land
PreToolUse  browser design-verify-gate.py   inspection discipline before the first look
PostToolUse write   design-route.py         name the right skill for what was written
PostToolUse Skill   design-telemetry.py     attribute every skill call to its component
Stop                design-stop.py          deep detector pass + the session report
```

### The telemetry

Every session writes a report. The number that matters is the **route-vs-invocation gap** — how often the router named a skill and nothing loaded it. That is the direct measurement of the original failure, and it has to be zero. A build that looks right but ships an empty ledger has not passed; it got lucky.

Full explainer in [ROUTER.md](ROUTER.md). Verification: `python verify-design-system.py` (60 mechanical checks).

## The audit — what got picked, what got demoted

Out of 32 design-related skills installed on my machine (across `~/.agents/skills/` and `~/designpowers/skills/`), the router relies on five. The rest are either redundant, niche, project-locked, or process-heavy. The full audit table with per-skill scores on a five-axis rubric (anti-slop teeth / aesthetic ceiling / execution fidelity / routing clarity / maintenance cost) is in [AUDIT.md](AUDIT.md).

| Rank | Skill | Verdict |
|---|---|---|
| 1 | Impeccable | Primary engine — strongest anti-slop teeth, register-aware, 22 sub-commands |
| 2 | design-taste-frontend (taste-skill) | Anti-bias enforcer with Bento 2.0 + 5-card archetypes |
| 3 | high-end-visual-design (taste-skill) | Apple/Linear detail vocabulary (Double-Bezel, button-in-button, Variance Engine) |
| 4 | gpt-taste (taste-skill) | Awwwards lane — AIDA + GSAP scrolltelling + 2-line H1 iron rule |
| 5 | extract-design | URL → tokens (the only skill that operates on existing sites instead of briefs) |
| 6–14 | minimalist-ui, industrial-brutalist-ui, polish, redesign-existing-projects, brandkit, imagegen-frontend-web, image-to-code, designpowers/design-taste, designpowers/motion-choreography | Conditional / phase-specific |
| 15–26 | (taste-feedback, ui-composition, designpowers-critique, vercel-composition-patterns, vercel-react-best-practices, web-design-guidelines, ui-ux-pro-max, others) | Demoted — process-heavy, accessibility-led, or compliance-checklists that cap aesthetic ceiling |
| 27–32 | (using-designpowers, stitch-*, design-md, react-components, webpage-builder) | Skip unless project demands them (welcome-ritual overhead, Stitch MCP required, project-locked) |

The top picks are the same five that this repo composes. The router is the routing layer; **the upstreams are where the taste lives**.

## Credits — please star these repos

The five upstreams the router composes, with verified star counts at publish time:

| Repo | Stars | License | What it provides |
|---|---:|---|---|
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 29.2k | Apache 2.0 | The engine: 22 sub-commands, brand vs product register, named reflex-reject font + aesthetic-lane lists, polish + critique flow |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 18.4k | MIT | design-taste-frontend, gpt-taste, high-end-visual-design, minimalist-ui, industrial-brutalist-ui |
| [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) | 5.6k | Apache 2.0 | Stitch MCP integration (loaded only when user opts in to Stitch) |
| [Manavarya09/design-extract](https://github.com/Manavarya09/design-extract) | 2.8k | MIT | URL → 8 token output files via `designlang` npm |
| [Owl-Listener/designpowers](https://github.com/Owl-Listener/designpowers) | 175 | MIT | 9-agent inclusive design workflow + taste calibration + motion choreography |

Detailed credits, per-skill descriptions, and install commands in [attribution/UPSTREAMS.md](attribution/UPSTREAMS.md).

## Install

```bash
git clone https://github.com/pbakaus/impeccable ~/.agents/skills/impeccable
git clone https://github.com/blader/humanizer ~/.agents/skills/humanizer
git clone https://github.com/Leonxlnx/taste-skill ~/.agents/skills/taste-skill
cp -r skills/design skills/design-verify skills/brand-system ~/.agents/skills/
cp .claude/hooks/design*.py ~/.claude/hooks/
python verify-design-system.py
```

Then wire the six hooks into `~/.claude/settings.json` (see [ROUTER.md](ROUTER.md)) and type a design brief — no trigger word needed, in any language.

Kill switch: `DESIGN_HOOKS_DISABLED=1`. Gate blocking instead of advisory: `DESIGN_GATE_BLOCKING=1`.

## The honest footnote

This whole thing — the audit of 32 skills, the router skill, three full landing pages, screenshots at desktop + mobile, the write-up — was produced in a single Claude Code session, Opus 4.7 high, **wall-clock under 20 minutes**. Built on a Windows machine, Tailwind CDN, Google Fonts, Chrome headless for screenshots. No build pipeline. No CI. No Next.js scaffolding.

The output is not magic. The output is the upstreams above, composed correctly, for the first time. **Star them.**

---

<sub>Built by [@oloflun](https://github.com/oloflun). MIT for the routing layer; upstreams under their own licenses. The Snipra brand referenced in some session logs is private and intentionally not in this repo — its rebuild lives offline, in my drawer, until further notice.</sub>
