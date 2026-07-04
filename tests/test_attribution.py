import pandas as pd

from risk_control_agent.attribution import SAFETY_NOTE, build_segment_risk_summary


def test_segment_risk_summary_outputs_high_risk_ratio():
    df = pd.DataFrame({"segment": ["a", "a", "b"], "risk_score": [200, 900, 300], "target": [1, 0, 1]})
    summary = build_segment_risk_summary(df, "segment", target_col="target")
    assert "high_risk_ratio" in summary.columns
    assert len(summary) == 2


def test_attribution_safety_note_not_causal():
    assert "不是因果证明" in SAFETY_NOTE
