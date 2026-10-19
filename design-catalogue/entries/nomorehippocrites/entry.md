---
title: "Hippocrites - Interactive short film"
url: https://www.nomorehippocrites.com/
source_url: https://www.nomorehippocrites.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: ""
family: interactive-film-title-reel
dna: "Interactive short film on reproductive health x a hot pink title over the film"
register: cinematic dark
grammar: filmic one-shot
lane: "An interactive film's landing: festival laurels, 'a broken oath in reproductive health' and a huge hot pink condensed 'HIPPOCRITES' fixed over the film's footage (a phone message, a bedroom, doctors in white coats, the Hippocratic oath text) with watch and trailer buttons."
mode: experience
traits: ["hot pink condensed title", "footage cycling behind", "festival laurels", "blackletter tagline", "watch / trailer buttons", "no scroll content"]
palette: ["#2D1F19", "#0C070C", "#EE0686", "#634F3B", "#49342E", "#716654"]
type: ["California Palms Serif"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

One loud title over the film's key images sets the tone and subject in seconds.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fix the title and let the film's key shots cycle behind it

## What to leave

- Nothing beyond the hero

## Signature move

A hot pink 'HIPPOCRITES' over doctors in white coats.

## Motion

Intro: black, the title appears over the first shot. Scroll: none; the footage cycles behind the fixed title.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; 2 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: an interactive film's landing: festival laurels, 'a broken oath in reproductive health' and a huge hot pink condensed 'HIPPOCRITES' fixed over the film's footage (a phone message, a bedroom, doctors in white coats, the Hippocratic oath text) with watch and trailer buttons. Type: California Palms Serif.
Ground and ink from the measured palette (#2D1F19, #0C070C, #EE0686). Motion carries the page through
a hot pink 'HIPPOCRITES' over doctors in white coats. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills

## Reference lock

Primary reference/direction: Hippocrites - Interactive short film — An interactive film's landing: festival laurels, 'a broken oath in reproductive health' and a huge hot pink condensed 'HIPPOCRITES' fixed over the film's footage (a phone message, a bedroom, doctors in white coats, the Hippocratic oath text) with watch and trailer buttons.
Preserve (3-5 traits): hot pink condensed title; footage cycling behind; festival laurels; blackletter tagline; watch / trailer buttons.
Borrow only (1-2): Fix the title and let the film's key shots cycle behind it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills
Reject: Nothing beyond the hero
Token commitments: palette #2D1F19, #0C070C, #EE0686, #634F3B, #49342E, #716654; type California Palms Serif; engine GSAP + Lenis linked (never vendored).
