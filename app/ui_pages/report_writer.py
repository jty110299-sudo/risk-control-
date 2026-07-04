from __future__ import annotations

import streamlit as st

from risk_control_agent.interactive_report import build_user_report_context, generate_user_markdown_report, save_user_report
from risk_control_agent.visualization_data import get_risk_band_summary
from ui_components import render_empty_state, render_markdown_report, render_page_title
from ui_state import add_audit_log


SECTION_OPTIONS = {
    "报告摘要": "summary",
    "数据概览": "data_overview",
    "模型训练结果": "model_results",
    "风险评分分布": "risk_distribution",
    "归因分析结果": "attribution",
    "智能建议": "recommendations",
    "人工确认事项": "human_confirmation",
    "限制说明": "limitations",
    "免责声明": "disclaimer",
}


def render() -> None:
    render_page_title("报告撰写", "选择报告章节，生成可下载 Markdown 报告。")
    if st.session_state.current_dataframe is None or st.session_state.scored_dataframe is None:
        render_empty_state("请先完成数据接入和风险评估", "没有数据或评分结果时，不生成空洞报告。")
        return
    selected_labels = st.multiselect("选择报告包含章节", list(SECTION_OPTIONS), default=list(SECTION_OPTIONS))
    selected_sections = [SECTION_OPTIONS[label] for label in selected_labels]
    if st.button("生成报告", use_container_width=False):
        context = build_user_report_context(
            dataset_profile=st.session_state.dataset_profile,
            model_metrics=st.session_state.model_metrics,
            risk_band_summary=get_risk_band_summary(st.session_state.scored_dataframe).to_dict("records"),
            attribution_summary=st.session_state.attribution_summary,
            recommendations=st.session_state.recommendations,
        )
        report = generate_user_markdown_report(context, selected_sections)
        save_user_report(report, "outputs/reports/user_risk_analysis_report.md")
        st.session_state.generated_report = report
        add_audit_log("generate_user_report", "success", outputs={"path": "outputs/reports/user_risk_analysis_report.md"})
        st.success("报告已生成。")
    render_markdown_report(st.session_state.generated_report)
    if st.session_state.generated_report:
        st.download_button("下载 Markdown", st.session_state.generated_report, "user_risk_analysis_report.md", "text/markdown")
        html_text = "<html><body>" + st.session_state.generated_report.replace("\n", "<br>") + "</body></html>"
        st.download_button("下载 HTML", html_text, "user_risk_analysis_report.html", "text/html")
