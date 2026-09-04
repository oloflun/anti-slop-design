---
title: "Spring/Summer"
url: https://springsummer.dk/
source_url: https://springsummer.dk/
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: celadon-annual-report
dna: "Scandinavian design-annual celadon paper x crushed 386px display type"
register: editorial print
grammar: typographic poster
lane: "A pale sage page carries a whisper-thin nav band and flush-left plum headlines crushed to near-touching leading, with a horizontal project carousel of oversized image cards scrolling off the right edge like spreads in a printed annual"
mode: portfolio
traits: ["386px display at 0.75 leading, letters nearly touch", "five-colour palette total, no accent hue", "4px radius on every rectangular element", "white overlay caption strip, not a full card", "live clock + city in nav, typeset not badged", "typographic arrows as the only scroll control"]
palette: ["#fe3939", "#ffffff", "#000000", "#dedcd3"]
type: ["Supply", "Montreal", "Grotesk"]
measured: designlang
kind: reference-style
source: anton
status: ready
refero: processed/SpringSummer.md
---

## Why it works

Palette and type are read from Refero's extracted tokens. Note: the designlang
extract, run against the current live page, measures a dramatically different
palette than the one documented below — a saturated red `#fe3939` is now the
single most-used colour on the page (1792 uses, more than white or black), and
neither plum ink `#44394c` nor the two warm-gray borders appear anywhere in the
live colour inventory. The typeface picture shifts too: "Supply" (331 elements,
used for all) is the actual dominant functional face, not documented below at
all, while Grotesk registers only 3 elements — still plausibly display-only
(a single hero headline is often just 1-3 DOM nodes) but no longer the
system's clear second voice. This reads as a full brand relaunch since
capture, not a measurement artifact; the sage/plum "annual report" reading
below describes the captured screenshot faithfully, but no longer describes
the live site. The system holds to exactly five colours — sage paper, plum ink,
white, and two warm-gray borders — with no accent hue anywhere; the source
states plainly that "color never decorates; it only separates ink from
paper." Because sage paper is the sole background and white is the only
elevated surface, depth is a single binary step, which keeps the whole page
reading as one continuous printed sheet rather than a stack of UI panels.

Grotesk, the display face, exists at one weight only and is used exclusively
at 170-386px with a crushed 0.75-0.76 line-height — tight enough that letters
"nearly touch" and the type feels "carved rather than set." Montreal, at a
single weight with slight positive tracking (0.02-0.023em), handles literally
everything else, including the 43px agency descriptor, which the source
treats as a large caption rather than a second display size — there is no
intermediate heading tier between whisper-small Montreal and monumental
Grotesk.

Interaction chrome is reduced to typography itself: carousel navigation is a
pair of plain arrow glyphs with no button container, the contact form uses an
underline-only input with no box, and even the live clock in the nav reads as
inline type rather than a widget. Combined with 4px radius as the single
allowed corner value system-wide, the page commits fully to reading as a
printed agency annual that happens to scroll rather than a software product.

## What to borrow (principle)

- **Hold a genuine five-colour ceiling with zero accent.** Declaring the exact
  colour count and enforcing "no sixth colour" prevents an accent from
  creeping in through buttons or badges over time.
- **Crush display leading until letters nearly touch.** A 0.75 line-height at
  300px+ sizes is what turns "big type" into a carved, architectural mass
  rather than merely oversized text.
- **Treat a large caption as a caption, not a second display tier.** Keeping
  the 43px agency descriptor in the body typeface (not the display face)
  avoids inventing an unnecessary in-between heading size.
- **Make scroll controls purely typographic.** Plain arrow characters with no
  button background or padding read as editorial page-turning, not app
  navigation.
- **Use underline-only inputs on the page canvas.** A form field with no box,
  just a 1px bottom border, keeps even functional UI inside the printed-page
  metaphor.

## What to leave

- Zero intermediate heading sizes between ~43px and 170px is a genuine content
  constraint — any section needing a "medium" headline has no native size to
  reach for without introducing a new scale step.
- A single elevation step (sage to white, nothing between) works for a
  portfolio with few content types; a denser product interface would need more
  surface levels than this system provides.
- The live clock and city label in the nav is a bespoke, agency-specific
  flourish; reproducing it elsewhere requires genuinely live data, not a
  decorative placeholder.

