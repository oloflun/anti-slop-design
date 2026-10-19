---
title: "Son Daven"
url: https://sondaven.com/en
source_url: https://sondaven.com/en
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "luxury-craft"
family: carpathian-engraving-resort
dna: "Carpathian design resort x stippled engraving graphics"
register: warm photographic
grammar: chaptered editorial
lane: "A mountain resort in khaki and dark brown where stippled, engraved-style illustrations (sheep, firs, the moon, mountains) dissolve between photographs, a giant mono wordmark builds in pixel blocks, and sections arrive as collages of photos over the engraving texture."
mode: persuade
traits: ["stippled/engraved line illustrations", "khaki and deep brown palette", "pixel-built wordmark", "photos collaged over engraving texture", "condensed serif caps", "15 WebGL canvases"]
palette: ["#A59272", "#2E2923", "#574E40", "#D6CFC9", "#B0AAA2"]
type: ["KTF Metro Roman", "KTF Metro Blueline"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The region's folklore is drawn as stippled line-engravings (sheep, fir trees, moon) that appear between sections and dissolve into photographs, so the resort has a texture of its own that no stock photo can give. The palette is the colour of wool and wood.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: THE FIRST THE LAST, The First The Last).

## What to borrow (principle)

- Draw local motifs as stippled engraving that dissolves into photography
- A two-colour palette from the place's materials (wool, wood)
- Build the wordmark from pixel blocks in the intro

## What to leave

- Cookie bar over every frame
- 100 ScrollTriggers on a long page

## Signature move

Stippled engravings of sheep, firs and the moon dissolving into the resort's photographs.

## Motion

Intro: a stippled sheep walks across brown, 'SON DAVEN' builds in pixel blocks, fir trees rise (~2 s). Scroll (Lenis, ~120 px glide, 100 ScrollTriggers, Barba, SplitText, WebGL x15): building render; sheep engraving; serif logo with 'concept'; 31 min walk dial; moon/forest engraving; 'WHY SON DAVEN CAPTIVATE'; photo collages over textures; construction timeline; financial indicators marquee; engraved mountains; project gallery; news; FAQ letters spaced wide.

Measured (`motion/probe.json`): GSAP 3.13.0; 100 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x15; 3 video; split text; smoothed scroll (median 130 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a mountain resort in khaki and dark brown where stippled, engraved-style illustrations (sheep, firs, the moon, mountains) dissolve between photographs, a giant mono wordmark builds in pixel blocks, and sections arrive as collages of photos over the engraving texture. Type: KTF Metro Roman, KTF Metro Blueline.
Ground and ink from the measured palette (#A59272, #2E2923, #574E40). Motion carries the page through
stippled engravings of sheep, firs and the moon dissolving into the resort's photographs. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural renders in mountain mist plus stippled engraving illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural renders in mountain mist plus stippled engraving illustration

## Reference lock

Primary reference/direction: Son Daven — A mountain resort in khaki and dark brown where stippled, engraved-style illustrations (sheep, firs, the moon, mountains) dissolve between photographs, a giant mono wordmark builds in pixel blocks, and sections arrive as collages of photos over the engraving texture.
Preserve (3-5 traits): stippled/engraved line illustrations; khaki and deep brown palette; pixel-built wordmark; photos collaged over engraving texture; condensed serif caps.
Borrow only (1-2): Draw local motifs as stippled engraving that dissolves into photography; A two-colour palette from the place's materials (wool, wood)
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural renders in mountain mist plus stippled engraving illustration
Reject: Cookie bar over every frame; 100 ScrollTriggers on a long page
Token commitments: palette #A59272, #2E2923, #574E40, #D6CFC9, #B0AAA2; type KTF Metro Roman, KTF Metro Blueline; engine GSAP + Lenis linked (never vendored).
