# Domain Packs

Optional domain-specific configuration and sample data for the generic research engine.

## Purpose

A domain pack proves that complex real-world research (e.g. professional services,
regulated vendors, cross-border selection) can be configured **without modifying**
the generic engine.

## Structure

```text
examples/domain_packs/<domain>/
├── README.md           # What is generic vs domain-specific
├── config/             # Copy to config/research/<project-id>/
└── data/               # Sample master data (fictional)
```

## Relationship

```text
Generic engine (AGENTS.md, templates, prompts)
        ↓
Domain pack (examples/domain_packs/<domain>/)
        ↓
Research project (config/research/<id>/ + research/<id>/)
        ↓
Research outputs (dossiers, evidence, scoring, reports)
```

## Available Packs

| Pack | Description | Candidates |
|---|---|---|
| [cpa/](cpa/) | US CPA / tax professional selection (fictional) | 3 fictional |

## Usage

1. Copy `examples/domain_packs/<domain>/config/` → `config/research/<your-project-id>/`
2. Edit `project.yaml` project_id and paths
3. Copy or reference domain pack data for master CSV
4. Create `research/<your-project-id>/` directories
5. Run bounded prompts from `prompts/`

Do not edit generic engine files for domain-specific needs.
