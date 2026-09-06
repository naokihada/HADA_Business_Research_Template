# Candidate Dossier — {{display_name}}

<!-- テンプレート: 候補エンティティ調査レコード / Template: candidate entity research record -->
<!-- Replace placeholders. Narrative may be Japanese or English. -->

## 1. Identity / 基本情報

| Field | Value |
|---|---|
| candidate_id | {{candidate_id}} |
| canonical_slug | {{canonical_slug}} |
| display_name | {{display_name}} |
| organization | {{organization}} |
| entity_type | ORGANIZATION / INDIVIDUAL / PRODUCT / SERVICE / UNKNOWN |
| website | |
| phone | |
| location | |
| research_date | YYYY-MM-DD |
| wave_id | |
| source | |

## 2. Entity Resolution / エンティティ解決

| Field | Value |
|---|---|
| canonical_entity | |
| possible_duplicates | |
| related_listings | |
| identity_confidence | HIGH / MEDIUM / LOW |
| resolution_notes | |

Preserve original discovery source values when corrected. Record both original and
verified values when they differ.

## 3. Capability Matrix / 能力評価

Use rows from `config/research/<project-id>/verification_checklist.md`.

| Requirement ID | Requirement | Status | Classification | Evidence |
|---|---|---|---|---|
| | | YES / NO / LIKELY / UNKNOWN | VERIFIED / STATED / … | link or summary |

## 4. Fit Assessment / 適合性

### Geographic / 地理的条件

| Item | Status | Evidence |
|---|---|---|
| | | |

### Communication / コミュニケーション

| Item | Status | Evidence |
|---|---|---|
| | | |

### Engagement / エンゲージメント適合

| Item | Status | Evidence |
|---|---|---|
| | | |

## 5. Eligibility Gates / 適格性ゲート

| Gate ID | Status | Evidence |
|---|---|---|
| | YES / NO / LIKELY / UNKNOWN | |

## 6. Evidence Index / 証拠一覧

| Evidence File | Phase | Summary |
|---|---|---|
| | | |

## 7. Strengths / 強み

-

## 8. Weaknesses / 弱み

-

## 9. Unknowns / 未確認事項

-

## 10. Questions to Confirm / 確認質問

-

## 11. Scoring Reference / スコア参照

| Field | Value |
|---|---|
| scoring_csv | research/<project-id>/scoring/scoring_results.csv |
| score_total | |
| confidence | HIGH / MEDIUM / LOW |
| recommendation | A / B / C / D |

Scores must be explainable from evidence in this dossier. Do not record unexplained numbers.

## 12. Recommendation Summary / 推薦サマリー

| Field | Value |
|---|---|
| eligibility_status | ELIGIBLE / NOT_ELIGIBLE / CONDITIONAL / UNKNOWN |
| recommendation | A / B / C / D |
| rationale | |
