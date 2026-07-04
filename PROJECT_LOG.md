# Project Log

## 2026-07-04 - Phase 1 Knowledge Base Construction

### Goal

Build the financial risk control knowledge base, project documentation structure, and safety boundary before implementing any code.

### Actions

* Created the project documentation structure.
* Added risk control knowledge-base files.
* Added product design blueprints.
* Added future synthetic data design documents.
* Added output folders for future reports, alerts, and logs.
* Added Agent safety boundary and development rules for future work.
* Recorded verified reference sources in `SOURCES.md`.

### Created Directories

* `docs/knowledge_base/`
* `docs/product_design/`
* `docs/data_design/`
* `outputs/reports/`
* `outputs/alerts/`
* `outputs/logs/`
* `src/`

### Created Files

* `README.md`
* `PROJECT_LOG.md`
* `CHANGELOG.md`
* `SOURCES.md`
* `AGENT_DEVELOPMENT_RULES.md`
* Knowledge-base documents under `docs/knowledge_base/`
* Product design documents under `docs/product_design/`
* Data design documents under `docs/data_design/`
* Placeholder `.gitkeep` files under future output and source directories.

### Design Rationale

The Agent should be a monitoring and analysis assistant, not an autonomous credit decision engine. This phase defines terminology, metrics, report rules, analysis boundaries, and safety constraints so that later implementation can be traceable, auditable, and human-reviewed.

### Risk Control Boundary

The project is limited to synthetic, educational, and portfolio-oriented design work. It does not process real personal financial data, make real credit decisions, connect to production systems, or modify production risk policies.

All high-risk recommendations must be marked as requiring human confirmation. / 所有高风险建议均需要人工确认。

### Next Step

Move to Phase 2: Public Dataset Research and Data Source Design.

## 2026-07-04 - Phase 2 Public Dataset Research and Data Source Design

### Goal

Adjust the data strategy from fully synthetic data to a public-dataset-first approach:

```text
Public official datasets first, synthetic data only as clearly labeled supplements.
```

### Why the Data Strategy Was Adjusted

Fully synthetic data is useful for controlled demonstrations, but it is not ideal as the primary data foundation for a credit risk monitoring portfolio project. Official or authoritative public datasets can better support realistic field definitions, time windows, loan performance behavior, application outcomes, and data limitations.

Synthetic fields remain useful only when public datasets do not contain internal monitoring fields such as strategy rule hits, manual review results, or fraud strategy outcomes.

### Public Datasets Researched

* Fannie Mae Single-Family Loan Performance Data
* Freddie Mac Single-Family Loan-Level Dataset
* CFPB / FFIEC HMDA Data

### Added Documents

* `docs/data_design/public_dataset_strategy.md`
* `docs/data_design/public_dataset_candidates.md`
* `docs/data_design/dataset_field_mapping_plan.md`
* `docs/data_design/data_usage_and_github_policy.md`

### Updated Documents

* `README.md`
* `PROJECT_LOG.md`
* `CHANGELOG.md`
* `SOURCES.md`
* `docs/data_design/synthetic_data_policy.md`
* `docs/data_design/data_schema_blueprint.md`
* `docs/data_design/metric_calculation_plan.md`
* `docs/product_design/workflow_blueprint.md`

### Execution Boundary

This phase did not implement code, did not download large datasets, did not generate data files, did not train models, and did not perform Git operations.

### Next Step

Phase 3: Public Dataset Acquisition Plan and MVP Data Sample Construction.

Phase 3 should first define download, sampling, storage, privacy, license, and field-processing plans. It should not directly download full large datasets without a documented acquisition and storage plan.

## 2026-07-04 - v0.2.1 UI Dashboard Design Added

### Goal

Add product design requirements for a future analyst-facing UI / Dashboard.

### Why the Project Needs an Interactive UI

Risk Control Agent should be usable by risk analysts, not only executable as a backend script or command-line tool. A Dashboard can help analysts inspect risk levels, triggered alert rules, key metrics, root cause analysis, model stability, data quality, reports, and human-confirmation items in one review flow.

