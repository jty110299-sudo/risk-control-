from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOGS_DIR = PROJECT_ROOT / "outputs" / "logs"
PROJECT_PHASE = "Phase 10 - Agent Workflow Packaging and GitHub Showcase"
SAFETY_NOTE = "Risk Control Agent 仅用于风险监控、分析辅助和作品集展示，所有最终业务决策都需要人工审核与确认。"

PIPELINE_STEPS = [
    ("build_monitoring_tables", Path("scripts/build_monitoring_tables.py")),
    ("run_alert_engine", Path("scripts/run_alert_engine.py")),
    ("run_root_cause_analysis", Path("scripts/run_root_cause_analysis.py")),
    ("generate_risk_report", Path("scripts/generate_risk_report.py")),
]


def run_step(step_name: str, script_path: Path) -> dict[str, Any]:
    absolute_script = PROJECT_ROOT / script_path
    print(f"运行步骤：{step_name}")
    if not absolute_script.exists():
        return {
            "step_name": step_name,
            "script": str(script_path),
            "returncode": 1,
            "stdout": "",
            "stderr": "脚本不存在，已跳过。",
            "status": "missing_script",
        }

    completed = subprocess.run(
        [sys.executable, str(absolute_script)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    status = "completed" if completed.returncode == 0 else "failed"
    return {
        "step_name": step_name,
        "script": str(script_path),
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "status": status,
    }


def save_pipeline_log(log: dict[str, Any]) -> Path:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = LOGS_DIR / f"full_pipeline_run_{timestamp}.json"
    path.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def main() -> int:
    timestamp = datetime.now(timezone.utc).isoformat()
    steps = [run_step(step_name, script_path) for step_name, script_path in PIPELINE_STEPS]
    failed_steps = [step for step in steps if step["returncode"] != 0]
    overall_status = "completed_with_possible_skips" if not failed_steps else "failed"

    log = {
        "run_name": "full_pipeline_run",
        "timestamp": timestamp,
        "project_phase": PROJECT_PHASE,
        "steps": steps,
        "overall_status": overall_status,
        "safety_note": SAFETY_NOTE,
    }
    log_path = save_pipeline_log(log)

    print("完整本地流程已结束。")
    print(f"overall_status: {overall_status}")
    print(f"运行日志已保存：{log_path}")
    print("如果当前没有官方样本或 processed monitoring tables，部分步骤会按既有逻辑跳过。")
    return 0 if not failed_steps else 1


if __name__ == "__main__":
    raise SystemExit(main())
