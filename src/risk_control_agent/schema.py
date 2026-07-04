from typing import Any, Dict, List


def get_table_schema(schema_config: Dict[str, Any], table_name: str) -> Dict[str, Any]:
    if table_name not in schema_config:
        raise KeyError(f"Table schema not found: {table_name}")
    table_schema = schema_config[table_name]
    if not isinstance(table_schema, dict):
        raise ValueError(f"Table schema must be a mapping: {table_name}")
    return table_schema


def get_required_columns(schema_config: Dict[str, Any], table_name: str) -> List[str]:
    return list(get_table_schema(schema_config, table_name).get("required_columns", []))


def get_optional_columns(schema_config: Dict[str, Any], table_name: str) -> List[str]:
    return list(get_table_schema(schema_config, table_name).get("optional_columns", []))


def list_supported_tables(schema_config: Dict[str, Any]) -> List[str]:
    return sorted(schema_config.keys())

