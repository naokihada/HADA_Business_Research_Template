# Logging Rules

After completing a bounded task, append a log entry.

| Task type | Log file |
|---|---|
| Research execution | `logs/research/<project-id>.md` |
| Template or engine work | `logs/development/YYYY-MM-DD-<topic>.md` |
| Rubric, gate, or shortlist rule change | `logs/decisions/YYYY-MM-DD-<slug>.md` |
| QC or validation pass | `logs/validation/<project-id>/YYYY-MM-DD-<module>.md` |

Log:

- date, project_id, action, artifact path, brief notes
- execution_id when using prompt execution log template
- prompt file reference (path only — do not paste full prompt)
- counts (candidates processed, pass/fail)

Do not log:

- passwords, API keys, tokens, credentials
- full raw AI transcripts by default
- unnecessary personal information

If sensitive data appears during research, redact in artifacts and note redaction
in the research log.

Update `logs/artifacts-index.md` when creating major dated outputs.
