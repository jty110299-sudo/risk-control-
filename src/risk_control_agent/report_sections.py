def _not_available() -> str:
    return "Not available in this run."


def format_markdown_table(rows, columns=None) -> str:
    """Format a list of dictionaries as a Markdown table."""
    if not rows:
        return _not_available()
    if columns is None:
        columns = list(rows[0].keys())
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join(["---"] * len(columns)) + " |"
    body = []
    for row in rows:
        body.append("| " + " | ".join(str(row.get(column, "")) for column in columns) + " |")
    return "\n".join([header, separator] + body)


def render_executive_summary(alert_summary=None, root_cause_summary=None) -> str:
    """Render executive summary without fabricating missing findings."""
    if not alert_summary and not root_cause_summary:
        return "## Executive Summary\n\n" + _not_available()
    lines = ["## Executive Summary", ""]
    if alert_summary:
        lines.append(f"* Overall risk level: `{alert_summary.get('overall_risk_level', 'Unknown')}`.")
        lines.append(f"* Triggered alert count: `{alert_summary.get('alert_count', 0)}`.")
    if root_cause_summary:
        lines.append(
            "* Root cause findings are investigation leads, not causal proof."
        )
        lines.append(f"* Root cause analysis status: `{root_cause_summary.get('analysis_status', 'Unknown')}`.")
    return "\n".join(lines)


def render_overall_risk_level(alert_summary=None) -> str:
    """Render overall risk level section."""
    if not alert_summary:
        return "## Overall Risk Level\n\n" + _not_available()
    return (
        "## Overall Risk Level\n\n"
        f"* Overall risk level: `{alert_summary.get('overall_risk_level', 'Unknown')}`\n"
        f"* Human confirmation required: `{alert_summary.get('human_confirmation_required', False)}`"
    )


def render_triggered_alert_rules(alert_summary=None) -> str:
    """Render triggered alert rule evidence."""
    alerts = (alert_summary or {}).get("triggered_alerts", [])
    if not alerts:
        return "## Triggered Alert Rules\n\n" + _not_available()
    rows = [
        {
            "rule_id": alert.get("rule_id"),
            "metric": alert.get("metric"),
            "risk_level": alert.get("risk_level"),
            "evidence": alert.get("evidence"),
            "human_confirmation_required": alert.get("human_confirmation_required"),
        }
        for alert in alerts
    ]
    return "## Triggered Alert Rules\n\n" + format_markdown_table(rows)


def render_key_metric_findings(alert_summary=None) -> str:
    """Render key metric findings based on triggered alerts."""
    alerts = (alert_summary or {}).get("triggered_alerts", [])
    if not alerts:
        return "## Key Metric Findings\n\n" + _not_available()
    lines = ["## Key Metric Findings", ""]
    for alert in alerts:
        lines.append(
            f"* `{alert.get('metric')}` triggered `{alert.get('rule_id')}` with evidence `{alert.get('evidence')}`."
        )
    return "\n".join(lines)


def render_root_cause_findings(root_cause_summary=None) -> str:
    """Render root cause findings as investigation leads, not causality."""
    findings = (root_cause_summary or {}).get("metric_change_findings", [])
    if not findings:
        return "## Root Cause Findings\n\n" + _not_available()
    lines = ["## Root Cause Findings", "", "These findings are investigation leads, not causal proof.", ""]
    for finding in findings:
        lines.append(
            f"* Metric `{finding.get('metric')}` changed by `{finding.get('change')}` in period `{finding.get('monitoring_period')}`."
        )
    return "\n".join(lines)


def render_segment_contribution_findings(root_cause_summary=None) -> str:
    """Render segment contribution findings."""
    contributors = (root_cause_summary or {}).get("top_contributors", [])
    if not contributors:
        return "## Segment Contribution Findings\n\n" + _not_available()
    return (
        "## Segment Contribution Findings\n\n"
        "Contribution indicates investigation priority, not causal proof.\n\n"
        + format_markdown_table(contributors)
    )


def render_data_availability(alert_summary=None, root_cause_summary=None) -> str:
    """Render data availability section."""
    rows = [
        {"input": "alert_summary", "available": bool(alert_summary)},
        {"input": "root_cause_summary", "available": bool(root_cause_summary)},
    ]
    if root_cause_summary:
        for key, value in root_cause_summary.get("available_inputs", {}).items():
            rows.append({"input": key, "available": value})
    return "## Data Availability\n\n" + format_markdown_table(rows)


def render_human_confirmation_items(alert_summary=None, root_cause_summary=None) -> str:
    """Render human confirmation items."""
    items = []
    for alert in (alert_summary or {}).get("triggered_alerts", []):
        if alert.get("human_confirmation_required"):
            items.append(f"* Rule `{alert.get('rule_id')}` requires human confirmation.")
    if (root_cause_summary or {}).get("human_confirmation_required"):
        items.append("* Root cause summary indicates human confirmation is required.")
    if not items:
        return "## Items Requiring Human Confirmation\n\n" + _not_available()
    return "## Items Requiring Human Confirmation\n\n" + "\n".join(items)


def render_limitations() -> str:
    """Render report limitations."""
    return (
        "## Limitations\n\n"
        "* This report is generated from available structured summaries only.\n"
        "* Missing sections are marked as unavailable and are not fabricated.\n"
        "* Root cause findings are investigation leads, not causal proof.\n"
        "* Thresholds are illustrative and require calibration before real-world use.\n"
        "* The report does not execute business actions."
    )


def render_appendix(alert_summary=None, root_cause_summary=None) -> str:
    """Render appendix summary."""
    return (
        "## Appendix\n\n"
        f"* Alert summary available: `{bool(alert_summary)}`\n"
        f"* Root cause summary available: `{bool(root_cause_summary)}`"
    )

