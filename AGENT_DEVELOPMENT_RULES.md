# Agent Development Rules

## Purpose

This document defines mandatory rules for future Codex or Agent development work in this repository.

## Rules

1. Do not implement production credit decisioning.
2. Do not describe the Agent as an autonomous lending decision system.
3. Do not generate conclusions without metric evidence or rule evidence.
4. Always separate facts, assumptions, and recommendations.
5. Always mark high-risk recommendations as requiring human confirmation.
6. Always save future reports and logs under `outputs/`.
7. Always update `PROJECT_LOG.md` after meaningful changes.
8. Always update `README.md` when scope, structure, or usage changes.
9. All sample data must be labeled as synthetic data.
10. Do not use real personal financial data.
11. Do not create code in Phase 1 unless explicitly instructed.
12. Do not initialize Git or make commits unless explicitly instructed.
13. Do not overwrite existing files without checking them first.
14. Do not claim that a feature is implemented unless code and usage instructions exist.
15. All risk thresholds in this project are illustrative and must be calibrated before real-world use.
16. Do not commit large raw official datasets to GitHub.
17. Do not use restricted datasets without checking usage terms.
18. Do not remove source attribution from derived files.
19. Do not mix public data and synthetic supplements without labeling.
20. Do not claim public datasets represent real internal business data.
21. Do not proceed with data processing until field mapping is documented.
22. Do not process data before source metadata is recorded.
23. Do not process data before field layout is verified.
24. Do not commit large raw datasets to GitHub.
25. Do not proceed with MVP ingestion until download logs and metadata templates are prepared.
26. Any downloaded sample file must be traceable to official source documentation.
27. Any derived monitoring table must document source data and transformation logic.
28. Do not hard-code local absolute paths.
29. Do not fabricate project data when official sample files are missing.
30. Data ingestion scripts must fail gracefully or skip with clear logs when input data is missing.
31. All generated outputs must go to ignored output directories unless explicitly approved.
32. Every processing script should create a run log.
33. Unit test fixtures are allowed only as in-memory test data and must not be saved as project data.
34. Do not implement alerting, report generation, UI, or LLM integration before the planned phases.
35. Alert rules must be configurable and traceable.
36. Alert rules must not execute business actions.
37. Alert summaries must include triggered rule IDs.
38. High-risk alerts must require human confirmation.
39. Missing data must not be replaced with fabricated values.
40. Rules marked `future_not_active` must not run in MVP.
41. Risk level output must not be described as a final business decision.
42. Alerting must precede report generation and UI integration.
43. Segment contribution must not be described as causal proof.
44. Root cause findings must be labeled as investigation leads.
45. Root cause analysis must cite input metrics or triggered alert IDs when available.
46. Missing data must not be replaced with fabricated values.
47. Root cause outputs must not recommend automatic credit decisions.
48. High-risk root cause findings must require human confirmation.
49. Full report generation must remain in Phase 8.
50. UI integration must remain in Phase 9.
51. Reports must not fabricate missing metrics or findings.
52. Reports must separate facts, interpretations, recommendations, and limitations.
53. Reports must cite triggered rule IDs when available.
54. Reports must label root cause findings as investigation leads.
55. Reports must include human confirmation items.
56. Reports must not recommend automatic credit decisions.
57. Report generation must not depend on LLM output in MVP.
58. UI integration must remain in Phase 9.

## Human Confirmation Rule

High-risk recommendations must include both labels:

* Requires human confirmation.
* 需要人工确认。

## Evidence Rule

Every risk conclusion must be traceable to at least one of the following:

* A metric value or metric change.
* A triggered rule.
* A documented data quality issue.
* A clearly labeled assumption.

## Phase 9 UI Development Rules

59. UI must not fabricate missing data.
60. UI must not execute arbitrary user commands.
61. UI may only trigger whitelisted local scripts.
62. UI must not execute Git commands.
63. UI must not download official datasets.
64. UI must not perform automatic business decisions.
65. UI must display human confirmation boundaries.
66. UI must use Chinese-first labels except professional terms.
67. UI must handle missing files gracefully.
68. UI must clearly state that it is a local MVP dashboard.

## Phase 10 Release and Showcase Rules

69. Do not claim production readiness.
70. Do not claim real financial institution deployment.
71. Do not commit large raw datasets.
72. Do not commit real personal financial data.
73. Do not commit fabricated risk results as real results.
74. Do not run Git commands automatically.
75. README must reflect actual implemented capabilities.
76. GitHub showcase materials must preserve safety boundaries.
77. Interview materials must not exaggerate project scope.
78. Release checklist must be reviewed manually before upload.

## UI Design System Rules

79. Future UI changes must follow `DESIGN.md`.
80. Do not add visual patterns outside the design system without updating `DESIGN.md`.
81. UI must remain Chinese-first except professional terms.
82. UI must not fabricate missing data for visual appeal.
83. UI must not add business-action buttons.
84. UI must preserve human confirmation boundary.

## v2.0 Product Workbench Rules

85. UI pages must each serve a clear user function.
86. Do not expose development phase status as primary UI content.
87. Do not fabricate score, target, or model result.
88. Supervised model training requires a valid target label.
89. If no target and no score exist, only exploratory analysis is allowed.
90. Risk score is an analytical signal, not a credit decision.
91. Attribution outputs are investigation leads, not causality.
92. Smart recommendations must not execute business actions.
93. UI must remain Chinese-first and Apple-like minimal.
94. All uploaded user data must be ignored by Git.
