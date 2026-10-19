---
title: "Specia1ne"
url: https://specia1ne.com/
source_url: https://specia1ne.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "product-focused"
family: blue-panel-systems-practice
dna: "Product and systems practice x Swiss grid with one blue"
register: modern clean
grammar: chaptered editorial
lane: "A paper-grey practice page with one cobalt blue: the hero headline sits on a vertical hairline, a blue panel grows from that line into the work list, and every list (work, practice, about) activates one row at a time along a central axis with numbered markers."
mode: persuade
traits: ["single cobalt blue", "vertical axis hairline through the page", "blue panel that grows from the axis", "list rows activating one at a time with markers", "Geist + Geist Mono", "bracketed CTA '[ Let's talk ]'"]
palette: ["#1C39F5", "#F3F1EB", "#C4C6CE", "#1A2DAB"]
type: ["Geist", "Geist Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The page has one structural idea, a vertical line, and everything hangs off it: the blue panel grows out of the line, list items light up as their marker crosses it, and the about section is 'one continuous line from idea to working form' drawn literally. The restraint (one blue, one sans) makes the axis the visual identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A single vertical axis that lists, panels and markers all refer to
- Grow the colour panel out of the axis instead of scrolling a coloured section in
- Activate list rows as their marker crosses the axis

## What to leave

- Heavy smoothing (~160 px glide)
- Hero headline in a generic bold sans

## Signature move

A cobalt panel that grows sideways out of the page's vertical hairline into the work list.

## Motion

Intro: static hero (no measurable intro). Scroll (Lenis, ~160 px glide): headline scrolls up as a blue panel expands from the axis to full width; work names grey out except the active one, whose blue marker sits on the axis; the panel recedes into the paper for 'Practice'; rows activate one at a time; 'One continuous line' draws a line down to the next section; contact CTA in a blue block.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; smoothed scroll (median 162 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a paper-grey practice page with one cobalt blue: the hero headline sits on a vertical hairline, a blue panel grows from that line into the work list, and every list (work, practice, about) activates one row at a time along a central axis with numbered markers. Type: Geist, Geist Mono.
Ground and ink from the measured palette (#1C39F5, #F3F1EB, #C4C6CE). Motion carries the page through
a cobalt panel that grows sideways out of the page's vertical hairline into the work list. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — no photography; product UI for case details

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: no photography; product UI for case details

## Reference lock

Primary reference/direction: Specia1ne — A paper-grey practice page with one cobalt blue: the hero headline sits on a vertical hairline, a blue panel grows from that line into the work list, and every list (work, practice, about) activates one row at a time along a central axis with numbered markers.
Preserve (3-5 traits): single cobalt blue; vertical axis hairline through the page; blue panel that grows from the axis; list rows activating one at a time with markers; Geist + Geist Mono.
Borrow only (1-2): A single vertical axis that lists, panels and markers all refer to; Grow the colour panel out of the axis instead of scrolling a coloured section in
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: no photography; product UI for case details
Reject: Heavy smoothing (~160 px glide); Hero headline in a generic bold sans
Token commitments: palette #1C39F5, #F3F1EB, #C4C6CE, #1A2DAB; type Geist, Geist Mono; engine GSAP + Lenis linked (never vendored).
