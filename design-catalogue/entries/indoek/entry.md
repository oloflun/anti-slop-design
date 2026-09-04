---
title: "Indoek"
url: https://indoek.com
source_url: https://indoek.com
captured: 2026-09-04
origin: raw-url
raw: raw/106f570fb1dea605-indoek-com.webp
extract: ok
category: editorial
category2: "consumer-brand"
family: cobalt-surf-wordmark
dna: "Surf shop signage x gallery wordmark poster"
register: warm photographic
grammar: typographic poster
lane: "A cobalt outline wordmark fills the fold with a product photo windowed through its middle, then drops straight into a ruled shop/gallery grid — cream ground and one blue ink throughout"
mode: experience
traits: ["cream ground", "single cobalt-blue ink", "oversized outline wordmark", "photo windowed through headline letters", "surf-shop product photography", "ruled product grid", "no serif anywhere", "gallery + shop in one nav"]
palette: ["#EEEBE3", "#03315C", "#1B58A0", "#7294B0", "#B3C7D2", "#96775C"]
type: ["Calibre"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
---

## Why it works

The entire page runs on one typeface and one ink colour. Calibre, a plain grotesque, sets
the giant outline wordmark, the nav, the body copy and the price tags identically — there
is no display/body split at all. What creates hierarchy instead is pure scale: the
wordmark is set at a size that breaks the viewport, everything else sits at conservative
reading size, and the jump between the two is the entire type system. Cobalt blue
(`#03315C`–`#1B58A0`) is the only ink on cream; it never competes with the product
photography because nothing else is coloured.

The hero repeats Indoek's own version of the windowed-photo device seen elsewhere in this
set (compare theequityfund.org): a single product or gallery photograph sits inside the
counters of the wordmark, so the giant letters frame real merchandise rather than floating
as empty branding. Because the photo changes (surf shack interior, gallery opening, a
craftsman at work) while the wordmark stays fixed, the hero can rotate content without
ever needing a second layout.

Below the fold the page drops immediately into a ruled, ungapped product/gallery grid —
books, prints, editorial features — with the same blue ink and the same Calibre labels.
The lack of a second visual register (no card shadows, no rounded corners, no accent) is
what lets a shop, a gallery and a magazine share one page without feeling like three
different sites stitched together.

The copy voice stays third-person throughout rather than addressing the reader as "we,"
which matches the gallery/catalog distance of the layout more than a typical direct-address
commerce voice (from designlang extract).

## What to borrow (principle)

- **One typeface, hierarchy by scale alone.** Skipping a display/body split entirely and
  using size as the only lever keeps the whole system legible and fast to extend.
- **Window content through the wordmark, not beside it.** A hero photo inset into the
  counters of oversized outline letters gets an image and a logo lockup in one move.
- **One ink colour, unlimited photography.** Restricting the palette to a single blue lets
  product and editorial photography carry all the colour variation.
- **Let commerce and editorial share the same grid.** Shop items and gallery features in
  identical ruled cells read as one coherent publication, not a store bolted onto a blog.

## What to leave

- The wordmark's photo window can clip mid-word depending on image aspect ratio (visible
  in both captures, different crops) — needs a locked mask ratio so the letterforms never
  read as broken.
- Long, information-dense hero copy set at the same weight as the wordmark's surrounding
  text ("CELEBRATING COASTAL CREATIVE CULTURE") competes with the product photo for the
  same visual band; a size step down would separate them more cleanly.
- Outline-only letterforms at this scale rely entirely on screen anti-aliasing for
  crispness; thin strokes shimmer at in-between browser zoom levels.

## Signature move

The photo-windowed wordmark: a real product or gallery photograph is masked into the open
counters of the giant "INDOEK" outline type, so the logo and the hero image are the same
object rather than stacked elements — and because the wordmark's outline weight is
constant, any photo can rotate through it without a redesign.

## Motion

Feel reads as mixed and the page is marked scroll-linked, but almost nothing here is
bespoke: the only keyframes present in the DOM are Shopify/Swiper platform boilerplate — a
checkout-skeleton opacity pulse, a cart-icon rotator, a dash-offset "drawing" loader, and
two generic spin loops for carousel/checkout preloaders — none of which the extract curates
as identity-bearing motion. Hover and link-state transitions run short, 150-300ms, on two
easing families: a standard decelerate `cubic-bezier(0.4,0,0.2,1)` for colour/border/fill
changes, and the browser-default `ease` for a couple of max-height/background-size moves.
This confirms what the compositional signature move already implies: Indoek's identity
device is the photo-windowed wordmark, not a timed animation, so the hero reads as a static
or simple-crossfade rotation rather than a choreographed sequence (from designlang
extract).

| token | value | used for |
|---|---|---|
| xs | 150ms | link/colour/border/fill hover states |
| md | 300ms | background-size, max-height moves |
| ease (custom) | `cubic-bezier(0.4,0,0.2,1)` | colour/border/fill/opacity/transform hovers |
| ease (browser) | `ease` | max-height, background-size transitions |

## Brief

Build a single-typeface commerce-and-gallery page for a coastal creative brand. Ground
everything in warm cream with one cobalt-blue ink; use no second colour and no second
typeface. Open on an oversized outline wordmark sized to break the viewport, with a
rotating product or gallery photograph masked into its open counters, plus one line of
mission copy and a caption line beneath. Set nav, captions, prices and body copy in the
same grotesque at conservative reading size — hierarchy comes from scale jumps only, never
from a second face or weight family. Below the fold, run shop and gallery items in one
ruled, ungapped grid with no card shadows or rounded corners. Keep photography as the only
source of colour variation on the page.

## Image recipe

Documentary lifestyle photograph of [SUBJECT] — a surf shack interior, a craft studio, a
gallery opening — shot in warm natural daylight, true-to-life colour (not desaturated),
handmade objects and real texture in frame (wood, ceramic, textile), composed with a clear
open band through the centre so it can be masked into large outline letterforms without
losing legibility.

## Photo search

Unsplash first, Pexels second.
- "surf shack interior wood shelves"
- "ceramic studio craftsman daylight"
- "coastal gallery opening warm light"
- "surfboard shop pegboard display"

## Reference lock

Primary reference/direction: Indoek — cobalt single-ink surf/gallery wordmark, photo
windowed through oversized outline type, one grotesque for everything.
Preserve (3-5 traits): cream ground with a single cobalt ink, no second accent colour; one
grotesque typeface for wordmark, nav, body and prices, hierarchy by scale only; a hero
photograph masked into the open counters of the giant wordmark; commerce and editorial
content sharing one ruled, ungapped grid with no card chrome.
Borrow only (1-2): the arrow-plus-caption link style under hero images; the rotating
featured-item strip directly beneath the hero.
Role rules: no second typeface is ever introduced, including for prices or labels; blue is
the only ink — photography carries all other colour; the wordmark is always photo-
windowed, never shown as flat solid type on the homepage.
Media strategy: photo:unsplash — warm, true-colour lifestyle/craft photography with a
clear open band for letterform masking; never desaturated or heavily graded.
Reject: a second typeface for any role; rounded corners or drop shadows on grid cells;
flat (non-windowed) wordmark treatment; a second accent colour; centred hero copy.
Token commitments: bg `#EEEBE3`, ink `#03315C`, ink-mid `#1B58A0`, ink-tint `#7294B0`,
ink-pale `#B3C7D2`, wood-accent (photography only) `#96775C`; type `Calibre` for every
role; wordmark set at viewport-breaking scale, all other text at one conservative reading
size; grid ruled, zero card radius, zero shadow.
