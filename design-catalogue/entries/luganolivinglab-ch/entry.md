---
title: "Lugano Living Lab - City of Lugano"
url: https://www.luganolivinglab.ch/
source_url: https://www.luganolivinglab.ch/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: city-lab-particle-map
dna: "City innovation lab x a particle map of the city and pixel shapes"
register: cinematic dark
grammar: chaptered editorial
lane: "A city's innovation lab: a counter with a gradient bar, the big 'Lugano Living Lab' title over a gold particle map of the city, a statement, stats (2030, 40+, 100+), a lilac-lime gradient event panel with pixel diamonds, 'Ascoltiamo / Sperimentiamo / Misuriamo / Diffondiamo' stepping, project cards and a partner logo grid."
mode: read
traits: ["gold particle city map", "verbs stacked as a manifesto", "lilac to lime gradient", "pixel diamond shapes", "counter loader with gradient bar", "logo grid"]
palette: ["#000000", "#A097AD", "#28262C", "#645F6D", "#BFBEA8"]
type: ["neue-haas-grotesk-display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The particle map grounds a civic tech lab in its actual city, and the four verbs give the mission a rhythm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: SPOTHEROZ).

## What to borrow (principle)

- A particle map of the place as the hero ground
- Stack the method as four verbs

## What to leave

- Small labels
- Generic logo grid

## Signature move

'Lugano Living Lab' over a gold particle map of the city.

## Motion

Intro: black, a counter 0 to 100 with a gradient bar (~2 s), the title fills. Wheel (Lenis ~135 px glide): the particle map drifts; the statement rises; stats count; the gradient panel slides with pixel diamonds shifting; verbs slide in one by one; cards and logos stagger.

Measured (`motion/probe.json`): GSAP 3.13.0; 10 ScrollTriggers; Lenis; 2 video; smoothed scroll (median 137 px still travelling after input stops); entry gate: RIFIUTA TUTTO, ×. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a city's innovation lab: a counter with a gradient bar, the big 'Lugano Living Lab' title over a gold particle map of the city, a statement, stats (2030, 40+, 100+), a lilac-lime gradient event panel with pixel diamonds, 'Ascoltiamo / Sperimentiamo / Misuriamo / Diffondiamo' stepping, project cards and a partner logo grid. Type: neue-haas-grotesk-display.
Ground and ink from the measured palette (#000000, #A097AD, #28262C). Motion carries the page through
'Lugano Living Lab' over a gold particle map of the city. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — particle map, project images

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: particle map, project images

## Reference lock

Primary reference/direction: Lugano Living Lab - City of Lugano — A city's innovation lab: a counter with a gradient bar, the big 'Lugano Living Lab' title over a gold particle map of the city, a statement, stats (2030, 40+, 100+), a lilac-lime gradient event panel with pixel diamonds, 'Ascoltiamo / Sperimentiamo / Misuriamo / Diffondiamo' stepping, project cards and a partner logo grid.
Preserve (3-5 traits): gold particle city map; verbs stacked as a manifesto; lilac to lime gradient; pixel diamond shapes; counter loader with gradient bar.
Borrow only (1-2): A particle map of the place as the hero ground; Stack the method as four verbs
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: particle map, project images
Reject: Small labels; Generic logo grid
Token commitments: palette #000000, #A097AD, #28262C, #645F6D, #BFBEA8; type neue-haas-grotesk-display; engine GSAP + Lenis linked (never vendored).
