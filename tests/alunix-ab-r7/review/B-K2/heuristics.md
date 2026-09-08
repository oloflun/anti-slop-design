# Heuristic evaluation — Alunix K2 (B), run B/K2

URL tested: `http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html`
Source: `tests/alunix-ab-r7/runs/B/K2/` (index.html + scrollcraft.js/css, unmodified)
Screenshots and raw data referenced below live in `tests/alunix-ab-r7/review/B-K2/`
(files named `m-*` = motion/no-preference, `rm-*` = `prefers-reduced-motion: reduce`,
`mobile-*` = 390x844 narrow viewport, both at 1440x900 desktop unless noted).
Console output was captured for the full scroll range in both modes and is empty in
both (`console-motion.txt`, `console-rm.txt`) — no script/render errors surfaced.

## Summary

The primary path — understand the offer, see three real example sites, reach a
plain-SEK price list, find contact — works well for a pointer/scroll user: the offer
line reads before any scrolling, the "Oppna X" links are visually well-placed and
legible, prices are unambiguous, and kontakt@alunix.se is pinned in the header on
every single screen state in both motion and reduced-motion modes, so contact is never
more than a glance away. The two things that would make me hold this for revision are
keyboard-specific: Tab forces a user through every focusable element inside all three
embedded demo iframes (with two intermediate stops landing off-screen) before reaching
the next piece of Alunix's own content, and reduced-motion/mobile visitors see the same
wordmark block rendered twice in a row with no connective cue, which can read as
duplicated content rather than the intended two-stage reveal.

## Heuristic findings

