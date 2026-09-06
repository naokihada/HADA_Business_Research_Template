# Data Model Sketch — Business Research Template

**Status:** Design proposal (not implemented)  
**Related:** [001-reference-to-generic-architecture.md](../analysis/001-reference-to-generic-architecture.md)

This document defines CSV column contracts and Markdown section contracts for the generic template. Internal field names use English. User-entered display values may be Japanese or English.

---

## 1. Master Candidate CSV

**Path:** `data/master/candidates_master.csv`

### Required Columns

| Column | Type | Description |
|---|---|---|
| `candidate_id` | string | Stable ID; format `{wave_prefix}-{seq}` configured per project |
| `canonical_slug` | string | kebab-case; used in filenames |
| `display_name` | string | Primary display name |
| `organization` | string | Company or org name if applicable |
| `entity_type` | enum | `ORGANIZATION`, `INDIVIDUAL`, `PRODUCT`, `SERVICE`, `UNKNOWN` |
| `phone` | string | Optional |
| `address` | string | Optional |
| `city` | string | Optional |
| `region` | string | State/province/prefecture |
| `country` | string | ISO country or free text |
| `postal_code` | string | Optional |
| `website` | string | URL |
| `source` | string | Discovery source key |
| `referral` | string | Referral provenance summary |
| `wave_id` | string | e.g. `wave1`, `wave2` |
| `research_status` | enum | See §4 |
| `canonical_candidate_id` | string | If duplicate row; points to canonical |
| `notes` | string | Free text |

### Optional Extension Columns (Domain Config)

Domain packs add columns only through documented extensions, e.g.:

- `license_number`, `license_region` (regulated professions)
- `product_category`, `pricing_model` (vendor/product research)

Do not add domain columns to the base template CSV without marking them as extensions.

---

## 2. Scoring Results CSV

**Path:** `research/<project-id>/scoring/scoring_results.csv`

### Core Columns

| Column | Description |
|---|---|
| `candidate_id` | FK to master |
| `candidate_name` | Snapshot for readable exports |
| `slug` | canonical_slug |
| `score_total` | Numeric total |
| `{dimension_id}` | One column per rubric dimension from config |
| `gate_{gate_id}` | YES / NO / LIKELY / UNKNOWN per configured gate |
| `confidence` | HIGH / MEDIUM / LOW |
| `recommendation` | A / B / C / D |
| `shortlist_tier` | TIER_1 / TIER_2 / TIER_3 / EXCLUDED |
| `qc_status` | Aggregate QC state |
| `key_unknowns` | Semicolon-separated summary |
| `last_checked` | ISO date |

Dimension columns are **not fixed** in the base template. The scoring rubric config declares dimension IDs and max points.

---

## 3. QC Summary CSV (Generic Pattern)

**Path:** `research/<project-id>/scoring/{qc_module}_summary.csv`

Each optional QC module defines its own columns but should include:

| Column | Description |
|---|---|
| `candidate_id` | FK to master |
| `qc_module` | Module key |
| `qc_pass` | YES / NO / SKIPPED |
| `risk_level` | Module-specific enum |
| `confidence` | Evidence confidence for this QC |
| `last_checked` | ISO date |
| `notes` | Free text |

The CPA project's `reputation_risk_summary.csv` and `final_license_entity_qc.csv` are **examples** of module-specific schemas, not template defaults.

---

## 4. Status Enumerations

### research_status (base)

| Value | Meaning |
|---|---|
| `DISCOVERED` | Known but not researched |
| `NOT_RESEARCHED` | In master; pending |
| `RESEARCHING` | In progress |
| `RESEARCHED` | Dossier complete |
| `QC_PENDING` | Awaiting QC |
| `QC_PASS` | Passed required QC |
| `QC_FAIL` | Failed required QC |
| `SHORTLISTED` | On active shortlist |
| `EXCLUDED` | Removed from consideration |
| `DUPLICATE` | Non-canonical duplicate row |
| `INACTIVE` | Entity inactive/closed |
| `UNVERIFIED` | Existence not confirmed |

Domain extensions (config only): e.g. `NON_CPA`, `WRONG_CATEGORY`, `NOT_ELIGIBLE`.

### eligibility_status

| Value | Meaning |
|---|---|
| `ELIGIBLE` | Passes gates for deep research |
| `NOT_ELIGIBLE` | Fails hard gate |
| `CONDITIONAL` | Partial fit; needs confirmation |
| `UNKNOWN` | Insufficient evidence |

