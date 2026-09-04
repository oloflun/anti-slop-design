---
title: "Groupe Montoni"
url: https://groupemontoni.com
source_url: https://groupemontoni.com
captured: 2026-09-04
origin: raw-url
extract: ok
category: institutional
category2: portfolio
family: aerial-drone-wordmark
dna: "Live aerial drone footage x centred serif wordmark, live inventory counters"
register: cinematic dark
grammar: filmic one-shot
lane: "A full-bleed aerial drone video of the firm's own developments carries a huge centred serif wordmark and live space/careers counters, then the page runs a dark grid of project cards and a multicolour ESG-claim mosaic"
mode: persuade
traits: ["full-bleed aerial drone video hero", "centred serif wordmark over footage", "live inventory counters in nav (spaces/careers)", "dark project card grid with caption overlays", "multicolour ESG claim tile mosaic", "bilingual FR/EN toggle", "editorial serif for stat claims"]
palette: ["#EFEEE1", "#0D0D0D", "#B99C6A", "#123F4E", "#BFBDB9", "#717372", "#3D3533", "#A39F9D"]
type: ["fkroman", "studiopro"]
measured: designlang
kind: reference-style
source: claude
status: ready
raw: raw/f355e7d3d75b87c5-groupemontoni-com.webp
---

## Why it works

The hero is drone footage of the developer's own real estate, not stock
aerial photography — the two captures taken weeks apart show completely
different seasons (autumn foliage vs. snow cover) over the same buildings,
confirming this is either live/rotating footage of actual sites or a
frequently refreshed asset either way, it is the company's real portfolio
shown at city scale. A single-weight serif wordmark, MONTONI, sits centred
and large directly on the footage with no background treatment, legible
purely because the display size and letter-spacing exceed the busiest parts
of the image below it. The nav carries live counters — "Available spaces 31,"
"Careers 12" — turning what could be static menu items into a real-time signal
that the business is active.

Below the fold, dark full-bleed project cards use a consistent caption
pattern: project name, one-line description, and a text link, layered over
photography with a soft dark gradient at the bottom edge only — enough for
legibility without an overlay across the whole image. Further down, the ESG
section breaks into a tiled mosaic of flat colour panels (cream, forest green,
deep teal, olive, stone), each carrying one concrete, numbered claim ("Over
35% reduction in energy costs...", "The first company to construct a LEED®
Gold-certified industrial building in Québec") set in the same serif as the
wordmark. Claims are specific and sourced (a footnote citation appears under
the energy-cost claim), which is the opposite of Areto's unattributed
percentage stats — the same visual pattern, done with real substance behind
it.

The extract shows the page's true ground colour is a warm cream (`#efeee1`,
by far the most-used colour on the page) rather than pure white or near-black,
with a muted gold (`#b99c6a`) and deep teal (`#123f4e`) doing quiet accent
work in text and borders — the ink-on-photography read above holds, but the
resting state of the page is warmer and more coloured than a black/white
read would suggest.

## What to borrow (principle)

- **Use real drone/aerial footage of the company's own assets for the hero**,
  not stock — it's a stronger authority signal than any photography a stock
  library could offer, and it's honest.
- **Put a live operational number in the nav** (open positions, available
  inventory) to signal an active business without a dedicated "About" claim.
