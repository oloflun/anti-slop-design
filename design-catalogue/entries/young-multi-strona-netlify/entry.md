---
title: "Young Multi - Official Website"
url: https://young-multi-strona.netlify.app/
source_url: https://young-multi-strona.netlify.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: rapper-chrome-album-site
dna: "Polish rapper x chrome headline and tilted album cards"
register: cinematic dark
grammar: chaptered editorial
lane: "A rapper's site: percent loader on the logo, a chrome 'GDZIE MOJ DOM' headline over a video player with streaming links, a white discography where album cards tilt in 3D and stack, a black circle reveal into an 'O MNIE' outline title over an illustrated portrait, a smoke wipe to white merch and a black contact block."
mode: persuade
traits: ["chrome metallic headline", "3D tilted album cards stacking", "circle reveal to black", "smoke wipe between sections", "outline display type", "merch grid on white"]
palette: ["#000000", "#FFFFFF", "#C0C8C5", "#434343"]
type: ["Anton", "Antonio", "Bernoru"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Every section change has a different physical cause (a card stack, a black circle, a smoke cloud), so the page alternates black and white without ever just cutting.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Different wipe per section: circle, smoke, stack
- Album cards as tilted 3D objects that stack

## What to leave

- Empty white frames while assets load
- Small streaming links

## Signature move

Tilted album cards and a smoke wipe between black and white chapters.

## Motion

Intro: black, logo fills with a percent counter (~2 s). Wheel (Lenis ~150 px glide): the chrome headline lifts as the video and streaming links slide in; the page flips to white with tilted album cards stacking one by one; a black circle grows from a card into the 'O MNIE' section; smoke billows across to white merch; the contact block arrives on black.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 1 video; smoothed scroll (median 141 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a rapper's site: percent loader on the logo, a chrome 'GDZIE MOJ DOM' headline over a video player with streaming links, a white discography where album cards tilt in 3D and stack, a black circle reveal into an 'O MNIE' outline title over an illustrated portrait, a smoke wipe to white merch and a black contact block. Type: Anton, Antonio, Bernoru.
Ground and ink from the measured palette (#000000, #FFFFFF, #C0C8C5). Motion carries the page through
tilted album cards and a smoke wipe between black and white chapters. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — music video stills, album art, line illustration, merch photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: music video stills, album art, line illustration, merch photos

## Reference lock

Primary reference/direction: Young Multi - Official Website — A rapper's site: percent loader on the logo, a chrome 'GDZIE MOJ DOM' headline over a video player with streaming links, a white discography where album cards tilt in 3D and stack, a black circle reveal into an 'O MNIE' outline title over an illustrated portrait, a smoke wipe to white merch and a black contact block.
Preserve (3-5 traits): chrome metallic headline; 3D tilted album cards stacking; circle reveal to black; smoke wipe between sections; outline display type.
Borrow only (1-2): Different wipe per section: circle, smoke, stack; Album cards as tilted 3D objects that stack
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: music video stills, album art, line illustration, merch photos
Reject: Empty white frames while assets load; Small streaming links
Token commitments: palette #000000, #FFFFFF, #C0C8C5, #434343; type Anton, Antonio, Bernoru; engine GSAP + Lenis linked (never vendored).
