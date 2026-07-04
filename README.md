# Risk Control Agent

Risk Control Agent 是一个面向金融信贷风控监控场景的本地 MVP 分析工作台。项目以 Credit Risk Monitoring 为主线，辅助覆盖 Fraud Risk Indicators，用 Streamlit 提供中文优先的交互界面，展示从数据接入、模型评分、风险预警、Root Cause Analysis 到风险报告生成的完整分析流程。

这个项目不是生产级风控系统，也不是自动信贷审批系统。它的定位是 portfolio project / local MVP，用于展示风控分析流程、指标理解、模型评估、规则预警、归因分析、报告表达和安全边界意识。

## 当前状态

当前版本已经不是单纯的文档阶段。项目已经包含可运行的本地 Streamlit UI 和核心 Python 模块，可以在用户上传本地 CSV 后完成 MVP 级风控分析流程。

已实现的能力包括：

* 上传 CSV，并识别字段类型、缺失率和基础数据概况
* 选择 target label，进行本地二分类模型训练
* 支持 Logistic Regression、Random Forest、Gradient Boosting 和 XGBoost
* 展示 AUC、KS、Precision、Recall、F1 等模型评估指标
* 支持轻量 GridSearchCV 调参，并在训练前展示预计耗时、训练轮数、参与训练样本数和特征数
* 生成 `predicted_probability`、`risk_score` 和 `risk_band`
* 进行交互式数据可视化
* 展示模型归因、样本 reason codes 和 Segment Contribution
* 基于规则生成风险提醒和智能建议
* 撰写并下载 Markdown / HTML 风险分析报告
* 记录本地操作审计日志
* 提供风控知识库、产品设计文档、技术设计文档和面试展示材料

## 明确边界

为了避免误解，Risk Control Agent 当前不做以下事情：

* 不内置大型官方数据集
* 不使用真实个人金融数据
* 不接入 LLM API
* 不训练或部署生产级模型
* 不连接生产数据库
* 不执行真实信贷审批
* 不自动拒贷
* 不自动放款
* 不自动调整授信额度
* 不自动关闭渠道
* 不自动修改生产风控策略
* 不自动上线或下线模型
* 不绕过人工审批
* 不对个人用户直接做欺诈定性

当前项目中的模型训练只用于本地 MVP 分析和作品集展示。模型输出是风险分析信号，不是业务决策结论。所有高风险建议都需要 Human Confirmation。

## 项目价值

这个项目的重点不是声称自己能替代真实金融机构的风控系统，而是展示一个风控分析人员应当如何组织分析链路：

* 如何理解 Credit Risk Monitoring 和 Fraud Risk Indicators 的边界
* 如何设计风险指标、模型监控指标和数据质量检查
* 如何从上传数据进入模型训练、AUC / KS 评估和风险评分
* 如何把风险异常拆解到分群、特征和规则层面
* 如何把分析结果整理成可复核的风险报告
* 如何在 Agent 或 dashboard 产品中设置安全边界和人工确认机制

对中文风控实习、数据分析、数据产品和金融科技方向面试来说，本项目更像一个可运行的风控分析样例，而不是生产系统仿真。

## 运行方式

安装依赖：

```bash
pip install -r requirements.txt
```

启动本地 UI：

```bash
streamlit run app/streamlit_app.py
```

运行测试：

```bash
python -m pytest
```

运行项目健康检查：

```bash
python scripts/project_health_check.py
```

运行完整本地 pipeline：

```bash
python scripts/run_full_pipeline.py
```

## UI 使用流程

推荐按以下顺序体验：

1. 打开 Streamlit UI
2. 在数据接入页面上传本地 CSV
3. 检查字段识别、缺失率和 target label
4. 在风险评估页面选择模型类型
5. 选择快速训练、标准训练或调参训练
6. 查看训练前的预计耗时、训练轮数、样本数和特征数
7. 训练模型并查看 AUC、KS、Precision、Recall、F1
8. 生成 risk_score 和 risk_band
9. 查看数据可视化、归因分析和规则化建议
10. 撰写并下载风险分析报告

## 核心模块

