from __future__ import annotations

import streamlit as st

from ui_components import render_empty_state, render_metric_card, render_page_title, render_project_header, render_safety_banner


def render() -> None:
    render_project_header()
    render_safety_banner()

    df = st.session_state.current_dataframe
    scored = st.session_state.scored_dataframe
    metrics = st.session_state.model_metrics or {}
    high_risk_ratio = _high_risk_ratio(scored)

    cols = st.columns(5)
    with cols[0]:
        render_metric_card("数据状态", st.session_state.dataset_name or "未上传", "当前数据集名称", "ready" if df is not None else "warning")
    with cols[1]:
        render_metric_card("模型状态", "已训练" if st.session_state.trained_model is not None else "未训练", "supervised binary risk model", "ready" if st.session_state.trained_model else "warning")
    with cols[2]:
        render_metric_card("风险等级", _overall_risk_level(high_risk_ratio), "基于高风险占比", "danger" if high_risk_ratio and high_risk_ratio > 0.2 else "info")
    with cols[3]:
        render_metric_card("高风险占比", f"{high_risk_ratio:.1%}" if high_risk_ratio is not None else "暂无", "risk_band = 高风险", "warning")
    with cols[4]:
        render_metric_card("报告状态", "已生成" if st.session_state.generated_report else "未生成", "Markdown report", "ready" if st.session_state.generated_report else "warning")

    render_page_title("工作流进度", "数据接入 → 模型训练 → 风险评估 → 归因分析 → 报告生成")
    progress_cols = st.columns(5)
    steps = [
        ("数据接入", "已完成" if df is not None else "可运行"),
        ("模型训练", "已完成" if st.session_state.trained_model else "可运行" if df is not None and st.session_state.target_col else "未开始"),
        ("风险评估", "已完成" if scored is not None else "可运行" if st.session_state.trained_model else "未开始"),
        ("归因分析", "已完成" if st.session_state.attribution_summary else "可运行" if scored is not None else "未开始"),
        ("报告生成", "已完成" if st.session_state.generated_report else "可运行" if scored is not None else "未开始"),
    ]
    for col, (name, status) in zip(progress_cols, steps):
        with col:
            render_metric_card(name, status, "下一步" if status == "可运行" else "", _status_color(status))

    render_page_title("核心指标", "只展示已有结果，不伪造模型或风险指标。")
    metric_cols = st.columns(5)
    with metric_cols[0]:
        render_metric_card("样本量", len(df) if df is not None else "暂无", "uploaded dataset", "info")
    with metric_cols[1]:
        render_metric_card("特征数", len(df.columns) if df is not None else "暂无", "字段数量", "info")
    with metric_cols[2]:
        render_metric_card("AUC", metrics.get("auc", "暂无"), "模型训练后可用", "ready" if metrics else "warning")
    with metric_cols[3]:
        render_metric_card("KS", metrics.get("ks", "暂无"), "模型训练后可用", "ready" if metrics else "warning")
    with metric_cols[4]:
        render_metric_card("人工确认事项", _human_confirmation_count(), "建议与报告中的复核项", "review")

    render_page_title("快速操作", "从这里跳到对应页面执行任务。")
    st.info("请使用左侧功能分组进入：数据接入、风险评估、归因分析、报告撰写。")
    if df is None:
        render_empty_state("还没有数据", "请先进入“数据接入”页面上传 CSV。", "上传数据后才能训练模型和生成 risk_score。")


def _high_risk_ratio(scored):
    if scored is None or "risk_band" not in scored.columns:
        return None
    return float((scored["risk_band"] == "高风险").mean())


def _overall_risk_level(high_risk_ratio):
    if high_risk_ratio is None:
        return "暂无"
    if high_risk_ratio > 0.2:
        return "高风险"
    if high_risk_ratio > 0.1:
        return "中风险"
    return "低风险"


def _status_color(status: str) -> str:
    return {"已完成": "ready", "可运行": "info", "需要检查": "warning"}.get(status, "warning")


def _human_confirmation_count() -> int:
    return sum(1 for item in st.session_state.recommendations if item.get("human_confirmation_required"))
