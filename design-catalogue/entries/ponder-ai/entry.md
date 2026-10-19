---
title: "Ponder"
url: https://ponder.ai/
source_url: https://ponder.ai/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: product-ui-video-editor
dna: "AI video editor x full product UI as hero"
register: cinematic dark
grammar: live surface
lane: "An AI video editor's page where the hero is the product itself: a full editor window with a playing film, a prompt panel and a timeline whose clips rearrange as the scroll advances and the film cuts."
mode: persuade
traits: ["full product UI as the hero", "live video playing inside the UI", "timeline clips reordering", "black ground, small white type", "download CTA"]
palette: ["#000000", "#242424", "#323A46", "#626A74"]
type: ["Inter Variable", "YDYoonche", "Lay Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Instead of a mock-up, the actual editor runs on the page: the film inside it plays and cuts, and the timeline below updates as if the AI were editing while you scroll. The product demonstrates itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the real product UI run as the hero and animate its own state with scroll

## What to leave

- Captures show the same frame for many steps: little visible progression
- Very small UI text

## Signature move

A live editor window whose film and timeline keep cutting as you scroll.

## Motion

Intro: headline and editor window present; the film inside plays (~1 s). Scroll (Lenis, mostly pinned): the editor zooms to fill the frame; prompt text appears; timeline clips slide and reorder; the preview cuts between shots; 'An editor that works the way you do.' stays below.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 2 video. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: an AI video editor's page where the hero is the product itself: a full editor window with a playing film, a prompt panel and a timeline whose clips rearrange as the scroll advances and the film cuts. Type: Inter Variable, YDYoonche, Lay Grotesk.
Ground and ink from the measured palette (#000000, #242424, #323A46). Motion carries the page through
a live editor window whose film and timeline keep cutting as you scroll. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cinematic film frames inside product UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cinematic film frames inside product UI

## Reference lock

Primary reference/direction: Ponder — An AI video editor's page where the hero is the product itself: a full editor window with a playing film, a prompt panel and a timeline whose clips rearrange as the scroll advances and the film cuts.
Preserve (3-5 traits): full product UI as the hero; live video playing inside the UI; timeline clips reordering; black ground, small white type; download CTA.
Borrow only (1-2): Let the real product UI run as the hero and animate its own state with scroll
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cinematic film frames inside product UI
Reject: Captures show the same frame for many steps: little visible progression; Very small UI text
Token commitments: palette #000000, #242424, #323A46, #626A74; type Inter Variable, YDYoonche, Lay Grotesk; engine GSAP + Lenis linked (never vendored).
