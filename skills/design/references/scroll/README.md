# Scroll · Step 2b — Grammar, feeling curve, signature move, fingerprint

Where vendored scroll-craft (`../upstream/scroll-craft/`) plugs into `design`.
Runs between Step 2 (the gate) and Step 4 (build), only on a Persuade/
Experience surface whose brief actually asked for scroll choreography.

## The scope rule (verbatim)

> Persuade/Experience surfaces (landing, marketing, portfolio, campaign) MUST
> ship ≥4 device families, never the same device twice in a row, one
> engineered peak with the largest span, one signature move, and pass the
> fingerprint gate; Operate/Read surfaces (dashboards, admin, settings, docs)
> get NO scroll choreography (frequency rule: 100+/day = no animation) —
> state motion 150–250 ms only; reduced motion removes travel, not content.

The Operate/Read half is not new: it's `../motion.md`'s existing scroll-
linked-motion ban (reveal-once only, no parallax, no scrub), restated in
scroll-craft's vocabulary. Nothing here overrides `../../SKILL.md` § Product
surfaces for an authenticated page.

## Contract

**Reads** — the `design` Step 1 interview (scroll-craft's eight questions
fold in, not asked twice); [`grammars.md`](grammars.md) (pick one grammar
against the register); [`devices.md`](devices.md) (nine devices, cue
contract); [`feel-and-fingerprint.md`](feel-and-fingerprint.md) (curve, peak,
move, gate); the registry `VAULT/wiki/projects/_index/design-fingerprints.md`;
`../house-physics.md` Motion + `../motion.md` — output must clear both bars.

**Does** — names the grammar and states why the other seven lost; writes the
feeling curve (emotion → cause per act) and names the peak; invents one
signature move, bespoke and coded in the page, never a kit parameter tweak;
scores the journey into a device table (≥4 families, never twice running, ≤2
`scrub`); runs the fingerprint gate against every existing registry row (≥4
of 6 dimensions clear, per row).

**Writes** — `BRIEF.md` additions (feeling curve, peak sentence,
tell-someone sentence, signature move); the score table (beat → device →
why); one new registry row, appended after ship.

**Human checks** — the fingerprint result is shown, not asserted (≥4-of-6
printed against every row, not "it passed"); the feel check
([`feel-and-fingerprint.md`](feel-and-fingerprint.md) § Peak: scroll cold,
one word per act, diff against the intended curve before opening `BRIEF.md`);
the verification JSON pasted, not summarized (`scroll_verify.py`, generic, or
scroll-craft's own `shoot.mjs` on the real engine); a human reads the contact
sheet — no automated pass above substitutes for that.

## Files here

- [`grammars.md`](grammars.md) — the eight grammars + register fit matrix.
- [`devices.md`](devices.md) — the nine devices + the cue contract's gotchas.
- [`feel-and-fingerprint.md`](feel-and-fingerprint.md) — curve, peak,
  tell-someone test, signature move, fingerprint gate, registry format.
- Full upstream source for anything condensed here:
  `../upstream/scroll-craft/plugins/nateherk-design/skills/scroll-craft/`.
- Engine + starting template (copy per project, never edit it):
  `../../scripts/scroll/` — `scrollcraft.js`, `.css`, `template.html`, `NOTE.md`.
- Generic verification harness: `../../scripts/scroll_verify.py`.

**Engine is opt-in per grammar (AB06).** Use the vendored engine only when the chosen grammar needs scrub, pin or pan acts, and never in a blind one-shot: build, read the console for `[scrollcraft]` warnings, run `scroll_verify.py`, fix, repeat. Otherwise the chain's own signature set-piece + shared reveal (house-physics) is the default.
