# Coding Agent Adapters

This project separates project knowledge from agent-specific configuration.

## Layer model

```text
Agent-independent rules (AGENTS.md)
        ↓
Design documentation (docs/design/)
        ↓
Agent-specific adapters (this directory, .cursor/rules/, etc.)
        ↓
Individual coding agent
```

## Single source of truth

| Need | Read first |
|---|---|
| Shared operating rules | [AGENTS.md](../../AGENTS.md) |
| Data model and logging design | [docs/design/](../../design/) |
| User overview | [README.md](../../README.md) |

Do not copy AGENTS.md rules into adapter files.

Formal project specification (`SPEC.md`) lives in the private Dev repository only.
It is not shipped in this public Template.

## Current adapters

| Agent | Location | Status |
|---|---|---|
| Cursor | [.cursor/rules/](../../.cursor/rules/) | Active — thin pointers to AGENTS.md |
| Claude Code | — | Not configured — read AGENTS.md and docs/design/ directly |
| OpenAI Codex | — | Not configured — read AGENTS.md and docs/design/ directly |
| Other | — | Add adapter here only when needed |

## Adding a new adapter

1. Confirm the rule belongs in AGENTS.md (shared) vs agent-specific (adapter).
2. Shared rules go in AGENTS.md only — not duplicated in the adapter.
3. Architecture and data-model details belong in docs/design/ — not duplicated in the adapter.
4. Adapter files should reference AGENTS.md section names, not restate rules.
5. Keep operational notes that truly require a specific IDE or CLI in the adapter only.

## Task prompts

Phase prompts live under `prompts/`. They are agent-independent task definitions.
See [prompts/README.md](../../prompts/README.md).
