#!/usr/bin/env python3
"""mapa_knjige.py — mjeri SADRŽAJNU mapu knjige: povezanost, motivaciju, primjere, primjene.

Za svaku datoteku:
  - odjeljci (## i ###), riječi
  - izlazne upute (→ pogl. N, → dodatak X) i ULAZNE upute (koliko ih drugi upućuju na nju)
  - ima li: tezu/motivaciju („Teza poglavlja", naslov s „Zašto"/„Kako"/„Što"), radni primjer,
    praktikum, vježbe, sažetak, ključne pojmove, literaturu
  - broj primjera („primjer", „slučaj"), primjena/postupaka i provjera
  - broj nepotvrđenih jedinica (❓) i oznaka vrste dokaza (mjereno/procjena/izvedeno)
"""
import glob
import os
import re
import sys

B = "/home/agent/knjiga-emergencija/rukopis/"
GENERIRANO = {"sadrzaj.md", "dodatak-E-izvori-i-brojke.md", "dodatak-G-kazalo.md"}


def analiza(put):
    t = open(put, encoding="utf-8").read()
    proza = re.sub(r"^[|#>].*$", " ", t, flags=re.M)
    rijeci = len(re.findall(r"[^\W\d_]+", re.sub(r"[*_`]", " ", proza), re.UNICODE))
    izlaz = re.findall(r"→\s*pogl\.\s*([0-9]+)", t) + re.findall(r"→\s*dodatk\w*\s*([A-Z])", t)
    return {
        "rijeci": rijeci,
        "h2": len(re.findall(r"^## ", t, re.M)),
        "h3": len(re.findall(r"^### ", t, re.M)),
        "izlaz": izlaz,
        "teza": len(re.findall(r"Teza poglavlja|> \*Teza", t)),
        "radni": len(re.findall(r"[Rr]adni primjer", t)),
        "praktikum": len(re.findall(r"[Pp]raktikum", t)),
        "vjezbe": len(re.findall(r"^### Vježbe", t, re.M)),
        "sažetak": len(re.findall(r"^### Sažetak", t, re.M)),
        "pojmovi": len(re.findall(r"^### Ključni pojmovi", t, re.M)),
        "lit": len(re.findall(r"^### Literatura", t, re.M)),
        "primjer": len(re.findall(r"\bprimjer\w*", t, re.I)),
        "slucaj": len(re.findall(r"\bslučaj\w*", t, re.I)),
        "primjena": len(re.findall(r"\bprimjen\w*", t, re.I)),
        "postupak": len(re.findall(r"\bpostup\w*|\bkorak\w*|\bprotokol\w*", t, re.I)),
        "provjera": len(re.findall(r"\bprovjer\w*|\btest\w*|\bobor\w*", t, re.I)),
        "usporedba": len(re.findall(r"\bne tvrdi\b|\bne stoji\b|\bgranic\w*|\bograda\w*", t, re.I)),
        "ne_potvrdjeno": t.count("❓"),
        "mjereno": len(re.findall(r"\bmjereno\b", t)),
        "procjena": len(re.findall(r"\bprocjena\b", t)),
        "izvedeno": len(re.findall(r"\bizvedeno\b", t)),
    }


def main():
    pogl = sorted(glob.glob(B + "poglavlje-*.md"))
    ostalo = sorted([p for p in glob.glob(B + "*.md") + glob.glob(B + "dodaci/*.md")
                     + glob.glob(B + "studije-slucaja/*.md")
                     if os.path.basename(p) not in GENERIRANO and not os.path.basename(p).startswith("poglavlje-")])
    ulaz = {}
    svi = {}
    for p in pogl + ostalo:
        m = analiza(p)
        svi[p] = m
        for c in m["izlaz"]:
            ulaz[c] = ulaz.get(c, 0) + 1
    print(f"{'datoteka':<40}{'riječi':>7}{'##':>4}{'###':>5}{'izlaz':>6}{'ulaz':>6}{'teza':>5}{'radni':>6}"
          f"{'prakt':>6}{'vjež':>5}{'saž':>4}{'pojm':>5}{'lit':>4}{'primj':>6}{'primjena':>9}{'provj':>6}{'❓':>4}")
    for p, m in svi.items():
        ime = os.path.relpath(p, B)
        broj = re.sub(r"\D", "", os.path.basename(p))
        u = ulaz.get(broj, 0) if broj else ulaz.get(os.path.basename(p)[:1].upper(), 0)
        print(f"{ime:<40}{m['rijeci']:>7}{m['h2']:>4}{m['h3']:>5}{len(m['izlaz']):>6}{u:>6}{m['teza']:>5}"
              f"{m['radni']:>6}{m['praktikum']:>6}{m['vjezbe']:>5}{m['sažetak']:>4}{m['pojmovi']:>5}{m['lit']:>4}"
              f"{m['primjer']:>6}{m['primjena']:>9}{m['provjera']:>6}{m['ne_potvrdjeno']:>4}")
    print("\nIZLAZNE UPUTE po cilju:", dict(sorted(ulaz.items(), key=lambda x: -x[1])))
    print("ukupno riječi:", sum(m["rijeci"] for m in svi.values()))


if __name__ == "__main__":
    sys.exit(main())
