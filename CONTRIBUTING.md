# Contributing

Thank you for contributing to the Business Research Template.

## Scope

This repository is the **public generic template**. Domain-specific rules belong
in project configuration or optional domain packs — not in the generic engine.

Do not move CPA-specific or other domain logic into:

- generic prompts under `prompts/`
- generic validators under `tools/`
- generic templates under `templates/`
- generic Cursor rules under `.cursor/rules/`

## Workflow

1. Open an issue or discussion describing the proposed change
2. Fork the repository and create a focused branch
3. Make minimal, well-scoped changes
4. Run validation locally (see below)
5. Submit a pull request with a clear description

No repository-specific URLs are assumed here — use your fork and the upstream
remote configured in your local clone.

## Before You Submit

1. Run `python tools/check_prompts.py`
2. Run `python tools/validate_research_data.py` on affected CSV fixtures
3. Use `--strict` if you want warnings to fail the run
4. Do not add nested quotation structures to prompt files
5. Do not add secrets, credentials, or real personal data
6. Do not add real private candidate research outputs
7. Keep user-facing documentation Japanese-first where applicable
8. Keep internal IDs, field names, and enum values in English

## Evidence and Data Quality

Contributions must preserve:

- separation of gates, score, confidence, and recommendation
- evidence traceability
- UNKNOWN as a valid state — do not treat UNKNOWN as NO
- master data protection — no silent master rewrites during research examples

## Validation Expectations

Typical local checks:

```powershell
python tools/check_prompts.py
python tools/validate_research_data.py `
  --master data/master/candidates_master.csv `
  --config-dir config/research/_example_project
```

When changing scoring fixtures, include `--scoring` and keep rubric dimension
sums consistent with `score_total`.

## License

By contributing, you agree that your contributions are licensed under the
Apache License 2.0.

Copyright 2026 Naoki Hada. See [NOTICE](NOTICE) for attribution information.
See [DISCLAIMER.md](DISCLAIMER.md) for important disclaimers.
