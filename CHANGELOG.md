# Changelog

## v2.0.1 - Positioning Clarification

### Updated

* Clarified that the project supports local MVP-level supervised model training, AUC / KS evaluation, lightweight tuning, and risk scoring on user-uploaded CSV files.
* Clarified that the project does not include production-grade model training, production model deployment, LLM integration, real credit approval, or automatic business decisions.
* Updated README, project summary, and GitHub showcase wording to avoid understating implemented local modeling capabilities.

## v2.0.0 - Product-grade Risk Control Agent Workbench

### Added

* Redesigned Streamlit UI into a functional risk workbench.
* Added data upload and profiling workflow.
* Added supervised risk model training module.
* Added XGBoost as an optional risk model type.
* Added lightweight GridSearchCV tuning with AUC as the optimization metric.
* Added `risk_score` and `risk_band` generation.
* Added interactive data visualization.
* Rebuilt attribution analysis with global, record-level, and segment-level explanations.
* Added rule-based smart recommendations.
* Added interactive report writing workflow.
* Added Apple-like minimal UI design system.
* Added user upload, model, scoring, visualization, attribution, recommendation, and interactive report modules.
* Added unit tests for v2.0 workbench modules.

### Updated

* Removed unnecessary project-status-focused UI elements from the main workbench.
* Preserved no-LLM, no-auto-decision, and human-confirmation boundaries.

## v1.0.1 - UI Design System and Dashboard Redesign

### Added

* Added root `DESIGN.md` design system.
* Added Streamlit UI theme module.
* Added unified cards, badges, empty states, report viewer, run log table, and safety banner styling.

### Updated

* Redesigned dashboard with professional risk workstation style.
* Improved Chinese-first navigation and page content.
* Added a first-page usage guide so users understand the workflow order.
* Added local in-session AUC / KS calculation for uploaded, desensitized CSV files.
* Improved risk level and human confirmation visual display.
* Preserved no-fabrication and no-business-action boundaries.
* Added output log, alert, and report ignore rules for GitHub release hygiene.
* Confirmed local MVP and portfolio project positioning remains accurate.
* Confirmed Git upload commands are documented only for manual user execution.

### Cleaned

* Removed local run logs from `outputs/logs/` while preserving `.gitkeep`.
* Confirmed `outputs/alerts/` and `outputs/reports/` contain no generated local result files.

## v1.0.0 - Workflow Packaging and GitHub Showcase

### Added

* Added full local pipeline runner.
* Added project health check script.
* Added GitHub showcase documents.
* Added architecture documentation and Mermaid diagrams.
* Added interview talk tracks.
* Added resume bullets.
* Added interview Q&A bank.
* Added GitHub upload guide.
* Added pre-release checklist.
* Added data safety checklist.
* Added final project summary.

### Updated

* Updated README, project log, and development rules.
* Clarified that production deployment, LLM integration, model training, and real credit decisioning are not implemented.

## v0.9.0 - Streamlit UI Dashboard MVP

### Added

* Added local Streamlit dashboard MVP.
* Added Chinese-first UI navigation and page content.
* Added UI data loading utilities.
* Added reusable UI components.
* Added safe script action wrappers.
* Added pages for risk overview, data governance, alerts, root cause analysis, model/data stability, report center, run logs, and project overview.
* Added UI empty-state handling.
* Added UI safety boundary messaging.

### Updated

* Updated README, project log, workflow blueprint, output specification, and UI design documentation.
* Clarified that production deployment, LLM integration, model training, and real credit decisioning are not implemented.

## v0.8.0 - Risk Report Generation Framework

### Added

* Added deterministic Markdown report generation framework.
* Added report template configuration.
* Added recommendation rules configuration.
* Added report section rendering utilities.
* Added operations recommendation utilities.
* Added report generator module.
* Added `generate_risk_report` script.
* Added unit tests for report sections, recommendations, and report generation.
* Added Phase 8 technical design document.

### Updated

* Updated README, project log, workflow blueprint, output specification, report standard, and ops advice policy.
* Clarified that LLM integration, UI, model training, and automatic business actions are not implemented.

## v0.7.0 - Root Cause Analysis and Segment Contribution Engine

### Added

* Added segment contribution analysis utilities.
* Added root cause analysis engine.
* Added root cause summary generation.
* Added YAML-based root cause configuration.
* Added `run_root_cause_analysis` script.
* Added unit tests for contribution analysis and root cause summary.
* Added Phase 7 technical design document.

### Updated

* Updated README, project log, workflow blueprint, output specification, and root cause playbook.
* Clarified that contribution findings are investigation leads, not causal proof.
* Clarified that report generation, LLM integration, and UI are not implemented yet.

## v0.6.0 - Risk Metric Calculation and Alert Rule Engine

### Added

* Added metric calculation utilities.
* Added risk level utilities.
* Added YAML-based alert rule configuration.
* Added rule evaluation engine.
* Added alert summary generation.
* Added `run_alert_engine` script.
* Added development test requirements.
* Added unit tests for metrics, alert rules, and alert summaries.

### Updated

* Updated README, project log, knowledge base, and technical design documentation.
* Clarified that root cause analysis, report generation, LLM integration, and UI are not implemented yet.

## v0.5.0 - MVP Data Ingestion Framework

### Added

* Added Python package structure.
* Added YAML configuration files.
* Added safe data loading utilities.
* Added schema and validation utilities.
* Added basic data quality checks.
* Added MVP monitoring table construction framework.
* Added run logging utility.
* Added `build_monitoring_tables` script.
* Added minimal unit tests.

### Updated

* Updated README, project log, and technical design documentation.
* Clarified that no full raw data or final risk reports are included.

## v0.4.0 - Data Preparation Structure and Download Instructions

### Added

* Added data directory structure.
* Added GitHub-safe data storage rules.
* Added dataset metadata template.
* Added download log template.
* Added field layout verification checklist.
* Added Freddie Mac download instructions.
* Added MVP small sample preparation plan.
* Added data preparation quality checklist.

### Updated

* Updated README, project log, sources, and data governance documents.
* Clarified that no full raw datasets are committed to GitHub.

## v0.3.0 - Public Dataset Acquisition and MVP Sample Plan

### Added

* Added public dataset acquisition plan.
* Added MVP sample construction plan.
* Added Freddie Mac MVP field plan.
* Added Fannie Mae backup plan.
* Added HMDA auxiliary dataset plan.
* Added data directory plan.

### Updated

* Updated README, project log, sources, and data design documents.
* Clarified that no large raw datasets are committed to GitHub.

## v0.2.1 - UI Dashboard Design Added

### Added

* Added UI dashboard design document.
* Added Streamlit as recommended MVP UI technology.
* Clarified UI safety boundaries.

### Updated

* Updated roadmap to include Phase 8 UI implementation.
* Updated product positioning and workflow blueprint.

## v0.2.0 - Public Dataset Strategy Design

### Added

* Replaced fully synthetic data strategy with public-dataset-first strategy.
* Added public dataset strategy document.
* Added public dataset candidates comparison.
* Added dataset field mapping plan.
* Added data usage and GitHub storage policy.

### Updated

* Updated README, project log, sources, and data design documents.

## v0.1.0 - Knowledge Base Initialization

### Added

* Initialized project documentation structure.
* Added financial risk control knowledge base.
* Added risk metrics dictionary.
* Added model monitoring dictionary.
* Added data quality and drift monitoring guidance.
* Added alert rule design.
* Added root cause analysis playbook.
* Added risk report standard.
* Added operations advice policy.
* Added Agent safety boundary.
* Added project development rules.
* Added product design and future data design blueprints.
