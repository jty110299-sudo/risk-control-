from __future__ import annotations

from typing import Any

import streamlit as st

from ui_theme import (
    COLOR_TOKENS,
    STATUS_COLORS,
    badge_html,
    card_html,
    empty_state_html,
    get_risk_band_color,
    section_header_html,
)


STATUS_LABELS = {
    "official_sample_available": "官方样本",
    "daily_monitoring_table_available": "daily monitoring table",
    "segment_monitoring_table_available": "segment monitoring table",
    "alert_summary_available": "Alert Summary",
    "root_cause_summary_available": "Root Cause Summary",
    "risk_report_available": "Markdown report",
    "run_logs_available": "run log",
}

STATUS_DESCRIPTIONS = {
    "official_sample_available": "data/samples/official/",
    "daily_monitoring_table_available": "data/processed/daily_risk_metrics_mvp.csv",
    "segment_monitoring_table_available": "data/processed/segment_risk_metrics_mvp.csv",
    "alert_summary_available": "outputs/alerts/risk_alert_summary_mvp.json",
    "root_cause_summary_available": "outputs/alerts/root_cause_summary_mvp.json",
    "risk_report_available": "outputs/reports/risk_analysis_report_mvp.md",
    "run_logs_available": "outputs/logs/*.json",
}


def render_project_header() -> None:
    st.markdown(
        """
<div class="rc-hero">
  <div class="rc-hero-title">Risk Control Agent</div>
  <p class="rc-hero-subtitle">上传数据、训练评分模型、生成 risk_score、查看归因、形成报告的智能风控分析工作台。</p>
</div>
""",
        unsafe_allow_html=True,
    )


def render_safety_banner() -> None:
    st.markdown(
        """
<div class="rc-safety">
  <strong>安全边界</strong>：Risk Control Agent 仅用于风险监控、分析辅助和作品集展示。
  模型输出是分析信号，不是信贷决策；所有高风险建议都需要人工确认。
</div>
""",
        unsafe_allow_html=True,
    )


def render_page_title(title: str, subtitle: str | None = None) -> None:
    st.markdown(section_header_html(title, subtitle), unsafe_allow_html=True)


def render_status_cards(status: dict[str, bool]) -> None:
    columns = st.columns(3)
    for index, (key, available) in enumerate(status.items()):
        color = STATUS_COLORS["ready"] if available else STATUS_COLORS["missing"]
        value = "已就绪" if available else "暂无"
        subtitle = STATUS_DESCRIPTIONS.get(key, "本地输出状态")
        with columns[index % 3]:
            st.markdown(
                card_html(STATUS_LABELS.get(key, key), value, subtitle=subtitle, accent_color=color),
                unsafe_allow_html=True,
            )


def render_empty_state(title: str, message: str, next_step: str | None = None) -> None:
    st.markdown(empty_state_html(title, message, next_step), unsafe_allow_html=True)


def render_metric_card(label: str, value: Any, help_text: str | None = None, status: str | None = None) -> None:
    color = STATUS_COLORS.get(status or "info", COLOR_TOKENS["accent_blue"])
    st.markdown(card_html(label, value if value not in (None, "") else "暂无", help_text, color), unsafe_allow_html=True)


def render_alert_summary_card(alert_summary: dict[str, Any] | None) -> None:
    if not alert_summary:
        render_empty_state("暂无 Alert Summary", "请先运行风险预警引擎。", "点击“运行风险预警”。")
        return

    columns = st.columns(3)
    with columns[0]:
        render_risk_level_badge(alert_summary.get("overall_risk_level"))
    with columns[1]:
        render_metric_card("Alert Count", alert_summary.get("alert_count", 0), "触发规则数量", "warning")
    with columns[2]:
        render_human_confirmation_badge(bool(alert_summary.get("human_confirmation_required")))


def render_risk_level_badge(level: object) -> None:
    label = str(level or "暂无风险等级")
    color = get_risk_band_color(label)
    st.markdown(card_html("整体风险等级", label, "基于已生成 risk_score / risk_band。", color), unsafe_allow_html=True)
    st.markdown(badge_html(label, color), unsafe_allow_html=True)


def render_human_confirmation_badge(required: bool) -> None:
    if required:
        color = STATUS_COLORS["danger"]
        label = "需要人工确认 Human Confirmation"
        subtitle = "高风险内容必须由分析人员复核。"
    else:
        color = STATUS_COLORS["ready"]
        label = "暂未标记人工确认"
        subtitle = "当前没有高风险人工确认项，仍需人工审核最终结论。"
    st.markdown(card_html("Human Confirmation", label, subtitle, color), unsafe_allow_html=True)
    st.markdown(badge_html(label, color), unsafe_allow_html=True)


def render_json_viewer(data: Any, title: str) -> None:
    if data in (None, [], {}):
        render_empty_state(f"暂无 {title}", "当前没有对应的结构化输出文件。")
        return
    st.markdown('<div class="rc-table-card">', unsafe_allow_html=True)
    with st.expander(title, expanded=False):
        st.json(data)
    st.markdown("</div>", unsafe_allow_html=True)


def render_markdown_report(markdown_text: str | None) -> None:
    st.markdown('<div class="rc-report-card">', unsafe_allow_html=True)
    if not markdown_text:
        render_empty_state(
            "暂无风险分析报告",
            "请先运行风险预警、归因分析，再生成报告。",
            "点击“生成风险报告”。",
        )
    else:
        st.markdown(markdown_text)
    st.markdown("</div>", unsafe_allow_html=True)


def render_run_log_table(logs: list[dict[str, Any]]) -> None:
    if not logs:
        render_empty_state(
            "暂无运行日志",
            "运行任一流程后会在 outputs/logs/ 中生成日志；上传 GitHub 前应清理本地日志。",
            "先运行一个本地分析脚本，或直接查看 release checklist。",
        )
        return

    rows = [
        {
            "file_name": log.get("file_name"),
            "run_name": log.get("run_name"),
            "timestamp": log.get("timestamp"),
            "status": log.get("status"),
            "project_phase": log.get("project_phase"),
            "output_path": log.get("output_path"),
        }
        for log in logs
    ]
    st.markdown('<div class="rc-table-card">', unsafe_allow_html=True)
    st.dataframe(rows, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)


def render_quick_action_result(result: dict[str, Any]) -> None:
    status = "ready" if result.get("success") else "danger"
    title = "脚本执行完成" if result.get("success") else "脚本执行未成功"
    render_metric_card(title, f"returncode: {result.get('returncode')}", "仅运行 UI 白名单内的本地脚本。", status)
    if result.get("stdout"):
        with st.expander("stdout", expanded=False):
            st.code(str(result.get("stdout")))
    if result.get("stderr"):
        with st.expander("stderr", expanded=False):
            st.code(str(result.get("stderr")))


def render_pipeline_step_card(step_name: str, available: bool, description: str) -> None:
    color = STATUS_COLORS["ready"] if available else STATUS_COLORS["missing"]
    value = "已就绪" if available else "暂无"
    st.markdown(card_html(step_name, value, description, color), unsafe_allow_html=True)
