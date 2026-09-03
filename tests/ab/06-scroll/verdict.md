# AB06 — scroll-craft i kedjan (Persuade-sida, specialkaffe på burk, warm photographic)

A = SKILL.md + house-physics (kedjans egna "one signature scroll set-piece"). B = samma + references/scroll/* + devices.md (fullt kit) + motorn inlinad; ≥4 device-familjer, grammatik, känslokurva, peak, signature move.

| Mått | A | B | Not |
|---|---|---|---|
| grammatik / känslokurva / peak / signature move | — / ja / — / "Förseglingen" (lerp) | filmic one-shot / 6 akter / Rosteriet span 4.8 / SVG-lock på `--sc-p` | B:s plan är den bättre planen |
| device-familjer | 1 set-piece + delad reveal | pin, reveal, pan, flow+in, pin+parallax, kinetic+magnet (6) | |
| scroll_verify: deadScroll-intervall | 1 | **18** | B:s tre pinnade akter scrollade bort |
| cuesNeverFull | 1 | 1 | |
| contrastUnderMedia (fynd / sämsta) | 3 / 1.18 | 7 / 1.01 | B:s hero utan scrim, tunn serif på bönor |
| unrevealed | 0 | 0 | |
| konsol | 0 | 3 × `[scrollcraft] act will not pin: stage computes position:relative … something is overriding .sc-stage` | byggarens CSS skrev över motorns klass |

Visuellt (scrollv/sheet.png för båda, lästa): A är en sammanhängande sida med en tom mörk panel där jar-set-piecen skulle vara (dess bilder syns inte). B har tre nästan tomma skärmsviter (mörk grund med micro-text, cream utan innehåll) där pin-akterna skulle hålla, ett fungerande pan-galleri och en fungerande parallax-peak i nedre halvan; hero-typen är svårläst över bönorna. Orsaken är entydig: motorn varnar tre gånger att `.sc-stage` blivit `position: relative` — byggaren tematiserade med egna regler på motorns klasser i stället för via de sex tokens.

**Beslut: IN-MODIFIERAD.** In: grammatikerna, känslokurvan, fingerprint-gaten (strukturaxeln kedjan saknade; B:s plan var bättre än A:s) och scroll_verify (som fångade båda sidornas fel). Modifierat: motorn är **opt-in per grammatik** (scrub/pin/pan-grammatiker), aldrig i ett blint one-shot; Step 5 läser konsolen efter `[scrollcraft]`-varningar innan något annat; devices.md får regeln "rör aldrig .sc-*-klasserna, tematisera bara via tokens; en varning om position: relative betyder att din CSS vann över motorn". Kedjans egen "en set-piece + delad reveal" förblir default för Persuade-sidor som inte väljer en pin/pan/scrub-grammatik.
