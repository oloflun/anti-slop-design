# Kontrakt r5 — tre varianter av M1, en agent per cell

Cellerna: `cells/V1-chain`, `cells/V2-chain`, `cells/V3-chain`, var och en `index.html` +
`scrollcraft.js/.css` (oförändrade kopior) + `NOTES.md` + `shots/`. Utgångspunkt: kopiera
`../alunix-concepts-r4/cells/M1-chain/index.html` och bygg om enligt brief.md + din rad nedan.

| V | hero-bild och presentation | Hyperborea i blå blocket | scroll för resten av sidan | signature move | källor |
|---|---|---|---|---|---|
| V1 Dokumentär band | `k4-cabin-desk.webp` i färg, men **inte** fullbleed-med-text-i-hörnet: heron är ett band där fotot tar 62 % till höger och rubrik + underrad står i en cream-panel till vänster (Public Sans 300, hårlinje), fotot beskuret till fönsterljuset | figuren blir en **fullbreddsremsa** under tesblockets text (16:6, hela blockets bredd, bildtext i mono under), aldrig halvt utanför | **wipes**: varje panel `reveal` växelvis left/right när den passerar, jätterubriken `kinetic lines`, ledgern `in` med stagger, grunden `drift` i tre stopp, fotot i heron `parallax` -1.2 | cream-panelen i heron **glider över fotot** i takt med scrollen (från 62/38 till 100 % panel) innan den släpper | insign (tjänsteband), creative-giants, rre-ventures |
| V2 Cinematisk tvätt | `k1-stage-beams.webp` under svart tvätt (planhat: en enda filmisk bild, rubriken centrerad i stor skala, sedan hårt klipp till ljust), rubrik Public Sans 300 i 8cqw, underrad Literata-lik serif ej tillåten: använd Public Sans 400 | **ingen figur** i blå blocket (bara typ, luftigare), Hyperborea blir i stället en **tredje exempelram** under Calyx i vänsterspalten (`/sites/hyperborea.html`, egen kicker) | **lager**: hero-fotot sjunker (parallax -1.5) medan rubriken stiger; blå blocket **pinnat** (`pin`, span 2) där texten hälsar och en andra rad korsar; foton parallax, text rise ≤ 90 px; grunden `drift` | den svarta tvätten i heron **lättar** i takt med scrollen (opacity från 0.72 → 0.2 via `--sc-p`) så bilden framträder först när man lämnar den | planhat, mattis-studio, veloura |
| V3 Plåt i grunden | `k1-stage-pool.webp` som en **inramad plåt** (marginal 6cqw runt om, hårlinje) på den mörka grunden, rubriken **utanför bilden** ovanför plåten i affischskala (Public Sans 300, 9cqw), underraden under plåten till höger | figuren som en **plåt som medvetet bleeder** ut över blockets högerkant (Mattis-devicen, R5:s källa) men helt inom viewporten vid 1440: max 12 % av bildens bredd utanför blocket, med bildtextband till vänster om bilden | **typografiskt**: ledgerns tre rader **scrubbas ord för ord** ur scrollen (vintergatan) med tråd, Hōrai öppnar med `iris` (en gång), jätterubriken skalar 0.92 → 1 från `--sc-p`, tjänsterna `in` med stagger, grunden `drift` | ljuspölen i hero-plåten **vandrar**: bildens `object-position` styrs av `--sc-p` så ljuset flyttar sig när man scrollar (bespoke, aldrig kit-parameter) | vintergatan, mattis-studio, garden-eight |

Fingerprint mellan V1–V3: ≤ 2/6 delade (grammatik får delas eftersom alla är M1: räkna hero-device,
aktform, signature move, blå blockets figur, scrollfamilj, avslut).

## Gemensamt

- `Skill(design)` laddas via Skill-verktyget. NOTES.md: reference lock, decision ledger,
  känslokurva, topp, tell-someone, signature move, device-tabell per akt, fingerprint-rad,
  luck-mätningen (spalt, panel→panel, px, vh), verifieringssiffror.
- Inga sub-agenter, inga ändringar utanför den egna cellen, ingen commit, ingen ny copy.
