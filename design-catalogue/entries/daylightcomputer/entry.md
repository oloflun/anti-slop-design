---
title: "Daylight Computer - DC-1"
url: https://daylightcomputer.com/
source_url: https://daylightcomputer.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: sunlit-paper-tablet
dna: "Calm tablet x sunlit shadows across white, a paper-like tablet in grass and sand, an amber glow chapter for night"
register: warm photographic
grammar: chaptered editorial
lane: "A paper-display tablet: 'The computer, de-invented' over the tablet lying in grass with a botanical drawing on screen, a video of the tablet in sand, a manifesto on white with leaf shadows moving across it ('We refuse to accept a future where our devices are exhausting, addictive and distracting', the last word in red), 'Introducing Daylight', the paper-like display with a pen, use-case photos (reading, notes, writing), app icons, an outdoor portrait ('it's a computer you can use outside'), then the ground turning to warm orange with window shadows ('When the lights go off, enjoy the amber glow'), the tablet glowing amber in hands on black, 'Goodbye, blue light', reviews and a public-benefit close."
mode: persuade
traits: ["moving leaf and window shadows on white", "tablet in natural settings", "manifesto with one red word", "day-to-amber-night ground change", "serif italics in headings"]
palette: ["#E5E3E2", "#1B1912", "#CBC9C7", "#797266", "#FAF7F6", "#403223"]
type: ["__abcRoomFont_38b1ae", "__abcRoomExtendedFont_412c3c", "__abcArizonaFlareFont_498f8e"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Shadows of leaves and windows on the page itself make the product's promise (a screen that lives in daylight) part of the reading surface.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Basement Studio).

## What to borrow (principle)

- Cast real light and shadow across the page ground
- Change the ground's light from day to evening as the story turns

## What to leave

- Newsletter popup on every frame

## Signature move

Leaf shadows drifting across a white manifesto page.

## Motion

Wheel (Lenis, smoothed): shadow video overlays drift; words fade in; the ground warms to amber; the tablet glows; cards rise.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; WebGL canvas x1; 2 video; smoothed scroll (median 64 px still travelling after input stops); entry gate: Play video. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a paper-display tablet: 'The computer, de-invented' over the tablet lying in grass with a botanical drawing on screen, a video of the tablet in sand, a manifesto on white with leaf shadows moving across it ('We refuse to accept a future where our devices are exhausting, addictive and distracting', the last word in red), 'Introducing Daylight', the paper-like display with a pen, use-case photos (reading, notes, writing), app icons, an outdoor portrait ('it's a computer you can use outside'), then the ground turning to warm orange with window shadows ('When the lights go off, enjoy the amber glow'), the tablet glowing amber in hands on black, 'Goodbye, blue light', reviews and a public-benefit close. Type: __abcRoomFont_38b1ae, __abcRoomExtendedFont_412c3c, __abcArizonaFlareFont_498f8e.
Ground and ink from the measured palette (#E5E3E2, #1B1912, #CBC9C7). Motion carries the page through
leaf shadows drifting across a white manifesto page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lifestyle photography, shadow video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lifestyle photography, shadow video

## Reference lock

Primary reference/direction: Daylight Computer - DC-1 — A paper-display tablet: 'The computer, de-invented' over the tablet lying in grass with a botanical drawing on screen, a video of the tablet in sand, a manifesto on white with leaf shadows moving across it ('We refuse to accept a future where our devices are exhausting, addictive and distracting', the last word in red), 'Introducing Daylight', the paper-like display with a pen, use-case photos (reading, notes, writing), app icons, an outdoor portrait ('it's a computer you can use outside'), then the ground turning to warm orange with window shadows ('When the lights go off, enjoy the amber glow'), the tablet glowing amber in hands on black, 'Goodbye, blue light', reviews and a public-benefit close.
Preserve (3-5 traits): moving leaf and window shadows on white; tablet in natural settings; manifesto with one red word; day-to-amber-night ground change; serif italics in headings.
Borrow only (1-2): Cast real light and shadow across the page ground; Change the ground's light from day to evening as the story turns
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lifestyle photography, shadow video
Reject: Newsletter popup on every frame
Token commitments: palette #E5E3E2, #1B1912, #CBC9C7, #797266, #FAF7F6, #403223; type __abcRoomFont_38b1ae, __abcRoomExtendedFont_412c3c, __abcArizonaFlareFont_498f8e; engine GSAP + Lenis linked (never vendored).
