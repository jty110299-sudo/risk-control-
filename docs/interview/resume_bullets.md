# Resume Bullets

## 中文简历项目描述

Risk Control Agent：面向金融信贷风控监控场景的 Python + Streamlit 本地分析工作台，覆盖公开数据源治理、监控表构建、风险指标计算、规则化预警、分群贡献分析、Markdown 报告生成、Dashboard 展示和运行日志审计。

## English Project Description

Risk Control Agent: A Python and Streamlit-based local risk monitoring assistant for credit risk analytics, covering public data governance, monitoring table construction, risk metric utilities, rule-based alerts, segment contribution analysis, Markdown reports, dashboard display, and audit logs.

## 3 条简洁版中文 bullet

* 使用 Python 和 Streamlit 构建本地风控监控工作台，覆盖指标计算、规则预警、归因线索和报告展示。
* 设计 public-dataset-first 数据治理方案，避免真实个人金融数据和大型原始数据直接进入仓库。
* 实现 run log、发布检查和安全边界文档，保证项目可审计、可解释且不夸大生产能力。

## 5 条详细版中文 bullet

* 设计 Credit Risk Monitoring 主线流程，围绕 bad_rate、delinquency_rate 等指标构建风险监控框架。
* 实现配置化 Risk Alert Rules，引擎输出 Alert Summary，并对高风险结果标注 Human Confirmation。
* 构建 Root Cause Analysis 和 Segment Contribution 框架，将分群贡献作为排查线索而非因果结论。
* 实现确定性 Markdown report generation，区分事实、解释、建议和限制，避免 LLM 式无依据判断。
* 搭建 Streamlit Dashboard MVP 和本地 full pipeline runner，支持结果展示、日志审计和安全脚本触发。

## 3 条英文 bullet

* Built a Python and Streamlit MVP dashboard for credit risk monitoring, rule-based alerts, root cause analysis, Markdown reports, and audit logs.
* Designed a public-dataset-first governance approach to avoid real personal financial data and unsafe large-data commits.
* Implemented deterministic reporting and human-confirmation boundaries to keep risk outputs explainable and auditable.

## 技术栈

Python, Streamlit, pandas, numpy, PyYAML, pytest, Markdown, JSON, Mermaid.

## 风控关键词

Credit Risk Monitoring, Fraud Risk Indicators, bad_rate, delinquency_rate, Risk Alert Rules, Root Cause Analysis, Segment Contribution, Model Monitoring, Data Stability, Human Confirmation.

## 可根据应聘岗位调整的版本

* 数据分析岗：突出指标体系、数据治理、可视化和报告生成。
* 风控策略岗：突出预警规则、阈值校准思路、归因线索和人工确认边界。
* 产品/数据产品岗：突出 Streamlit Dashboard、用户场景、审计日志和 GitHub 展示材料。
