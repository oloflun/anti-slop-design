# Higgsfield-logg, K1 Skymning v2 (2026-09-06)

Tak: 35 credits (Antons beslut). Saldo före: 110 (plan Plus). Alla kostnader lästa med
`get_cost` innan körning.

| # | Steg | Modell | Indata | Kostnad | Utfall |
|---|---|---|---|---|---|
| 1 | Startbild | (ingen generering) | `runs/B/K1/assets/dusk.webp` (Rafael Peier, Unsplash) → `start-dusk.jpg` 2200×1467, media `91f4d481…` | 0 | uppladdad, bekräftad |
| 2 | Fönsterbeskärning som referens | (ingen generering) | `window-crop.jpg` 640×360 ur samma foto, media `c2496821…` | 0 | uppladdad |
| 3 | Slutbild | Nano Banana 2, 2k, 16:9, image-to-image | prompt: samma tända bågfönster på nära håll, varmt inre ljus fyller rutan, inga människor, inga skyltar | 2 | `end-window.png` 2752×1536; läst: bågfönster i sten med takrosett och ljuskrona bakom glaset, blå timme i glaset. Godkänd som slutruta. media `4ebd862d…` |
| 4 | Videotest | Kling 3.0 std, 10 s, 16:9, ljud av, start+end image | prompt: en enda långsam stadig dolly push-in från kajen mot det tända bågfönstret, inga klipp, inga människor, konstant skymningsljus, slutar med fönstret i hela rutan | 15 | `test-std.mp4` 1176×784, 24 fps, 10 s. Läst som 10 rutor (`test-std-sheet.png`): resan från kajen till bågfönstret håller, sista 3 s står stilla; en hallucinerad banderoll med oläsliga tecken t=4–6, resan går till gatunivå. Skickad till Anton för beslut om pro. Provisorisk sekvens i `runs/B/K1/assets/push/`. |

| 5 | Ny slutbild (Antons rättelse: fönstret bredvid porten, det nedre) | Nano Banana 2, 2k, 16:9, image-to-image | prompt: det tända bågkrönta bottenvåningsfönstret till vänster om entrén, kameran rakt framför, träspröjs, ingen port i bild | 2 | `end-window-2.png` 2752×1536; läst: bågkrönt fönster med spröjs, varmt inre, stenomfattning. Godkänd. jobb `ad7cd396…` (används som `end_image` via job-id) |

| 6 | Omtagning, slutmaterial (Antons ja till pro, 2026-09-07) | Kling 3.0 **pro**, 10 s, 16:9, ljud av, start = `91f4d481…`, end = jobb `ad7cd396…` | prompt: samma push-in, passerar porten till höger, slutar i det tända bågkrönta fönstret till vänster om entrén, aldrig i porten, inga skyltar | 17,5 | jobb `8e58cea5…` → `pro.mp4`; rutor i `pro-sheet.png` |

Kostnader totalt: 36,5 (taket 35 höjt av Anton med "Ja, kör pro").