## Signature move

The typeset live-status nav element: a real-time clock ("18:35:18") paired
with a city name ("Copenhagen"), rendered as plain inline Montreal type with
no badge, icon frame, or background — presented as fact rather than as a
decorative widget.

## Motion

(from designlang extract) Feel reads as smooth, and the page is scroll-linked.
A plain `ease` curve dominates overwhelmingly (186 uses) across five duration
steps from 200ms to 1.3s, with a single fast ease-out
(`cubic-bezier(0, 0.55, 0.45, 1)`) appearing once. The one keyframe confirmed
firing, `sweep` (a slide transform, 1 use), most plausibly drives a hover-wipe
effect on a link or the carousel's arrow controls rather than a page-load
reveal. (observed in capture) the live capture confirms the horizontal project
carousel and the live clock/status indicator are present and functioning,
consistent with a genuinely real-time nav element; given the flat,
shadow-free system and the extract's own heavy reliance on plain `ease`, the
carousel most plausibly still scrolls via native horizontal drag/scroll rather
than a custom-eased animation.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | `ease` |
| md | 300ms | `ease` |
| lg | 500ms | `ease` |
| xl | 800ms | `ease` |
| xxl | 1.3s | `ease` |
| sweep | slide transform | 1 use |

## Brief

Build a Scandinavian design-agency portfolio homepage. Canvas is sage paper
`#e5ebda` — the only background colour on the page; white `#ffffff` is the
sole elevated surface, used only for project-card image fills and caption
overlays. Plum ink `#44394c` carries every piece of text, with warm-gray
borders (`#c0c3b6`, `#b0b2a9`) as hairline dividers only — no sixth colour is
ever introduced. Set the hero display in Grotesk at one weight, 170-386px,
crushed to 0.75 line-height, flush left with no background or decoration. Use
Montreal at one weight throughout for nav, body, captions and the 43px agency
descriptor, with consistent +0.02-0.023em tracking. Build a horizontal project
carousel of large image cards (480-640px wide) with a small white caption
strip inset bottom-left, navigated by two plain typographic arrow glyphs with
no button chrome. Cap every rectangular corner at 4px. Show a live clock and
city label in the nav, styled as inline type, not a widget. No drop shadows or
gradients anywhere; elevation is the single sage-to-white step only.

## Image recipe

Editorial documentary photograph of [SUBJECT] — environmental or campaign
photography from real project work, landscape-cropped, full-bleed within its
4px-radius card frame, natural or venue lighting rather than studio-lit,
presented at large scale as a standalone visual paragraph with no overlay
text beyond a small caption strip.

## Photo search

Unsplash first, Pexels second.
- "creative agency event photography documentary"
- "design studio work environmental photography"
- "brand campaign editorial photography wide"
- "creative award ceremony stage photography"

## Reference lock

Primary reference/direction: Spring/Summer — celadon-paper Scandinavian design
annual, crushed 386px display type, five-colour ceiling with no accent.
Preserve (3-5 traits): sage paper `#e5ebda` as the sole background, white as
the only elevated surface; Grotesk at one weight, 170-386px, 0.75-0.76 leading
so letters nearly touch, never used below 40px; Montreal at one weight for
everything else including the 43px descriptor; exactly five colours total,
zero accent hue; 4px radius as the single allowed corner value.
Borrow only (1-2): the live clock-plus-city status element in the nav; the
plain typographic arrow scroll controls with no button container.
Role rules: Grotesk never sets body copy or sizes under 40px; Montreal never
sets display headlines above 43px; no colour beyond the declared five is ever
introduced, including for CTAs.
Media strategy: photo:unsplash — full-bleed editorial documentary photography
of real work/events; no illustration, no icons beyond the monogram and status
dot.
Reject: a sixth colour anywhere; drop shadows or gradients; radius above 4px;
a filled/coloured CTA button; an intermediate heading size between caption and
display.
Token commitments: bg `#e5ebda`, surface `#ffffff`, ink `#44394c`, border-1
`#c0c3b6`, border-2 `#b0b2a9`; display Grotesk 400 at 170-386px/leading 0.75;
body Montreal 400 at 12-43px/leading 1.1-1.5/+0.02-0.023em tracking; radius
4px universal; page max-width 1440px, section gap 64-96px.
