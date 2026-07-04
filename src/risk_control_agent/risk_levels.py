RISK_LEVEL_ORDER = {
    "Level 0": 0,
    "Level 1": 1,
    "Level 2": 2,
    "Level 3": 3,
    "Level 4": 4,
}


def normalize_risk_level(level: str | None) -> str:
    """Return a standard risk level, defaulting to Level 0 for empty input."""
    if level is None:
        return "Level 0"
    normalized = str(level).strip()
    if normalized not in RISK_LEVEL_ORDER:
        raise ValueError(f"Unknown risk level: {level}")
    return normalized


def compare_risk_levels(level_a: str, level_b: str) -> int:
    """Compare two risk levels; positive means level_a is higher."""
    a = RISK_LEVEL_ORDER[normalize_risk_level(level_a)]
    b = RISK_LEVEL_ORDER[normalize_risk_level(level_b)]
    return a - b


def get_max_risk_level(levels) -> str:
    """Return the highest standard risk level from an iterable."""
    if not levels:
        return "Level 0"
    normalized = [normalize_risk_level(level) for level in levels]
    return max(normalized, key=lambda level: RISK_LEVEL_ORDER[level])


def is_high_risk(level: str) -> bool:
    """Return True for Level 3 or Level 4."""
    return RISK_LEVEL_ORDER[normalize_risk_level(level)] >= RISK_LEVEL_ORDER["Level 3"]

