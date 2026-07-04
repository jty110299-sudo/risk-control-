from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from ui_pages import (  # noqa: E402
    attribution_analysis,
    audit_logs,
    data_ingestion,
    data_visualization,
    main_console,
    report_writer,
    risk_assessment,
    smart_recommendations,
)
from ui_state import init_session_state  # noqa: E402
from ui_theme import inject_global_css  # noqa: E402


st.set_page_config(
    page_title="Risk Control Agent",
    page_icon="🛡️",
    layout="wide",
)

inject_global_css()
init_session_state()

PAGE_GROUPS = {
    "风险工作台": ["主控台", "数据接入", "风险评估"],
    "分析中心": ["数据可视化", "归因分析", "智能建议"],
    "交付中心": ["报告撰写", "运行审计"],
}

PAGE_RENDERERS = {
    "主控台": main_console.render,
    "数据接入": data_ingestion.render,
    "风险评估": risk_assessment.render,
    "数据可视化": data_visualization.render,
    "归因分析": attribution_analysis.render,
    "智能建议": smart_recommendations.render,
    "报告撰写": report_writer.render,
    "运行审计": audit_logs.render,
}


def render_sidebar() -> str:
    st.sidebar.markdown("## Risk Control Agent")
    st.sidebar.caption("智能风控分析工作台")
    selected = st.session_state.get("selected_page", "主控台")
    for group, pages in PAGE_GROUPS.items():
        st.sidebar.markdown("---")
        st.sidebar.caption(group)
        for page in pages:
            if st.sidebar.button(page, use_container_width=True, type="primary" if page == selected else "secondary"):
                selected = page
                st.session_state.selected_page = page
    st.sidebar.markdown("---")
    st.sidebar.caption("模型输出是分析辅助，不是信贷决策。高风险建议需要人工确认。")
    return selected


def main() -> None:
    selected_page = render_sidebar()
    PAGE_RENDERERS[selected_page]()


if __name__ == "__main__":
    main()