* `app/`：Streamlit UI 工作台
* `src/risk_control_agent/`：核心 Python 模块
* `scripts/`：本地流程入口和健康检查脚本
* `configs/`：指标、规则、字段映射、报告和建议配置
* `tests/`：单元测试
* `docs/knowledge_base/`：金融风控知识库
* `docs/product_design/`：产品定位、用户场景、工作流和 UI 设计
* `docs/technical_design/`：技术设计文档
* `docs/showcase/`：GitHub 展示材料
* `docs/interview/`：面试讲解稿、简历 bullet 和 Q&A
* `docs/release/`：发布前检查和上传说明
* `data/`：数据目录和治理模板，不提交大型原始数据
* `outputs/`：本地输出目录，生成的报告、日志和预警文件默认不提交
* `models/`：本地模型文件目录，训练产物默认不提交

## 风控知识库

项目包含一套基础金融风控知识库，用于支撑分析逻辑和报告表达：

* `00_knowledge_base_index.md`：知识库索引
* `01_risk_control_overview.md`：风控整体概念和 Agent 角色边界
* `02_credit_and_fraud_risk.md`：信用风险与反欺诈风险边界
* `03_risk_metrics_dictionary.md`：业务风险指标字典
* `04_model_monitoring_dictionary.md`：AUC、KS、PSI 等模型监控指标
* `05_data_quality_and_drift.md`：数据质量与漂移监控说明
* `06_risk_alert_rules.md`：Risk Alert Rules 与风险等级设计
* `07_root_cause_analysis_playbook.md`：Root Cause Analysis 分析路径
* `08_risk_report_standard.md`：风险报告标准
* `09_ops_advice_policy.md`：运维建议边界
* `10_agent_safety_boundary.md`：Agent 安全边界与 Human Confirmation 原则

## 项目阶段

当前阶段：Phase 10 - Agent Workflow Packaging and GitHub Showcase

已完成：

| 阶段 | 内容 | 状态 |
| --- | --- | --- |
| Phase 1 | Risk Control Knowledge Base Construction | 已完成 |
| Phase 2 | Public Dataset Research and Data Source Design | 已完成 |
| Phase 3 | Public Dataset Acquisition Plan and MVP Data Sample Construction | 已完成 |
| Phase 4 | Public Dataset Download Instructions and Small Sample Preparation | 已完成 |
| Phase 5 | MVP Data Ingestion and Monitoring Table Construction | 已完成 |
| Phase 6 | Risk Metric Calculation and Alert Rule Engine | 已完成 |
| Phase 7 | Root Cause Analysis and Segment Contribution Engine | 已完成 |
| Phase 8 | Risk Report Generation Framework | 已完成 |
| Phase 9 | Streamlit UI Dashboard MVP | 已完成 |
| Phase 10 | Agent Workflow Packaging and GitHub Showcase | 已完成 |

后续可以继续扩展：

* 更清晰的 UI 交互体验和视觉设计
* 更完整的 Model Monitoring 页面
* 时间外验证集、PSI、score distribution 和分群稳定性分析
* 更细的模型调参记录和模型治理记录
* 在严格安全边界下探索 LLM 作为报告解释助手或指标解读助手

LLM 如果接入，应当只用于解释、总结、问答和报告辅助，不能直接做审批、拒贷、调额、策略修改或模型上线决策。

## 数据与 GitHub 安全

仓库采用 public-dataset-first 的数据策略，但当前不内置大型官方数据文件。

默认不提交：

* `data/raw/*`
* `data/external/*`
* `data/interim/*`
* `data/processed/*`
* `data/user_uploads/*`
* `models/*.joblib`
* `outputs/logs/*.json`
* `outputs/alerts/*.json`
* `outputs/reports/*.md`
* `outputs/reports/*.json`

相关目录通过 `.gitkeep` 保留结构。

## 安全与治理原则

* 风险结论必须基于指标、规则或明确假设
* 报告必须区分事实、推测和建议
* 高风险建议必须标注需要 Human Confirmation
* 不处理真实个人金融数据
* 不执行真实信贷决策
* 不输出无证据的因果判断
* UI 只能触发白名单本地脚本，不能执行任意用户命令
* 模型输出只作为分析参考，不作为自动业务动作依据

## 免责声明

本项目为学习、作品集和风控分析流程展示项目，不使用真实个人金融数据，不进行真实信贷审批，不构成任何金融机构的实际风控建议。项目中的阈值、指标、规则和模型结果用于演示风控监控与分析逻辑，真实业务中需要结合历史样本、业务口径、风险偏好、模型治理流程和监管要求进行校准。
