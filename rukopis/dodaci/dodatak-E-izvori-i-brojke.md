# Dodatak E — Izvori, podaci i provjera brojki

Ovaj dodatak nije popis literature — literatura je u `referencije/REFERENCE_BASE.md`. Ovo je **evidencija brojki**: svaka brojka koja se u knjizi pojavljuje ima ovdje svoj redak, s izvorom, datumom i **vrstom**. Pravilo je iz 4.5: *brojka bez izvora, datuma i vrste nije brojka*, i provjerava se automatski (`kod/check_fakti.py --strict`). Tablica se generira iz `data/fakti.csv` skriptom `kod/evidencija_build.py`.

**Stanje (generirano):** zapisa 35 · izvedeno: 2 · mjereno: 24 · procjena: 9.

---

## E.1 Zašto je vrsta brojke dio tvrdnje

- **mjereno** — vrijednost je očitana s izvora ili izmjerena u vlastitom postavu; smije nositi tvrdnju.
- **procjena** — vrijednost je procijenjena (modelom, ekstrapolacijom ili autorovom procjenom); nikad se ne prikazuje kao mjerenje i uvijek se navodi uz datum i metodu procjene.
- **izvedeno** — vrijednost je izračunata iz drugih brojki u ovoj evidenciji; uz nju se navodi iz čega je izvedena.

Uz svaku se brojku bilježi i **datum izvora**, jer se predmet knjige mijenja brže od knjige: brojka bez datuma ne može se ni provjeriti ni ispraviti.

## E.2 Brojke — mjereno

| brojka | jedinica | izvor | datum | gdje se pojavljuje | napomena |
|---|---|---|---|---|---|
| 125 | leksema | Ban Kirigin & Perak 2020 (Rasprave IHJJ 46(2): 957-996); Perak 2014; EmoCNet 2019-21 | 2020 | `razine/6` | mreža hrvatskih emocionalnih leksema sa 'strah' u središtu |
| 139255 | neurona | Dorkenwald et al. 2024 (Nature) | 2024 | `razine/10;razine/12` | užiži mozak vinske mušice; video o konektomu navodi pogrešnu brojku 166 |
| 50000000 | sinapsi | Dorkenwald et al. 2024 (Nature) | 2024 | `razine/10;razine/12` | ~50 milijuna |
| 395 | organizacija | GreyNoise (2026; 9. rujna) | 2026 | `razine/13` | napadacka kampanja s AI agentima; PaperCut NG/MF |
| 11 | ciljeva | GreyNoise (2026; 9. rujna) | 2026 | `razine/13` | u jednom naletu (26 sekundi) |
| 26 | sekundi | GreyNoise (2026; 9. rujna) | 2026 | `razine/13` | trajanje naleta u kojem je pogođeno 11 ciljeva |
| 734 | parametara | Lappalainen et al. 2024 (Nature 634:1132–1140) | 2024 | `razine/10;razine/12` | model aktivnosti 64 tipa neurona iz konektoma |
| 64 | tipova neurona | Lappalainen et al. 2024 (Nature) | 2024 | `razine/10;razine/12` |  |
| 9 | sekundi | METR 2025 (arXiv:2503.14499) | 2020 | `razine/10` | vremenski horizont zadatka na 50 % |
| 16 | sati | METR 2026 (napomena uz graf) | 2026 | `razine/10` | mjerenja iznad 16 h nepouzdana sa sadašnjim skupom zadataka (METR: Measurements above 16 hrs are unreliable with our current task suite) |
| 825 | pojavnica | Perak 2014 (doktorski rad: tiskana str. 304) | 2014 | `razine/6` | prijedložni izraz od straha - drugi po čestotnosti |
| 17 | pojavnica | Perak 2014 (doktorski rad: tiskana str. 369) | 2014 | `razine/6` | konstrukcija mijesati se sa strahom |
| 131.8 | Mw | Perak 2014 (doktorski rad; sažetak izvornika) | 2014 | `razine/6` | Hrvatski nacionalni korpus |
| 14875 | pojavnica | Perak 2014 (doktorski rad; sažetak izvornika) | 2014 | `razine/6` | pojavnice leme strah u HNK-u |
| 978-953-361-147-1 | ISBN | Perak 2025 (FFRI) | 2025 | `docs/CITIRANJE.md` | elektroničko izdanje |
| 8594 | riječi | Perak 2026 (IUC Dubrovnik; govorne bilješke) | 2026 | `—` | predavanje kao kondenzat knjige |
| 4096 | dimenzija | Qwen Team 2025 (arXiv:2506.05176) | 2025 | `razine/4;razine/10` | vlastiti mjerni postav (spark-embed) |
| 3 | domene | Searle 1995;2010 | 1995 | `razine/2;razine/3` | materijalna / psihološka / društvena |
| 93.8 | % | Thompson 2026 (Gemini 3 Pro; 11/2025) | 2025 | `razine/10` | rezultat pri zasićenju GPQA; strop je niži (~80%) |
| 50 | % | Thompson 2026 (Mapping) | 2025 | `razine/10` | GPT-5.2 na HLE (prosinac 2025) |
| 92.3 | % | Thompson 2026 (o1-preview; 9/2024) | 2024 | `razine/10` | rezultat pri zasićenju MMLU; strop ~91% |
| 300 | dimenzija | fastText pretrenirani vektori cc.hr.300 (vlastiti mjerni postav) | 2026 | `razine/10` | slika 10.2 izrađena je na ovome instrumentu — nije isti model kao ostatak knjige (Qwen3-Embedding 4096 dim.) |
| 512 | tokena | provider documentation 2026 | 2020 | `razine/10` | povijesna vrijednost ranih modela |
| 10000000 | tokena | provider documentation 2026 | 2026 | `razine/10` | kontekstni prozori 2026 |

