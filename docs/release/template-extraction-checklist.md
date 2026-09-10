# Template Extraction Checklist

Use when synchronizing **HADA_Business_Research_Template** (public) from
**HADA_Business_Research_Template_Dev** (private development source).

Dev formal specification: `SPEC.md` in Dev repo only — **do not copy to Public Template**  
Release process: [v0.1.0-release-process.md](v0.1.0-release-process.md)

---

## Pre-flight

- [ ] Dev validation passes (`check_prompts.py`, `validate_research_data.py`)
- [ ] No secrets or real PII in public tree
- [ ] `LICENSE`, `NOTICE`, `DISCLAIMER.md` present
- [ ] Root `SPEC.md` **absent** from Public Template
- [ ] No `ReSPEC.md` or `ReSPEC_COMPARISON.md` in public Template

---

## Include (PUBLIC TEMPLATE)

### Root and legal

- [ ] `AGENTS.md` (multi-agent structure; no Dev-only session rules)
- [ ] `README.md` (public positioning — no Dev status, bilingual EN→JA)
- [ ] `LICENSE`, `NOTICE`, `DISCLAIMER.md`, `.gitignore`
- [ ] `CHANGELOG.md`, `CONTRIBUTING.md` (if maintained for public)

### Agent integration

- [ ] `.cursor/rules/` (thin adapters pointing to AGENTS.md)
- [ ] `docs/agents/README.md`

### Engine

- [ ] `templates/`, `prompts/`, `tools/`
- [ ] `.github/workflows/validate.yml` (public Template CI — not Dev research fixtures)

### Configuration and examples

- [ ] `config/research/_example_project/`
- [ ] `examples/domain_packs/` (CPA pack — fictional only)
- [ ] `data/master/` header templates (no private research data)
- [ ] `data/inbox/README.md`
- [ ] `communications/` (if public)

### Public documentation

- [ ] `docs/design/`, `docs/guides/`
- [ ] `docs/release/` (this folder)
- [ ] Exclude `docs/analysis/`, `docs/implementation/`, `docs/dev-only/`

---

## Exclude (DEV-ONLY or SAMPLE)

- [ ] `SPEC.md` (Dev-only formal project specification)
- [ ] `docs/analysis/`
- [ ] `docs/implementation/`
- [ ] `docs/decisions/` (internal ADRs)
- [ ] `docs/dev-only/`
- [ ] `logs/development/`, `logs/research/`, `logs/prompt-runs/`
- [ ] `research/*` full project outputs — ship in **Sample** repo, not Template
- [ ] Dev-only fictional research fixtures used only in Dev CI
- [ ] `ReSPEC.md`, `ReSPEC_COMPARISON.md`

---

## Sanitize

- [ ] No `D:\_dev\...` or other local filesystem paths
- [ ] No private repository URLs unless public GitHub links
- [ ] No Phase/status language in README
- [ ] All example URLs use `example.invalid` or are clearly fictional
- [ ] No references to `ReSPEC` as formal specification
- [ ] No references assuming root `SPEC.md` exists in Public Template

---

## Verify (Public Template)

```powershell
python tools/check_prompts.py
python tools/validate_research_data.py `
  --master data/master/candidates_master.csv `
  --config-dir config/research/_example_project `
  --strict
python tools/validate_research_data.py `
  --master examples/domain_packs/cpa/data/candidates_master.csv `
  --config-dir examples/domain_packs/cpa/config `
  --strict
python tools/bootstrap_project.py ci-test-project --dry-run
```

- [ ] No absolute Windows paths in `.cursor/rules` or `prompts`
- [ ] Apache 2.0 headers consistent
- [ ] Root `SPEC.md` absent
- [ ] README links to Sample early

---

## Tag and publish

- [ ] Commit synced public Template content
- [ ] Push to public remote
- [ ] Apply `v0.1.0` tag to the **synced commit** (not an outdated pre-sync tag)
- [ ] Create GitHub Release: `v0.1.0 — Initial Public Release`
- [ ] Verify Sample repository separately (see release process doc)

---

## CI difference (intentional)

Public Template CI validates:

- `_example_project` master header
- CPA domain pack config/master
- bootstrap dry-run

Public Template CI does **not** require Dev-only paths such as
`research/2026-09-cloud-vendor-example/scoring/*.csv`.

Complete fictional pipeline outputs live in **HADA_Business_Research_Template_Sample**.
