# Financial Fraud Tracing Report
## Operation Hydra — Transaction Flow Analysis

## 1. Scenario

Two victim accounts (`ACC-VICTIM-01`, `ACC-VICTIM-02`) had credentials
captured via the malware payload analyzed in `03-malware-analysis/`.
Between 2026-06-13 18:22 and 2026-06-14 10:05, unauthorized UPI/IMPS
transfers moved funds out of both accounts.

## 2. Anomaly Detection Logic

`trace_fraud.py` flags transactions over ₹10,000 marked as anomalous
in the log — in a real system this would instead be a live rules
engine (velocity checks, new-payee risk scoring, geo-mismatch), which
is noted here as the production equivalent of the simplified CSV flag
used for this simulation.

## 3. Fund Flow

Three flagged transfers from `ACC-VICTIM-01` (₹49,500 + ₹49,500 +
₹49,000 = ₹148,000, each kept just under a hypothetical ₹50,000
reporting threshold — a classic **structuring** pattern) land in
`ACC-MULE-A`. A fourth flagged transfer from a second victim
(`ACC-VICTIM-02`, ₹62,000) also lands in `ACC-MULE-A`, confirming it
as a shared collection point across multiple victims rather than a
one-off.

From `ACC-MULE-A`, funds move in a single IMPS hop to `ACC-MULE-B`
(₹145,000), then to `ACC-MULE-C` (₹140,000), before exiting to a
simulated Bitcoin wallet (`BTC-WALLET-SIM-1`, ₹138,000) — three hops
in under 90 minutes, consistent with layering to break the audit
trail before an off-ramp to a harder-to-trace asset.

## 4. Total Traced

₹138,000+ moved from two victims through three mule accounts to a
crypto off-ramp within roughly 16 hours of the initial malware
compromise.

## 5. Investigative Implications

- The sub-₹50,000 structuring pattern across three consecutive
  transfers from the same victim is itself a flaggable pattern
  independent of the absolute amount.
- A shared mule account (`ACC-MULE-A`) receiving funds from two
  distinct compromised victims is strong evidence linking the two
  infections to the same campaign/operator.
- The crypto off-ramp is the hardest point to trace further without
  exchange-level KYC cooperation — this is exactly the tension
  discussed in the ethical section of the final report.