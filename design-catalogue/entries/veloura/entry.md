---
title: "Veloura Hotel Template"
url: https://veloura-hotel-template.webflow.io
source_url: https://veloura-hotel-template.webflow.io
captured: 2026-09-04
origin: raw-url
raw: raw/476ae8adcb382cf5-veloura-hotel-template-webflow-io.webp
extract: ok
category: hospitality
category2: luxury-craft
family: chocolate-vignette-boutique
dna: "Boutique hotel serif signage x continuous chocolate-vignette atmosphere"
register: cinematic dark
grammar: continuous world
lane: "One deep chocolate-brown vignette ground persists from the hero through the photo grid and into a warm serif pull-quote, so the whole scroll reads as one dim, candlelit hotel corridor rather than stacked sections"
mode: experience
traits: ["deep chocolate-brown vignette ground", "warm serif display headline", "small-caps tracked nav and kickers", "three-photo interior grid", "pill CTA with icon", "warm pull-quote serif sentence", "room card with arrow link", "consistent warm interior photography"]
palette: ["#2A0800", "#EEE3E0", "#BA6957", "#9E4632", "#703324"]
type: ["Ltremark", "Funnel Display", "Funnel Sans"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

Unlike most of this set, which marks section boundaries with hard colour-field changes,
Veloura keeps one continuous deep chocolate-brown vignette ground running from the hero
through the photo grid and into the pull-quote sentence — the background never resets to
white or a different hue. Because the ground stays constant, the page reads as one dim,
warmly lit space the visitor walks through rather than a series of discrete screens, which
suits a boutique-hotel brief better than hard chapter breaks would.

Typography carries the hierarchy the colour system doesn't: a serif display (Ltremark) at
large size for headlines, small-caps tracked labels for nav and section kickers, and a
plain grotesque (Funnel Sans) for everything else. The serif headline is warm off-white,
never pure white, which keeps it sitting inside the vignette rather than cutting through
it — a small but deliberate restraint that a brighter white would break.

Photography does the only real colour work on the page: three interior shots (a café
banquette, a floral atrium staircase, a champagne pour) sit in a plain three-up grid
directly on the brown ground, each keeping its own warm-toned lighting rather than being
graded to match. Because the surrounding ground is already warm and dark, the photos read
as windows into the same building rather than inserted stock imagery.

## What to borrow (principle)

- **Let one dark, vignetted ground colour persist across multiple scroll sections**
  instead of resetting per section — it reads as one continuous space rather than stacked
  screens, which suits an immersive, atmospheric brief.
- **Keep display type warm off-white, not pure white, against a warm dark ground** so
  headlines sit inside the atmosphere instead of puncturing it.
- **Use a plain, ungraded photo grid and let the vignette ground supply the mood** —
  photography doesn't need heavy colour treatment if the surrounding page is already
  doing the atmospheric work.
- **Reserve small-caps tracked type for structural labels only** (nav, kickers, section
  markers), keeping the serif free to carry every actual sentence.

## What to leave

- A vignette this dark and this consistent risks flattening contrast between adjacent
  photo tiles and their surrounding ground at low screen brightness; worth confirming
  minimum contrast against accessibility guidance before shipping.
- The template-marketplace "Buy the template" pill button sits inside the live hero grid
  in this capture — a marketplace artifact to exclude from any derived build, same caution
  as the Snapifye entry in this set.
- Long serif pull-quote sentences set at a large size against a very dark, low-contrast
  ground (the "Cozy interiors, warm tones..." line) sit close to the comfortable reading
  contrast floor; fine as a short accent line, risky if copy grows.

## Signature move

The persistent vignette: rather than resetting the background between hero, gallery and
quote sections, Veloura keeps one radial dark-brown gradient running the full scroll
length, so the transition between "sections" is invisible — the page feels like one dim
room rather than a sequence of screens.

## Motion

The designlang extract (separate from the static `capture.py` scroll-through) reads the
overall feel as responsive and confirms scroll-linked behaviour. Five durations are in
use, from a near-instant 1ms discrete toggle up to a full 1 second, plus an unnamed 1.2s
transform transition that runs longer than any named token. A single custom easing
family, `cubic-bezier(0.075, 0.82, 0.165, 1)` (8 uses), is a fast-out ease — it commits
most of its motion very early (y already at 0.82 by x=0.075) then eases gently into
place — with no spring or overshoot; it's reserved for a 1.2s transform-plus-background
pairing (likely a hover/parallax move) and a 0.6s padding-plus-opacity pairing (likely an
expanding card or accordion). Everything else — colour, background-colour, opacity,
background-position — uses default browser ease. Only one keyframe (`spin`, a plain
360deg rotation) is defined in the CSS bundle and it does not appear in the "in use" set,
so no dedicated fade/slide keyframe backs the vignette's soft radial glow — a per-section
glow shift, as implied by the still frames, remains unconfirmed rather than disproven
(from designlang extract).

| Duration | Value | Notes |
|---|---|---|
| `instant` | 1ms | discrete overflow toggle |
| `xs` | 100ms | — |
| `sm` | 200ms | colour, background-colour, opacity, background-position |
| `lg` | 600ms | padding (paired with the ease-out curve) |
| `xl` | 1s | border-colour |
| unnamed | 1.2s | transform (paired with the ease-out curve) |
| ease-out | `cubic-bezier(0.075, 0.82, 0.165, 1)` | fast-out, no overshoot; 8 uses |

## Brief

Build a boutique-hotel landing page on one continuous deep, warm dark vignette ground that
persists unbroken from the hero through at least two subsequent sections — no hard
colour-field resets. Set headlines in a warm off-white (never pure white) serif at large
size; use small-caps tracked type only for nav items and section kickers; set all other
copy in a plain grotesque. Open on a two-line serif headline with a small discover-arrow
link. Follow with a plain three-up grid of warm interior photography, each photo kept in
its own native lighting rather than colour-graded to match. Use a large serif pull-quote
sentence directly on the vignette ground as a mid-page accent, then introduce individual
room or feature cards with a simple arrow-link affordance.

## Image recipe

Warm interior photograph of [SUBJECT] — a boutique hotel lobby, a café banquette, a
champagne service, a floral atrium — shot with warm practical or candle-like lighting,
rich ambers and browns, shallow depth of field, real texture (velvet, brass, glass) in
frame, no cool or flat daylight tones that would fight the page's warm vignette.

## Photo search

Unsplash first, Pexels second.
- "boutique hotel lobby warm lighting"
- "hotel cafe banquette evening ambiance"
- "champagne pour celebration warm light"
- "floral atrium staircase hotel interior"

## Reference lock

Primary reference/direction: Veloura — continuous chocolate-vignette boutique hotel page,
serif display over one unbroken dark ground.
Preserve (3-5 traits): one continuous, unbroken deep-brown vignette ground running across
multiple scroll sections with no hard colour resets; warm off-white (never pure white)
serif display headlines; small-caps tracked type reserved for nav and kickers only; a
plain, ungraded photo grid where each image keeps its native warm lighting; a large serif
pull-quote sentence used as a mid-page atmospheric accent.
Borrow only (1-2): the discover-arrow link beneath the hero headline; the small dot-
bracketed section kicker style (`· BOUTIQUE HOTEL ·`).
Role rules: the ground colour never resets to white or a contrasting hue within the
primary scroll journey; display serif never drops to pure white; small-caps type never
carries a full sentence, only labels.
Media strategy: photo:unsplash — warm, practically-lit boutique hotel interior
photography, each image ungraded and kept in its native warm tone; never cool or flat
daylight interiors.
Reject: hard white or contrasting section breaks; pure-white display type against the
dark ground; heavy colour-grading applied uniformly across the photo grid; template-
marketplace UI chrome left in the design.
Token commitments: bg-vignette `#2B0800` (radial, darkest at edges), ink-warm `#EFE4E0`,
tint `#BFA9A0`, warm-mid `#7D6457`, warm-deep `#563629`; display `Ltremark` / `Funnel
Display` for headlines, body/UI `Funnel Sans`; small-caps tracking reserved for nav and
kickers only.
