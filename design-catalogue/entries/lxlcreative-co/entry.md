---
title: "LxL Creative"
url: https://www.lxlcreative.co.uk/
source_url: https://www.lxlcreative.co.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: script-swash-entertainment-agency
dna: "Entertainment creative agency x hand-drawn orange swash"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark entertainment-agency page where an orange hand-drawn swash draws itself through the sections, services sit as a pinned stack of cards that flip one by one, and caps statements carry script-italic words."
mode: persuade
traits: ["orange DrawSVG swash line running through sections", "script italic words inside heavy caps", "pinned service card stack", "video BTS hero", "cream section with photo grid", "blue CTA card"]
palette: ["#27201E", "#5D5751", "#03080B", "#4C4038", "#B4A687"]
type: ["Owners Wide", "Scribo", "Manrope"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One drawn line ties the page together: an orange swash that draws itself on scroll, loops behind the service cards, and ends under the closing CTA. The type pairs a wide heavy caps face with a hand script for single words, so every statement has one handwritten accent that echoes the line.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Jordan Gilroy).

## What to borrow (principle)

- Let one SVG line draw through the whole page (DrawSVG scrubbed) as the thread between sections
- Pin services as a stack of cards where each scroll beat swaps the front card
- One script word inside a caps statement as the voice accent

## What to leave

- Statement text over busy video frames loses contrast
- Section-by-section colour changes (cream, blue) feel unrelated to the dark main ground

## Signature move

An orange hand-drawn swash that draws itself through every section.

## Motion

Intro: hero portrait and wordmark already placed, swash draws in. Scroll (Lenis, ~100–130 px glide, 25 ScrollTriggers, Barba): BTS video scales up into full bleed; a caps statement reveals line by line over the video; 'Our SERVICES' pins while key-art cards swap (Key Art, Social, EPK, Editorial, Activations) with the swash looping behind; about block with the line continuing; featured project full bleed; cream 'Why LxL' with photo grid, quote; blue studios card; closing CTA with the swash ending under it. Draggable/Inertia on a carousel.

Measured (`motion/probe.json`): GSAP 3.15.0; 25 ScrollTriggers; Lenis; Barba page transitions; 2 video; smoothed scroll (median 105 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark entertainment-agency page where an orange hand-drawn swash draws itself through the sections, services sit as a pinned stack of cards that flip one by one, and caps statements carry script-italic words. Type: Owners Wide, Scribo, Manrope.
Ground and ink from the measured palette (#27201E, #5D5751, #03080B). Motion carries the page through
an orange hand-drawn swash that draws itself through every section. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — entertainment key art and BTS, bold colour grading, faces

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: entertainment key art and BTS, bold colour grading, faces

## Reference lock

Primary reference/direction: LxL Creative — A dark entertainment-agency page where an orange hand-drawn swash draws itself through the sections, services sit as a pinned stack of cards that flip one by one, and caps statements carry script-italic words.
Preserve (3-5 traits): orange DrawSVG swash line running through sections; script italic words inside heavy caps; pinned service card stack; video BTS hero; cream section with photo grid.
Borrow only (1-2): Let one SVG line draw through the whole page (DrawSVG scrubbed) as the thread between sections; Pin services as a stack of cards where each scroll beat swaps the front card
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: entertainment key art and BTS, bold colour grading, faces
Reject: Statement text over busy video frames loses contrast; Section-by-section colour changes (cream, blue) feel unrelated to the dark main ground
Token commitments: palette #27201E, #5D5751, #03080B, #4C4038, #B4A687; type Owners Wide, Scribo, Manrope; engine GSAP + Lenis linked (never vendored).
