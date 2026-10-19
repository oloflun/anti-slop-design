---
title: "a-lign studio"
url: https://a-lign.studio/
source_url: https://a-lign.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: dashed-frame-coral-studio
dna: "Web studio x dashed-frame collage and coral slatted type"
register: modern clean
grammar: chaptered editorial
lane: "A pale studio page where everything sits in dashed frames like a moodboard, a quote spreads its words across the width as you scroll, and coral slatted display words (Work, Process, About) build out of horizontal bars."
mode: persuade
traits: ["dashed-outline frames around every image", "coral slatted/striped display type", "quote words spread across the width", "rotated vertical section word", "bar-graph block transition", "pixel heart close"]
palette: ["#F7F7F7", "#4C1B1D", "#C5C1BD", "#9F8882"]
type: ["Geist Medium", "Geist Regular", "Geist Semi Bold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The studio's name (align) is the system: everything sits in dashed frames that look like layout guides, and big section words are drawn from horizontal coral bars, as if typed by a plotter. A quote spreads apart word by word across the width on scroll, making justification itself the animation.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Show layout guides (dashed frames) as the visual language of a design studio
- Build display words out of horizontal bars that slide in
- Spread a quote's words across the width as the reader scrolls (justification as motion)

## What to leave

- Ghosted grey text before activation is hard to read
- Many small framed images compete

## Signature move

Section words built from sliding coral bars, like a plotter drawing type.

## Motion

Intro: 'LOADING 99%' corners, a huge outlined '<a-lign>' ghosted, then the hero card zooms from a dark frame to full screen (~1.5 s). Scroll (Lenis, 13 ScrollTriggers, Barba, Flip, Draggable/Inertia, ScrambleText): framed photos drift; quote words separate across the width; 'Work' in coral bars with framed cases; vertical 'Process' word with Strategy/Design/Build cards; three coral bars grow as a transition; 'Craft / Honesty / Partnership' with photos tucked between words; coral 'About' bars; testimonial cards; pixel heart.

Measured (`motion/probe.json`): GSAP 3.15.0; 13 ScrollTriggers; Lenis; Barba page transitions; 4 video; smoothed scroll (median 183 px still travelling after input stops); entry gate: SKIP TO MAIN CONTENT. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a pale studio page where everything sits in dashed frames like a moodboard, a quote spreads its words across the width as you scroll, and coral slatted display words (Work, Process, About) build out of horizontal bars. Type: Geist Medium, Geist Regular, Geist Semi Bold.
Ground and ink from the measured palette (#F7F7F7, #4C1B1D, #C5C1BD). Motion carries the page through
section words built from sliding coral bars, like a plotter drawing type. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — editorial studio portraits and product stills, neutral grey with one coral

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: editorial studio portraits and product stills, neutral grey with one coral

## Reference lock

Primary reference/direction: a-lign studio — A pale studio page where everything sits in dashed frames like a moodboard, a quote spreads its words across the width as you scroll, and coral slatted display words (Work, Process, About) build out of horizontal bars.
Preserve (3-5 traits): dashed-outline frames around every image; coral slatted/striped display type; quote words spread across the width; rotated vertical section word; bar-graph block transition.
Borrow only (1-2): Show layout guides (dashed frames) as the visual language of a design studio; Build display words out of horizontal bars that slide in
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: editorial studio portraits and product stills, neutral grey with one coral
Reject: Ghosted grey text before activation is hard to read; Many small framed images compete
Token commitments: palette #F7F7F7, #4C1B1D, #C5C1BD, #9F8882; type Geist Medium, Geist Regular, Geist Semi Bold; engine GSAP + Lenis linked (never vendored).
