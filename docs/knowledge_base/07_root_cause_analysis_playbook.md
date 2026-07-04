# Root Cause Analysis Playbook

## Purpose

Define a structured path for investigating risk changes in future Agent reports.

## Core Framework

```text
Risk Change =
  Volume Change
+ Population Mix Change
+ Segment Risk Change
+ Model Performance Change
+ Data Quality Change
+ Policy / Strategy Change
+ External Event Impact
```

中文补充：

```text
风险变化 =
  规模变化
+ 客群结构变化
+ 分群风险变化
+ 模型表现变化
+ 数据质量变化
+ 策略变化
+ 外部事件影响
```

## Analysis Path

1. Start from overall risk indicators.
2. Check volume and approval rate changes.
3. Decompose by channel, product, region, customer segment, and score band.
4. Check score distribution migration.
5. Check AUC, KS, Recall, and Precision changes.
6. Check PSI, missing rate, and feature drift.
7. Check strategy or policy changes.
8. Generate possible explanations and human-confirmation items.

## Contribution Logic

```text
segment_bad_increase = current_segment_bad_count - baseline_segment_bad_count

segment_contribution = segment_bad_increase / total_bad_increase
```

The denominator `total_bad_increase` is the increase in bad-count total across all included segments for the same comparison window.

## Key Principles

* The Agent must not claim causality without sufficient evidence.
* Root-cause analysis should distinguish facts, assumptions, and possible explanations.
* Segment contribution should be calculated only when the baseline and current windows are comparable.
* Data quality exceptions must be reviewed before business interpretation.

## v0.7.0 Root Cause Framework Notes

The current v0.7.0 implementation provides the first root cause analysis framework.

* Segment contribution is an investigation priority signal, not causal proof.
* Contribution analysis requires comparison between current period and baseline period.
* Contribution share is meaningful only when total increase is greater than 0.
* Missing segment data must not be forced into root cause conclusions.
* Root cause findings must enter a human confirmation workflow.
* The root cause module does not automatically execute strategy actions.
* Outputs are structured JSON for later report generation, not a full Markdown report.
