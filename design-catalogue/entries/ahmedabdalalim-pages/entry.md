---
title: "Ahmed Abd Alalim - Frontend Developer"
url: https://ahmedabdalalim.pages.dev/
source_url: https://ahmedabdalalim.pages.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: diamond-logo-dev-folio
dna: "Frontend developer x a diamond logo reveal and condensed section titles"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio: a yellow logo mark with a percent counter, lines crossing into a diamond, a black diamond on grey that expands to the screen, a portrait in a night street, a statement that fills white, 'LATEST WORK' with project mockups, 'NUMBERS DON'T LIE' with stats, 'CODE SAMPLES' with tilted screens and a process."
mode: persuade
traits: ["diamond shape as the transition", "yellow logo mark", "condensed uppercase section titles", "statement fill on scroll", "tilted screen mockups", "stat counters"]
palette: ["#0A0A0A", "#252523", "#6D665B"]
type: ["Geist", "Anton"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The diamond is a clean, single transition that turns the loader into the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Grow the logo's container shape to fill the screen as the reveal

## What to leave

- Generic sections after the hero
- Small captions

## Signature move

A black diamond growing from the logo to fill the screen.

## Motion

Intro: black, the mark fills yellow as the counter runs 0 to 100%, two lines cross and form a diamond outline (~3 s); the grey page appears with a solid black diamond that expands. Wheel (ScrollSmoother, 3 pins): the portrait fades; the statement fills; section titles pin while project cards rise; stats count; code screens tilt in.

Measured (`motion/probe.json`): GSAP 3.13.0; 3 pinned sections; ScrollSmoother. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio: a yellow logo mark with a percent counter, lines crossing into a diamond, a black diamond on grey that expands to the screen, a portrait in a night street, a statement that fills white, 'LATEST WORK' with project mockups, 'NUMBERS DON'T LIE' with stats, 'CODE SAMPLES' with tilted screens and a process. Type: Geist, Anton.
Ground and ink from the measured palette (#0A0A0A, #252523, #6D665B). Motion carries the page through
a black diamond growing from the logo to fill the screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — portrait, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: portrait, device mockups

## Reference lock

Primary reference/direction: Ahmed Abd Alalim - Frontend Developer — A developer folio: a yellow logo mark with a percent counter, lines crossing into a diamond, a black diamond on grey that expands to the screen, a portrait in a night street, a statement that fills white, 'LATEST WORK' with project mockups, 'NUMBERS DON'T LIE' with stats, 'CODE SAMPLES' with tilted screens and a process.
Preserve (3-5 traits): diamond shape as the transition; yellow logo mark; condensed uppercase section titles; statement fill on scroll; tilted screen mockups.
Borrow only (1-2): Grow the logo's container shape to fill the screen as the reveal
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: portrait, device mockups
Reject: Generic sections after the hero; Small captions
Token commitments: palette #0A0A0A, #252523, #6D665B; type Geist, Anton; engine GSAP + Lenis linked (never vendored).
