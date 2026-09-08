# Catalogue first — Step 0, before the verb is even classified

The catalogue is the bar. r7 (2026-09-06/07) named the reference slugs in the builder
prompt, the builders read them, the reference floor was satisfied — and
`Skill(design-catalog)` was never invoked, because the *selection* came out of the
orchestrator's memory rather than out of the catalogue. Nothing afterwards could tell the
difference. This step is that difference, and it is mechanical.

Run it before Step 0a. `hooks/design-gate.py` denies the first UI write until steps 5–7
have left their marks in the ledger.

## 1 · Sweep the sources

```bash
python scripts/catalogue/sweep_raw.py
```

Lists every file under `raw/` and `processed/` that no entry references. Exit 0 means
every source Anton has saved is reachable by a query; exit 1 means a reference exists on
disk that the chain cannot select, which is the same as not having it. Anything genuinely
not worth an entry goes in `raw/.ignore` with its reason, never silently skipped.

A source that arrives after this sweep is a source the build could not have used. That is
why the sweep is first and not last.

## 2 · Identify what the file is of

`raw-url` files carry their domain in the name (`www-happyrobot-ai` →
`https://www.happyrobot.ai`; `*-webflow-io` and `*-framer-website` are template hosts).
`sweep_raw.py` guesses it for you.

For a domain-less screenshot, two passes, in this order:

1. **Read the image exhaustively** — wordmark, product names, visible copy, any URL in a
   browser chrome. If a string is unreadable, say `UNREADABLE`; never guess it.
2. **Feed the image back with `index.json` in context** and ask whether it matches an
   entry the catalogue already has. Only then search the web, at most three queries.

Confirm before committing a URL: run `capture.py <candidate-url> tmp` and compare the
fold against the raw image. Not confidently identified → `url: ""`, `origin: raw-image`,
`extract: none`, everything read off the image, Motion marked inferred. **Never invent a
URL** (SCHEMA.md invariant).

## 3 · Extract the mechanics

```bash
python scripts/catalogue/capture.py <url> <slug>
designlang <url> --wait 2000 --ignore-widgets -q -o design-catalogue/entries/<slug>/extract
```

Those are the measured flags. `--full` hangs; `--screenshots --interactions` costs 269 s
and 4.8 MB per site for screenshots `capture.py` already takes. Base extraction runs in
about a minute and still carries Motion Language, Component Anatomy and Brand Voice.

A local example site has no public URL: serve it and extract the served URL. A `file://`
URL yields nothing.

## 4 · Write the entry

`SCHEMA.md` is the contract: 20 frontmatter keys with enumerated values, nine H2 sections
in fixed order. Fill the frontmatter from the extract's tokens; write the prose after
reading `shot.png` and every slice **as images**. Describe relations — type weight against
air against image against surface against motion — not a token list. Never invent a
palette, a font or a number.

`python scripts/catalogue/drift.py` is the check: enum values outside SCHEMA, missing
required sections, an `extract: ok` with no `*-design-language.md` behind it, a slug that
is not kebab-case. An entry with `register: warm photography` is not a small typo — it
becomes `other` in `index.json` and is then permanently unfindable by `query.py`.

## 5 · Select the references for this brief

```bash
python scripts/catalogue/select.py --brief BRIEF.md --k 4 --wildcard --explain
```

Deterministic scoring over `index.json`: register and grammar match hardest, then
category and authority, then free-text overlap with the brief. The build's own example
sites score negative — they are output, not reference — and a slug used as primary in the
previous round for the same client is penalised, because that is how two rounds end up
looking like each other.

`--wildcard` adds one high-scoring entry from **outside** the brief's category. The
catalogue *is* the category; a move it does not already contain has to come from
somewhere else, and taking one deliberately beats drifting into one by accident. The
wildcard is still tested against TASTE.md § 5 like everything else.

Empty result: widen the register, drop the grammar, try an adjacent category, or query a
known brand. An empty query is not permission to work from memory.

`select.py` writes one `catalogue-select` row into the session ledger. That row is what
the reference floor reads.

## 6 · Read them, then consolidate

Read each selected entry **as pixels** (`fold.webp`, every slice) **and as text**
(`entry.md` including § Motion and § Reference lock, plus `extract/*-design-language.md`).
Three lines of digest per file: what it does, what you take, what you leave. The floor
checks that `entry.md` and a fold were read for every selected slug.

Then consolidate. Three documents assert authority over the same decisions, and this is
the order when they disagree:

> **FEEDBACK post > TASTE.md § 4 rule > TASTE.md § 3 category > the entry's own Reference
> lock > an impeccable reference.** A newer F-post supersedes an older one.

Write the reference lock, the decision ledger and the direction contract into `BRIEF.md`
per [`reference-lock.md`](reference-lock.md). Media strategy is not chosen freehand: the
selected entries carry `## Image recipe` and `## Photo search`, and `select.py --explain`
prints them.

## 7 · Fingerprint

Against **every** row of `wiki/projects/_index/design-fingerprints.md`, not just the
recent ones: at least 4 of 6 dimensions different (grammar, nav, hero device, act form,
close, signature). Write the comparison out. On a scroll brief the floor requires the
registry to have been read, because a gate cannot be held against rows nobody looked at.

If a concept fails the gate, change the concept. Never the row.

## What this step is not

It is not research for its own sake, and it is not a licence to average. One primary
source, one or two borrowed details, each with a bounded job (this source owns the
canvas and the type, that one owns the close). A blend of four references is a page with
no author — gate 90.
