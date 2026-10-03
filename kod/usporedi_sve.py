#!/usr/bin/env python3
"""usporedi_sve.py — za svaku datoteku ispisuje rezultat --usporedi (citati/godine/brojke/naslovi/upute)."""
import importlib.util
import os
import subprocess

B = "/home/agent/knjiga-emergencija/"
STARO = "/tmp/stil-staro"
spec = importlib.util.spec_from_file_location("cs", B + "kod/check_stil.py")
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

losih = []
for put in cs.datoteke():
    rel = os.path.relpath(put, B)
    stari = os.path.join(STARO, rel[len("rukopis/"):] if rel.startswith("rukopis/") else rel)
    r = subprocess.run(["python3", "kod/check_stil.py", "--usporedi", stari, put],
                       cwd=B, capture_output=True, text=True)
    izlaz = r.stdout
    gubitak = "sadržaj istovjetan" in izlaz
    oznaka = "OK " if gubitak else "!! "
    linije = [l.strip() for l in izlaz.splitlines() if "prije" in l or "izgubljeno" in l]
    print(f"{oznaka}{rel}")
    for l in linije:
        print("      ", l)
    if not gubitak:
        losih.append(rel)
print("\n=== datoteke s gubitkom:", losih if losih else "nijedna")
