---
title: "WarholArts - Webflow showcase"
url: https://warhol-arts.webflow.io/
source_url: https://warhol-arts.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: pop-art-exhibition-scroll
dna: "Warhol exhibition concept x pop-art objects and a gallery of icons"
register: other
grammar: chaptered editorial
lane: "An exhibition concept on black: a loading percent, 'WARHOL' huge with an italic 'Andy' and a paint tube, Elvis silkscreens sliding as a filmstrip, a quote with a banana field and Rolling Stones lips, 'Vivid colors' over Marilyn, 'Icon reborn' with an Apple Macintosh opening, Campbell's soup, 'Unlock the experience' with tickets flying, a wall of Warhol portraits and an orange footer with the cow."
mode: experience
traits: ["pop-art objects as section props", "silkscreen filmstrip", "banana wallpaper field", "tickets flying", "portrait wall", "italic script with condensed caps"]
palette: ["#050505", "#5C566C", "#827F8D", "#CBBAB5", "#4B2E32"]
type: ["Mangogrotesque", "Tomato Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each chapter uses an actual Warhol icon as its prop, so the scroll is a walk through the oeuvre.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Give each chapter one iconic prop from the subject

## What to leave

- Webflow badge over frames

## Signature move

A field of bananas with the Rolling Stones lips floating over it.

## Motion

Intro: black with a percent counter (~2 s). Wheel (201 triggers): the title pins and the filmstrip slides; quote words fill; bananas fill the screen in rows; Marilyn scales; the Macintosh opens; tickets fly; the portrait wall tilts; the orange wave rises.

Measured (`motion/probe.json`): GSAP 3.15.0; 201 ScrollTriggers; Lenis; WebGL canvas x3 (three.js); 7 video; split text; smoothed scroll (median 102 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: an exhibition concept on black: a loading percent, 'WARHOL' huge with an italic 'Andy' and a paint tube, Elvis silkscreens sliding as a filmstrip, a quote with a banana field and Rolling Stones lips, 'Vivid colors' over Marilyn, 'Icon reborn' with an Apple Macintosh opening, Campbell's soup, 'Unlock the experience' with tickets flying, a wall of Warhol portraits and an orange footer with the cow. Type: Mangogrotesque, Tomato Grotesk.
Ground and ink from the measured palette (#050505, #5C566C, #827F8D). Motion carries the page through
a field of bananas with the Rolling Stones lips floating over it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — Warhol artworks

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: Warhol artworks

## Reference lock

Primary reference/direction: WarholArts - Webflow showcase — An exhibition concept on black: a loading percent, 'WARHOL' huge with an italic 'Andy' and a paint tube, Elvis silkscreens sliding as a filmstrip, a quote with a banana field and Rolling Stones lips, 'Vivid colors' over Marilyn, 'Icon reborn' with an Apple Macintosh opening, Campbell's soup, 'Unlock the experience' with tickets flying, a wall of Warhol portraits and an orange footer with the cow.
Preserve (3-5 traits): pop-art objects as section props; silkscreen filmstrip; banana wallpaper field; tickets flying; portrait wall.
Borrow only (1-2): Give each chapter one iconic prop from the subject
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: Warhol artworks
Reject: Webflow badge over frames
Token commitments: palette #050505, #5C566C, #827F8D, #CBBAB5, #4B2E32; type Mangogrotesque, Tomato Grotesk; engine GSAP + Lenis linked (never vendored).