| # | Heuristic | Verdict | Key finding |
|---|---|---|---|
| 1 | Visibility of system status | Caution | Several short scroll segments inside the 300vh hero pin produce almost no visible change (team's own scroll_verify.py "deadScroll" diffs of 0.0011-0.0149); a fast flick-scroll can pass through the entire visible payoff (p 0.62-0.84, about 400px of a 1800px pin) without the user noticing it happened. |
| 2 | Match between system and real world | Pass | Plain Swedish copy, real SEK prices, a real ticking Stockholm clock -- nothing invented or jargon-heavy. |
| 3 | User control and freedom | Caution | Crossing the 899px breakpoint live triggers location.reload() (by design, per the page's own JS comment) -- a mid-read window resize/rotation restarts the page and drops scroll position. |
| 4 | Consistency and standards | Caution | Reduced-motion/mobile show the ALU/NIX wordmark as two near-identical static blocks back to back (crushed, then "opened") with no divider or transition cue, unlike the single continuous morph motion users get for the same content -- see rm-hero.png to rm-opened.png and mobile-fold.png to mobile-opened.png. |
| 5 | Error prevention | Pass (N/A) | No forms, no destructive actions; only affordances are links (mailto + external demo sites), nothing to prevent. |
| 6 | Recognition rather than recall | Pass | Every demo link's caption ("Exempelsida: X") and its "Oppna X" link use the identical name, right next to each other -- no memory burden. |
| 7 | Flexibility and efficiency of use | Caution | Efficiency is lopsided by input method: a scroll/pointer user reaches pricing and contact in a few gestures; a keyboard user must pass roughly 20 Tab stops through three embedded sites' own internal navigation to do the same (see walkthrough below). |
| 8 | Aesthetic and minimalist design | Pass | Five-tone palette, generous whitespace, no decorative chrome -- confirmed across all captured states. |
| 9 | Help users recognize/diagnose/recover from errors | N/A | No error states exist on this static page. |
| 10 | Help and documentation | N/A | Not needed for a page this size and scope; none present, none missing. |

## Cognitive walkthrough -- key task

Task: understand what Alunix sells, then see proof (three example sites), then reach
prices, then find contact (kontakt@alunix.se).

### Persona A -- pointer/scroll (mouse, trackpad, touch)

1. Land on page, understand the offer. The tagline "Webbdesign, design och system.
   Allt pa ett stalle." sits directly under the header, visible with zero scrolling
   (m-hero-00-000pct.png). Right action obvious (keep looking / start scrolling),
   correctly associated, progress visible immediately. Pass.
2. Scroll through the signature hero. The mask cycles Calyx to Horai to Hyperborea
   behind the letterforms with a caption naming each site (m-hero-03-030pct.png,
   m-hero-06-060pct.png) -- the user correctly reads this as "these are examples."
   Between p about 0.7 and p about 1.0 the block opens into "VI BYGGER ERT VARUMARKE."
   At p about 0.8 the second line is caught mid-fade, very low contrast, overlapping
   the top of N (m-hero-08-080pct.png) -- if the user's scroll happens to stop exactly
   there, the frame briefly reads as unfinished/broken rather than mid-transition; two
   steps later it is fully resolved and legible (m-hero-10-100pct.png). Caution --
   brief, scroll-position-dependent, self-resolving.
3. See proof. The "Bevis" section shows three full, live, labelled iframes with a
   caption and an "Oppna X" link directly beside each (m-proof-spread-0.png,
   m-proof-spread-1.png, m-proof-spread-2.png). The link text mirrors the caption,
   sits in bold ink against the paper background, and needs no explanation. Pass --
   this is the strongest part of the flow for this persona.
4. Reach prices. "Tjanster" then "Paket" follow in the same ledger visual language;
   all three price rows are legible with plain SEK figures or "Pris vid forfragan"
   (m-price.png, matching rm-price.png). Pass.
5. Find contact. kontakt@alunix.se is in the sticky header, visible in every
   screenshot captured in this review regardless of scroll position or mode -- the
   user never has to look for it, it is simply always there. It is also repeated,
   larger and underlined, at the very bottom (m-close.png). Pass, strongest single
   feature of the page for this task.
   - Minor friction on the way there: after the price list, roughly half of the dark
     "close" section is empty vertical space before the mail link and colophon appear
     (m-close.png, m-bottom.png) -- a user who has just finished reading prices and
     keeps scrolling hits a large, undifferentiated dark void before the payoff. Caution.

### Persona B -- keyboard only

1. Tab 1-2: logo mark, then the header's kontakt@alunix.se link -- task-critical
   content is reachable in two presses from page load. Pass, and arguably beats the
   scroll persona for pure "find contact" speed.
2. Tab 3: "Oppna Calyx" -- link is announced and visible mid-viewport once the
   browser's smooth-scroll settles (confirmed directly: text/href read back as
   "Oppna Calyx" / /sites/calyx.html, focus ring rendered correctly per
   :focus-visible computed styles, focus-calyx-settled.png). Pass -- my first pass at
   this test showed no visible ring because the screenshot was taken mid
   smooth-scroll-animation, before the browser had settled; re-tested with the
   animation allowed to finish and the outline renders as specified.
3. Tabs 4-9 (6 stops): focus moves inside the Calyx iframe's own internal navigation
   (its INDEX/STUDIO/COMMISSIONS-style links) -- none of this is Alunix's content, and
   the outer document.activeElement reports the same iframe element for all six
   presses (focus-log-motion.json, entries 3-8). The user has no way to know how many
   more presses this will take.
4. Tabs 10-11: focus lands inside the next article's iframe (Horai) while it is still
   fully below the fold -- visible:false, bounding box top:1074 bottom:1648 against a
   900px-tall viewport (focus-log-motion.json, entries 9-10). The focus indicator is,
   for two presses, on-screen nowhere the user can see it -- a genuine orientation
   failure for a keyboard user (heuristic 1, visibility of system status).
5. Tabs 12+ repeat the same pattern for Horai's remaining internal links and then for
   Hyperborea's (8 more iframe-internal stops) before "Oppna Hyperborea" is reachable.
   Total: about 12 Tab presses to pass all three demo links, only 3 of which are
   Alunix's own actionable content -- a keyboard user reaches the pricing section only
   after working through the equivalent of three strangers' navigation menus. Fail for
   heuristic 7 (efficiency), Caution for heuristic 1 (two invisible stops).
6. Prices and the final mail link remain reachable by continuing to Tab -- no dead
   ends -- but the cost to get there is the finding above.

## Findings by severity

**Major**
- Keyboard Tab order forces a user through every focusable element inside all three
  embedded demo iframes (about 6 + 2-or-more + 8 stops), and at least two of those
  intermediate stops land on elements with visible:false bounding boxes before
  autoscroll catches up. Heuristic 1 & 7. Evidence: focus-log-motion.json (entries
  3-20), m-focus-2-calyx.png. Fix: add tabindex="-1" to the three .frame iframe
  elements -- they are live decorative previews, not the intended interactive path
  (the adjacent "Oppna X" link already is), so Tab should skip straight from one
  arrow-link to the next.
- Reduced-motion and narrow (under 900px) viewports show the ALU/NIX wordmark as two
  near-identical static sections back to back with no connecting cue, unlike the
  single continuous morph motion users see. Heuristic 4. Evidence: rm-hero.png plus
  rm-opened.png, mobile-fold.png plus mobile-opened.png. Fix: add a small connecting
  label or divider mark between the crushed and opened blocks (e.g. a short
  down-chevron or a one-line caption) so the sequence reads as one idea shown twice,
  not two copies of the same graphic.

**Minor**
- At approximately p=0.8 of the hero pin scrub, "ERT VARUMARKE." renders at very low
  opacity while overlapping the top of the N in NIX -- a user who stops scrolling in
  this narrow window sees what can read as a rendering glitch. Heuristic 8. Evidence:
  m-hero-08-080pct.png vs. the resolved m-hero-10-100pct.png. Fix: raise the minimum
  opacity floor on the --l1/--l2 reveal curve, or shift the reveal threshold slightly
  earlier relative to the row separation, so no intermediate frame sits at a
  barely-legible mid-opacity.
- Roughly half of Akt E's dark "close" section is empty space below the mail link and
  colophon. A user who has just read the price list and keeps scrolling meets a large,
  undifferentiated void before the actual end of page. Heuristic 1. Evidence:
  m-close.png, m-bottom.png. Fix: trim the empty tail height, or add a subtle
  low-opacity anchor near the very bottom so continued scrolling still reads as
  purposeful.
- Several short "hold" segments inside the hero pin produce near-zero visible change
  on a fast scroll gesture, per the team's own scroll_verify.py deadScroll output
  (diffs 0.0011-0.0149 across four windows). A quick flick-scroll can jump past the
  entire p 0.62-0.84 reveal window (about 400px of scroll) without the user seeing the
  headline resolve. Heuristic 1. Fix: none required if this pacing is an accepted
  trade-off (it is explicitly documented as intentional in the build's own NOTES.md);
  flagging for awareness rather than as a defect.
- Resizing/rotating across the 899px breakpoint mid-session triggers a full
  location.reload() (by the page's own design, documented in its JS). A user who
  rotates a tablet mid-read loses their scroll position outright. Heuristic 3. Fix:
  acceptable as a pragmatic trade-off given the structural layout change involved, but
  worth confirming this matches the orchestrator's intent for tablet users
  specifically.

**Ruled out (investigated, not a real finding)**
- Small stray blue/orange-tinted pixels visible in raw per-pixel sampling of the
  services-list body copy (m-services.png) turned out to be ordinary LCD-style
  subpixel/antialiasing fringing at 1-pixel scale -- invisible once the same region is
  viewed at normal size or resampled (crop-typografi-visual.png, crop-kod-visual.png,
  crop-kunddatabas-visual.png all show clean black text on paper). Not a rendering
  defect, not reported as a finding.
- An apparently-missing keyboard focus ring on "Oppna Calyx" in the first capture pass
  (m-focus-2-calyx.png) was a timing artifact of my own test script (screenshot taken
  mid smooth-scroll-into-view, before layout settled) -- retested with the animation
  allowed to finish and the :focus-visible outline renders exactly as specified in CSS
  (focus-calyx-settled.png).

## What works well

- kontakt@alunix.se and the Alunix wordmark are visible in the sticky header on
  literally every screen state captured, in both motion and reduced-motion modes --
  the "find contact" half of the task is solved before the user does anything.
- The "Oppna X" links are consistently placed, legibly weighted, and use the exact
  same site name as the caption right beside them -- no ambiguity about what a link
  does before clicking it.
- Pricing is stated in plain SEK with no hedging, and the bespoke/"ask" tier is
  clearly marked "Pris vid forfragan" rather than left blank.
- Reduced-motion mode preserves every piece of information the motion mode
  communicates (per the build's own F-001 compliance) -- nothing is exclusively
  conveyed through animation.
- Console is completely clean across the full scroll range in both motion and
  reduced-motion modes -- no script or render errors surfaced during the walkthrough.

## Recommendation

**Revise.** The core task -- understand, see proof, reach prices, find contact --
works well for the majority pointer/scroll persona, and contact discoverability in
particular is excellent. But the keyboard tab-trap through three embedded sites'
internal navigation and the unexplained double-wordmark in reduced-motion/mobile are
both concrete, evidenced problems worth fixing before shipping; both fixes are small
and targeted (a tabindex attribute; a connecting caption/divider) rather than
structural.
