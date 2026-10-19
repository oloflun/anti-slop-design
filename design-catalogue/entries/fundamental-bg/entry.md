---
title: "Fundamental Studio - Creative Digital Agency"
url: https://fundamental.bg/en
source_url: https://fundamental.bg/en
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: floating-tiles-universe-agency
dna: "Sofia digital agency x a universe of floating project tiles"
register: cinematic dark
grammar: chaptered editorial
lane: "An agency on black: a soft green blur with a checklist loader ('launching the rocket', 'googling the error'), then 'A whole new universe' surrounded by dozens of project screenshots floating in 3D space around the camera, which settles into a two-column grid of laptop mockups, a statement, services list and reviews."
mode: persuade
traits: ["humorous checklist loader", "project tiles floating in 3D space", "camera drifting through the tiles", "tiles settling into a grid", "green accent", "pill nav"]
palette: ["#000000", "#444E48"]
type: ["Acari Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Flying through a cloud of every project turns 'we have done a lot' into a felt space, and the tiles landing in a grid makes the switch from spectacle to browsing.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Float the archive in 3D around the headline, then settle it into a grid
- A loader checklist with a sense of humour

## What to leave

- Generic services and reviews
- Small grid captions

## Signature move

Dozens of project tiles floating in 3D around 'A whole new universe'.

## Motion

Intro: green blur with a checklist ticking through jokes (~3 s). Wheel (Lenis ~90 px glide, 1 pin): tiles fly towards the camera from depth and drift around the pinned headline; they slow and fall into a two-column grid; mockups slide in pairs; the statement fills; service cards highlight; reviews scroll.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; 23 video; split text; smoothed scroll (median 74 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an agency on black: a soft green blur with a checklist loader ('launching the rocket', 'googling the error'), then 'A whole new universe' surrounded by dozens of project screenshots floating in 3D space around the camera, which settles into a two-column grid of laptop mockups, a statement, services list and reviews. Type: Acari Sans.
Ground and ink from the measured palette (#000000, #444E48). Motion carries the page through
dozens of project tiles floating in 3D around 'A whole new universe'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device mockups and site screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device mockups and site screenshots

## Reference lock

Primary reference/direction: Fundamental Studio - Creative Digital Agency — An agency on black: a soft green blur with a checklist loader ('launching the rocket', 'googling the error'), then 'A whole new universe' surrounded by dozens of project screenshots floating in 3D space around the camera, which settles into a two-column grid of laptop mockups, a statement, services list and reviews.
Preserve (3-5 traits): humorous checklist loader; project tiles floating in 3D space; camera drifting through the tiles; tiles settling into a grid; green accent.
Borrow only (1-2): Float the archive in 3D around the headline, then settle it into a grid; A loader checklist with a sense of humour
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device mockups and site screenshots
Reject: Generic services and reviews; Small grid captions
Token commitments: palette #000000, #444E48; type Acari Sans; engine GSAP + Lenis linked (never vendored).
