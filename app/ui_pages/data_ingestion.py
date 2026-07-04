from __future__ import annotations

from pathlib import Path

import streamlit as st

from risk_control_agent.user_data import (
    calculate_missing_summary,
    get_basic_dataset_profile,
    infer_column_types,
    load_user_dataset,
    save_uploaded_file,
    validate_training_target,
)
from ui_components import render_empty_state, render_metric_card, render_page_title
from ui_state import add_audit_log


def render() -> None:
    render_page_title("数据接入", "上传 CSV，识别字段，选择 target label，并确定训练 / 评分模式。")
    uploaded = st.file_uploader("上传 CSV 文件", type=["csv"])
    if uploaded is not None and st.button("读取并保存到本地临时目录", use_container_width=False):
        path = save_uploaded_file(uploaded, Path("data/user_uploads"))
        df = load_user_dataset(path)
        st.session_state.uploaded_data_path = str(path)
        st.session_state.dataset_name = uploaded.name
        st.session_state.current_dataframe = df
        st.session_state.dataset_profile = get_basic_dataset_profile(df)
        add_audit_log("upload_dataset", "success", inputs={"file_name": uploaded.name}, outputs={"path": str(path), "rows": len(df)})
        st.success("数据已读取。上传文件会被 .gitignore 忽略，不应提交到 GitHub。")

    df = st.session_state.current_dataframe
    if df is None:
        render_empty_state("等待上传数据", "当前仅支持 CSV。Excel 支持暂未启用，避免额外依赖。", "上传脱敏 CSV 后继续字段配置。")
        return

    profile = get_basic_dataset_profile(df)
    st.session_state.dataset_profile = profile
    types = infer_column_types(df)

    cols = st.columns(4)
    with cols[0]:
        render_metric_card("样本量", profile["row_count"], "数据行数", "info")
    with cols[1]:
        render_metric_card("字段数", profile["column_count"], "全部列", "info")
    with cols[2]:
        render_metric_card("数值字段", profile["numeric_count"], "可用于建模和分布分析", "ready")
    with cols[3]:
        render_metric_card("缺失字段数", profile["missing_column_count"], "存在缺失的列", "warning")

    render_page_title("数据预览", "仅展示前 20 行。不要上传真实个人敏感信息。")
    st.dataframe(df.head(20), use_container_width=True)

    render_page_title("字段配置", "监督模型必须选择 target label；不能伪造 target。")
    columns = df.columns.tolist()
    mode = st.radio(
        "训练 / 评分模式",
        ["有标签数据：训练风控模型", "无标签但已有 score：直接做风险评估", "无标签且无 score：仅探索分析"],
        horizontal=True,
    )
    st.session_state.mode = mode
    target_col = st.selectbox("目标变量 target label", [""] + columns)
    id_col = st.selectbox("ID 字段（可选）", [""] + columns)
    time_col = st.selectbox("时间字段（可选）", [""] + columns)
    st.session_state.target_col = target_col or None
    st.session_state.id_col = id_col or None
    st.session_state.time_col = time_col or None

    if mode == "有标签数据：训练风控模型":
        validation = validate_training_target(df, st.session_state.target_col)
        if validation["valid"]:
            st.success(validation["message"])
        else:
            st.warning(validation["message"])
    elif mode == "无标签但已有 score：直接做风险评估":
        st.info("请选择已有 score 字段后，可在风险评估页进行风险分层。")
    else:
        st.warning("无 target 且无 score 时，不能训练 supervised credit risk model，只能做数据质量和探索分析。")

    render_page_title("字段类型识别", "自动识别结果可作为字段映射参考。")
    st.json(types)
    render_page_title("缺失率概览", "优先检查缺失率高的字段。")
    st.dataframe(calculate_missing_summary(df), use_container_width=True, hide_index=True)
