from __future__ import annotations

import streamlit as st


DEFAULT_STATE = {
    "uploaded_data_path": None,
    "dataset_name": None,
    "current_dataframe": None,
    "dataset_profile": None,
    "target_col": None,
    "id_col": None,
    "time_col": None,
    "mode": "有标签数据：训练风控模型",
    "excluded_cols": [],
    "trained_model": None,
    "model_metrics": None,
    "feature_cols": [],
    "model_path": None,
    "scored_dataframe": None,
    "attribution_summary": None,
    "recommendations": [],
    "report_sections": [],
    "generated_report": None,
    "audit_logs": [],
}


def init_session_state() -> None:
    for key, value in DEFAULT_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value.copy() if isinstance(value, list) else value


def add_audit_log(action_name: str, status: str, inputs: dict | None = None, outputs: dict | None = None, warnings: list | None = None, errors: list | None = None) -> None:
    from datetime import datetime, timezone

    st.session_state.audit_logs.append(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action_name": action_name,
            "status": status,
            "inputs": inputs or {},
            "outputs": outputs or {},
            "warnings": warnings or [],
            "errors": errors or [],
        }
    )
