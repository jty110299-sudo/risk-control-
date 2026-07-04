# Risk Report Standard

## Purpose

Define the expected structure and writing rules for future Risk Control Agent reports.

## Report Template

```markdown
# Risk Analysis Report - YYYY-MM-DD

## 1. Executive Summary

## 2. Overall Risk Level

## 3. Key Metric Changes

## 4. Triggered Alert Rules

## 5. Root Cause Analysis

## 6. Segment Contribution Analysis

## 7. Model Monitoring Findings

## 8. Data Quality and Drift Findings

## 9. Risk Interpretation

## 10. Operations Recommendations

## 11. Items Requiring Human Confirmation

## 12. Appendix: Metric Tables
```

## Writing Rules

1. Facts must be supported by metrics.
2. Assumptions must be labeled as assumptions.
3. Recommendations must be actionable.
4. High-risk recommendations must require human confirmation.
5. The report must not claim causality without evidence.
6. Data quality issues must be disclosed.
7. Risk level must cite triggered rules.
8. Every recommendation must map to a risk source.

## Key Principles

* Reports should be clear, auditable, and traceable.
* Every conclusion should have evidence or a labeled assumption.
* Recommendations should be written for human review and execution.

## v0.8.0 Report Generation Notes

The current v0.8.0 implementation provides the first deterministic Markdown report generation framework.

* Reports must be based on alert summary and root cause summary.
* If no input exists, the system must not generate a fabricated report.
* Reports must separate facts, interpretations, recommendations, and limitations.
* Root cause findings must be labeled as investigation leads.
* High-risk recommendations must require human confirmation.
* Reports do not execute any business action.
* Current report generation does not use LLMs.
