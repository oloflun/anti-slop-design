---
title: "Aevi Wellness"
url: ""
source_url: ""
captured: 2026-09-04
origin: refero
extract: none
category: consumer-brand
category2: editorial
family: nordic-apothecary
dna: "Clinical apothecary x editorial magazine spread"
register: modern clean
grammar: chaptered editorial
lane: "A full-bleed product-photo hero with the wordmark set as a giant overlay, then a strict rhythm of white and powder-blue chapters, each one a hairline-bordered card or a full-bleed image with a caption in the corner"
mode: persuade
traits: ["weight-300 headlines", "hairline borders only", "achromatic + one slate accent", "2px radii except the pill", "full-bleed overlapping product photography", "powder-blue chapter bands", "no shadows"]
palette: ["#d5e0ea", "#a3bfdb", "#231f20", "#000000", "#ffffff", "#5f6368"]
type: ["Display Sans (custom, weight 300)", "Primary Sans (custom, serif-influenced grotesque)"]
kind: reference-style
source: anton
status: ready
refero: processed/Aevi Wellness.md
---

## Why it works

Palette and type are read from Refero's extracted tokens: an almost entirely
achromatic system (near-black `#231f20` ink, white `#ffffff` surface, powder-blue
`#d5e0ea` bands) with exactly one chromatic accent, slate-blue `#a3bfdb`, reserved
for the single primary button. Everything else — cards, inputs, ghost buttons — is
capped at a 2px radius; only that one pill button is allowed the soft 60px curve.
The restriction of colour and radius to a single component each is what keeps a
skincare page from turning into wallpaper.

Type weight does the same job as colour: every size in the system, from a 10px
caption to the 54px hero display, runs at weight 300. Nothing is ever bolded for
hierarchy — hierarchy is size and line-height (1.08 on display, 1.3+ on body), not
weight. That whisper-weight type is only legible as confident because the
photography is doing the visual work it usually does: bottles and droppers overlap
edge-to-edge across full-bleed hero and category images, with captions floating in
plain white type over the bottom corner rather than sitting in a card.

Elevation is banned outright — no shadow, no glow, no blur anywhere in the system.
Depth instead comes from the alternation of white and powder-blue bands (press
strip, testimonial block) and from hairline borders in ink or powder-blue. The page
reads as a sequence of printed chapters rather than a stack of elevated UI panels,
which is exactly the "clinical-luxury" register the brand wants: nothing about the
interface competes with the product for attention.

## What to borrow (principle)

- **Spend colour on exactly one component.** A single muted accent, reserved for
  the primary action only, reads as more confident than a full accent palette.
- **Let one weight carry the whole system.** Using the same light weight at
  caption size and display size forces every other cue (size, leading, colour) to
  do the hierarchy work honestly.
- **Cap radius everywhere except one shape.** A near-flat 2px system with a single
  soft pill makes that one curve feel like punctuation, not decoration.
- **Replace shadow with band contrast.** Alternating background bands (white,
  tinted) can carry the same "section break" job a shadow usually does, without
  the cost of a blurred layer.
- **Let photography overlap its container.** Product shots that bleed past the
  card or grid line read as more editorial than photography boxed inside padding.

## What to leave

- The near-total achromatic palette risks reading as clinical-to-cold outside
  skincare/beauty; most categories need at least a second warm neutral.
- Weight-300-only typography sets a high bar for font choice and rendering —
  it fails on typefaces without a true light weight or on low-DPI displays.
- Hairline-border-only cards need genuinely high-contrast photography behind them
  to read as separated sections; on a duller image the band system collapses.

## Signature move

The wordmark set as an oversized, semi-transparent display overlay directly on top
of the hero product photograph — not a logo in a header, but a headline-scale
typographic watermark the photography shows through. It turns the brand name into
part of the image rather than a UI chrome element.

## Motion

No motion or interaction data is captured in the Refero export (components and
surfaces are described statically). Inferred from the image: the flat, hairline,
shadow-free system and the full-bleed photographic hero suggest restrained
crossfades between hero images and simple opacity reveals on section bands, rather
than parallax or scroll-scrubbed choreography — motion would be an interruption in
a system this quiet. (inferred)

## Brief

Build a clinical-editorial skincare landing page. Ground is white with powder-blue
`#d5e0ea` chapter bands; ink is warm near-black `#231f20`; the single accent is
slate-blue `#a3bfdb`, reserved for the primary CTA pill. Set every headline and
most body copy at weight 300 — caption at 10px, display at 54px, both at the same
weight, differentiated only by size and tight display leading (1.08). Cap every
radius at 2px except the primary button, which gets a 60px pill. Open on a
full-bleed product photograph with the wordmark overlaid at display scale in
translucent white. Follow with a press-logo strip on a powder-blue band, an
editorial split section (photography left, copy right), a testimonial block on
another powder-blue band, and a 3-column product-category grid where images bleed
to the card edge and captions float in the bottom corner. No shadows anywhere;
depth comes only from hairline borders and band-to-band contrast.

## Image recipe

Editorial still life of [SUBJECT] — glass or frosted-plastic apothecary bottles and
droppers, overlapping at close range, shot in soft diffused daylight with warm
highlights and cool desaturated shadow, tight crop with objects bleeding past the
frame edge, no props, no gradient backdrop, a grainy high-contrast black-and-white
treatment reserved for press or editorial inserts only.

## Photo search

Unsplash first, Pexels second.
- "skincare bottles overlapping flat lay natural light"
- "dropper bottle apothecary product close up"
- "minimal beauty product photography desaturated"
- "hand applying serum close up natural light"

## Reference lock

Primary reference/direction: Aevi Wellness — achromatic clinical-apothecary
skincare page, weight-300 type throughout, single slate-blue accent on one button.
Preserve (3-5 traits): white canvas with powder-blue `#d5e0ea` chapter bands and
near-black `#231f20` ink; weight 300 on every text size from caption to display;
2px radius on every element except the one 60px primary pill; hairline borders
(1px, ink or powder-blue) as the only structural device; full-bleed, overlapping
product photography with captions floating in plain type over the image corner.
Borrow only (1-2): the oversized translucent wordmark overlay on the hero image;
the grainy black-and-white treatment for press/editorial-only imagery.
Role rules: slate-blue `#a3bfdb` appears only on the primary button, never as text,
border or decorative fill; no shadow, glow or blur anywhere; headings never exceed
weight 300.
Media strategy: photo:unsplash — tight, overlapping product stills and natural-
light close-ups; no illustration, no 3D render, no icon-heavy decoration.
Reject: any bolded heading; any radius above 2px outside the primary button; drop
shadows or elevation cards; a second accent colour; padded/framed product images.
Token commitments: bg `#ffffff`, band `#d5e0ea`, accent `#a3bfdb`, ink `#231f20`,
ink-heavy `#000000`, mist `#5f6368`; display + body weight 300 throughout; display
leading 1.08-1.11, body leading 1.29-1.33; radius 2px default, 60px pill only;
base spacing unit 4px; page max-width 1200px, section gap 48px.
