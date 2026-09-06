# Prompt: Capability Evaluation

## Scope

Evaluate capability criteria for ELIGIBLE or CONDITIONAL candidates. No final scoring.

## Inputs

- project_id
- candidate_id list
- config/research/<project-id>/capability_criteria.yaml
- dossiers and evidence

## Task

For each candidate in scope:

1. Read capability criteria from config.
2. Evaluate each criterion: YES / NO / LIKELY / UNKNOWN.
3. Assign evidence classification per claim.
4. Update dossier Capability Matrix.
5. Extract or update evidence files for material capability claims.
6. List unknowns requiring confirmation before scoring.

## Outputs

- Updated dossier Capability Matrix
- Evidence files for unsupported or disputed capabilities

## Rules

- STATED for vendor marketing claims not independently verified
- Do not award implied capabilities from product bundle names
- Map criteria to scoring dimensions but do not compute score in this task

## Stop Condition

Report: criteria evaluated, unknown count, evidence gaps. Append research log. Stop.
