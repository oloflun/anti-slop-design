---
title: "See What Eye See"
url: https://www.seewhateyesee.org/
source_url: https://www.seewhateyesee.org/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "institutional"
family: dark-mascot-simulator
dna: "Charity awareness campaign x Pixar-lit 3D mascot"
register: illustrated dark
grammar: filmic one-shot
lane: "A black screen speaks two lines of copy one at a time over a dim lamp-lit room, then a 3D eyeball mascot in an armchair lands with a brush-script headline and two entry buttons into a vision-loss simulator."
mode: experience
traits: ["copy-first intro sequence on black", "3D WebGL mascot as the hero", "hand-brush display face", "single warm lamp light", "entry buttons instead of scroll"]
palette: ["#000000", "#2B1D14", "#745443"]
type: ["exo-2-variable", "brush-up-too"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page withholds the product: the first four seconds are only sentences ('You can still drive. You can still read. Until one day, you can't.'), each wiped in and out on black with a lamp barely glowing behind. Only after the copy has made the point does the light come up on the mascot and the headline. The brush face and the pink-on-amber palette keep a heavy subject (vision loss) approachable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: A24, Built Kindly, David Lubofsky, Huy Phan, Huy Phan Portfolio, Illoca, Jesper Langberg, Ravi Klaassens, Revelatio Studio, Tom Miller, Unseen Studio).

## What to borrow (principle)

- Let two or three timed lines of copy do the opening before any image; the reveal of the hero then reads as the answer
- Light the hero up out of the dark instead of fading it in: the scene was there all along
- Give an experience page explicit entry buttons rather than pretending it scrolls

## What to leave

- The page does not scroll at all: nothing below the fold to reach without a click
- Brush display type at hero scale only works for a campaign voice

## Signature move

A copy-only intro on black that ends by lighting the 3D mascot already sitting in the dark room.

## Motion

Intro: text lines appear and wipe out one by one at centre (~1 s each) over a near-black frame where only a lamp glows. Hero: the room brightens, the eyeball character in its chair comes up, headline and CTA pills settle in. After that the page is static under the wheel; the simulator lives behind the two buttons (WebGL, three.js).

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x2 (three.js); 1 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the filmic one-shot grammar: a black screen speaks two lines of copy one at a time over a dim lamp-lit room, then a 3D eyeball mascot in an armchair lands with a brush-script headline and two entry buttons into a vision-loss simulator. Type: exo-2-variable, brush-up-too.
Ground and ink from the measured palette (#000000, #2B1D14, #745443). Motion carries the page through
a copy-only intro on black that ends by lighting the 3D mascot already sitting in the dark room. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — one character render, low-key tungsten light, deep blacks, warm practical lamp in frame

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: one character render, low-key tungsten light, deep blacks, warm practical lamp in frame

## Reference lock

Primary reference/direction: See What Eye See — A black screen speaks two lines of copy one at a time over a dim lamp-lit room, then a 3D eyeball mascot in an armchair lands with a brush-script headline and two entry buttons into a vision-loss simulator.
Preserve (3-5 traits): copy-first intro sequence on black; 3D WebGL mascot as the hero; hand-brush display face; single warm lamp light; entry buttons instead of scroll.
Borrow only (1-2): Let two or three timed lines of copy do the opening before any image; the reveal of the hero then reads as the answer; Light the hero up out of the dark instead of fading it in: the scene was there all along
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: one character render, low-key tungsten light, deep blacks, warm practical lamp in frame
Reject: The page does not scroll at all: nothing below the fold to reach without a click; Brush display type at hero scale only works for a campaign voice
Token commitments: palette #000000, #2B1D14, #745443; type exo-2-variable, brush-up-too; engine GSAP + Lenis linked (never vendored).
