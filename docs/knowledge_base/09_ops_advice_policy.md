# Operations Advice Policy

## Purpose

Define safe boundaries for future operations recommendations.

## Advice by Risk Source

| Risk source | Allowed recommendation type |
| --- | --- |
| Overall metric abnormality | Recommend manual review of key metric movements and affected segments. |
| Channel risk | Recommend human review of abnormal channel traffic, quality, and policy history. |
| Product risk | Recommend product-level risk review and sample validation. |
| Regional risk | Recommend regional decomposition and business-context confirmation. |
| Population mix change | Recommend reviewing customer mix and acquisition changes. |
| Model performance degradation | Recommend model monitoring review with risk, model, and data teams. |
| Data quality issue | Recommend data validation before business conclusions. |
| Fraud indicator increase | Recommend focused review of fraud indicators and confirmed labels. |
| Policy or strategy change | Recommend reviewing recent policy changes and approval history. |

## Advice by Risk Level

| Level | Recommendation |
| --- | --- |
| Level 0 | Continue normal monitoring. |
| Level 1 | Increase monitoring frequency. |
| Level 2 | Conduct manual investigation on abnormal segments. |
| Level 3 | Start focused risk review with risk, data, and business teams. Requires human confirmation. |
| Level 4 | Recommend human approval for emergency response. Requires human confirmation. |

## Prohibited Actions

The Agent must not perform or recommend direct execution of:

1. Automatically closing channels.
2. Automatically rejecting users.
3. Automatically lowering user credit limits.
4. Automatically changing production rules.
5. Automatically taking down models.

## Recommendation Examples

Allowed:

```text
Recommend human review on whether to temporarily tighten rules for the abnormal channel.
Requires human confirmation.
```

Not allowed:

```text
Automatically reject all users from this channel.
```

## Key Principles

* Recommendations must support investigation, escalation, and human review.
* The Agent must not bypass human approval.
* Every recommendation must map to a risk source.

## v0.8.0 Recommendation Generation Notes

The current v0.8.0 implementation supports configuration-based operations recommendations.

* Recommendations may only be investigation recommendations or human-confirmation recommendations.
* Recommendations must not suggest automatic rejection, automatic credit limit adjustment, automatic channel closure, or automatic production policy changes.
* Level 3 and Level 4 recommendations must require human confirmation.
* Recommendations should relate to triggered rules or root cause investigation leads.
* Recommendations are not final business decisions.
