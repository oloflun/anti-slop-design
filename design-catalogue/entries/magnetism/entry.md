---
title: "Magnetism"
url: https://magnetism.fr
source_url: https://magnetism.fr
captured: 2026-09-04
origin: refero
extract: ok
category: portfolio
category2: editorial
family: linen-gallery-wordmark
dna: "Wordmark-as-architecture x full-bleed luxury campaign photography"
register: editorial print
grammar: gallery/catalog
lane: "A 140px whisper-weight wordmark stretches edge-to-edge over a bone-white canvas threaded with faint field-line graphics, then the page drops into a strict 2-column grid of full-bleed, unframed campaign photographs labelled only by a hairline and a tracked-out caption row"
mode: portfolio
traits: ["140px weight-300 edge-to-edge wordmark", "99% achromatic, colour only in photography", "0px radius on every surface", "bullet-separated nav, no dividers", "0.10-0.22em tracking on all labels", "repeating M watermark on left margin"]
palette: ["#e5e7eb", "#222222", "#343434", "#aaaaaa", "#cccccc", "#dbdbdb"]
type: ["TT Hoves Pro Trial", "NeueMontreal"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Magnetism.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. The system is 99% achromatic by explicit design contract: bone white
canvas, graphite ink, three grays for hairlines and de-emphasis — nothing else.
Because the UI itself carries zero colour, the full-bleed campaign photography
(vivid ocean blue, pastel skincare, amber spirits, high-contrast black-and-white)
reads as the only chromatic event on the page, which is exactly the "page is a
wall, photograph is the art" relationship the source states outright.

Type does something unusual: a single typeface runs both extremes of the scale at
once, with no intermediate steps — a 140px weight-300 wordmark stretched edge to
edge as the page's entire header, and 8-10px micro-labels at up to 0.22em
tracking as the entire functional vocabulary. Wide, positive letter-spacing is
treated as "a structural material, not a finishing touch" — it is precisely what
keeps 8px text legible and intentional rather than merely tiny.

Geometry stays at 0px radius everywhere and elevation is banned outright; the only
depth cues are whitespace and 1px hairlines in two closely related grays. That
flatness is what allows the repeating "M" watermark and the faint concentric
field-line graphics to read as ambient texture rather than clutter — they sit at
the same visual weight as the rest of the chrome, never competing with the
photography above them.

## What to borrow (principle)

- **Run one typeface at two extreme, non-adjacent sizes.** A whisper-weight
  140px wordmark and 8-10px tracked-out labels, with nothing between, makes the
  single typeface do the entire identity job.
- **Let tracking carry legibility at small sizes.** Wide positive letter-spacing
  (0.22em) on micro-labels is what makes 8-10px text read as deliberate rather
  than cramped.
- **Separate nav items with a typographic character, not a UI element.** Middle-
  dot bullets instead of borders or backgrounds keep the whole nav pure
  typography.
- **Never overlay text on photography.** Keeping captions in a dedicated row
  below each image, never on top of it, preserves the "photograph as
  untouched art object" contract.
- **Give the brand mark a quiet, repeating presence instead of a fixed logo
  placement.** A faint watermark character on the margin can carry identity
  continuously without ever demanding attention.

## What to leave

- Zero-radius, zero-shadow, zero-accent-colour is an extremely narrow palette to
  extend into functional UI (forms, states, errors) — the system explicitly has
  no answer for anything beyond editorial display.
- A 140px wordmark stretched edge-to-edge assumes a short brand name; a longer
  name would either break the "stretch to full width" effect or force a much
  smaller size that undercuts the device entirely.
- The captioned-photography-only imagery mode depends on a genuinely large,
  high-quality campaign photo library; a thinner asset base would make the
  2-column grid feel sparse rather than curated.

## Signature move

The 140px edge-to-edge wordmark as the entire page header: no logo mark, no
tagline, no lockup — the brand name itself, set at whisper weight and stretched
to the full viewport width, functions as both identity and architecture.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Five easing families are in play across four durations (200/300/500/800ms):
plain `ease` and `linear` for simple state changes, a slow-starting ease-in
(`cubic-bezier(0.55, 0.055, 0.675, 0.19)`) and a fast-settling ease-out
(`cubic-bezier(0.19, 1, 0.22, 1)`, 17 uses — the most-used curve) for entrances,
plus a standard `cubic-bezier(0.4, 0, 0.2, 1)`. Notably, `clip-path` itself is
animated at 0.8s (ease-in-out) and 0.4s (the slow-start ease-in curve) — a
wipe/reveal effect rather than a simple fade, most plausibly how each full-bleed
campaign image or video enters the grid as it scrolls into view. (observed in
capture) the live capture (a project page, not the homepage) shows full-bleed
video/motion content used as campaign imagery itself — sailing footage in
motion — confirming that "photography" in this system extends to autoplaying
video within the same unframed, full-bleed treatment as still images.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | `ease` / `linear` |
| md | 300ms | `linear` |
| lg | 500ms | `cubic-bezier(0.19, 1, 0.22, 1)` |
| xl (clip-path wipe) | 800ms | `ease-in-out` |

## Brief

Build a luxury creative-agency portfolio homepage. Canvas is bone white `#e5e7eb`
throughout, ink is graphite `#222222` — no chromatic UI colour anywhere, ever.
Open with the agency wordmark set edge-to-edge at ~140px, TT Hoves Pro Trial
weight 300, no tracking, with a small "TM" superscript. Beneath it, a narrow
description column at 10-11px with 0.10-0.22em tracking. A bullet-separated nav
(• WORKS • ABOUT • BOUTIQUE •) floats below at 12-14px weight 400. Render a large
faint "M" watermark vertically centred on the left margin, and thin concentric
field-line graphics as ambient texture behind the header. Below the fold, lay out
full-bleed campaign photography edge-to-edge with 0px radius and 0px padding — a
single hero banner followed by a strict 2-column grid, each image followed by a
label row (client name right-aligned, "CAMPAIGN" left-aligned) at 8-10px with
0.22em tracking, separated from the image by a 1px hairline. No shadows, no
overlay text on photography, no border-radius anywhere. Section gaps run
64-80px.

## Image recipe

Full-bleed luxury campaign photograph of [SUBJECT] — high-production editorial or
product photography (watches, spirits, fashion, lifestyle), vivid and fully
saturated regardless of subject (ocean blue, pastel skincare tone, warm amber, or
high-contrast black-and-white), shot at magazine-cover quality, no crop
constraint or aspect-ratio limit, no vignette, no colour grading applied on top —
the photography's native palette is the only colour on the page.

## Photo search

Unsplash first, Pexels second.
- "luxury product editorial photography vivid colour"
- "sailing yacht ocean blue high contrast"
- "watch product photography macro"
- "fashion editorial studio portrait vivid"

## Reference lock

Primary reference/direction: Magnetism — wordmark-as-architecture agency
portfolio, 99% achromatic UI, colour arriving only through campaign photography.
Preserve (3-5 traits): bone white `#e5e7eb` canvas with graphite `#222222` ink, no
chromatic UI colour anywhere; single typeface run at two extreme sizes (140px
wordmark, 8-10px labels) with nothing intermediate; 0px radius and zero shadow on
every surface; bullet-separated nav with no borders or backgrounds; captions
always in a dedicated row below imagery, never overlaid.
Borrow only (1-2): the repeating "M" watermark on the left margin; the faint
concentric field-line decorative graphic.
Role rules: no accent hue is ever introduced, including for interaction states —
use the existing gray scale only; text never overlays a photograph; the wordmark
never renders above weight 300 or in a condensed/extended cut.
Media strategy: photo:unsplash — full-bleed, high-production campaign
photography and video in their native saturated colour; no illustration, no
icons, no abstract graphics.
Reject: any chromatic UI element (button fill, link colour, badge); border-radius
on images or cards; box-shadow of any kind; text overlaid directly on
photography; nav dividers other than the bullet character.
Token commitments: bg `#e5e7eb`, ink `#222222`, nav-ink `#343434`, muted `#aaaaaa`,
hairline `#cccccc`, decorative-stroke `#dbdbdb`; wordmark 140px weight
300/leading 1.0; body 14-16px/leading 1.5/1.4-1.6px tracking; micro-label 8-10px/
0.22em tracking; radius 0px universal; section gap 64px.
