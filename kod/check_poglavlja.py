#!/usr/bin/env python3
"""Provjera uputa izrečenih RIJEČIMA i tvrdnji o samome rukopisu (ZAPIS-017).

Numeričke upute („→ pogl. 7.5") provjerava `check_refs.py`. Ovaj alat pokriva ono što on ne vidi:

1. **Upute riječima** — „u petom poglavlju", „četrnaesto poglavlje" — ispisuje ih s kontekstom jer se
   njihova ispravnost ne može odlučiti automatski, ali se moraju pregledati (na ovome je nađeno da
   pogl. 1 upućuje na peto poglavlje za razinu 14, a razina 14 je u sedmome).
2. **Tvrdnje o vlastitu rukopisu** — „knjiga ima N poglavlja", „tablica pokriva N poglavlja" — te se
   automatski uspoređuju sa stvarnim brojem poglavlja i stvarnim brojem redaka tablice u 16.4.
   (Na ovome je nađeno da je tekst tvrdio petnaest poglavlja, a tablica imala četrnaest redaka.)

Uporaba:  python3 kod/check_poglavlja.py [--strogo]
"""
import os
import re
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUKOPIS = os.path.join(KOR, "rukopis")
if "--dir" in sys.argv:
    RUKOPIS = sys.argv[sys.argv.index("--dir") + 1]
BROJEVI = {"prv": 1, "drug": 2, "treć": 3, "četvrt": 4, "pet": 5, "šest": 6, "sedm": 7, "osm": 8,
           "devet": 9, "deset": 10, "jedanaest": 11, "dvanaest": 12, "trinaest": 13, "četrnaest": 14,
           "petnaest": 15, "šesnaest": 16}
RIJECIMA = re.compile(r"\b(" + "|".join(BROJEVI) + r")\w{0,3}\s+poglavlj\w*", re.I)
TVRDNJA = re.compile(r"\b(ima|pokriva|sadrži|obuhvaća|navodi)\s+\*{0,2}(\w+)\s+poglavlj\w*\*{0,2}", re.I)


def broj(riječ):
    for k, v in BROJEVI.items():
        if riječ.lower().startswith(k):
            return v
    return {"dva": 2, "tri": 3, "četiri": 4, "pet": 5}.get(riječ.lower())


def main():
    strogo = "--strogo" in sys.argv
    poglavlja = sorted(f for f in os.listdir(RUKOPIS) if re.match(r"poglavlje-\d+\.md$", f))
    stvarno = len(poglavlja)
    print(f"poglavlja u rukopisu: {stvarno}\n")
    print("=== 1. UPUTE IZREČENE RIJEČIMA (za pregled) ===")
    uk = 0
    for ime in ["uvod.md", "predgovor.md"] + poglavlja + ["zakljucak.md"]:
        p = os.path.join(RUKOPIS, ime)
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        for m in RIJECIMA.finditer(t):
            uk += 1
            print(f"  {ime:<20} → pogl. {broj(m.group(1)):<3} …{' '.join(t[max(0, m.start()-90):m.end()+110].split())}")
    print(f"  ukupno: {uk}\n")

    print("=== 2. TVRDNJE O VLASTITU RUKOPISU (automatska provjera) ===")
    nalazi = []
    for ime in ["uvod.md", "predgovor.md"] + poglavlja + ["zakljucak.md"]:
        p = os.path.join(RUKOPIS, ime)
        if not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        for m in TVRDNJA.finditer(t):
            n = broj(m.group(2))
            if n is None:
                continue
            kon = " ".join(t[max(0, m.start()-120):m.end()+120].split())
            ok = (n == stvarno)
            print(f"  {'OK ' if ok else '⚠  '}{ime:<20} „{m.group(0).strip()}\"")
            if not ok:
                nalazi.append(f"{ime}: tvrdnja „{m.group(0).strip()}\" (stvarno {stvarno})\n      …{kon}…")

    # tablica u 16.4 mora imati redak za svako poglavlje
    p16 = os.path.join(RUKOPIS, "poglavlje-16.md")
    if os.path.exists(p16):
        t = open(p16, encoding="utf-8").read()
        seg = t[t.find("| pogl. |"):t.find("## 16.5")]
        redci = [l for l in seg.splitlines() if l.startswith("|") and not set(l) <= set("|- ")]
        redci = [l for l in redci if not l.startswith("| pogl. |")]
        print(f"  {'OK ' if len(redci)==stvarno else '⚠  '}poglavlje-16.md     tablica 16.4 ima {len(redci)} redaka "
              f"(poglavlja: {stvarno})")
        if len(redci) != stvarno:
            nalazi.append(f"poglavlje-16.md: tablica 16.4 ima {len(redci)} redaka, a poglavlja je {stvarno}")
    print("\n=== NALAZI ===")
    print("\n".join("  ⚠ " + n for n in nalazi) if nalazi else "  nema nalaza")
    return 1 if (nalazi and strogo) else 0


if __name__ == "__main__":
    sys.exit(main())
