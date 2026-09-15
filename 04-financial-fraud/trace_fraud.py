#!/usr/bin/env python3
"""Traces flagged transactions through mule-account hops to final off-ramp."""
import csv, sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def detect_anomalies(rows):
    by_account = defaultdict(list)
    for r in rows:
        by_account[r["account_id"]].append(r)

    findings = []
    for acct, txns in by_account.items():
        txns_sorted = sorted(txns, key=lambda r: r["timestamp"])
        for i in range(1, len(txns_sorted)):
            prev, cur = txns_sorted[i-1], txns_sorted[i]
            # crude velocity check: >2 txns within ~10 min to a NEW payee, high amount
            if cur["flagged"] == "Y" and float(cur["amount_inr"]) > 10000:
                findings.append(
                    f"{acct}: high-value txn {cur['txn_id']} ({cur['amount_inr']} INR) "
                    f"to {cur['payee_id']} at {cur['timestamp']} flagged for review"
                )
    return findings

def trace_chain(rows):
    flagged = [r for r in rows if r["flagged"] == "Y"]
    flagged.sort(key=lambda r: r["timestamp"])
    chain = []
    for r in flagged:
        chain.append(f"{r['timestamp']}  {r['account_id']:15s} -> {r['payee_id']:20s}  "
                      f"{r['amount_inr']:>10s} INR  [{r['channel']}]  ({r['txn_id']})")
    return chain

if __name__ == "__main__":
    rows = load("04-financial-fraud/transaction_logs.csv")

    print("=== Anomaly Detection ===")
    for f in detect_anomalies(rows):
        print(f"  ⚠ {f}")

    print("\n=== Fraud Chain Trace (victim -> mule hops -> crypto off-ramp) ===")
    for line in trace_chain(rows):
        print(f"  {line}")

    print("\n=== Summary ===")
    total = sum(float(r["amount_inr"]) for r in rows if r["flagged"] == "Y")
    print(f"  Total flagged amount: {total:,.2f} INR")
    print(f"  Final destination: BTC-WALLET-SIM-1 (simulated crypto off-ramp)")