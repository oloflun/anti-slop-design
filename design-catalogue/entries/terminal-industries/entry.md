---
title: "Terminal - Yard Operating System"
url: https://terminal-industries.com/
source_url: https://terminal-industries.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: saas-ui-scroll-demo
dna: "Logistics yard software x the actual product UI scrolling as the page"
register: modern clean
grammar: live surface
lane: "A logistics software page that is essentially its UI: a logo loader over a faint road map, then a dark-green sidebar and white dashboard ('Yard Operating System') with gate automation, asset inventory, movements, shipments, analytics bars, compliance and fraud tables scrolling as the page."
mode: operate
traits: ["real product UI as the page", "dark green sidebar", "truck photo cards in gate log", "bar charts", "demonstration data labels", "road map loader"]
palette: ["#F9FBFC", "#0E2519", "#687970"]
type: ["Suisse", "Roboto Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Showing the actual dashboard is the most direct pitch for an operations product.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Propagande Studio, Rejouice).

## What to borrow (principle)

- Let the product UI be the landing page for an ops tool

## What to leave

- No narrative or hierarchy

## Signature move

The yard dashboard itself scrolling as the landing page.

## Motion

Intro: a faint road map and logo assemble (~2 s). Wheel: the dashboard panels scroll; numbers tick; bars fill.

Measured (`motion/probe.json`): virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: EXPLORE PRODUCT, Explore Terminal — home. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a logistics software page that is essentially its UI: a logo loader over a faint road map, then a dark-green sidebar and white dashboard ('Yard Operating System') with gate automation, asset inventory, movements, shipments, analytics bars, compliance and fraud tables scrolling as the page. Type: Suisse, Roboto Mono.
Ground and ink from the measured palette (#F9FBFC, #0E2519, #687970). Motion carries the page through
the yard dashboard itself scrolling as the landing page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product UI, truck photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product UI, truck photos

## Reference lock

Primary reference/direction: Terminal - Yard Operating System — A logistics software page that is essentially its UI: a logo loader over a faint road map, then a dark-green sidebar and white dashboard ('Yard Operating System') with gate automation, asset inventory, movements, shipments, analytics bars, compliance and fraud tables scrolling as the page.
Preserve (3-5 traits): real product UI as the page; dark green sidebar; truck photo cards in gate log; bar charts; demonstration data labels.
Borrow only (1-2): Let the product UI be the landing page for an ops tool
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product UI, truck photos
Reject: No narrative or hierarchy
Token commitments: palette #F9FBFC, #0E2519, #687970; type Suisse, Roboto Mono; engine GSAP + Lenis linked (never vendored).
