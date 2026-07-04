from __future__ import annotations

import streamlit as st

from risk_control_agent.visualization_data import (
    get_categorical_top_values,
    get_missing_rate_ranking,
    get_risk_band_summary,
    get_score_distribution,
    get_target_by_risk_band,
)
from ui_components import render_empty_state, render_metric_card, render_page_title


def render() -> None:
    render_page_title("数据可视化", "对上传数据、评分结果和模型结果进行交互式探索。")
    df = st.session_state.scored_dataframe if st.session_state.scored_dataframe is not None else st.session_state.current_dataframe
    if df is None:
        render_empty_state("暂无数据", "请先在“数据接入”页面上传数据。")
        return

    target_col = st.session_state.target_col
    cols = st.columns(6)
    with cols[0]:
        render_metric_card("样本量", len(df), "rows", "info")
    with cols[1]:
        render_metric_card("特征数", len(df.columns), "columns", "info")
    with cols[2]:
        render_metric_card("缺失字段数", int((df.isna().sum() > 0).sum()), "missing columns", "warning")
    with cols[3]:
        bad_rate = round(float(df[target_col].mean()), 4) if target_col and target_col in df.columns else "暂无"
        render_metric_card("坏样本率", bad_rate, "target=1", "warning")
    with cols[4]:
        avg_score = round(float(df["risk_score"].mean()), 2) if "risk_score" in df.columns else "暂无"
        render_metric_card("平均 risk_score", avg_score, "score 越低风险越高", "info")
    with cols[5]:
        high_ratio = round(float((df["risk_band"] == "高风险").mean()), 4) if "risk_band" in df.columns else "暂无"
        render_metric_card("高风险占比", high_ratio, "risk_band=高风险", "danger" if high_ratio != "暂无" and high_ratio > 0.2 else "info")

    render_page_title("图表区", "图表只基于当前数据，不使用随机假图。")
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
    chart_type = st.selectbox("选择图表类型", ["数值字段分布", "类别字段 Top N", "缺失率排行", "risk_score 分布", "risk_band 占比", "target 与 risk_band"])
    if chart_type == "数值字段分布" and numeric_cols:
        col = st.selectbox("选择数值字段", numeric_cols)
        st.bar_chart(df[col].dropna().value_counts(bins=20).sort_index())
    elif chart_type == "类别字段 Top N" and categorical_cols:
        col = st.selectbox("选择类别字段", categorical_cols)
        top_values = get_categorical_top_values(df, col)
        st.bar_chart(top_values, x=col, y="count")
    elif chart_type == "缺失率排行":
        missing = get_missing_rate_ranking(df).head(20)
        st.bar_chart(missing, x="column", y="missing_rate")
    elif chart_type == "risk_score 分布":
        score_dist = get_score_distribution(df)
        if score_dist.empty:
            render_empty_state("暂无 risk_score", "请先在风险评估页生成评分。")
        else:
            st.bar_chart(score_dist["risk_score"].value_counts(bins=20).sort_index())
    elif chart_type == "risk_band 占比":
        summary = get_risk_band_summary(df)
        if summary.empty:
            render_empty_state("暂无 risk_band", "请先生成风险分层。")
        else:
            st.bar_chart(summary, x="risk_band", y="ratio")
    else:
        summary = get_target_by_risk_band(df, target_col) if target_col else None
        if summary is None or summary.empty:
            render_empty_state("暂无 target 与 risk_band 关系", "需要同时有 target 和 risk_band。")
        else:
            st.bar_chart(summary, x="risk_band", y="bad_rate")
