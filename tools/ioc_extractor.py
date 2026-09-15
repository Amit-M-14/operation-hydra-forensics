#!/usr/bin/env python3
"""Pulls all IOCs from iocs.md into a flat list — used in CI/reporting."""
import sys, re

sys.stdout.reconfigure(encoding="utf-8")

def extract(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    rows = re.findall(r"\|\s*(`[^`]+`|\S.*?)\s*\|\s*(`[^`]+`|\S.*?)\s*\|", text)
    return [(a.strip("` "), b.strip("` ")) for a, b in rows if a not in ("IOC Type", "IOC", "---")]

if __name__ == "__main__":
    for ioc_type, value in extract("03-malware-analysis/iocs.md"):
        print(f"{ioc_type}: {value}")