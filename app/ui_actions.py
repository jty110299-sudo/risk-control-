from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]

ALLOWED_SCRIPTS = {
    "build_monitoring_tables": Path("scripts/build_monitoring_tables.py"),
    "run_alert_engine": Path("scripts/run_alert_engine.py"),
    "run_root_cause_analysis": Path("scripts/run_root_cause_analysis.py"),
    "generate_risk_report": Path("scripts/generate_risk_report.py"),
}


def run_script(script_name: str) -> dict[str, Any]:
    if script_name not in ALLOWED_SCRIPTS:
        return {
            "success": False,
            "returncode": 1,
            "stdout": "",
            "stderr": "脚本不在 UI 白名单中，已拒绝执行。",
        }

    script_path = PROJECT_ROOT / ALLOWED_SCRIPTS[script_name]
    if not script_path.exists():
        return {
            "success": False,
            "returncode": 1,
            "stdout": "",
            "stderr": f"未找到脚本：{ALLOWED_SCRIPTS[script_name]}",
        }

    completed = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "success": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def run_monitoring_table_builder() -> dict[str, Any]:
    return run_script("build_monitoring_tables")


def run_alert_engine() -> dict[str, Any]:
    return run_script("run_alert_engine")


def run_root_cause_analysis() -> dict[str, Any]:
    return run_script("run_root_cause_analysis")


def run_report_generation() -> dict[str, Any]:
    return run_script("generate_risk_report")