### Why Streamlit Is Recommended for the MVP

Streamlit is recommended for the first UI version because it fits Python data analysis projects, supports metric cards, charts, tables, and report previews with low implementation overhead, and is suitable for a GitHub portfolio project. React, Vue, and FastAPI may be considered later, but they are not the first priority for the MVP.

### Added Document

* `docs/product_design/ui_dashboard_design.md`

### Updated Documents

* `README.md`
* `docs/product_design/agent_positioning.md`
* `docs/product_design/workflow_blueprint.md`
* `docs/product_design/output_specification.md`
* `PROJECT_LOG.md`
* `CHANGELOG.md`

### Execution Boundary

This update only adds UI / Dashboard product design documentation. It does not implement UI code, Streamlit code, frontend code, Python business code, data generation, dataset downloads, model training, Agent workflow execution, or Git operations.

### UI Safety Boundary

The future UI must not provide automatic approval, automatic rejection, automatic credit limit adjustment, automatic production policy modification, automatic channel closure, model deployment actions, or individual fraud accusation features.

### Future Implementation Phase

UI implementation is planned for Phase 8: Interactive UI Design and Implementation.

## 2026-07-04 - Phase 3 Public Dataset Acquisition Plan and MVP Data Sample Construction

### Goal

Design the official public dataset acquisition plan, MVP sample construction strategy, field selection plan, sampling strategy, storage strategy, and GitHub demonstration strategy.

This phase does not download full raw datasets and does not generate final CSV data files.

### Why Full Raw Data Is Not Downloaded Directly

Full public mortgage datasets can be large, source-specific, and governed by official terms of use. The project should first document source terms, file versions, field layouts, sampling criteria, storage rules, and transformation logic before any data acquisition. This keeps the repository GitHub-safe, auditable, and easier to reproduce.

### Why Freddie Mac Is the MVP Primary Candidate

Freddie Mac Single-Family Loan-Level Dataset is recommended as the MVP primary candidate because it is an official public source, includes loan-level origination data and monthly performance data, and is suitable for demonstrating credit risk monitoring, delinquency status analysis, risk migration, and segment-level performance monitoring.

Future phases must confirm the applicable user guide, release notes, and file layout version before processing any data.

### Role of Fannie Mae and HMDA

Fannie Mae Single-Family Loan Performance Data remains an alternative primary or backup dataset because it includes acquisition and performance data suitable for credit performance monitoring.

CFPB / FFIEC HMDA remains an auxiliary dataset for application volume, approval and denial monitoring, product, geography, and institution-level analysis. HMDA is not the primary source for bad-rate, overdue-rate, or monthly loan performance analysis.

### Added Documents

* `docs/data_design/public_dataset_acquisition_plan.md`
* `docs/data_design/mvp_sample_construction_plan.md`
* `docs/data_design/freddie_mac_mvp_field_plan.md`
* `docs/data_design/fannie_mae_backup_plan.md`
* `docs/data_design/hmda_auxiliary_plan.md`
* `docs/data_design/data_directory_plan.md`

### Updated Documents

* `README.md`
* `PROJECT_LOG.md`
* `CHANGELOG.md`
* `SOURCES.md`
* `docs/data_design/public_dataset_strategy.md`
* `docs/data_design/public_dataset_candidates.md`
* `docs/data_design/dataset_field_mapping_plan.md`
* `docs/data_design/data_usage_and_github_policy.md`
* `docs/product_design/workflow_blueprint.md`
* `AGENT_DEVELOPMENT_RULES.md`

### Execution Boundary

This phase did not write code, did not generate data, did not train models, did not implement UI, did not download large raw datasets, and did not perform Git operations.

### Next Step

Phase 4: Public Dataset Download Instructions and Small Sample Preparation.

Phase 4 may consider downloading approved small samples or official sample files, but it should still not download or commit large full raw datasets.

## 2026-07-04 - Phase 4 Public Dataset Download Instructions and Small Sample Preparation

### Goal

