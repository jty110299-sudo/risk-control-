from __future__ import annotations

from html import escape

import streamlit as st


COLOR_TOKENS = {
    "background": "#F5F5F7",
    "surface": "#FFFFFF",
    "surface_soft": "#FBFBFD",
    "text_primary": "#1D1D1F",
    "text_secondary": "#6E6E73",
    "accent_blue": "#0071E3",
    "border": "#D2D2D7",
    "success": "#34C759",
    "warning": "#FF9F0A",
    "danger": "#FF3B30",
    "purple": "#AF52DE",
}

STATUS_COLORS = {
    "ready": COLOR_TOKENS["success"],
    "missing": COLOR_TOKENS["text_secondary"],
    "warning": COLOR_TOKENS["warning"],
    "danger": COLOR_TOKENS["danger"],
    "info": COLOR_TOKENS["accent_blue"],
    "review": COLOR_TOKENS["purple"],
}

RISK_LEVEL_COLORS = {
    "低风险": COLOR_TOKENS["success"],
    "中低风险": COLOR_TOKENS["accent_blue"],
    "中风险": COLOR_TOKENS["warning"],
    "中高风险": "#FF7A00",
    "高风险": COLOR_TOKENS["danger"],
}


def inject_global_css() -> None:
    st.markdown(
        f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
  background: {COLOR_TOKENS["background"]};
  color: {COLOR_TOKENS["text_primary"]};
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", sans-serif;
}}

[data-testid="stAppViewContainer"] *,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span,
[data-testid="stText"],
[data-testid="stCaptionContainer"],
label,
.stSelectbox label,
.stMultiSelect label,
.stTextInput label,
.stNumberInput label,
.stRadio label,
.stFileUploader label,
.stCheckbox label {{
  color: {COLOR_TOKENS["text_primary"]};
}}

[data-testid="stCaptionContainer"],
.stCaption,
small {{
  color: {COLOR_TOKENS["text_secondary"]} !important;
}}

[data-testid="stHeader"] {{
  background: rgba(245,245,247,0.88);
  border-bottom: 1px solid rgba(210,210,215,0.75);
}}

[data-testid="stSidebar"] {{
  background: #FFFFFF;
  border-right: 1px solid {COLOR_TOKENS["border"]};
}}

[data-testid="stSidebar"] * {{
  color: {COLOR_TOKENS["text_primary"]};
}}

[data-testid="stSidebar"] .stButton > button {{
  background: #FFFFFF;
  border: 1px solid {COLOR_TOKENS["border"]};
  color: {COLOR_TOKENS["text_primary"]};
}}

[data-testid="stSidebar"] .stButton > button:hover {{
  background: #F5F5F7;
  border-color: {COLOR_TOKENS["accent_blue"]};
  color: {COLOR_TOKENS["text_primary"]};
}}

.block-container {{
  max-width: 1180px;
  padding-top: 2.5rem;
  padding-bottom: 3rem;
}}

h1, h2, h3 {{
  color: {COLOR_TOKENS["text_primary"]};
  letter-spacing: 0;
}}

p, li, span, div {{
  color: inherit;
}}

