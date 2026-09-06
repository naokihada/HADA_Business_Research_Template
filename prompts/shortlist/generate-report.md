# Prompt: Generate Report

## Scope

Produce dated human-readable report from research artifacts. No new research.

## Inputs

- project_id
- config/research/<project-id>/project.yaml
- scoring/scoring_results.csv
- shortlist/shortlist.md
- logs/research/<project-id>.md
- templates/report.md

## Task

1. Read aggregates — do not conduct new web research.
2. Summarize objective, scope, method, and key findings in Japanese-first prose.
3. Include recommended candidates with score, confidence, tier, rationale.
4. List exclusions, risks, and open questions.
5. Write dated report: research/<project-id>/reports/YYYY-MM-DD-final-report-ja.md
6. Update logs/artifacts-index.md

## Outputs

- Dated report markdown
- Updated artifacts-index entry

## Rules

- Distinguish verified facts, assessment, and unknowns
- State that score, confidence, and recommendation are separate
- Do not overwrite prior reports — use new dated filename
- Report supports decision — does not replace human judgment

## Stop Condition

Report: report path, date, candidate count summarized. Append research log. Stop.
