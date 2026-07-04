# Synthetic Data Policy

## Purpose

Define when synthetic data may be used after the project's Phase 2 shift to a public-dataset-first strategy.

Synthetic data is no longer the primary data strategy.

The project prioritizes official or authoritative public datasets. Synthetic data is allowed only as a clearly labeled supplement when public datasets do not contain required internal monitoring fields or controlled demonstration scenarios.

## Policy Rules

1. Official or authoritative public datasets should be used first whenever possible.
2. Synthetic data is allowed only for missing internal strategy-rule fields.
3. Synthetic data is allowed only for fraud indicator placeholders.
4. Synthetic data is allowed only for demo-only abnormal scenarios.
5. Synthetic data is allowed for unit testing in later coding phases.
6. Synthetic data is allowed for fields that official public datasets do not provide.
7. No real personal financial data may be used.
8. No real customer identifiers may be used.
9. No real bank or platform private data may be used.
10. README, reports, and data dictionaries must disclose any synthetic fields.

## Labeling Requirements

All synthetic fields must be explicitly labeled.

Future synthetic files or fields should include clear documentation such as:

```text
This field is synthetic and created for educational demonstration only.
It is not sourced from official public data and does not contain real personal financial data.
```

## Key Principles

* Synthetic data must not be presented as official performance data.
* Future reports must state which findings are based on public data and which depend on synthetic supplements.
* No production or customer-identifiable data is allowed in this repository.
* Synthetic supplements should be excluded from MVP if they are not necessary for explaining the public-dataset workflow.
