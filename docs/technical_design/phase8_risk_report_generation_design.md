# Phase 8 Risk Report Generation Design

## Phase 8 Goal

Implement the first deterministic Markdown risk report generation framework.

## What Code Was Added

* `src/risk_control_agent/report_sections.py`
* `src/risk_control_agent/recommendations.py`
* `src/risk_control_agent/report_generator.py`
* `scripts/generate_risk_report.py`
* Unit tests for report sections, recommendations, and report generation.

## What Code Does

* Reads structured alert summary and root cause summary inputs.
* Renders Markdown report sections.
* Builds investigation-oriented operations recommendations.
* Saves Markdown reports and report manifests when inputs exist.
* Skips gracefully when report inputs are missing.

## What Code Does Not Do

This phase implements deterministic Markdown report generation based on structured alert and root cause summaries. It does not implement LLM integration, UI, model training, automatic business actions, or real financial decisioning.

## Report Input Design

Report generation uses:

* `outputs/alerts/risk_alert_summary_mvp.json`
* `outputs/alerts/root_cause_summary_mvp.json`

At least one input must exist. Otherwise report generation is skipped.

## Report Section Design

The generated report separates:

* Facts
* Interpretations
* Recommendations
* Limitations

Missing sections are marked unavailable rather than fabricated.

## Recommendation Generation Design

Recommendations come from `configs/recommendation_rules.yaml` and structured alert or root cause inputs. Recommendations are investigation-oriented and do not execute actions.

## Human Confirmation Design

High-risk recommendations and alerts requiring human confirmation are explicitly marked. Final decisions require human review and approval.

## Handling Missing Input Data

If no alert or root cause summary exists, the script skips with status `skipped_no_report_inputs` and saves a run log. It does not generate a fake report.

## Safety Boundary

The report is for monitoring and analysis support only. It must not be treated as real financial advice or an automated credit decision.

## Limitations

* No LLM-generated narrative.
* No UI.
* No model training.
* No automatic business action.
* Report content depends on available structured inputs.

## Next Phase Recommendation

Phase 9: Streamlit UI Dashboard.

