from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def resolve_project_path(path: str | Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return PROJECT_ROOT / candidate


def load_json_file(path: str | Path) -> dict[str, Any] | list[Any] | None:
    file_path = resolve_project_path(path)
    if not file_path.exists() or not file_path.is_file():
        return None
    try:
        return json.loads(file_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def load_csv_file(path: str | Path) -> list[dict[str, str]]:
    file_path = resolve_project_path(path)
    if not file_path.exists() or not file_path.is_file():
        return []
    try:
        with file_path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    except OSError:
        return []


def load_markdown_file(path: str | Path) -> str | None:
    file_path = resolve_project_path(path)
    if not file_path.exists() or not file_path.is_file():
        return None
    try:
        return file_path.read_text(encoding="utf-8")
    except OSError:
        return None


def list_run_logs(logs_dir: str | Path = "outputs/logs") -> list[dict[str, Any]]:
    directory = resolve_project_path(logs_dir)
    if not directory.exists() or not directory.is_dir():
        return []

    logs: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*.json"), key=lambda item: item.stat().st_mtime, reverse=True):
        payload = load_json_file(path)
        if isinstance(payload, dict):
            logs.append(
                {
                    "file_name": path.name,
                    "file_path": str(path.relative_to(PROJECT_ROOT)),
                    "run_name": payload.get("run_name"),
                    "timestamp": payload.get("timestamp") or payload.get("run_timestamp"),
                    "status": payload.get("status"),
                    "project_phase": payload.get("project_phase"),
                    "output_path": payload.get("output_path"),
                    "messages": payload.get("messages", []),
                    "raw": payload,
                }
            )
    return logs


def get_latest_file(directory: str | Path, pattern: str) -> Path | None:
    dir_path = resolve_project_path(directory)
    if not dir_path.exists() or not dir_path.is_dir():
        return None
    candidates = [path for path in dir_path.glob(pattern) if path.is_file()]
    if not candidates:
        return None
    return max(candidates, key=lambda item: item.stat().st_mtime)


def load_latest_alert_summary() -> dict[str, Any] | None:
    return _load_latest_json("outputs/alerts", "risk_alert_summary*.json")


def load_latest_root_cause_summary() -> dict[str, Any] | None:
    return _load_latest_json("outputs/alerts", "root_cause_summary*.json")


def load_latest_report() -> str | None:
    latest = get_latest_file("outputs/reports", "risk_analysis_report*.md")
    return load_markdown_file(latest) if latest else None


def load_latest_report_manifest() -> dict[str, Any] | None:
    return _load_latest_json("outputs/reports", "risk_analysis_report_manifest*.json")


def load_pipeline_status() -> dict[str, bool]:
    official_dir = resolve_project_path("data/samples/official")
    official_sample_available = official_dir.exists() and any(path.is_file() for path in official_dir.iterdir())

    return {
        "official_sample_available": official_sample_available,
        "daily_monitoring_table_available": resolve_project_path(
            "data/processed/daily_risk_metrics_mvp.csv"
        ).exists(),
        "segment_monitoring_table_available": resolve_project_path(
            "data/processed/segment_risk_metrics_mvp.csv"
        ).exists(),
        "alert_summary_available": resolve_project_path("outputs/alerts/risk_alert_summary_mvp.json").exists(),
        "root_cause_summary_available": resolve_project_path("outputs/alerts/root_cause_summary_mvp.json").exists(),
        "risk_report_available": resolve_project_path("outputs/reports/risk_analysis_report_mvp.md").exists(),
        "run_logs_available": bool(list_run_logs()),
    }


def summarize_pipeline_status(status: dict[str, bool]) -> dict[str, str]:
    return {
        key: "已就绪" if value else "暂无"
        for key, value in status.items()
    }


def get_output_file_status() -> dict[str, dict[str, str | bool]]:
    outputs = {
        "Alert Summary": resolve_project_path("outputs/alerts/risk_alert_summary_mvp.json"),
        "Root Cause Summary": resolve_project_path("outputs/alerts/root_cause_summary_mvp.json"),
        "Markdown Report": resolve_project_path("outputs/reports/risk_analysis_report_mvp.md"),
        "Report Manifest": resolve_project_path("outputs/reports/risk_analysis_report_manifest_mvp.json"),
    }
    result: dict[str, dict[str, str | bool]] = {}
    for label, path in outputs.items():
        result[label] = {
            "available": path.exists(),
            "path": str(path.relative_to(PROJECT_ROOT)),
        }
    return result


def get_latest_run_log_summary() -> dict[str, Any] | None:
    logs = list_run_logs()
    if not logs:
        return None
    latest = logs[0]
    return {
        "file_name": latest.get("file_name"),
        "run_name": latest.get("run_name"),
        "timestamp": latest.get("timestamp"),
        "status": latest.get("status"),
        "project_phase": latest.get("project_phase"),
    }


def _load_latest_json(directory: str | Path, pattern: str) -> dict[str, Any] | None:
    latest = get_latest_file(directory, pattern)
    payload = load_json_file(latest) if latest else None
    return payload if isinstance(payload, dict) else None
