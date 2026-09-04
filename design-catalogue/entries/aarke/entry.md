---
title: "Aarke"
url: https://aarke.com
source_url: https://aarke.com
captured: 2026-09-04
origin: raw-url
extract: ok
category: luxury-craft
category2: "consumer-brand"
family: monospace-kitchen-editorial
dna: "Warm in-situ product photography x typewriter-monospace campaign headlines"
register: warm photographic
grammar: gallery/catalog
lane: "A full-bleed styled kitchen photograph carries a monospace campaign headline over one hero product, then the page runs a plain grotesque product grid before returning to monospace for a two-up lifestyle gallery and an editorial mission statement"
mode: persuade
traits: ["typewriter-monospace campaign headlines", "plain grotesque wordmark and UI", "warm in-situ kitchen/counter photography", "outline pill CTA button", "two-up split lifestyle photo gallery", "on-image product name tags", "steel/matte product finishes", "promo utility bar (shipping/Klarna)"]
palette: ["#FFFFFF", "#000000", "#3C3C3C", "#EFEFEF", "#ADADAD", "#101010", "#7E6247", "#2C190C"]
type: ["monospace (campaign/editorial headlines)", "grotesque sans (wordmark/UI/body)"]
measured: designlang (font names unresolved in extract — generic "Body Font"/"Heading Font" labels only; role split confirmed, palette corrected)
kind: reference-style
source: claude
status: ready
raw: raw/ffe49833120f8500-aarke-com.webp
---

## Why it works

The hero is one warm, styled photograph of the product in a real kitchen
setting (wood cabinetry, natural counter light, a bowl of pears) rather than a
studio cutout — the product looks lived-with, not merely photographed. Over
it, the campaign headline "The new drip" is set in a monospace/typewriter
face, a deliberate departure from the clean grotesque used for the wordmark
and every UI element (nav, prices, buttons). That contrast recurs later at
"Everyday Engineering," confirming the monospace isn't a one-off hero
treatment but the brand's consistent voice for editorial/campaign statements,
while the grotesque stays reserved for wordmark, navigation and commerce.

The product grid below is almost aggressively plain — white ground, product
photography on white, name/price/description in small grotesque type, arrow
carousel controls — letting the hero's warmth and the monospace headline be
the only "designed" moments on an otherwise catalogue-standard shop layout.
Further down, a two-up split gallery pairs two products in two different
lifestyle settings (a cool marble counter, a warm wood counter with food
styling) side by side, each labelled with a simple on-image name tag rather
than a caption block — letting the photography's own warm/cool contrast do
the differentiation work between products.

## What to borrow (principle)

- **Reserve a second typeface (here, monospace) exclusively for
  editorial/campaign headlines**, never for UI or commerce copy — the split
  gives the brand a distinct "voice" moment without touching functional type.
- **Photograph hero products in situ, styled with unrelated but thematically
  consistent objects** (fruit, food, natural materials) rather than isolated
  on a plain background — it reads as lifestyle, not spec sheet.
- **Keep the commerce grid catalogue-plain** (white ground, small type, no
  extra ornament) so any editorial styling elsewhere reads as considered
  rather than diluted across the whole site.
- **Pair two products in contrasting lighting/material settings side by side**
  to let photography, not copy, carry the comparison.

## What to leave

- The promo utility bar (shipping/Klarna) at the very top competes with the
  wordmark for the first thing a visitor reads — standard e-commerce
  necessity, but worth noting it's the actual first line on the page.
- A live chat bubble sits fixed bottom-right across every section, a
  functional necessity that adds visual noise to otherwise very clean
  photography-led sections.

## Signature move

A typewriter-monospace face reserved exclusively for campaign and editorial
headlines, kept completely separate from the grotesque used everywhere
else — a two-typeface system where the split marks "brand speaking" versus
"store functioning."

## Motion

