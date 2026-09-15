#!/usr/bin/env python3
"""Parses raw .eml headers and flags spoofing indicators."""
import sys, re, email
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

def parse_eml(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        msg = email.message_from_file(f)

    from_addr = msg.get("From", "")
    reply_to = msg.get("Reply-To", "")
    return_path = msg.get("Return-Path", "")
    received = msg.get_all("Received", [])
    message_id = msg.get("Message-ID", "")

    def domain_of(addr):
        m = re.search(r"@([\w\.-]+)", addr or "")
        return m.group(1).lower() if m else None

    from_dom = domain_of(from_addr)
    rp_dom = domain_of(return_path)
    rt_dom = domain_of(reply_to)

    flags = []
    if rp_dom and from_dom and rp_dom != from_dom:
        flags.append(f"Return-Path domain ({rp_dom}) != From domain ({from_dom}) — classic spoof indicator")
    if rt_dom and from_dom and rt_dom != from_dom:
        flags.append(f"Reply-To domain ({rt_dom}) != From domain ({from_dom}) — redirect harvesting risk")
    if from_dom and "." in from_dom and from_dom.count(".") >= 2 and any(k in from_dom for k in ["-", "0", "verify", "secure"]):
        flags.append(f"From domain ({from_dom}) matches lookalike/typosquat pattern")

    origin_ip = None
    if received:
        m = re.search(r"\[([\d\.]+)\]", received[0])
        if m:
            origin_ip = m.group(1)

    return {
        "file": Path(path).name,
        "from": from_addr, "from_domain": from_dom,
        "reply_to": reply_to, "return_path": return_path,
        "message_id": message_id, "origin_ip": origin_ip,
        "flags": flags,
    }

if __name__ == "__main__":
    for p in sys.argv[1:]:
        r = parse_eml(p)
        print(f"\n=== {r['file']} ===")
        for k, v in r.items():
            if k == "flags":
                continue
            print(f"{k}: {v}")
        print("Flags:")
        for f in r["flags"]:
            print(f"  ⚠ {f}")