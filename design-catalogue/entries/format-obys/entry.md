---
title: "FORMAT - Obys format study"
url: https://format.obys.agency/
source_url: https://format.obys.agency/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: shape-format-study
dna: "Format study x block wordmark and circle / triangle shape chapters"
register: cinematic dark
grammar: chaptered editorial
lane: "A design study on charcoal: a chunky pixel-block 'FORMAT' wordmark building, a grey plinth, collage of usage lists (Desktop, Business cards, Editorial, TV), a white circle as a dial with a needle, 'CIRCLE FORMAT IS CENTERED, CALM AND SMOOTH' set on a circle, a 'TRIANGLE' tag with text set inside a triangle, photos clipped into circles and triangles, a huge white arc rotating like a dial, 'THE FORMAT IS PART OF THE BIGGER IDEA' with letters falling out of line, a sunflower print, and the whole layout shrinking into a small card on black with 'click'."
mode: experience
traits: ["chunky block wordmark", "text set inside shapes", "dial with needle", "photos clipped to circle and triangle", "giant rotating arc", "letters falling out of a line"]
palette: ["#222222", "#FFFFFF", "#7F7F7F", "#B5B5B5"]
type: ["Obys Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Each format (circle, triangle) is demonstrated by the layout itself, so the page is the lesson.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Obys Agency).

## What to borrow (principle)

- Set the text inside the shape it describes
- Shrink the whole layout into a card at the end

## What to leave

- Hard to read crops

## Signature move

'CIRCLE FORMAT IS CENTERED, CALM AND SMOOTH' set around a circle.

## Motion

Intro: the block wordmark builds (~2 s), the plinth rises. Wheel (Lenis): collage panels slide; the dial rotates; circle text spins; the triangle drops; photos clip into shapes; the arc sweeps; letters fall; the page shrinks to a card.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 155 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a design study on charcoal: a chunky pixel-block 'FORMAT' wordmark building, a grey plinth, collage of usage lists (Desktop, Business cards, Editorial, TV), a white circle as a dial with a needle, 'CIRCLE FORMAT IS CENTERED, CALM AND SMOOTH' set on a circle, a 'TRIANGLE' tag with text set inside a triangle, photos clipped into circles and triangles, a huge white arc rotating like a dial, 'THE FORMAT IS PART OF THE BIGGER IDEA' with letters falling out of line, a sunflower print, and the whole layout shrinking into a small card on black with 'click'. Type: Obys Sans.
Ground and ink from the measured palette (#222222, #FFFFFF, #7F7F7F). Motion carries the page through
'CIRCLE FORMAT IS CENTERED, CALM AND SMOOTH' set around a circle. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photography, shapes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photography, shapes

## Reference lock

Primary reference/direction: FORMAT - Obys format study — A design study on charcoal: a chunky pixel-block 'FORMAT' wordmark building, a grey plinth, collage of usage lists (Desktop, Business cards, Editorial, TV), a white circle as a dial with a needle, 'CIRCLE FORMAT IS CENTERED, CALM AND SMOOTH' set on a circle, a 'TRIANGLE' tag with text set inside a triangle, photos clipped into circles and triangles, a huge white arc rotating like a dial, 'THE FORMAT IS PART OF THE BIGGER IDEA' with letters falling out of line, a sunflower print, and the whole layout shrinking into a small card on black with 'click'.
Preserve (3-5 traits): chunky block wordmark; text set inside shapes; dial with needle; photos clipped to circle and triangle; giant rotating arc.
Borrow only (1-2): Set the text inside the shape it describes; Shrink the whole layout into a card at the end
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photography, shapes
Reject: Hard to read crops
Token commitments: palette #222222, #FFFFFF, #7F7F7F, #B5B5B5; type Obys Sans; engine GSAP + Lenis linked (never vendored).
