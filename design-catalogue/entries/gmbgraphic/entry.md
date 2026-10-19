---
title: "Guillaume Maurin-Belay - Graphic Designer"
url: https://www.gmbgraphic.com/
source_url: https://www.gmbgraphic.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: music-video-titles-reel
dna: "Graphic designer for music videos x a centred clip window between a split name"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A title designer's folio: 'GUILLAUME' top left and 'MAURIN-BELAY' bottom right on black, then a centred window plays his music-video title sequences one after another (Girlfriend, Say you love me, That Door, Mardy) while faint thumbnails of other projects sit around it."
mode: experience
traits: ["name split across corners", "centred clip window", "music video title sequences", "faint thumbnails around", "black ground", "condensed bold name"]
palette: ["#000000", "#ADAEBD", "#384950", "#131618", "#E0E0DF", "#7E6C76"]
type: ["Ppneuemontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The work is title design, so a single window playing titles framed by the split name is all it needs.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Split the name across opposite corners to frame the work

## What to leave

- Nothing else on the page

## Signature move

Music-video title sequences in a centred window between a split name.

## Motion

Intro: the name in grey brightens and splits to the corners (~2 s), thumbnails scatter. Scroll: the centre window steps through clips.

Measured (`motion/probe.json`): GSAP 3.9.1; 16 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a title designer's folio: 'GUILLAUME' top left and 'MAURIN-BELAY' bottom right on black, then a centred window plays his music-video title sequences one after another (Girlfriend, Say you love me, That Door, Mardy) while faint thumbnails of other projects sit around it. Type: Ppneuemontreal.
Ground and ink from the measured palette (#000000, #ADAEBD, #384950). Motion carries the page through
music-video title sequences in a centred window between a split name. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — music video stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: music video stills

## Reference lock

Primary reference/direction: Guillaume Maurin-Belay - Graphic Designer — A title designer's folio: 'GUILLAUME' top left and 'MAURIN-BELAY' bottom right on black, then a centred window plays his music-video title sequences one after another (Girlfriend, Say you love me, That Door, Mardy) while faint thumbnails of other projects sit around it.
Preserve (3-5 traits): name split across corners; centred clip window; music video title sequences; faint thumbnails around; black ground.
Borrow only (1-2): Split the name across opposite corners to frame the work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: music video stills
Reject: Nothing else on the page
Token commitments: palette #000000, #ADAEBD, #384950, #131618, #E0E0DF, #7E6C76; type Ppneuemontreal; engine GSAP + Lenis linked (never vendored).
