# Tools

Generic utilities for the Business Research Template. No external dependencies. Python 3.9+ standard library only.

---

## bootstrap_project.py

Scaffold a new research project from the generic example configuration.

```powershell
python tools/bootstrap_project.py 2026-10-vendor-search
python tools/bootstrap_project.py 2026-10-vendor-search --dry-run
python tools/bootstrap_project.py 2026-10-vendor-search --force
```

### Behavior

- Copies `config/research/_example_project/` to `config/research/<project-id>/`
- Creates `research/<project-id>/` subdirectories (candidates, evidence, scoring, shortlist, reports, sources)
- Initializes `logs/research/<project-id>.md` from template
- Writes master CSV header stub at `data/master/candidates_master.csv` only if missing

### Safety

- Does not overwrite existing config unless `--force`
- Does not overwrite existing master CSV unless `--force`
- No network access, no secrets, no domain-specific logic

See [docs/guides/new-project-bootstrap.md](../docs/guides/new-project-bootstrap.md) for the full 17-step manual process.

---

## validate_research_data.py

Generic CSV validator for master, scoring, QC, and unified ranking files.

```powershell
python tools/validate_research_data.py `
  --master data/master/candidates_master.csv `
  --config-dir config/research/_example_project `
  --scoring research/2026-09-cloud-vendor-example/scoring/scoring_results.csv

python tools/validate_research_data.py `
  --master examples/domain_packs/cpa/data/candidates_master.csv `
  --config-dir config/research/2026-09-cpa-fictional-example `
  --scoring research/2026-09-cpa-fictional-example/scoring/scoring_results.csv `
  --ranking research/2026-09-cpa-fictional-example/scoring/unified_ranking.csv `
  --verbose
```

### Options

| Option | Purpose |
|---|---|
| `--master` | Path to candidates_master.csv |
| `--config-dir` | Project config directory (for wave prefix cross-check) |
| `--scoring` | Path to scoring_results.csv |
| `--ranking` | Path to unified_ranking.csv |
| `--qc-summary` | Path to QC summary CSV (optional) |
| `--verbose` | Show warnings |
| `--strict` | Treat warnings as errors (exit 1) |

Exit code 0 on pass, 1 on failure.

### Validates (Generic Only)

- Master CSV required columns and duplicate IDs
- entity_type and research_status enums (base set)
- canonical_candidate_id references
- Wave prefix cross-check vs discovery_sources.yaml (regex parse, no YAML dependency)
- Scoring CSV confidence, recommendation, shortlist_tier, gate columns
- Unified ranking CSV columns, score ranges, duplicate final_rank
- Master/scoring ID cross-check
- eligibility_status enum warnings
- Numeric score_total range warning
- QC summary qc_pass values
- Rubric dimension sum vs score_total (when --config-dir and --scoring provided)

### Does Not Validate

- Domain-specific gate semantics
- Evidence file content

---

## check_prompts.py

Audit reusable prompts for format compliance.

```powershell
python tools/check_prompts.py
python tools/check_prompts.py --path prompts/research
```

Checks:

- No nested blockquote structures (nested quotation rule)
- No absolute Windows paths in prompt files

Exit code 0 on pass, 1 on failure. Used by GitHub Actions CI.

---

## CI Integration

See [.github/workflows/validate.yml](../.github/workflows/validate.yml) for automated checks on push and pull request.