Establish a standardized, safe, and reproducible data preparation workflow. This includes the data directory structure, download instructions, metadata templates, field layout verification checklist, GitHub storage rules, and small sample preparation documentation.

### Why Create Data Directories and Metadata Templates First

The project needs a clear separation between raw data, external reference files, interim files, processed outputs, small samples, and metadata before any data ingestion begins. Metadata templates and download logs ensure that every future file has source attribution, access dates, version information, storage decisions, and usage notes.

### Why Full Raw Data Is Not Downloaded Directly

Full Freddie Mac, Fannie Mae, and HMDA datasets may be large and governed by official source terms. The project should verify file layout, file size, license terms, source documentation, and MVP sampling strategy before downloading or processing any data. Large raw official datasets must not be committed to GitHub.

### Added Directories

* `data/`
* `data/raw/`
* `data/external/`
* `data/interim/`
* `data/processed/`
* `data/samples/`
* `data/samples/official/`
* `data/metadata/`

### Added Files

* `.gitignore`
* `data/README.md`
* `data/raw/.gitkeep`
* `data/external/.gitkeep`
* `data/interim/.gitkeep`
* `data/processed/.gitkeep`
* `data/samples/.gitkeep`
* `data/samples/official/.gitkeep`
* `data/metadata/.gitkeep`
* `data/metadata/dataset_metadata_template.md`
* `data/metadata/download_log_template.md`
* `data/metadata/field_layout_verification_checklist.md`
* `docs/data_design/freddie_mac_download_instructions.md`
* `docs/data_design/mvp_small_sample_preparation.md`
* `docs/data_design/data_preparation_quality_checklist.md`
* `docs/data_design/phase4_data_preparation_summary.md`

### Updated Documents

* `README.md`
* `PROJECT_LOG.md`
* `CHANGELOG.md`
* `SOURCES.md`
* `AGENT_DEVELOPMENT_RULES.md`
* `docs/data_design/public_dataset_acquisition_plan.md`
* `docs/data_design/mvp_sample_construction_plan.md`
* `docs/data_design/freddie_mac_mvp_field_plan.md`
* `docs/data_design/data_usage_and_github_policy.md`
* `docs/product_design/workflow_blueprint.md`

### Official Sample File Download Status

No official sample files were downloaded in this phase. The project records manual download instructions and verification requirements first.

### Execution Boundary

This phase did not write business code, did not train models, did not implement UI, did not generate final monitoring CSV files, did not download full raw datasets, and did not perform Git operations.

### Next Step

Phase 5: MVP Data Ingestion and Monitoring Table Construction.

Phase 5 may begin minimum data reading and monitoring table construction code only after metadata, download logs, and field layout verification are complete.

## 2026-07-04 - Phase 5 MVP Data Ingestion and Monitoring Table Construction

### Goal

Create the minimum Python data engineering framework for data reading, field mapping, field validation, basic data quality checks, and first-version monitoring table construction.

The goal is to create a reproducible processing entry point for future official public dataset samples.

### Added Code Directories and Files

* `src/risk_control_agent/`
* `src/risk_control_agent/__init__.py`
* `src/risk_control_agent/config.py`
* `src/risk_control_agent/io_utils.py`
* `src/risk_control_agent/schema.py`
* `src/risk_control_agent/validators.py`
* `src/risk_control_agent/quality_checks.py`
* `src/risk_control_agent/monitoring_tables.py`
* `src/risk_control_agent/run_logger.py`
* `scripts/build_monitoring_tables.py`

### Added Configuration Files

* `configs/data_paths.yaml`
* `configs/freddie_mac_field_mapping.yaml`
* `configs/monitoring_table_schemas.yaml`
* `requirements.txt`

### Added Tests

* `tests/test_validators.py`
* `tests/test_monitoring_tables.py`

### Added Technical Design

* `docs/technical_design/phase5_data_ingestion_design.md`

### Why This Phase Only Covers Ingestion and Monitoring Table Construction

Field layout verification and safe ingestion must come before risk metric expansion, alerting, root cause analysis, report generation, and UI. This phase avoids over-claiming functionality and keeps the project boundary focused on reproducible data preparation.

