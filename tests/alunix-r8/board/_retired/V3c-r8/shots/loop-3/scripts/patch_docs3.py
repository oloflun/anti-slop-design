"""patch_docs3.py: README § R9 and BRIEF § Arkitektens rader, loop 3."""
from pathlib import Path
CELL = Path("C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3c")

P = CELL / "plans/README.md"; s = P.read_text(encoding="utf-8")
anchor = "## R8 (helhetsloopen runda 2), i ordning (åtta planer; taket är åtta)"
assert anchor in s
new = """## R9 (helhetsloopen runda 3), i ordning (sju planer; taket är åtta)

Skrivna av arkitekten 2026-09-17 mot R8-läget av `runs/V3c/index.html` (md5 `70214a22`);
matchar raderna inte när byggaren öppnar filen, stoppar byggaren. Ordningen är kontraktets:
funktion → states → flöde/hierarki → visuellt → kod. Källor: `HELHET.md` § 3 (loop 3-raderna),
`NOTES.md` § Loop 3, `reviews/loop-3-astra.md`, leadens pixelläsning R8 (två fynd, båda först).

| # | Titel | Allvar | Ordning | Källor |
|---|---|---|---|---|
| 035 | Revealens latch samplar shimens lerp tills den landat (aktobjektet löses per tick, exakt 1) | HIGH | 1, funktion | leadens R8-fynd 1; `shots/loop-3/latch_diag.json`, `slices-1440-fix/`; Astra loop 3 fix 1 |
| 036 | Revealen klipper aldrig en levande ram: irisen och uppdragningen som transform på en inre box, ramen kontraskalad | HIGH | 2, funktion (bildtiden) | `shots/loop-3/probe/ab/` (clip-path över levande Hōrai 101 till 303 ms, transformreceptet 35 till 47, ingen klippning 35 till 62); Astra loop 3 K7 |
| 037 | `?preview=process-0N` siktar om efter `load` och `fonts.ready` | HIGH | 3, funktion | `shots/loop-3/preview_check.json`; Astra loop 3 fix 5 |
| 039 | Kortsidan, `is-turning` och `data-on` av läser shimens `cur` | MEDIUM | 4, states | Astra loop 3 fix 2, 3; `index.html` 1660, 1666, 1708 |
| 040 | Arkets kontur hel medan steg 01 läses | LOW | 5, flöde/hierarki | H-15; `slices-1440/v3c-1440--s06.png`, `process-390/…life-01.png`; Astra loop 3 fix 6 |
| 038 | Grunddriften 44 → 24 %, H-19 omskriven på mellantonen | MEDIUM | 6, visuellt | leadens R8-fynd 2; `shots/loop-3/drift2/` |
| 041 | Driften skrivs på `.ground` av sidan, mätgrindad | LOW | 7, kod | loop 2 `synth3` (9,13 → 0,24 ms per skrivning); loop 3 `probe/ab/` (ingen vinst i prisfönstret); Astra loop 3 fix 4 |

035 först: 036 bygger på samma `--rv` och samma sampler, 039 hänger tre konsumenter till
på 035:s `latchTick`. 036 mäts med `shots/loop-3/scripts/motion_probe_ab.py --pre` i
prisfönstret (3 873, 18 ticks) och jättefönstret (2 700, 28 ticks) före och efter, tre
körningar var, median. 037 är oberoende. 040 och 038 är enradsändringar. 041 sist och bara
med mätt vinst (som 028 E).

**Utanför R9:** Q30 (bandets omkomposition; H-02/H-03/H-08 s03), H-24 (verktygsskuld),
H-34 (leadens grind), jättens skala 0,92 → 1 (oläsbar, redundant mot ordscrubben,
rapporterad), sidvikten (462 kB), a11y-skulden, K3-mallens `.process-grid`-spann (R6-fynd).

**Verktygsfynd loop 3:** `slices.py`/`shoot_slices` når sina positioner med `scrollTo`,
alltså exakt den väg latchen inte täcker (K5): skivor 04/05 visade klippta ramar utan att
ramarna var sovande. `slices_fix.py` injicerar 035:s sampler före fångsten och är
helhetsloopens skivfångst tills 035 är byggd. `motion_probe_ab.py --pre "<js>"` (scratchkopia)
kör en ablation efter `load` + 5 s före hjulet; A/B-talen svänger ±50 % mellan identiska
körningar, så tre körningar och median.

"""
s = s.replace(anchor, new + anchor)
P.write_text(s, encoding="utf-8"); print("README ok")

