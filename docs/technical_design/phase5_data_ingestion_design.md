# Phase 5 Data Ingestion Design

## Phase 5 Goal

Phase 5 creates the data ingestion and monitoring table construction framework for Risk Control Agent.

The goal is to provide a reproducible entry point for future official public dataset samples, especially the Freddie Mac MVP candidate.

## What Code Was Added

* Python package structure under `src/risk_control_agent/`
* YAML configuration files under `configs/`
* Safe data loading utilities
* Schema helpers
* Validation helpers
* Basic data quality checks
* MVP monitoring table construction framework
* Run logging utility
* `scripts/build_monitoring_tables.py`
* Minimal unit tests

## What Code Does Not Do

This phase does not:

* Download official datasets
* Fabricate project data
* Train models
* Implement anomaly detection
* Implement alerting or risk level assignment
* Implement root cause analysis
* Generate risk reports
* Implement Streamlit UI
* Connect to databases
* Call LLM APIs

## Input Data Assumptions

The script expects official sample files to be placed under `data/samples/official/`.

If no official sample file exists, the script skips processing gracefully and creates a run log with status `skipped_no_input_data`.

## Freddie Mac Field Mapping Limitation

The Freddie Mac field mapping is a draft. Field names are placeholders or candidate mappings until verified against the official Freddie Mac user guide and file layout.

No data processing should proceed without field layout verification.

## Monitoring Table Construction Approach

The first supported construction function creates a period-level `daily_risk_metrics` style table from monthly performance data. For Freddie Mac MVP, the time grain may be monthly and represented by `monitoring_period`.

Candidate delinquency logic:

* Delinquent loan count: delinquency status greater than 0.
* Serious delinquent loan count: delinquency status greater than or equal to 3.

This logic must be verified against the official data dictionary before production-like use.

## Data Quality Checks

Phase 5 includes basic checks for:

* Row count
* Column count
* Missing rate
* Duplicate key count
* Required columns
* Empty DataFrames
* Numeric fields
* Date or period fields

## Run Log Design

Every processing run should create a local run log under `outputs/logs/`.

Run logs include:

* `run_name`
* `timestamp`
* `status`
* `messages`
* `output_path`
* `project_phase`

## Safety and GitHub Boundaries

Large raw data remains excluded from GitHub.

Generated monitoring tables should be written only to `data/processed/` in later runs. `data/processed/` is ignored by `.gitignore`.

Unit test fixtures are in-memory only and are not project data.

This phase creates the data ingestion and monitoring table construction framework, but does not complete full risk analysis, alerting, report generation, or UI implementation.

## Next Phase Recommendation

Phase 6: Risk Metric Calculation and Alert Rule Engine.

