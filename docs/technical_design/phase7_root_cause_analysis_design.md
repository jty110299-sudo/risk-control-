# Phase 7 Root Cause Analysis Design

## Phase 7 Goal

Implement the first root cause analysis and segment contribution analysis framework for Risk Control Agent.

## What Code Was Added

* `src/risk_control_agent/contribution_analysis.py`
* `src/risk_control_agent/root_cause.py`
* `src/risk_control_agent/root_cause_summary.py`
* `scripts/run_root_cause_analysis.py`
* Unit tests for contribution analysis and root cause summary.

## What Code Does

* Calculates segment count increases.
* Calculates contribution share from positive segment increases.
* Ranks top contributing segments.
* Links triggered alerts to investigation hints.
* Builds structured root cause summaries.
* Skips gracefully when required inputs are missing.

## What Code Does Not Do

This phase implements root cause analysis and segment contribution analysis only. It does not implement full Markdown report generation, LLM integration, model training, automatic business actions, or UI.

## Segment Contribution Design

Segment contribution is calculated as:

```text
segment_increase = current_segment_count - baseline_segment_count
total_increase = sum of positive segment increases
contribution_share = segment_increase / total_increase
```

Contribution analysis identifies possible investigation priorities, not proven causality.

## Root Cause Engine Design

The root cause engine accepts daily monitoring data, segment monitoring data, and alert summary data when available. It produces metric-change findings, segment contribution findings, alert-linked hints, warnings, and a safety note.

## Alert-Linked Hint Design

Alert-linked hints cite triggered rule IDs and related metrics when available. These hints guide investigation and must not be interpreted as automatic business decisions.

## Input Dependency

Useful outputs depend on prior phases:

* `data/processed/daily_risk_metrics_mvp.csv`
* `data/processed/segment_risk_metrics_mvp.csv`
* `outputs/alerts/risk_alert_summary_mvp.json`

## Handling Missing Data

If no inputs exist, `scripts/run_root_cause_analysis.py` skips with status `skipped_no_input_data` and saves a run log.

If segment data is missing, contribution analysis is skipped and a warning is returned.

## Safety Boundary

Root cause findings are investigation leads, not causal proof. Final decisions require human review and approval.

The module does not recommend automatic credit decisions, automatic strategy changes, or individual fraud accusations.

## Limitations

* No causal inference.
* No full report generation.
* No UI integration.
* No LLM integration.
* No model training.
* No automatic strategy action.

## Next Phase Recommendation

Phase 8: Risk Report Generation.

