---
title: "LaCrapule Studio - Image, CGI and Moving Things"
url: https://lacrapulestudio.com/
source_url: https://lacrapulestudio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: cgi-triptych-studio-reel
dna: "Paris CGI studio x triptych of moving panels per client"
register: modern clean
grammar: rhythmic cutlist
lane: "A CGI studio on white then grey: name intro, then each client (Lacoste, Audemars Piguet, Coperni, Lancome, MCM) appears as a triptych of three moving panels across the screen with the client name large at bottom left, a counter and a project arrow; panels change in sequence as you scroll."
mode: experience
traits: ["triptych of three video panels", "client name large bottom left", "grey neutral ground", "luxury product CGI", "client index along the bottom", "virtual scroll"]
palette: ["#231C1B", "#B8B8B8", "#4A644C", "#8D8E8A", "#767574", "#3A3D39"]
type: ["sa", "jb", "bl"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Three panels per client show range (detail, product, mood) at once, and the fixed name and arrow make the reel navigable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Show each project as a three-panel triptych

## What to leave

- Hard to know how many projects remain
- Small index

## Signature move

Three CGI panels side by side per client with the name big at bottom left.

## Motion

Intro: white with the name (~2 s). Wheel (virtual, no native scroll): the triptych changes panel by panel, left to right, between clients; the name swaps with a slide; the index highlights; panels zoom slowly while playing.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 5 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the rhythmic cutlist grammar: a CGI studio on white then grey: name intro, then each client (Lacoste, Audemars Piguet, Coperni, Lancome, MCM) appears as a triptych of three moving panels across the screen with the client name large at bottom left, a counter and a project arrow; panels change in sequence as you scroll. Type: sa, jb, bl.
Ground and ink from the measured palette (#231C1B, #B8B8B8, #4A644C). Motion carries the page through
three CGI panels side by side per client with the name big at bottom left. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — luxury product CGI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: luxury product CGI

## Reference lock

Primary reference/direction: LaCrapule Studio - Image, CGI and Moving Things — A CGI studio on white then grey: name intro, then each client (Lacoste, Audemars Piguet, Coperni, Lancome, MCM) appears as a triptych of three moving panels across the screen with the client name large at bottom left, a counter and a project arrow; panels change in sequence as you scroll.
Preserve (3-5 traits): triptych of three video panels; client name large bottom left; grey neutral ground; luxury product CGI; client index along the bottom.
Borrow only (1-2): Show each project as a three-panel triptych
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: luxury product CGI
Reject: Hard to know how many projects remain; Small index
Token commitments: palette #231C1B, #B8B8B8, #4A644C, #8D8E8A, #767574, #3A3D39; type sa, jb, bl; engine GSAP + Lenis linked (never vendored).
