---
title: "Hyperborea"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/hyperborea.html
captured: 2026-09-03
family: nordic-solstice
dna: "Conference poster x observatory diagram"
register: illustrated dark
grammar: chaptered editorial
lane: "Midnight-blue conference page lit by one amber sun that recurs as hero disc, drawn speaker portraits and a sundial diagram, running through day columns, a ruled ticket table and a letter-not-a-form close"
mode: persuade
traits: ["midnight blue ground", "single amber light source", "Italiana display", "Archivo micro-caps", "code-native SVG portraits", "day-column programme", "ruled ticket tiers with kr prices", "speaker name marquee", "kanji subtitle pairs"]
palette: ["#020916", "#0E1927", "#202A36", "#F2EADE", "#DDD3C4", "#FFA23D", "#C8682C", "#B3222A"]
type: ["Italiana", "Archivo", "Noto Serif JP"]
kind: example
source: claude
origin: example-site
extract: none
category: institutional
category2: "editorial"
status: ready
---

## Why it works

The whole page is lit by one light. An amber disc sits behind the headline, and
every subsequent illustration is a variation on it: a circled sun in an orbit, a
sun setting behind a curve, two mountains, a fourteen-metre sundial. Nothing else
on the page is warm. Because the light source is single and consistent, a
midnight-blue page with no photography still reads as a place, not as a template.

Italiana — a high-contrast didone display face — is used only in large sizes, where
its hairlines survive; Archivo, a plain grotesque, takes every size below about
18px. This is the correct division for a face like Italiana, and the page never
cheats it: there is not one line of Italiana at caption size, and not one headline
in Archivo.

The programme is three day columns, deliberately unaligned — Day 01 sits high, Day
02 lower, Day 03 lower still, each under its own rule. The stagger reads as three
days descending rather than as a table of three equal cells, and it makes the whole
programme legible in one glance without any timeline chrome.

The speakers are not photographed. Each gets a small drawn panel — a sun in an
orbit, two triangles, a horizon — built from flat shapes in the same amber, rust
and slate. It sidesteps the mismatched-headshot problem that ruins most conference
pages, and it costs nothing to add a speaker.

The ticket tiers are set as ruled ledger rows: name, seat count and condition in
micro-caps, price at the right in Italiana. `0 kr · SEK · FUNDED` for the bursary
row is the most persuasive line on the page, precisely because it uses the same
format as the paid rows instead of being dressed up as a badge.

## What to borrow (principle)

- **One light source, repeated.** Pick a single warm accent, give it a physical
  identity (here: a sun), and let every illustration be a restatement of it. A dark
  page with one consistent light needs no gradients and no second colour.
- **Split the type by size, not by section.** A high-contrast display face above a
  size threshold, a plain grotesque below it, with no exceptions in either
  direction.
- **Stagger parallel columns.** Three descending columns say "three days" better
  than three aligned boxes.
- **Draw the people.** Flat geometric panels in the page's own palette beat mixed
  headshots, and they scale to any number of speakers.
- **Put the free tier in the same table as the paid ones.** `0 kr` in the price
  column, with the same rule above and the same micro-caps condition, sells harder
  than any callout.

## What to leave

- The hero copy collides at 1440×900: the lede paragraph overlaps the `WHERE
  Studieshuset / Helgonavägen 3` block. Two absolutely-placed blocks in the same
  region with no reserved space — give the hero a real grid row.
- The 70-second infinite name marquee. It never stops, it says nothing a static
  row of names would not, and it is a permanently animating layer behind every
  scroll.
- The blanket reveal on `section, h1, h2, h3, article, li, blockquote, figure` at
  1.4s. On a page with a sixteen-item speaker grid that is sixteen staggered fades
  the reader must wait out.
- The fixed `mix-blend-mode: screen` overlay at 0.35 — it lifts the blacks of a
  page whose whole argument is a dark room with one light in it.
- The 18-second looping "rise" animation on the hero sun. The sun is a good idea
  standing still; breathing it makes it decorative.

## Signature move

Speakers as drawn panels. Every speaker gets a flat SVG built from the same four
shapes — circle, triangle, arc, dot — in the page's amber, rust and slate, with the
name in Italiana and the role and city in Archivo micro-caps beneath. The page
gains a consistent portrait gallery that no photo commission could match for
coherence, and the illustration budget is a few dozen lines of markup.

## Brief

Build a midnight-blue conference page (`#020916` ground, `#0E1927` panels) lit by a
single amber `#FFA23D`. Open with an oversized Italiana headline whose last word is
amber, a Japanese subtitle line beneath it in the same amber, and a large amber sun
disc bleeding off the right edge. Set every display line in Italiana and everything
under 18px in Archivo with 0.14em tracking — never cross them. Run a top status bar
with edition, tagline and dates in micro-caps. Lay the programme out as three
descending day columns, each with a rule above it, an amber day number, an English
title, a Japanese title and one paragraph. Give every speaker a flat geometric SVG
panel drawn from circles, triangles and arcs in amber, rust `#B3222A` and slate.
Set ticket tiers as ruled rows with the price in Italiana at the right and the
bursary row priced `0 kr`. Close on a two-column contact spread split by a vertical
hairline, headline reading "Write us a letter, not a form."

## Image recipe

Flat geometric vector composition of [SUBJECT], drawn with three or four primitives
only — filled circle, triangle, thin arc, small dot — on a midnight-blue panel,
single amber light source with one rust accent, no gradients, no texture, no
outlines except a 1px amber orbit, generous empty space around the motif, motif
centred and small relative to the panel. Reads as an instrument diagram, not as an
illustration.

## Photo search

Code-native — draw in SVG, do not source photography. If a photograph is
unavoidable:
Unsplash first, Pexels second.
- "midnight sun horizon minimal"
- "nordic winter landscape dark blue"

## Reference lock

Primary reference/direction: Hyperborea — midnight-blue conference page lit by one amber sun, Italiana over Archivo, code-native geometric speaker portraits.
Preserve (3-5 traits): midnight-blue ground `#020916` with a single amber `#FFA23D` light source restated in every illustration; Italiana above 18px and Archivo below it, never crossed; three descending day columns as the programme; flat SVG panels instead of speaker photographs; ticket tiers as ruled rows with the price in Italiana at the right.
Borrow only (1-2): the English/Japanese headline pairing; the "letter, not a form" contact close.
Role rules: Italiana never sets anything under 18px; Archivo never sets a headline; amber is the only warm colour and rust `#B3222A` appears only inside illustrations; micro-caps capped at 11px and 0.14em; no photograph anywhere.
Media strategy: code-native — every image is flat SVG built from circle, triangle, arc and dot in the page palette.
Reject: infinite marquees; fixed screen-blend overlays; blanket scroll reveals across list items; looping ambient animation on the hero; gradients; stock speaker headshots.
Token commitments: night `#020916`, panel `#0E1927`, slate `#202A36`, bone `#F2EADE`, bone-dim `#DDD3C4`, amber `#FFA23D`, amber-deep `#C8682C`, rust `#B3222A`; display `Italiana`, body `Archivo`, mark `Noto Serif JP`; display size floor 18px, micro-caps tracking 0.14em, body 1rem/1.6.
