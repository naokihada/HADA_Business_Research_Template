# Migration Guide — CPA Research Architecture to Generic Template

**Audience:** Developers familiar with the original CPA research workflow  
**Scope:** Conceptual mapping only — no real data migration

This guide explains how patterns from a real-world CPA candidate research project
map to the generic Business Research Template. It does **not** instruct copying
private candidate data.

---

## Overview

```text
Real CPA project (private)
    ↓ concepts extracted
Generic Template engine
    ↓ domain configuration
CPA domain pack (fictional example)
    ↓ user project
Your live CPA research (private — your data)
```

---

## Architecture Mapping

| CPA Project Concept | Generic Template Location |
|---|---|
| Project objective README | config/research/<id>/project.yaml + requirements |
| User tax/business requirements | data/master/requirements.md |
| CPA candidate master CSV | data/master/candidates_master.csv |
| VividNavi / referral import | discovery_sources.yaml + wave config |
| Per-candidate dossier | research/<id>/candidates/<slug>.md |
| Evidence folders by QC phase | research/<id>/evidence/<phase>/ |
| Eligibility gate checklist | eligibility_gates.yaml |
| Capability verification tables | capability_criteria.yaml + dossier |
| Scoring README (100-point rubric) | scoring_rubric.yaml |
| Confidence rules | confidence_rules.yaml |
| Shortlist rules | shortlist_rules.yaml |
| QC modules (review, license) | modules.yaml + optional evidence |
| Scoring CSV | research/<id>/scoring/scoring_results.csv |
| Unified ranking across waves | scoring/unified_ranking.csv + unified-ranking prompt |
| Research log | logs/research/<id>.md |
| Japanese final report | research/<id>/reports/YYYY-MM-DD-*-ja.md |
| AGENTS.md operating rules | Template AGENTS.md |
| Cursor rules | .cursor/rules/ |
| Bounded AI tasks | prompts/ |

---

## Candidate Master

**CPA:** `cpa_candidates_master.csv` with VN- prefixed IDs from directory import.

**Generic:**

- `candidates_master.csv` with configurable wave prefix (e.g. FCPA-, W1-)
- Columns: candidate_id, canonical_slug, wave_id, research_status, canonical_candidate_id
- Master = who is investigated — not what was proven

**Migration action:** Export your candidate list to generic CSV format. Replace source-specific prefixes via discovery_sources.yaml — do not hard-code VN in engine.

---

## Eligibility Gates

**CPA examples:**

- Federal individual tax
- California individual tax
- S-Corp taxation
- Historical file review
- Professional type (CPA vs financial planner)

**Generic:**

- eligibility_gates.yaml defines gate id, label, hard_fail_values
- Gate status: YES / NO / LIKELY / UNKNOWN
- UNKNOWN is not automatic failure

**Migration action:** Copy CPA gate definitions into domain pack or project config — not into AGENTS.md.

---

## Scoring Rubric

**CPA:** Seven dimensions totaling 100 points (core tax, cross-border, IRS, etc.)

**Generic:**

- scoring_rubric.yaml lists dimension id, max_points, labels
- Scoring CSV columns match dimension ids
- Score separate from confidence and recommendation

**Migration action:** Transcribe CPA scoring README weights into scoring_rubric.yaml. Retire prose-only rubric in research folder.

---

## QC Modules

| CPA QC | Generic Module |
|---|---|
| Reputation / review QC | reputation_review (optional, off by default) |
| License / entity QC | regulatory_verification (optional) |
| Source quality | source_quality_review |
| Dossier/scoring alignment | consistency_review |

**Migration action:** Enable modules in modules.yaml. Define module-specific evidence templates under research/evidence/.

---

## Research Waves

**CPA:** Wave 1 (VN-001–038) + Wave 2 (VN2-001–005 from BaySpo)

**Generic:**

- waves in project.yaml with id, prefix, source_key
- Entity resolution before unified ranking
- unified-ranking prompt merges canonical entities

**Migration action:** Configure waves per discovery source. Run entity-resolution prompt before unified-ranking.

---

## Evidence Model

**CPA:** VERIFIED / STATED classifications, source tiers, per-claim URLs

**Generic:** Same enums in AGENTS.md — domain-agnostic

**Migration action:** Map CPA evidence files to generic evidence_record.md template. Mark live vs simulated via evidence_mode in project.yaml.

---

## Shortlist

**CPA:** Tier 1/2/3, gate-heavy rules, contact priority separate from score

**Generic:** shortlist_rules.yaml — same pattern

**Migration action:** Transcribe shortlist_rules.md from CPA project into YAML. Fix rules before applying to candidates.

---

## What Not to Migrate

- Real candidate dossiers and evidence
- Personal requirements with identifying details
- Introduction and social media referral raw content
- Contact lists and email drafts with real addresses
- Any material marked confidential in original project

---

## Recommended Migration Steps

1. Clone generic Template (when published)
2. Copy CPA domain pack OR create config/research/<your-cpa-project>/
3. Define gates and rubric from your CPA requirements — in config only
4. Import sanitized candidate master (your data — stays private)
5. Run bounded prompts phase by phase
6. Enable QC modules as needed
7. Keep research outputs in private repo — do not publish client data

---

## Fictional Reference in Dev Repo

Dev repository includes:

- `examples/domain_packs/cpa/` — 3 fictional candidates
- `research/2026-09-cpa-fictional-example/` — simulated pipeline demo

Use these to understand mapping — not as real research results.

---

## Related

- [repository-strategy.md](repository-strategy.md)
- [new-project-bootstrap.md](new-project-bootstrap.md)
- [../analysis/001-reference-to-generic-architecture.md](../analysis/001-reference-to-generic-architecture.md)
