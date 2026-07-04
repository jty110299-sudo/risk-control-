import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


PROJECT_PHASE = "Phase 5 - MVP Data Ingestion and Monitoring Table Construction"


def create_run_log(
    run_name: str,
    status: str,
    messages: Iterable[str],
    output_path: str | None = None,
    project_phase: str | None = None,
) -> dict:
    return {
        "run_name": run_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "messages": list(messages),
        "output_path": output_path,
        "project_phase": project_phase or PROJECT_PHASE,
    }


def save_run_log(log_dict: dict, logs_dir: str | Path) -> Path:
    directory = Path(logs_dir)
    directory.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = directory / f"{log_dict.get('run_name', 'run')}_{timestamp}.json"
    with path.open("w", encoding="utf-8") as file:
        json.dump(log_dict, file, indent=2, ensure_ascii=False)
    return path
