---
title: "Sui Overflow 2026 - hackathon"
url: https://overflow.sui.io/
source_url: https://overflow.sui.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: hackathon-keycap-grid
dna: "Global hackathon x 3D keycaps spelling OVERFLOW on a blue grid"
register: modern clean
grammar: chaptered editorial
lane: "A hackathon site on a blue graph-paper grid: a terminal-style loader window with a progress bar, 'Sui Overflow 2026' in bold grotesk with colourful 3D keycaps spelling OVERFLOW plus a cursor, pencil and speech bubble, 'Why join' on dark navy with benefit chips, 'Tracks' as coloured cards (Agentic Web, DeFi and Payments, Walrus, DeepBook) with 3D props, 'Prizes' in a table with coins and gems, sponsor blocks in colour and 'Two years of Sui's flagship hackathon'."
mode: persuade
traits: ["graph-paper grid ground", "3D keycaps spelling the name", "terminal window loader", "coloured track cards with 3D props", "prize table with coins", "bottom tab nav highlighting the section"]
palette: ["#F7F7F7", "#00101F", "#89A0B3", "#413743", "#FBE791"]
type: ["TWK Everett", "TWK Everett Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Keycaps spelling the event name say 'build' instantly, and the bottom tab bar keeps a long info page navigable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Spell the event name in objects of the craft
- A bottom tab bar that lights the current section

## What to leave

- Grey skeleton placeholders

## Signature move

Colourful 3D keycaps spelling OVERFLOW on graph paper.

## Motion

Intro: a terminal window fills a progress bar (~2 s), then closes. Wheel: keycaps tumble; the navy panel rises; chips stagger; track cards slide in pairs; prize cells fill; sponsor blocks flip colour; the tab bar follows.

Measured (`motion/probe.json`): GSAP 3.12.7; 202 ScrollTriggers; Lenis; split text; smoothed scroll (median 134 px still travelling after input stops); entry gate: Decline. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a hackathon site on a blue graph-paper grid: a terminal-style loader window with a progress bar, 'Sui Overflow 2026' in bold grotesk with colourful 3D keycaps spelling OVERFLOW plus a cursor, pencil and speech bubble, 'Why join' on dark navy with benefit chips, 'Tracks' as coloured cards (Agentic Web, DeFi and Payments, Walrus, DeepBook) with 3D props, 'Prizes' in a table with coins and gems, sponsor blocks in colour and 'Two years of Sui's flagship hackathon'. Type: TWK Everett, TWK Everett Mono.
Ground and ink from the measured palette (#F7F7F7, #00101F, #89A0B3). Motion carries the page through
colourful 3D keycaps spelling OVERFLOW on graph paper. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D keycaps and props

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D keycaps and props

## Reference lock

Primary reference/direction: Sui Overflow 2026 - hackathon — A hackathon site on a blue graph-paper grid: a terminal-style loader window with a progress bar, 'Sui Overflow 2026' in bold grotesk with colourful 3D keycaps spelling OVERFLOW plus a cursor, pencil and speech bubble, 'Why join' on dark navy with benefit chips, 'Tracks' as coloured cards (Agentic Web, DeFi and Payments, Walrus, DeepBook) with 3D props, 'Prizes' in a table with coins and gems, sponsor blocks in colour and 'Two years of Sui's flagship hackathon'.
Preserve (3-5 traits): graph-paper grid ground; 3D keycaps spelling the name; terminal window loader; coloured track cards with 3D props; prize table with coins.
Borrow only (1-2): Spell the event name in objects of the craft; A bottom tab bar that lights the current section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D keycaps and props
Reject: Grey skeleton placeholders
Token commitments: palette #F7F7F7, #00101F, #89A0B3, #413743, #FBE791; type TWK Everett, TWK Everett Mono; engine GSAP + Lenis linked (never vendored).
