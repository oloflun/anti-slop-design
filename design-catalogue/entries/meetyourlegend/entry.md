---
title: "Meet Your Legend - creative mentorship"
url: https://meetyourlegend.com/
source_url: https://meetyourlegend.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: mentorship-orange-duotone
dna: "Creative-industry mentorship x orange duotone portraits and stacking service cards"
register: other
grammar: chaptered editorial
lane: "A mentorship platform: 'Animation 2D & 3D' loader on orange, 'Meet your legend' with orange duotone portraits of mentors, a category marquee, statements with portraits floating around ('Guided by creative experts', 'Empower by their experience'), stacking service cards on cream and orange glow, and 'Get in touch'."
mode: persuade
traits: ["orange duotone portraits", "category marquee", "portraits floating around statements", "stacking cream service cards", "orange glow on black", "wide extended display"]
palette: ["#140000", "#BB7F3A", "#825736", "#46271C", "#ECE7CD", "#D5A053"]
type: ["DrukWide", "IBMPlexSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Duotone mentor portraits floating around each claim keep the people at the centre of the pitch.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Float duotone portraits around each statement

## What to leave

- Cookie panel over frames

## Signature move

Orange duotone mentor portraits around 'Meet your legend'.

## Motion

Intro: orange with a bar loader (~1.5 s). Wheel (Lenis): portraits drift; the marquee runs; statements centre while portraits slide in from edges; service cards stack; the glow pulses.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); smoothed scroll (median 143 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a mentorship platform: 'Animation 2D & 3D' loader on orange, 'Meet your legend' with orange duotone portraits of mentors, a category marquee, statements with portraits floating around ('Guided by creative experts', 'Empower by their experience'), stacking service cards on cream and orange glow, and 'Get in touch'. Type: DrukWide, IBMPlexSans.
Ground and ink from the measured palette (#140000, #BB7F3A, #825736). Motion carries the page through
orange duotone mentor portraits around 'Meet your legend'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — duotone portraits, film stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: duotone portraits, film stills

## Reference lock

Primary reference/direction: Meet Your Legend - creative mentorship — A mentorship platform: 'Animation 2D & 3D' loader on orange, 'Meet your legend' with orange duotone portraits of mentors, a category marquee, statements with portraits floating around ('Guided by creative experts', 'Empower by their experience'), stacking service cards on cream and orange glow, and 'Get in touch'.
Preserve (3-5 traits): orange duotone portraits; category marquee; portraits floating around statements; stacking cream service cards; orange glow on black.
Borrow only (1-2): Float duotone portraits around each statement
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: duotone portraits, film stills
Reject: Cookie panel over frames
Token commitments: palette #140000, #BB7F3A, #825736, #46271C, #ECE7CD, #D5A053; type DrukWide, IBMPlexSans; engine GSAP + Lenis linked (never vendored).
