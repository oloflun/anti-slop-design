---
title: "Good Fella"
url: http://good-fella.com/
source_url: http://good-fella.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: orange-block-studio-process
dna: "Digital studio x orange block reveals and grey-white"
register: modern clean
grammar: chaptered editorial
lane: "A two-founder studio site that opens on a full orange screen, reveals headlines by sliding an orange-and-black block off them, counts big numbers beside a founders' photo, runs 'How we work' steps lighting one at a time, and shows selected work as device mockups beside a thumbnail rail."
mode: persuade
traits: ["full orange flash intro", "orange/black block wipe revealing text", "big counted numbers", "steps lit one at a time", "device mockups with thumbnail rail", "grey-white and black alternation"]
palette: ["#EFEFEF", "#131313", "#897F7B"]
type: ["geistMono", "aktiv-grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One gesture repeats: an orange-and-black block slides across a line of text and leaves it revealed, used for every key heading. Combined with a process list that lights one step at a time, the page has a clear rhythm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Reveal headings with a two-colour block wipe
- Light one process step at a time with its own photo

## What to leave

- Block wipes cover the text for many frames
- Generic mockup grid

## Signature move

An orange-and-black block sliding across each heading to reveal it.

## Motion

Intro: full orange, a logo, then black (~2 s). Scroll (Lenis, WebGL x3, SplitText): 'The digital landmark studio.' over a pixel portrait; numbers count ($50B+, 10M+, 50+); 'How we work' steps (brief, conversation, design and build, ship) light one by one with changing photos; block wipe into 'Selected work' with mockups and a thumbnail rail; FAQ; 'Start a…' block wipe; founders.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x3 (three.js); smoothed scroll (median 141 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a two-founder studio site that opens on a full orange screen, reveals headlines by sliding an orange-and-black block off them, counts big numbers beside a founders' photo, runs 'How we work' steps lighting one at a time, and shows selected work as device mockups beside a thumbnail rail. Type: geistMono, aktiv-grotesk.
Ground and ink from the measured palette (#EFEFEF, #131313, #897F7B). Motion carries the page through
an orange-and-black block sliding across each heading to reveal it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white founder photography, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white founder photography, device mockups

## Reference lock

Primary reference/direction: Good Fella — A two-founder studio site that opens on a full orange screen, reveals headlines by sliding an orange-and-black block off them, counts big numbers beside a founders' photo, runs 'How we work' steps lighting one at a time, and shows selected work as device mockups beside a thumbnail rail.
Preserve (3-5 traits): full orange flash intro; orange/black block wipe revealing text; big counted numbers; steps lit one at a time; device mockups with thumbnail rail.
Borrow only (1-2): Reveal headings with a two-colour block wipe; Light one process step at a time with its own photo
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white founder photography, device mockups
Reject: Block wipes cover the text for many frames; Generic mockup grid
Token commitments: palette #EFEFEF, #131313, #897F7B; type geistMono, aktiv-grotesk; engine GSAP + Lenis linked (never vendored).
