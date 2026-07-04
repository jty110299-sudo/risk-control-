from risk_control_agent.interactive_report import build_user_report_context, generate_user_markdown_report


def test_report_contains_human_confirmation_and_disclaimer():
    context = build_user_report_context(recommendations=[{"level": "需要人工确认", "recommendation": "人工复核高风险分层"}])
    report = generate_user_markdown_report(context)
    assert "人工确认" in report
    assert "免责声明" in report
