# AGENTS.md — HADA Business Research Template

Portable operating rules for humans and **all coding agents** (Cursor, Claude Code,
Codex, and others) working in this repository.

---

## Documentation Layers

Do not treat agent-specific configuration as the primary source of project rules.

| Layer | Location | Purpose |
|---|---|---|
| Agent-independent instructions | `AGENTS.md` (this file) | Shared operating rules for any coding agent |
| Design documentation | `docs/design/` | Data model, logging architecture, and related design notes |
| User overview | `README.md` | Human-facing overview |
| Agent-specific adapters | `.cursor/rules/`, etc. | Thin pointers to this file — not a second source of truth |

Read this file before project work. Read `docs/design/` when you need data-model
or validation details. Read `README.md` for user-facing overview.

Adapter index: [docs/agents/README.md](docs/agents/README.md)

---

## Mission

Maintain a generic, evidence-based research workspace for comparing and selecting
business candidates such as companies, service providers, vendors, consultants,
organizations, products, and other entities.

Domain-specific requirements belong in project configuration and optional domain
packs — not in the generic engine.

---

## Architecture Principles

### Source hierarchy

Treat these categories differently:

| Location | Role |
|---|---|
| `data/master/` | User-provided authoritative facts |
| `data/inbox/` | User-provided but not yet normalized |
| `config/research/<project-id>/` | Domain configuration for a research project |
| `research/<project-id>/` | External research findings and analysis |
| `research/*/scoring/` | Scoring and QC aggregates |
| `research/*/shortlist/` | Shortlist and ranking outputs |
| `communications/` | Contact and drafting material (optional) |
| `logs/` | Audit and development history |

Never silently rewrite master facts based on external research.

### Separation of concerns

Keep these concepts separate:

| Concept | Purpose |
|---|---|
| **Gates** | Eligibility or exclusion (YES / NO / LIKELY / UNKNOWN) |
| **Score** | Comparative capability or fit (numeric rubric) |
| **Confidence** | Trust in underlying findings (HIGH / MEDIUM / LOW) |
| **Recommendation** | Decision category (A / B / C / D) |

Do not collapse gates, score, confidence, and recommendation into one number.

### Discovery vs entity resolution

Candidate discovery and entity resolution are separate steps.

The same real-world entity may appear in multiple discovery sources. Preserve
provenance. Record duplicates and canonical entities explicitly. Do not silently
merge or overwrite source records.

### Research waves

Multiple discovery waves are supported. Wave ID and candidate ID prefix are
configured per project — not hard-coded in the engine.

---

## Research Workflow

Standard pipeline:

```text
Configure project → Import master candidates → Dossier research
    → Entity resolution → Evidence collection → Gate evaluation
    → Capability scoring → Confidence assessment → Recommendation
    → QC modules (optional) → Ranking → Shortlist → Reports
```

Each phase produces bounded artifacts. Stop after the requested phase unless
explicitly instructed to continue.

Human checkpoints:

1. Approve candidate universe before full-universe research.
2. Fix scoring rubric before scoring.
3. Fix shortlist rules before tier assignment.
4. Review QC summaries before final selection.

---

## Evidence Discipline

For externally researched claims, preserve:

- entity name
- claim
- source URL (when available)
- source title (when available)
- research or access date
- evidence classification
- confidence
- notes or limitations

Evidence classifications:

- VERIFIED — directly supported by reliable evidence
- STATED — claimed by the candidate or vendor
- RECOMMENDED — third-party referral
- ASSESSED — researcher assessment
- UNKNOWN — insufficient evidence
- REQUIRES_CONFIRMATION — must confirm directly before reliance

Source tiers (configurable labels):

1. Official — vendor website, government, regulatory
2. Professional — directories, published credentials
3. Referral — known contact recommendation
4. General web — search snippets, reviews, social media

Tier 4 alone is insufficient for important qualification claims.

Prefer first-party official sources. Secondary sources may be discovery leads but
should not silently become verified facts.

Do not present inference as verified fact. Do not fabricate contact information,
credentials, locations, or capabilities.

When evidence is insufficient, use UNKNOWN. Do not convert UNKNOWN to YES or NO
by assumption.

---

## Bounded AI Execution

Research must be bounded.

DO NOT:

- run open-ended autonomous research loops
- continue searching after the requested deliverable is complete
- recursively launch additional research tasks without explicit instruction
- overwrite previous research results destructively
- automatically proceed to the next research phase
- modify `data/master/` during research unless explicitly asked

DO:

- identify the requested scope before starting
- state what will be changed
- create or update only the requested artifacts
- prefer new dated files over destructive edits
- append a research log entry after completing a bounded task
- stop and wait for the next instruction

### Per-task procedure

1. Read this file and the active project config under `config/research/<project-id>/`.
2. Identify the requested scope and inputs.
3. Perform only the requested pass.
4. Save the requested artifacts under `research/<project-id>/`.
5. Append one row to `logs/research/<project-id>.md`.
6. Report completion and stop.

### Candidate universe

Do not silently expand the candidate universe during scoring or shortlist phases.

Newly discovered candidates may be recorded as research leads or a new wave — not
added to the scoring population without an explicit scope decision.

---

## Master Data Protection

Files under `data/master/` are user-provided project facts.

External research must not silently update master records. If research finds a
discrepancy (stale address, wrong category, duplicate listing), record the
finding in the dossier, evidence, or research log — and flag for human review.

