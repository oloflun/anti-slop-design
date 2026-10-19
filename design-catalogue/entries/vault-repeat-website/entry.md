---
title: "Repeat - reorder automation"
url: https://vault-repeat-website.vercel.app/
source_url: https://vault-repeat-website.vercel.app/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: line-drawing-packaging-saas
dna: "Reorder automation x line-drawn product packs and a lime accent"
register: modern clean
grammar: chaptered editorial
lane: "A SaaS for consumer brands: 'RESTOCK REORDER REPEAT' in caps on lime, line drawings of bottles and cans floating with small notification tags, 'The easiest way to automate reordering', 'Get more from your automations and flows' with a case card (4x revenue), stats rows, 'Automatically trigger your reorder flows' with a phone showing a curve, 'Offer the right products', 'Automate the conversion point', 'Stop fighting with flows. Use Repeat.' on black with line-drawn packs and a lime footer."
mode: persuade
traits: ["line-drawn product packs", "lime and black", "caps headings", "phone UI cards", "notification tags", "stacked panels"]
palette: ["#EBE7E2", "#C5C5BC", "#FFFFFF", "#5D4643", "#F4FC85"]
type: ["Mabry"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Drawing the customers' products as line art makes the SaaS feel close to the brands it serves.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Studio Freight).

## What to borrow (principle)

- Draw the customer's products as floating line art

## What to leave

- Many similar panels

## Signature move

Line-drawn bottles and cans floating with notification tags.

## Motion

Intro: lime with three caps words (~1 s). Wheel: packs float and rotate; panels stack; the curve on the phone draws; panels alternate lime and white; the black panel rises with packs.

Measured (`motion/probe.json`): GSAP 3.10.4; WebGL canvas x2 (three.js); smoothed scroll (median 84 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a SaaS for consumer brands: 'RESTOCK REORDER REPEAT' in caps on lime, line drawings of bottles and cans floating with small notification tags, 'The easiest way to automate reordering', 'Get more from your automations and flows' with a case card (4x revenue), stats rows, 'Automatically trigger your reorder flows' with a phone showing a curve, 'Offer the right products', 'Automate the conversion point', 'Stop fighting with flows. Use Repeat.' on black with line-drawn packs and a lime footer. Type: Mabry.
Ground and ink from the measured palette (#EBE7E2, #C5C5BC, #FFFFFF). Motion carries the page through
line-drawn bottles and cans floating with notification tags. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — line drawings, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: line drawings, UI

## Reference lock

Primary reference/direction: Repeat - reorder automation — A SaaS for consumer brands: 'RESTOCK REORDER REPEAT' in caps on lime, line drawings of bottles and cans floating with small notification tags, 'The easiest way to automate reordering', 'Get more from your automations and flows' with a case card (4x revenue), stats rows, 'Automatically trigger your reorder flows' with a phone showing a curve, 'Offer the right products', 'Automate the conversion point', 'Stop fighting with flows. Use Repeat.' on black with line-drawn packs and a lime footer.
Preserve (3-5 traits): line-drawn product packs; lime and black; caps headings; phone UI cards; notification tags.
Borrow only (1-2): Draw the customer's products as floating line art
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: line drawings, UI
Reject: Many similar panels
Token commitments: palette #EBE7E2, #C5C5BC, #FFFFFF, #5D4643, #F4FC85; type Mabry; engine GSAP + Lenis linked (never vendored).
