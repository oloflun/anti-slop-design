---
title: "Tea Teearu - Web Design and Development"
url: http://teateearu.com/
source_url: http://teateearu.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: red-duotone-brushstroke-folio
dna: "Web designer x red duotone portrait over teal brush strokes"
register: editorial print
grammar: chaptered editorial
lane: "A designer folio on pale blue: a red duotone portrait over a teal brush stroke with a red italic 'Welcome - glad you're here' and a big serif name, which blurs as an italic intro fills over the portrait, a 'Design / Development / E-commerce' list, an about with a wavy red portrait and a closing CTA in a yellow highlight."
mode: persuade
traits: ["red duotone portrait", "teal brush strokes", "italic red serif", "blurred giant name behind", "wavy distortion on portrait", "yellow highlighted CTA"]
palette: ["#B7D1D8", "#BE908B"]
type: ["Dmsans Variablefont Opsz Wght", "Silene Roman", "Silene"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The duotone red against teal brush is a distinctive, hand-made palette for a solo designer, and blur is used as the transition between layers.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Duotone portrait over a painted stroke as the personal mark
- Blur the hero as the next layer of text arrives

## What to leave

- Blur makes much of the page unreadable
- Small body text

## Signature move

A red duotone portrait over a teal brush stroke on pale blue.

## Motion

Intro: pale blue with a thin line (~1.5 s), the portrait and name fade in. Wheel (Lenis ~60 px glide, 1 pin): the name blurs; the intro fills in italic over the portrait; the list slides in; the portrait warps with a wave shader; the brush stroke stretches; the CTA highlight sweeps.

Measured (`motion/probe.json`): GSAP 3.12.5; 2 ScrollTriggers; 1 pinned sections; Lenis; WebGL canvas x4; 2 video; split text; smoothed scroll (median 58 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a designer folio on pale blue: a red duotone portrait over a teal brush stroke with a red italic 'Welcome - glad you're here' and a big serif name, which blurs as an italic intro fills over the portrait, a 'Design / Development / E-commerce' list, an about with a wavy red portrait and a closing CTA in a yellow highlight. Type: Dmsans Variablefont Opsz Wght, Silene Roman, Silene.
Ground and ink from the measured palette (#B7D1D8, #BE908B). Motion carries the page through
a red duotone portrait over a teal brush stroke on pale blue. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — duotone portrait, brush texture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: duotone portrait, brush texture

## Reference lock

Primary reference/direction: Tea Teearu - Web Design and Development — A designer folio on pale blue: a red duotone portrait over a teal brush stroke with a red italic 'Welcome - glad you're here' and a big serif name, which blurs as an italic intro fills over the portrait, a 'Design / Development / E-commerce' list, an about with a wavy red portrait and a closing CTA in a yellow highlight.
Preserve (3-5 traits): red duotone portrait; teal brush strokes; italic red serif; blurred giant name behind; wavy distortion on portrait.
Borrow only (1-2): Duotone portrait over a painted stroke as the personal mark; Blur the hero as the next layer of text arrives
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: duotone portrait, brush texture
Reject: Blur makes much of the page unreadable; Small body text
Token commitments: palette #B7D1D8, #BE908B; type Dmsans Variablefont Opsz Wght, Silene Roman, Silene; engine GSAP + Lenis linked (never vendored).
