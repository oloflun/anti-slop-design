# 040 · Arkets kontur är färdig medan steg 01 läses: entréskärmens högerspalt bär en hel ram, inte ett streck

- **Status**: TODO (R9, loop 3)
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Severity**: LOW (flöde/hierarki: entréskärmens högerspalt väger mindre än sin bredd tills konturen är ritad)
- **Category**: Flöde / visuellt, H-15, house physics ("weight every column you open"); Astra loop 3 fix 6 (bild 86, 98), arkitektens egen läsning av `s06`
- **Estimated scope**: 1 fil, 2 rader CSS (två fönsterkvoter)
- **Källor**: loop 3 `shots/loop-3/slices-1440/v3c-1440--s06.png` (entrén: kicker, rubrik, steg 01 till vänster; till höger ett hörn av ramen), `process-1440/v3c-1440-life-00.png`, `life-01.png`, `process-390/v3c-390-life-01.png` (rubrik, ett ensamt streck, tom nedre skärm); `index.html` rad 945 (`#p-outline` ritas över `--k1` 0 till 0,55), rad 951 till 952 (`#p-glyph` 0,45 till 1,0), rad 1620 till 1627 (`--s1` = arkets ankomst + 0,05 vh, `--e1` = li 01:s mitt i viewportens mitt)

## Problem

Konturen (`#p-outline`) ritas över `--k1` 0 till 0,55, och `--k1` går från arkets ankomst
(`--s1`) till li 01 centrerad (`--e1`). Vid 1440 är det ~1 000 px scroll; konturen är alltså
hel först när läsaren nått halvvägs genom steg 01:s text. På entréskärmen (`s06`, arket
en tredjedel in) består högerspalten av en toppkant och en högerkant: en 900 px bred spalt
som bär ett streck. Vid 390 (`life-01`) står rubriken över ett ensamt streck och en tom
nedre skärm. Konceptet ("ett tomt ark") kräver att arket **finns** som ram när steg 01
läses; det är ramen som är formen (gate 47/79), inte tomheten.

```css
/* index.html:945, 951-952 - current */
  #p-outline{--p-l:clamp(0,calc((var(--k1) - 0) / 0.55),1);}
  .process-sheet #p-glyph{... --p-l:clamp(0,calc((var(--k1) - 0.45) / 0.55),1);}
```

## Target

Konturen ritas över `--k1` 0 till 0,30 (hel när arket är en knapp tredjedel in, dvs på
entréskärmen), glyfen 0,30 till 0,70 (färdig innan `--e1`, så preview 01 är oförändrad:
båda står på 1 vid `--k1` = 1). Ingen ändring av `--s1`/`--e1`, inga nya banor.

```css
/* target, index.html:945, 951-952 */
  /* PLAN 040 (loop 3): konturen är hel medan steg 01 läses; entréskärmens
     högerspalt bär en ram, inte ett streck (H-15). Glyfen följer efter. */
  #p-outline{--p-l:clamp(0,calc((var(--k1) - 0) / 0.30),1);}
  .process-sheet #p-glyph{... --p-l:clamp(0,calc((var(--k1) - 0.30) / 0.40),1);}
```

Banornas överlappning (perf 4: högst halva fönstret): konturen 0 till 0,30, glyfen 0,30
till 0,70: ingen överlappning. Steg 02:s första bana (`#p-guides`, `--k2` från 0) rörs inte.

## Repo conventions to follow

- `pathLength="1"` med `*1px`, `.draw`-mekaniken, `@property`-raderna: orörda.
- Bara fönsterkvoterna; ritningen ritar samma form (gate 47/79).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Konturen hel på entréskärmen (`--k1` 0 till 0,30)".

## Steps

1. Byt kvoterna på rad 945 och 952 enligt Target.
2. Mät (1440x900, 390x844): vid scrollY där `.process-grid`:s överkant står på 60 % av viewporthöjden (arket en dryg tredjedel in) är `#p-outline`:s `stroke-dashoffset` `0px`; vid `--e1` (preview 01) är `#p-glyph` `0px`.
3. Tolv ramar genom `#process` (som `frames.py life`): `life-01` visar hela ramen.
4. `motion_probe.py` `#process:--sc-ps` cpu 1, 100:60: staircase 0, p95 inte sämre än loop 3 (32 ms ned, 18,5 upp).

## Boundaries

- Rör inte `--s1`/`--e1`, inte steg 02 till 07:s fönster, inte prosan.
- Matchar inte rad 945 eller 951 till 952: STOPPA.

## Verification

- **Mekaniskt:** steg 2, 4.
- **Skärmbild:** `slices-1440/v3c-1440--s06.png` motsvarighet: högerspalten bär en hel hårlinjeram med glyfen påbörjad; `process-390/…-life-01.png`: ramen hel under rubriken. Felet: `shots/loop-3/slices-1440/v3c-1440--s06.png`, `process-390/v3c-390-life-01.png`.
- **Feel check:** scrolla in i processakten: arket kommer in och sluter sig till en ram medan rubriken läses; sedan ritas glyfen.
- **Done when:** H-15 bockad utan not om entrén.
