# HADA Business Research Template

AI-assisted business research and evaluation template for comparing companies,
services, vendors, consultants, organizations, products, and other candidate
entities — with evidence, scoring, quality control, and auditability.

エビデンス・スコアリング・QC・監査可能性を備えた、汎用ビジネスリサーチテンプレートです。
特定業界専用ではありません — ドメイン設定とオプションのドメインパックで拡張します。

---

## このテンプレートとは

実務的な候補調査ワークフロー（発見 → 正規化 → エンティティ解決 → 証拠 → ゲート → スコア → 信頼度 → QC → ランキング → ショートリスト → レポート）を、
**汎用エンジン + ドメイン設定 + 調査成果** に分離して再利用できるようにしたテンプレートです。

本リポジトリは実務的なリサーチワークフローを汎用化したものです。実在の非公開ビジネスデータは含みません。

AI（Cursor 等）は各フェーズを**範囲限定タスク**として支援します。最終判断は人間が行います。

---

## 誰向けか

- ベンダー、専門家、サービス、製品などを**根拠付きで比較選定**したいチーム
- 調査プロセスを再現可能・監査可能にしたいプロジェクト
- ドメイン固有の適格性ゲートやスコアリングを**設定で差し替え**たい場合
- Cursor / AI エージェントと協働しつつ、成果物をファイルベースで管理したい場合

---

## 解決する問題

候補を**感覚や検索順位だけで選ばない**ための調査ワークスペースです。

- ユーザー提供の要件と外部調査結果を分離
- クレームごとに証拠とソースを残す
- 適格性ゲート、スコア、信頼度、推薦区分を混同しない
- QC を明示的なフェーズとして実行
- 複数ディスカバリ波（Wave）を統合してランキング可能

---

## ワークフロー概要

```text
Configure project
    → Import master candidates
    → Discovery (Wave 1, 2, 3 …)
    → Entity resolution
    → Dossier research
    → Evidence collection
    → Gate evaluation
    → Capability scoring
    → Confidence assessment
    → Unified ranking (multi-wave)
    → QC modules (optional)
    → Shortlist
    → Report
```

```text
Generic Engine（AGENTS.md, templates, prompts, tools）
        ↓
Domain Pack（任意 — examples/domain_packs/<domain>/）
        ↓
Research Project（config/research/<id>/ + research/<id>/）
        ↓
Research Outputs（dossiers, evidence, scoring, reports, logs）
```

---

## 主要概念

| 概念 | 役割 |
|---|---|
| **Gates** | 適格 / 除外（YES / NO / LIKELY / UNKNOWN） |
| **Score** | 比較スコア（設定可能なルーブリック） |
| **Confidence** | 調査結果への信頼度（HIGH / MEDIUM / LOW） |
| **Recommendation** | 推薦区分（A / B / C / D） |

高スコア ≠ 高信頼度 ≠ 最終選定。**UNKNOWN を NO として扱わない**（AGENTS.md Ranking Safety 参照）。

証拠の流れ:

```text
Claim → Evidence → Source → Confidence → Gate / Score / Decision
```

---

## Template / Domain Pack / Research Project

| レイヤ | 場所 | 役割 |
|---|---|---|
| **Generic Engine** | AGENTS.md, templates/, prompts/, tools/ | ドメイン非依存のワークフローと成果物形式 |
| **Domain Pack** | examples/domain_packs/<domain>/ | 再利用可能なドメイン設定（任意） |
| **Research Project** | config/research/<id>/ + research/<id>/ | 1 回の調査実行 |

