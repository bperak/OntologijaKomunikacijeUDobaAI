#!/usr/bin/env python3
"""Provjera META-UPUTA (ZAPIS-019).

Čita docs/meta-upute.yaml, pokreće `provjera` za svaku uputu i traži `ocekivano` u izlazu.
Generira i docs/META-UPUTE.md (pregled za čitanje) — generirana datoteka se ne uređuje ručno.

Uporaba:  python3 kod/check_meta.py [--samo MU-18] [--tiho]
Izlaz:    0 ako sve prođe; 1 ako ijedna uputa padne (uz ispis što je palo).
"""
import os
import re
import subprocess
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YAML = os.path.join(KOR, "docs", "meta-upute.yaml")
IZLAZ = os.path.join(KOR, "docs", "META-UPUTE.md")


def ucitaj():
    """Minimalni čitač našega YAML-a (bez ovisnosti): vraća listu dictova iz `upute:`."""
    telo = open(YAML, encoding="utf-8").read()
    telo = telo[telo.index("upute:"):]
    zapisi, trenutni = [], None
    for red in telo.splitlines():
        m = re.match(r"\s*-\s*id:\s*(\S+)", red)
        if m:
            trenutni = {"id": m.group(1)}
            zapisi.append(trenutni)
            continue
        m = re.match(r'\s+([a-z]+):\s*"?(.*?)"?\s*$', red)
        if m and trenutni is not None and m.group(1) in (
                "vrsta", "pravilo", "izvor", "obuhvat", "provjera", "ocekivano", "status"):
            trenutni[m.group(1)] = m.group(2).replace('\\"', '"')
    return zapisi


def main():
    tiho = "--tiho" in sys.argv
    samo = None
    if "--samo" in sys.argv:
        samo = sys.argv[sys.argv.index("--samo") + 1]
    upute = ucitaj()
    redovi, padovi = [], []
    for u in upute:
        if samo and u["id"] != samo:
            continue
        r = subprocess.run(["bash", "-c", u["provjera"]], cwd=KOR, capture_output=True, text=True)
        izlaz = r.stdout + r.stderr
        status = u.get("status", "provjereno automatski")
        rucno = status.startswith("ručni pregled")
        ok = (u["ocekivano"] in izlaz) or rucno
        redovi.append((u["id"], u["vrsta"], u["pravilo"], status, ok, u["ocekivano"]))
        if not ok:
            padovi.append((u["id"], u["provjera"], u["ocekivano"], r.returncode,
                           " ".join(izlaz.split())[-260:]))
    if not tiho:
        print(f"{'id':<7}{'vrsta':<13}{'ishod':<8}{'status':<26}pravilo")
        for i, v, p, s, ok, o in redovi:
            oznaka = "· pregled" if s.startswith("ručni pregled") else ("✔" if ok else "✘ PAD")
            print(f"{i:<7}{v:<13}{oznaka:<8}{s[:26]:<26}{p[:60]}")
        print(f"\nprovjereno: {len(redovi)} meta-uputa · prošlo: {sum(1 for r in redovi if r[4])} · "
              f"palo: {len(padovi)}")
        for i, c, o, rc, iz in padovi:
            print(f"\n  ✘ {i}: očekivano „{o}\" (exit {rc})\n     {c}\n     …{iz}")

    # generiraj pregled za čitanje
    with open(IZLAZ, "w", encoding="utf-8") as f:
        f.write("*GENERIRANO skriptom `kod/check_meta.py` iz `docs/meta-upute.yaml` — ne uređivati ručno.*\n\n")
        f.write("# META-UPUTE — sve upute, provjerljive\n\n")
        f.write("*Svaka uputa ima provjeru: `provjera` se pokreće, a `ocekivano` mora se pojaviti u izlazu. "
                "Ako uputa nema provjeru, nije meta-uputa nego želja.*\n\n")
        f.write(f"**Stanje provjere:** {sum(1 for r in redovi if r[4])}/{len(redovi)} prolazi.\n\n")
        f.write("| id | vrsta | pravilo | status |\n|---|---|---|---|\n")
        for i, v, p, s, ok, o in redovi:
            f.write(f"| `{i}` | {v} | {p} | {s} |\n")
        f.write("\n## Kako se pokreće\n\n```bash\npython3 kod/check_meta.py            # sve upute\n"
                "python3 kod/check_meta.py --samo MU-18\n```\n")
    return 1 if padovi else 0


if __name__ == "__main__":
    sys.exit(main())
