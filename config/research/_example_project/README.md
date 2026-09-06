# Example Project Configuration

This directory demonstrates how domain-specific research logic is configured
without modifying the generic engine.

## Files

| File | Purpose |
|---|---|
| project.yaml | Project identity, waves, paths, output language |
| requirements.md | User requirements (fictional) |
| discovery_sources.yaml | Wave and source definitions with ID prefixes |
| discovery_queries.md | Search strategy |
| eligibility_gates.yaml | Gate definitions |
| capability_criteria.yaml | Capability matrix rows |
| verification_checklist.md | Dossier verification checklist |
| evidence_requirements.yaml | Minimum evidence for scoring and shortlist |
| scoring_rubric.yaml | Scoring dimensions and recommendation bands |
| confidence_rules.yaml | Confidence level definitions |
| shortlist_rules.yaml | Tier rules and disqualifiers |
| modules.yaml | Optional QC modules |

## Usage

1. Copy this directory to `config/research/<your-project-id>/`.
2. Edit placeholders for your research objective.
3. Create matching paths under `research/<your-project-id>/`.
4. Import candidates into `data/master/candidates_master.csv`.
5. Run bounded prompts from `prompts/` for each workflow phase.

## Fictional Data Only

The linked example research project uses invented vendor names.
Do not treat this as real vendor research.
