# Interview Talk Track

## 30 秒版本

Risk Control Agent 是我做的一个金融信贷风控监控作品集项目，主线是 Credit Risk Monitoring。它从公开数据源治理开始，设计了数据接入、指标计算、规则化预警、分群贡献分析、Markdown 风险报告、Streamlit Dashboard 和 run log 审计。项目不是自动信贷决策系统，所有高风险结论都需要 Human Confirmation。

## 1 分钟版本

这个项目模拟风控分析师日常监控风险指标的工作流。我没有用 LLM 直接判断风险，而是采用规则化 Risk Alert Rules，并把结论绑定到指标、规则或明确假设。归因部分做的是 Segment Contribution 和 Root Cause Analysis 线索，不把贡献当成因果证明。报告生成会区分事实、解释、建议和限制。UI 使用 Streamlit，主要用于展示和触发本地脚本，不执行自动拒贷、调额或策略修改。

## 3 分钟版本

Risk Control Agent 的设计目标是展示一条可解释、可审计的风控监控链路。数据策略上，我采用 public-dataset-first，优先考虑 Freddie Mac、Fannie Mae 和 HMDA 等官方或权威公开数据源，不把 synthetic data 作为主数据源。工程上，项目分为配置、核心 Python 模块、本地 scripts、outputs logs、Streamlit UI 和文档体系。分析链路包括 monitoring table construction、metric calculation、rule-based alert engine、root cause and segment contribution、Markdown report generation 和 UI 展示。项目强调安全边界：不处理真实个人金融数据，不做真实信贷审批，不执行自动业务动作，不把 LLM 当作黑盒风险判断器。

## 技术版讲解

项目采用 Python-first 架构，核心模块拆分在 `src/risk_control_agent/`，配置在 `configs/`，入口脚本在 `scripts/`。`run_full_pipeline.py` 串联已有脚本，`project_health_check.py` 做发布前检查。Streamlit UI 读取 outputs 和 logs，并通过白名单脚本触发本地流程。

## 风控业务版讲解

业务上我关注 bad_rate、delinquency_rate、serious_delinquency_rate、Risk Alert Rules、Human Confirmation 和数据治理。预警不是最终业务结论，而是触发分析师复核的信号。

## 产品设计版讲解

产品上我把它设计成智能风控分析工作台。页面覆盖风险总览、数据源与治理、风险预警、归因分析、模型与数据稳定性、报告中心、运行日志与审计。

## 项目亮点

* public-dataset-first 数据策略
* 规则化预警而不是 LLM 凭空判断
* 贡献分析是排查线索，不是因果证明
* 报告区分事实、解释、建议和限制
* UI 是分析工作台，不是自动决策系统
* GitHub 数据安全和可审计设计

## 项目边界

项目没有内置大型官方数据，没有生产数据库连接，没有 LLM integration，没有模型训练，没有真实信贷决策。

## 设计取舍

第一版优先做可解释和可审计，所以使用规则引擎和确定性报告，而不是直接上复杂模型或 LLM。UI 先用 Streamlit 做本地 MVP，后续再做视觉优化。

## 后续优化方向

准备小型官方样本，跑出真实 derived outputs；优化 UI 视觉；补充模型监控；在严格边界下探索 LLM 报告辅助。
