---
title: "Matt Jinn"
url: https://mattjinn.com/
source_url: https://mattjinn.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: single-portrait-artist-card
dna: "Musician link page x serif italic over portrait"
register: warm photographic
grammar: typographic poster
lane: "A one-screen musician page: a lowercase serif name assembles letter by letter on white, then the white lifts to a warm shadowed portrait with the name set large in italic over it and streaming links beneath."
mode: read
traits: ["single full-bleed portrait", "large lowercase italic serif name", "letter-by-letter name assembly on white", "small release card bottom-left", "no scroll"]
palette: ["#9E968C", "#080503", "#251E18", "#A27F62", "#7C553C", "#C0B8B0"]
type: ["omnes-pro", "big-caslon-fb"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

An artist page that is a poster: one warm, hard-shadowed portrait and the name in a big italic serif, nothing else above the links. The intro builds the name in grey letters on white first, so the photograph arrives as a reveal of who the letters are.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Luis Bizarro, Williams Alamu).

## What to borrow (principle)

- Build the name on a blank ground first, then lift the ground to the portrait
- Italic serif at display size over a photo for an intimate voice
- One release card as the only secondary element

## What to leave

- Nothing beyond the fold
- Name over the face's shadow side loses contrast at the descender

## Signature move

A grey serif name that assembles on white before the white lifts to the portrait.

## Motion

Intro: letters of 'matt jinn' fade in individually in grey on white (~1.2 s, SplitText + CustomEase), then the white ground lifts away revealing the portrait with the name now large in italic. The page holds; no scroll motion.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x2; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the typographic poster grammar: a one-screen musician page: a lowercase serif name assembles letter by letter on white, then the white lifts to a warm shadowed portrait with the name set large in italic over it and streaming links beneath. Type: omnes-pro, big-caslon-fb.
Ground and ink from the measured palette (#9E968C, #080503, #251E18). Motion carries the page through
a grey serif name that assembles on white before the white lifts to the portrait. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — warm hard-light portrait with a cast shadow on a plain wall

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: warm hard-light portrait with a cast shadow on a plain wall

## Reference lock

Primary reference/direction: Matt Jinn — A one-screen musician page: a lowercase serif name assembles letter by letter on white, then the white lifts to a warm shadowed portrait with the name set large in italic over it and streaming links beneath.
Preserve (3-5 traits): single full-bleed portrait; large lowercase italic serif name; letter-by-letter name assembly on white; small release card bottom-left; no scroll.
Borrow only (1-2): Build the name on a blank ground first, then lift the ground to the portrait; Italic serif at display size over a photo for an intimate voice
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: warm hard-light portrait with a cast shadow on a plain wall
Reject: Nothing beyond the fold; Name over the face's shadow side loses contrast at the descender
Token commitments: palette #9E968C, #080503, #251E18, #A27F62, #7C553C, #C0B8B0; type omnes-pro, big-caslon-fb; engine GSAP + Lenis linked (never vendored).
