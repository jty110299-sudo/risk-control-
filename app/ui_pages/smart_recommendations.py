from __future__ import annotations

import streamlit as st

from risk_control_agent.recommendation_engine import (
    filter_prohibited_actions,
    generate_attribution_recommendations,
    generate_data_quality_recommendations,
    generate_model_recommendations,
    generate_next_step_recommendations,
    generate_risk_band_recommendations,
)
from risk_control_agent.visualization_data import get_risk_band_summary
from ui_components import render_empty_state, render_metric_card, render_page_title
from ui_state import add_audit_log


def render() -> None:
    render_page_title("智能建议", "MVP 使用规则化建议，不接入 LLM，不执行业务动作。")
    context = {
        "has_data": st.session_state.current_dataframe is not None,
        "has_model": st.session_state.trained_model is not None,
        "has_target": st.session_state.target_col is not None,
        "has_score": st.session_state.scored_dataframe is not None,
        "has_report": st.session_state.generated_report is not None,
    }
    recommendations = []
    if st.session_state.dataset_profile:
        recommendations += generate_data_quality_recommendations(st.session_state.dataset_profile)
    if st.session_state.model_metrics:
        recommendations += generate_model_recommendations(st.session_state.model_metrics)
    if st.session_state.scored_dataframe is not None:
        recommendations += generate_risk_band_recommendations(get_risk_band_summary(st.session_state.scored_dataframe).to_dict("records"))
    if st.session_state.attribution_summary:
        recommendations += generate_attribution_recommendations(st.session_state.attribution_summary)
    recommendations += generate_next_step_recommendations(context)
    recommendations = filter_prohibited_actions(recommendations)
    st.session_state.recommendations = recommendations
    add_audit_log("generate_recommendations", "success", outputs={"recommendation_count": len(recommendations)})

    if not recommendations:
        render_empty_state("暂无建议", "请先上传数据或生成模型结果。")
        return
    for item in recommendations:
        render_metric_card(item["level"], item["recommendation"], item["boundary"], "danger" if item["human_confirmation_required"] else "info")
        if item["human_confirmation_required"]:
            st.warning("需要人工确认 Human Confirmation")
