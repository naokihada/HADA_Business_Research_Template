# Prompt: Run QC Module

## Scope

Execute one configured QC module. No shortlist or report.

## Inputs

- project_id
- qc_module id from config/research/<project-id>/modules.yaml
- candidate scope per module config (all / top_n / shortlist)
- templates/qc_result.md
- dossiers, evidence, scoring_results.csv

## Task

1. Read module definition from modules.yaml.
2. Determine candidate scope and skip conditions.
3. For each in-scope candidate, run module checks.
4. Write per-candidate QC evidence under evidence/<module>/.
5. Write summary CSV under scoring/<module>_summary.csv.
6. Set qc_pass, risk_level, confidence per module schema.
7. Append validation log under logs/validation/<project-id>/.

## Outputs

- evidence/<module>/<candidate_id>-<module>.md or qc_result format
- scoring/<module>_summary.csv
- logs/validation/<project-id>/YYYY-MM-DD-<module>.md

## Rules

- Skip with documented reason — do not silently omit
- QC may flag exclude or downgrade independent of score
- Do not run disabled modules unless explicitly requested

## Stop Condition

Report: module id, pass/fail/skip counts, summary CSV path. Append research log. Stop.
