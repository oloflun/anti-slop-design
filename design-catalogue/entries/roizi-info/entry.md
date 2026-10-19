---
title: "Roizi - Web and Digital Creative Designer"
url: http://roizi.info/
source_url: http://roizi.info/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: bilingual-shape-folio
dna: "Taipei designer x a black cog shape and bilingual intro"
register: modern clean
grammar: chaptered editorial
lane: "A designer folio: 'I'm Roizi, I focused on...' typing on black, a white page where a black cog shape wipes away to reveal a bilingual Chinese/English intro, a laptop mockup that grows to full width, and an 'Any idea? Make it interesting!' footer."
mode: read
traits: ["typed intro on black", "black cog shape as the wipe", "bilingual Chinese and English copy", "laptop mockup that grows", "small 3D figure", "quiet footer"]
palette: ["#FFFFFF", "#000000", "#2E2414", "#D7D6D4", "#535252", "#CEB789"]
type: ["台北黑體", "Urbanist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The cog shape is a simple, bold wipe that turns a short folio intro into an event.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Roizi Lu).

## What to borrow (principle)

- A large bold shape as the wipe between intro and content

## What to leave

- Short page with little work shown
- Small text

## Signature move

A black cog shape rolling away to reveal a bilingual intro.

## Motion

Intro: black, 'I'm Roizi, I focused on' types with a cycling word (~2 s). Wheel (smoothed ~100 px): the cog shape shrinks and rotates off; the intro fills in; the laptop mockup scales to full width; the footer rises.

Measured (`motion/probe.json`): GSAP 3.13.0; 21 ScrollTriggers; smoothed scroll (median 115 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a designer folio: 'I'm Roizi, I focused on...' typing on black, a white page where a black cog shape wipes away to reveal a bilingual Chinese/English intro, a laptop mockup that grows to full width, and an 'Any idea? Make it interesting!' footer. Type: 台北黑體, Urbanist.
Ground and ink from the measured palette (#FFFFFF, #000000, #2E2414). Motion carries the page through
a black cog shape rolling away to reveal a bilingual intro. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device mockups

## Reference lock

Primary reference/direction: Roizi - Web and Digital Creative Designer — A designer folio: 'I'm Roizi, I focused on...' typing on black, a white page where a black cog shape wipes away to reveal a bilingual Chinese/English intro, a laptop mockup that grows to full width, and an 'Any idea? Make it interesting!' footer.
Preserve (3-5 traits): typed intro on black; black cog shape as the wipe; bilingual Chinese and English copy; laptop mockup that grows; small 3D figure.
Borrow only (1-2): A large bold shape as the wipe between intro and content
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device mockups
Reject: Short page with little work shown; Small text
Token commitments: palette #FFFFFF, #000000, #2E2414, #D7D6D4, #535252, #CEB789; type 台北黑體, Urbanist; engine GSAP + Lenis linked (never vendored).
