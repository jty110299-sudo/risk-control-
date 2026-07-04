# UI Dashboard Design

## v0.9.0 Implementation Status

Streamlit UI MVP has been implemented as a local dashboard named Risk Control Agent Console / 智能风控分析工作台.

The UI uses Chinese-first navigation and explanatory text, while retaining necessary professional English terms such as Alert Summary, Root Cause Analysis, Segment Contribution, Model Monitoring, Data Stability, Human Confirmation, AUC, KS, PSI, monitoring table, run log, and Markdown report.

Implemented pages:

* 风险总览
* 数据源与治理
* 风险预警
* 归因分析
* 模型与数据稳定性
* 报告中心
* 运行日志与审计
* 关于项目

The UI does not execute automatic business actions, does not integrate LLM APIs, and does not connect to production systems. Missing files are shown as empty states rather than fabricated results.

## v1.0.1 UI Design System and Dashboard Redesign

The project now includes root `DESIGN.md` as the UI design system guide. The Streamlit UI has been redesigned into a professional dark financial risk monitoring workstation.

The redesigned UI uses Chinese-first navigation and page content. It includes cards, badges, empty states, safety banner, report viewer, and run log table components. Risk level and Human Confirmation states are visually highlighted.

The UI still does not execute automatic business actions, does not integrate LLM APIs, does not train models, does not fabricate missing data, and does not represent a production system.

## 1. Purpose

The UI should make Risk Control Agent usable by risk analysts, not just executable as a backend script.

交互界面用于让风控分析人员查看风险变化、异常规则、贡献因素、模型稳定性、数据质量和未来自动生成的风险报告。

This document is a product design specification only. It does not mean the UI has been implemented.

## 2. Target Users

* Risk analysts
* Model monitoring analysts
* Risk operation teams
* Data analysts
* Portfolio reviewers

## 3. Recommended MVP UI Technology

Recommended MVP technology: Streamlit

Streamlit is recommended for the first UI version because:

* It is suitable for Python data analysis projects.
* It can display metric cards, charts, tables, and report previews efficiently.
* It is appropriate for a GitHub portfolio project.
* It can later integrate metric calculation, anomaly detection, root cause analysis, and report generation modules.
* It is more suitable than React or Vue for the first MVP of this project.

React, Vue, and FastAPI can be future extension directions, but they are not the first-version priority.

## 4. Planned UI Pages

### Page 1: Overview Dashboard

Purpose: show the overall risk status.

Planned content:

* Analysis date
* Overall risk level
* Key metric cards
* `bad_rate` trend
* `overdue_rate` trend
* `approval_rate` trend
* Number of triggered alert rules
* Human confirmation required flag

### Page 2: Data Source and Governance

Purpose: show data source and data governance information.

Planned content:

* Dataset source
* Public dataset name
* Source link or source reference
* Data period
* Sample size
* Whether synthetic supplement is used
* Data usage disclaimer
* GitHub storage note

### Page 3: Risk Monitoring

Purpose: show core risk metric changes.

Planned content:

* `application_count`
* `approval_rate`
* `rejection_rate`
* `overdue_rate`
* `bad_rate`
* Fraud indicator if available
* Baseline comparison
* Triggered metric-level alerts

### Page 4: Root Cause Analysis

Purpose: show contribution factors behind risk changes.

Planned content:

* Segment contribution table
* Channel contribution
* Product contribution
* Region contribution
* Customer segment contribution
* Score band migration
* Top contributing segments
* Note that contribution is not causal proof

### Page 5: Model and Data Stability

Purpose: show model performance and data quality changes.

Planned content:

* AUC
* KS
* Precision
* Recall
* PSI
* Feature missing rate
* Feature drift
* Score distribution shift
* Data quality flags

### Page 6: Report Center

Purpose: show and export risk analysis reports.

Planned content:

* Report preview
* Risk level
* Triggered alert rules
* Executive summary
* Operations recommendations
* Items requiring human confirmation
* Download Markdown report
* View agent run log

## 5. User Interaction Flow

Future user flow:

1. Select dataset or monitoring period.
2. Run risk analysis.
3. Review overall risk level.
4. Inspect triggered alerts.
5. Review root cause analysis.
6. Check model and data stability.
7. Generate or open risk report.
8. Export report.
9. Review items requiring human confirmation.

This is a future design, not a currently implemented capability.

## 6. Safety Boundary in UI

The UI must not provide:

* Auto approve loan
* Auto reject loan
* Auto adjust credit limit
* Auto close channel
* Auto modify production policy
* Auto deploy or remove model
* Accuse individual user of fraud

The UI may provide:

* Generate risk report
* View triggered rules
* View contribution analysis
* Export report
* Mark as requiring human confirmation
* Generate investigation suggestions

## 7. Future Extension

Future extensions may include:

* Authentication
* FastAPI backend
* React dashboard
* Database connection
* Scheduled monitoring
* Alert notification
* Role-based permission control

These are not MVP-stage goals.
