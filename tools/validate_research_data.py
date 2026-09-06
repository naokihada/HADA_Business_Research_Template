#!/usr/bin/env python3
"""
Generic research data validator — no external dependencies.

Validates CSV files against the Business Research Template data contracts.
Domain-specific rules belong in domain pack config — not in this script.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

MASTER_REQUIRED_COLUMNS = [
    "candidate_id",
    "canonical_slug",
    "display_name",
    "organization",
    "entity_type",
    "wave_id",
    "research_status",
]

RESEARCH_STATUS = {
    "DISCOVERED",
    "NOT_RESEARCHED",
    "RESEARCHING",
    "RESEARCHED",
    "QC_PENDING",
    "QC_PASS",
    "QC_FAIL",
    "SHORTLISTED",
    "EXCLUDED",
    "DUPLICATE",
    "INACTIVE",
    "UNVERIFIED",
}

ENTITY_TYPES = {"ORGANIZATION", "INDIVIDUAL", "PRODUCT", "SERVICE", "UNKNOWN"}
GATE_STATUS = {"YES", "NO", "LIKELY", "UNKNOWN", ""}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW", "INSUFFICIENT_DATA", ""}
RECOMMENDATION = {"A", "B", "C", "D", ""}
SHORTLIST_TIER = {"TIER_1", "TIER_2", "TIER_3", "EXCLUDED", ""}
QC_PASS = {"YES", "NO", "SKIPPED", ""}
ELIGIBILITY = {"ELIGIBLE", "NOT_ELIGIBLE", "CONDITIONAL", "UNKNOWN", ""}

RANKING_REQUIRED = {
    "candidate_id",
    "candidate_name",
    "score_total",
    "confidence",
    "recommendation",
}


class ValidationResult:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return [], []
        rows = list(reader)
        return list(reader.fieldnames), rows


def extract_wave_prefixes(config_dir: Path) -> set[str]:
    prefixes: set[str] = set()
    discovery = config_dir / "discovery_sources.yaml"
    if not discovery.exists():
        return prefixes
    text = discovery.read_text(encoding="utf-8")
    for match in re.finditer(r"id_prefix:\s*(\S+)", text):
        prefixes.add(match.group(1))
    for match in re.finditer(r"prefix:\s*(\S+)", text):
        prefixes.add(match.group(1))
    return prefixes


def extract_rubric_dimensions(config_dir: Path) -> tuple[list[str], int | None, int | None]:
    """Parse scoring_rubric.yaml without a YAML dependency."""
    rubric = config_dir / "scoring_rubric.yaml"
    if not rubric.exists():
        return [], None, None

    text = rubric.read_text(encoding="utf-8")
    max_total: int | None = None
    match = re.search(r"^max_total:\s*(\d+)\s*$", text, re.MULTILINE)
    if match:
        max_total = int(match.group(1))

    dim_ids = re.findall(r"^\s*-\s*id:\s*(\S+)\s*$", text, re.MULTILINE)
    max_points_values = [
        int(v) for v in re.findall(r"^\s*max_points:\s*(\d+)\s*$", text, re.MULTILINE)
    ]
    max_points_sum = sum(max_points_values) if max_points_values else None

    if max_total is not None and max_points_sum is not None and max_total != max_points_sum:
        # Stored for caller to emit a config-level warning once.
        pass

    return dim_ids, max_total, max_points_sum


def validate_scoring_rubric_consistency(
    path: Path,
    columns: list[str],
    rows: list[dict[str, str]],
    config_dir: Path | None,
    result: ValidationResult,
) -> None:
    """Warn when score_total does not equal the sum of configured rubric dimensions."""
    if not config_dir:
        return

    dim_ids, max_total, max_points_sum = extract_rubric_dimensions(config_dir)
    if not dim_ids:
        return

    if max_total is not None and max_points_sum is not None and max_total != max_points_sum:
        result.warn(
            f"{config_dir / 'scoring_rubric.yaml'}: max_total ({max_total}) "
            f"!= sum of dimension max_points ({max_points_sum})"
        )

    missing_cols = [dim for dim in dim_ids if dim not in columns]
    if missing_cols:
        result.warn(f"Scoring CSV missing rubric dimension columns: {missing_cols}")

    for i, row in enumerate(rows, start=2):
        cid = (row.get("candidate_id") or "").strip() or f"row {i}"
        dim_sum = 0.0
        has_dimension_value = False

        for dim in dim_ids:
            if dim not in columns:
                continue
            raw = (row.get(dim) or "").strip()
            if not raw:
                continue
            has_dimension_value = True
            try:
                dim_sum += float(raw)
            except ValueError:
                result.error(f"{path}:{i} non-numeric dimension {dim}: {raw}")

        score_raw = (row.get("score_total") or "").strip()
        if not has_dimension_value or not score_raw:
            continue

        try:
            score_total = float(score_raw)
        except ValueError:
            continue

        if abs(dim_sum - score_total) > 0.01:
            result.warn(
                f"{path}:{i} {cid}: rubric dimension sum {dim_sum:g} "
                f"!= score_total {score_total:g}"
            )


def validate_master_csv(
    path: Path, config_dir: Path | None, result: ValidationResult
) -> set[str]:
    ids: set[str] = set()
    if not path.exists():
        result.error(f"Master CSV not found: {path}")
        return ids

    columns, rows = read_csv(path)
    if not columns:
        result.error(f"Master CSV has no header: {path}")
        return ids

    missing = [c for c in MASTER_REQUIRED_COLUMNS if c not in columns]
    if missing:
        result.error(f"Master CSV missing required columns: {missing}")

    prefixes = extract_wave_prefixes(config_dir) if config_dir else set()
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    all_ids: set[str] = set()

    for i, row in enumerate(rows, start=2):
        cid = (row.get("candidate_id") or "").strip()
        slug = (row.get("canonical_slug") or "").strip()
        if not cid:
            result.error(f"{path}:{i} missing candidate_id")
            continue
        if cid in seen_ids:
            result.error(f"{path}:{i} duplicate candidate_id: {cid}")
        seen_ids.add(cid)
        all_ids.add(cid)
        ids.add(cid)

        if slug in seen_slugs:
            result.warn(f"{path}:{i} duplicate canonical_slug: {slug}")
        seen_slugs.add(slug)

        status = (row.get("research_status") or "").strip()
        if status and status not in RESEARCH_STATUS:
            result.warn(f"{path}:{i} non-standard research_status: {status}")

        etype = (row.get("entity_type") or "").strip()
        if etype and etype not in ENTITY_TYPES:
            result.error(f"{path}:{i} invalid entity_type: {etype}")

        if prefixes:
            if not any(cid.startswith(p + "-") for p in prefixes):
                result.warn(
                    f"{path}:{i} candidate_id {cid} does not match wave prefixes {sorted(prefixes)}"
                )

    for i, row in enumerate(rows, start=2):
        canonical = (row.get("canonical_candidate_id") or "").strip()
        if canonical and canonical not in all_ids:
            result.error(
                f"{path}:{i} canonical_candidate_id references unknown id: {canonical}"
            )

    return ids


def validate_scoring_csv(
    path: Path,
    result: ValidationResult,
    master_ids: set[str] | None = None,
    config_dir: Path | None = None,
) -> set[str]:
    scoring_ids: set[str] = set()
    if not path.exists():
        result.warn(f"Scoring CSV not found (optional): {path}")
        return scoring_ids

    columns, rows = read_csv(path)
    missing = [c for c in ("candidate_id", "score_total", "confidence", "recommendation") if c not in columns]
    if missing:
        result.error(f"Scoring CSV missing columns: {missing}")

    gate_cols = [c for c in columns if c.startswith("gate_")]
    seen: set[str] = set()

    for i, row in enumerate(rows, start=2):
        cid = (row.get("candidate_id") or "").strip()
        if not cid:
            result.error(f"{path}:{i} missing candidate_id")
            continue
        if cid in seen:
            result.error(f"{path}:{i} duplicate candidate_id: {cid}")
        seen.add(cid)
        scoring_ids.add(cid)

        if master_ids is not None and cid not in master_ids:
            result.warn(f"{path}:{i} candidate_id {cid} not in master CSV")

        conf = (row.get("confidence") or "").strip()
        if conf and conf not in CONFIDENCE:
            result.error(f"{path}:{i} invalid confidence: {conf}")

        rec = (row.get("recommendation") or "").strip()
        if rec and rec not in RECOMMENDATION:
            result.error(f"{path}:{i} invalid recommendation: {rec}")

        tier = (row.get("shortlist_tier") or "").strip()
        if tier and tier not in SHORTLIST_TIER:
            result.error(f"{path}:{i} invalid shortlist_tier: {tier}")

        score = (row.get("score_total") or "").strip()
        if score:
            try:
                val = float(score)
                if val < 0 or val > 100:
                    result.warn(f"{path}:{i} score_total out of 0-100 range: {val}")
            except ValueError:
                result.error(f"{path}:{i} non-numeric score_total: {score}")

        for gc in gate_cols:
            gv = (row.get(gc) or "").strip()
            if gv and gv not in GATE_STATUS:
                result.error(f"{path}:{i} invalid {gc}: {gv}")

    validate_scoring_rubric_consistency(path, columns, rows, config_dir, result)

    return scoring_ids


def validate_ranking_csv(path: Path, result: ValidationResult) -> None:
    if not path.exists():
        result.warn(f"Ranking CSV not found (optional): {path}")
        return

    columns, rows = read_csv(path)
    missing = [c for c in RANKING_REQUIRED if c not in columns]
    if missing:
        result.error(f"Ranking CSV missing columns: {missing}")

    seen: set[str] = set()
    ranks: list[int] = []

    for i, row in enumerate(rows, start=2):
        cid = (row.get("candidate_id") or "").strip()
        if not cid:
            result.error(f"{path}:{i} missing candidate_id")
            continue
        if cid in seen:
            result.error(f"{path}:{i} duplicate canonical candidate_id in ranking: {cid}")
        seen.add(cid)

        conf = (row.get("confidence") or "").strip()
        if conf and conf not in CONFIDENCE:
            result.error(f"{path}:{i} invalid confidence: {conf}")

        rec = (row.get("recommendation") or "").strip()
        if rec and rec not in RECOMMENDATION:
            result.error(f"{path}:{i} invalid recommendation: {rec}")

        elig = (row.get("eligibility_status") or "").strip()
        if elig and elig not in ELIGIBILITY:
            result.warn(f"{path}:{i} non-standard eligibility_status: {elig}")

        rank = (row.get("final_rank") or "").strip()
        if rank and rank not in ("—", "-", ""):
            try:
                ranks.append(int(rank))
            except ValueError:
                result.warn(f"{path}:{i} non-numeric final_rank: {rank}")

    if ranks and len(ranks) != len(set(ranks)):
        result.warn(f"{path}: duplicate final_rank values detected")


def validate_qc_summary(path: Path, result: ValidationResult) -> None:
    if not path.exists():
        return
    columns, rows = read_csv(path)
    for col in ("candidate_id", "qc_module", "qc_pass"):
        if col not in columns:
            result.error(f"QC summary missing column {col}: {path}")
            return
    for i, row in enumerate(rows, start=2):
        qp = (row.get("qc_pass") or "").strip()
        if qp and qp not in QC_PASS:
            result.error(f"{path}:{i} invalid qc_pass: {qp}")


def print_summary(result: ValidationResult, verbose: bool) -> None:
    if verbose:
        print(f"Warnings: {len(result.warnings)}")
        print(f"Errors: {len(result.errors)}")
    if result.ok and not result.warnings:
        print("Validation passed.")
    elif result.ok:
        print(f"Validation passed with {len(result.warnings)} warning(s).")
    else:
        print(f"Validation failed with {len(result.errors)} error(s).")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generic research CSV data")
    parser.add_argument("--master", type=Path, help="Path to candidates_master.csv")
    parser.add_argument("--scoring", type=Path, help="Path to scoring_results.csv")
    parser.add_argument("--ranking", type=Path, help="Path to unified_ranking.csv")
    parser.add_argument("--qc-summary", type=Path, action="append", default=[])
    parser.add_argument("--config-dir", type=Path, help="Project config directory")
    parser.add_argument("--verbose", action="store_true", help="Summary statistics")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors",
    )
    args = parser.parse_args()

    if not any([args.master, args.scoring, args.ranking, args.qc_summary]):
        parser.error("Provide at least one of --master, --scoring, --ranking, --qc-summary")

    result = ValidationResult()
    master_ids: set[str] | None = None

    if args.master:
        master_ids = validate_master_csv(args.master, args.config_dir, result)
    if args.scoring:
        validate_scoring_csv(args.scoring, result, master_ids, args.config_dir)
    if args.ranking:
        validate_ranking_csv(args.ranking, result)
    for qc in args.qc_summary:
        validate_qc_summary(qc, result)

    if args.strict and result.warnings:
        for w in result.warnings:
            result.error(f"(strict) {w}")

    for w in result.warnings:
        print(f"WARNING: {w}")
    for e in result.errors:
        print(f"ERROR: {e}")

    print_summary(result, args.verbose)
    return 0 if result.ok else 1


if __name__ == "__main__":
    sys.exit(main())
