---
title: "TA Design - Interior design"
url: https://www.tadesign.nl/
source_url: https://www.tadesign.nl/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: interior-designer-serif-beige
dna: "Dutch interior designer x 3D interior renders and a giant serif name"
register: warm photographic
grammar: chaptered editorial
lane: "An interior design studio on warm beige: full-bleed 3D interior renders (a mountain-mural bedroom, an arched bathroom), 'TA DESIGN' in a huge thin serif cut by horizontal strips, a portrait, 'Waar jouw plekje jouw verhaal vertelt', small interiors drifting around service statements, full-bleed rooms with a quote, project cards, testimonials, blog and a form above a repeated giant name."
mode: read
traits: ["full-bleed interior renders", "huge thin serif name sliced in strips", "warm beige and olive", "small photos drifting around statements", "quote over a room", "giant name footer"]
palette: ["#4E5647", "#E1D2BE", "#A09788"]
type: ["Pangaia", "Inter 24 Pt"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The sliced giant serif name and drifting interior photos give a solo designer an editorial, calm presence.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Slice the giant name into horizontal strips as it reveals

## What to leave

- Thin serif small text

## Signature move

'TA DESIGN' in a huge thin serif sliced into strips.

## Motion

Intro: olive bar then the render (~1 s). Wheel (Lenis): the render pans; the giant name assembles from horizontal strips; the portrait rises; small photos drift; rooms scale to full bleed; the name returns in the footer.

Measured (`motion/probe.json`): GSAP 3.12.2/3.11.4; 12 ScrollTriggers; Lenis; 1 video; split text; smoothed scroll (median 154 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: an interior design studio on warm beige: full-bleed 3D interior renders (a mountain-mural bedroom, an arched bathroom), 'TA DESIGN' in a huge thin serif cut by horizontal strips, a portrait, 'Waar jouw plekje jouw verhaal vertelt', small interiors drifting around service statements, full-bleed rooms with a quote, project cards, testimonials, blog and a form above a repeated giant name. Type: Pangaia, Inter 24 Pt.
Ground and ink from the measured palette (#4E5647, #E1D2BE, #A09788). Motion carries the page through
'TA DESIGN' in a huge thin serif sliced into strips. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior 3D renders, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior 3D renders, portrait

## Reference lock

Primary reference/direction: TA Design - Interior design — An interior design studio on warm beige: full-bleed 3D interior renders (a mountain-mural bedroom, an arched bathroom), 'TA DESIGN' in a huge thin serif cut by horizontal strips, a portrait, 'Waar jouw plekje jouw verhaal vertelt', small interiors drifting around service statements, full-bleed rooms with a quote, project cards, testimonials, blog and a form above a repeated giant name.
Preserve (3-5 traits): full-bleed interior renders; huge thin serif name sliced in strips; warm beige and olive; small photos drifting around statements; quote over a room.
Borrow only (1-2): Slice the giant name into horizontal strips as it reveals
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior 3D renders, portrait
Reject: Thin serif small text
Token commitments: palette #4E5647, #E1D2BE, #A09788; type Pangaia, Inter 24 Pt; engine GSAP + Lenis linked (never vendored).
