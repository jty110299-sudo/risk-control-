# Risk Metrics Dictionary

## Purpose

Define business risk monitoring metrics for later synthetic data design, calculation logic, alert rules, and reports.

## Metric Dictionary

| Metric name | Formula | Business meaning | Increase may indicate | Decrease may indicate | Common abnormal causes | Segment analysis |
| --- | --- | --- | --- | --- | --- | --- |
| `application_count` | Count of applications in the observation period. Denominator: not applicable. | Application volume. | Traffic growth, channel expansion, campaign impact. | Traffic decline, channel outage, demand decrease. | Channel mix change, data delay, duplicate records. | Yes, by channel, product, region, segment. |
| `approved_count` | Count of approved applications in the observation period. Denominator: not applicable. | Number of applications passing approval criteria. | Looser strategy, better population quality, volume growth. | Tighter strategy, worse population quality, system issue. | Policy change, score distribution shift, data issue. | Yes. |
| `rejected_count` | Count of rejected applications in the observation period. Denominator: not applicable. | Number of applications not approved. | Tighter strategy, worse applicants, rule changes. | Looser strategy, better applicants, missing rejection data. | Policy change, data mapping issue. | Yes. |
| `approval_rate` | `approved_count / application_count`; denominator is all applications in the observation period. | Share of applications approved. | Looser strategy or better applicant mix. | Tighter strategy or worse applicant mix. | Strategy change, channel shift, model score shift. | Yes. |
| `rejection_rate` | `rejected_count / application_count`; denominator is all applications in the observation period. | Share of applications rejected. | Tighter strategy or deteriorating population. | Looser strategy or improved population. | Rule change, channel shift, data issue. | Yes. |
| `manual_review_rate` | `manual_review_count / application_count`; denominator is all applications in the observation period. | Share routed to manual review. | More borderline or abnormal applications. | Reduced manual workload or routing issue. | Rule changes, score distribution shift, staffing policy. | Yes. |
| `overdue_rate` | `overdue_users / due_users`; denominator is users with payments due in the observation window. | Share of due users with overdue status. | Repayment stress or poorer risk mix. | Improved repayment performance or collection timing effect. | Population mix, macro stress, data delay. | Yes. |
| `first_payment_default_rate` | `first_payment_default_users / first_payment_due_users`; denominator is users whose first payment is due. | Early repayment risk indicator. | Early-stage credit deterioration. | Improved new-book quality. | Channel issue, onboarding policy change, fraud-related pressure. | Yes. |
| `bad_rate` | `bad_count / total_observed_users`; denominator is users with a completed performance observation window. | Portfolio or segment credit loss proxy. | Worse credit quality. | Better credit quality or immature observation window. | Vintage mix, channel risk, policy change. | Yes. |
| `fraud_rate` | `fraud_cases / application_count`; denominator is all applications in the observation period. | Confirmed or labeled fraud cases relative to applications. | Higher fraud pressure or labeling change. | Lower detected fraud or under-labeling. | Channel abuse, rule changes, delayed confirmation. | Yes. |
| `rule_hit_rate` | `rule_hit_count / application_count`; denominator is all applications in the observation period. | Share of applications hitting risk rules. | More risky traffic or rule expansion. | Less risky traffic or rule failure. | Strategy change, data missingness, channel shift. | Yes. |
| `intercept_rate` | `intercept_count / rule_hit_count`; denominator is applications that hit relevant rules. | Share of rule-hit cases stopped or blocked from the next stage in a synthetic monitoring design. | Tighter operational treatment. | Looser treatment or workflow issue. | Rule policy change, review process change. | Yes. |
| `false_positive_rate` | `false_positive_count / predicted_positive_count`; denominator is cases flagged positive by a rule or model. | Share of flagged cases later judged not risky. | Overly broad detection or drift. | Better precision or under-reviewing. | Label delay, threshold setting, segment shift. | Yes. |

## Key Principles

* Every rate must define its denominator.
* Metrics should be analyzed by segment when a change may be concentrated.
* A metric change alone is not proof of causality.
* Data quality must be checked before strong business conclusions.

