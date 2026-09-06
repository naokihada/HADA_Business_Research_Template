# Prompt: Entity Resolution

## Scope

Resolve identity, duplicates, and canonical entities. No scoring.

## Inputs

- project_id
- candidate_id list or full master scope
- data/master/candidates_master.csv
- existing dossiers under research/<project-id>/candidates/

## Task

For each candidate or suspected duplicate group:

1. Identify canonical legal or trade entity.
2. Detect duplicate listings across sources or waves.
3. Detect wrong entity type or inactive entities.
4. Update dossier Entity Resolution section.
5. For duplicate rows: set research_status DUPLICATE and canonical_candidate_id.
6. Record original source values — do not erase provenance.
7. Propose master CSV corrections in a review file — do not silently edit master.

## Outputs

- Updated dossier Entity Resolution sections
- research/<project-id>/sources/YYYY-MM-DD-entity-resolution.md summary
- Proposed master updates in research/<project-id>/sources/YYYY-MM-DD-master-proposals.csv if needed

## Rules

- Discovery source listing ≠ verified entity identity
- Same real-world entity may appear in multiple waves — link via canonical_candidate_id
- INACTIVE if vendor shut down or product discontinued
- UNVERIFIED if existence cannot be confirmed

## Stop Condition

Report: duplicates found, canonical mappings, inactive entities. Append research log. Stop.
