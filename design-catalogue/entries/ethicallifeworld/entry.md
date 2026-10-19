---
title: "Ethical Life - Multivitamin Gummies"
url: https://ethicallifeworld.com/
source_url: https://ethicallifeworld.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: gummy-jar-lime-commerce
dna: "Vitamin gummies x a jar that moves between lime product sections"
register: modern clean
grammar: chaptered editorial
lane: "A product page on a lime gradient: 'Daily Multivitamin Gummies' beside a jar, the jar moving between sections (why choose, formulation, clean ingredients) with pink star gummies flying out, benefit cards in lime, gummies vs pills, who it's for, values, FAQ and a giant 'ethical life' wordmark footer."
mode: persuade
traits: ["lime gradient ground", "product jar travelling", "gummies flying out", "benefit cards", "giant wordmark footer", "shop buttons"]
palette: ["#FCFBFE", "#E3F469", "#D7D7C9", "#EDF6B6", "#96927E"]
type: ["Inter", "Sora"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The jar staying in view through the sections keeps a long e-commerce page anchored to the product.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the product jar travel between sections

## What to leave

- Long generic text sections

## Signature move

A gummy jar with pink stars flying out on a lime gradient.

## Motion

Intro: lime hero. Wheel (Lenis, Barba): the jar drifts between sections and tilts; gummies burst out; cards slide; the wordmark rises in the footer.

Measured (`motion/probe.json`): GSAP 3.12.4; 4 ScrollTriggers; Lenis; Barba page transitions; smoothed scroll (median 144 px still travelling after input stops); entry gate: ×. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a product page on a lime gradient: 'Daily Multivitamin Gummies' beside a jar, the jar moving between sections (why choose, formulation, clean ingredients) with pink star gummies flying out, benefit cards in lime, gummies vs pills, who it's for, values, FAQ and a giant 'ethical life' wordmark footer. Type: Inter, Sora.
Ground and ink from the measured palette (#FCFBFE, #E3F469, #D7D7C9). Motion carries the page through
a gummy jar with pink stars flying out on a lime gradient. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product photography and renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product photography and renders

## Reference lock

Primary reference/direction: Ethical Life - Multivitamin Gummies — A product page on a lime gradient: 'Daily Multivitamin Gummies' beside a jar, the jar moving between sections (why choose, formulation, clean ingredients) with pink star gummies flying out, benefit cards in lime, gummies vs pills, who it's for, values, FAQ and a giant 'ethical life' wordmark footer.
Preserve (3-5 traits): lime gradient ground; product jar travelling; gummies flying out; benefit cards; giant wordmark footer.
Borrow only (1-2): Let the product jar travel between sections
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product photography and renders
Reject: Long generic text sections
Token commitments: palette #FCFBFE, #E3F469, #D7D7C9, #EDF6B6, #96927E; type Inter, Sora; engine GSAP + Lenis linked (never vendored).
