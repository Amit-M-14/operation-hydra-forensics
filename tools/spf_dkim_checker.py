#!/usr/bin/env python3
"""Evaluates SPF/DKIM/DMARC against a SIMULATED DNS record set (no live lookups)."""

# Simulated DNS TXT records for the fictional sender domains in our samples
SIMULATED_DNS = {
    "secure-bank0nline.com": {"spf": None, "dkim": None, "dmarc": None},
    "vendor-invoices-corp.com": {"spf": "v=spf1 -all", "dkim": None, "dmarc": "v=DMARC1; p=none"},
    "upi-secure-verify.com": {"spf": None, "dkim": None, "dmarc": None},
}

def evaluate(domain, sending_ip):
    rec = SIMULATED_DNS.get(domain, {"spf": None, "dkim": None, "dmarc": None})
    result = {"domain": domain, "spf": "FAIL", "dkim": "FAIL", "dmarc": "FAIL", "verdict": ""}

    if rec["spf"] is None:
        result["spf"] = "FAIL — no SPF record published, any host can send as this domain"
    elif "-all" in rec["spf"]:
        result["spf"] = "PASS (hard fail policy present)"

    result["dkim"] = "FAIL — no DKIM signature / key published" if rec["dkim"] is None else "PASS"

    if rec["dmarc"] is None:
        result["dmarc"] = "FAIL — no DMARC record, spoofed mail has no enforcement policy to be rejected by"
    elif "p=none" in rec["dmarc"]:
        result["dmarc"] = "WEAK — DMARC present but policy is monitor-only (p=none), spoofed mail still delivered"

    fails = sum(1 for v in [result["spf"], result["dkim"], result["dmarc"]] if "FAIL" in v)
    result["verdict"] = "HIGH SPOOFING RISK" if fails >= 2 else "MODERATE RISK"
    return result

if __name__ == "__main__":
    samples = [
        ("secure-bank0nline.com", "185.220.101.44"),
        ("vendor-invoices-corp.com", "45.153.160.2"),
        ("upi-secure-verify.com", "103.224.182.9"),
    ]
    for dom, ip in samples:
        r = evaluate(dom, ip)
        print(f"\n=== {dom} (sending IP {ip}) ===")
        for k, v in r.items():
            print(f"{k}: {v}")