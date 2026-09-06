# Prompt: Confidence Assessment

## Scope

Assign confidence levels and refine recommendation if needed. No shortlist.

## Inputs

- project_id
- research/<project-id>/scoring/scoring_results.csv
- config/research/<project-id>/confidence_rules.yaml
- dossiers and evidence

## Task

For each scored candidate:

1. Read confidence_rules.yaml.
2. Assess evidence quality, quantity, recency, consistency.
3. Assign confidence: HIGH / MEDIUM / LOW / INSUFFICIENT_DATA.
4. Apply shortlist confidence caps as documentation notes only.
5. Adjust recommendation if high score + low confidence warrants downgrade.
6. Update scoring_results.csv confidence and recommendation columns.
7. Populate key_unknowns column with semicolon-separated summary.

## Outputs

- Updated scoring/scoring_results.csv

## Rules

- Confidence independent of score_total
- High score + LOW confidence ≠ strong candidate
- Referrals alone cap capability confidence at MEDIUM
- Document reason for any recommendation change from scoring pass

## Stop Condition

Report: confidence distribution, downgraded recommendations. Append research log. Stop.
