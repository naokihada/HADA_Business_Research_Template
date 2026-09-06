# Prompt Execution Log Entry

<!-- Append to logs/prompt-runs/YYYY-MM-DD-<execution_id>.md or research log summary -->

| Field | Value |
|---|---|
| execution_id | EX-YYYYMMDD-NNN |
| timestamp | ISO-8601 |
| project_id | |
| phase | discovery / dossier / scoring / qc / shortlist / report |
| prompt_id | prompts/<path>.md |
| prompt_version | git ref or date |
| evidence_mode | live / simulated |
| input_artifacts | comma-separated paths |
| output_artifacts | comma-separated paths |
| validation_result | PASS / FAIL / SKIPPED |
| decision_ref | logs/decisions/ or docs/decisions/ if applicable |
| notes | counts, anomalies — no secrets |

## Rules

- Do not paste full AI output by default
- Do not log credentials or environment variables
- Reference prompt file path — do not duplicate full prompt text
- Distinguish reusable prompt (prompts/) from this execution record
