---
title: "Shader Development Studio"
url: https://www.shader.se/
source_url: https://www.shader.se/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: crt-boot-3d-showroom
dna: "Swedish 3D studio x a retro CRT boot screen, then a curved filmstrip carousel of 3D showrooms in a dark room"
register: cinematic dark
grammar: live surface
lane: "A 3D studio: a CRT monitor with a blue boot screen ('Shader Development Studio, Website Version 1.02') and a loading bar, the camera pushing past the monitor into a dark room where a curved filmstrip holds projects, the centre frame a rotating 3D showroom ('eHealth Arena') whose room swaps colourways as you scroll."
mode: experience
traits: ["CRT boot screen loader", "camera pushes into the screen", "curved filmstrip carousel", "live 3D showroom in the centre frame"]
palette: ["#3E3987", "#090909", "#4A5970", "#292567", "#AFA9A1", "#727681"]
type: ["STIX Two Text"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Booting a fake computer and diving through its screen sets up the studio as makers of digital spaces before a word is read.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Shader Development Studio).

## What to borrow (principle)

- Dive through the loader's screen into the site

## What to leave

- Wheel drives only the carousel, no page

## Signature move

A blue CRT boot screen with a loading bar.

## Motion

Intro: CRT boot with loading bar (~4 s), camera dollies into the screen. Wheel: rotates the filmstrip and swaps the showroom variant; no page scroll.

Measured (`motion/probe.json`): virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a 3D studio: a CRT monitor with a blue boot screen ('Shader Development Studio, Website Version 1.02') and a loading bar, the camera pushing past the monitor into a dark room where a curved filmstrip holds projects, the centre frame a rotating 3D showroom ('eHealth Arena') whose room swaps colourways as you scroll. Type: STIX Two Text.
Ground and ink from the measured palette (#3E3987, #090909, #4A5970). Motion carries the page through
a blue CRT boot screen with a loading bar. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL 3D rooms

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL 3D rooms

## Reference lock

Primary reference/direction: Shader Development Studio — A 3D studio: a CRT monitor with a blue boot screen ('Shader Development Studio, Website Version 1.02') and a loading bar, the camera pushing past the monitor into a dark room where a curved filmstrip holds projects, the centre frame a rotating 3D showroom ('eHealth Arena') whose room swaps colourways as you scroll.
Preserve (3-5 traits): CRT boot screen loader; camera pushes into the screen; curved filmstrip carousel; live 3D showroom in the centre frame.
Borrow only (1-2): Dive through the loader's screen into the site
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL 3D rooms
Reject: Wheel drives only the carousel, no page
Token commitments: palette #3E3987, #090909, #4A5970, #292567, #AFA9A1, #727681; type STIX Two Text; engine GSAP + Lenis linked (never vendored).
