---
title: "Cip Harvin"
url: https://cipharvin.ro/en
source_url: https://cipharvin.ro/en
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: black-red-freight-headline
dna: "Romanian freight haulier x giant red marquee words"
register: cinematic dark
grammar: chaptered editorial
lane: "A freight company page in black, white and signal red where giant red words ('Capacity', 'Certified', '25 years', 'Direct') slide across the frame behind monochrome truck photographs as each claim is made."
mode: persuade
traits: ["monochrome truck photography", "giant red words sliding across sections", "red closing section", "pill nav bar at the bottom", "dark/white split blocks", "logo bubbles for testimonials"]
palette: ["#000000", "#FFFFFF", "#2C2426", "#5E595B", "#E1DDDD"]
type: ["Satoshi"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A plain B2B business (transport) gets one big, legible gesture: each proof point has a single giant red word that travels horizontally across the frame behind the photo while the short claim sits small beside it. The photos are monochrome, so the red word is the only colour until the final red section.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Adrian Dascal).

## What to borrow (principle)

- One giant word per claim, scrubbed horizontally behind the image, as the section's headline
- Monochrome photography so a single signal colour carries the whole page
- Bottom-docked pill nav so the frame above stays clean

## What to leave

- The giant words are cut at both edges most of the time and read as fragments
- Sections are similar in rhythm; the scroll gets repetitive

## Signature move

Giant red claim words sliding across the frame behind black-and-white truck photography.

## Motion

Intro: a small loader dash on pale, then the dark hero with a truck and 'Safe. Fast. Reliable.' revealing word by word with red dots (~2 s). Scroll (Lenis, ~125 px glide, 20 ScrollTriggers, SplitText): sections split black/white with images rising; 'Capacity', 'Certified', '25 years', 'Direct', 'Consistent' slide horizontally (scrubbed) across the frame behind the photos; testimonials in white pills on red; closing red section with a tunnel photo and Contact.

Measured (`motion/probe.json`): GSAP 3.15.0; 20 ScrollTriggers; Lenis; smoothed scroll (median 132 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a freight company page in black, white and signal red where giant red words ('Capacity', 'Certified', '25 years', 'Direct') slide across the frame behind monochrome truck photographs as each claim is made. Type: Satoshi.
Ground and ink from the measured palette (#000000, #FFFFFF, #2C2426). Motion carries the page through
giant red claim words sliding across the frame behind black-and-white truck photography. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — black-and-white industrial photography of trucks, depots, light tunnels

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: black-and-white industrial photography of trucks, depots, light tunnels

## Reference lock

Primary reference/direction: Cip Harvin — A freight company page in black, white and signal red where giant red words ('Capacity', 'Certified', '25 years', 'Direct') slide across the frame behind monochrome truck photographs as each claim is made.
Preserve (3-5 traits): monochrome truck photography; giant red words sliding across sections; red closing section; pill nav bar at the bottom; dark/white split blocks.
Borrow only (1-2): One giant word per claim, scrubbed horizontally behind the image, as the section's headline; Monochrome photography so a single signal colour carries the whole page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: black-and-white industrial photography of trucks, depots, light tunnels
Reject: The giant words are cut at both edges most of the time and read as fragments; Sections are similar in rhythm; the scroll gets repetitive
Token commitments: palette #000000, #FFFFFF, #2C2426, #5E595B, #E1DDDD; type Satoshi; engine GSAP + Lenis linked (never vendored).
