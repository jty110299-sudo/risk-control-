from __future__ import annotations

import streamlit as st

from risk_control_agent.attribution import (
    SAFETY_NOTE,
    build_attribution_summary,
    build_segment_risk_summary,
    generate_reason_codes_for_record,
    get_global_feature_importance,
)
from ui_components import render_empty_state, render_metric_card, render_page_title
from ui_state import add_audit_log


def render() -> None:
    render_page_title("归因分析", "选择归因类型 → 选择字段 / 样本 → 查看结果 → 加入报告。")
    scored = st.session_state.scored_dataframe
    model = st.session_state.trained_model
    if scored is None:
        render_empty_state("暂无评分数据", "请先完成风险评估并生成 risk_score。")
        return

    st.info(SAFETY_NOTE)
    attribution_type = st.radio("选择归因类型", ["模型归因", "样本归因", "分群归因"], horizontal=True)

    if attribution_type == "模型归因":
        if model is None:
            render_empty_state("暂无模型", "请先训练模型。")
            return
        importance = get_global_feature_importance(model).head(10)
        if importance.empty:
            render_empty_state("暂无 Feature Importance", "当前模型暂未提供可解释重要性。")
        else:
            st.dataframe(importance, use_container_width=True, hide_index=True)
            st.session_state.attribution_summary = build_attribution_summary(model, scored, st.session_state.target_col)
            add_audit_log("model_attribution", "success", outputs={"top_features": len(importance)})
    elif attribution_type == "样本归因":
        high_risk = scored.sort_values("predicted_probability", ascending=False) if "predicted_probability" in scored.columns else scored
        row_number = st.number_input("选择样本序号", min_value=0, max_value=max(len(high_risk) - 1, 0), value=0)
        record = high_risk.iloc[int(row_number)]
        render_metric_card("risk_score", record.get("risk_score", "暂无"), "该样本评分", "warning")
        render_metric_card("predicted_probability", record.get("predicted_probability", "暂无"), "预测坏样本概率", "info")
        render_metric_card("risk_band", record.get("risk_band", "暂无"), "风险分层", "danger" if record.get("risk_band") == "高风险" else "info")
        reasons = generate_reason_codes_for_record(model, record, scored)
        st.dataframe(reasons, use_container_width=True, hide_index=True)
        render_empty_state("Reason codes 说明", "Reason codes 是模型解释线索，不是最终业务结论。")
    else:
        categorical_cols = scored.select_dtypes(exclude=["number"]).columns.tolist()
        if not categorical_cols:
            render_empty_state("暂无可分群字段", "数据中没有识别到类别字段。")
            return
        segment_col = st.selectbox("选择分群字段", categorical_cols)
        summary = build_segment_risk_summary(scored, segment_col, target_col=st.session_state.target_col)
        if summary.empty:
            render_empty_state("无法生成分群归因", "需要 risk_score 和有效分群字段。")
        else:
            st.dataframe(summary, use_container_width=True, hide_index=True)
            st.session_state.attribution_summary = build_attribution_summary(model, scored, st.session_state.target_col, segment_col)
            add_audit_log("segment_attribution", "success", inputs={"segment_col": segment_col}, outputs={"segments": len(summary)})
