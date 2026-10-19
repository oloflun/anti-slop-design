---
title: "Glenn Catteeuw - Interactive Art Director"
url: https://glenncatteeuw.com/
source_url: https://glenncatteeuw.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: looping-project-list-over-film
dna: "Interactive art director x condensed project list looping over a desert film"
register: cinematic dark
grammar: typographic poster
lane: "An art director's one-screen folio behind a sound choice: the name types in as staggered condensed italic on white, then an orange mountain film fills the screen and an endless list of project names in condensed uppercase loops upward over it."
mode: read
traits: ["ENTER WITHOUT SOUND gate", "staggered italic condensed name", "infinite looping project list", "orange film behind type", "tiny mono metadata", "no images per project on scroll"]
palette: ["#CD6F0E", "#692704", "#DFC3AA", "#8E4F27", "#EDE2D8", "#D29559"]
type: ["Replica Mono", "Druk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

An infinite list makes the body of work feel bottomless, and the warm film keeps a list of names from being dry.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Loop the project list so scroll never ends
- Put a list of names straight over moving footage

## What to leave

- List repeats without showing work
- Only one mode for the whole page

## Signature move

An endless list of condensed project names scrolling over an orange mountain film.

## Motion

Intro: ENTER WITHOUT SOUND (unlocked), the name and title stagger in letter by letter on white (~2 s), then the film cuts in. Wheel (Lenis, ~60 px glide): the list scrolls and wraps around endlessly; the film keeps playing; hover would swap previews.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 33 px still travelling after input stops); entry gate: ENTER WITHOUT SOUND. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the typographic poster grammar: an art director's one-screen folio behind a sound choice: the name types in as staggered condensed italic on white, then an orange mountain film fills the screen and an endless list of project names in condensed uppercase loops upward over it. Type: Replica Mono, Druk.
Ground and ink from the measured palette (#CD6F0E, #692704, #DFC3AA). Motion carries the page through
an endless list of condensed project names scrolling over an orange mountain film. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — warm landscape film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: warm landscape film

## Reference lock

Primary reference/direction: Glenn Catteeuw - Interactive Art Director — An art director's one-screen folio behind a sound choice: the name types in as staggered condensed italic on white, then an orange mountain film fills the screen and an endless list of project names in condensed uppercase loops upward over it.
Preserve (3-5 traits): ENTER WITHOUT SOUND gate; staggered italic condensed name; infinite looping project list; orange film behind type; tiny mono metadata.
Borrow only (1-2): Loop the project list so scroll never ends; Put a list of names straight over moving footage
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: warm landscape film
Reject: List repeats without showing work; Only one mode for the whole page
Token commitments: palette #CD6F0E, #692704, #DFC3AA, #8E4F27, #EDE2D8, #D29559; type Replica Mono, Druk; engine GSAP + Lenis linked (never vendored).
