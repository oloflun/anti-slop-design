---
title: "Debabrata Giri"
url: https://debabratagiri.vercel.app/
source_url: https://debabratagiri.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: desktop-os-dev-folio
dna: "Creative developer folio x desktop operating system"
register: modern clean
grammar: live surface
lane: "A folio styled as a pale operating system: a sidebar of apps (projects, terminal, notes, playground), a typed 'Hello, I'm Debabrata Giri_' greeting, a live clock, and an orbiting line diagram that drifts beside it."
mode: operate
traits: ["OS chrome: sidebar apps, clock, command bar", "typed greeting with cursor", "orbital line diagram (DrawSVG)", "monospace throughout", "chip tags"]
palette: ["#F5F3EF", "#D7D6D2"]
type: ["Source Code Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The folio is a tool you operate rather than a page you read: apps in a sidebar, a command line at the bottom, a live clock. The orbit diagram is the only decoration and it moves continuously, which makes the OS feel switched on.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- When the audience is technical, an OS/terminal frame can replace the landing page
- One continuously drawn diagram as the ambient motion

## What to leave

- Nothing happens on scroll
- Monospace for all text flattens hierarchy

## Signature move

A personal OS with a typed greeting and an orbit diagram that keeps drawing.

## Motion

Intro: greeting types character by character with a blinking cursor (~1.2 s), the orbit rings draw in (DrawSVG). Idle: dots travel the rings continuously; Draggable/Inertia on windows. The wheel does not move the page.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a folio styled as a pale operating system: a sidebar of apps (projects, terminal, notes, playground), a typed 'Hello, I'm Debabrata Giri_' greeting, a live clock, and an orbiting line diagram that drifts beside it. Type: Source Code Pro.
Ground and ink from the measured palette (#F5F3EF, #D7D6D2). Motion carries the page through
a personal OS with a typed greeting and an orbit diagram that keeps drawing. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — line diagrams and UI chrome, no photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: line diagrams and UI chrome, no photography

## Reference lock

Primary reference/direction: Debabrata Giri — A folio styled as a pale operating system: a sidebar of apps (projects, terminal, notes, playground), a typed 'Hello, I'm Debabrata Giri_' greeting, a live clock, and an orbiting line diagram that drifts beside it.
Preserve (3-5 traits): OS chrome: sidebar apps, clock, command bar; typed greeting with cursor; orbital line diagram (DrawSVG); monospace throughout; chip tags.
Borrow only (1-2): When the audience is technical, an OS/terminal frame can replace the landing page; One continuously drawn diagram as the ambient motion
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: line diagrams and UI chrome, no photography
Reject: Nothing happens on scroll; Monospace for all text flattens hierarchy
Token commitments: palette #F5F3EF, #D7D6D2; type Source Code Pro; engine GSAP + Lenis linked (never vendored).
