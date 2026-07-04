# Data Preparation Quality Checklist

## Purpose

Define quality checks that must be completed before data is used for metric calculation, alerting, report generation, or UI display.

## Checklist

| Area | Check | Status | Notes |
| --- | --- | --- | --- |
| Source verification | Confirm official source link and source owner. | Not started |  |
| File integrity check | Confirm file opens and is not corrupted. | Not started |  |
| File size check | Confirm file size is suitable for local use and GitHub policy. | Not started |  |
| Layout verification | Confirm file layout matches official documentation. | Not started |  |
| Row count check | Record row count if known. | Not started |  |
| Column count check | Record column count if known. | Not started |  |
| Missing value pattern check | Identify missing value encodings and high-missing fields. | Not started |  |
| Date field validation | Confirm reporting and origination dates are parseable and consistent. | Not started |  |
| Duplicate loan ID check | Identify duplicate or repeated records based on expected grain. | Not started |  |
| Performance period continuity check | Confirm monthly performance periods behave as expected. | Not started |  |
| Delinquency status value check | Confirm delinquency or performance status values match documentation. | Not started |  |
| Segment field availability check | Confirm candidate segment fields are present. | Not started |  |
| Mapping completeness check | Confirm required Agent monitoring fields are mapped or excluded. | Not started |  |
| Privacy and attribution check | Confirm no re-identification attempt and source attribution is preserved. | Not started |  |
| GitHub safety check | Confirm raw large files are ignored and no restricted files are committed. | Not started |  |

## Gate

Data preparation must happen before metric calculation, alerting, report generation, or UI implementation.

