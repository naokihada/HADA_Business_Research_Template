# Sample Repository Plan

**Target repository:** `HADA_Business_Research_Template_Sample`  
**Date:** 2026-09-06

---

## Purpose

Provide a public, runnable demonstration of the Business Research Template without requiring users to execute a full research cycle from scratch.

The Sample repository is **not** the Template. It is Template plus demonstration artifacts.

---

## Primary Demo Scenario

**Cloud backup vendor comparison** (fictional example)

Why not CPA for primary Sample:

- Neutral domain — easier for general audience
- No professional licensing confusion
- Still demonstrates gates, scoring, QC, shortlist, reports

---

## Planned Contents

```text
HADA_Business_Research_Template_Sample/
├── README.md
├── AGENTS.md, prompts/, templates/, tools/
├── data/master/
│   ├── candidates_master.csv
│   └── requirements.md
├── config/research/2026-09-cloud-vendor-example/
├── research/2026-09-cloud-vendor-example/
│   ├── candidates/
│   ├── evidence/                # SIMULATED labeled
│   ├── scoring/
│   ├── shortlist/
│   └── reports/
└── logs/research/
```

---

## evidence_mode

Primary demo: **simulated**

Every evidence file and report must state:

- Fictional vendors
- example.invalid URLs
- Not real product recommendations

---

## Relationship to Template

| Repo | Role |
|---|---|
| Template | Reusable skeleton users copy |
| Sample | Template usage plus filled fictional project |
| Dev | Private engineering history |

Sample should reference Template release version after the user creates the tag
(for example v0.1.0). The tag is not created until after commit and push.

---

## User Journey

1. Clone Sample repository
2. Read README — understand simulated demo
3. Open final report under research/
4. Trace backward through scoring → evidence → dossiers
5. Read config/research/ — see domain configuration
6. Run validator on the demo project
7. Fork Template to start your own project

---

## What Sample Must Not Contain

- Real candidate data
- Private client requirements
- CPA domain pack (optional advanced example stays in Template only)
- Dev phase analysis documents

---

## Related

- [repository-strategy.md](repository-strategy.md)