### Execution Boundary

This phase did not download large datasets, did not fabricate project data, did not train models, did not implement anomaly detection, did not implement report generation, did not implement UI, and did not perform Git operations.

### Next Step

Phase 6: Risk Metric Calculation and Alert Rule Engine.

## 2026-07-04 - Phase 6 Risk Metric Calculation and Alert Rule Engine

### Goal

Implement the first version of risk metric calculation utilities and a YAML-configured, rule-based alert engine.

### Added Code Files

* `src/risk_control_agent/metrics.py`
* `src/risk_control_agent/risk_levels.py`
* `src/risk_control_agent/alert_rules.py`
* `src/risk_control_agent/alert_summary.py`
* `scripts/run_alert_engine.py`

### Added Configuration Files

* `configs/metric_definitions.yaml`
* `configs/risk_alert_rules.yaml`
* `requirements-dev.txt`

### Added Tests

* `tests/test_metrics.py`
* `tests/test_alert_rules.py`
* `tests/test_alert_summary.py`

### Added Technical Design

* `docs/technical_design/phase6_metric_alert_engine_design.md`

### Why Rule Engine Comes Before Reports and UI

Alert rules create traceable, evidence-based risk signals. Report generation and UI should consume structured alert outputs later, rather than mixing rule logic with presentation logic. This phase therefore focuses only on metric calculation, rule evaluation, alert summary structure, and run logs.

### Execution Boundary

This phase did not download large datasets, did not fabricate project data, did not train models, did not implement root cause analysis, did not generate Markdown risk reports, did not implement UI, did not integrate LLMs, and did not perform Git operations.

### Next Step

Phase 7: Root Cause Analysis and Segment Contribution Engine.

## 2026-07-04 - Phase 7 Root Cause Analysis and Segment Contribution Engine

### Goal

Implement the first root cause analysis and segment contribution analysis framework.

### Added Code Files

* `src/risk_control_agent/contribution_analysis.py`
* `src/risk_control_agent/root_cause.py`
* `src/risk_control_agent/root_cause_summary.py`
* `scripts/run_root_cause_analysis.py`

### Added Configuration Files

* `configs/root_cause_analysis.yaml`

### Added Tests

* `tests/test_contribution_analysis.py`
* `tests/test_root_cause_summary.py`

### Added Technical Design

* `docs/technical_design/phase7_root_cause_analysis_design.md`

### Why Root Cause Engine Comes Before Full Reports and UI

Root cause findings and segment contribution outputs should be structured before they are turned into narrative reports or displayed in UI. This keeps the investigation logic auditable and prevents report text from overstating causal conclusions.

### Execution Boundary

This phase did not download large datasets, did not fabricate project data, did not train models, did not generate a full Markdown report, did not implement UI, did not integrate LLMs, and did not perform Git operations.

### Next Step

Phase 8: Risk Report Generation.

## 2026-07-04 - Phase 8 Risk Report Generation

### Goal

Implement the first deterministic Markdown risk report generation framework based on structured alert summaries and root cause summaries.

### Added Code Files

* `src/risk_control_agent/report_sections.py`
* `src/risk_control_agent/recommendations.py`
* `src/risk_control_agent/report_generator.py`
* `scripts/generate_risk_report.py`

### Added Configuration Files

* `configs/report_template.yaml`
* `configs/recommendation_rules.yaml`

### Added Tests

* `tests/test_report_sections.py`
* `tests/test_recommendations.py`
* `tests/test_report_generator.py`

### Added Technical Design

* `docs/technical_design/phase8_risk_report_generation_design.md`

### Why Deterministic Markdown Report Comes Before LLM

The first report framework should be deterministic and evidence-based so that report sections, safety wording, triggered rule references, and human confirmation items are auditable. LLM-generated narrative is intentionally excluded from this phase.

### Why Reports Must Separate Facts, Interpretations, and Recommendations

Risk reports can influence operational thinking. The report must distinguish metric facts, investigation interpretations, recommendations, and limitations so it does not overstate uncertain evidence or imply automatic business decisions.

