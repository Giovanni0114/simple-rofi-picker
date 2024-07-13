from typing import Any

TYPES_IN_CONFIG_ROOT = [
    ("name", str),
    ("base_command", str),
    ("case_sensitive", bool),
    ("options", list),
]

TYPES_IN_CONFIG_OPTION = [
    ("name", str),
    ("value", str),
]


def validate_json_data(data: Any):
    if not isinstance(data, dict):
        raise ValueError("JSON data must be a dictionary")

    for name, t in TYPES_IN_CONFIG_ROOT:
        if name not in data or not isinstance(data[name], t):
            raise ValueError(f"Missing or invalid '{name}' field")

    if "%1" not in data["base_command"]:
        raise ValueError("No placeholder for value in 'base_command'")

    if len(data["options"]) == 0:
        raise ValueError("List of options should not be empty")

    for option in data["options"]:
        if not isinstance(option, dict):
            raise ValueError("Each option must be a dictionary")

        for name, t in TYPES_IN_CONFIG_ROOT:
            if name not in data or not isinstance(data[name], t):
                raise ValueError(f"Missing or invalid '{name}' field")
