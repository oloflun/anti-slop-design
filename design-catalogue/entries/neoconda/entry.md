---
title: "Neoconda - cyber security device"
url: https://neoconda.com/
source_url: https://neoconda.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: handheld-device-feature-screens
dna: "Security gadget x one handheld device whose screen carries every feature"
register: cinematic dark
grammar: chaptered editorial
lane: "A product page on black: a loading percent, 'Neoconda' in a wide grotesk that scrolls off, the device tilted in 3D, 'A powerful cyber device designed for reconnaissance, hacking, and security' beside the device showing a terminal, 'The most comprehensive feature set in its class' with the device centred and features listed around it as the screen changes (C2 framework, AI engine, defence mode with a red radar and streams of red glyphs flowing in), 'Precision in every component' as giant type with the device passing through, then an exploded view of the hardware with callouts."
mode: persuade
traits: ["one device as the stage", "screen content changing per feature", "red glyph streams", "giant type the device passes through", "exploded hardware view", "green status dot"]
palette: ["#060606", "#3A3E3B"]
type: ["Neuemachina", "Neuehaasunicaw 1 G", "Jetbrainsmono Variable", "Space Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Holding the device still and changing what is on its screen turns a feature list into a demo.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: SHIFTBRAIN).

## What to borrow (principle)

- Keep the product fixed and change its screen per feature
- End with the product exploded into its parts

## What to leave

- Tiny mono labels

## Signature move

A handheld device centred on black with red glyph streams flowing into its radar screen.

## Motion

Intro: black counter to 100 % (~2 s), the wordmark slides out. Wheel (Lenis, 140 triggers): the device rotates in; features swap on its screen; red streams flow in from the left; the device shrinks and passes through the giant line; the hardware explodes layer by layer with callouts.

Measured (`motion/probe.json`): GSAP 3.12.5/3.12.5/3.12.5; 140 ScrollTriggers; WebGL canvas x2 (three.js); 4 video; smoothed scroll (median 94 px still travelling after input stops); entry gate: REJECT ALL, EXPLORE NEOCONDA. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a product page on black: a loading percent, 'Neoconda' in a wide grotesk that scrolls off, the device tilted in 3D, 'A powerful cyber device designed for reconnaissance, hacking, and security' beside the device showing a terminal, 'The most comprehensive feature set in its class' with the device centred and features listed around it as the screen changes (C2 framework, AI engine, defence mode with a red radar and streams of red glyphs flowing in), 'Precision in every component' as giant type with the device passing through, then an exploded view of the hardware with callouts. Type: Neuemachina, Neuehaasunicaw 1 G, Jetbrainsmono Variable, Space Grotesk.
Ground and ink from the measured palette (#060606, #3A3E3B). Motion carries the page through
a handheld device centred on black with red glyph streams flowing into its radar screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product renders

## Reference lock

Primary reference/direction: Neoconda - cyber security device — A product page on black: a loading percent, 'Neoconda' in a wide grotesk that scrolls off, the device tilted in 3D, 'A powerful cyber device designed for reconnaissance, hacking, and security' beside the device showing a terminal, 'The most comprehensive feature set in its class' with the device centred and features listed around it as the screen changes (C2 framework, AI engine, defence mode with a red radar and streams of red glyphs flowing in), 'Precision in every component' as giant type with the device passing through, then an exploded view of the hardware with callouts.
Preserve (3-5 traits): one device as the stage; screen content changing per feature; red glyph streams; giant type the device passes through; exploded hardware view.
Borrow only (1-2): Keep the product fixed and change its screen per feature; End with the product exploded into its parts
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product renders
Reject: Tiny mono labels
Token commitments: palette #060606, #3A3E3B; type Neuemachina, Neuehaasunicaw 1 G, Jetbrainsmono Variable, Space Grotesk; engine GSAP + Lenis linked (never vendored).
