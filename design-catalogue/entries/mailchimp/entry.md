---
title: "Mailchimp (email dashboard)"
url: ""
source_url: https://mailchimp.com
captured: 2026-09-04
origin: raw-image
extract: none
category: product-focused
category2: ""
family: sample-data-analytics-console
dna: "Email marketing analytics dashboard x sample-data disclosure banner"
register: modern clean
grammar: live surface
lane: "A white product console opens on a serif page title and a persistent sample-data disclosure banner, then rows of card-based analytics — revenue tiles, a replicate-email table, a funnel chart and a time-series line chart — fill the working canvas"
mode: operate
traits: ["white console ground", "left icon rail navigation", "serif page title beside a pill \"sample data\" tag", "persistent disclosure banner", "metric tiles with trend deltas", "sortable proof table with inline \"replicate\" actions", "funnel bar chart", "time-series line chart", "mascot logomark top-left"]
palette: ["#FFFFFF", "#FFE01B", "#241C15", "#0A5C56", "#E8623D", "#4F8A5B"]
type: ["serif display (visual match, unverified)", "sans UI (visual match, unverified)"]
kind: reference-style
source: anton
status: ready
raw: raw/refero.design 2637b30a-7c2f-452a-9677-d902edf6476c.png
---

## Why it works

This is a working product console, not a marketing page, and it reads that way
immediately: a slim left icon rail for primary navigation, a serif page title
("Email dashboard") paired with a plain pill tag reading "Sample data," and an
inline banner beneath repeating the disclosure in full sentences ("You're using
Mailchimp's sample data... upgrade to a Standard plan"). Stating the same fact
twice, once as a two-word tag and once as a full sentence, means a user
skimming and a user reading closely both get the same information at the
speed they're moving.

The serif page title is a small, telling choice for a data product: most
dashboards default to sans-serif for headings to match their UI chrome, but a
serif title here softens what is otherwise a dense grid of numbers, tables and
charts — a easy way to keep a data-heavy screen from feeling cold.

The layout stacks proof in increasing density: four metric tiles with trend
deltas first (fastest to scan), then a sortable table of past campaigns with an
inline "Replicate" action per row (turns analysis directly into the next
action), then a funnel chart and a time-series line chart (slowest, most
detailed). Each row of the page asks for a little more attention than the one
above it, which matches how someone actually works through a dashboard.

## What to borrow (principle)

- **State a data-quality disclosure twice** — once as a compact pill tag, once
  as a full-sentence banner — so it's legible at both skim and read speed.
- **Use a serif for a dense dashboard's page title** to soften an otherwise
  all-numbers, all-sans-serif screen.
- **Order dashboard sections by increasing density**: scannable metric tiles
  first, a sortable table next, charts last — matching how attention actually
  degrades down a long screen.
- **Put the next action directly inside the proof row** (a "Replicate" button
  on a top-performing email), so analysis and action share one row instead of
  requiring a separate step.

## What to leave

- A persistent disclosure banner this prominent, if it can't be dismissed,
  permanently claims real estate that could otherwise show more of the user's
  actual data once available.
- Mixing a percentage-format y-axis with dollar and count metrics in adjacent
  charts (as the time-series chart does, showing "700%" on an open-rate axis)
  risks reading as a data or formatting error rather than a design choice.

## Signature move

The doubled disclosure: the same "you're looking at sample data" fact stated
as both a two-word pill tag beside the page title and a full explanatory
sentence in a banner directly beneath it — belt-and-braces communication for a
fact users need to register instantly but also fully understand.

## Motion

(inferred from image) No motion is visible in the capture; metric tiles,
table rows and charts read as static. A dashboard of this density likely
animates chart data in on load and supports row-level hover states, though
this isn't confirmed without a captured extract.

## Brief

Build a dense but legible analytics-dashboard screen. Use a slim icon rail for
primary navigation, and set the page title in a serif to soften an otherwise
all-numeric canvas. If showing placeholder or sample data, disclose it twice —
a compact pill tag beside the title and a full-sentence banner beneath — so
the fact registers at any reading speed. Order the page by increasing
information density: scannable metric tiles with trend deltas first, a
sortable proof table with an inline next-action button next, then detailed
charts (funnel, time-series) last. Keep the palette to a single bright brand
accent plus warm/cool trend colours (green up, coral down) and neutral ink on
white.

## Image recipe

Not applicable — this reference is a product UI screenshot, not photography.
If illustrating a similar dashboard, keep imagery limited to a small mascot or
brand mark in the navigation only; the canvas itself should stay data (tables,
charts, tiles), not photographic.

## Photo search

Not applicable — no photography used in this reference.

## Reference lock

Primary reference/direction: Mailchimp email dashboard — doubled sample-data disclosure, serif page title, density-ordered analytics layout.
Preserve (3-5 traits): a serif page title paired with a compact status pill beside dense, all-numeric UI; a data-quality or status disclosure stated both as a tag and as a full-sentence banner; dashboard sections ordered by increasing density (metric tiles, then a sortable table with inline actions, then charts); a next-action button embedded directly inside the proof table row, not a separate step.
Borrow only (1-2): the small mascot logomark in the navigation rail; the warm/cool (coral down, green up) trend-delta colour convention.
Role rules: any placeholder/sample-data state must be disclosed in at least two forms (tag + sentence); chart axis units must always match the metric being shown, never mixed formats.
Media strategy: no photography — this is a working product console; imagery limited to a small brand mark and functional icons only.
Reject: a single, easily-missed disclosure of placeholder data; charts with mismatched axis units; ordering a dashboard's densest content before its most scannable content.
Token commitments: white `#FFFFFF`, brand-yellow `#FFE01B`, ink `#241C15`, teal-link `#0A5C56`, trend-down-coral `#E8623D`, trend-up-sage `#4F8A5B`; serif for the page title only, sans for all other UI and data type.
