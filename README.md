# 🚀 AEO Vanguard Agency: Autonomous Multi-Agent AI System

An autonomous agency designed for **Answer Engine Optimization (AEO)**, built using the `ai-employees` role architecture. The agency autonomously monitors, tests, and optimizes enterprise brand visibility across next-generation generative AI engines (ChatGPT, Perplexity, Claude, Gemini).

---

## 🔗 Live Artifacts & Deliverables
* **Live Google Sheet Activity Ledger:** [AEO Agency Ledger](https://docs.google.com/spreadsheets/d/1gg-cqQ1Fctq1Cmq1PFBdkBdMntjxho6NtMOg9IJhk2E/edit?usp=sharing)
* **Configuration:** [`.installed.json`](.installed.json)
* **Automation Bridge Script:** [`pm_bridge.py`](pm_bridge.py)

---

## 👥 The 8-Employee Autonomous Team

| Employee ID | Role Name | Primary Responsibility |
|---|---|---|
| **Agent 1** | **Project Manager (Chief of Staff)** | Audits all 7 agents, updates the Google Sheet ledger, signs client SOWs, and dispatches daily email digests. |
| **Agent 2** | **Lead LLM Researcher** | Deploys synthetic prompt batteries across LLMs to map category citations and competitor visibility. |
| **Agent 3** | **Knowledge Architect** | Authors structured information assets, `llms.txt`, FAQ schemas, and comparison matrices. |
| **Agent 4** | **SoM Performance Analyst** | Computes Share of Model (SoM) percentages, audits hallucinations, and monitors sentiment polarity. |
| **Agent 5** | **Consensus Builder** | Distributes technical benchmarks across authoritative LLM feeder hubs (Reddit, GitHub, tech blogs). |
| **Agent 6** | **Technical AEO Auditor** | Manages JSON-LD / Schema.org microdata, audits robots.txt, and ensures seamless AI crawler ingestion. |
| **Agent 7** | **Solution Engineer** | Bridges generated AEO data with client CMS platforms (WordPress, Webflow) and handles technical sync. |
| **Agent 8** | **Outbound Growth Lead** | Scans target SaaS domains for zero-visibility gaps in LLMs and dispatches automated cold audit reports. |

---

## ⚙️ Automated Integration Architecture

```
[Agent 8: Outbound Lead] ➔ Scans prospect zero-visibility gaps & books discovery calls
       ↓
[Agent 1: Project Manager] ➔ Generates AEO SOW contract & initializes client in ledger
       ↓
[Agents 2, 6, 3, 5, 7] ➔ Execute technical audits, schema injection, llms.txt & Reddit distribution
       ↓
[Agent 4: Performance Analyst] ➔ Measures Share of Model (SoM) shift & verifies 0 hallucinations
       ↓
[Agent 1: Project Manager] ➔ Appends logs to Google Sheets & dispatches executive email bulletin
```

---

## 🚀 Running the Automation Bridge

Execute the orchestration bridge locally:

```bash
python3 pm_bridge.py
```

The script will:
1. Sequentially execute cycles for all 8 agents.
2. Push rows to the live Google Sheet in format: `[Timestamp | Agent Name | Task Performed | Output Status]`.
3. Trigger an executive HTML status bulletin directly to leadership's inbox.
