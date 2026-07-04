# Phase 6 Metric Alert Engine Design

## Phase 6 Goal

Implement the first risk metric calculation utilities and rule-based alert engine for Risk Control Agent.

## What Code Was Added

* `src/risk_control_agent/metrics.py`
* `src/risk_control_agent/risk_levels.py`
* `src/risk_control_agent/alert_rules.py`
* `src/risk_control_agent/alert_summary.py`
* `scripts/run_alert_engine.py`
* Unit tests for metrics, alert rules, and alert summary.

## What Code Does

* Calculates safe rates and change metrics.
* Adds baseline comparison fields.
* Loads YAML-based alert rules.
* Evaluates active MVP alert rules.
* Produces structured alert summaries.
* Saves local run logs.
* Skips gracefully when no processed monitoring table exists.

## What Code Does Not Do

This phase implements metric calculation and rule-based alerting only. It does not implement root cause analysis, report generation, LLM integration, model training, or UI.

## Metric Calculation Design

The metric utilities include safe division, absolute change, relative change, period-over-period comparison, baseline average, and baseline comparison. Division by zero returns `numpy.nan`.

## Alert Rule Engine Design

Rules are configured in `configs/risk_alert_rules.yaml`. Only rules with `mvp_applicability: active_mvp` are evaluated. Future rules are present for planning but are not active.

## Risk Level Design

Risk levels use the standard order:

* Level 0
* Level 1
* Level 2
* Level 3
* Level 4

Level 4 is highest. Level 3 and Level 4 are treated as high risk and require human confirmation.

## Alert Summary Output Design

`outputs/alerts/risk_alert_summary_mvp.json` may contain:

* `project_phase`
* `run_timestamp`
* `overall_risk_level`
* `alert_count`
* `alert_count_by_level`
* `human_confirmation_required`
* `triggered_alerts`
* `warnings`
* `safety_note`

## Handling Missing Processed Data

If `data/processed/daily_risk_metrics_mvp.csv` does not exist, `scripts/run_alert_engine.py` skips processing with status `skipped_no_processed_data` and saves a run log.

## Safety Boundary

Alert rules must not execute business actions. Risk level output is a monitoring signal, not a final business decision. High-risk alerts require human confirmation.

## Limitations

* Thresholds are illustrative and must be calibrated.
* No root cause analysis is implemented.
* No Markdown risk report is generated.
* No UI or LLM integration is implemented.
* AUC, KS, PSI, and model monitoring metrics remain future work.

## Next Phase Recommendation

Phase 7: Root Cause Analysis and Segment Contribution Engine.