## E.3 Brojke — procjena

| brojka | jedinica | izvor | datum | gdje se pojavljuje | napomena |
|---|---|---|---|---|---|
| 51.3 | % | FutureHouse (7/2025) preko Thompsona 2026 | 2025 | `razine/10` | uncontroversially correct strop HLE; Alibaba (2/2026; arXiv:2602.13964v2) navodi 25.6% — u knjizi se navode oba izvora |
| 10 | % | Grace et al. (2024; JAIR) | 2024 | `razine/16` | 10% do 2027 i 50% do 2047 (anketa 2.778 istraživača) |
| 10-20 | % | Hinton (2024; The Guardian) | 2024 | `razine/16` | izumiranje u ~30 godina - procjena |
| 10 | % | Hubinger (2026); prenose CNBC i BBC | 2026 | `razine/16` | vjerojatnost "pobiti sve ljude" u desetljeću - procjena stručnjaka; ne mjerenje |
| 12 | sati | METR 2026 (ispravak 3.3.2026; prvotna procjena 14.5 h od 20.2.2026) | 2026 | `razine/10` | Claude Opus 4.6; METR je ispravio bug u modeliranju i spustio vrijednost s 14.5 h na ~12 h |
| 80 | % | Thompson 2026 (Mapping IQ/MMLU/MMLU-Pro/GPQA/HLE; ažurirano 4.8.2026) | 2026 | `razine/10` | GPQA strop ~80% (zavisi od podskupa); zasićen 11/2025 (Gemini 3 Pro 93.8%); Anthropic prestao izvještavati GPQA od 6/2026; ISPRAVAK: u izlaganju je bilo navedeno 90% |
| 90 | % | Thompson 2026 (Mapping) | 2026 | `razine/10` | zasićen 11/2025 (Gemini 3 Pro 90.1%) |
| 91 | % | Thompson 2026 (Mapping; analiza UoE) | 2026 | `razine/10` | zasićen 9/2024 (o1-preview 92.3%) |
| 700 | agenata | prema izvještajima (Fortune, CNN, Taipei Times) | 2026 | `razine/12;razine/13` | broj agenata u koordiniranom napadu - nije potvrđena mjera |

## E.4 Brojke — izvedeno