ドメイン固有のゲートやルーブリックは **config/research/** に置き、エンジン本体は変更しません。

---

## 新規リサーチプロジェクトの開始

### 方法 A — ブートストラップスクリプト（推奨）

```powershell
python tools/bootstrap_project.py 2026-10-vendor-search --dry-run
python tools/bootstrap_project.py 2026-10-vendor-search
```

既存の config / master CSV はデフォルトで上書きしません。詳細: [tools/README.md](tools/README.md)

### 方法 B — 手動

[docs/guides/new-project-bootstrap.md](docs/guides/new-project-bootstrap.md)

### 開始後の流れ

1. `config/research/<project-id>/project.yaml` を編集
2. `data/master/requirements.md` にユーザー要件を記載
3. `data/master/candidates_master.csv` に候補をインポート
4. `prompts/` の該当プロンプトを 1 フェーズずつ実行
5. 各タスク後に `logs/research/<project-id>.md` に 1 行追加

---

## ディレクトリガイド

| パス | 内容 |
|---|---|
| `AGENTS.md` | portable な運用ルール（AI・人間共通） |
| `.cursor/rules/` | Cursor 向け補助ルール |
| `config/research/_example_project/` | 新規プロジェクト用スケルトン設定 |
| `data/master/` | 権威あるマスターデータ（調査で silently 更新しない） |
| `research/<id>/` | 調査成果（ユーザーが生成） |
| `templates/` | Markdown / CSV テンプレート |
| `prompts/` | フェーズ別再利用プロンプト |
| `tools/` | バリデータ、ブートストラップ、プロンプト監査 |
| `examples/domain_packs/` | オプションのドメインパック例 |

---

## 証拠の扱い

- 外部調査の重要クレームには URL、確認日、分類、信頼度を記録
- 分類: VERIFIED / STATED / RECOMMENDED / ASSESSED / UNKNOWN / REQUIRES_CONFIRMATION
- ソース階層: Tier 1（公式）→ Tier 4（一般 Web）
- Tier 4 のみでは重要資格を VERIFIED にしない
- `project.yaml` の `evidence_mode: live|simulated` で実調査か模擬かを明示
- テンプレート: [templates/evidence_record.md](templates/evidence_record.md)

---

## Cursor / AI の使い方

1. 最初に `AGENTS.md` を読む
2. 1 タスク = 1 フェーズ（discovery のみ、dossier のみ、など）
3. `prompts/` の該当ファイルを参照
4. 完了後 `logs/research/<project-id>.md` に追記して停止

**プロンプト規則:** nested quotation（引用の入れ子）禁止。見出しと箇条書きを使う。

AI は調査を加速する補助であり、証拠の代替ではありません。

---

## ログとプライバシー

| 種類 | 場所 |
|---|---|
| 調査実行 | `logs/research/<project-id>.md` |
| QC 検証 | `logs/validation/<project-id>/` |

**ログに入れてはいけないもの:** パスワード、API キー、認証トークン、不要な個人情報、クライアント機密情報。

実行ログのコミットは必須ではありません。詳細: [docs/design/logging-architecture.md](docs/design/logging-architecture.md)

---

## 例示とデモ

### 設定スケルトン

- [config/research/_example_project/](config/research/_example_project/) — bootstrap のコピー元

### 完成デモ（別リポジトリ）

完成した架空調査プロジェクトのデモは **HADA_Business_Research_Template_Sample** リポジトリを参照してください。
クラウドバックアップベンダー比較の全パイプライン（模擬証拠付き）を含みます。

### オプション — CPA ドメインパック（架空）

**実在 CPA 推薦ではありません。** ドメイン分離の高度な例です。

- [examples/domain_packs/cpa/](examples/domain_packs/cpa/) — 架空候補 3 件、example.invalid URL

---

## データ検証

```powershell
python tools/validate_research_data.py `
  --master data/master/candidates_master.csv `
  --config-dir config/research/_example_project

python tools/check_prompts.py
```

CI: [.github/workflows/validate.yml](.github/workflows/validate.yml)（シークレット不要）

---

## 関連リポジトリ

| リポジトリ | 役割 |
|---|---|
| **HADA_Business_Research_Template** | 本リポジトリ — 再利用可能な汎用テンプレート |
| **HADA_Business_Research_Template_Sample** | 公開デモ — 完成した架空調査プロジェクト |

詳細: [docs/guides/repository-strategy.md](docs/guides/repository-strategy.md)

---

## ドキュメント

| 文書 | 内容 |
|---|---|
| [docs/guides/new-project-bootstrap.md](docs/guides/new-project-bootstrap.md) | 新規プロジェクト開始 |
| [docs/guides/repository-strategy.md](docs/guides/repository-strategy.md) | Template / Sample 関係 |
| [docs/guides/migration-from-cpa-research.md](docs/guides/migration-from-cpa-research.md) | 概念移行ガイド（データ非含有） |
| [docs/design/data-model.md](docs/design/data-model.md) | データモデル |
| [docs/design/logging-architecture.md](docs/design/logging-architecture.md) | ログ設計 |

---

## ライセンス

Apache License 2.0 — 詳細は [LICENSE](LICENSE) と [NOTICE](NOTICE) を参照。

NOTICE の著作権表示は、著作権者確認待ちのプレースホルダーを使用しています。
リリースタグ v0.1.0 は commit/push 後に作成予定です。

---

## 変更履歴

[CHANGELOG.md](CHANGELOG.md)
