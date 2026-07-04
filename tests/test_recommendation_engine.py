from risk_control_agent.recommendation_engine import filter_prohibited_actions


def test_prohibited_recommendations_filtered():
    recommendations = [
        {"recommendation": "建议自动拒贷", "level": "bad"},
        {"recommendation": "建议人工复核高风险客群", "level": "ok"},
    ]
    filtered = filter_prohibited_actions(recommendations)
    assert len(filtered) == 1
    assert "人工复核" in filtered[0]["recommendation"]
