---
title: "Studio Lumio - Digital Experience Agency"
url: https://studiolumio.com/
source_url: https://studiolumio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: smoke-field-agency-hero
dna: "Digital experience agency x condensed name over a drifting smoke field"
register: cinematic dark
grammar: live surface
lane: "An agency hero: 'Studio Lumio' split with a sound choice between the words, then a dark field of drifting grey smoke and stars with the condensed name, which scrambles and resolves, and a small project card cycling in the corner."
mode: experience
traits: ["sound choice between the two words", "drifting smoke field", "condensed uppercase name", "text scramble", "small cycling project card", "lime nav button"]
palette: ["#111111", "#413F3F", "#94948C"]
type: ["Oswald", "GeistSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The sound gate is integrated into the name itself, and the smoke field gives one hero real atmosphere; the capture shows nothing beyond it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Put the sound choice inside the wordmark

## What to leave

- Capture did not move past the hero
- Tiny corner card

## Signature move

'Studio Lumio' resolving over drifting grey smoke and stars.

## Motion

Intro: black, the name splits to reveal 'enter with sound / without sound' (without clicked), the words scramble out and the smoke field fades in (~3 s). Wheel: the name scrambles once and settles; the corner card cycles projects; the smoke keeps drifting.

Measured (`motion/probe.json`): GSAP 3.14.2; WebGL canvas x2 (three.js); 2 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Enter without sound. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an agency hero: 'Studio Lumio' split with a sound choice between the words, then a dark field of drifting grey smoke and stars with the condensed name, which scrambles and resolves, and a small project card cycling in the corner. Type: Oswald, GeistSans.
Ground and ink from the measured palette (#111111, #413F3F, #94948C). Motion carries the page through
'Studio Lumio' resolving over drifting grey smoke and stars. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL smoke, project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL smoke, project thumbnails

## Reference lock

Primary reference/direction: Studio Lumio - Digital Experience Agency — An agency hero: 'Studio Lumio' split with a sound choice between the words, then a dark field of drifting grey smoke and stars with the condensed name, which scrambles and resolves, and a small project card cycling in the corner.
Preserve (3-5 traits): sound choice between the two words; drifting smoke field; condensed uppercase name; text scramble; small cycling project card.
Borrow only (1-2): Put the sound choice inside the wordmark
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL smoke, project thumbnails
Reject: Capture did not move past the hero; Tiny corner card
Token commitments: palette #111111, #413F3F, #94948C; type Oswald, GeistSans; engine GSAP + Lenis linked (never vendored).
