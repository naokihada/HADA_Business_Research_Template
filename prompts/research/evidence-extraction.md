# Prompt: Evidence Extraction

## Scope

Extract and file structured evidence for specified claims. No scoring.

## Inputs

- project_id
- candidate_id
- claim list or dossier section to support
- config/research/<project-id>/evidence_requirements.yaml
- templates/evidence_record.md

## Task

1. Identify material claims needing evidence from dossier or gate checklist.
2. Locate sources per evidence tier hierarchy in AGENTS.md.
3. Create evidence files under research/<project-id>/evidence/<phase>/.
4. For each claim record: classification, source tier, URL, access date, confidence.
5. Link evidence files from dossier Evidence Index.
6. Note limitations when source is incomplete or inaccessible.

## Outputs

- Evidence markdown files: <candidate_id>-<topic>.md
- Updated dossier Evidence Index links

## Rules

- Tier 4 alone insufficient for core qualification claims
- Do not fabricate URLs or access dates
- VERIFIED only with direct reliable support
- UNKNOWN classification when evidence not found

## Stop Condition

Report: evidence files created, claims covered, gaps remaining. Append research log. Stop.
