---
title: "GATZARA Studio - brand and digital"
url: https://gatzara.studio/
source_url: https://gatzara.studio/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: loud-colour-block-agency
dna: "Studio site x red, lime, blue and saffron blocks, circular rotating headline and condensed stencil-like display"
register: other
grammar: chaptered editorial
lane: "A loud studio: on red, 'Digital & brand design, bridging…' set on a circle that rotates around project screenshots, the studio's name explained in a paragraph, then a stack of colour cards (Cobra, Macmillan, Google, Buff) that slide over each other with a circle-cropped photo each, a grey services split into Digital and Brand lists, 'Work with us' as icon tiles on saffron, testimonials hung on a looping black scribble, and 'Selected clients' on red."
mode: persuade
traits: ["text on a rotating circle", "stacked colour cards sliding over each other", "circle-cropped photos", "condensed geometric display", "black scribble line", "primary colour blocks"]
palette: ["#FF1416", "#426EDB", "#0A0C0D", "#9DB294", "#EAFCB4", "#801313"]
type: ["Roko Bold", "Parafina Bold M", "Aeonik Fono Bold", "Aeonik Fono SemiBold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each case gets a whole colour, so a short project list reads as a run of posters rather than a grid of thumbnails.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: GATZARA).

## What to borrow (principle)

- Give each case its own full-bleed colour card stacked over the last

## What to leave

- Testimonials as the longest section

## Signature move

A headline set on a rotating circle around project screenshots, on red.

## Motion

Intro: the circle text spins in (~2 s). Wheel (Lenis, no GSAP): the ring rotates with scroll; cards stack with sticky offsets; the scribble draws; testimonial cards drift.

Measured (`motion/probe.json`): Lenis; 2 video; smoothed scroll (median 139 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a loud studio: on red, 'Digital & brand design, bridging…' set on a circle that rotates around project screenshots, the studio's name explained in a paragraph, then a stack of colour cards (Cobra, Macmillan, Google, Buff) that slide over each other with a circle-cropped photo each, a grey services split into Digital and Brand lists, 'Work with us' as icon tiles on saffron, testimonials hung on a looping black scribble, and 'Selected clients' on red. Type: Roko Bold, Parafina Bold M, Aeonik Fono Bold, Aeonik Fono SemiBold.
Ground and ink from the measured palette (#FF1416, #426EDB, #0A0C0D). Motion carries the page through
a headline set on a rotating circle around project screenshots, on red. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots, portrait photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots, portrait photography

## Reference lock

Primary reference/direction: GATZARA Studio - brand and digital — A loud studio: on red, 'Digital & brand design, bridging…' set on a circle that rotates around project screenshots, the studio's name explained in a paragraph, then a stack of colour cards (Cobra, Macmillan, Google, Buff) that slide over each other with a circle-cropped photo each, a grey services split into Digital and Brand lists, 'Work with us' as icon tiles on saffron, testimonials hung on a looping black scribble, and 'Selected clients' on red.
Preserve (3-5 traits): text on a rotating circle; stacked colour cards sliding over each other; circle-cropped photos; condensed geometric display; black scribble line.
Borrow only (1-2): Give each case its own full-bleed colour card stacked over the last
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots, portrait photography
Reject: Testimonials as the longest section
Token commitments: palette #FF1416, #426EDB, #0A0C0D, #9DB294, #EAFCB4, #801313; type Roko Bold, Parafina Bold M, Aeonik Fono Bold, Aeonik Fono SemiBold; engine GSAP + Lenis linked (never vendored).