| brojka | jedinica | izvor | datum | gdje se pojavljuje | napomena |
|---|---|---|---|---|---|
| 16 | razina | Perak OMLCC (izlaganja 2017a; 2017b; integralno neobjavljen) | 2017 | `razine/2;razine/3;kom2025/3` | autorov okvir; domene prema Searleu |
| 5000 | x (umnožak) | izvedeno iz context_window_small i context_window_large | 2026 | `razine/10` | 512 → 10 M |

## E.5 Ispravljene brojke

Popis ispravaka vodi se u `docs/ISPRAVKE.md`. Tri brojke koje su mijenjane nakon provjere jesu:

- **metr_horizon_2026** (12 sati) — ISPRAVAK-001: METR je 3. 3. 2026. ispravio bug u modeliranju; prvotna procjena 14,5 h spuštena je na ~12 h (vrijednosti iznad 16 h nepouzdane su sa sadašnjim skupom zadataka — zapis `metr_unreliable_above`).
- **gpqa_ceiling** (80 %) — ISPRAVAK-003: skala je zasićena (11/2025 Gemini 3 Pro 93,8 %), pa se ~80 % prikazuje kao povijesna vrijednost, ne kao trenutni strop; u izlaganju je bilo navedeno 90 %.
- **hle_ceiling** (51.3 %) — ISPRAVAK-002: rezultat HLE navodi se s OBA izvora (51,3 % FutureHouse 7/2025; 25,6 % Alibaba 2/2026, arXiv:2602.13964v2) — nijedan se ne navodi kao jedini točan.

## E.6 Kako se brojka provjerava

```bash
python3 kod/check_fakti.py --strict   # svaka brojka u tekstu ↔ evidencija
```

Alat traži brojke s jedinicom u rukopisu i provjerava da za svaku postoji zapis; prijavljuje i dvostruke identifikatore te vrste koje nisu dopuštene. Kada nalaz postoji, ispravlja se **tekst ili evidencija** — nikad oboje napola.

## E.7 Izvori podataka korišteni u knjizi

- Ban Kirigin & Perak 2020 (Rasprave IHJJ 46(2): 957-996); Perak 2014; EmoCNet 2019-21
- Dorkenwald et al. 2024 (Nature)
- FutureHouse (7/2025) preko Thompsona 2026
- Grace et al. (2024; JAIR)
- GreyNoise (2026; 9. rujna)
- Hinton (2024; The Guardian)
- Hubinger (2026); prenose CNBC i BBC
- Lappalainen et al. 2024 (Nature 634:1132–1140)
- Lappalainen et al. 2024 (Nature)
- METR 2025 (arXiv:2503.14499)
- METR 2026 (ispravak 3.3.2026; prvotna procjena 14.5 h od 20.2.2026)
- METR 2026 (napomena uz graf)
- Perak 2014 (doktorski rad: tiskana str. 304)
- Perak 2014 (doktorski rad: tiskana str. 369)
- Perak 2014 (doktorski rad; sažetak izvornika)
- Perak 2025 (FFRI)
- Perak 2026 (IUC Dubrovnik; govorne bilješke)
- Perak OMLCC (izlaganja 2017a; 2017b; integralno neobjavljen)
- Qwen Team 2025 (arXiv:2506.05176)
- Searle 1995;2010
- Thompson 2026 (Gemini 3 Pro; 11/2025)
- Thompson 2026 (Mapping IQ/MMLU/MMLU-Pro/GPQA/HLE; ažurirano 4.8.2026)
- Thompson 2026 (Mapping)
- Thompson 2026 (Mapping; analiza UoE)
- Thompson 2026 (o1-preview; 9/2024)
- fastText pretrenirani vektori cc.hr.300 (vlastiti mjerni postav)
- izvedeno iz context_window_small i context_window_large
- prema izvještajima (Fortune, CNN, Taipei Times)
- provider documentation 2026

> Zajednička evidencija brojki (sve tri knjige)
> Pravilo: svaka brojka koja se pojavljuje u više od jedne knjige ima ovdje JEDAN redak.
> vrsta: mjereno | procjena | izvedeno (izračunato iz drugih brojki u evidenciji)
> Provjera: kod/check_fakti.py
