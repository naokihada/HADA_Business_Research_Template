# 新規リサーチプロジェクト — ブートストラップガイド

**Generic — ドメイン非依存**

このガイドは、汎用 Business Research Template で新しい調査プロジェクトを
開始する手順を説明します。

---

## クイックスタート（スクリプト）

手動 17 ステップの前に、汎用スキャフォールドを生成できます:

```powershell
python tools/bootstrap_project.py 2026-10-vendor-search --dry-run
python tools/bootstrap_project.py 2026-10-vendor-search
```

- `_example_project` 設定をコピー
- `research/<project-id>/` サブディレクトリを作成
- 調査ログと master CSV ヘッダを初期化
- 既存 config / master CSV はデフォルトで上書きしない（`--force` で上書き）

詳細: [tools/README.md](../../tools/README.md)

以下のチェックリストは、スクリプト実行後も必要な設定・編集項目です。

---

## 関係性

```text
Template（エンジン）
    ↓
Domain Pack（任意 — 例: examples/domain_packs/cpa/）
    ↓
Research Project（config + data/master + research/）
    ↓
Research Outputs（dossiers, evidence, scoring, reports）
```

---

## チェックリスト

### 1. 調査目的を定義する

- 何を選定・比較するか（ベンダー、専門家、製品など）
- 成功条件と除外条件
- `config/research/<project-id>/project.yaml` の objective_ja に記載

### 2. 候補タイプを定義する

- candidate_type: vendor / professional_firm / product / service 等
- entity_types_allowed を設定

### 3. 地理的範囲を定義する

- geographic_scope.regions
- local_preferred / remote_acceptable

### 4. ディスカバリソースを設定する

- `discovery_sources.yaml` — wave_id, id_prefix, source_key
- `discovery_queries.md` — 検索・インポート戦略

### 5. 適格性ゲートを定義する

- `eligibility_gates.yaml`
- YES / NO / LIKELY / UNKNOWN
- required_for_shortlist と hard_fail_values

### 6. 能力基準を定義する

- `capability_criteria.yaml`
- `verification_checklist.md`

### 7. 証拠要件を定義する

- `evidence_requirements.yaml`
- 最低ソース階層、simulated vs live（evidence_mode）

### 8. スコアルーブリックを定義する

- `scoring_rubric.yaml` — 次元と配点
- スコアリング前に固定する

### 9. 信頼度ルールを定義する

- `confidence_rules.yaml`
- スコアとは独立

### 10. QC モジュールを選択する

- `modules.yaml` — 有効化するモジュールのみ enabled: true

### 11. ショートリストルールを設定する

- `shortlist_rules.yaml`
- ティア適用前に固定する

### 12. プロジェクトディレクトリを作成する

```text
config/research/<project-id>/
research/<project-id>/
  candidates/
  evidence/
  scoring/
  shortlist/
  reports/
  sources/
logs/research/<project-id>.md
```

### 13. 候補マスターデータを用意する

- `templates/candidates_master.csv` をコピー
- `data/master/candidates_master.csv` または project.yaml paths.master_csv
- wave prefix と research_status を設定

### 14. bounded 調査タスクを実行する

`prompts/` から 1 フェーズずつ:

1. candidate-discovery
2. candidate-dossier
3. entity-resolution
4. evidence-extraction
5. eligibility-evaluation
6. capability-evaluation
7. run-scoring
8. confidence-assessment
9. run-qc-module（モジュールごと）
10. generate-shortlist
11. generate-report

### 15. QC を実行する

- 有効なモジュールのみ
- skip 理由を記録

### 16. ショートリストとレポートを生成する

- ゲート・スコア・信頼度を区別して記載
- 日付付きファイル名 — 上書きしない

### 17. ログと決定を保存する

- `logs/research/<project-id>.md` — 各タスク後に 1 行
- ルール変更時 `logs/decisions/` または `docs/decisions/`
- QC 結果 `logs/validation/<project-id>/`

---

## Domain Pack を使う場合

1. `examples/domain_packs/<domain>/config/` を `config/research/<project-id>/` にコピー
2. `project.yaml` の project_id と paths を更新
3. `data/` をコピーまたは paths.master_csv を設定
4. エンジンファイル（AGENTS.md, templates, prompts）は変更しない

---

## 検証

```bash
python tools/validate_research_data.py \
  --master data/master/candidates_master.csv \
  --config-dir config/research/<project-id> \
  --scoring research/<project-id>/scoring/scoring_results.csv
```

---

## evidence_mode

| Value | Meaning |
|---|---|
| live | 通常の外部調査 — 実 URL と確認日が必要 |
| simulated | ワークフロー例示 — 証拠ファイルに SIMULATED 表示必須 |

---

## 禁止事項

- 調査中の data/master/ サイレント更新
- 推測を VERIFIED として記録
- スコアと信頼度の混同
- ネストした引用形式のプロンプト作成

See `AGENTS.md` for full operating rules.
