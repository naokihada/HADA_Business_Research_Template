# Prompt: Candidate Discovery

## Scope

Bounded discovery pass only. Do not run dossier research, scoring, or QC.

## Inputs

- project_id
- config/research/<project-id>/discovery_sources.yaml
- config/research/<project-id>/discovery_queries.md
- config/research/<project-id>/project.yaml
- target wave_id (e.g. wave1 or wave2)

## Task

1. Read discovery configuration and queries.
2. Search or process the specified discovery source scope.
3. Normalize findings into candidate master row format.
4. Assign candidate_id using wave prefix from discovery_sources.yaml.
5. Set research_status to DISCOVERED.
6. Preserve source provenance in source and referral columns.
7. Write new rows to a dated import file OR propose rows for human review.

## Outputs

- Dated discovery note: research/<project-id>/sources/YYYY-MM-DD-discovery-<wave_id>.md
- Proposed CSV rows matching templates/candidates_master.csv columns
- Do NOT silently merge into data/master/ unless explicitly instructed

## Rules

- Do not infer capabilities from listing titles alone
- Do not fabricate contact details
- Record discovery source key in source column
- Stop after discovery deliverable is complete
- Append one row to logs/research/<project-id>.md

## Stop Condition

Report: count of candidates discovered, source key, output file paths. Then stop.
