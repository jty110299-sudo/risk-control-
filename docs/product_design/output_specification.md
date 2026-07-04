# Output Specification

## Purpose

Define planned and MVP output files and UI display outputs. The current project includes a local Streamlit UI Dashboard MVP that reads existing files and shows empty-state guidance when files are missing.

## Planned Outputs

| Output path | Purpose | Intended audience | Required fields | Safety notes |
| --- | --- | --- | --- | --- |
| `outputs/reports/risk_analysis_report_YYYYMMDD.md` | Human-readable risk analysis report. | Risk analysts, model monitoring analysts, risk operation teams. | Date, risk level, key metrics, triggered rules, root-cause analysis, recommendations, human-confirmation items. | Must disclose synthetic data and data quality limits. |
| `outputs/alerts/risk_alert_summary_YYYYMMDD.json` | Structured alert summary for review. | Analysts and future tooling. | Date, alert level, triggered rules, affected segments, metric changes, status. | Must not trigger production actions. |
| `outputs/logs/agent_run_log_YYYYMMDD.json` | Trace log for future Agent runs. | Developers and reviewers. | Run time, inputs, validation checks, calculation steps, output paths, warnings. | Must avoid real personal financial data. |

## MVP Alert Summary Output

Planned path:

```text
outputs/alerts/risk_alert_summary_mvp.json
```

Required fields:

| Field | Meaning |
| --- | --- |
| `project_phase` | Current project phase that generated the summary. |
| `run_timestamp` | Alert summary generation timestamp. |
| `overall_risk_level` | Highest risk level among triggered rules. |
| `alert_count` | Number of triggered alerts. |
| `alert_count_by_level` | Count of alerts by risk level. |
| `human_confirmation_required` | Whether any alert requires human confirmation. |
| `triggered_alerts` | List of triggered rule details. |
| `warnings` | Validation or missing-data warnings. |
| `safety_note` | Reminder that final decisions require human review and approval. |

## MVP Root Cause Summary Output

Planned path:

```text
outputs/alerts/root_cause_summary_mvp.json
```

Required fields:

| Field | Meaning |
| --- | --- |
| `project_phase` | Current project phase that generated the summary. |
| `run_timestamp` | Root cause summary generation timestamp. |
| `analysis_status` | Completion or skipped status. |
| `available_inputs` | Which prior outputs were available. |
| `top_contributors` | Top segment contribution records, if segment data is available. |
| `metric_change_findings` | Metric movement findings, if daily monitoring data is available. |
| `alert_linked_hints` | Investigation hints linked to triggered alert IDs. |
| `warnings` | Missing-data or validation warnings. |
| `human_confirmation_required` | Whether findings require human confirmation. |
| `safety_note` | Reminder that root cause findings are investigation leads, not causal proof. |

## MVP Markdown Risk Report Output

Planned path:

```text
outputs/reports/risk_analysis_report_mvp.md
```

Required sections:

1. Executive Summary
2. Overall Risk Level
3. Triggered Alert Rules
4. Key Metric Findings
5. Root Cause Findings
6. Segment Contribution Findings
7. Data Availability
8. Operations Recommendations
9. Items Requiring Human Confirmation
10. Limitations
11. Appendix
12. Footer Disclaimer

## MVP Report Manifest Output

Planned path:

```text
outputs/reports/risk_analysis_report_manifest_mvp.json
```

Required fields:

| Field | Meaning |
| --- | --- |
| `report_path` | Saved Markdown report path. |
| `status` | Report generation status. |
| `inputs_used` | Structured inputs used for report generation. |
| `warnings` | Missing-input or generation warnings. |
| `generated_at` | Manifest generation timestamp. |
| `project_phase` | Current project phase. |

## MVP Streamlit UI Display Inputs

The local Streamlit UI reads and displays:

1. `data/processed/daily_risk_metrics_mvp.csv`
2. `data/processed/segment_risk_metrics_mvp.csv`
3. `outputs/alerts/risk_alert_summary_mvp.json`
4. `outputs/alerts/root_cause_summary_mvp.json`
5. `outputs/reports/risk_analysis_report_mvp.md`
6. `outputs/reports/risk_analysis_report_manifest_mvp.json`
7. `outputs/logs/*.json`

If these files are missing, the UI displays empty-state guidance instead of fabricated results.

## Future UI Display Outputs

| UI output | Purpose | Notes |
| --- | --- | --- |
| Risk level summary | Show the overall risk status for the selected period. | Must cite triggered rules or evidence. |
| Triggered alert rules | Show which Risk Alert Rules were triggered. | Must not trigger production actions. |
| Key metric cards | Display core metrics such as `application_count`, `approval_rate`, `overdue_rate`, and `bad_rate`. | Must disclose unavailable or unsupported metrics. |
| Segment contribution table | Show top contributing segments for risk changes. | Contribution is not causal proof. |
| Model monitoring summary | Show AUC, KS, Precision, Recall, PSI, and related monitoring indicators when available. | Accuracy should not be the primary metric in imbalanced risk scenarios. |
| Data quality flags | Show missingness, drift, data delay, schema change, or validation warnings. | Data issues must limit strong business conclusions. |
| Report preview | Display the generated risk analysis report before export. | Report generation is a future capability. |
| Human confirmation items | Highlight recommendations requiring Human Confirmation. | Required for high-risk recommendations. |
| Agent run log summary | Show source, period, validation status, warnings, and output references. | Useful for audit and traceability. |

## Key Principles

* Future outputs must be saved under `outputs/`.
* High-risk recommendations must require human confirmation.
* Output files must not contain real personal financial data.
* Future UI outputs must not imply the project can make autonomous credit decisions.
