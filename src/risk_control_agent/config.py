from pathlib import Path
from typing import Any, Dict

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - exercised only in minimal environments
    yaml = None


def _parse_simple_yaml_mapping(text: str) -> Dict[str, Any]:
    """Parse simple key-value YAML files when PyYAML is not installed.

    This fallback is intentionally limited to flat mappings such as
    configs/data_paths.yaml. Nested project configs should use PyYAML.
    """
    result: Dict[str, Any] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            raise RuntimeError("PyYAML is required for nested YAML configuration files.")
        key, value = stripped.split(":", 1)
        value = value.strip()
        if not value:
            raise RuntimeError("PyYAML is required for nested YAML configuration files.")
        result[key.strip()] = value
    return result


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def resolve_path(path_string: str) -> Path:
    path = Path(path_string)
    if path.is_absolute():
        return path
    return get_project_root() / path


def load_yaml_config(path: str | Path) -> Dict[str, Any]:
    config_path = resolve_path(str(path))
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as file:
        text = file.read()
    if yaml is None:
        data = _parse_simple_yaml_mapping(text)
    else:
        data = yaml.safe_load(text) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config file must contain a mapping: {config_path}")
    return data


def load_data_paths(config_path: str = "configs/data_paths.yaml") -> Dict[str, Path]:
    raw_config = load_yaml_config(config_path)
    resolved = {}
    for key, value in raw_config.items():
        if key == "project_root":
            resolved[key] = resolve_path(str(value))
        else:
            resolved[key] = resolve_path(str(value))
    return resolved
