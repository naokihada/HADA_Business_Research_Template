# Prompt: Generate Shortlist

## Scope

Apply shortlist tier rules. No final report.

## Inputs

- project_id
- config/research/<project-id>/shortlist_rules.yaml
- scoring/scoring_results.csv
- QC summary CSVs if available
- templates/shortlist.md

## Task

1. Confirm shortlist rules are fixed before applying.
2. Apply disqualifiers from shortlist_rules.yaml.
3. Assign TIER_1 / TIER_2 / TIER_3 / EXCLUDED per tier requirements.
4. Compute contact priority order with documented tie-breakers.
5. Write research/<project-id>/shortlist/shortlist.md from template.
6. Update scoring_results.csv shortlist_tier column.

## Outputs

- shortlist/shortlist.md
- Updated scoring_results.csv shortlist_tier column

## Rules

- Shortlist is not score-only
- DUPLICATE and INACTIVE → EXCLUDED
- Document discretionary adjustments with rationale
- Tier and contact priority may differ

## Stop Condition

Report: tier counts, contact priority list, excluded reasons. Append research log. Stop.
