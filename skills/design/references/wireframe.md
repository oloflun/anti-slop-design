# Wireframe · exploring the space before committing

**Load when the user wants direction, not code: "what should this look like", "mood", "ideas", a brief with no build yet.**

> Source: Anthropic's Claude Design "Wireframe" skill, ported verbatim. Blocks marked **[ours]** are this repo's framing.

---

## Verbatim

> *"Help the user explore design ideas quickly. Interview them, then generate multiple rough wireframes to map out the design space before committing to a direction. Prioritize breadth over polish: show 3-5 distinctly different approaches for each idea. Use simple shapes, placeholder text, and minimal color to keep the focus on structure and flow. Use a sketchy vibe — handwritten but readable fonts; b&w with some color; low-fi and simple. Lay the wireframes out as a vertical options stack."*

Layout format → [`options.md`](options.md).

---

## [ours] How to use this tier

**Interview first.** The interview is not optional — it is the first word of the source. Use the calibration table in [`process.md`](process.md) to size it. A vague brief earns a lot of questions; a precise one earns none.

**Breadth over polish is the whole point.** Three to five *distinctly different* approaches, not one approach at three fidelities. If two wireframes differ only in spacing, one of them is wasted. Vary the thing that actually changes the answer: what leads the page, what the reading order is, whether the proof is a demo or a number or an image, whether the structure is a single spread or a long scroll.

**Low fidelity is a feature.** Sketchy, b&w with a little colour, placeholder text. The moment a wireframe looks finished, the user starts reviewing the typeface instead of the structure — which is the wrong conversation at this stage and costs a round.

**Do not write production code at this tier.** Wireframes are throwaway. Wait for the user to pick a direction before building anything real.

**The gate still runs.** Wireframing does not suspend Tier 0–2. If the brand exists, the wireframes use its type scale and its ground colour even at low fidelity — a wireframe in generic greyscale for a brand with a committed orange gives the user a structure decision divorced from how it will actually feel. Low fidelity means *simple*, not *unbranded*.

**ASCII wireframes are the cheapest form, and they belong in the plan as well as on the board.** Anthropic's frontend-design skill puts them inside the design plan itself, alongside the palette and the type roles: *"a layout concept, using one-sentence prose descriptions and ASCII wireframes to ideate and compare."* Two things follow.

**First: one sentence of prose per wireframe, next to the drawing.** The box diagram shows the arrangement; the sentence says what the arrangement is *for*. A wireframe with no sentence gets compared on how tidy the boxes look.

**Second: alignment is a decision the wireframe has to state.** The same source: *"Include alignment guidance; should the content be left aligned, center aligned, justified?"* Say it per block, in words, because ASCII cannot show it — a monospace box cannot distinguish a left-flush head from a centred one, so a set of wireframes that omits it silently defers the decision to the build, and the build defaults to centred. Note the alignment *and* whether it coheres with the body beneath it or deliberately breaks from it (`layout-and-space.md` § Asymmetry techniques owns that rule; the accidental mismatch is what reads as a mistake).

```
┌──────────────────────────────────────────┐
│  ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁     ██████████████   │   A: display line left-flush against
│  ▁▁▁▁▁▁▁▁▁▁▁▁                            │      a full-bleed figure holding the
│  ▁▁▁▁▁▁▁▁▁                ██████████████ │      right two fifths.
│                                          │      Head: left. Body: left. Figure
│  ── ▁▁▁▁▁▁▁▁                             │      bleeds past the right edge.
└──────────────────────────────────────────┘
```

**This lives between 2b and 4** in the front door's sequence: after the grammar, feeling curve and signature act are named, before any code is written. That is the point where a structure decision is still cheap and a rebuild is not.

**Structural variety comes from [`structure.md`](structure.md).** Its six axes — section-heading placement, body composition, divider language, button voice, image treatment, reveal pattern — are the dimensions to vary across the 3–5 approaches. Use them as the checklist for "are these actually different" before showing the set.

**Next step after a pick.** The chosen wireframe becomes the input to the full flow at Step 3 of the front door. Do not rebuild from scratch — carry the structural decision forward and hang the derived system on it.
