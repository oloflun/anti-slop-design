---
title: "Parker - AI creative strategist for ads"
url: https://heyparker.ai/
source_url: https://heyparker.ai/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: retro-mac-cartoon-strategist
dna: "Ad strategy AI x a vintage Mac that types and a cartoon strategist in colour panels"
register: other
grammar: chaptered editorial
lane: "A product page: a beige vintage Mac whose screen types 'The way you make ads is...' then 'Meet Parker', a cartoon moustached man thinking on violet with platform icons, 'Parker tells you what ads to make', 'Let me sh_' with drawn arrows, step tabs (Research, Chat, Grow) as coloured folders, a green maze the character walks through ('Creative strategy used to be a maze'), 'What makes Parker different?' with his open head on three colour arcs, pricing, testimonials and a big red 'Parker' footer."
mode: persuade
traits: ["vintage Mac typing", "cartoon character", "colour panels per step", "drawn arrows", "maze walk", "big red script footer"]
palette: ["#FFFFFF", "#B3A789", "#4E4B66", "#DDD2AD"]
type: ["Radio Canada", "Radio Canada Big", "Source Serif Pro Regular", "Inter Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The Mac typing the first words and the character carried through every panel make a dense product story read as a comic.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Ashwin Pradeep Kumar).

## What to borrow (principle)

- Let one character carry the reader through each panel
- Type the first words on a device before the page opens

## What to leave

- Many sections

## Signature move

A cartoon strategist walking through a green maze.

## Motion

Intro: the Mac screen types (~3 s). Wheel: panels slide up in colour; the character crops in and out; folders tab across; the maze path draws; the head's arcs change colour; the red name rises.

Measured (`motion/probe.json`): Lenis; 3 video; smoothed scroll (median 146 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a product page: a beige vintage Mac whose screen types 'The way you make ads is...' then 'Meet Parker', a cartoon moustached man thinking on violet with platform icons, 'Parker tells you what ads to make', 'Let me sh_' with drawn arrows, step tabs (Research, Chat, Grow) as coloured folders, a green maze the character walks through ('Creative strategy used to be a maze'), 'What makes Parker different?' with his open head on three colour arcs, pricing, testimonials and a big red 'Parker' footer. Type: Radio Canada, Radio Canada Big, Source Serif Pro Regular, Inter Display.
Ground and ink from the measured palette (#FFFFFF, #B3A789, #4E4B66). Motion carries the page through
a cartoon strategist walking through a green maze. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustration

## Reference lock

Primary reference/direction: Parker - AI creative strategist for ads — A product page: a beige vintage Mac whose screen types 'The way you make ads is...' then 'Meet Parker', a cartoon moustached man thinking on violet with platform icons, 'Parker tells you what ads to make', 'Let me sh_' with drawn arrows, step tabs (Research, Chat, Grow) as coloured folders, a green maze the character walks through ('Creative strategy used to be a maze'), 'What makes Parker different?' with his open head on three colour arcs, pricing, testimonials and a big red 'Parker' footer.
Preserve (3-5 traits): vintage Mac typing; cartoon character; colour panels per step; drawn arrows; maze walk.
Borrow only (1-2): Let one character carry the reader through each panel; Type the first words on a device before the page opens
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustration
Reject: Many sections
Token commitments: palette #FFFFFF, #B3A789, #4E4B66, #DDD2AD; type Radio Canada, Radio Canada Big, Source Serif Pro Regular, Inter Display; engine GSAP + Lenis linked (never vendored).
