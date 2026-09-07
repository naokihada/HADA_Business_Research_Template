# HADA Business Research Template

Reusable, domain-independent framework for evidence-based business research — comparing companies, services, vendors, consultants, organizations, products, and other candidates with scoring, quality control, and auditability.

**Complete fictional demonstration:** [HADA_Business_Research_Template_Sample](https://github.com/naokihada/HADA_Business_Research_Template_Sample) — a full cloud-vendor comparison pipeline with simulated evidence.

日本語の情報は、このページの下にあります。

---

## Overview

This template separates a practical candidate-research workflow into a **generic engine**, **domain configuration**, and **research outputs** so teams can reuse the same process across different business domains.

The workflow covers discovery, normalization, entity resolution, evidence, gates, scoring, confidence, QC, ranking, shortlist, and reporting. AI tools such as Cursor assist each phase as **bounded tasks**; humans make final decisions.

This repository contains the reusable framework and skeleton configuration. It does not include real private business data.

---

## Intended users

- Teams that need to compare and select vendors, experts, services, or products **with documented evidence**
- Projects that want reproducible, auditable research processes
- Teams that want to swap domain-specific eligibility gates and scoring rubrics **via configuration**
- Users who collaborate with Cursor or other AI agents while keeping artifacts in files

---

## Problems addressed

A workspace for candidate selection **without relying on intuition or search ranking alone**.

- Separate user-provided requirements from external research findings
- Record evidence and sources per claim
- Keep eligibility gates, scores, confidence, and recommendation categories distinct
- Run QC as an explicit phase
- Integrate multiple discovery waves (Wave 1, 2, 3 …) into unified ranking

---

## Workflow

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

Layered architecture:

```text
Generic Engine (AGENTS.md, templates, prompts, tools)
        ↓
Domain Pack (optional — examples/domain_packs/<domain>/)
        ↓
Research Project (config/research/<id>/ + research/<id>/)
        ↓
Research Outputs (dossiers, evidence, scoring, reports, logs)
```

---

## Architecture

| Location | Role |
|---|---|
| `data/master/` | User-provided authoritative facts |
| `data/inbox/` | User-provided content not yet normalized |
| `config/research/<project-id>/` | Domain configuration for a research project |
| `research/<project-id>/` | External research findings and analysis |
| `research/*/scoring/` | Scoring and QC aggregates |
| `research/*/shortlist/` | Shortlist and ranking outputs |
| `communications/` | Contact and drafting material (optional) |
| `logs/` | Audit and development history |

External research must not silently rewrite master facts. See [AGENTS.md](AGENTS.md) for portable operating rules.

---

## Core concepts

| Concept | Role |
|---|---|
| **Gates** | Eligibility or exclusion (YES / NO / LIKELY / UNKNOWN) |
| **Score** | Comparative capability or fit (configurable rubric) |
| **Confidence** | Trust in underlying findings (HIGH / MEDIUM / LOW) |
| **Recommendation** | Decision category (A / B / C / D) |

High score ≠ high confidence ≠ final selection. **Do not treat UNKNOWN as NO** (see Ranking Safety in [AGENTS.md](AGENTS.md)).

Evidence flow:

```text
Claim → Evidence → Source → Confidence → Gate / Score / Decision
```

Candidate discovery and entity resolution are separate steps. Preserve provenance when merging waves; do not silently merge duplicate source records.

---

## Template / Domain Pack / Research Project

| Layer | Location | Role |
|---|---|---|
| **Generic Engine** | AGENTS.md, templates/, prompts/, tools/ | Domain-independent workflow and artifact formats |
| **Domain Pack** | examples/domain_packs/<domain>/ | Reusable domain configuration (optional) |
| **Research Project** | config/research/<id>/ + research/<id>/ | One research execution |

Domain-specific gates and rubrics live under **config/research/**; the engine itself is not modified for each domain.

---

## Starting a new research project

### Method A — Bootstrap script (recommended)

```powershell
python tools/bootstrap_project.py 2026-10-vendor-search --dry-run
python tools/bootstrap_project.py 2026-10-vendor-search
```

Existing config and master CSV files are not overwritten by default. Details: [tools/README.md](tools/README.md)

### Method B — Manual setup

[docs/guides/new-project-bootstrap.md](docs/guides/new-project-bootstrap.md)

### After bootstrap

1. Edit `config/research/<project-id>/project.yaml`
2. Document user requirements in `data/master/requirements.md`
3. Import candidates into `data/master/candidates_master.csv`
4. Run one phase at a time using prompts under `prompts/`
5. Append one line to `logs/research/<project-id>.md` after each bounded task

---

## Directory guide

| Path | Contents |
|---|---|
| `AGENTS.md` | Portable operating rules (humans and AI) |
| `.cursor/rules/` | Cursor-specific supplementary rules |
| `config/research/_example_project/` | Skeleton config copied by bootstrap |
| `data/master/` | Authoritative master data (do not silently update during research) |
| `research/<id>/` | Research outputs (user-generated) |
| `templates/` | Markdown and CSV templates |
| `prompts/` | Reusable phase prompts |
| `tools/` | Validator, bootstrap, prompt audit |
| `examples/domain_packs/` | Optional domain pack examples |

---

## Evidence handling

- Record URL, access date, classification, and confidence for important external claims
- Classifications: VERIFIED / STATED / RECOMMENDED / ASSESSED / UNKNOWN / REQUIRES_CONFIRMATION
- Source tiers: Tier 1 (official) through Tier 4 (general web)
- Tier 4 alone is insufficient to mark important qualifications as VERIFIED
- Set `evidence_mode: live|simulated` in `project.yaml` to declare live research or simulated evidence
- Template: [templates/evidence_record.md](templates/evidence_record.md)

When evidence is insufficient, use UNKNOWN. Do not convert UNKNOWN to YES or NO by assumption.

---

## Cursor / AI usage

1. Read `AGENTS.md` first
2. One task = one phase (discovery only, dossier only, etc.)
3. Reference the appropriate file under `prompts/`
4. Append to `logs/research/<project-id>.md` when done, then stop

**Prompt rule:** Do not use nested quotations in Cursor instructions or prompt files. Use headings and bullet lists instead.

AI accelerates research; it does not replace evidence.

---

## Logs and privacy

| Log type | Location |
|---|---|
| Research execution | `logs/research/<project-id>.md` |
| Template or rule changes | `logs/decisions/` |
| QC validation | `logs/validation/<project-id>/` |
| Template development (optional) | `logs/development/` |

**Do not log:** passwords, API keys, authentication tokens, unnecessary personal information, or client-confidential content.

Committing execution logs is not required. Details: [docs/design/logging-architecture.md](docs/design/logging-architecture.md)

---

## Example projects

### Config skeleton

- [config/research/_example_project/](config/research/_example_project/) — source copied by bootstrap

### Complete demonstration (separate repository)

The finished fictional cloud-vendor comparison — full pipeline with simulated evidence — lives in the public Sample repository:

**[HADA_Business_Research_Template_Sample](https://github.com/naokihada/HADA_Business_Research_Template_Sample)**

### Optional — fictional CPA domain pack

**Not a recommendation of real CPAs.** An advanced example of domain separation and regulatory-style QC configuration.

- [examples/domain_packs/cpa/](examples/domain_packs/cpa/) — three fictional candidates, example.invalid URLs only

---

## Data validation

```powershell
python tools/validate_research_data.py `
  --master data/master/candidates_master.csv `
  --config-dir config/research/_example_project

python tools/check_prompts.py
```

CI: [.github/workflows/validate.yml](.github/workflows/validate.yml) (no secrets required)

Unified ranking prompt: [prompts/scoring/unified-ranking.md](prompts/scoring/unified-ranking.md)

---

## Repository structure

Three-repository model for this ecosystem:

| Repository | Role |
|---|---|
| **HADA_Business_Research_Template** | Public reusable framework (this repository) |
| **HADA_Business_Research_Template_Sample** | Public complete fictional demonstration |
| **HADA_Business_Research_Template_Dev** | Private development source (not required to use the Template) |

Details: [docs/guides/repository-strategy.md](docs/guides/repository-strategy.md)

---

## Documentation

| Document | Topic |
|---|---|
| [docs/guides/new-project-bootstrap.md](docs/guides/new-project-bootstrap.md) | Starting a new project |
| [docs/guides/repository-strategy.md](docs/guides/repository-strategy.md) | Template / Sample / Dev relationship |
| [docs/guides/migration-from-cpa-research.md](docs/guides/migration-from-cpa-research.md) | Conceptual migration guide (no data) |
| [docs/guides/sample-repository-plan.md](docs/guides/sample-repository-plan.md) | Sample repository plan |
| [docs/design/data-model.md](docs/design/data-model.md) | Data model |
| [docs/design/logging-architecture.md](docs/design/logging-architecture.md) | Logging design |
| [CHANGELOG.md](CHANGELOG.md) | Change history |

---

## License

Apache License 2.0.

Copyright 2026 Naoki Hada.

See [LICENSE](LICENSE) (full license text) and [NOTICE](NOTICE) (attribution).

---

## Disclaimer

Important limitations, exclusions, and user responsibilities are in [DISCLAIMER.md](DISCLAIMER.md).

---

# 日本語

## 概要

本テンプレートは、候補調査ワークフローを **汎用エンジン**、**ドメイン設定**、**調査成果** に分離し、異なるビジネスドメインで同じプロセスを再利用できるようにしたものです。

発見、正規化、エンティティ解決、証拠、ゲート、スコア、信頼度、QC、ランキング、ショートリスト、レポートをカバーします。Cursor 等の AI は各フェーズを **範囲限定タスク** として支援し、最終判断は人間が行います。

本リポジトリは再利用可能なフレームワークとスケルトン設定を含みます。実在の非公開ビジネスデータは含みません。

**完成デモ（別リポジトリ）:** [HADA_Business_Research_Template_Sample](https://github.com/naokihada/HADA_Business_Research_Template_Sample) — 模擬証拠付きクラウドバックアップベンダー比較の全パイプライン。

---

## 対象ユーザー

- ベンダー、専門家、サービス、製品などを **根拠付きで比較選定** したいチーム
- 調査プロセスを再現可能・監査可能にしたいプロジェクト
- ドメイン固有の適格性ゲートやスコアリングを **設定で差し替え** たい場合
- Cursor / AI エージェントと協働しつつ、成果物をファイルベースで管理したい場合

---

## 解決する問題

候補を **感覚や検索順位だけで選ばない** ための調査ワークスペースです。

- ユーザー提供の要件と外部調査結果を分離
- クレームごとに証拠とソースを残す
- 適格性ゲート、スコア、信頼度、推薦区分を混同しない
- QC を明示的なフェーズとして実行
- 複数ディスカバリ波（Wave 1, 2, 3 …）を統合してランキング可能

---

## ワークフロー

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

レイヤー構成:

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

## アーキテクチャ

| 場所 | 役割 |
|---|---|
| `data/master/` | ユーザー提供の権威ある事実 |
| `data/inbox/` | 未正規化のユーザー提供コンテンツ |
| `config/research/<project-id>/` | 調査プロジェクトのドメイン設定 |
| `research/<project-id>/` | 外部調査の成果と分析 |
| `research/*/scoring/` | スコアリングと QC 集計 |
| `research/*/shortlist/` | ショートリストとランキング出力 |
| `communications/` | 連絡・下書き素材（任意） |
| `logs/` | 監査・開発履歴 |

外部調査でマスター事実を silently 上書きしてはいけません。portable な運用ルールは [AGENTS.md](AGENTS.md) を参照。

---

## 主要概念

| 概念 | 役割 |
|---|---|
| **Gates** | 適格 / 除外（YES / NO / LIKELY / UNKNOWN） |
| **Score** | 比較スコア（設定可能なルーブリック） |
| **Confidence** | 調査結果への信頼度（HIGH / MEDIUM / LOW） |
| **Recommendation** | 推薦区分（A / B / C / D） |

高スコア ≠ 高信頼度 ≠ 最終選定。**UNKNOWN を NO として扱わない**（[AGENTS.md](AGENTS.md) の Ranking Safety 参照）。

証拠の流れ:

```text
Claim → Evidence → Source → Confidence → Gate / Score / Decision
```

候補発見とエンティティ解決は別ステップです。複数 Wave を統合する際は出所を保持し、ソースレコードを silently マージしないでください。

---

## Template / Domain Pack / Research Project

| レイヤ | 場所 | 役割 |
|---|---|---|
| **Generic Engine** | AGENTS.md, templates/, prompts/, tools/ | ドメイン非依存のワークフローと成果物形式 |
| **Domain Pack** | examples/domain_packs/<domain>/ | 再利用可能なドメイン設定（任意） |
| **Research Project** | config/research/<id>/ + research/<id>/ | 1 回の調査実行 |

ドメイン固有のゲートやルーブリックは **config/research/** に置き、エンジン本体はドメインごとに変更しません。

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
| `config/research/_example_project/` | bootstrap のコピー元スケルトン |
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

証拠が不十分な場合は UNKNOWN を使用し、推測で YES / NO に変換しないでください。

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
| ルール変更の決定 | `logs/decisions/` |
| QC 検証 | `logs/validation/<project-id>/` |
| テンプレート開発（任意） | `logs/development/` |

**ログに入れてはいけないもの:** パスワード、API キー、認証トークン、不要な個人情報、クライアント機密情報。

実行ログのコミットは必須ではありません。詳細: [docs/design/logging-architecture.md](docs/design/logging-architecture.md)

---

## 例示プロジェクト

### 設定スケルトン

- [config/research/_example_project/](config/research/_example_project/) — bootstrap のコピー元

### 完成デモ（別リポジトリ）

模擬証拠付きの架空クラウドバックアップベンダー比較（全パイプライン）は公開 Sample リポジトリにあります:

**[HADA_Business_Research_Template_Sample](https://github.com/naokihada/HADA_Business_Research_Template_Sample)**

### オプション — 架空 CPA ドメインパック

**実在 CPA 推薦ではありません。** ドメイン分離と規制系 QC 設定の高度な例です。

- [examples/domain_packs/cpa/](examples/domain_packs/cpa/) — 架空候補 3 件、example.invalid URL のみ

---

## データ検証

```powershell
python tools/validate_research_data.py `
  --master data/master/candidates_master.csv `
  --config-dir config/research/_example_project

python tools/check_prompts.py
```

CI: [.github/workflows/validate.yml](.github/workflows/validate.yml)（シークレット不要）

統合ランキングプロンプト: [prompts/scoring/unified-ranking.md](prompts/scoring/unified-ranking.md)

---

## リポジトリ構成

本エコシステムの 3 リポジトリモデル:

| リポジトリ | 役割 |
|---|---|
| **HADA_Business_Research_Template** | 公開再利用可能フレームワーク（本リポジトリ） |
| **HADA_Business_Research_Template_Sample** | 公開完成架空デモ |
| **HADA_Business_Research_Template_Dev** | 非公開開発ソース（Template 利用に不要） |

詳細: [docs/guides/repository-strategy.md](docs/guides/repository-strategy.md)

---

## ドキュメント

| 文書 | 内容 |
|---|---|
| [docs/guides/new-project-bootstrap.md](docs/guides/new-project-bootstrap.md) | 新規プロジェクト開始 |
| [docs/guides/repository-strategy.md](docs/guides/repository-strategy.md) | Template / Sample / Dev 関係 |
| [docs/guides/migration-from-cpa-research.md](docs/guides/migration-from-cpa-research.md) | 概念移行ガイド（データ非含有） |
| [docs/guides/sample-repository-plan.md](docs/guides/sample-repository-plan.md) | Sample リポジトリ計画 |
| [docs/design/data-model.md](docs/design/data-model.md) | データモデル |
| [docs/design/logging-architecture.md](docs/design/logging-architecture.md) | ログ設計 |
| [CHANGELOG.md](CHANGELOG.md) | 変更履歴 |

---

## ライセンス

Apache License 2.0.

Copyright 2026 Naoki Hada.

詳細は [LICENSE](LICENSE)（ライセンス全文）および [NOTICE](NOTICE)（帰属表示）を参照してください。

---

## 免責事項

重要な免責事項、制限事項、および利用者の責任については [DISCLAIMER.md](DISCLAIMER.md) を参照してください。
