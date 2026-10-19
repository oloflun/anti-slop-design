---
title: "Design by Dylan - Digital Designer and Webflow Developer"
url: https://dylanbrouwer.design/
source_url: https://dylanbrouwer.design/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: monitor-stage-designer-folio
dna: "Webflow designer x a desktop monitor that plays the work under a giant headline"
register: modern clean
grammar: chaptered editorial
lane: "A designer folio on grey: 'SITES THAT MOVE' in huge condensed type with a monitor in front of it that cycles through client sites, the monitor drops away into an intro paragraph and portrait, project mockups slide in on laptops and screens, a white featured case card, a client logo strip, Define/Design/Develop service cards and a giant 'Design by Dylan' footer with a hanging 3D tag."
mode: persuade
traits: ["monitor in front of a giant headline", "screens cycling through client sites", "grey gradient stage", "laptops and devices as project frames", "service cards with chrome icons", "hanging 3D tag in the footer"]
palette: ["#161616", "#E0DAE3", "#C3B1A9"]
type: ["ABC Gravity Variable", "Die Grotesk B", "IBM Plex Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The monitor is the signature object: it stands in the hero playing the work, then becomes the device frames down the page, so the site literally shows sites that move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A device in the hero that plays the portfolio
- Let the hero object reappear as the frame for each case

## What to leave

- Grey-on-grey low contrast
- Small body copy

## Signature move

A monitor cycling client sites in front of a giant 'SITES THAT MOVE' headline.

## Motion

Intro: grey stage, the headline slides up in strips and the monitor rises in front (~2 s). Wheel (Lenis ~90 px glide, 15 triggers): the monitor keeps swapping screens, then tilts and drops as the intro text fills in; device mockups slide in from both sides at different speeds; the featured case card scales up; logos scroll; service cards stagger; the footer tag swings.

Measured (`motion/probe.json`): GSAP 3.15.0; 15 ScrollTriggers; Lenis; 7 video; split text; smoothed scroll (median 108 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a designer folio on grey: 'SITES THAT MOVE' in huge condensed type with a monitor in front of it that cycles through client sites, the monitor drops away into an intro paragraph and portrait, project mockups slide in on laptops and screens, a white featured case card, a client logo strip, Define/Design/Develop service cards and a giant 'Design by Dylan' footer with a hanging 3D tag. Type: ABC Gravity Variable, Die Grotesk B, IBM Plex Mono.
Ground and ink from the measured palette (#161616, #E0DAE3, #C3B1A9). Motion carries the page through
a monitor cycling client sites in front of a giant 'SITES THAT MOVE' headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device mockups, client site screenshots, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device mockups, client site screenshots, portrait

## Reference lock

Primary reference/direction: Design by Dylan - Digital Designer and Webflow Developer — A designer folio on grey: 'SITES THAT MOVE' in huge condensed type with a monitor in front of it that cycles through client sites, the monitor drops away into an intro paragraph and portrait, project mockups slide in on laptops and screens, a white featured case card, a client logo strip, Define/Design/Develop service cards and a giant 'Design by Dylan' footer with a hanging 3D tag.
Preserve (3-5 traits): monitor in front of a giant headline; screens cycling through client sites; grey gradient stage; laptops and devices as project frames; service cards with chrome icons.
Borrow only (1-2): A device in the hero that plays the portfolio; Let the hero object reappear as the frame for each case
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device mockups, client site screenshots, portrait
Reject: Grey-on-grey low contrast; Small body copy
Token commitments: palette #161616, #E0DAE3, #C3B1A9; type ABC Gravity Variable, Die Grotesk B, IBM Plex Mono; engine GSAP + Lenis linked (never vendored).
