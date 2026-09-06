#!/usr/bin/env python3
"""
Bootstrap a new generic research project directory structure.

Safe by default: refuses to overwrite existing paths unless --force.
No network. No secrets. No domain-specific logic.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_CONFIG_SOURCE = REPO_ROOT / "config" / "research" / "_example_project"
TEMPLATE_MASTER = REPO_ROOT / "templates" / "candidates_master.csv"
TEMPLATE_LOG = REPO_ROOT / "templates" / "research_log.md"

RESEARCH_SUBDIRS = [
    "candidates",
    "evidence",
    "scoring",
    "shortlist",
    "reports",
    "sources",
]

README_RESEARCH = """# Research Project — {project_id}

**Created:** {today}

Configure this project in `config/research/{project_id}/`.

## Directories

| Path | Purpose |
|---|---|
| candidates/ | Candidate dossiers |
| evidence/ | Evidence records |
| scoring/ | Scoring and QC CSV |
| shortlist/ | Shortlist outputs |
| reports/ | Dated reports |
| sources/ | Discovery and entity resolution notes |

## Next Steps

1. Edit config/research/{project_id}/project.yaml
2. Add master data (data/master/ or path in project.yaml)
3. Run bounded prompts from prompts/
4. Append to logs/research/{project_id}.md after each task

See docs/guides/new-project-bootstrap.md
"""


def patch_project_yaml(config_dst: Path, project_id: str) -> None:
    proj_yaml = config_dst / "project.yaml"
    if not proj_yaml.exists():
        return
    text = proj_yaml.read_text(encoding="utf-8")
    text = re.sub(
        r"^project_id:\s*.+$",
        f"project_id: {project_id}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^  research_root:\s*.+$",
        f"  research_root: research/{project_id}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = re.sub(
        r"^  config_root:\s*.+$",
        f"  config_root: config/research/{project_id}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    proj_yaml.write_text(text, encoding="utf-8")


def bootstrap(project_id: str, force: bool, dry_run: bool) -> int:
    config_dst = REPO_ROOT / "config" / "research" / project_id
    research_dst = REPO_ROOT / "research" / project_id
    log_dst = REPO_ROOT / "logs" / "research" / f"{project_id}.md"
    master_dst = REPO_ROOT / "data" / "master" / f"candidates_master_{project_id}.csv"

    def act(label: str, fn) -> None:
        if dry_run:
            print(f"PLAN  {label}")
        else:
            fn()
            print(f"DONE  {label}")

    if config_dst.exists() and not force:
        print(f"SKIP  config/research/{project_id}/ — exists (use --force)")
    else:
        def copy_config() -> None:
            if config_dst.exists() and force:
                shutil.rmtree(config_dst)
            shutil.copytree(DEFAULT_CONFIG_SOURCE, config_dst)
            patch_project_yaml(config_dst, project_id)

        act(f"copy config to config/research/{project_id}/", copy_config)

    for sub in RESEARCH_SUBDIRS:
        sub_path = research_dst / sub

        def make_sub(p=sub_path) -> None:
            p.mkdir(parents=True, exist_ok=True)

        act(f"mkdir research/{project_id}/{sub}/", make_sub)

    readme = research_dst / "README.md"
    if readme.exists() and not force:
        print(f"SKIP  research/{project_id}/README.md — exists")
    else:

        def write_readme() -> None:
            readme.write_text(
                README_RESEARCH.format(project_id=project_id, today=date.today().isoformat()),
                encoding="utf-8",
            )

        act(f"write research/{project_id}/README.md", write_readme)

    if log_dst.exists() and not force:
        print(f"SKIP  logs/research/{project_id}.md — exists")
    else:

        def write_log() -> None:
            log_dst.parent.mkdir(parents=True, exist_ok=True)
            content = TEMPLATE_LOG.read_text(encoding="utf-8").replace(
                "{{project_id}}", project_id
            )
            log_dst.write_text(content, encoding="utf-8")

        act(f"write logs/research/{project_id}.md", write_log)

    if master_dst.exists() and not force:
        print(f"SKIP  data/master/candidates_master_{project_id}.csv — exists")
    else:

        def write_master() -> None:
            master_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(TEMPLATE_MASTER, master_dst)

        act(f"write data/master/candidates_master_{project_id}.csv", write_master)

    if dry_run:
        print("Dry run complete — no files written.")
    else:
        print("Bootstrap complete.")
        print(f"Next: edit config/research/{project_id}/project.yaml")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap a new generic research project (safe by default)"
    )
    parser.add_argument("project_id", help="Project ID e.g. 2026-10-vendor-search")
    parser.add_argument("--dry-run", action="store_true", help="Show plan only")
    parser.add_argument("--force", action="store_true", help="Overwrite existing config")
    args = parser.parse_args()

    if not re.match(r"^[\w\-]+$", args.project_id):
        print("ERROR: project_id must use letters, numbers, hyphens, underscores only")
        return 1

    if not DEFAULT_CONFIG_SOURCE.is_dir():
        print(f"ERROR: config template missing: {DEFAULT_CONFIG_SOURCE}")
        return 1

    return bootstrap(args.project_id, args.force, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