### gate_status

| Value | Meaning |
|---|---|
| `YES` | Verified positive |
| `NO` | Verified negative |
| `LIKELY` | Strong indirect support; not fully verified |
| `UNKNOWN` | Not confirmed |

---

## 5. Evidence Classification

| Value | Meaning |
|---|---|
| `VERIFIED` | Directly supported by reliable evidence |
| `STATED` | Claimed by candidate/vendor |
| `RECOMMENDED` | Third-party referral |
| `ASSESSED` | Researcher assessment |
| `UNKNOWN` | Insufficient evidence |
| `REQUIRES_CONFIRMATION` | Must confirm directly before reliance |

---

## 6. Source Tier

| Value | Typical Sources (configurable labels) |
|---|---|
| `TIER_1_OFFICIAL` | Official website, government/regulatory |
| `TIER_2_PROFESSIONAL` | Professional directories, published credentials |
| `TIER_3_REFERRAL` | Known contact recommendation |
| `TIER_4_GENERAL_WEB` | Search snippets, review sites, social media |

---

## 7. Candidate Dossier Markdown Contract

**Path:** `research/<project-id>/candidates/<slug>.md`

### Required Sections

1. **Identity** — candidate_id, names, entity type, key contacts, research date
2. **Entity Resolution** — canonical entity, duplicates, identity confidence
3. **Capability Matrix** — rows from `verification_checklist` config; columns: requirement, status, evidence
4. **Fit Assessment** — geographic, communication, engagement (as configured)
5. **Evidence Index** — links to evidence files
6. **Strengths / Weaknesses / Unknowns / Questions**
7. **Scoring Reference** — pointer to scoring CSV row; no unexplained numbers
8. **Recommendation Summary** — category + one-paragraph rationale

Sections may include Japanese prose. Section headings in templates can be bilingual comments for author guidance.

---

## 8. Evidence Record Markdown Contract

**Path:** `research/<project-id>/evidence/<phase>/<candidate_id>-<topic>.md`

### Required Fields

- candidate_id
- phase / module
- research date
- summary verdict (if QC-style)
- claims table: claim | classification | source_url | access_date | confidence | notes
- limitations section

---

## 9. Research Log Format

**Path:** `logs/research/<project-id>.md`

Markdown table:

| Date | Project | Action | Artifact | Notes |

One row minimum per bounded AI task or manual research session.

---

## 10. Contacts Master CSV (Optional Module)

**Path:** `data/master/contacts_master.csv`

| Column | Description |
|---|---|
| `record_type` | PERSON, ORGANIZATION, INTROducer |
| `name` | |
| `organization` | |
| `role` | |
| `email` | |
| `phone` | |
| `website` | |
| `location` | |
| `introduced_by` | |
| `relationship` | |
| `status` | |
| `notes` | |

---

## 11. Configuration Files (Proposed)

### project.yaml

```yaml
project_id: 2026-09-example-search
domain_pack: null
evidence_mode: live
title: 例示プロジェクト
candidate_type: service_provider
default_report_language: ja
waves:
  - id: wave1
    prefix: W1
    master_file: candidates_master.csv
modules:
  - reputation-review-qc
  - regulatory-license-qc
```

### eligibility_gates.yaml

```yaml
gates:
  - id: core_capability_1
    label_ja: コア要件1
    required_for_shortlist: true
    hard_fail_values: [NO]
  - id: engagement_timeline
    label_ja: エンゲージメント開始時期
    required_for_shortlist: false
```

### scoring_rubric.yaml

```yaml
max_total: 100
dimensions:
  - id: core_capability
    label_ja: コア能力
    max_points: 25
  - id: fit_local
    label_ja: 地域・コミュニケーション適合
    max_points: 10
recommendation_rules:
  A: { min_score: 75, min_confidence: MEDIUM, max_hard_gate_failures: 0 }
```

Exact YAML syntax is illustrative; Markdown-first config is acceptable for v1.

---

## 12. Language Handling

| Layer | Language |
|---|---|
| CSV column headers | English |
| Enum values | English |
| Config IDs | English |
| Config labels (`label_ja`) | Japanese for display |
| Dossier body | User choice; template defaults Japanese guidance |
| Final reports | Config default `ja`; optional `en` |

No duplicate JP/EN enum sets. Reports translate labels at render time if needed.