When normalizing inbox content, preserve the original material before moving
structured facts into master data.

### Inbox normalization

When organizing `data/inbox/` content:

- preserve the original content
- copy structured facts into the appropriate master or research location
- leave uncertain items in inbox with a flag for review

Save external research under `research/<project-id>/`. Domain-specific gates,
rubrics, shortlist rules, and QC modules are configured under
`config/research/<project-id>/` — not hard-coded in engine templates.

---

## Append-Only Research Artifacts

Prefer dated, append-friendly outputs:

- reports: `YYYY-MM-DD-<topic>-<lang>.md`
- preserve earlier reports rather than overwriting
- log scoring changes with reason
- document QC exclusions with rule reference

---

## Scoring and QC

Scoring measures comparative fit using a configured rubric. QC is explicit and
modular — not an informal final check.

Optional QC modules include reputation review, regulatory verification, source
quality review, and consistency review. Enable modules in project config.

A high score does not automatically mean the best choice. Low confidence caps
recommendation strength even when score is high.

Referrals and popularity are discovery signals — not automatic proof of
capability. Do not auto-bonus scores for referrals or review counts.

### QC module procedure

Before running a QC module:

1. Read `config/research/<project-id>/modules.yaml`.
2. Confirm scope (all candidates, top-N, shortlist-only).
3. Use the module template from `templates/qc_result.md`.
4. Write per-candidate evidence under `research/<project-id>/evidence/<module>/`.
5. Write summary CSV under `research/<project-id>/scoring/`.
6. Append validation notes to `logs/validation/<project-id>/` when appropriate.

QC outcomes may change shortlist membership independently of numeric score.

Do not run QC modules that are not enabled in project configuration unless
explicitly requested. Skip conditions (e.g. NOT_ELIGIBLE) must be recorded — not
silently omitted.

---

## Ranking Safety

Unified ranking and shortlist generation must follow these rules:

- Do not treat UNKNOWN as NO for gates or capabilities
- Do not fabricate missing evidence or contact details
- Do not silently upgrade STATED, ASSESSED, or UNKNOWN claims to VERIFIED
- Do not use confidence as a hard eligibility gate unless explicitly configured
- Do not replace objective gate failures with numeric score
- Do not hide excluded or NOT_ELIGIBLE candidates — document them
- Do not silently modify data/master/ during ranking
- Preserve entity resolution provenance when merging waves
- If uncertain, keep UNKNOWN and record follow-up questions

Prompt: `prompts/scoring/unified-ranking.md`

---

## Logging Principles

After bounded tasks, append to the appropriate log:

| Task type | Log location |
|---|---|
| Research execution | `logs/research/<project-id>.md` |
| Template development | `logs/development/YYYY-MM-DD-<topic>.md` |
| Rule or rubric change | `logs/decisions/YYYY-MM-DD-<slug>.md` |
| QC or validation pass | `logs/validation/<project-id>/YYYY-MM-DD-<module>.md` |

Each entry should include: date, project_id, action, artifact path, brief notes.

When applicable, also include: execution_id, prompt file path (not full prompt
text), and counts (candidates processed, pass/fail).

Do not log passwords, API keys, tokens, credentials, or unnecessary personal
information. Redact sensitive content if encountered during research.

Log task scope, artifact paths, counts, and decisions — not full raw AI
transcripts by default.

Update `logs/artifacts-index.md` when creating major dated outputs.

---

## Language

| Layer | Language |
|---|---|
| User-facing docs and reports | Japanese-first (configurable) |
| Internal identifiers, field names, enums | English |
| User-entered values in data | Japanese or English |

Language is a presentation concern — not a data-model concern. Do not maintain
duplicate Japanese and English internal rule systems.

---

## Data Formats

Prefer:

- Markdown for human-readable research records
- CSV for tabular master and aggregate data
- YAML for project configuration
- JSON only when structured machine interchange is clearly useful

Use UTF-8 text and stable filenames.

Do not store secrets in this repository.

---

## Coding Agent Integration

All essential project knowledge belongs in this file, `docs/design/`, or other
user-facing docs — not in a single agent's configuration alone.

Reusable task prompts live under `prompts/`. Reference config paths and
templates — do not embed domain rubrics in prompts.

Use **relative paths** from the repository root in all instructions and outputs.

### Prompt formatting rule (mandatory)

Never create nested quotations in agent instructions or prompt files.

Do not place a quoted block inside another quoted block.

Prefer headings, bullet lists, numbered sections, indentation, file paths, and
plain text descriptions.

Enforced by `tools/check_prompts.py`.

### Agent adapters

| Agent | Adapter | Role |
|---|---|---|
| Cursor | `.cursor/rules/` | Auto-loaded thin pointers to sections in this file |
| Others | See [docs/agents/README.md](docs/agents/README.md) | Add an adapter only when needed; always reference this file |

Do not copy shared rules into adapter files. Adapters may add IDE-specific
operational notes only.

---

## Recommendations

A recommendation must distinguish:

- verified facts
- user requirements and preferences
- analysis and assessment
- uncertainty and unknowns

Recommendations support decisions — they do not replace human judgment.

---

## Portability

`AGENTS.md`, `README.md`, `config/`, `data/master/`, and `templates/` are the
portable source of truth. A research project should be reproducible from
configuration plus master data plus research artifacts.
