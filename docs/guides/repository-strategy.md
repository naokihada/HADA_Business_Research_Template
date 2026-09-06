# Repository Strategy

**Date:** 2026-09-06

Three-repository model for the Business Research Template ecosystem.
Public repositories exist on GitHub. This document describes how they relate.

---

## Repositories

| Repository | Visibility | Purpose |
|---|---|---|
| **HADA_Business_Research_Template** | Public | This repository — reusable generic template |
| **HADA_Business_Research_Template_Sample** | Public | Runnable fictional demonstration |
| **HADA_Business_Research_Template_Dev** | Private | Development source (not required to use Template) |

---

## HADA_Business_Research_Template (Public)

### Contains

- Generic research engine (AGENTS.md, templates, prompts, tools)
- Cursor rules (relative paths)
- Generic example project config (`config/research/_example_project/`)
- Optional domain packs with **fictional** data only
- Design and user guides
- Apache 2.0 LICENSE
- CI validation workflow

### Does not contain

- Real candidate datasets
- Private client requirements
- Internal development phase reports
- Execution logs from real research

---

## HADA_Business_Research_Template_Sample (Public)

### Contains

- Fictional cloud vendor comparison demo (`research/2026-09-cloud-vendor-example/`)
- Simulated evidence clearly labeled
- Minimal engine files needed for standalone validation
- Project config and master data for the demo

### Purpose

Show newcomers a working tree without requiring a full research cycle first.

---

## HADA_Business_Research_Template_Dev (Private)

Private development repository for template engineering history, internal analysis,
and reference-derived design work. Not required to use the public Template.

---

## How Template Is Derived

1. Copy PUBLIC-TEMPLATE classified files from Dev
2. Remove development-only documentation and logs
3. Generalize README and AGENTS.md for public users
4. Verify validator and prompt audit pass
5. Tag a release (for example v0.1.0) after commit and push

---

## How Sample Demonstrates Template

1. Start from Template release content
2. Add complete fictional cloud vendor research outputs
3. Label all evidence as simulated
4. Document the demo in Sample README

Sample is not a second engine — it is Template usage plus demonstration data.

---

## Must Never Copy into Public Repositories

| Content | Reason |
|---|---|
| Real candidate master CSV | Private / identifying |
| Personal requirements | Private |
| Real firm names, contacts, licenses | Identifying |
| Evidence with real private URLs | Identifying / stale |
| Scoring results for real candidates | Private research output |

Concepts only: gates, waves, QC phases, evidence model, shortlist tiers.

---

## Related Documents

- [sample-repository-plan.md](sample-repository-plan.md)
- [migration-from-cpa-research.md](migration-from-cpa-research.md)
