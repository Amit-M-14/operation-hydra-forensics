# WHOIS Analysis Notes — Operation Hydra Sample Domains

> **All records below are SIMULATED for coursework purposes.**
> No live WHOIS queries were run against these domains, since they are
> fictional constructs created for this assignment and do not resolve to
> real registered infrastructure. This document instead documents (a)
> what a real investigator checks in a WHOIS record and why, and (b) a
> plausible simulated record per sample, in the format a real registrar
> lookup would return.

## 1. What a real investigator looks for in WHOIS

| Field | Why it matters for spoofing/phishing investigations |
|---|---|
| **Registrar** | Some registrars are known to be lax on abuse takedowns or popular with bulletproof hosting — a red flag by itself |
| **Creation date** | Domains registered days/weeks before a phishing campaign launches ("newly registered domain" / NRD) are a strong indicator; legitimate bank domains are typically years old |
| **Registrant / privacy proxy** | WHOIS privacy (redacted registrant) is common and not inherently malicious, but combined with an NRD and a lookalike name, it raises suspicion |
| **Nameservers** | Free/anonymous DNS providers, or nameservers shared across many other flagged domains, indicate bulk phishing infrastructure |
| **Registrant country vs. impersonated brand's country** | A domain impersonating an Indian bank registered through a registrar with no India presence, or with a registrant address in an unrelated country, is a mismatch worth noting |
| **Expiry date close to creation date** | Attackers often register the minimum 1-year term — throwaway infrastructure |

## 2. Simulated WHOIS records

### `secure-bank0nline.com` (phish-01-bank-alert.eml)

Domain Name: SECURE-BANK0NLINE.COM
Registrar: NameSilo, LLC [SIMULATED]
Creation Date: 2026-06-02T00:00:00Z (8 days before campaign)
Registry Expiry Date: 2027-06-02T00:00:00Z
Registrant Organization: REDACTED FOR PRIVACY
Registrant Country: PA (Panama) [SIMULATED]
Name Server: NS1.FREEDNS-HOSTING.NET
Name Server: NS2.FREEDNS-HOSTING.NET


**Assessment:** Newly registered (8 days old), privacy-redacted, free/anonymous DNS provider, registrant country unrelated to the impersonated bank — textbook disposable phishing domain profile.

### `vendor-invoices-corp.com` (phish-02-invoice-malware.eml)

Domain Name: VENDOR-INVOICES-CORP.COM
Registrar: Namecheap, Inc. [SIMULATED]
Creation Date: 2025-11-14T00:00:00Z (7 months before campaign)
Registry Expiry Date: 2026-11-14T00:00:00Z
Registrant Organization: REDACTED FOR PRIVACY
Registrant Country: US [SIMULATED]
Name Server: NS1.NAMECHEAPHOSTING.COM
Name Server: NS2.NAMECHEAPHOSTING.COM


**Assessment:** Older than the bank-alert domain and on a mainstream registrar/DNS — consistent with the earlier note that this domain has partial SPF/DMARC protection. Likely a domain aged deliberately to build reputation before use, or a compromised/purchased aged domain rather than a same-day throwaway.

### `upi-secure-verify.com` (phish-03-otp-harvest.eml)

Domain Name: UPI-SECURE-VERIFY.COM
Registrar: Alibaba Cloud Computing (Beijing) Co., Ltd. [SIMULATED]
Creation Date: 2026-06-10T00:00:00Z (3 days before campaign)
Registry Expiry Date: 2027-06-10T00:00:00Z
Registrant Organization: REDACTED FOR PRIVACY
Registrant Country: CN [SIMULATED]
Name Server: NS1.DNSPOD.NET
Name Server: NS2.DNSPOD.NET


**Assessment:** Extremely newly registered (3 days), no SPF/DKIM/DMARC at all (per Step 4c), privacy-redacted, registrant country unrelated to Indian UPI infrastructure — highest-confidence disposable phishing domain of the three.

## 3. Cross-reference with SPF/DKIM/DMARC findings

The WHOIS age pattern correlates with the email authentication findings: the two domains with **zero** DNS authentication records (`secure-bank0nline.com`, `upi-secure-verify.com`) are also the two **most recently registered**, consistent with attacker infrastructure that's stood up fast and burned fast. `vendor-invoices-corp.com`, the oldest domain with partial protection, matches its "MODERATE RISK" verdict — supporting the theory that it may be a pre-aged or compromised legitimate-adjacent domain rather than throwaway infrastructure.