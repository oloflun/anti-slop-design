---
title: "Amelie Guider - Webflow Partner"
url: https://amelieguider.webflow.io/
source_url: https://amelieguider.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pill-tags-work-cards-folio
dna: "Webflow developer x falling pill tags and project cards sliding over a giant WORK"
register: modern clean
grammar: chaptered editorial
lane: "A Webflow developer: 'Where great design meets flawless code' with coloured pills peeking from the right edge, the pills falling and scrambling into tool names (GSAP, Finsweet, Custom code), a portrait card, a giant 'WORK' with tilted coloured project cards sliding across it, testimonials as full-colour numbered panels and a contact form."
mode: persuade
traits: ["colourful pill tags", "text scramble into tool names", "giant WORK word", "tilted colour project cards", "numbered testimonial panels", "wide geometric type"]
palette: ["#FFFFFF", "#1F1022", "#72615B", "#A8A5A7", "#44403E"]
type: ["Neuemetana", "Mulish"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The pills and the colour cards share one palette, so the page moves from tools to work with the same coloured shapes.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Reuse the same coloured shapes from skills to projects

## What to leave

- Testimonials repeat
- Generic form

## Signature move

Tilted coloured project cards sliding across a giant 'WORK'.

## Motion

Intro: white with 'W' (~1 s), headline types in, pills peek from the edge. Wheel (Barba, 35 triggers): pills fall into a stack and scramble into tool names; the portrait card scales; the WORK word pins as cards slide over it at angles; testimonial panels stack in colours.

Measured (`motion/probe.json`): GSAP 3.12.5; 35 ScrollTriggers; Barba page transitions; 12 video; split text. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a Webflow developer: 'Where great design meets flawless code' with coloured pills peeking from the right edge, the pills falling and scrambling into tool names (GSAP, Finsweet, Custom code), a portrait card, a giant 'WORK' with tilted coloured project cards sliding across it, testimonials as full-colour numbered panels and a contact form. Type: Neuemetana, Mulish.
Ground and ink from the measured palette (#FFFFFF, #1F1022, #72615B). Motion carries the page through
tilted coloured project cards sliding across a giant 'WORK'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait, project cards

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait, project cards

## Reference lock

Primary reference/direction: Amelie Guider - Webflow Partner — A Webflow developer: 'Where great design meets flawless code' with coloured pills peeking from the right edge, the pills falling and scrambling into tool names (GSAP, Finsweet, Custom code), a portrait card, a giant 'WORK' with tilted coloured project cards sliding across it, testimonials as full-colour numbered panels and a contact form.
Preserve (3-5 traits): colourful pill tags; text scramble into tool names; giant WORK word; tilted colour project cards; numbered testimonial panels.
Borrow only (1-2): Reuse the same coloured shapes from skills to projects
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait, project cards
Reject: Testimonials repeat; Generic form
Token commitments: palette #FFFFFF, #1F1022, #72615B, #A8A5A7, #44403E; type Neuemetana, Mulish; engine GSAP + Lenis linked (never vendored).
