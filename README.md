# Operation Hydra — Cybercrime Forensics Simulation

Coursework simulation for Assignment 2 (Unit 2: Types of Cyber Crimes).
All phishing emails, malware payload, transaction logs, and WHOIS
records are **fabricated for educational purposes** — no live
lookups were performed against real infrastructure, and no functional
malware is included anywhere in this repository.

## Structure
- `01-classification/` — crime decomposition & legal mapping (IT Act, IPC, CFAA, GDPR, Budapest Convention)
- `02-phishing-spoofing/` — 3 simulated phishing samples, header/SPF/DKIM/DMARC analysis, WHOIS notes
- `03-malware-analysis/` — simulated payload structure, IOCs, analysis report
- `04-financial-fraud/` — dummy transaction data, fraud-tracing script, report
- `05-report/` — final Legal-Ethical-Impact-Report.docx
- `tools/` — parser and checker scripts used across the analysis

## Setup
```bash
uv sync
uv run tools/email_header_parser.py 02-phishing-spoofing/samples/*.eml
uv run tools/spf_dkim_checker.py
uv run 04-financial-fraud/trace_fraud.py
```

## Authorship
[Amit Mohanty / 2301730325] — [Cyber Crime Investigation and Forensics]. All analysis and code
written for this assignment; no external malware or live attack
infrastructure used.