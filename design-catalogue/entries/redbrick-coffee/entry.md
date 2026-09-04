---
title: "Redbrick Coffee"
url: https://redbrick.coffee/
source_url: https://redbrick.coffee/
captured: 2026-09-04
origin: refero
extract: ok
category: consumer-brand
category2: editorial
family: scarlet-broadsheet-storefront
dna: "Weight-300 didone display serif x a single scarlet ink thread running through every UI element"
register: editorial print
grammar: chaptered editorial
lane: "A cream broadsheet page runs scarlet ink through every interactive surface — logo, nav, labels, borders, arrows — while a weight-300 serif at up to 150px commands alternating 50/50 image-and-text splits like a print magazine, never a filled button in sight"
mode: persuade
traits: ["one red for every interactive element, no second accent", "100-150px weight-300 serif, ~1.0 leading", "outlined links only, zero filled buttons", "25px card/image radius, 50px pills, 3.75px links", "alternating 50/50 image-text splits", "10px tracked-out running-head labels"]
palette: ["#e82c2a", "#212529", "#ffffff", "#f2f2f2", "#121212"]
type: ["Editorial Old", "Surt", "GTStandard-M"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Redbrick Coffee.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Brick red `#e82c2a` is treated as a single chromatic thread running
through every interactive and label element on the page — logo, nav links,
section labels, hairline rules, arrow links, the announcement bar — while body
paragraphs stay in press black and the canvas stays cream white. Because red
never appears as a filled surface (there is explicitly no filled-button style
in this system), the colour reads as ink rather than UI chrome, reinforcing the
"printed broadsheet" register the source names directly.

Type performs a two-voice split calibrated for extremes: Editorial Old at
weight 300 only, 100-150px, near-1.0 leading, is reserved exclusively for
display headlines — "never bold, never weight 400+" per the source — while
Surt carries every functional role at consistently positive, size-scaling
tracking (0.013em at 15px up to 0.06em at 10px labels), giving even the
smallest running-head text a typeset, slightly old-style character that
matches the serif's editorial mood instead of reading as generic UI.

The layout commits fully to a magazine rhythm: alternating 50/50 image-and-
text splits, each section opened by a tiny tracked-out red running head and
closed by a right-aligned arrow link, exactly mimicking a print magazine's
section markers. Elevation is banned outright — the 25px card radius and one
tonal step (white canvas to `#f2f2f2` card) do all the separation work a
shadow normally would, keeping the page reading as flat printed pages rather
than a stack of floating panels.

## What to borrow (principle)

- **Run one accent colour through every UI role simultaneously.** Using the
  same red for logo, nav, labels, borders and links — never diluted, never
  supplemented — makes a single hue carry an entire brand's interactivity.
- **Ban filled buttons entirely in favour of outlined ink.** A system with no
  filled-button style at all reads as editorial (ink on paper) rather than
  app-like (surfaces and elevation).
- **Reserve the display serif for one weight and one job only.** Locking
  Editorial Old to weight 300, display-only, prevents the "anti-convention"
  thin-weight statement from ever being diluted by a bolder variant.
- **Give tracking a consistent scaling formula, not a flat value.** Surt's
  0.013em-to-0.06em curve across sizes gives every text role its own tuned
  legibility rather than one generic letter-spacing value.
- **Structure every section with a running-head-plus-arrow-link pair.** A tiny
  tracked label at the top and a right-aligned arrow link at the same visual
  weight bookend each section like a magazine spread, giving scannable
  wayfinding without any nav chrome.

## What to leave

- Zero filled buttons anywhere is a strict commercial constraint — a checkout
  or high-urgency conversion flow may need at least one filled, unmissable
  action that this system doesn't provide a pattern for.
- Weight 300 at up to 150px depends on a genuinely well-drawn light cut of the
  display serif; a lower-quality substitute will read as broken rather than
  intentionally thin at that scale.
- A single-colour-only rule (no second accent permitted) is fragile once a
  product line grows — seasonal or limited-edition products will have no
  built-in way to differentiate without either breaking the rule or relying
  entirely on packaging photography to carry that signal.

## Signature move

The magazine running head: a tiny 10px uppercase red label with 0.06em
tracking sitting above a 1px red hairline rule, paired with a right-aligned
arrow link ("Shop blends →") at the same visual weight — a section-opener
device borrowed directly from print magazine page furniture.

## Motion

(from designlang extract) Feel reads as smooth, and the page is scroll-linked.
The system is genuinely minimal in practice, not just by omission: only two
durations are confirmed (100ms and 500ms), both riding a plain `ease` curve (8
uses), and no keyframe animations are confirmed firing anywhere. That matches
the component notes precisely — primary nav links have "no color shift" on
hover, "the only state change is opacity." (observed in capture) the live
capture confirms a static composition matching the layout and colour system
closely; given the flat, shadow-free elevation philosophy and the extract's own
minimal timing set, any further interaction state most plausibly relies on
opacity or border-weight shifts on that same 100-500ms range rather than colour
change or a keyframed reveal.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | `ease` |
| lg | 500ms | `ease` |

## Brief

Build an editorial coffee-storefront landing page. Canvas is cream white
`#ffffff`; press black `#212529` carries body paragraphs; brick red `#e82c2a`
is the single accent, running through the logo, every nav link, section
labels, hairline rules and arrow links — never as a filled button background,
never diluted with a second hue. Open with a full-bleed red announcement bar
above a white nav strip, then a 50/50 hero split: a weight-300 Editorial Old
headline at 100-150px, ~1.0 leading, in red on the text side, paired with a
25px-radius lifestyle photograph on the other. Alternate 50/50 image-and-text
splits down the page, each opened by a 10px uppercase red running-head label
above a hairline rule and closed by a right-aligned arrow link at the same
size. Product cards sit on `#f2f2f2` surfaces at 25px radius with no shadow;
every interactive element is either a 1px outlined red pill (50px radius for
buttons/inputs, 3.75px for inline links) or plain red text — never a solid
fill. Keep Surt's positive tracking scaling with size throughout, and close on
a dark `#121212` footer panel.

## Image recipe

Warm overhead or waist-level lifestyle photograph of [SUBJECT] — coffee,
pastries or brewing equipment styled on a wooden table with books or magazines
in frame, natural warm light, tightly cropped to feel like a magazine spread
rather than a product catalog shot, no white-cyc studio background, no posed
model shots.

## Photo search

Unsplash first, Pexels second.
- "coffee wooden table overhead warm light"
- "espresso cup croissant cafe table"
- "coffee brewing equipment lifestyle"
- "open book coffee cup warm tone"

## Reference lock

Primary reference/direction: Redbrick Coffee — scarlet-ink editorial coffee
storefront, weight-300 display serif, zero filled buttons.
Preserve (3-5 traits): cream white canvas with press black body text; brick
red `#e82c2a` as the sole accent across logo, nav, labels, borders and links,
never a second hue; Editorial Old locked to weight 300, display-only, never
bolder; zero filled buttons anywhere — every action is outlined red or plain
red text; alternating 50/50 image-and-text section splits, each with a
running-head label and arrow-link pair.
Borrow only (1-2): the magazine running-head-plus-arrow-link section-opener
pattern; the 10px GTStandard-M micro-label treatment for the announcement bar.
Role rules: red never fills a large surface or a button background outside
the announcement bar; the display serif never sets body copy or drops below
100px; body text is never centred in a narrow column.
Media strategy: photo:unsplash — warm overhead lifestyle photography with
wooden surfaces, books and hands; no studio white-cyc product shots.
Reject: any filled (solid-background) button; bold or heavier weight on
Editorial Old; a second accent colour; drop shadows on cards or images;
centred display headlines in narrow columns.
Token commitments: bg `#ffffff`, card `#f2f2f2`, dark `#121212`, ink `#212529`,
accent `#e82c2a`; display Editorial Old 300 at 100-150px/leading 0.99-1.2;
body Surt 400 at 15-35px with 0.013-0.04em tracking; label 10px/0.06em
tracking; radius 25px cards/images, 50px pills, 3.75px inline links; section
gap 50px, card padding 30px.
