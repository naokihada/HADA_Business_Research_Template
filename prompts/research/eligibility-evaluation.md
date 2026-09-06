# Prompt: Eligibility Evaluation

## Scope

Evaluate eligibility gates only. No scoring or shortlist.

## Inputs

- project_id
- candidate_id list
- config/research/<project-id>/eligibility_gates.yaml
- dossiers and evidence under research/<project-id>/

## Task

For each candidate:

1. Read gate definitions from eligibility_gates.yaml.
2. Evaluate each gate: YES / NO / LIKELY / UNKNOWN.
3. Assign eligibility_status: ELIGIBLE / NOT_ELIGIBLE / CONDITIONAL / UNKNOWN.
4. Update dossier Eligibility Gates section.
5. Create evidence file if gate decision needs dedicated support.
6. Skip deep capability work for NOT_ELIGIBLE unless explicitly requested.

## Outputs

- Updated dossier gate tables
- Optional: research/<project-id>/evidence/eligibility/<candidate_id>-eligibility.md
- Summary note if batch: research/<project-id>/reports/YYYY-MM-DD-eligibility-summary.md

## Rules

- Hard fail on NO for required_for_shortlist gates → NOT_ELIGIBLE
- UNKNOWN does not auto-fail unless configured
- Do not infer YES from vendor category or name

## Stop Condition

Report: per-candidate eligibility_status and gate summary. Append research log. Stop.
