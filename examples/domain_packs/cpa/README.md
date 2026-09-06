# CPA Domain Pack (Fictional / Sanitized)

This domain pack demonstrates how **US CPA / tax professional selection** research
maps to the generic Business Research Template — without modifying the generic engine.

## Why This Pack Exists

A real-world regulated-profession research workflow validated the architecture
(gates, evidence, scoring, QC waves, shortlist). This pack proves the same
complexity can live entirely in **domain configuration** without engine changes.

## What Is Generic (Engine)

- `AGENTS.md`, templates, prompts, Cursor rules
- Gate / score / confidence / recommendation separation
- Evidence tiers and classifications
- Research waves, entity resolution, QC module pattern
- Logging and master-data protection

## What Is CPA-Specific (This Pack Only)

- Tax gates: federal individual, California, S-Corp, historical file review
- Capability criteria: Schedule C, IRS representation, cross-border, estate
- Scoring dimensions: core tax, business fit, IRS controversy, cross-border, etc.
- QC: regulatory license verification (simulated in fictional example)
- Geographic scope: Silicon Valley / Bay Area (fictional scenario)
- Japanese-first reports for user-facing output

## Fictional Candidates (Exactly 3)

| ID | Name | Demonstrates |
|---|---|---|
| FCPA-001 | Bay Mesa Tax Partners LLP | Clearly eligible — strong gates and score |
| FCPA-002 | Tanaka Crossborder Advisory | Eligibility uncertainty — UNKNOWN gates |
| FCPA-003 | Redwood Financial Planning Inc | Excluded — not a CPA/tax practice (gate NO) |

**All data is fictional.** URLs use `example.invalid`. No real people, firms,
license numbers, or contact details from the reference repository.

## Optional QC Modules Enabled

| Module | Status in pack |
|---|---|
| source_quality_review | enabled |
| consistency_review | enabled (top 2) |
| regulatory_verification | enabled (simulated evidence) |
| reputation_review | disabled (optional) |

## Evidence Mode

The bundled research example uses `evidence_mode: simulated` in project.yaml.
Evidence files are clearly marked as **simulated** for workflow demonstration —
not real external research.

## Architecture Borrowed from Reference (Concepts Only)

Conceptual patterns from a private regulated-profession research project:

- Master vs research separation
- Gate checklist before scoring
- 100-point multi-dimensional rubric
- Score ≠ confidence
- QC phases before shortlist
- Shortlist tiers not score-only
- Research log audit trail
- Japanese-first final reports

**Not copied:** real candidate dataset, personal requirements, introductions,
Facebook content, real firm names, or any PII.

## How to Use

1. Copy `config/` to `config/research/<your-project-id>/`
2. Copy `data/candidates_master.csv` to your master data location
3. Set `domain_pack: cpa` and `evidence_mode: live` for real research
4. Create `research/<your-project-id>/` and run bounded prompts

See the cloud vendor demonstration in `HADA_Business_Research_Template_Sample`
for a complete fictional pipeline walkthrough.

## Do Not

- Treat fictional outputs as real CPA recommendations
- Copy this pack into generic engine files
- Import real CPA candidate data into the public template
