---
title: "dope.security"
url: https://dope.security
source_url: https://dope.security
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: editorial
family: midnight-boarding-pass
dna: "Twilight sky photography x a translucent boarding-pass card, violet rationed like runway lighting"
register: cinematic dark
grammar: split stage
lane: "A near-black canvas carries a single dramatic dusk-sky photograph as the hero, with a frosted glass boarding-pass card floating on the right and 74px letterspaced mono stamps signposting every section below — the one violet accent appearing only once or twice per page"
mode: persuade
traits: ["signal violet rationed to 1-2 uses per page, never a border", "GrandSlang italic reserved for 2-3 largest moments only", "74px mono stamp headings, 0.2em tracking", "shadowless, hairline strokes at low opacity only", "two button radii only: 8px controls, 1584px pills", "coordinate-stamp footer signature"]
palette: ["#090909", "#f7f9fa", "#af50ff", "#828384", "#423738", "#e1bdff"]
type: ["Whyte Inktrap", "Whyte Inktrap Mono", "GrandSlang"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/dope.security.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the
live capture. Signal violet `#af50ff` is rationed with a stated frequency —
"one feature card glow, one filled action, and one accent stroke per page" —
and the Do's list frames it explicitly as "signal lighting, not decoration."
Everything else lives in a tight nine-step achromatic scale from
`#f7f9fa` down to `#090909`, so the single violet reads as genuinely rare
against a page that is otherwise a near-black void.

Three typefaces hold three non-overlapping jobs with hard rules against
mixing them: Whyte Inktrap (a geometric sans with distinctive inktrap
corners) carries nearly everything; Whyte Inktrap Mono, at a constant 0.2em
tracking, exists only to stamp 74px uppercase section headings that read as
boarding-pass signage; GrandSlang, an italic display serif, is reserved for
"the two or three largest display moments" and is explicitly forbidden below
32px. The source states plainly that GrandSlang and the mono stamp voice must
never share a line — each face stays in its own register.

The system trusts line weight over depth for every separation need: cards
default to 19.2px radius with zero internal padding fill, borders sit at
0.5-1px and low opacity, and the only documented shadow is a near-invisible
1px hairline on the nav. Two button radii — 8px for controls, 1584px for
pill CTAs — are the system's entire rounding vocabulary, and the page closes
on a signature "coordinate stamp" footer that writes a live GPS location as
if signing a postcard, reinforcing the travel-editorial conceit the whole
system runs on.

## What to borrow (principle)

- **State an accent's frequency as a number, not a feeling.** "One glow, one
  fill, one stroke per page" is auditable in a way "use sparingly" is not.
- **Assign three typefaces three genuinely exclusive jobs.** A workhorse
  sans, a mechanical mono for section stamps, and an italic serif for only
  the largest 2-3 moments — with an explicit rule against ever mixing the
  mono and the serif on one line — keeps a three-font system legible.
- **Cap shadow to a single 1px hairline, everywhere else use line weight.**
  Trusting borders at low opacity instead of blur is what keeps a dark,
  atmospheric hero from turning heavy or app-like below the fold.
- **Reserve two button radii for two distinct roles.** 8px for compact
  controls, a full pill for primary CTAs — no radius in between — keeps
  every interactive element legible by shape alone.
- **Give the page a signature closing gesture.** A live-coordinate footer
  that "signs" the page like a postcard turns a generic footer into a brand
  device.

## What to leave

- Rationing violet to 1-2 uses per page is a strict discipline that will be
  tempting to break for secondary conversion goals (a second "featured"
  badge, an extra highlighted row) — it requires active editorial review to
  hold.
- GrandSlang's ban below 32px means any smaller editorial moment (a
  pull-quote, an inline emphasis) has no serif option available and must
  fall back to the sans or mono voice instead.
- A single dramatic hero photograph with almost no imagery afterward (the
  source notes imagery drops to "less than 15% of the page" after the hero)
  depends on that one image being genuinely striking — a weaker photograph
  would leave the rest of the page visually thin.

## Signature move

The coordinate-stamp footer: a live-updating GPS coordinate paired with a
small heart icon and "Fly Direct" labeling, written as if the brand is
signing a postcard from a physical location — the closing gesture that
completes the travel/boarding-pass conceit running through the whole page.

## Motion