.rc-hero {{
  background: linear-gradient(180deg, #FFFFFF 0%, #FBFBFD 100%);
  border: 1px solid {COLOR_TOKENS["border"]};
  border-radius: 28px;
  padding: 34px 38px;
  margin-bottom: 22px;
  box-shadow: 0 18px 55px rgba(0,0,0,0.08);
}}

.rc-hero-title {{
  font-size: 40px;
  line-height: 1.08;
  font-weight: 760;
  margin: 0 0 10px 0;
}}

.rc-hero-subtitle {{
  color: {COLOR_TOKENS["text_secondary"]};
  font-size: 17px;
  line-height: 1.7;
  margin: 0;
}}

.rc-card {{
  background: {COLOR_TOKENS["surface"]};
  border: 1px solid rgba(210,210,215,0.85);
  border-radius: 22px;
  padding: 22px;
  margin-bottom: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
}}

.rc-card-label {{
  color: {COLOR_TOKENS["text_secondary"]};
  font-size: 13px;
  margin-bottom: 9px;
}}

.rc-card-value {{
  color: {COLOR_TOKENS["text_primary"]};
  font-size: 29px;
  line-height: 1.12;
  font-weight: 740;
  margin-bottom: 8px;
}}

.rc-card-subtitle {{
  color: {COLOR_TOKENS["text_secondary"]};
  font-size: 13px;
  line-height: 1.55;
}}

.rc-section {{
  margin: 30px 0 14px 0;
}}

.rc-section-title {{
  font-size: 25px;
  line-height: 1.18;
  font-weight: 730;
  margin: 0 0 6px 0;
}}

.rc-section-subtitle {{
  color: {COLOR_TOKENS["text_secondary"]};
  font-size: 15px;
  line-height: 1.6;
  margin: 0;
}}

.rc-badge {{
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 6px 11px;
  font-size: 12px;
  font-weight: 700;
  margin: 2px 4px 2px 0;
}}

.rc-empty {{
  background: {COLOR_TOKENS["surface_soft"]};
  border: 1px dashed {COLOR_TOKENS["border"]};
  border-radius: 22px;
  padding: 24px;
  margin: 14px 0;
}}

.rc-empty-title {{
  font-size: 18px;
  font-weight: 730;
  margin-bottom: 8px;
}}

.rc-empty-message, .rc-empty-next {{
  color: {COLOR_TOKENS["text_secondary"]};
  font-size: 14px;
  line-height: 1.65;
}}

.rc-empty-next {{
  color: {COLOR_TOKENS["accent_blue"]};
  margin-top: 10px;
}}

.rc-safety {{
  background: #F2F7FF;
  border: 1px solid #B9D8FF;
  border-radius: 20px;
  padding: 14px 18px;
  color: {COLOR_TOKENS["text_primary"]};
  margin-bottom: 18px;
}}

.stButton > button, .stDownloadButton > button {{
  border-radius: 999px;
  border: 1px solid {COLOR_TOKENS["accent_blue"]};
  background: {COLOR_TOKENS["accent_blue"]};
  color: #FFFFFF;
  font-weight: 700;
  min-height: 42px;
}}

.stButton > button:hover, .stDownloadButton > button:hover {{
  background: #005BB5;
  color: #FFFFFF;
  border-color: #005BB5;
}}

.stButton > button *,
.stDownloadButton > button * {{
  color: inherit !important;
}}

input,
textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea {{
  background: #FFFFFF !important;
  color: {COLOR_TOKENS["text_primary"]} !important;
  caret-color: {COLOR_TOKENS["accent_blue"]};
}}

[data-baseweb="select"] > div,
[data-baseweb="popover"] {{
  background: #FFFFFF !important;
  color: {COLOR_TOKENS["text_primary"]} !important;
}}

[data-baseweb="select"] span,
[data-baseweb="popover"] span,
[data-baseweb="popover"] li,
[role="option"],
[role="listbox"] * {{
  color: {COLOR_TOKENS["text_primary"]} !important;
}}

[data-testid="stFileUploader"] section {{
  background: #FFFFFF;
  border: 1px dashed {COLOR_TOKENS["border"]};
  border-radius: 18px;
}}

[data-testid="stFileUploader"] section *,
[data-testid="stUploadedFile"] * {{
  color: {COLOR_TOKENS["text_primary"]} !important;
}}

[data-testid="stRadio"] *,
[data-testid="stCheckbox"] *,
[data-testid="stMultiSelect"] *,
[data-testid="stSelectbox"] *,
[data-testid="stNumberInput"] *,
[data-testid="stTextInput"] * {{
  color: {COLOR_TOKENS["text_primary"]};
}}

[data-testid="stExpander"] {{
  background: #FFFFFF;
  border: 1px solid {COLOR_TOKENS["border"]};
  border-radius: 18px;
}}

[data-testid="stExpander"] * {{
  color: {COLOR_TOKENS["text_primary"]};
}}

[data-testid="stAlert"] {{
  background: #FFFFFF !important;
  border: 1px solid {COLOR_TOKENS["border"]};
  border-radius: 18px;
}}

[data-testid="stAlert"] * {{
  color: {COLOR_TOKENS["text_primary"]} !important;
}}

[data-testid="stDataFrame"], [data-testid="stTable"] {{
  border: 1px solid {COLOR_TOKENS["border"]};
  border-radius: 18px;
  overflow: hidden;
  background: #FFFFFF;
}}

[data-testid="stDataFrame"] *,
[data-testid="stTable"] * {{
  color: {COLOR_TOKENS["text_primary"]};
}}
</style>
""",
        unsafe_allow_html=True,
    )


def card_html(title: str, value: object, subtitle: str | None = None, accent_color: str | None = None) -> str:
    border = f' style="border-top: 4px solid {escape(accent_color)};"' if accent_color else ""
    subtitle_html = f'<div class="rc-card-subtitle">{escape(subtitle)}</div>' if subtitle else ""
    return (
        f'<div class="rc-card"{border}>'
        f'<div class="rc-card-label">{escape(title)}</div>'
        f'<div class="rc-card-value">{escape(str(value))}</div>'
        f"{subtitle_html}</div>"
    )


def badge_html(label: str, color: str, background: str | None = None) -> str:
    background_color = background or _hex_to_rgba(color, 0.12)
    return f'<span class="rc-badge" style="color:{escape(color)};background:{escape(background_color)};">{escape(label)}</span>'


def section_header_html(title: str, subtitle: str | None = None) -> str:
    subtitle_html = f'<p class="rc-section-subtitle">{escape(subtitle)}</p>' if subtitle else ""
    return f'<div class="rc-section"><h2 class="rc-section-title">{escape(title)}</h2>{subtitle_html}</div>'


def empty_state_html(title: str, message: str, next_step: str | None = None) -> str:
    next_html = f'<div class="rc-empty-next">下一步：{escape(next_step)}</div>' if next_step else ""
    return (
        '<div class="rc-empty">'
        f'<div class="rc-empty-title">{escape(title)}</div>'
        f'<div class="rc-empty-message">{escape(message)}</div>'
        f"{next_html}</div>"
    )


def get_risk_band_color(band: object) -> str:
    return RISK_LEVEL_COLORS.get(str(band), COLOR_TOKENS["text_secondary"])


def _hex_to_rgba(hex_color: str, alpha: float) -> str:
    cleaned = hex_color.lstrip("#")
    red = int(cleaned[0:2], 16)
    green = int(cleaned[2:4], 16)
    blue = int(cleaned[4:6], 16)
    return f"rgba({red}, {green}, {blue}, {alpha})"
