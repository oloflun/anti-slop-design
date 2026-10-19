---
title: "bleibtgleich"
url: https://bleibtgleich.dev/
source_url: https://bleibtgleich.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: stretched-sentence-swiss-folio
dna: "UX/UI developer folio x Swiss sentence typography"
register: modern clean
grammar: typographic poster
lane: "A white Swiss folio where short sentences are set in staggered lines on a hairline axis, each word smeared horizontally as it arrives, and a cloud of small work cards orbits between 'Work' and '24-26'."
mode: persuade
traits: ["staggered sentence lines on a vertical hairline", "smeared/ink-drag word reveal", "Akzidenz Grotesk only", "orbiting card cloud for work", "grey edge wordmarks 'bleibt' 'gleich'", "percentage loader"]
palette: ["#FFFFFF", "#131313", "#E3E3E2", "#B1B1B1", "#5A5A5A"]
type: ["Akzidenz Grotesk Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The whole folio is set as typographic sentences ('the best ideas deserve execution.', 'nothing more than a sentence.'), staggered on a hairline axis. The motion is in the ink: each word arrives smeared sideways like wet print and snaps sharp. Work is a small 3D cloud of cards between two words, so even the gallery is part of a sentence.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Maksym Ponomarenko).

## What to borrow (principle)

- Reveal words with a horizontal smear that resolves (MorphSVG/blur), as if ink is still wet
- Stagger short sentences on a fixed hairline axis instead of centring them
- Place the gallery inside a sentence: 'Work [cards] 24-26'

## What to leave

- Smear frames make words illegible mid-transition
- Very sparse; little information density

## Signature move

Words that arrive smeared sideways like wet ink and snap sharp on a hairline axis.

## Motion

Intro: percentage counter bottom-left (78%), then the vertical hairline draws and the name and role set in (~2 s). Scroll (Lenis, ~135 px glide, 15 ScrollTriggers, Barba): each sentence's words come in with a horizontal ink-smear and resolve; 'Work 24-26' splits apart as a 3D ring of small cards rotates between; 'Awards & Recognitions' table; clock '(16 : 38)' with an image between the digits; closing sentence and wordmark.

Measured (`motion/probe.json`): GSAP 3.15.0; 15 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x2 (three.js); smoothed scroll (median 137 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the typographic poster grammar: a white Swiss folio where short sentences are set in staggered lines on a hairline axis, each word smeared horizontally as it arrives, and a cloud of small work cards orbits between 'Work' and '24-26'. Type: Akzidenz Grotesk Pro.
Ground and ink from the measured palette (#FFFFFF, #131313, #E3E3E2). Motion carries the page through
words that arrive smeared sideways like wet ink and snap sharp on a hairline axis. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — small black-and-white work cards, mono objects

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: small black-and-white work cards, mono objects

## Reference lock

Primary reference/direction: bleibtgleich — A white Swiss folio where short sentences are set in staggered lines on a hairline axis, each word smeared horizontally as it arrives, and a cloud of small work cards orbits between 'Work' and '24-26'.
Preserve (3-5 traits): staggered sentence lines on a vertical hairline; smeared/ink-drag word reveal; Akzidenz Grotesk only; orbiting card cloud for work; grey edge wordmarks 'bleibt' 'gleich'.
Borrow only (1-2): Reveal words with a horizontal smear that resolves (MorphSVG/blur), as if ink is still wet; Stagger short sentences on a fixed hairline axis instead of centring them
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: small black-and-white work cards, mono objects
Reject: Smear frames make words illegible mid-transition; Very sparse; little information density
Token commitments: palette #FFFFFF, #131313, #E3E3E2, #B1B1B1, #5A5A5A; type Akzidenz Grotesk Pro; engine GSAP + Lenis linked (never vendored).
