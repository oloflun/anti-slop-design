---
title: "Forms"
url: https://www.forms.world/
source_url: https://www.forms.world/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: fullbleed-reel-index
dna: "Production company x full-bleed film index"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A production company with no page at all: every wheel step cuts to the next full-bleed film loop, with a small serif title and credits on one hairline across the middle."
mode: experience
traits: ["full-bleed looping film per project", "one hairline row with client / title in small serif italic", "wordmark preloader", "wheel = next cut (virtual)", "serif + mono micro type"]
palette: ["#040709", "#4F4E61", "#1E262A", "#888A91"]
type: ["PP Editorial New", "Sometype Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The index is the reel. There is no layout to scroll; each wheel step is an edit to the next film, and the only typography is one hairline row carrying client and title in a small serif italic. The restraint keeps every campaign frame intact.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Beaucoup).

## What to borrow (principle)

- When the work is film, make the wheel cut between full-bleed loops instead of scrolling a grid
- Hold all text on one constant hairline so cuts change only the picture
- Serif italic for titles at caption size keeps a luxury register without a headline

## What to leave

- No overview of how many projects or where you are
- Wheel-only navigation; the list loops so the end never arrives

## Signature move

A wheel that cuts between full-bleed films while the title line stays fixed.

## Motion

Intro: black, 'FORMS' wordmark with a small glyph grid, then the first film fades up (~2.5 s). Wheel (virtual, Lenis, Taxi): each step crossfades/cuts to the next looping film; the hairline row's client/title text swaps with a SplitText line reveal; after the last project the list loops back to the first.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; 11 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a production company with no page at all: every wheel step cuts to the next full-bleed film loop, with a small serif title and credits on one hairline across the middle. Type: PP Editorial New, Sometype Mono.
Ground and ink from the measured palette (#040709, #4F4E61, #1E262A). Motion carries the page through
a wheel that cuts between full-bleed films while the title line stays fixed. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign film frames, high-end grading, strong single colour per film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign film frames, high-end grading, strong single colour per film

## Reference lock

Primary reference/direction: Forms — A production company with no page at all: every wheel step cuts to the next full-bleed film loop, with a small serif title and credits on one hairline across the middle.
Preserve (3-5 traits): full-bleed looping film per project; one hairline row with client / title in small serif italic; wordmark preloader; wheel = next cut (virtual); serif + mono micro type.
Borrow only (1-2): When the work is film, make the wheel cut between full-bleed loops instead of scrolling a grid; Hold all text on one constant hairline so cuts change only the picture
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign film frames, high-end grading, strong single colour per film
Reject: No overview of how many projects or where you are; Wheel-only navigation; the list loops so the end never arrives
Token commitments: palette #040709, #4F4E61, #1E262A, #888A91; type PP Editorial New, Sometype Mono; engine GSAP + Lenis linked (never vendored).
