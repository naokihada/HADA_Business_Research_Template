# Prompt: Candidate Dossier Research

## Scope

Create or update dossiers for specified candidates only. No scoring or shortlist.

## Inputs

- project_id
- candidate_id list (batch scope)
- data/master/candidates_master.csv
- config/research/<project-id>/verification_checklist.md
- config/research/<project-id>/capability_criteria.yaml
- templates/candidate_dossier.md

## Task

For each candidate in scope:

1. Read master row — do not modify master CSV.
2. Research using official sources first.
3. Create or update research/<project-id>/candidates/<canonical_slug>.md from template.
4. Fill Identity and Entity Resolution sections.
5. Fill Capability Matrix from capability_criteria.yaml.
6. Record gate statuses as YES / NO / LIKELY / UNKNOWN with evidence.
7. List strengths, weaknesses, unknowns, and questions.
8. Update master research_status to RESEARCHED when dossier complete.

## Outputs

- One dossier file per candidate under research/<project-id>/candidates/
- Optional inline evidence references — full evidence files may be separate task

## Rules

- UNKNOWN when evidence is insufficient
- Do not convert STATED vendor claims to VERIFIED without verification
- Preserve original master values when correcting stale directory data
- Stop after batch dossiers are complete

## Stop Condition

Report: candidate IDs completed, dossier paths, anomalies found. Append research log. Stop.
