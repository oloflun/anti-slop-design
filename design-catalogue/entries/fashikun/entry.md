---
title: "Fashikun"
url: https://www.fashikun.com/
source_url: https://www.fashikun.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: brand-designer-wordmark-archive
dna: "Lagos brand designer x a giant wordmark and a poster archive strip"
register: cinematic dark
grammar: gallery/catalog
lane: "A brand designer's folio: a 'loading site' line, a black page with a mono spec sheet and the giant 'FASHIKUN(c)' wordmark, then a full-screen 'FORWARDS' repeat type poster, project tiles in a dense two-row grid of brand work (Strikers, Table Soccer, Pith, Studio Fola), a services list and a 'Fash archive' strip of tiny posters where the hovered one grows."
mode: read
traits: ["giant wordmark with (c)", "mono spec sheet header", "repeat-type poster interlude", "dense project tile grid", "archive strip of tiny posters", "one poster enlarging"]
palette: ["#101010", "#C2C7C3", "#09257F", "#2C262A", "#EFEBB6", "#738080"]
type: ["suisseIntl", "mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The archive strip is a smart closer: dozens of posters as thumbnails with one growing, which shows volume and taste at once.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- An archive strip of tiny thumbnails where one enlarges
- A repeat-type poster as the transition into work

## What to leave

- Tiny mono text
- Project grid is crowded

## Signature move

A strip of tiny posters with one growing into a full poster.

## Motion

Intro: black 'loading site' for ~2 s, the wordmark slides up. Wheel (Lenis): the repeat-type poster fills the screen; tiles slide in and swap media on hover; the archive strip scrolls sideways and one poster scales up in the middle.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 8 video; smoothed scroll (median 150 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the gallery/catalog grammar: a brand designer's folio: a 'loading site' line, a black page with a mono spec sheet and the giant 'FASHIKUN(c)' wordmark, then a full-screen 'FORWARDS' repeat type poster, project tiles in a dense two-row grid of brand work (Strikers, Table Soccer, Pith, Studio Fola), a services list and a 'Fash archive' strip of tiny posters where the hovered one grows. Type: suisseIntl, mono.
Ground and ink from the measured palette (#101010, #C2C7C3, #09257F). Motion carries the page through
a strip of tiny posters with one growing into a full poster. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand identity work, posters

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand identity work, posters

## Reference lock

Primary reference/direction: Fashikun — A brand designer's folio: a 'loading site' line, a black page with a mono spec sheet and the giant 'FASHIKUN(c)' wordmark, then a full-screen 'FORWARDS' repeat type poster, project tiles in a dense two-row grid of brand work (Strikers, Table Soccer, Pith, Studio Fola), a services list and a 'Fash archive' strip of tiny posters where the hovered one grows.
Preserve (3-5 traits): giant wordmark with (c); mono spec sheet header; repeat-type poster interlude; dense project tile grid; archive strip of tiny posters.
Borrow only (1-2): An archive strip of tiny thumbnails where one enlarges; A repeat-type poster as the transition into work
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand identity work, posters
Reject: Tiny mono text; Project grid is crowded
Token commitments: palette #101010, #C2C7C3, #09257F, #2C262A, #EFEBB6, #738080; type suisseIntl, mono; engine GSAP + Lenis linked (never vendored).
