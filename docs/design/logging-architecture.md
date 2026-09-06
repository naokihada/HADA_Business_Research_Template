# Logging Architecture — Business Research Template

**Status:** Design proposal  
**Related:** [001-reference-to-generic-architecture.md](../analysis/001-reference-to-generic-architecture.md)

---

## 1. Purpose

The template must preserve enough context to reconstruct:

- What research was done and when
- Which AI prompts and rules guided execution
- Why scores, shortlist tiers, or QC outcomes changed
- Which artifacts were produced
- What template/design decisions were made during development

Without storing secrets, credentials, or unnecessary raw transcripts.

---

## 2. Log Type Separation

| Log Type | Audience | Mutability | Typical Retention |
|---|---|---|---|
| Reusable prompts | Template authors / AI | Versioned; curated | Permanent in repo |
| Research execution log | Research operators | Append-only | Per project |
| Analysis notes | Researchers | Append-only | Per project |
| Decision records | Team / future self | Immutable once accepted | Permanent |
| Generated outputs | Stakeholders | Dated artifacts | Permanent |
| Validation results | QC operators | Append-only | Per QC cycle |
| Development log | Template maintainers | Append-only | Template lifetime |
| Prompt execution summaries | Debugging / audit | Append-only | Optional; may redact |

---

## 3. Directory Layout

```text
logs/
├── research/
│   └── <project-id>.md              # Primary research audit trail
├── development/
│   └── YYYY-MM-DD-<topic>.md        # Template build decisions
├── decisions/
│   └── YYYY-MM-DD-<slug>.md         # Formal decision records
├── validation/
│   └── <project-id>/
│       └── YYYY-MM-DD-<qc-module>.md
├── prompt-runs/                      # Optional; gitignore by default
│   └── .gitkeep
└── artifacts-index.md               # Rolling index of major outputs
```

```text
prompts/
├── research/
├── scoring/
├── qc/
├── shortlist/
└── README.md                          # Usage + no nested quotes rule
```

---

## 4. Research Execution Log

**File:** `logs/research/<project-id>.md`

Mirrors the CPA project's `logs/research_log.md` pattern.

### Required Columns

| Column | Content |
|---|---|
| Date | ISO date |
| Project | project_id |
| Action | Short verb phrase |
| Artifact | Path or description |
| Notes | Anomalies, ID cross-refs, decisions |

### When to Append

After every bounded task:

- Batch dossier completion
- Entity resolution finding
- Scoring run
- QC module completion
- Shortlist change
- Wave merge
- Report generation

### Example Row Types (generic)

- Master CSV imported — N candidates — source key
- Duplicate resolved — ID-A → canonical ID-B
- Wrong category — ID marked INACTIVE
- Scoring completed — scoring_results.csv
- QC module skipped — NOT_ELIGIBLE candidates
- Shortlist tier change — ID moved TIER_1 → EXCLUDED — rule reference

Do not copy real CPA log rows into the template.

---

## 5. Decision Records

**File:** `logs/decisions/YYYY-MM-DD-<slug>.md`

Use when changing:

- Scoring rubric weights
- Gate definitions
- Shortlist tier rules
- QC module scope
- Candidate universe expansion

### Suggested Sections

1. Context
2. Decision
3. Alternatives considered
4. Consequences for existing artifacts
5. Approval (human reviewer if applicable)

---

## 6. Development Log

**File:** `logs/development/YYYY-MM-DD-<topic>.md`

Records template engineering:

- Architecture choices from analysis phase
- Cursor rule changes
- Prompt template revisions
- Schema column additions

Separates template evolution from research project execution.

---

## 7. Validation Results

**Path:** `logs/validation/<project-id>/`

Store QC pass summaries, checklist completions, and optional script output.

Link to evidence folders and summary CSVs; do not duplicate full evidence text.

---

## 8. Reusable Prompts vs Execution Logs

| Aspect | Reusable Prompt | Execution Log |
|---|---|---|
| Location | `prompts/` | `logs/prompt-runs/` or research log summary |
| Content | Task scope, inputs, outputs, stop rules | What was actually run, when, result paths |
| Editing | Curated updates | Append-only |
| Secrets | Never | Never |
| Nested quotes | Forbidden | N/A |

Execution logs should reference prompt file path + git hash or version tag, not paste the full prompt each time.

### Execution metadata fields (Phase B)

| Field | Purpose |
|---|---|
| execution_id | Stable id e.g. EX-YYYYMMDD-NNN |
| project_id | Research project |
| phase | Workflow phase |
| prompt_id | Path under prompts/ |
| timestamp | ISO-8601 |
| input_artifacts | Paths read |
| output_artifacts | Paths written |
| validation_result | PASS / FAIL / SKIPPED |
| decision_ref | Link to decision record if applicable |

Template: `templates/prompt_execution_log.md`

---

## 9. Artifacts Index

**File:** `logs/artifacts-index.md`

Rolling table of major outputs:

| Date | Project | Type | Path | Supersedes |
|---|---|---|---|---|

 Helps navigate dated reports without overwriting history.

---

## 10. Sensitive Data Policy

### Never Store in Logs or Committed Artifacts

- Passwords, API keys, authentication tokens
- Government ID numbers (SSN, tax ID)
- Bank account numbers
- Unnecessary personal information
- Private client or customer information
- Full private message threads with PII

Research prompts and AI outputs in logs may contain project context. That is expected.
Users must not paste credentials or confidential business data into prompt-run logs.

### Public Template Expectation

The generic template does not require logs to be committed to version control.
Reusable prompt definitions live under `prompts/` separately from execution logs under `logs/`.

Default `.gitignore` excludes `logs/prompt-runs/` and optional local research outputs.
Users may keep execution logs locally without publishing them.

### If Encountered During Research

1. Redact in artifact body.
2. Note redaction in research log.
3. Do not append raw content to prompt-run logs.

### .gitignore Recommendations

```gitignore
logs/prompt-runs/*
!logs/prompt-runs/.gitkeep
data/inbox/*
!data/inbox/README.md
.env
*.secret.*
```

---

## 11. Cursor Integration

Add `.cursor/rules/50-logging.md`:

After completing a bounded task, append one row to `logs/research/<project-id>.md` unless the task was pure template development (then use `logs/development/`).

Do not log full AI responses by default. Log:

- Task name
- Files written
- Counts (candidates processed, QC pass/fail)
- Rule or prompt reference

---

## 12. Relationship to CPA Reference

The CPA project implements only **research execution log** today (`logs/research_log.md`). The generic template expands logging for:

- Template development traceability
- Decision records when rules change mid-project
- Optional prompt-run summaries
- Validation/QC result indexing

The CPA log format is the seed for `logs/research/<project-id>.md`.
