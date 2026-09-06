# Research Rules

## Bounded execution

Never run an open-ended research loop.

For every research task:

1. Read `AGENTS.md` and the active project config under `config/research/<project-id>/`.
2. Identify the requested scope and inputs.
3. Perform only the requested pass.
4. Save the requested artifacts under `research/<project-id>/`.
5. Append one row to `logs/research/<project-id>.md`.
6. Report completion and stop.

Do not automatically move from discovery to dossier to scoring to QC unless
explicitly requested.

## Evidence

For each material claim, preserve source URL and access date when available.

Do not invent capabilities, credentials, locations, pricing, or contact details.

Use UNKNOWN when information is unavailable. Do not infer missing facts.

Prefer first-party official sources. Secondary sources may be discovery leads but
should not silently become verified facts.

## Candidate universe

Do not silently expand the candidate universe during scoring or shortlist phases.

Newly discovered candidates may be recorded as research leads or a new wave —
not added to the scoring population without an explicit scope decision.
