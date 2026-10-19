---
title: "Getty - Frank Gehry and Walt Disney Concert Hall"
url: https://gehry.getty.edu/
source_url: https://gehry.getty.edu/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "institutional"
family: poster-type-architecture-story
dna: "Architecture story x orange, green, blue and black colour fields, a hand-drawn Gehry scribble, enormous condensed chapter titles and archival models"
register: historical art
grammar: chaptered editorial
lane: "A sound-on archive story: on orange a Gehry-style pen scribble draws itself, a black wordmark slides in over an aerial video of the concert hall, chapters open as full-colour fields with giant condensed titles that break apart ('Ship in the box' with a scribbled ship, 'Sea of sound', 'Shaping', 'Making noise', 'A place to gather'), between them archival paper models rotate on black, sketches and photos slide in, and a video of the orchestra closes the story above a gallery of archive items."
mode: read
traits: ["self-drawing pen scribble", "giant condensed chapter titles", "solid colour fields per chapter", "rotating archival models", "sound-on narration"]
palette: ["#FFA541", "#16A247", "#202220", "#2F6B3E", "#826F53", "#A8BC7D"]
type: ["Roboto Mono", "Reckless"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The architect's own scribble draws the thread, and each chapter's title is set so large it reads like the building's own shapes.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Resn).

## What to borrow (principle)

- Let the subject's own hand (a sketch line) draw the thread between chapters

## What to leave

- Sound prompt

## Signature move

A Gehry-style scribble drawing itself on orange before the hall appears.

## Motion

Intro: scribble draws (~3 s). Wheel (Lenis): videos scrub; titles slide and break by letter; models rotate; colour fields wipe between chapters.

Measured (`motion/probe.json`): GSAP 3.12.1; 82 ScrollTriggers; Lenis; WebGL canvas x1 (three.js); 19 video; split text; smoothed scroll (median 73 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the chaptered editorial grammar: a sound-on archive story: on orange a Gehry-style pen scribble draws itself, a black wordmark slides in over an aerial video of the concert hall, chapters open as full-colour fields with giant condensed titles that break apart ('Ship in the box' with a scribbled ship, 'Sea of sound', 'Shaping', 'Making noise', 'A place to gather'), between them archival paper models rotate on black, sketches and photos slide in, and a video of the orchestra closes the story above a gallery of archive items. Type: Roboto Mono, Reckless.
Ground and ink from the measured palette (#FFA541, #16A247, #202220). Motion carries the page through
a Gehry-style scribble drawing itself on orange before the hall appears. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — aerial video, archival models and sketches

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: aerial video, archival models and sketches

## Reference lock

Primary reference/direction: Getty - Frank Gehry and Walt Disney Concert Hall — A sound-on archive story: on orange a Gehry-style pen scribble draws itself, a black wordmark slides in over an aerial video of the concert hall, chapters open as full-colour fields with giant condensed titles that break apart ('Ship in the box' with a scribbled ship, 'Sea of sound', 'Shaping', 'Making noise', 'A place to gather'), between them archival paper models rotate on black, sketches and photos slide in, and a video of the orchestra closes the story above a gallery of archive items.
Preserve (3-5 traits): self-drawing pen scribble; giant condensed chapter titles; solid colour fields per chapter; rotating archival models; sound-on narration.
Borrow only (1-2): Let the subject's own hand (a sketch line) draw the thread between chapters
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: aerial video, archival models and sketches
Reject: Sound prompt
Token commitments: palette #FFA541, #16A247, #202220, #2F6B3E, #826F53, #A8BC7D; type Roboto Mono, Reckless; engine GSAP + Lenis linked (never vendored).