(from designlang extract) Feel reads as responsive, and the page is
scroll-linked — correcting the earlier "no durations captured" read. A
fast-settling ease-out family (`cubic-bezier(0.23, 1, 0.32, 1)` and
`cubic-bezier(0.165, 0.84, 0.44, 1)`, 9 uses) carries transitions across four
durations from 100ms to 600ms. One keyframe is confirmed firing: `sparkle`, a
reveal combining opacity and transform (1 use) — almost certainly the "one
feature card glow" the violet accent is rationed to, giving that single
signal-violet moment a small animated flourish rather than a static highlight.
(observed in capture) the live capture confirms the hero's atmospheric sky
photograph, translucent boarding-pass card, and streaking airplane-light
motif are present and match the described composition; given the frosted nav
pattern, hover and scroll states beyond the sparkle most plausibly still rely
on opacity or blur intensity shifts on that same ease-out family rather than
translation, consistent with the shadowless, line-weight-driven elevation
philosophy documented throughout.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | ease-out family |
| sm | 200ms | ease-out family |
| md | 300ms | ease-out family |
| lg | 600ms | ease-out family |
| sparkle (violet glow) | reveal (opacity + transform) | 1 use |

## Brief

Build a premium, midnight-terminal security-product landing page. Canvas is
near-black `#090909`; almost-white `#f7f9fa` carries primary text and 1px
borders. Signal violet `#af50ff` is the only chromatic voice, appearing at
most once or twice per page as a feature-card glow, a single filled CTA, or
an accent stroke — never a border, never body text. Open full-bleed on a
single dramatic twilight-sky photograph with a left-column hero mixing
GrandSlang italic (146px, "Your new" / "with AI DLP") and Whyte Inktrap
(64px, the product name), plus a translucent 19.2px-radius "boarding pass"
card floating on the right with two pill CTAs. Signpost every section below
with a 74px Whyte Inktrap Mono uppercase heading at constant 0.2em tracking
— never mixed on the same line as GrandSlang. Use only two button radii: 8px
for compact bordered controls, 1584px for pill CTAs. Replace shadows with
0.5-1px low-opacity hairlines everywhere except a single 1px nav shadow.
Close on a coordinate-stamp footer with a live GPS location and a heart
icon. Keep 120px section gaps and a 1200px content max-width.

## Image recipe

Atmospheric wide-format sky photograph of [SUBJECT] — a dramatic twilight or
dusk scene with saturated purple-to-amber gradient clouds over a glowing
horizon, shot uncropped and unmasked to fill the full viewport, with a
single small streak of light (aircraft trail) crossing the frame as the
only literal subject beyond the sky itself.

## Photo search

Unsplash first, Pexels second.
- "dramatic twilight sky purple clouds horizon"
- "dusk sky gradient clouds wide format"
- "airplane light trail night sky"
- "atmospheric sunset clouds moody"

## Reference lock

Primary reference/direction: dope.security — midnight boarding-pass product
page, violet rationed as a stated 1-2-uses-per-page signal.
Preserve (3-5 traits): near-black `#090909` canvas with almost-white
`#f7f9fa` text, nine-step achromatic scale; signal violet `#af50ff` capped at
1-2 uses per page, never a border or body-text colour; three typefaces in
strictly separate roles (Whyte Inktrap workhorse, mono for 74px 0.2em-
tracked section stamps, GrandSlang italic for 2-3 largest moments only,
never below 32px); zero box-shadow beyond one 1px nav hairline; exactly two
button radii (8px controls, 1584px pills).
Borrow only (1-2): the translucent "boarding pass" hero card device; the
live-coordinate postcard-signature footer.
Role rules: GrandSlang and the mono stamp voice never share a line; violet
never becomes a border or large text colour; card padding stays at 0 —
layout, not fill, creates the boundary.
Media strategy: photo:unsplash for a single dramatic atmospheric sky hero;
everything after the hero stays iconographic/typographic — no further
photography.
Reject: a second accent colour; GrandSlang below 32px; box-shadow beyond the
one documented hairline; a button radius outside {8px, 1584px}; centred
body copy or multi-column text.
Token commitments: bg `#090909`, nav-panel `#333248b3`, wash `#423738`,
accent `#af50ff`, accent-tint `#e1bdff`, ink `#f7f9fa`, muted `#828384`;
display Whyte Inktrap 300-400 at 48-88px, GrandSlang 300-400 at 32-146px;
mono stamp 74px/0.2em tracking; radius 19.2px cards, 8px controls, 1584px
pills; page max-width 1200px, section gap 120px.
