# Dodatak A — Postavljanje okruženja

Knjiga ne traži posebnu opremu, ali traži da se **zna što je bilo na ulazu**. Ovaj dodatak opisuje najmanje okruženje u kojemu se svi postupci iz praktikuma mogu ponoviti, i to tako da rezultat bude provjerljiv. Ništa od navedenoga nije uvjet za razumijevanje tvrdnji knjige — kod se u svakom poglavlju može preskočiti bez gubitka tvrdnje.

---

## A.1 Što je potrebno

| sastavnica | čemu služi | napomena |
|---|---|---|
| **Python 3.11+** (ili Google Colab) | izračuni, mreže, ugrađivanja | Colab je dovoljan za sve vježbe 🟢 i 🟡 |
| **poslužitelj ugrađivanja** s OpenAI-uspravnim sučeljem (`/v1/embeddings`) | pretvorba jedinica u vektore | model i **verzija** se obavezno zapisuju; u ovoj je knjizi rabljen Qwen3-Embedding (Qwen Team 2025) |
| **program za mrežnu analizu** | izračun gustoće, modularnosti, skupina | dovoljan je Python uz biblioteku za grafove; vizualni alat je kazalo, a ne mjera |
| **repozitorij knjige** | skripte za provjere, evidencija brojki, baza referenci | `kod/`, `data/`, `referencije/` |

## A.2 Najmanji radni postav

1. **Zapis o okruženju.** Prije prvoga mjerenja u datoteku se upiše: inačica Pythona, naziv i verzija modela ugrađivanja, inačica korpusa i datum pristupa. Bez toga se rezultat ne može ponoviti, a ni usporediti s kasnijim.
2. **Provjera veze s poslužiteljem ugrađivanja.** Uputa mora završavati na `/v1`; ako model traži istu dimenziju za sve ulaze, miješanje dviju inačica daje grešku oblika, a ne pogrešan broj — i to je dobro, jer se pogreška vidi odmah.
3. **Normalizacija prije mjere.** Kosinusna srodnost računa se na normaliziranim vektorima; ako su sve vrijednosti blizu jedinice, mjera nije kosinus nego norma (→ pogl. 10.7).
4. **Fiksiranje jedinica.** Popis jedinica sprema se u jednu datoteku i uz njega se upisuje kontrolni zbroj. Popis se između dvaju mjerenja ne mijenja (→ dodatak D.1).
5. **Provjere prije zaključka.** Prije nego se nalaz napiše, pokreću se provjere iz repozitorija:

```bash
python3 kod/check_fakti.py --strict   # svaka brojka ima redak u data/fakti.csv
python3 kod/check_lit.py              # svaki citat ima izvor u referencije/REFERENCE_BASE.md
python3 kod/check_cisto.py            # higijena zapisa (homoglifi, nazivlje, markeri)
python3 kod/check_links.py            # upute i poveznice
```

## A.3 Reproducibilnost: četiri stavke uz svaki rezultat

Rezultat je reproducibilan ako uz njega stoje: **verzija podataka** (korpus i inačica), **verzija postupka** (jedinica, mjera, prag, broj dimenzija, vrsta udaljenosti), **verzija modela** (ugrađivanja iz različitih inačica nisu ista mjera) i **kontrolni zapis (checksum) uz licencu** (bez toga se ne može utvrditi je li reproduciran isti skup podataka). Te su četiri stavke u knjizi navedene u 4.5 i u praktikumima; ovdje su izdvojene jer se u praksi najčešće preskaču.

## A.4 Što okruženje ne rješava

Okruženje ne rješava nijedno od pitanja koja knjiga postavlja. Ono omogućuje samo jedno: da se tvrdnja o razini **pretvori u mjerni zadatak** i da se taj zadatak može ponoviti — uključujući i ponavljanje koje nalaz **obara**. Ako se postupak ne može ponoviti, nalaz ne pripada knjizi, nego bilježnici.

## A.5 Licenca i citiranje

Materijali u repozitoriju knjige objavljeni su pod licencom **CC BY-NC 4.0** (uz obavezno navođenje autorstva); komercijalna uporaba nije dopuštena, a prerade jesu uz navođenje izvora. Način citiranja knjige i njezinih dijelova opisan je u `docs/CITIRANJE.md`, a strojno čitljiv zapis u `CITATION.cff`.
