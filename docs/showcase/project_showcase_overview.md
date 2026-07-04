# Risk Control Agent 项目展示总览

## 项目名称

Risk Control Agent

## 中文定位

面向金融信贷风控监控场景的智能风控分析工作台。

## English Positioning

A Streamlit-based financial risk control monitoring assistant for credit risk metrics, rule-based alerts, root cause analysis, Markdown risk reports, and audit logs.

## 项目解决的问题

风控分析工作往往需要同时查看数据质量、风险指标、预警规则、贡献因素、报告和运行日志。本项目把这些流程整理成一个可复现的本地 MVP，方便展示从数据治理到风险报告的完整分析链路。

## 核心能力

* 官方公开数据源接入规划
* Data ingestion framework
* Monitoring table construction framework
* Metric calculation utilities
* Rule-based alert engine
* Root Cause Analysis 与 Segment Contribution
* Markdown risk report generation
* Streamlit Dashboard MVP
* run log 与审计记录

## 技术架构

项目采用 Python-first 架构，核心模块位于 `src/risk_control_agent/`，本地脚本位于 `scripts/`，配置位于 `configs/`，UI 位于 `app/`，文档位于 `docs/`，输出位于 `outputs/`。

## 风控专业点

项目覆盖 Credit Risk Monitoring、Fraud Risk Indicators、Risk Alert Rules、Root Cause Analysis、Model Monitoring 规划、Data Stability、Human Confirmation 和报告治理边界。

## 数据策略

项目采用 public-dataset-first 策略，优先使用 Freddie Mac、Fannie Mae、HMDA 等官方或权威公开数据源。当前仓库不内置大型官方数据文件，不使用真实个人金融数据。

## UI 展示能力

Risk Control Agent Console / 智能风控分析工作台可以展示 pipeline status、Alert Summary、Root Cause Analysis、Markdown report、run logs，并触发白名单本地脚本。

## 安全边界

项目不执行真实信贷决策，不自动拒贷，不自动调额，不自动关闭渠道，不自动修改策略，不对个人用户做欺诈定性。

## 当前限制

当前没有内置官方样本数据，没有 LLM integration，没有模型训练，没有生产数据库连接，也不是生产部署系统。

## 后续可扩展方向

* 准备小型官方样本并生成真实 derived outputs
* UI visual polish
* 更完整的 Model Monitoring
* 调度与权限控制
* 受控 LLM 报告辅助
* 生产化部署设计
