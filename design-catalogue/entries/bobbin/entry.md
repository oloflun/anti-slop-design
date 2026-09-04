---
title: "Bobbin (by TutorCruncher)"
url: https://withbobbin.com/
source_url: https://withbobbin.com/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/67e166cc185aa719-screenshot-upload.webp
category: product-focused
category2: ""
family: yellow-glass-tutor-console
dna: "EdTech desk photography x glass status card"
register: modern clean
grammar: live surface
lane: "A warm desk photograph carries a floating glass status card mid-hero, then a cream accordion of features sits beside a live analytics-dashboard screenshot"
mode: persuade
traits: ["yellow-black brand accent", "floating glass status card on photo", "roman headline with one highlighted phrase", "cream accordion feature panel", "dashboard analytics screenshot as proof", "logo trust row", "dual typeface (sans UI + serif accent)", "parent brand credited in the subtitle"]
palette: ["#F5C518", "#151515", "#F2EDE1", "#FFFFFF", "#8A6A3B"]
type: ["GT Standard", "GT Alpina"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The hero photograph — a tutor at a desk, mid-lesson — is doing ordinary work
until a glass status card ("Transcribing in progress," with duration and word
count) floats over it. That single card converts a generic "person working"
stock photo into a specific claim: the product is listening to this exact
moment. The headline pairs a plain roman line with one phrase set in the brand
yellow ("Built with **Bobbin**"), so the accent colour marks the product name
and nothing else.

Trust and proof are kept close together rather than in separate sections: a
"trusted by 1,800+ tutoring companies" logo row sits directly under the hero,
and just below that, a cream feature panel pairs a plain accordion list (four
capabilities, one expanded by default) against a real analytics screenshot —
engagement metrics, a conversation-insights bar chart, per-student rows. The
expanded accordion item and the screenshot are visually adjacent, so the one
feature being described is the one feature being shown.

Two typefaces carry two jobs cleanly: a grotesk sans for all UI chrome, labels
and navigation, and a serif for larger display and pull-style moments —
GT Standard for structure, GT Alpina for warmth — which keeps the product feeling
credible (sans) without losing personality (serif) entirely to software-default
type.

## What to borrow (principle)

- **Float one small status card over the hero photo** naming the exact thing the
  product is doing right now, rather than a generic feature callout.
- **Highlight the product name in your accent colour within the headline**, and
  nowhere else, so the colour stays meaningful.
- **Pair an accordion feature list directly beside a matching screenshot**, with
  the expanded item and the visible screen showing the same capability.
- **Credit a parent brand in a small subtitle** under the product wordmark if the
  product is a spin-out — it borrows trust without needing its own case studies
  yet.

## What to leave

- A default-expanded accordion item competing for attention with the hero's own
  glass card risks giving the visitor two "look here" moments in one screen.
- The cream feature panel and the yellow-black hero are strong individually but
  meet at a hard edge; a shared texture or gradient transition would soften the
  section break.

## Signature move

The glass status card as hero proof: rather than a floating UI mockup showing
the whole product, one small card shows a single live action ("Transcribing in
progress," with a duration counter and student/topic counts) directly over the
photograph. It's a narrower, more credible claim than a full dashboard preview.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed.
Most UI transitions ride a fast, near-uniform `300ms` on Tailwind's default
ease-out (`cubic-bezier(0.4,0,0.2,1)`/`cubic-bezier(0,0,0.2,1)`, 152 uses
combined) — this is a Tailwind/shadcn-driven page, not a bespoke motion
system. Confirming the "status card" read: `cta-unlock-in` and `cta-fade-up`
slide/fade a card up into place, `cursor-blink` ticks a text cursor on/off
(the "live" typing feel), and `border-rotate` spins a conic gradient around a
card edge as a glow. The one outlier token is `xxl` at a full `8s` — almost
certainly the cursor-blink or a slow ambient loop, not a content reveal.

| token | value | role |
|---|---|---|
| `xs`–`md` | 150–300ms | default UI/card transitions |
| `lg` | 450ms | larger surface transitions |
| `xxl` | 8s | ambient loop (cursor/glow) |
| custom (Tailwind) | `cubic-bezier(0.4,0,0.2,1)` | dominant (112 uses) |
| ease-out | `cubic-bezier(0,0,0.2,1)` | secondary (40 uses) |

## Brief

Build a yellow-and-black EdTech product page. Open on a warm, documentary photo
of the user mid-task, with one small glass-morphic status card floating over it
naming a specific live action and its metrics. Set the headline in a plain
grotesk sans with exactly one phrase — the product name — highlighted in the
brand yellow. Directly under the hero, run a trust logo row, then a cream
section pairing a four-item accordion (one open by default) against a real
analytics screenshot showing the same feature the open item describes. Use a
serif for occasional display warmth against an otherwise all-sans UI.

## Image recipe

Documentary photo of a person mid-task at [SUBJECT] — a desk, natural window
light, warm tones, genuine focus/absorption in their expression, workspace
details (notebook, plant, laptop) visible but not staged, shot at a slight
angle rather than head-on.

## Photo search

Unsplash first, Pexels second.
- "person working desk natural light focused"
- "tutor writing notebook warm light"
- "remote work desk candid documentary"

## Reference lock

Primary reference/direction: Bobbin — glass status-card hero over documentary desk photography, accordion features paired with a live analytics screenshot.
Preserve (3-5 traits): one small glass-morphic status card floating over the hero photo, naming a specific live action rather than a generic feature; brand-yellow highlight reserved for the product name inside the headline; accordion feature list with the open item paired directly beside a matching screenshot; trust logo row placed immediately under the hero.
Borrow only (1-2): the parent-brand subtitle under the wordmark; the serif accent typeface for occasional display warmth.
Role rules: only one floating status card per hero; accent yellow never used for body text or large fills, only the product-name highlight and small UI chrome; accordion default-open item must match whatever screenshot sits beside it.
Media strategy: photo:unsplash — warm, documentary, single-subject work-in-progress photography only; no posed stock-office imagery.
Reject: a full dashboard mockup replacing the single-action status card; more than one accent colour; an accordion with no matching visual proof.
Token commitments: yellow `#F5C518`, ink `#151515`, cream `#F2EDE1`, white `#FFFFFF`, warm-brown `#8A6A3B`; sans `GT Standard` for UI/labels, serif `GT Alpina` for display/warmth accents.
