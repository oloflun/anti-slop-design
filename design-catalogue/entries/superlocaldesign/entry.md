---
title: "Superlocal - design festival (Uruguay)"
url: https://superlocaldesign.com/
source_url: https://superlocaldesign.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: gradient-festival-dot-type
dna: "Design festival x grey-to-orange gradient, a dotted bitmap display face, circle photo bubbles and a coin with a face"
register: other
grammar: chaptered editorial
lane: "A design festival: a grey-orange gradient with the name in a dotted bitmap face, photo bubbles of past talks floating, a magenta-orange gradient orb, 'Las mejores ideas están hechas para circular' in dotted type over a talk photo, a gold coin with a speaker's face spinning in the centre while the line-up names list on either side, then a programme where each day is a coloured band with the date in large figures and the weekday in dotted type, workshop cards, sponsor circles and ticket packs."
mode: persuade
traits: ["dotted bitmap display face", "circular photo bubbles", "coin with a face (circulation)", "coloured day bands", "gradient orb"]
palette: ["#BDBDBD", "#0B0707", "#DB7038", "#271E1A", "#DC9471", "#734338"]
type: ["fontSans", "fontDisplay", "PlataPin_1_0", "PlataPin_50_700"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The coin with a face turns the slogan (ideas made to circulate) into one object at the heart of the line-up.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: hellohello).

## What to borrow (principle)

- Make the tagline's metaphor the centre object

## What to leave

- Small card text

## Signature move

A spinning gold coin with a speaker's face between two columns of names.

## Motion

Wheel (Lenis): bubbles drift; the orb pulses; the coin rotates; day bands slide over each other.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x2 (three.js); split text; smoothed scroll (median 132 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a design festival: a grey-orange gradient with the name in a dotted bitmap face, photo bubbles of past talks floating, a magenta-orange gradient orb, 'Las mejores ideas están hechas para circular' in dotted type over a talk photo, a gold coin with a speaker's face spinning in the centre while the line-up names list on either side, then a programme where each day is a coloured band with the date in large figures and the weekday in dotted type, workshop cards, sponsor circles and ticket packs. Type: fontSans, fontDisplay, PlataPin_1_0, PlataPin_50_700.
Ground and ink from the measured palette (#BDBDBD, #0B0707, #DB7038). Motion carries the page through
a spinning gold coin with a speaker's face between two columns of names. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — event photography, 3D coin

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: event photography, 3D coin

## Reference lock

Primary reference/direction: Superlocal - design festival (Uruguay) — A design festival: a grey-orange gradient with the name in a dotted bitmap face, photo bubbles of past talks floating, a magenta-orange gradient orb, 'Las mejores ideas están hechas para circular' in dotted type over a talk photo, a gold coin with a speaker's face spinning in the centre while the line-up names list on either side, then a programme where each day is a coloured band with the date in large figures and the weekday in dotted type, workshop cards, sponsor circles and ticket packs.
Preserve (3-5 traits): dotted bitmap display face; circular photo bubbles; coin with a face (circulation); coloured day bands; gradient orb.
Borrow only (1-2): Make the tagline's metaphor the centre object
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: event photography, 3D coin
Reject: Small card text
Token commitments: palette #BDBDBD, #0B0707, #DB7038, #271E1A, #DC9471, #734338; type fontSans, fontDisplay, PlataPin_1_0, PlataPin_50_700; engine GSAP + Lenis linked (never vendored).
