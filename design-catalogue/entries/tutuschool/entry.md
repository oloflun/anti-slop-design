---
title: "Tutu School - Ballet Classes for Kids"
url: http://tutuschool.com/
source_url: http://tutuschool.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "playful"
family: pastel-storybook-kids-school
dna: "Children's ballet school x pastel pink storybook with stacked offer cards"
register: warm photographic
grammar: chaptered editorial
lane: "A kids' ballet franchise: a rounded pink hero with 'Discover the magic', a 'Storybook adventures in ballet' block with photos floating around it, a pinned 'What we offer' where cards (classes, camps, birthday parties, bravo bash) replace each other, and a rounded video panel 'Every child deserves to dance'."
mode: persuade
traits: ["pastel pink and lilac", "swash italic serif words", "photos floating around a text block", "pinned card swap for offers", "rounded panels", "sparkle icons"]
palette: ["#F4E9F4", "#D6939B", "#AE676E", "#D1C1C6"]
type: ["archermedium", "archermedium_italic", "australis_pro_swashitalic", "soin_sans_promedium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The pinned card swap lets parents read one offer at a time, and the floating photos make the storybook idea literal without illustrations.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: DASH Creative Strategy).

## What to borrow (principle)

- Pin the section and swap one offer card at a time
- Float photos around a centred text block

## What to leave

- Low contrast pink-on-pink text
- Generic hero

## Signature move

Offer cards swapping in place under 'What we offer' on a lilac ground.

## Motion

Intro: the pink hero with a slow zoom; cookie banner declined. Wheel (native, 1 pin): photos drift in around the storybook block; 'What we offer' pins while each card fades and rises in place of the last; the video panel expands into view.

Measured (`motion/probe.json`): GSAP 3.12.5; 8 ScrollTriggers; 1 pinned sections; split text; entry gate: Deny. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a kids' ballet franchise: a rounded pink hero with 'Discover the magic', a 'Storybook adventures in ballet' block with photos floating around it, a pinned 'What we offer' where cards (classes, camps, birthday parties, bravo bash) replace each other, and a rounded video panel 'Every child deserves to dance'. Type: archermedium, archermedium_italic, australis_pro_swashitalic, soin_sans_promedium.
Ground and ink from the measured palette (#F4E9F4, #D6939B, #AE676E). Motion carries the page through
offer cards swapping in place under 'What we offer' on a lilac ground. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — children's dance photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: children's dance photography

## Reference lock

Primary reference/direction: Tutu School - Ballet Classes for Kids — A kids' ballet franchise: a rounded pink hero with 'Discover the magic', a 'Storybook adventures in ballet' block with photos floating around it, a pinned 'What we offer' where cards (classes, camps, birthday parties, bravo bash) replace each other, and a rounded video panel 'Every child deserves to dance'.
Preserve (3-5 traits): pastel pink and lilac; swash italic serif words; photos floating around a text block; pinned card swap for offers; rounded panels.
Borrow only (1-2): Pin the section and swap one offer card at a time; Float photos around a centred text block
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: children's dance photography
Reject: Low contrast pink-on-pink text; Generic hero
Token commitments: palette #F4E9F4, #D6939B, #AE676E, #D1C1C6; type archermedium, archermedium_italic, australis_pro_swashitalic, soin_sans_promedium; engine GSAP + Lenis linked (never vendored).
