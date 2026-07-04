# Phase 9 Streamlit UI Dashboard Design

## v1.0.1 UI Redesign Note

The Streamlit dashboard has been redesigned with a formal local design system.

Changes:

* Added root `DESIGN.md`.
* Added `app/ui_theme.py`.
* Improved Streamlit CSS.
* Improved component hierarchy with cards, badges, empty states, report viewer, and run log table.
* Improved empty-state handling.
* Preserved MVP boundaries: no fabricated data, no LLM integration, no model training, no production deployment, and no automated business actions.

## 1. Phase 9 Goal

Phase 9 implements the first local Streamlit dashboard MVP for Risk Control Agent. The UI name is Risk Control Agent Console, with the Chinese name 智能风控分析工作台.

This phase implements a local Streamlit dashboard MVP. It does not implement production deployment, authentication, LLM integration, model training, database connection, or real credit decisioning.

## 2. UI Architecture

The UI is a display and workflow trigger layer. It reads existing project outputs, renders empty states when files are missing, and triggers only whitelisted local scripts.

Main files:

* `app/streamlit_app.py`
* `app/ui_data_loader.py`
* `app/ui_components.py`
* `app/ui_actions.py`

## 3. Page Structure

The dashboard includes eight Chinese-first pages:

* 风险总览
* 数据源与治理
* 风险预警
* 归因分析
* 模型与数据稳定性
* 报告中心
* 运行日志与审计
* 关于项目

## 4. Data Loading Design

`app/ui_data_loader.py` reads JSON, CSV, Markdown reports, run logs, and pipeline status using `pathlib`. Missing files return `None` or empty results. The loader does not fabricate data, does not write to `data/`, and does not generate files.

## 5. Script Action Design

`app/ui_actions.py` can trigger only these whitelisted scripts:

* `scripts/build_monitoring_tables.py`
* `scripts/run_alert_engine.py`
* `scripts/run_root_cause_analysis.py`
* `scripts/generate_risk_report.py`

It does not accept arbitrary commands, does not run Git commands, does not download datasets, and does not perform business actions.

## 6. Empty State Handling

The UI handles missing official samples, missing monitoring tables, missing alert summary, missing root cause summary, missing report, missing run logs, and partial outputs. It displays Chinese guidance and next-step suggestions instead of fabricated results.

## 7. Safety Boundary

The UI must not provide automatic loan rejection, automatic lending, automatic limit adjustment, automatic channel closure, automatic policy modification, model deployment, user blacklisting, or fraud accusation functions. High-risk content must show Human Confirmation boundaries.

## 8. Chinese-First UI Language Policy

Navigation, buttons, hints, and explanatory text are Chinese-first. Necessary professional terms are retained, including Risk Control Agent, Alert Summary, Root Cause Analysis, Segment Contribution, Model Monitoring, Data Stability, Human Confirmation, AUC, KS, PSI, bad_rate, monitoring table, run log, Markdown report, and MVP.

## 9. What Code Was Added

* Streamlit main app
* UI data loading utilities
* Reusable UI components
* Safe script action wrappers
* App README

## 10. What Code Does Not Do

The code does not fabricate data, does not train models, does not connect to production systems, does not integrate LLM APIs, does not execute Git commands, and does not make real credit decisions.

## 11. Limitations

The dashboard depends on prior pipeline outputs. If `data/processed/`, `outputs/alerts/`, or `outputs/reports/` do not contain expected files, the UI shows empty-state guidance. Current Model Monitoring and Data Stability pages are status and roadmap views, not full model monitoring implementations.

## 12. Next Phase Recommendation

Next phase: Phase 10 - Agent Workflow Packaging and GitHub Showcase.
