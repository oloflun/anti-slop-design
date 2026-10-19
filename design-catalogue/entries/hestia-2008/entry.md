---
title: "Hestia 2008 - Business advisory"
url: https://www.hestia-2008.com/
source_url: https://www.hestia-2008.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: magenta-statue-advisory
dna: "French advisory firm x a magenta-lit Hestia statue and marquee titles"
register: cinematic dark
grammar: chaptered editorial
lane: "An advisory firm: a dotted 'HESTIA' loader, a marquee 'Porteurs d'idees' with portrait thumbnails in the line, a dark section with a magenta-lit classical statue of Hestia, marquee 'Claire <•> une vision', magenta slashes and wavy line dividers, 'Histoire' with giant outline '2008' and partner photos."
mode: persuade
traits: ["magenta-lit classical statue", "marquee titles with inline thumbnails", "magenta highlighted words", "wavy line dividers", "giant outline year", "black and white alternation"]
palette: ["#F5F5F5", "#0B0F12", "#26262E", "#543753", "#B7ADB9"]
type: ["Safiro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The lit statue of the firm's namesake goddess gives a sober advisory site a striking emblem.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use the namesake as a lit statue emblem
- Wavy and slash line dividers as section transitions

## What to leave

- Dense highlighted body text

## Signature move

A classical statue of Hestia lit magenta on black.

## Motion

Intro: black with a dotted loader resolving to the name (~2 s). Wheel (Lenis, 3 triggers): marquees slide; the dark panel rises with the statue; magenta slashes and waves animate across; the outline year rises; photos slide.

Measured (`motion/probe.json`): GSAP 3.11.3/3.11.4; 3 ScrollTriggers; Lenis; split text; smoothed scroll (median 82 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: an advisory firm: a dotted 'HESTIA' loader, a marquee 'Porteurs d'idees' with portrait thumbnails in the line, a dark section with a magenta-lit classical statue of Hestia, marquee 'Claire <•> une vision', magenta slashes and wavy line dividers, 'Histoire' with giant outline '2008' and partner photos. Type: Safiro.
Ground and ink from the measured palette (#F5F5F5, #0B0F12, #26262E). Motion carries the page through
a classical statue of Hestia lit magenta on black. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — classical sculpture, partner photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: classical sculpture, partner photography

## Reference lock

Primary reference/direction: Hestia 2008 - Business advisory — An advisory firm: a dotted 'HESTIA' loader, a marquee 'Porteurs d'idees' with portrait thumbnails in the line, a dark section with a magenta-lit classical statue of Hestia, marquee 'Claire <•> une vision', magenta slashes and wavy line dividers, 'Histoire' with giant outline '2008' and partner photos.
Preserve (3-5 traits): magenta-lit classical statue; marquee titles with inline thumbnails; magenta highlighted words; wavy line dividers; giant outline year.
Borrow only (1-2): Use the namesake as a lit statue emblem; Wavy and slash line dividers as section transitions
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: classical sculpture, partner photography
Reject: Dense highlighted body text
Token commitments: palette #F5F5F5, #0B0F12, #26262E, #543753, #B7ADB9; type Safiro; engine GSAP + Lenis linked (never vendored).
