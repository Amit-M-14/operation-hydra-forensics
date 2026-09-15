# Cybercrime Decomposition & Legal Mapping
## Case: Operation Hydra — Multi-Vector Phishing, Spoofing & Financial Fraud Campaign

## 1. Scenario Summary

"Operation Hydra" is a simulated multi-stage cyber-crime campaign in
which attackers sent phishing emails from spoofed domains impersonating
a bank, tricked victims into opening a malicious attachment (a
keylogger/RAT), harvested banking credentials and OTPs, and used them to
execute unauthorized UPI/card transactions — routing the stolen funds
through money-mule accounts and simulated crypto wallets to obscure the
trail.

## 2. Attack Chain (Kill Chain View)

| Stage | Action | Crime Category |
|---|---|---|
| 1 | Attacker registers a lookalike domain (e.g. `secure-bank0nline.com`) | Spoofing / Cybersquatting |
| 2 | Mass phishing email sent impersonating the bank, spoofed sender header | Phishing / Email Spoofing |
| 3 | Victim opens malicious attachment; keylogger/RAT silently installs | Malware Distribution / Unauthorized Access |
| 4 | Malware exfiltrates banking credentials and OTPs to attacker C2 | Unauthorized Access / Data Theft / Identity Theft |
| 5 | Attacker uses stolen credentials to make fraudulent UPI/card transactions | Financial/Payment Fraud |
| 6 | Funds routed through mule accounts and simulated crypto wallets | Money Laundering |

## 3. Identified Crime Types (6 distinct crimes)

| # | Crime | Description |
|---|-------|-------------|
| 1 | Phishing | Fraudulent email impersonating a trusted entity to trick victims into revealing credentials |
| 2 | Email/Domain Spoofing | Forging sender headers and registering lookalike domains to appear legitimate |
| 3 | Malware Distribution & Unauthorized Access | Delivering a keylogger/RAT via attachment to gain unauthorized access to the victim's device |
| 4 | Identity Theft / Data Theft | Harvesting and using victims' credentials, OTPs, and personal data without authorization |
| 5 | Financial/Payment Fraud | Using stolen credentials to execute unauthorized UPI/card transactions |
| 6 | Money Laundering | Routing fraudulent proceeds through mule accounts and crypto wallets to obscure origin |

## 4. Legal Mapping

### 4.1 Indian IT Act, 2000 (as amended)

| Section | Provision | Applicability |
|---|---|---|
| Sec 66 | Computer-related offences (dishonest/fraudulent act under Sec 43) | Malware installation, unauthorized access |
| Sec 66C | Identity theft — fraudulent use of password/unique identification | Use of stolen credentials/OTPs |
| Sec 66D | Cheating by personation using computer resource | Phishing impersonation of the bank |
| Sec 43 | Unauthorized access, download, introduction of virus/contaminant | Keylogger/RAT installation on victim device |
| Sec 66F | Cyber terrorism (if scale/intent threatens critical infrastructure) | Only if campaign scale meets this threshold — noted for completeness |
| Sec 72 | Breach of confidentiality and privacy | Exfiltration of personal/financial data |

### 4.2 Indian Penal Code, 1860 (mirrored in BNS 2023)

| Section | Provision | Applicability |
|---|---|---|
| Sec 420 | Cheating and dishonestly inducing delivery of property | Fraudulent transactions using stolen credentials |
| Sec 463/465 | Forgery | Spoofed domain/email presented as genuine bank communication |
| Sec 468 | Forgery for purpose of cheating | Fabricated sender identity |
| Sec 471 | Using a forged document/electronic record as genuine | Victim relying on the spoofed email as authentic |
| Sec 120B | Criminal conspiracy | Coordinated multi-stage campaign involving multiple actors (phishing ops, mule handlers) |

### 4.3 Global Equivalents

| Framework | Provision | Applicability |
|---|---|---|
| **CFAA (US) — 18 U.S.C. § 1030** | Unauthorized access to a protected computer; fraud via computer access | Malware-based unauthorized access, credential theft |
| **GDPR (EU) — Art. 32, Art. 33** | Security of processing; breach notification duty | If any EU data subjects' personal data was exfiltrated, the victim organization would have breach-notification obligations |
| **Budapest Convention** Art. 2 | Illegal access | Malware-enabled device access |
| **Budapest Convention** Art. 7 | Computer-related forgery | Spoofed domain/email as forged electronic record |
| **Budapest Convention** Art. 8 | Computer-related fraud | Fraudulent financial transactions |
| **Budapest Convention** Art. 6 | Misuse of devices | Development/possession of the malware payload itself |

## 5. Summary Table (Crime → Law)

| Crime | IT Act | IPC | Global |
|---|---|---|---|
| Phishing | §66D | §420 | Budapest Art. 8 |
| Spoofing | §66D, §66C | §463, §468, §471 | Budapest Art. 7; CFAA §1030 |
| Malware/Unauthorized Access | §43, §66 | — | CFAA §1030; Budapest Art. 2, 6 |
| Identity/Data Theft | §66C, §72 | — | GDPR Art. 32/33; Budapest Art. 2 |
| Financial Fraud | §66D | §420 | Budapest Art. 8; CFAA §1030 |
| Money Laundering | §66, §43 (as instrumental crime) | §120B | Budapest Art. 25 (MLA); FATF standards (reference framework, not a treaty per se) |

## 6. Justification for Classification Approach

Crimes are grouped along the attack chain rather than alphabetically,
because in a multi-vector campaign like Hydra, each crime is a
*precondition* for the next: spoofing enables phishing to succeed,
phishing enables malware delivery, malware enables credential theft,
credential theft enables financial fraud, and financial fraud requires
laundering to be useful to the attacker. Mapping crimes to law in this
sequence also mirrors how a real investigation would build its case —
proving the spoofing/phishing first establishes intent and method, which
supports the fraud and laundering charges downstream.