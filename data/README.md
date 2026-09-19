# data/ — podaci knjige

## Što se verzionira, a što ne
- **Verzionira se:** mali, kurirani skupovi (leksikoni, anotacije, tablice brojki s izvorima) i **opisi podataka**.
- **Ne verzionira se:** veliki korpusi, arhive, binarne reprezentacije (vidi `.gitignore`).

## Planirani izvori

| izvor | što je | poglavlja | napomena |
|---|---|---|---|
| **hrWac** | hrvatski web-korpus (primarni korpus knjige) | 4, 6, 10 | pristup preko poslužitelja; ne commitati cijeli korpus |
| **EmoCNet (2019–21)** | mreža emocionalnih leksema iz hrWac-a | 6 | izvor za figuru `emotion_network.png` |
| **leksikon *strah*** | 125 hrvatskih emocionalnih leksema | 6 | ❓ potvrditi točnu publikaciju prije citiranja |
| **ugrađivanja (Qwen3-Embedding)** | vektori, 4096 dimenzija (vlastiti poslužitelj) | 4, 10 | zapisati **verziju modela** uz svaki rezultat |
| **Thompson (2026), Models Table** | veličine modela — **procjene** | 10 | označiti kao procjene, s datumom pristupa |
| **METR (2025)** | vremenski horizonti zadataka | 10 | *mjereno*, ali s ogradom o saturaciji skupa zadataka |

## Pravilo zapisa
Za svaki skup: **naziv · izvor · licenca · datum pristupa · verzija · kontrola (checksum)**. Bez toga se rezultat ne može reproducirati, a brojka se ne smije citirati u rukopisu.

## Popis jedinica u praktikumu 10.7 (`data/leksemi.txt`)
Praktikum u 10.7 traži da se popis jedinica **fiksira u jednoj datoteci** (`data/leksemi.txt`). Ta
datoteka **nije dio repozitorija**: knjiga svoj popis od 125 emocionalnih jedinica ne prenosi, nego ga
navodi izvorom (Perak 2014; EmoCNet 2019–21; Ban Kirigin & Perak 2020), pa je sastavlja onaj tko
postupak ponavlja — po vlastitome kriteriju, koji se u zapisu navodi. Ono što se od te datoteke traži
jest **kontrolni zbroj** popisa, jer se popis između dvaju mjerenja ne smije mijenjati.

## Negativni i neuspjeli rezultati
Spremaju se u `data/negativni/` i navode u rukopisu kad su relevantni za tvrdnju (vidi poglavlja 4 i 16).
