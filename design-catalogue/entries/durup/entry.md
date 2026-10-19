---
title: "Studio Durup - textiles and interiors"
url: https://www.durup.com/
source_url: https://www.durup.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "editorial"
family: textile-studio-editorial-white
dna: "Textile and interior studio x thin serif caps and photos sliding into a white page"
register: editorial print
grammar: chaptered editorial
lane: "A textile studio: an orange-to-grey blur that clears into an interior with a vase, 'DURUP / Pioneering a new way of working with textiles' in thin serif caps, a quote ''Dress your home as you would dress yourself' - Nicoline Durup' beside a photo of a woman in a checked dress on a staircase, a white page where photos (a woman in yellow outside a shop, a vase on curtains) slide in from the sides with blur, 'Book an appointment' with a minimal form, and a full-bleed close-up of striped curtains as the footer."
mode: persuade
traits: ["thin serif caps", "blur-to-sharp photos", "photos sliding in from the edges", "white space", "dark red button", "fabric close-up footer"]
palette: ["#FFFFFF", "#645046", "#5A382B", "#352119", "#B59B8A", "#817165"]
type: ["IvyPresto Disp Lt", "Futura PT Book", "Futura PT Light", "Termina Demi"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Photos entering through motion blur feel like fabric moving; the quote makes the founder's idea the brand.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Bring photos in from the edge through motion blur

## What to leave

- Thin serif small sizes

## Signature move

'Dress your home as you would dress yourself' beside a woman in a checked dress.

## Motion

Intro: an orange blur clears into the interior (~2 s), the serif lines reveal. Wheel (Lenis): the quote section slides over; photos enter from the edges with blur and settle; the form fades in; the curtain close-up rises as the footer.

Measured (`motion/probe.json`): GSAP 3.12.5; split text; entry gate: Discover our studio →READ READ. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a textile studio: an orange-to-grey blur that clears into an interior with a vase, 'DURUP / Pioneering a new way of working with textiles' in thin serif caps, a quote '"Dress your home as you would dress yourself" - Nicoline Durup' beside a photo of a woman in a checked dress on a staircase, a white page where photos (a woman in yellow outside a shop, a vase on curtains) slide in from the sides with blur, 'Book an appointment' with a minimal form, and a full-bleed close-up of striped curtains as the footer. Type: IvyPresto Disp Lt, Futura PT Book, Futura PT Light, Termina Demi.
Ground and ink from the measured palette (#FFFFFF, #645046, #5A382B). Motion carries the page through
'Dress your home as you would dress yourself' beside a woman in a checked dress. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior and fashion photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior and fashion photography

## Reference lock

Primary reference/direction: Studio Durup - textiles and interiors — A textile studio: an orange-to-grey blur that clears into an interior with a vase, 'DURUP / Pioneering a new way of working with textiles' in thin serif caps, a quote '"Dress your home as you would dress yourself" - Nicoline Durup' beside a photo of a woman in a checked dress on a staircase, a white page where photos (a woman in yellow outside a shop, a vase on curtains) slide in from the sides with blur, 'Book an appointment' with a minimal form, and a full-bleed close-up of striped curtains as the footer.
Preserve (3-5 traits): thin serif caps; blur-to-sharp photos; photos sliding in from the edges; white space; dark red button.
Borrow only (1-2): Bring photos in from the edge through motion blur
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior and fashion photography
Reject: Thin serif small sizes
Token commitments: palette #FFFFFF, #645046, #5A382B, #352119, #B59B8A, #817165; type IvyPresto Disp Lt, Futura PT Book, Futura PT Light, Termina Demi; engine GSAP + Lenis linked (never vendored).
