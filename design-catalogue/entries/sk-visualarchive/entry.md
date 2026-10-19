---
title: "SK Visual Archive"
url: https://sk-visualarchive.vercel.app/
source_url: https://sk-visualarchive.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: index-card-archive
dna: "Japanese poster archive x file-folder UI"
register: editorial print
grammar: gallery/catalog
lane: "A charcoal archive of personal poster designs laid out as index cards on a crosshair grid, with '( INDEX )' brackets, then a theme switcher built as tabbed file folders with APPLY buttons."
mode: read
traits: ["crosshair grid with corner marks", "index-card entries with tiny metadata", "bracket title '( INDEX )'", "tabbed file-folder theme switcher", "Inter + JetBrains Mono", "poster thumbnails as the only colour"]
palette: ["#282828", "#555853", "#FAFAFA", "#97AAA1"]
type: ["Inter", "JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The archive treats its own UI as print ephemera: index cards, bracketed headings, file folders with tabs. The posters are the only colour on a charcoal grid, so each card reads like a specimen pinned to a board.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Kaisei Sadatoki).

## What to borrow (principle)

- Present a collection as index cards with metadata on a measured grid
- Turn a settings feature (themes) into a physical metaphor: tabbed folders with an APPLY stamp
- Brackets as a typographic frame that can open and close empty

## What to leave

- Heavy smoothing (~210 px glide)
- Very small metadata

## Signature move

A theme switcher built as tabbed file folders with an APPLY button on each.

## Motion

Intro: brackets '( )' open and 'INDEX' types in (~1.5 s). Scroll (Lenis, ~210 px glide): index cards drift up at slightly different rates; the bracket pair reappears empty between sections; the theme copy fades per line from grey; folders stack and each tab raises in turn; profile card expands from a small white rectangle to a full panel.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; smoothed scroll (median 206 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a charcoal archive of personal poster designs laid out as index cards on a crosshair grid, with '( INDEX )' brackets, then a theme switcher built as tabbed file folders with APPLY buttons. Type: Inter, JetBrains Mono.
Ground and ink from the measured palette (#282828, #555853, #FAFAFA). Motion carries the page through
a theme switcher built as tabbed file folders with an APPLY button on each. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat poster scans, bold type posters, Japanese typography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat poster scans, bold type posters, Japanese typography

## Reference lock

Primary reference/direction: SK Visual Archive — A charcoal archive of personal poster designs laid out as index cards on a crosshair grid, with '( INDEX )' brackets, then a theme switcher built as tabbed file folders with APPLY buttons.
Preserve (3-5 traits): crosshair grid with corner marks; index-card entries with tiny metadata; bracket title '( INDEX )'; tabbed file-folder theme switcher; Inter + JetBrains Mono.
Borrow only (1-2): Present a collection as index cards with metadata on a measured grid; Turn a settings feature (themes) into a physical metaphor: tabbed folders with an APPLY stamp
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat poster scans, bold type posters, Japanese typography
Reject: Heavy smoothing (~210 px glide); Very small metadata
Token commitments: palette #282828, #555853, #FAFAFA, #97AAA1; type Inter, JetBrains Mono; engine GSAP + Lenis linked (never vendored).
