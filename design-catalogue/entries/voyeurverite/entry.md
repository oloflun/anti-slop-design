---
title: "Voyeur Vérité"
url: https://www.voyeurverite.com/
source_url: https://www.voyeurverite.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: red-documentary-reel
dna: "Documentary film company x red title cards and serif credits"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A documentary company that opens on a red frame where a tilted red-tinted film still slides in under 'THE ART OF OBSERVATION', then lays each film out as a serif title card with credits followed by a collage of stills that grows into full-frame footage."
mode: persuade
traits: ["red title frames", "tilted image card entrance", "heavy wide caps over film", "serif film titles in red (The Symphony of Dance)", "credits table in small serif", "still collage that grows to full frame"]
palette: ["#F5F2EC", "#40342C", "#030403", "#A79D93"]
type: ["Review", "Feature Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page borrows the order of a film: title card, credits, then footage. Each project gets a red serif title and a credits block like an opening sequence, then its stills arrange into a collage that opens up into a single full-frame shot.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: BL/S).

## What to borrow (principle)

- Structure a project like a film opening: title card, credits, then footage
- Enter the hero image as a tilted card sliding onto a red frame
- Grow a still collage into one full-frame shot

## What to leave

- ENTER gate
- Body copy very small

## Signature move

A tilted red-tinted film still sliding onto a red frame under 'THE ART OF OBSERVATION'.

## Motion

Intro: red frame with a short line, a tilted card slides in and straightens (~1.5 s), then 'THE ART OF OBSERVATION' sets over the red still. Scroll (ScrollSmoother, 50 ScrollTriggers, SplitText): dance still full-bleed; cream section with 'The Symphony of Dance' serif title and credits columns; poster and stills collage; hospital-room stills grow; blurred close-ups; final dancer shot full frame.

Measured (`motion/probe.json`): GSAP 3.15.0; 50 ScrollTriggers; ScrollSmoother; split text; entry gate: EXPLORE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a documentary company that opens on a red frame where a tilted red-tinted film still slides in under 'THE ART OF OBSERVATION', then lays each film out as a serif title card with credits followed by a collage of stills that grows into full-frame footage. Type: Review, Feature Display.
Ground and ink from the measured palette (#F5F2EC, #40342C, #030403). Motion carries the page through
a tilted red-tinted film still sliding onto a red frame under 'THE ART OF OBSERVATION'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — observational documentary stills, natural light, red grade for titles

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: observational documentary stills, natural light, red grade for titles

## Reference lock

Primary reference/direction: Voyeur Vérité — A documentary company that opens on a red frame where a tilted red-tinted film still slides in under 'THE ART OF OBSERVATION', then lays each film out as a serif title card with credits followed by a collage of stills that grows into full-frame footage.
Preserve (3-5 traits): red title frames; tilted image card entrance; heavy wide caps over film; serif film titles in red (The Symphony of Dance); credits table in small serif.
Borrow only (1-2): Structure a project like a film opening: title card, credits, then footage; Enter the hero image as a tilted card sliding onto a red frame
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: observational documentary stills, natural light, red grade for titles
Reject: ENTER gate; Body copy very small
Token commitments: palette #F5F2EC, #40342C, #030403, #A79D93; type Review, Feature Display; engine GSAP + Lenis linked (never vendored).
