# Prompt: Run Scoring

## Scope

Compute numeric scores from evidence. No shortlist assignment.

## Inputs

- project_id
- candidate_id list (usually full universe)
- config/research/<project-id>/scoring_rubric.yaml
- config/research/<project-id>/eligibility_gates.yaml
- completed dossiers and evidence
- templates/scoring_results.csv

## Task

1. Confirm scoring rubric is fixed — do not change weights during this run.
2. For each candidate, score each dimension per rubric max_points.
3. Sum score_total (max per config, default 100).
4. Copy gate statuses into gate_<gate_id> columns.
5. Assign preliminary recommendation A/B/C/D using recommendation_bands.
6. Write research/<project-id>/scoring/scoring_results.csv.
7. Ensure every score is explainable from dossier evidence.

## Outputs

- scoring/scoring_results.csv with dimension columns from rubric
- Brief scoring notes for any score changes vs prior run

## Rules

- Do not score NOT_ELIGIBLE candidates beyond documentation unless configured
- Do not bonus score for referrals or popularity
- UNKNOWN capability → reduced dimension score — not full points
- Score is separate from confidence — leave confidence for next task

## Stop Condition

Report: CSV path, candidate count scored, top anomalies. Append research log. Stop.
