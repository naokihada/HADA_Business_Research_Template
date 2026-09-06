# Data Management

## Master data

Files under `data/master/` are user-provided authoritative facts.

Do not overwrite master data during external research unless the user explicitly
requests a master-data update.

If research contradicts master data, record the discrepancy in the dossier or
evidence and flag for human review — do not silently correct master rows.

## Inbox

Unorganized user material goes in `data/inbox/`.

When normalizing:

- preserve the original content
- copy structured facts into the appropriate master or research location
- leave uncertain items in inbox with a flag for review

## External research

Save research under `research/<project-id>/`.

Prefer new dated files over destructive edits to prior research artifacts.

## Configuration

Domain-specific gates, rubrics, shortlist rules, and QC modules are configured
under `config/research/<project-id>/` — not hard-coded in engine templates.
