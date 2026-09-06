# Prompt: Multi-Wave Unified Ranking

## Scope

Merge scored candidates from multiple discovery waves into one unified ranking CSV.
Do not run new web research. Do not modify master CSV silently.

## Inputs

- project_id
- config_root from project.yaml paths.config_root
- research_root from project.yaml paths.research_root
- scoring/scoring_results.csv per wave OR single combined scoring_results.csv
- sources/ entity resolution notes
- templates/unified_ranking.csv (header reference)
- config discovery_sources.yaml for wave and prefix metadata

## Task

1. Read entity resolution outcomes — identify DUPLICATE rows and canonical_candidate_id links.
2. Build unified candidate set:
   - One ranking row per canonical candidate
   - Preserve source candidate_id in source_candidate_ids column or resolution notes
   - DUPLICATE rows must not appear as separate ranked entities
3. For each canonical candidate collect:
   - wave_id (may list multiple if merged)
   - score_total, confidence, recommendation from scoring CSV
   - eligibility_status if documented
   - shortlist_tier if already assigned
4. Assign final_rank by configured rules — document tie-breakers used
5. Write research/<project-id>/scoring/unified_ranking.csv
6. Write research/<project-id>/sources/YYYY-MM-DD-unified-ranking-notes.md explaining merges

## Outputs

- scoring/unified_ranking.csv
- sources/YYYY-MM-DD-unified-ranking-notes.md
- Append logs/research/<project-id>.md

## Ranking Safety Rules (Mandatory)

- Do not treat UNKNOWN gate status as NO
- Do not fabricate evidence to justify rank changes
- Do not upgrade STATED or UNKNOWN claims to VERIFIED
- Do not use confidence alone as a hard eligibility gate unless shortlist_rules.yaml explicitly requires it
- Do not replace objective gate failures with score rank
- Include EXCLUDED and NOT_ELIGIBLE candidates in notes — do not hide them silently
- Do not silently edit data/master/ — record discrepancies in research artifacts
- If evaluation is uncertain, preserve UNKNOWN and document in ranking notes

## Entity Resolution Rules

- Same real-world entity in multiple waves → one canonical ranking row
- Record all source candidate_ids and wave provenance
- Never merge without documented entity resolution
- Preserve original source values in master — resolution lives in research layer

## Stop Condition

Report: canonical count, duplicates merged, excluded count, output paths. Stop.
