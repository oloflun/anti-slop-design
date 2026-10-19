---
title: "AIM - AI Modernism of Kharkiv (Obys)"
url: https://aim.obys.agency/
source_url: https://aim.obys.agency/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "portfolio"
family: constructivist-blocks-ai-gallery
dna: "AI art experiment x cream and black, heavy black bars that tumble from the AIM wordmark, generated modernist portraits"
register: historical art
grammar: typographic poster
lane: "An AI experiment reimagining 1910-30 Kharkiv modernism: a white square on black splitting into bars, 'AIM' as a huge wordmark built from black bars on cream, the bars tumbling apart and falling through 'AI Modernism of Kharkiv' and a long statement, settling into three upright slabs, a black curtain opening onto generated images (a figure in striped dress before constructivist shapes and an orange sun), and an 'Explore experiment' gallery."
mode: experience
traits: ["wordmark built of bars", "bars tumble and fall through text", "cream and black", "generated constructivist imagery", "Swiss header grid"]
palette: ["#E7E4DE", "#141414", "#85837F"]
type: ["Khtekatrial"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Breaking the wordmark into constructivist bars that fall through the text makes the page itself behave like the movement it studies.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Obys Agency).

## What to borrow (principle)

- Build the mark from parts that later become the page's shapes

## What to leave

- Very small header labels

## Signature move

Black bars of the AIM wordmark tumbling through the text on cream.

## Motion

Intro: a white square splits into bars (~2 s). Wheel (Lenis): bars fall with physics and rotation; text reveals by line; slabs rise; a curtain opens on the images.

Measured (`motion/probe.json`): Lenis; smoothed scroll (median 127 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the typographic poster grammar: an AI experiment reimagining 1910-30 Kharkiv modernism: a white square on black splitting into bars, 'AIM' as a huge wordmark built from black bars on cream, the bars tumbling apart and falling through 'AI Modernism of Kharkiv' and a long statement, settling into three upright slabs, a black curtain opening onto generated images (a figure in striped dress before constructivist shapes and an orange sun), and an 'Explore experiment' gallery. Type: Khtekatrial.
Ground and ink from the measured palette (#E7E4DE, #141414, #85837F). Motion carries the page through
black bars of the AIM wordmark tumbling through the text on cream. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — generated imagery

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: generated imagery

## Reference lock

Primary reference/direction: AIM - AI Modernism of Kharkiv (Obys) — An AI experiment reimagining 1910-30 Kharkiv modernism: a white square on black splitting into bars, 'AIM' as a huge wordmark built from black bars on cream, the bars tumbling apart and falling through 'AI Modernism of Kharkiv' and a long statement, settling into three upright slabs, a black curtain opening onto generated images (a figure in striped dress before constructivist shapes and an orange sun), and an 'Explore experiment' gallery.
Preserve (3-5 traits): wordmark built of bars; bars tumble and fall through text; cream and black; generated constructivist imagery; Swiss header grid.
Borrow only (1-2): Build the mark from parts that later become the page's shapes
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: generated imagery
Reject: Very small header labels
Token commitments: palette #E7E4DE, #141414, #85837F; type Khtekatrial; engine GSAP + Lenis linked (never vendored).
