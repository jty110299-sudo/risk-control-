# HMDA Auxiliary Plan

## Purpose

Define how CFPB / FFIEC HMDA Data may support Risk Control Agent as an auxiliary dataset.

## Why HMDA Is Auxiliary, Not Primary

HMDA is focused on mortgage application and lending activity. It is useful for application volume, approval or denial monitoring, product, geography, and institution-level analysis.

HMDA is not a monthly loan performance dataset and should not be used as the only primary source for bad-rate, overdue-rate, delinquency, or credit performance monitoring.

## Suitable Use Cases

* Application volume monitoring.
* Approval / denial action monitoring.
* Product type analysis.
* Geography-level application patterns.
* Institution-level analysis.
* Application-stage population mix review.

## Metrics HMDA Can Support

* `application_count`
* `approval_rate`
* `denial_rate`
* `action_taken` distribution
* Geography-level application patterns
* Product and loan-purpose distribution
* Institution-level application and action summaries

## Metrics HMDA Cannot Support Well

* `bad_rate`
* `overdue_rate`
* Delinquency status
* Monthly loan performance
* Model monitoring
* Internal manual review rate
* Internal rule hit rate
* Confirmed fraud rate

## Future Application-Monitoring Module

HMDA could support a future application-monitoring module that tracks:

* Application volume changes.
* Approval and denial movement.
* Product or geography shifts.
* Lender or institution-level public patterns.
* Population mix changes at the application stage.

This module should be separate from post-origination credit performance monitoring.

## Privacy and Public-Use Notes

HMDA public data may be modified for privacy and public disclosure. The project must not attempt to re-identify individuals, must follow source terms, and must not present HMDA data as the author's own business data.

