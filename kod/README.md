# kod/ — skripte za analize i figure

Ovdje idu skripte koje proizvode **brojke, tablice i figure** koje se citiraju u rukopisu.

## Načelo
Svaka figura u knjizi mora biti **reproducibilna**: skripta + ulazni podaci + verzija modela. Ako se figura ne može reproducirati, ne ulazi u knjigu.

## Planirane skripte (po poglavljima)

| poglavlje | skripta | što proizvodi |
|---|---|---|
| 4 | `pipeline_tekst_mreza_vektor.py` | cjevovod: korpus → ko-okurencija → mreža → vektori (Qwen3-Embedding, 4096 dim.) |
| 6 | `mreza_emocija.py` | mreža 125 hrvatskih emocionalnih leksema (*strah* u središtu) |
| 6 | `mjere_mreze.py` | gustoća, modularnost, centralnost + interpretacijske ograde |
| 10 | `geometrija_vlastiti_podaci.py` | srodnost, klasteri, vizualizacija (t-SNE/UMAP) |
| 10 | `provjera_brojki.py` | provjera svake brojke iz dodatka E na primarnom izvoru |
| 14 | `tablica_razine_12_16.py` | funkcionalno / intrinzično / nema — po agentskim sustavima |

## Konvencije
- Python 3, `requirements.txt` uz svaku veću skriptu.
- Ulazni podaci se **ne** commituju ako su veliki (vidi `data/README.md`).
- U zaglavlju skripte: što radi, ulaz, izlaz, verzije modela i biblioteka, datum.
- Negativni rezultati se **prijavljuju** (mapa `kod/negativni/`), ne brišu.
