---
title: "The Symphony - Webflow Community Challenge"
url: https://the-symphony.webflow.io/
source_url: https://the-symphony.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: timeline-composer-story
dna: "Webflow challenge entry x a video-editor timeline that becomes piano keys"
register: cinematic dark
grammar: chaptered editorial
lane: "A storytelling site about AI and the web: 'The future of the web is being composed' with an 'Allow sound?' choice, then a timeline panel at the bottom fills with coloured clips like a video editor, the clips turn into piano keys ('We don't start with complexity'), letters float in 'From silence to motion', 'Before AI, web was handwritten', and 'You prompt. You shape.' ends with a composer panel of five coloured keys."
mode: experience
traits: ["editor timeline with coloured clips", "clips turning into piano keys", "italic blue serif accents", "letters floating into words", "sound choice", "five-colour key palette"]
palette: ["#171717", "#2D2E2F", "#8B95A2", "#3E4E64"]
type: ["Geist", "Instrumentserif", "Robotomono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The editor timeline is the signature object: it fills as you scroll, becomes an instrument and ends as the product, so the metaphor (composing the web) is carried by one interface.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Make the scroll fill a timeline UI that later becomes the product

## What to leave

- Very dim intro frames
- Small instructions

## Signature move

A video-editor timeline whose clips turn into piano keys.

## Motion

Intro: the headline with an 'Allow sound?' choice (no clicked). Wheel (25 triggers): the hero dims and the timeline panel slides up; clips drop onto tracks one by one; the panel zooms into piano keys that slide in from the right; letters drift into place; blurred words sharpen in turn; the coloured keys line up in the composer.

Measured (`motion/probe.json`): GSAP 3.15.0; 25 ScrollTriggers; split text; entry gate: no. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a storytelling site about AI and the web: 'The future of the web is being composed' with an 'Allow sound?' choice, then a timeline panel at the bottom fills with coloured clips like a video editor, the clips turn into piano keys ('We don't start with complexity'), letters float in 'From silence to motion', 'Before AI, web was handwritten', and 'You prompt. You shape.' ends with a composer panel of five coloured keys. Type: Geist, Instrumentserif, Robotomono.
Ground and ink from the measured palette (#171717, #2D2E2F, #8B95A2). Motion carries the page through
a video-editor timeline whose clips turn into piano keys. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — UI illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: UI illustration

## Reference lock

Primary reference/direction: The Symphony - Webflow Community Challenge — A storytelling site about AI and the web: 'The future of the web is being composed' with an 'Allow sound?' choice, then a timeline panel at the bottom fills with coloured clips like a video editor, the clips turn into piano keys ('We don't start with complexity'), letters float in 'From silence to motion', 'Before AI, web was handwritten', and 'You prompt. You shape.' ends with a composer panel of five coloured keys.
Preserve (3-5 traits): editor timeline with coloured clips; clips turning into piano keys; italic blue serif accents; letters floating into words; sound choice.
Borrow only (1-2): Make the scroll fill a timeline UI that later becomes the product
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: UI illustration
Reject: Very dim intro frames; Small instructions
Token commitments: palette #171717, #2D2E2F, #8B95A2, #3E4E64; type Geist, Instrumentserif, Robotomono; engine GSAP + Lenis linked (never vendored).
