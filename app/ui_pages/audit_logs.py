from __future__ import annotations

import streamlit as st

from ui_components import render_empty_state, render_page_title


def render() -> None:
    render_page_title("运行审计", "记录上传、训练、评分、报告等操作，不记录敏感原始数据内容。")
    logs = st.session_state.audit_logs
    if not logs:
        render_empty_state("暂无操作日志", "完成上传、训练、评分或报告生成后，这里会显示审计记录。")
        return
    st.dataframe(logs, use_container_width=True, hide_index=True)
    selected = st.selectbox("查看单条日志", list(range(len(logs))), format_func=lambda index: logs[index]["action_name"])
    st.json(logs[selected])
