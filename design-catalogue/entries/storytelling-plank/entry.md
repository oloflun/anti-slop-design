---
title: "Digital Storytelling - Plank"
url: https://storytelling.plank.co/
source_url: https://storytelling.plank.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: blob-eye-storytelling-agency
dna: "Web studio x a green blob that becomes an eye, a heart and flowers"
register: illustrated dark
grammar: chaptered editorial
lane: "A storytelling studio page on dark green: a sage blob behind 'Digital Storytelling' with sketchy icons, the blob shrinks into an eye that opens, a statement with an inline eye icon, a flower and a heart blob, 'Storytelling projects we're proud of' on coral, and project cards stacking in pastel colours (From Vimy to Juno, Annual Impact Report, Ethical Web Collective, Year in Review, 25th Anniversary)."
mode: persuade
traits: ["morphing blob", "blob becoming an eye", "inline icons in a statement", "coral heading band", "stacking pastel project cards", "serif headlines"]
palette: ["#1E453A", "#657D73", "#E0DFBF", "#9BACA6", "#5983B1"]
type: ["Gascogne", "Untitled Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One blob shape morphs through every section (eye, heart, flower), so the page practises the storytelling it sells.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Morph one shape into the icon of each section
- Inline icons inside a statement

## What to leave

- Cards repeat the same layout

## Signature move

A sage blob shrinking into an eye that opens.

## Motion

Intro: dark green with a blob (~1 s), title with scribbled underline. Wheel (Lenis ~110 px glide, 3 pins): the blob shrinks to a circle, an iris appears and the eye blinks; the statement fills; the heart grows from the bottom; the coral band rises; heading words slide in from both sides; project cards stack.

Measured (`motion/probe.json`): GSAP 3.11.4; 11 ScrollTriggers; 3 pinned sections; Lenis; split text; smoothed scroll (median 168 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a storytelling studio page on dark green: a sage blob behind 'Digital Storytelling' with sketchy icons, the blob shrinks into an eye that opens, a statement with an inline eye icon, a flower and a heart blob, 'Storytelling projects we're proud of' on coral, and project cards stacking in pastel colours (From Vimy to Juno, Annual Impact Report, Ethical Web Collective, Year in Review, 25th Anniversary). Type: Gascogne, Untitled Sans.
Ground and ink from the measured palette (#1E453A, #657D73, #E0DFBF). Motion carries the page through
a sage blob shrinking into an eye that opens. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustration, project mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustration, project mockups

## Reference lock

Primary reference/direction: Digital Storytelling - Plank — A storytelling studio page on dark green: a sage blob behind 'Digital Storytelling' with sketchy icons, the blob shrinks into an eye that opens, a statement with an inline eye icon, a flower and a heart blob, 'Storytelling projects we're proud of' on coral, and project cards stacking in pastel colours (From Vimy to Juno, Annual Impact Report, Ethical Web Collective, Year in Review, 25th Anniversary).
Preserve (3-5 traits): morphing blob; blob becoming an eye; inline icons in a statement; coral heading band; stacking pastel project cards.
Borrow only (1-2): Morph one shape into the icon of each section; Inline icons inside a statement
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustration, project mockups
Reject: Cards repeat the same layout
Token commitments: palette #1E453A, #657D73, #E0DFBF, #9BACA6, #5983B1; type Gascogne, Untitled Sans; engine GSAP + Lenis linked (never vendored).
