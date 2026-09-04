---
title: "NGLM"
url: https://www.nglm.com
source_url: https://www.nglm.com
captured: 2026-09-04
origin: raw-url
extract: ok
category: institutional
category2: portfolio
family: white-ground-holding-company
dna: "Manifesto-scale grotesque headline x full-bleed portfolio-brand showcase panels"
register: modern clean
grammar: gallery/catalog
lane: "A near-empty white page states one manifesto headline and a founder portrait/quote, then the page becomes a sequence of full-bleed interior photographs each carrying one portfolio brand's wordmark, closing on a plain key-figures stat row"
mode: read
traits: ["oversized centred grotesque manifesto headline", "small centred founder portrait", "pull-quote with attribution", "full-bleed brand-showcase photo panels", "brand wordmark centred over each panel", "sidebar micro-labels (Companies/Information)", "plain numeral key-figures row", "cookie consent banner"]
palette: ["#FCFCFC", "#000000", "#51585C", "#C0C3C3", "#707575", "#131516", "#8D7C68", "#AB9F90"]
type: ["GD Trio Display", "GD Gaio VF"]
measured: designlang
kind: reference-style
source: claude
status: ready
raw: raw/fce87bc763466b0b-www-nglm-com.webp
---

## Why it works

The page opens with almost nothing on it: white ground, one manifesto-scale
headline in a high-contrast grotesque ("BUILDING THE NEXT GENERATION OF DESIGN
COMPANIES") centred alone, then a small founder portrait and a short
attributed quote — no navigation clutter, no hero image competing with the
statement. For a design holding company whose product is other design
companies, stating the thesis in plain oversized type before showing any of
the portfolio is the right order of operations: establish the idea, then the
evidence.

The evidence arrives as a sequence of full-bleed interior photographs, one per
portfolio brand, each with that brand's own wordmark set centred over the
image in a light display serif — "DUSTY DECO" over a warm dining-room
photograph, and so on. Small sidebar labels ("Companies," "Information") sit
at the panel's edges in tiny caps, functioning as museum wall-text rather than
UI chrome. This turns the portfolio section into something closer to a
gallery walk-through than a logo grid — each brand gets full-bleed
photographic space and one line of description before the reader moves to the
next.

The close is almost aggressively plain: "Key Figures" as three large numerals
(7 brands, 1.8B SEK revenue, 51.2% growth) on white with small caption labels
beneath — no charts, no icons, just numbers set at headline scale. The
restraint at open and close brackets the one indulgence in the middle (the
full-bleed brand photography), giving the page a clear three-beat structure.

## What to borrow (principle)

- **State the thesis in plain oversized type before any imagery**, especially
  for a holding company or platform brand whose "product" isn't visually
  obvious.
- **Give each portfolio brand a full-bleed photographic moment with its own
  wordmark**, rather than compressing a portfolio into a logo grid — it reads
  as a gallery of real work, not a client-logo wall.
- **Use tiny sidebar labels as wall-text**, not as active navigation — they
  add context without adding visual weight.
- **Close key metrics as bare numerals at headline scale**, with no
  chart or icon — bold numbers read as more confident than any visualisation
  of the same three data points.

## What to leave

- The founder-portrait-plus-quote block, while restrained, is a common
  "trust" device in this genre and doesn't differentiate the page — it works
  here mainly because everything else is so quiet.
- Full-bleed photography for every portfolio brand is a page-length-heavy
  choice; it works for seven brands, would need reconsidering at twenty.
- The cookie consent banner sits low-contrast (dark on dark) against the hero
  in the captured state, briefly competing with the quote text above it.

## Signature move

Each portfolio brand gets one full-bleed photographic panel with its own
wordmark centred directly on the image — treating the portfolio section as a
sequence of gallery rooms rather than a logo grid or card list.

## Motion

(from designlang extract) The extract rates overall feel "mixed" with
confirmed scroll-linked behaviour. Two duration steps (300/450ms) carry a
richer set of easing curves than the page's minimal visual vocabulary would
suggest — a dominant, pronounced ease-in-out family (95 uses, including
`cubic-bezier(0.455, 0.03, 0.515, 0.955)`, close to an "ease-in-out-quint")
alongside a lighter ease-out (40 uses). Only a generic `spin` loader keyframe
is defined; the manifesto-to-gallery scroll structure appears to run on
transitions rather than bespoke keyframe choreography. The extract's
component scan also surfaces a Decline/Accept button pair — the cookie
consent banner noted in What to leave — confirming it as a real interactive
component. (inferred from image) No pinned, parallax or scroll-scrub
behaviour is otherwise evident from the fold/slice sequence; the page reads
as simple stacked full-bleed sections.

| kind | tokens |
|---|---|
| durations | md 300ms · lg 450ms |
| easings | custom `cubic-bezier(0.455, 0.03, 0.515, 0.955)` / `cubic-bezier(0.515, 0.012, 0.25, 1)` / `cubic-bezier(0.645, 0.045, 0.355, 1)` (95×) · ease-out `cubic-bezier(0.165, 0.84, 0.44, 1)` / `cubic-bezier(0.215, 0.61, 0.355, 1)` (40×) |

## Brief

Build a holding-company or platform-brand page that opens on almost nothing:
white ground, one manifesto-scale headline in a high-contrast grotesque
stating the company's thesis, centred alone with generous surrounding space.
Follow with a small founder portrait and one short attributed quote. For the
portfolio section, give each company or brand a full-bleed photographic panel
with its own wordmark set centred over the image in a light display serif,
plus a one-line description and tiny sidebar wall-text labels at the panel
edges — treat it as a gallery walk-through, not a logo grid. Close on key
metrics as bare numerals at headline scale with small caption labels beneath,
no charts or icons.

## Image recipe

Documentary interior or lifestyle photograph representing [SUBJECT] (a
portfolio brand's own product or environment), warm natural light, real
furnished space rather than a staged studio set, colour grading consistent
with the brand being shown, generous negative space at top/centre for a
wordmark to sit over without obscuring key detail.

## Photo search

Unsplash first, Pexels second (for genre reference only — each real panel
should use the actual portfolio brand's own photography).
- "scandinavian interior dining room warm light"
- "furniture design showroom natural light"
- "founder portrait environmental candid"

## Reference lock

Primary reference/direction: NGLM — manifesto-scale opening headline, gallery-
style full-bleed portfolio brand panels, bare-numeral key figures close.
Preserve (3-5 traits): a single oversized centred grotesque headline stating
the company's thesis on an otherwise empty white opening; each portfolio
brand shown as one full-bleed photographic panel with its own wordmark
centred over the image; tiny sidebar wall-text labels rather than active
in-panel navigation; key metrics closed as bare numerals at headline scale
with no chart or icon.
Borrow only (1-2): the founder-portrait-plus-quote block; the "+" expandable
nav items (Companies+, About+, Our Model+).
Role rules: portfolio wordmarks are always centred on their own photograph,
never set on a flat panel; key-figures numerals never paired with a
supporting chart or icon.
Media strategy: photo:documentary — each portfolio panel should use that
brand's own real product/interior photography, not generic stock standing in
for it.
Reject: a logo-grid or card-list treatment for the portfolio section; charts
or icon decoration on the key-figures numerals; a busy or image-heavy hero
competing with the manifesto headline.
Token commitments: paper `#FDFDFD`, ink `#000000`, warm-taupe `#8D7C68`,
ink-warm `#322219`, stone `#4D4339`, stone-light `#AB9F90`, grey `#CCCCCA`;
display "GD Trio Display", body/UI "GD Gaio VF".
