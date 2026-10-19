---
title: "Signals Group - Future of Kidney Health"
url: http://signalsfs.com/
source_url: http://signalsfs.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: pixel-block-health-media
dna: "Kidney-health media group x coloured pixel blocks and fluid art"
register: modern clean
grammar: chaptered editorial
lane: "A health media and community group: a counter on pale blue, a split hero with 'Global ecosystem' and a teal block holding a green fluid-art video that grows to fill the screen, wide uppercase 'Your source for data driven insights shaping the future of kidney care', article cards in teal, black and pink, a gradient 'Community' band, a founder bio, a blue 'Share your vision' block made of pixel steps and a 'Kidneyverse' logo surrounded by floating coloured squares."
mode: read
traits: ["coloured pixel blocks as transitions", "green fluid-art video", "wide geometric uppercase", "teal, pink, yellow and blue blocks", "gradient community band", "glitch logo animation"]
palette: ["#F2F2F2", "#010107", "#05333A", "#0B775E", "#30AF89", "#F8F262"]
type: ["DM Sans", "gothic"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Turning a sober medical subject into a colourful media brand works because the pixel blocks are a consistent material: every section enters as stepped coloured blocks.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stepped coloured blocks as the one transition material
- A small video block that grows to fill the hero

## What to leave

- Tiny article text
- Founder section looks generic

## Signature move

Coloured pixel blocks stepping in around wide uppercase statements.

## Motion

Intro: pale blue with a counter from 00 (~2 s), then the split hero. Wheel (Lenis ~110 px glide, 1 pin): the fluid video block grows to full screen; the statement fills grey to black; cards rise in colour blocks; the gradient band sweeps; 'Share your vision' builds from blue stepped blocks; squares float around the Kidneyverse logo as it glitches.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; WebGL canvas x1 (three.js); 2 video; split text; smoothed scroll (median 108 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a health media and community group: a counter on pale blue, a split hero with 'Global ecosystem' and a teal block holding a green fluid-art video that grows to fill the screen, wide uppercase 'Your source for data driven insights shaping the future of kidney care', article cards in teal, black and pink, a gradient 'Community' band, a founder bio, a blue 'Share your vision' block made of pixel steps and a 'Kidneyverse' logo surrounded by floating coloured squares. Type: DM Sans, gothic.
Ground and ink from the measured palette (#F2F2F2, #010107, #05333A). Motion carries the page through
coloured pixel blocks stepping in around wide uppercase statements. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fluid art video, abstract black and white photography, portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fluid art video, abstract black and white photography, portraits

## Reference lock

Primary reference/direction: Signals Group - Future of Kidney Health — A health media and community group: a counter on pale blue, a split hero with 'Global ecosystem' and a teal block holding a green fluid-art video that grows to fill the screen, wide uppercase 'Your source for data driven insights shaping the future of kidney care', article cards in teal, black and pink, a gradient 'Community' band, a founder bio, a blue 'Share your vision' block made of pixel steps and a 'Kidneyverse' logo surrounded by floating coloured squares.
Preserve (3-5 traits): coloured pixel blocks as transitions; green fluid-art video; wide geometric uppercase; teal, pink, yellow and blue blocks; gradient community band.
Borrow only (1-2): Stepped coloured blocks as the one transition material; A small video block that grows to fill the hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fluid art video, abstract black and white photography, portraits
Reject: Tiny article text; Founder section looks generic
Token commitments: palette #F2F2F2, #010107, #05333A, #0B775E, #30AF89, #F8F262; type DM Sans, gothic; engine GSAP + Lenis linked (never vendored).