(from designlang extract) The extract rates overall feel "smooth" with
confirmed scroll-linked behaviour. Five duration steps span 100ms to 800ms,
dominated by a plain `ease-in-out` (`ease`, 143 uses) with a lighter ease-out
(27 uses) and two more dramatic custom curves (28 uses combined, including
`cubic-bezier(0.86, 0, 0.07, 1)`, a near-stepped ease-in-out) reserved for
less frequent moves. Three keyframes are confirmed in use: `movingText`, a
horizontal slide — plausibly the mechanism carrying the monospace campaign
headline or an on-image name tag into place; `slideOut` and
`msSelectboxSlideOut`, both vertical slide+fade combinations, read as
dropdown/selector close states rather than hero or gallery motion.
`shopify-rotator` and `shopify-dash` (a rotating stroke-dashoffset ring) are
Shopify's own loading-spinner keyframes, confirming the storefront runs on
Shopify rather than bespoke tooling. (inferred from image) The hero
photograph differs between the raw and fresh captures (different product,
different styling, same "Shop now" CTA position and monospace headline
treatment), indicating a rotating/seasonal hero campaign. A carousel with
left/right arrow controls is visible under the "Most popular" product row,
confirming horizontal scroll/swipe interaction on that section.

| kind | tokens |
|---|---|
| durations | xs 100ms · sm 200ms · md 300ms · lg 500ms · xl 800ms |
| easings | ease-in-out `ease` (143×, dominant) · ease-out `cubic-bezier(0.215, 0.61, 0.355, 1)` (27×) · custom `cubic-bezier(0.86, 0, 0.07, 1)` / `cubic-bezier(0.37, 0, 0, 1)` (28×) |
| keyframes in use | `movingText` (slide-x) · `slideOut` · `msSelectboxSlideOut` |

## Brief

Build a design-forward kitchenware/homeware brand on warm, in-situ lifestyle
photography for the hero — real counters, real natural light, incidental
styling objects (fruit, food, textiles) around the product rather than a
plain studio background. Reserve one monospace/typewriter face exclusively
for campaign and editorial headlines, keeping a plain grotesque for the
wordmark, navigation, prices and all commerce copy — never mix the two roles.
Keep the product grid itself catalogue-plain: white ground, small grotesque
labels, a simple arrow carousel. For a features/comparison section, pair two
products in two different lifestyle settings side by side with only a small
on-image name tag, letting the photography contrast do the comparison work.

## Image recipe

Styled lifestyle photograph of [SUBJECT] — a design object in active use on a
real kitchen counter — natural window light, warm or cool colour temperature
depending on setting, incidental food/organic styling objects nearby but not
overpowering the product, shallow depth of field, materials (steel, matte
ceramic, wood, marble) rendered with true tonal accuracy.

## Photo search

Unsplash first, Pexels second.
- "kitchen counter natural light product styled"
- "coffee maker steel kitchen morning light"
- "marble counter minimal styling natural"
- "wood counter food styling warm light"

## Reference lock

Primary reference/direction: Aarke — monospace campaign headlines against a
grotesque commerce system, warm in-situ product photography.
Preserve (3-5 traits): monospace/typewriter face reserved exclusively for
editorial and campaign headlines, never for UI or commerce; plain grotesque
for wordmark, nav, prices and body copy; hero and feature photography always
styled in situ on a real counter with incidental organic objects, never on a
plain studio background; a catalogue-plain product grid (white ground, small
type, simple carousel) as the visual "quiet zone" around styled photography.
Borrow only (1-2): the on-image product name tag (simple white label, no
extra ornament); the outline-only "Shop now" CTA button.
Role rules: monospace never appears in navigation, pricing or product-grid
copy; product-grid photography stays on plain white, styled photography stays
in situ — the two never mix within one section.
Media strategy: photo:unsplash — warm, in-situ lifestyle photography with
true material colour for hero/feature sections; plain white-background
product photography for the commerce grid.
Reject: studio-only photography for hero/feature sections; a second display
typeface beyond the monospace/grotesque pair; heavy ornament on the product
grid.
Token commitments: paper `#FFFFFF`, ink `#000000`, stone `#99968E`, wood-mid
`#7E6247`, wood-deep `#2C190C`, wood-accent `#563A26`, grey `#DEDEDD`,
grey-mid `#BDBFBB`; editorial monospace for campaign headlines, plain
grotesque for wordmark/UI/body.