### Execution Boundary

This phase did not download large datasets, did not fabricate project data, did not train models, did not implement UI, did not integrate LLMs, did not execute automatic business actions, and did not perform Git operations.

### Next Step

Phase 9: Streamlit UI Dashboard.
# 2026-07-04 - Phase 9: Streamlit UI Dashboard

## Phase Name

Phase 9 - Streamlit UI Dashboard

## Goal

Build the first local Streamlit dashboard MVP for Risk Control Agent, named Risk Control Agent Console / 智能风控分析工作台.

The UI is intended to display existing project outputs, show pipeline status, provide empty-state guidance, preview Markdown reports, expose run logs, and trigger already implemented local scripts.

## Added UI Files

* `app/streamlit_app.py`
* `app/ui_data_loader.py`
* `app/ui_components.py`
* `app/ui_actions.py`
* `app/README.md`

## Added Technical Design

* `docs/technical_design/phase9_streamlit_ui_dashboard_design.md`

## Why Streamlit

Streamlit is used because the project is a Python-first risk analytics portfolio project. It supports fast local dashboards, metric cards, tables, JSON viewers, Markdown previews, and buttons for local workflows without requiring a separate frontend stack.

## Why Chinese-First UI

The project is designed for GitHub 展示 and Chinese risk-control internship interview scenarios. Chinese-first navigation and prompts make the dashboard easier to explain to Chinese-speaking reviewers while retaining professional English terms such as Alert Summary, Root Cause Analysis, Segment Contribution, Model Monitoring, Data Stability, and Human Confirmation.

## Why UI Is Display and Trigger Only

The UI is not a business decision layer. It only displays existing outputs and triggers whitelisted local scripts. It does not automatically reject loans, adjust credit limits, close channels, modify policies, deploy models, or make real credit decisions.

## Boundaries

This phase did not download large datasets, did not generate fabricated data, did not train models, did not connect to LLM APIs, did not connect to production databases, and did not execute Git operations.

## Next Step

Phase 10: Agent Workflow Packaging and GitHub Showcase.
# 2026-07-04 - Phase 10: Agent Workflow Packaging and GitHub Showcase

## Phase Name

Phase 10 - Agent Workflow Packaging and GitHub Showcase

## Goal

Package Risk Control Agent as a GitHub-ready and interview-ready portfolio project. This phase focuses on local workflow entry points, showcase documents, architecture explanation, interview materials, release checklists, and safety review.

## Added Scripts

* `scripts/run_full_pipeline.py`
* `scripts/project_health_check.py`

## Added Showcase Documents

* `docs/showcase/project_showcase_overview.md`
* `docs/showcase/demo_walkthrough.md`
* `docs/showcase/github_repository_description.md`

## Added Architecture Documents

* `docs/architecture/system_architecture.md`
* `docs/architecture/workflow_mermaid_diagram.md`
* `docs/technical_design/phase10_workflow_packaging_design.md`

## Added Interview Materials

* `docs/interview/interview_talk_track.md`
* `docs/interview/resume_bullets.md`
* `docs/interview/qa_bank.md`

## Added Release Documents

* `docs/release/github_upload_guide.md`
* `docs/release/pre_release_checklist.md`
* `docs/release/data_safety_checklist.md`
* `PROJECT_SUMMARY.md`

## Why Packaging Instead of More Complex Features

After Phase 1-9, the project already has a local MVP chain. Phase 10 prioritizes reproducibility, explainability, GitHub presentation, interview readiness, and release safety instead of adding LLM integration, model training, database connection, or production deployment too early.

## Boundaries

This phase did not download large datasets, did not generate fabricated data, did not train models, did not connect to LLM APIs, did not execute Git operations, and did not perform automatic business actions.

## Next Suggestions

1. Manually install dependencies and run full tests.
2. Prepare a small Freddie Mac sample according to official instructions.
3. Run the full pipeline to generate real derived outputs.
4. Start Streamlit UI and capture screenshots.
5. Manually review release checklists before uploading to GitHub.
# 2026-07-04 - Release Hygiene Check

