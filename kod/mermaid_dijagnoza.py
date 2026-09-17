#!/usr/bin/env python3
"""Zašto 14.6 ne prolazi? Vidi odgovor poslužitelja."""
import json
import os

import paramiko

kod = open("/home/agent/knjiga-emergencija/figure/izvori/dijagram-14-6-funkcionalno-intrinzicno.mmd",
           encoding="utf-8").read()
klijent = paramiko.SSHClient()
klijent.set_missing_host_key_policy(paramiko.AutoAddPolicy())
klijent.connect("72.62.48.157", port=22, username="benedikt",
                pkey=paramiko.RSAKey.from_private_key_file(os.path.expanduser("~/.ssh/id_hermes")), timeout=20)
sftp = klijent.open_sftp()
for f in ("svg", "png"):
    with sftp.open("/tmp/dij_payload.json", "w") as fh:
        fh.write(json.dumps({"code": kod, "format": f, "theme": "default"}))
    _, out, err = klijent.exec_command(
        f"curl -s -X POST http://localhost:3333/render -H 'Content-Type: application/json' "
        f"-d @/tmp/dij_payload.json -o /tmp/dij_out.{f}; echo \"--exit:$?\"; head -c 300 /tmp/dij_out.{f}",
        timeout=180)
    print(f"=== {f} ===")
    print(out.read().decode("utf-8", errors="replace")[:600])
klijent.close()
