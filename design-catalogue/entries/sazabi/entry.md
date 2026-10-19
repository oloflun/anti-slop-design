---
title: "Sazabi"
url: https://www.sazabi.com/
source_url: https://www.sazabi.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: red-mecha-observability
dna: "AI observability platform x red mecha game UI"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer tool styled like a mecha game: 'SAZABI IS INITIALIZING' in red, a night city with a hovering craft under 'OBSERVABILITY ON AUTOPILOT', a cockpit frame, red angled panels for features, hexagonal integration nodes and a red 'SAVE THE DAY' close."
mode: persuade
traits: ["red and black mecha/game UI", "angled cockpit frames", "condensed italic caps", "3D city and craft hero", "hexagon integration nodes", "sound toggle"]
palette: ["#020501", "#1A181C", "#650511", "#5F575D"]
type: ["Spline Sans", "JetBrains Mono", "tekoSans", "eurostile"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A monitoring tool borrows the language of a mecha cockpit: initializing screens, angled HUD frames, a city at night. Features sit inside the same frame shapes, so the product reads as the machine's console.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Joyco Studio).

## What to borrow (principle)

- Frame features inside a single recurring HUD/cockpit shape
- An 'initializing' screen as the loader for a technical product

## What to leave

- Cookie notice over many frames
- Red on red reduces contrast in places

## Signature move

Product features shown inside an angled red cockpit frame.

## Motion

Intro: 'SAZABI IS INITIALIZING' with a red bar (~2.5 s). Scroll (Lenis, ~120 px glide, three.js): city with craft and headline; cockpit frame; autonomous alerts / coding agents panels; 'READY FOR ACTION' red frame with feature cards; hexagon integrations; manifesto; backers list; security; 'SAVE THE DAY' red close.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 122 px still travelling after input stops); entry gate: START AN INCIDENT. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer tool styled like a mecha game: 'SAZABI IS INITIALIZING' in red, a night city with a hovering craft under 'OBSERVABILITY ON AUTOPILOT', a cockpit frame, red angled panels for features, hexagonal integration nodes and a red 'SAVE THE DAY' close. Type: Spline Sans, JetBrains Mono, tekoSans, eurostile.
Ground and ink from the measured palette (#020501, #1A181C, #650511). Motion carries the page through
product features shown inside an angled red cockpit frame. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D night city and mecha craft renders, red UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D night city and mecha craft renders, red UI

## Reference lock

Primary reference/direction: Sazabi — A developer tool styled like a mecha game: 'SAZABI IS INITIALIZING' in red, a night city with a hovering craft under 'OBSERVABILITY ON AUTOPILOT', a cockpit frame, red angled panels for features, hexagonal integration nodes and a red 'SAVE THE DAY' close.
Preserve (3-5 traits): red and black mecha/game UI; angled cockpit frames; condensed italic caps; 3D city and craft hero; hexagon integration nodes.
Borrow only (1-2): Frame features inside a single recurring HUD/cockpit shape; An 'initializing' screen as the loader for a technical product
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D night city and mecha craft renders, red UI
Reject: Cookie notice over many frames; Red on red reduces contrast in places
Token commitments: palette #020501, #1A181C, #650511, #5F575D; type Spline Sans, JetBrains Mono, tekoSans, eurostile; engine GSAP + Lenis linked (never vendored).
