# The Router, in plain English

The full master skill is in [`skills/design/SKILL.md`](skills/design/SKILL.md). This page is the version you read first.

## What it is

A single Claude Code skill that you install at `~/.agents/skills/design/`. Once it's there, typing the word **design** anywhere in a brief (in any language — `design`, `designa`, `redesign`, "polera", "make me a landing page", "fix this AI-looking page") fires the router.

## What it does, in six steps

1. **Detects the task type.** Ground-up build? Redesign an existing site? Polish a finished one? Match a reference URL? Audit accessibility? The router classifies into one of 7 lanes.

2. **Forces a named aesthetic lane before any token is picked.** Not "modern and minimal." Something like *"Klim Type Foundry orange drench"*, *"Bloomberg Terminal meets Swiss specimen"*, *"Liquid Death acid maximalism"*. Unnamed ambition becomes beige; the router refuses to proceed without a name.

3. **Runs both slop tests.** First-order: could someone guess your palette from the category alone? (observability → dark blue, healthcare → white + teal, fintech → navy + gold, AI-SDR → egg-shell + navy). Second-order: could they guess the aesthetic family from category-plus-anti-references? ("Tech that's not Stripe-minimal → editorial-typographic"). If either is *yes*, rework.

4. **Layers the right specialist** for the chosen lane:
   - Brand work → **Impeccable** is the spine
   - Awwwards / GSAP scrolltelling → also load **gpt-taste**
   - Apple/Linear haptic detail → also load **high-end-visual-design**
   - Premium SaaS / Bento 2.0 → also load **design-taste-frontend**
   - Editorial / workspace-platform → **minimalist-ui**
   - Swiss / brutalist / tactical → **industrial-brutalist-ui**
   - Reference URL provided → run **extract-design** first to lock the tokens

5. **Enforces five hard bans** that win over anything underneath:
   - **No Inter** (or DM Sans, Plus Jakarta, Outfit, Space Grotesk, etc. — see Impeccable's reflex-reject list)
   - **No centered hero stack** (kicker + headline + subhead + two-buttons + screenshot)
   - **No 3-column card grid** with icon + title + body
   - **No hero-metric template** (big number + small label + supporting stats + gradient accent)
   - **No `#fff` / `#000`** as default. Tinted neutrals in OKLCH.

6. **Always ends with `impeccable polish`** — a final pass that aligns the work to the design system and resolves drift by *root cause*, not symptom.

## What it doesn't do

It's a router, not a builder. It does not replace any of the upstream skills it composes. It does not invent visual rules. It is the answer to the question *"I have 30 design skills installed and the model still produces AI-generic output — what's wrong?"* — and the answer is *"none of them were firing reliably, and none of them were composed in the right order."* The router fixes that. The taste comes from the upstreams.

## Install

Copy the file:

```bash
mkdir -p ~/.agents/skills/design
cp skills/design/SKILL.md ~/.agents/skills/design/SKILL.md
```

Then install the upstreams it composes — see [`attribution/UPSTREAMS.md`](attribution/UPSTREAMS.md) for the five repos and their one-line install commands.

## Use

In any Claude Code session, prefix a design brief with the word `design`:

```
design a premium landing page for [your brief]
```

Or any synonym in any language. The router fires and runs the chain.
