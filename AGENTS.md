# AGENTS.md — HADA Business Research Template

Portable operating rules for humans and AI agents working in this repository.

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

---

## Master Data Protection

Files under `data/master/` are user-provided project facts.

External research must not silently update master records. If research finds a
discrepancy (stale address, wrong category, duplicate listing), record the
finding in the dossier, evidence, or research log — and flag for human review.

When normalizing inbox content, preserve the original material before moving
structured facts into master data.

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
| Rule or rubric change | `logs/decisions/` |
| QC validation | `logs/validation/<project-id>/` |

Do not log passwords, API keys, tokens, credentials, or unnecessary personal
information. Redact sensitive content if encountered during research.

Log task scope, artifact paths, counts, and decisions — not full raw AI
transcripts by default.

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

## Cursor Integration

Portable rules live here in `AGENTS.md`. Cursor-specific behavior lives under
`.cursor/rules/`. Do not put essential project knowledge only in Cursor rules.

Reusable task prompts live under `prompts/`. Reference config paths and
templates — do not embed domain rubrics in prompts.

### Cursor prompt formatting rule (mandatory)

Never create nested quotations in Cursor instructions or prompt files.

Do not place a quoted block inside another quoted block.

Prefer headings, bullet lists, numbered sections, indentation, file paths, and
plain text descriptions.

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
