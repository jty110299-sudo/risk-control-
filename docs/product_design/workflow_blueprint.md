# Workflow Blueprint

## Purpose

Define the planned future Agent workflow. This is a future blueprint, not a currently implemented capability.

## Planned Workflow

This is a future blueprint, not a currently implemented capability.

## Current Implementation Status

Implemented:

* Public data source strategy
* Data directory and metadata templates
* Data ingestion framework
* Monitoring table construction framework
* Metric calculation utilities
* Rule-based alert engine
* Root cause analysis framework
* Segment contribution analysis framework
* Markdown risk report generation framework
* Streamlit UI Dashboard MVP
* Local full pipeline runner
* Project health check
* GitHub showcase documentation

Not implemented:

* Official sample data actually downloaded and processed
* LLM integration
* Model training
* Production database connection
* Automated scheduling
* Authentication and role-based permission
* Production deployment
* Real credit decisioning

## Planned System Layers

| Layer | Responsibility |
| --- | --- |
| Data Source Layer | Select, document, and access official or authoritative public datasets according to source terms. |
| Data Processing Layer | Clean, validate, and transform public raw data into analysis-ready structures. |
| Metric Calculation Layer | Calculate monitoring metrics, baseline comparisons, and segment-level indicators. |
| Alert and Root Cause Analysis Layer | Detect triggered rules and identify contribution factors for risk changes. |
| Report Generation Layer | Generate risk analysis reports, recommendations, and human-confirmation items. |
| UI / Dashboard Layer | Display and support analyst interaction with metrics, alerts, root causes, model stability, data quality, reports, and logs. |
| Audit and Logging Layer | Save execution logs, warnings, output paths, and traceable analysis records. |

The UI / Dashboard Layer is responsible only for display and analyst interaction. It must not perform automatic business decisions.

### Data Layer Workflow

1. Step 0: Select MVP dataset.
2. Step 1: Verify source terms and documentation.
3. Step 2: Prepare data directory and `.gitignore`.
4. Step 3: Record dataset metadata.
5. Step 4: Download only approved small sample files or follow manual download instructions.
6. Step 5: Verify field layout.
7. Step 6: Prepare MVP monitoring table mapping.
8. Step 7: Build data ingestion module in later phase.
9. Step 8: Generate monitoring tables in later phase.
10. Step 9: Run risk analysis in later phase.
11. Step 10: Display results in the local Streamlit UI Dashboard MVP.

These are planned workflow steps. The current UI can display available local outputs, but it does not create missing data or perform production actions.

### Agent Analysis Workflow

1. Step 1: Read monitoring data.
2. Step 2: Validate data quality.
3. Step 3: Calculate key metrics.
4. Step 4: Detect abnormal changes.
5. Step 5: Analyze root causes.
6. Step 6: Check model and data stability.
7. Step 7: Assign risk level.
8. Step 8: Generate recommendations.
9. Step 9: Generate report.
10. Step 10: Save logs and outputs.

### UI Review Workflow

1. Select dataset or monitoring period.
2. Review overall risk level.
3. Inspect triggered alert rules.
4. Review root cause analysis.
5. Check model and data stability.
6. Open report preview.
7. Export report if needed.
8. Review items requiring human confirmation.

## Safety Gates

* If data quality is abnormal, avoid strong business conclusions before validation.
* If risk level is Level 3 or Level 4, add `Requires human confirmation`.
* If evidence is insufficient, label explanations as assumptions.
* If no implementation exists, do not claim runtime capability.
* If public dataset limitations affect a metric, disclose the limitation before analysis.
* The UI must not provide automatic approval, rejection, credit limit adjustment, channel closure, production policy modification, or model deployment actions.

## Key Principles

* The workflow must remain explainable, auditable, and traceable.
* The Agent must not bypass human review.
* Official or authoritative public datasets should be used first.
* Synthetic data may only supplement missing fields and must be explicitly labeled.
* The future UI should support review, explanation, and report access, not autonomous lending decisions.
