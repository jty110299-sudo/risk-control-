# Financial Risk Control Overview

## Purpose

Define the risk control context for Risk Control Agent and clarify the boundary of the first project phase.

## Financial Risk Control Goals

Financial risk control aims to identify, monitor, explain, and govern risk changes in lending or credit-related business processes. For this project, the emphasis is monitoring and analysis, not credit decision execution.

## Risk Types

| Risk type | Meaning | Example monitoring focus |
| --- | --- | --- |
| Credit risk | Risk that borrowers fail to meet repayment obligations. | Bad rate, overdue rate, first payment default rate. |
| Fraud risk | Risk caused by intentionally deceptive applications or behaviors. | Fraud rate, rule hit rate, intercept rate. |
| Model risk | Risk from model performance degradation, misuse, or weak governance. | AUC, KS, PSI, score distribution shift. |
| Data risk | Risk caused by incomplete, delayed, duplicated, or changed data. | Missing rate, schema change, data delay, drift. |

## Lending Lifecycle

| Stage | Monitoring focus |
| --- | --- |
| Pre-loan | Application volume, approval rate, rejection rate, rule hit rate, fraud indicators. |
| In-loan | Usage behavior, overdue signals, account performance, monitoring alerts. |
| Post-loan | Delinquency, bad rate, recovery-related indicators, portfolio quality. |

## Daily Tasks of a Risk Monitoring System

* Track key risk metrics over time.
* Compare current values with baselines.
* Detect abnormal changes.
* Break down risk by segment.
* Identify possible contributing factors.
* Document findings and recommendations.
* Escalate high-risk issues for human review.

## Role of Risk Control Agent

Risk Control Agent is a monitoring and analysis assistant, not an autonomous credit decision engine.

The Agent is planned to help analysts organize metric evidence, detect abnormal indicators, structure root-cause analysis, and draft reports.

## Project Exclusions

This project does not make real credit decisions, does not use real lending data, and does not connect to production systems.

