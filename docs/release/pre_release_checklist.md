# Pre-Release Checklist

## Documentation Checklist

* [ ] README reflects Phase 10 / v1.0.0 status.
* [ ] PROJECT_SUMMARY.md is complete.
* [ ] SOURCES.md is present.
* [ ] PROJECT_LOG.md includes Phase 10.
* [ ] CHANGELOG.md includes v1.0.0.

## Code Checklist

* [ ] `scripts/run_full_pipeline.py` exists.
* [ ] `scripts/project_health_check.py` exists.
* [ ] `app/streamlit_app.py` exists.
* [ ] Core modules under `src/risk_control_agent/` are present.

## Data Safety Checklist

* [ ] No large raw official datasets are committed.
* [ ] No real personal identifiers are committed.
* [ ] No fabricated risk results are presented as real.
* [ ] outputs are manually reviewed before upload.

## UI Checklist

* [ ] Streamlit app can start locally.
* [ ] UI displays empty states when outputs are missing.
* [ ] UI does not show automatic business action buttons.
* [ ] UI shows Human Confirmation boundary.

## Test Checklist

* [ ] `python -m py_compile scripts/run_full_pipeline.py scripts/project_health_check.py` passes.
* [ ] `python -m py_compile app/streamlit_app.py app/ui_data_loader.py app/ui_components.py app/ui_actions.py` passes.
* [ ] `python -m pytest` passes or dependency issue is documented.

## README Checklist

* [ ] Current phase is accurate.
* [ ] Safety boundary is clear.
* [ ] Run commands are accurate.
* [ ] Showcase links are present.

## GitHub Checklist

* [ ] Repository description prepared.
* [ ] Topics prepared.
* [ ] `.gitignore` checked.
* [ ] Git commands will be run manually by the user only.

## Interview Readiness Checklist

* [ ] 30-second talk track prepared.
* [ ] 1-minute talk track prepared.
* [ ] Resume bullets prepared.
* [ ] Q&A bank reviewed.
