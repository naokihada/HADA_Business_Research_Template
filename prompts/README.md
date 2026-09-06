# Reusable Prompts

Curated bounded task prompts for AI-assisted research workflows.

## Usage

1. Read `AGENTS.md` and the active project config first.
2. Copy or reference the prompt for the requested phase only.
3. Provide explicit inputs: project_id, candidate IDs, batch scope.
4. After completion, append to `logs/research/<project-id>.md`.

## Formatting Rule (Mandatory)

Never use nested quotation structures in prompt files.

Do not place a quoted block inside another quoted block.

Prefer headings, bullet lists, file paths, and plain text.

## Prompt Index

| Phase | File |
|---|---|
| Candidate discovery | research/candidate-discovery.md |
| Dossier research | research/candidate-dossier.md |
| Entity resolution | research/entity-resolution.md |
| Evidence extraction | research/evidence-extraction.md |
| Eligibility evaluation | research/eligibility-evaluation.md |
| Capability evaluation | research/capability-evaluation.md |
| Scoring | scoring/run-scoring.md |
| Confidence assessment | scoring/confidence-assessment.md |
| Multi-wave unified ranking | scoring/unified-ranking.md |
| QC module | qc/run-qc-module.md |
| Shortlist | shortlist/generate-shortlist.md |
| Report | shortlist/generate-report.md |

## Multi-Wave Workflow

When multiple discovery waves feed one evaluation pipeline:

```text
Wave 1 → candidates
Wave 2 → additional candidates
Wave 3 → additional candidates
    ↓
Entity resolution → unified candidate set
    ↓
Evidence aggregation → gates → scoring → confidence
    ↓
Unified ranking → shortlist → report
```

Use `scoring/unified-ranking.md` after per-candidate scoring is complete.
See `templates/unified_ranking.csv` for output columns.

Ranking safety rules are in AGENTS.md and the unified-ranking prompt.

## Inputs All Prompts Expect

- project_id
- config_root: read paths.config_root from project.yaml, default config/research/<project-id>/
- research_root: research/<project-id>/
- master_csv: read paths.master_csv from project.yaml
- evidence_mode: live or simulated from project.yaml when applicable

Stop after producing the requested outputs. Do not chain phases.

## Prompt Audit (2026-09-06 Phase C)

All 12 workflow prompt files audited via check_prompts.py:

| Check | Result |
|---|---|
| Nested quotation structures | PASS |
| Absolute paths | PASS |
| CPA-specific assumptions in generic prompts | PASS |
| AGENTS.md conflicts | PASS |
| Ranking safety alignment | PASS |

Automated re-check: `python tools/check_prompts.py`
