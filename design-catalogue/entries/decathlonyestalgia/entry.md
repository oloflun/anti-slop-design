---
title: "Decathlon Yestalgia"
url: https://decathlonyestalgia.com/
source_url: https://decathlonyestalgia.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: memphis-retro-sport-capsule
dna: "Sporting-goods retro capsule x Memphis 80s shapes"
register: other
grammar: chaptered editorial
lane: "A retro-capsule collection page in pink with Memphis squiggles, lightning bolts and half-suns that float around photographs, condensed headlines that type in, an illustrated character on a cassette deck, and products named one by one in huge condensed caps."
mode: persuade
traits: ["Memphis shapes (squiggles, bolts, half-suns)", "pink ground", "condensed caps product names", "illustrated 80s character", "photo strips of the collection", "Roboto Flex variable"]
palette: ["#EAA2CF", "#F5F5F5", "#3E2E39", "#A78A89", "#C0ADAF", "#DAD4C9"]
type: ["Roboto Flex"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The 80s are brought by shapes, not filters: Memphis squiggles and bolts orbit every photograph, and the products are named in huge condensed caps like a catalogue from the decade. The photos stay modern and bright, so it reads as a capsule today, not a costume.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Index, Index Studio, Quentin Hocde).

## What to borrow (principle)

- Float a small set of era shapes around modern photos to set a period
- Name each product in huge condensed caps as its own beat

## What to leave

- Headlines are often cropped by the frame
- Busy: shapes on every section

## Signature move

Memphis squiggles and lightning bolts orbiting photographs on pink.

## Motion

Intro: photo cards swap in the centre with shapes floating around (~1 s). Scroll (Lenis, ~35 px glide, SplitText, Observer, WebGL x5): full-bleed fashion shot; 'À VOS CÔTÉS DEPUIS…' typing in; illustrated character on a cassette deck; 'LA DÉCENNIE LA PLUS VIBRANTE' lines revealing; product photo grids; artist intro; 'OG2K' wordmark; product names (T-SHIRT GRAPHIQUE, SAC, SHORT, CHAUSSETTES) stack in condensed caps; closing Yestalgia logo with shapes.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x5; 16 video; split text; smoothed scroll (median 39 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a retro-capsule collection page in pink with Memphis squiggles, lightning bolts and half-suns that float around photographs, condensed headlines that type in, an illustrated character on a cassette deck, and products named one by one in huge condensed caps. Type: Roboto Flex.
Ground and ink from the measured palette (#EAA2CF, #F5F5F5, #3E2E39). Motion carries the page through
memphis squiggles and lightning bolts orbiting photographs on pink. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — bright lifestyle fashion photography with 80s-styled props

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: bright lifestyle fashion photography with 80s-styled props

## Reference lock

Primary reference/direction: Decathlon Yestalgia — A retro-capsule collection page in pink with Memphis squiggles, lightning bolts and half-suns that float around photographs, condensed headlines that type in, an illustrated character on a cassette deck, and products named one by one in huge condensed caps.
Preserve (3-5 traits): Memphis shapes (squiggles, bolts, half-suns); pink ground; condensed caps product names; illustrated 80s character; photo strips of the collection.
Borrow only (1-2): Float a small set of era shapes around modern photos to set a period; Name each product in huge condensed caps as its own beat
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: bright lifestyle fashion photography with 80s-styled props
Reject: Headlines are often cropped by the frame; Busy: shapes on every section
Token commitments: palette #EAA2CF, #F5F5F5, #3E2E39, #A78A89, #C0ADAF, #DAD4C9; type Roboto Flex; engine GSAP + Lenis linked (never vendored).
