# Imagery picks — Florhuset Majorna (AB14)

Contact sheet: `contact-sheet.html`, captured to `sheet/*.png`. All 20 candidate
IDs loaded without a single grey box — nothing failed and nothing is excluded on
that ground. The exclusions below are fit judgements, not load failures.

**Pool inventory at contact-sheet resolution (600px).** Of the 20 verified IDs,
six read as genuinely on-register for a Göteborg florist at 600px: flowers,
hands-on floristry, or west-coast water. The other fourteen — fine dining
plates, a beach bonfire, library shelves, a restaurant interior, a sauna,
stacked books, a fountain pen, an archive of sepia portraits — read as generic
"warm indie business" stock and would misrepresent Florhuset Majorna if forced
into a slot (using a restaurant's dining room as "our atelier" is the same
dishonesty gate.md flags for a competitor's UI standing in for the product).
They are excluded, not because they failed to load, but because the
honest-imagery rule outranks filling a grid.

**One of the six did not survive a second look.** `1526047932273-341f2a7631f9`
(a pair of hands holding a heart-shaped bouquet) reads fine at 600px on the
contact sheet — bright, on-theme, hands actually touching flowers. Pulled at
full resolution for the build, it turned out to be a staged flat-lay: glossy
salon-manicured nails, and floating red glitter charms and a star clip
composited above the wrist that don't sit on anything and can't be real. That
is a styled product photograph, not documentary floristry, and using it for
*ateljékvällar* — real people learning real binderi in this specific atelier
— would have been a small dishonesty in the exact spot the page most needs to
be credible. Pulled from both slots it held (bouquet card 4 and
*ateljékvällar*) after that discovery. This is the render-time swap Step 5b's
pipeline exists to catch, done here rather than left for someone else to spot.

## The five photographs actually used

| ID | What it shows | Judgement |
|---|---|---|
| `1487530811176-3780de880c2d` | Dense jewel-tone bouquet held by someone in a navy jacket (hair, shoulder and a ringed hand are visible at the frame edges) — blush/cream roses, one orange dahlia, burgundy privet berries, eucalyptus, deep green-black ground | Richest, darkest, most detailed photo in the pool. Real dark passages for the hero scrim, and three visibly distinct flower clusters, so it can honestly carry three different crops across the page (hero, one bouquet card, one ateljékvällar detail) without repeating the same view |
| `1469371670807-013ccf25f16a` | Outdoor wedding aisle, gold chiavari chairs, cream/blush/white rose-and-ranunculus pedestal arrangements on wrought-iron stands, soft bokeh arch behind | Literally a floristry-dressed wedding aisle — no better bröllop photo exists in the pool. One pedestal arrangement, cropped tight, doubles as the fourth bouquet |
| `1561181286-d3fee7d55364` | Pink parrot tulips in a glass vase, white-grey ground, window light | Clean, bright, unambiguously spring |
| `1574684891174-df6b02ab38d7` | White ox-eye daisies (prästkragar) against open blue sky | Unambiguously midsummer — the one seasonal beat tulips can't cover |
| `1518837695005-2083093ee35b` | Close, textured dusk sea, no horizon clutter, cool teal-grey water | The only west-coast-water photo in the pool; earns its place once, as atmosphere, not as a claim about the shop's own view |

## Assignment

**Hero — `1487530811176`, wide crop, `object-position: 22% 38%`.** Full-bleed,
the bouquet fills the frame edge to edge. Brightness runs uneven: cream and
blush roses catch the light through the centre and right, but the top-left
corner and the lower band (stems, shadow between blooms) sit near-black. The
headline lockup goes bottom-left on that dark band, under a directional scrim
built from the photo's own darkest corner rather than a flat dim over the
whole frame, so the flowers on the right two-thirds stay uncovered.

**Säsongens buketter, four cards, framed with air, never full-bleed:**
1. *Tulpantid* (vår) — `1561181286`. Unedited crop.
2. *Prästkragesommar* (sommar) — `1574684891174`. Unedited crop.
3. *Höstens mörka* (höst) — `1487530811176`, 2nd crop,
   `object-position: 78% 55%`, tight on the dahlia-and-berry cluster
   right-of-frame. A different visible region than the hero's — disclosed as
   a reuse, not presented as a fourth unrelated commission.
4. *Vinterns vita* (vinter) — `1469371670807`, 2nd crop,
   `object-position: 16% 26%`, tight on the single cream-and-blush pedestal
   arrangement, cropped to exclude its stand and the aisle behind. Also a
   disclosed reuse of the bröllop photo, chosen once the pink hands-bouquet
   photo was pulled (see above) — a real rose dome reads as "a bouquet"
   honestly; a stock heart-shape did not.

**Bröllop — `1469371670807`, wide crop, `object-position: 22% 42%`.** Framed
with air, rounded corners, generous margin — matches the photo's own soft,
bright register better than a hard-edge full-bleed crop would.

**Ateljékvällar — `1487530811176`, 3rd crop, `object-position: 30% 78%`.**
The diptych frame is a 4:5 portrait box against a square source, which (by
how `object-fit: cover` scales a square into a portrait box) always shows
the photograph's full height regardless of the vertical object-position
value — a piece of CSS arithmetic worth stating plainly rather than
claiming a framing choice that isn't really happening. What the horizontal
shift actually buys is a different left-weighted slice: cream roses and
purple astrantia rather than bouquet card 4's dahlia-and-berry corner. It
doesn't stage "hands binding" the way the pulled photo tried to — the alt
text says what's honestly there (roses and blossom against dark green), not
more.

**Om ateljén — `1518837695005`.** Runs as a slim, framed band beside the
address-and-hours copy — coastal light, not a claim that this is the shop's
own window. The caption names the sea, not the storefront.

## What did not make it

Fine-dining plates (×3), a beach bonfire (×2), library shelves (×2), a dark
restaurant interior, a sauna, a fountain pen and ink, an archive of sepia
portraits, a salad bowl, a pasta dish, stacked books, an open book, and — on
closer inspection — the hands-and-heart-bouquet flat-lay, all loaded cleanly
and all excluded on fit or honesty. None of the fourteen generic ones is a
flower, a hand working one, or this coast; the flat-lay looked like all three
at thumbnail size and turned out to be stock. Forcing any of them into a slot
would have been the mismatched-photo failure the contact-sheet method exists
to catch — the point of pulling full resolution before calling a pick final.
