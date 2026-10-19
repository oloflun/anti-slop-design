---
title: "Lucas - developer portfolio"
url: https://www.lucasportfolio.dev/
source_url: https://www.lucasportfolio.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: white-torus-dev-folio
dna: "Interactive developer x a soft white 3D torus that rotates behind the text"
register: modern clean
grammar: live surface
lane: "A developer folio on white: 'DEVELOPER' in bold caps with a small subtitle, a soft white 3D torus that rotates and moves around the screen as text blocks about interactive installations and projects appear, with a red 'Let's talk' button."
mode: read
traits: ["soft white 3D torus", "bold caps title", "text blocks swapping", "white on white shading", "red CTA"]
palette: ["#FFFFFF", "#CBCBCB", "#EAEAEA", "#8B7C7B"]
type: ["__ibmMono_929560", "__satoshi_ba7a58"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A single soft object gives a text-only folio depth; the shading is subtle and calm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One soft white 3D object behind text blocks

## What to leave

- Repeats the same sections

## Signature move

A soft white torus rotating behind 'DEVELOPER'.

## Motion

Intro: 'DEVELOPER' with scroll hint (~1 s), the torus fades up. Wheel: the torus rotates and drifts; text blocks fade in and out.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); 9 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a developer folio on white: 'DEVELOPER' in bold caps with a small subtitle, a soft white 3D torus that rotates and moves around the screen as text blocks about interactive installations and projects appear, with a red 'Let's talk' button. Type: __ibmMono_929560, __satoshi_ba7a58.
Ground and ink from the measured palette (#FFFFFF, #CBCBCB, #EAEAEA). Motion carries the page through
a soft white torus rotating behind 'DEVELOPER'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL torus

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL torus

## Reference lock

Primary reference/direction: Lucas - developer portfolio — A developer folio on white: 'DEVELOPER' in bold caps with a small subtitle, a soft white 3D torus that rotates and moves around the screen as text blocks about interactive installations and projects appear, with a red 'Let's talk' button.
Preserve (3-5 traits): soft white 3D torus; bold caps title; text blocks swapping; white on white shading; red CTA.
Borrow only (1-2): One soft white 3D object behind text blocks
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL torus
Reject: Repeats the same sections
Token commitments: palette #FFFFFF, #CBCBCB, #EAEAEA, #8B7C7B; type __ibmMono_929560, __satoshi_ba7a58; engine GSAP + Lenis linked (never vendored).
