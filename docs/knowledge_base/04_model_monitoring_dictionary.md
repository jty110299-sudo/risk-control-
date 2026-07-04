# Model Monitoring Dictionary

## Purpose

Define model monitoring metrics and how Risk Control Agent should mention them in future reports.

## Important Principle

Accuracy is not a primary metric in highly imbalanced credit risk scenarios.

Reason: in credit risk scenarios where bad samples are a small share of the population, a model that predicts nearly all users as low risk may still show high accuracy, but it may provide little practical value for identifying risky users.

## Metric Dictionary

| Metric | Meaning | Technical interpretation | Risk control interpretation | Abnormal signal | Investigation direction | Report wording guidance |
| --- | --- | --- | --- | --- | --- | --- |
| AUC | Ranking ability across thresholds. | Probability that a random bad case ranks riskier than a random good case. | Overall model discrimination. | Drop from baseline. | Check data drift, label quality, segment performance. | State the change and baseline; avoid causality claims. |
| KS | Maximum separation between good and bad cumulative distributions. | Measures score separation at the strongest threshold. | Practical separation strength for risk ranking. | Drop from baseline. | Check score bands, segment KS, recent population mix. | Cite baseline and current value. |
| Precision | Share of predicted positive cases that are actual positives. | `true_positive / predicted_positive`. | Quality of flagged risky cases. | Significant decline. | Check threshold, label delay, segment shift. | Explain possible operational review burden. |
| Recall | Share of actual positives captured. | `true_positive / actual_positive`. | Ability to capture risky cases. | Significant decline. | Check threshold, drift, new risk patterns. | Mention missed-risk possibility as an assumption if labels are incomplete. |
| F1 | Harmonic mean of precision and recall. | Balances precision and recall. | Useful when both capture and review quality matter. | Drop from baseline. | Review threshold and class balance. | Use as supporting metric, not the only conclusion. |
| Lift | Risk concentration in selected score bands. | Event rate in selected group divided by average event rate. | Whether high-risk bands concentrate bad outcomes. | Lower lift in high-risk band. | Check score calibration and population shift. | Report by score band. |
| PSI | Population Stability Index. | Measures distribution shift between current and baseline populations. | Indicates score or feature population drift. | `PSI >= 0.25` in this demo rule set. | Check channel, product, region, and acquisition changes. | State it as drift evidence, not outcome evidence. |
| CSI | Characteristic Stability Index. | Feature-level distribution shift measure. | Helps locate variables driving population change. | High or rising CSI. | Review feature definition, data pipeline, segment mix. | Connect to possible feature drift. |
| `score_distribution` | Distribution of model scores. | Counts or shares by score band. | Shows risk population migration. | Shift toward riskier bands or unexpected gaps. | Check channel mix, scoring pipeline, input data. | Include score-band table. |
| `feature_missing_rate` | Missing share for a feature. | Missing records divided by expected records. | Data completeness risk. | Sudden increase or segment concentration. | Check upstream data feed and schema changes. | Disclose before conclusions. |
| `feature_mean_shift` | Mean movement of a numeric feature. | Current mean versus baseline mean. | Possible drift or definition change. | Large or persistent shift. | Check data source, business mix, outliers. | Label as data or population signal. |
| `segment_model_performance` | Model metrics by segment. | AUC, KS, recall, precision by segment. | Detects uneven model degradation. | One segment degrades materially. | Check sample size, segment drift, label quality. | Avoid broad portfolio conclusions from small samples. |

## Key Principles

* Model monitoring findings should be connected to data quality and segment analysis.
* The Agent should separate performance facts, possible explanations, and recommendations.
* High-risk model recommendations require human confirmation.

