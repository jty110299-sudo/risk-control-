# User Scenarios

## Purpose

Define future user scenarios for Risk Control Agent. These scenarios are design targets, not implemented features in Phase 1.

| Scenario | User question | Required input data | Expected Agent output | Human confirmation needed |
| --- | --- | --- | --- | --- |
| Daily credit risk monitoring | What changed in today's credit risk indicators? | Daily risk metrics, baseline metrics, data quality checks. | Summary of key changes, triggered rules, watch items. | Needed for Level 3 or Level 4 recommendations. |
| Bad rate increase investigation | Why did bad rate increase compared with baseline? | Bad-rate metrics, segment metrics, score distribution, model metrics. | Segment contribution analysis and possible explanations. | Yes, before operational action. |
| Channel risk abnormality analysis | Which channel contributed most to risk increase? | Channel-level application, approval, overdue, and bad metrics. | Channel contribution ranking and investigation suggestions. | Yes for high-risk channel actions. |
| Model performance degradation review | Did model performance degradation affect risk monitoring? | AUC, KS, precision, recall, score distribution, PSI. | Model monitoring findings and recommended review items. | Yes for model or policy actions. |
| Data quality and PSI abnormality review | Can current risk conclusions be trusted? | Missing rate, data delay, schema checks, PSI, CSI, sample size. | Data quality findings and limits on interpretation. | Yes if business conclusions depend on abnormal data. |

## Key Principles

* The Agent should answer with evidence, not unsupported conclusions.
* Reports should separate facts, assumptions, and recommendations.
* High-risk recommendations require human confirmation.