- **Cite the source next to every stat claim** ("*for LEED®-certified
  buildings") — turns a persuasive number into a credible one.
- **Tile ESG/values claims as flat colour panels of varying hue**, one claim
  per panel, rather than a uniform icon-plus-text list — the colour variation
  keeps a normally dry section visually alive.
- **Layer only a soft bottom-edge gradient on photographic cards**, not a
  full-image overlay, to keep captions legible while preserving photo clarity.

## What to leave

- A wordmark set directly on drone footage depends on there being enough open
  sky/rooftop in the frame at the point of capture — this composition is
  fragile if the footage changes.
- The multicolour ESG mosaic uses five distinct hues in one section; without
  the shared serif and consistent card proportions holding it together, this
  many colours in one view could read as scattered rather than intentional.

## Signature move

Live inventory counters built directly into the primary navigation —
"Available spaces 31," "Careers 12" — turning menu items into real-time proof
that the business is operating at the scale its drone footage implies.

## Motion

(from designlang extract) The extract rates overall feel "mixed" with
confirmed scroll-linked behaviour. Duration steps run from 150ms up to a full
1000ms, split between a dominant standard-material custom ease
(`cubic-bezier(0.4, 0, 0.2, 1)`, 18 uses) and a slower ease-out
(`cubic-bezier(0.19, 1, 0.22, 1)`, 5 uses) for larger transforms. Three
keyframes are defined: horizontal and vertical marquee loops (each a
continuous `translate`/`translateY` to `-100% - gap`) and a `spin` rotator.
The horizontal marquee is a plausible mechanism for a scrolling brand/logo
strip or the live counter display; the vertical variant suggests at least one
section scrolls content continuously rather than on a fixed reveal.
(observed in capture) The hero is confirmed to be video or a rotating
asset — raw and fresh captures of the same wordmark placement show entirely
different seasons over the same buildings. Live counter values also differ
between captures (28→31 spaces, 15→12 careers), confirming the nav numbers
are real-time/frequently updated data, not static copy.

| kind | tokens |
|---|---|
| durations | xs 150ms · lg 500ms · xl 1000ms |
| easings | custom `cubic-bezier(0.4, 0, 0.2, 1)` (18×) · ease-out `cubic-bezier(0.19, 1, 0.22, 1)` (5×) · linear (2×) |
| keyframes | marquee (horizontal) · marqueeVertical · spin |

## Brief

Build an institutional real-estate/developer site on full-bleed aerial or
drone footage of the company's actual portfolio, with a single large serif
wordmark set centred directly on the footage — no scrim needed if the frame
has enough open ground/sky. Put one or two live operational numbers (open
positions, available inventory) directly in the primary nav rather than
burying them in a stats section. Below the fold, run a dark grid of project
cards with a soft bottom-edge gradient only (not a full overlay) under
caption text. For a values/ESG section, tile concrete, sourced claims as flat
colour panels in varying hues, one claim per panel, in the same serif as the
wordmark — always cite the basis for any percentage or superlative claim.

## Image recipe

Aerial drone photograph or video of [SUBJECT] — a real estate development or
industrial/commercial property — shot from directly overhead or at a steep
oblique angle, natural daylight appropriate to the season, enough open
rooftop/ground/sky area to place large centred type without obscuring
architectural detail, real (not rendered) footage of an actual asset.

## Photo search

Unsplash first, Pexels second.
- "aerial drone industrial building rooftop"
- "aerial view commercial real estate development"
- "drone shot city development winter"
- "office lobby corporate walking candid"

## Reference lock

Primary reference/direction: Groupe Montoni — aerial drone hero with centred
wordmark, live nav counters, sourced ESG claim mosaic.
Preserve (3-5 traits): full-bleed real aerial/drone footage of the company's
own assets carrying a centred serif wordmark with no scrim; one or two live
operational numbers built into the primary nav; project cards with a
soft bottom-edge-only gradient under captions, never a full-image overlay;
ESG/values claims tiled as flat colour panels, one claim per panel, always
citing their basis; one serif for wordmark and all stat/claim copy.
Borrow only (1-2): the bilingual FR/EN nav toggle; the hamburger "Menu" label
paired with text rather than an icon alone.
Role rules: any percentage or superlative claim must carry a source citation
in the same section; the wordmark is set on photography/footage only, never
on a flat panel.
Media strategy: aerial/drone footage of real, owned assets for the hero and
project cards; documentary (not posed) photography for people/culture
sections.
Reject: unsourced percentage stats; a full-image dark overlay across
photographic cards; stock aerial photography in place of real asset footage.
Token commitments: ink `#0D0D0D`, stone `#BFBDB9`, stone-mid `#717372`,
ink-soft `#3D3533`, paper `#E2E2D6`, stone-light `#A39F9D`; display/stat serif
"fkroman", body/UI "studiopro".
