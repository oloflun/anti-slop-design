---
title: "Gen Z Broke The Funnel - Vogue Business x Archrival"
url: http://vogue.com/article/gen-z-broke-the-marketing-funnel-part-ii-what-now
source_url: http://vogue.com/article/gen-z-broke-the-marketing-funnel-part-ii-what-now
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "consumer-brand"
family: scrollytelling-report-pixel-flowers
dna: "Vogue Business research report x highlighted phrases, cut-out products and pixel flowers"
register: editorial print
grammar: chaptered editorial
lane: "A long research report: a loader with a face, cut-out clothes on a pink gradient, 'Shopping isn't fun anymore' in a blue highlight over a photo, then essay text with highlighted phrases, products floating past, survey questions with answers built as pixel bar charts, 'The rise of doomshopping', 'Gen Z craves the chase', retail vs social media splits and pixel flower decorations throughout."
mode: read
traits: ["phrases highlighted in blue, green and lilac", "cut-out product photos floating", "pixel bar charts", "pixel flower ornaments", "italic script mixed with mono", "soft gradient grounds"]
palette: ["#FCFAF6", "#E4D1F4", "#BCA8CD"]
type: ["fontAgaramondPro", "fontVogueAvantGarde", "fontAlicentHightower", "fontDidot"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

It turns a survey into a magazine feature: every statistic is a moment (a bar chart, a floating product, a highlighted phrase) and the pixel motif ties data and decoration together.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Noomo Agency).

## What to borrow (principle)

- Build data bars from the same pixel motif as the ornaments
- Highlight key phrases like a marker as you read

## What to leave

- Very long page
- Small body text

## Signature move

Survey answers drawn as pixel bar charts beside floating cut-out products.

## Motion

Intro: cream with a small face loader (~2 s). Wheel (Lenis light ~15 px glide, 6 pins): clothes float in on the gradient; the headline highlight sweeps behind words; highlights paint in as paragraphs reach mid-screen; products drift across; pixel bars fill to their percentages; title sections pin while the ground colour shifts.

Measured (`motion/probe.json`): GSAP 3.13.0; 6 pinned sections; Lenis; WebGL canvas x1 (three.js); split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a long research report: a loader with a face, cut-out clothes on a pink gradient, 'Shopping isn't fun anymore' in a blue highlight over a photo, then essay text with highlighted phrases, products floating past, survey questions with answers built as pixel bar charts, 'The rise of doomshopping', 'Gen Z craves the chase', retail vs social media splits and pixel flower decorations throughout. Type: fontAgaramondPro, fontVogueAvantGarde, fontAlicentHightower, fontDidot.
Ground and ink from the measured palette (#FCFAF6, #E4D1F4, #BCA8CD). Motion carries the page through
survey answers drawn as pixel bar charts beside floating cut-out products. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion cut-outs, editorial photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion cut-outs, editorial photography

## Reference lock

Primary reference/direction: Gen Z Broke The Funnel - Vogue Business x Archrival — A long research report: a loader with a face, cut-out clothes on a pink gradient, 'Shopping isn't fun anymore' in a blue highlight over a photo, then essay text with highlighted phrases, products floating past, survey questions with answers built as pixel bar charts, 'The rise of doomshopping', 'Gen Z craves the chase', retail vs social media splits and pixel flower decorations throughout.
Preserve (3-5 traits): phrases highlighted in blue, green and lilac; cut-out product photos floating; pixel bar charts; pixel flower ornaments; italic script mixed with mono.
Borrow only (1-2): Build data bars from the same pixel motif as the ornaments; Highlight key phrases like a marker as you read
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion cut-outs, editorial photography
Reject: Very long page; Small body text
Token commitments: palette #FCFAF6, #E4D1F4, #BCA8CD; type fontAgaramondPro, fontVogueAvantGarde, fontAlicentHightower, fontDidot; engine GSAP + Lenis linked (never vendored).