## Goal

Perform final GitHub upload hygiene checks before manual release.

## Checks Performed

* Scanned README, PROJECT_SUMMARY, PROJECT_LOG, and docs for local absolute paths and local username references.
* Reviewed `outputs/logs/`, `outputs/alerts/`, and `outputs/reports/`.
* Updated `.gitignore` to ignore local output JSON, Markdown reports, and logs while preserving `.gitkeep`.
* Confirmed `data/raw/`, `data/external/`, `data/interim/`, `data/processed/`, and `data/samples/official/` do not contain data files.
* Confirmed README still describes the project as a local MVP / portfolio project, not a production system.

## Boundaries

No Git commands were executed. No data was downloaded. No synthetic data was generated. No model was trained. No LLM integration was added. No real financial business action was performed.
# 2026-07-04 - v1.0.1 UI Design System and Dashboard Redesign

## Why Redesign Was Needed

The Phase 9 Streamlit UI was functional but still looked close to a default Streamlit page. It lacked a unified design system, strong visual hierarchy, and professional financial risk workstation feel.

## Why Add DESIGN.md

`DESIGN.md` was added as a design-system guide for future UI changes. It defines visual theme, color roles, typography, layout principles, component styling, risk-level rules, Do / Don't guidance, responsive behavior, and Codex UI modification rules.

## Why Dark Financial Risk Workstation Style

The dark workstation style better matches the product positioning: professional, trustworthy, risk-aware, auditable, data-dense but readable, and human-in-the-loop. It also makes risk levels, run logs, and Human Confirmation states easier to scan.

## UI Files Modified

* `app/streamlit_app.py`
* `app/ui_components.py`
* `app/ui_data_loader.py`

## Design System Files Added

* `DESIGN.md`
* `app/ui_theme.py`

## Boundaries

This phase did not download data, did not generate fabricated data, did not integrate LLM APIs, did not train models, did not execute Git operations, and did not add automatic business actions.

## Next Step

Manually start Streamlit, review the redesigned UI, capture screenshots, and then decide whether to upload the project to GitHub.

## Usability Follow-up

After manual review feedback, the UI was updated with a clearer first-page usage guide and an in-session CSV upload area for AUC / KS calculation. The uploaded CSV is read only within the local Streamlit session and is not written to the project directory. This improves usability without changing the project into a production data platform, model training system, or automated decision system.
# 2026-07-04 - v2.0.0 Product-grade Risk Control Agent Workbench

## Why Refactor the UI

The previous UI could run, but it behaved more like a project status display than a real risk analyst workbench. Users could not clearly understand where to upload data, train a model, generate score, review risk bands, inspect attribution, or write a report.

## Why Add Data Upload and Model Training

To make the product useful, the workbench now supports user CSV upload, field profiling, target selection, and supervised binary risk model training when a valid target label exists. If no target exists, the UI clearly states that supervised model training is not available.

## XGBoost and Tuning Follow-up

The model training workflow now supports XGBoost in addition to Logistic Regression, Random Forest, and Gradient Boosting. A lightweight GridSearchCV tuning option was added for model comparison and parameter search using AUC as the optimization metric. Tuning remains an analysis workflow, not an automated production model deployment process.

## Why Add Score Construction

The workbench now generates `predicted_probability`, `risk_score`, `risk_band`, and `risk_rank`. The score is an analytical signal for risk monitoring, not a credit decision.

## Why Rebuild Attribution Analysis

Attribution was redesigned into model-level, record-level, and segment-level analysis. Outputs are explicitly framed as investigation leads, not causal proof.

## Why Remove Project Status Clutter

The main UI no longer focuses on Phase completion, docs, CHANGELOG, or GitHub showcase materials. These remain in repository docs, while the app focuses on user tasks.

## Why Apple-like Minimal Dashboard

The new direction uses a light, minimal, content-first product style with clear cards, whitespace, concise copy, and task-oriented pages.

## Boundaries

This phase did not download large datasets, did not fabricate target or score, did not connect to LLM APIs, did not execute real business actions, and did not execute Git operations.
