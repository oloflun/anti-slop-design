# scroll-craft engine — copy, never edit

`scrollcraft.js`/`.css` are byte-identical copies of the upstream engine.
Copy both into each build folder; never edit per project — it's the
mechanism, not the design.

Theme via six tokens + two fonts: `--sc-canvas`, `--sc-surface`, `--sc-ink`,
`--sc-ink-soft`, `--sc-accent`, `--sc-accent-ink`, `--sc-font-display`,
`--sc-font-text`.

Bespoke behaviour (the signature move) reads `--sc-p` off an act element and
writes its own `data-sc-*` attributes in page CSS/JS — never touches the
engine file. `template.html` is the starting skeleton to copy in first.
