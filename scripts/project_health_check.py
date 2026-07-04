from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOGS_DIR = PROJECT_ROOT / "outputs" / "logs"
PROJECT_PHASE = "Phase 10 - Agent Workflow Packaging and GitHub Showcase"
LARGE_FILE_LIMIT_BYTES = 10 * 1024 * 1024


REQUIRED_DIRS = [
    "app",
    "configs",
    "data",
    "data/raw",
    "data/processed",
    "docs/knowledge_base",
    "docs/product_design",
    "docs/technical_design",
    "docs/showcase",
    "docs/interview",
    "docs/release",
    "docs/architecture",
    "outputs",
    "outputs/alerts",
    "outputs/reports",
    "outputs/logs",
    "scripts",
    "src/risk_control_agent",
    "tests",
]

REQUIRED_FILES = [
    ".gitignore",
    "README.md",
    "PROJECT_LOG.md",
    "CHANGELOG.md",
    "SOURCES.md",
    "AGENT_DEVELOPMENT_RULES.md",
    "PROJECT_SUMMARY.md",
    "requirements.txt",
    "requirements-dev.txt",
    "app/streamlit_app.py",
    "scripts/build_monitoring_tables.py",
    "scripts/run_alert_engine.py",
    "scripts/run_root_cause_analysis.py",
    "scripts/generate_risk_report.py",
    "scripts/run_full_pipeline.py",
    "scripts/project_health_check.py",
    "configs/data_paths.yaml",
    "configs/risk_alert_rules.yaml",
    "configs/root_cause_analysis.yaml",
    "configs/report_template.yaml",
    "docs/technical_design/phase10_workflow_packaging_design.md",
    "docs/showcase/project_showcase_overview.md",
    "docs/showcase/demo_walkthrough.md",
    "docs/showcase/github_repository_description.md",
    "docs/architecture/system_architecture.md",
    "docs/architecture/workflow_mermaid_diagram.md",
    "docs/interview/interview_talk_track.md",
    "docs/interview/resume_bullets.md",
    "docs/interview/qa_bank.md",
    "docs/release/github_upload_guide.md",
    "docs/release/pre_release_checklist.md",
    "docs/release/data_safety_checklist.md",
]


def check_path_exists(relative_path: str, expected_type: str) -> dict[str, Any]:
    path = PROJECT_ROOT / relative_path
    exists = path.exists()
    type_ok = path.is_dir() if expected_type == "dir" else path.is_file()
    status = "pass" if exists and type_ok else "fail"
    suggestion = "" if status == "pass" else f"请检查并补充 {relative_path}。"
    return {
        "item": relative_path,
        "expected_type": expected_type,
        "status": status,
        "suggestion": suggestion,
    }


def list_non_gitkeep_files(directory: str) -> list[dict[str, Any]]:
    path = PROJECT_ROOT / directory
    if not path.exists():
        return []
    files = []
    for item in path.rglob("*"):
        if item.is_file() and item.name != ".gitkeep":
            files.append(
                {
                    "path": str(item.relative_to(PROJECT_ROOT)),
                    "size_bytes": item.stat().st_size,
                }
            )
    return files


def check_data_and_outputs() -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    raw_files = list_non_gitkeep_files("data/raw")
    processed_files = list_non_gitkeep_files("data/processed")
    report_files = list_non_gitkeep_files("outputs/reports")
    alert_files = list_non_gitkeep_files("outputs/alerts")

    checks.append(
        {
            "item": "data/raw",
            "status": "pass" if not raw_files else "warning",
            "details": raw_files,
            "suggestion": "data/raw 应保持为空或仅包含 .gitkeep；上传 GitHub 前请人工确认。",
        }
    )
    large_processed = [file for file in processed_files if file["size_bytes"] > LARGE_FILE_LIMIT_BYTES]
    checks.append(
        {
            "item": "data/processed large files",
            "status": "pass" if not large_processed else "warning",
            "details": large_processed,
            "suggestion": "data/processed 不应提交大型 derived data，除非经过人工批准。",
        }
    )
    checks.append(
        {
            "item": "outputs/reports fabricated result review",
            "status": "pass" if not report_files else "manual_review",
            "details": report_files,
            "suggestion": "上传前请人工确认报告来自真实流程输入，不是伪造结果。",
        }
    )
    checks.append(
        {
            "item": "outputs/alerts fabricated result review",
            "status": "pass" if not alert_files else "manual_review",
            "details": alert_files,
            "suggestion": "上传前请人工确认 alert 来自真实流程输入，不是伪造结果。",
        }
    )
    return checks


def save_health_log(log: dict[str, Any]) -> Path:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = LOGS_DIR / f"project_health_check_{timestamp}.json"
    path.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def main() -> int:
    dir_checks = [check_path_exists(path, "dir") for path in REQUIRED_DIRS]
    file_checks = [check_path_exists(path, "file") for path in REQUIRED_FILES]
    safety_checks = check_data_and_outputs()
    all_checks = dir_checks + file_checks + safety_checks
    hard_failures = [check for check in all_checks if check["status"] == "fail"]
    warnings = [check for check in all_checks if check["status"] in {"warning", "manual_review"}]

    log = {
        "run_name": "project_health_check",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "project_phase": PROJECT_PHASE,
        "overall_status": "fail" if hard_failures else "pass_with_manual_review" if warnings else "pass",
        "summary": {
            "total_checks": len(all_checks),
            "failures": len(hard_failures),
            "warnings_or_manual_review": len(warnings),
        },
        "checks": all_checks,
        "safety_note": "健康检查只反映项目文件状态，不代表生产可用性；上传前仍需人工复核。",
    }
    log_path = save_health_log(log)

    print("项目健康检查完成。")
    print(f"overall_status: {log['overall_status']}")
    print(f"failures: {len(hard_failures)}")
    print(f"warnings_or_manual_review: {len(warnings)}")
    print(f"检查日志已保存：{log_path}")
    return 1 if hard_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