B = CELL / "BRIEF.md"; b = B.read_text(encoding="utf-8")
anchor2 = "## Direction contract"
assert anchor2 in b
rows = """### Arkitektens rader, helhetsloopen runda 3 (2026-09-17)

| Area | Decision | Source | Source rule | Why |
|---|---|---|---|---|
| **Revealens latch** | samplas av sidan per bildruta tills shimen landat, aktobjektet löses per tick, exakt 1 (plan 035) | `shots/loop-3/latch_diag.json`: samma scrollY ger `--rv` 0,98 (hjul), 0,21 (PageDown), 0 (`scrollTo`); med samplern ≥ 0,9988 på alla fyra | F-014, gate 94: det ögat ser läser det lerpade värdet, och en reveal ska nå 1 oavsett scrollsätt (a11y F-03) | Leadens R8-fynd 1; `readState` körs bara per scroll-händelse, shimen lerpar 30 bildrutor till |
| **Revealen över en levande ram** | ingen `clip-path`/`mask` på en wrapper som innehåller en monterad iframe; irisen som `border-radius:50%` + `scale(--rv)` på en inre box med ramen kontraskalad `scale(1/--rv)`, uppdragningen som `translateY` på en inre box med ramen kontratranslaterad; `--rv` `inherits:true` (plan 036) | `shots/loop-3/probe/ab/`: cpu 1, prisfönstret, ramarna förmonterade: clip-path 101 till 303 ms p95, `mask-image` 65 till 86, `will-change:clip-path` 71 till 142, transformreceptet 35,6 / 46,7, ingen klippning 35 till 62 | Ramen transformeras aldrig efter att den visats (PRODUCT.md); under revealen står innehållet pixelstilla (skala × 1/skala = 1) och efter revealen är transformen identitet | K7: bandets bildtid är klippningen, inte omräkningen; mätt i fem A/B-omgångar |
| **Previewlägena** | `aimPreview()` vid skripttid, på `load` och på `fonts.ready` (plan 037) | `shots/loop-3/preview_check.json`: 1440 process-02 `--k2` 0,19, 390 process-01 `--k1` 0,67 | `?preview=` visar det formade läget (BRIEF § `?preview=`-plan) | Astra loop 3 fix 5; typsnitten flyttar li 02 till 07 efter att målscrollen räknats |
| **Sidans lägen** | kortsidan (`inert`), `is-turning` och `data-on` av läser shimens `cur` via 035:s sampler (plan 039) | `index.html` 1660, 1666, 1708; `scrollcraft.js` 835 (dwell-remapp) | F-014; performance.md (ingen vilande `will-change`); 025 B4:s avsikt (baklängesritning, aldrig klipp) | Astra loop 3 fix 2, 3 |
| **Processentrén** | konturen över `--k1` 0 till 0,30, glyfen 0,30 till 0,70 (plan 040) | `slices-1440/v3c-1440--s06.png`, `process-390/v3c-390-life-01.png` | House physics: en öppen spalt bär en helhöjdslinje eller stänger; H-15 | Astra loop 3 fix 6 |
| **Grunddriften** | tonlagret 44 → 24 %; H-19 omskriven på mellantonen (chroma 12 till 24 på träpanelen vid tesen, ≤ 2 i folden) (plan 038) | `shots/loop-3/drift2/drift2.json`: 44 % chroma 38, 24 % chroma 21, 0 % 0 på (720,180); `d44-thesis.png` mot `d24-thesis.png` | TASTE § 4.4: accenten gör en sak; `mix-blend-mode:color` skalar kulör med luminans, så ett golv på svärtan tvingar en tvätt | Leadens R8-fynd 2 |
| **Driften på `.ground`** | sidan äger de tre stoppen och skriver `--sc-canvas` på `.ground`, behålls bara med ≥ 3 ms p95 vinst i tes- och jättefönstret (plan 041) | loop 2 `synth3` 9,13 → 0,24 ms per skrivning; loop 3 `probe/ab/mount-noclip*` mot `*-nodrift*`: ingen skillnad i prisfönstret | Mät före ändring (F-013 regel 2) | Astra loop 3 fix 4; 028 D |
| **H-01, H-05, H-19** | raderna omskrivna med källa och mätning (kedjans budget 8 till 14 vh; 390-golvet 96 px; mellantonen) | `geom3.json`, `drift2.json` | Golvet är kontrollerbara påståenden; ett tal utan källa byts mot talet med källa | Fas A:s 12 vh saknade källa; H-05 (a) och 032 B stod i konflikt; H-19:s mätpunkt var fel |
| **Skivfångsten** | `slices_fix.py` (035:s sampler injicerad) är loopens skivfångst tills 035 är byggd; `scrollTo`-skivorna visar klippta ramar som inte är sovande | `slices-1440/v3c-1440--s04.png` mot `slices-1440-fix/…s04.png` | Verktyget får inte mäta en väg sidan inte täcker utan att säga det | K5 |

"""
b = b.replace(anchor2, rows + anchor2)
B.write_text(b, encoding="utf-8"); print("BRIEF ok")
