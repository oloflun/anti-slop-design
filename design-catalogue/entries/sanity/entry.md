---
title: "Sanity.io"
url: https://www.sanity.io
source_url: https://www.sanity.io
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: editorial
family: geological-onyx-editorial
dna: "Geological dark-hero photography x numbered Swiss-editorial section rhythm"
register: cinematic dark
grammar: chaptered editorial
lane: "A full-bleed dark hero of geological texture carries a compressed, tightly-tracked headline and one orange pill CTA, then the page drops to white numbered sections (01-05) where real product screenshots stand in for marketing illustration"
mode: persuade
traits: ["one orange CTA, never decorative", "pill radius on every interactive control, 3px on inputs/images", "112px display at -4.48px tracking", "onyx not pure black, five-step dark surface stack", "numbered mono section labels (01-05)", "real product UI as marketing hero"]
palette: ["#ff4100", "#0b0b0b", "#ffffff", "#797979", "#0052ef", "#353535"]
type: ["Waldenburg", "IBM Plex Mono"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Sanity.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Ember orange `#ff4100` is treated as a single-use signal: it appears
on the logo dot and the one primary CTA per view, and the Do's list states the
rule explicitly — "never two orange CTAs competing for attention." Everything
else, including secondary buttons, stays achromatic; if a second accent is ever
needed, the source specifies Signal Blue at "20% of the visual weight of
orange," which is itself a rare, precisely rationed exception rather than a
free second colour.

Waldenburg runs the entire type system at weight 425 — "a true book weight
between 400 and 500" the source calls distinctive — with letter-spacing that
compresses hard at display scale (-4.48px at 112px) while staying loose to
normal below 16px. That precise compression curve, plus five custom stylistic
alternates baked into the typeface itself, is what gives 112px headlines their
"compressed, architectural" character rather than reading as merely large.

The system's most distinctive structural choice is treating its own product as
marketing content: Studio screenshots, code editors and content forms appear
at full scale in the marketing surface, "realistic, not stylized." Paired with
Swiss-editorial numbered sections (01-05 in IBM Plex Mono) and a five-step dark
surface stack (onyx → graphite → charcoal) that replaces shadow entirely,
Sanity reads as a product demonstrating its own credibility rather than
illustrating a promise.

## What to borrow (principle)

- **Ration a bright accent to exactly one instance per view.** Stating "never
  two competing CTAs" as a hard rule keeps a loud colour legible as signal, not
  decoration.
- **Give a workhorse typeface a true in-between weight.** A custom 425 weight
  (between regular and medium) can add warmth to body text without needing a
  separate typeface for that register.
- **Compress tracking sharply at display, relax it at body.** A precise curve
  from -4.48px at 112px down to normal at 16px keeps every size in its own
  correct register.
- **Show the actual product as marketing proof.** Real, unstyled screenshots of
  the working product carry more credibility than illustrated mockups —
  "the product IS the marketing visual."
- **Replace shadow with a graduated dark-surface stack.** Onyx → graphite →
  charcoal, each a lighter step of the same near-black hue, creates
  architectural depth without a single drop shadow.

## What to leave

- Confining orange to exactly one CTA per screen is a strict rule that content
  and growth teams will be tempted to break for secondary conversion goals —
  it requires active editorial discipline to hold at scale.
- A 112px display headline with a distinctive custom typeface (five stylistic
  alternates) is a high production bar; a generic substitute grotesque will
  lose the compressed architectural character the source calls the brand's
  defining trait.
- Showing real, unstyled product UI as the hero visual only works when the
  product itself is genuinely presentable — a rougher or inconsistent UI would
  undermine rather than reinforce the marketing message.

## Signature move

The numbered editorial section: a left column stack of IBM Plex Mono numerals
(01-05) with uppercase tracked labels, paired with a right column of headline
plus body plus real product screenshot — treating feature sections as
numbered magazine chapters rather than a generic feature grid.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked —
correcting the earlier "no duration or easing documented" read: a standard
`cubic-bezier(0.4, 0, 0.2, 1)` curve dominates (97 uses) across five duration
steps from 100ms to 1s, with smaller `linear` and `ease` sets alongside it.
Three keyframes are confirmed firing: `homepage-customers-countdown` (a scale
transform) most likely animates a customer/usage stat counting or scaling into
place; `marquee-scroll` (a slide transform) drives a horizontal customer-logo
marquee; `delay-overflow` (an overflow-property keyframe) is a scroll-lock
utility, likely behind a modal or dropdown rather than brand storytelling. The
counter and marquee both fit the "product demonstrating its own credibility"
theme directly — customer proof that counts and scrolls, not just states.
(observed in capture) the live capture shows a static hero on load with a
dismissible top announcement bar and a full-bleed video/photographic
background (foliage in motion against the dark hero) rather than a static
image — the "atmospheric organic photography" the source describes is video,
not a still.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| sm | 200ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| md | 300ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| lg | 500ms | `cubic-bezier(0.4, 0, 0.2, 1)` |
| xl | 1s | `linear` (marquee) |
| homepage-customers-countdown | scale transform | stat counter |
| marquee-scroll | slide transform | logo marquee |

## Brief

Build a developer-platform marketing homepage. Open full-bleed dark
(`#0b0b0b`, not pure black) with atmospheric organic or geological photography/
video, a left-anchored white headline at 72-112px in a custom grotesque with
tight negative tracking (-2.52px to -4.48px), one ember-orange `#ff4100` pill
CTA paired with a ghost pill secondary action — never two orange buttons on
one screen. Drop to a white canvas for editorial sections at max-width 1280px,
using a 2-column asymmetric grid: numbered IBM Plex Mono labels (01-05) in the
left column, headline plus body plus real product screenshot in the right.
Show actual product UI — code editors, content forms — realistically, not as
stylised illustration. Make every interactive control (buttons, nav, tags) a
full pill radius; cap inputs and images at 3px, cards at 12px. Reserve Signal
Blue `#0052ef` for links and focus rings only, at a fraction of orange's visual
weight. No box-shadow anywhere — depth comes from a five-step surface stack
(white → onyx → graphite → charcoal). Keep 96px section gaps on white, tighter
48px on dark.

## Image recipe

Atmospheric geological or organic photograph of [SUBJECT] — agate cross-
sections, mineral textures, or macro organic detail in warm earth tones, shot
with dramatic directional light against near-black shadow, full-bleed with no
crop constraint, photorealistic and unstylised — paired where relevant with a
genuine, unstyled screenshot of the product's own interface as equally valid
hero content.

## Photo search

Unsplash first, Pexels second.
- "agate geode cross section macro texture"
- "mineral rock texture warm light"
- "organic macro texture dark background"
- "geological formation close up dramatic light"

## Reference lock

Primary reference/direction: Sanity.io — geological dark-hero developer
platform, real product UI as marketing hero, numbered editorial sections.
Preserve (3-5 traits): onyx `#0b0b0b` (never pure black) for dark surfaces,
white for light sections; ember orange `#ff4100` confined to exactly one CTA
per view, never decorative or duplicated; Waldenburg at weight 425 with
tracking compressing from normal at 16px to -4.48px at 112px; real, unstyled
product screenshots used as marketing hero content; five-step dark surface
stack replacing all shadow.
Borrow only (1-2): the numbered (01-05) IBM Plex Mono section-label pattern;
the logo-dot-as-accent device (orange dot, monochrome wordmark).
Role rules: orange never sets body text or appears twice on one screen;
syntax-highlight colours (magenta, lime, electric blue) stay confined to
code/editor contexts only; headlines never centre-align.
Media strategy: photo:unsplash for atmospheric geological/organic textures;
supplement with genuine product-UI screenshots, never stylised mockups.
Reject: a second saturated CTA colour; drop shadows on any card; centred
display headlines; decorative gradients; illustrated (non-real) product
mockups.
Token commitments: bg `#ffffff`, dark `#0b0b0b`, elevated-1 `#212121`,
elevated-2 `#353535`, accent `#ff4100`, link `#0052ef`, muted `#797979`;
display Waldenburg 425 at 72-112px/leading 1.0-1.05/-2.52 to -4.48px tracking;
body 18-20px/leading 1.5; radius 99999px interactive, 3px inputs/images, 12px
cards; page max-width 1280px, section gap 96px (white) / 48px (dark).
