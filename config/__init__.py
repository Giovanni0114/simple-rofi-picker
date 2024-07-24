import json
from .validator import validate_json_data

class Option:
    def __init__(self, label: str, value: str):
        self.label = label
        self.value = value

    def __repr__(self):
        return f"Option(label={self.label}, value={self.value})"

class SingletonConfig:
    _instance = None

    name = None | str
    base_command = None | str
    case_sensitive = None | bool
    options = None | list[Option]

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonConfig, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def load_from_file(self, filepath: str) -> None:
        with open(filepath, 'r') as file:
            data = json.load(file)

        validate_json_data(data)

        self.name = data["name"]
        self.base_command = data['base_command']
        self.case_sensitive = data['case_sensitive']
        self.options = [Option(opt['label'], opt['value']) for opt in data['options']]

    def is_valid(self) -> bool:
        return self.name is not None and \
            self.base_command is not None and \
            self.case_sensitive is not None and \
            self.options is not None and len(self.options) > 0

    def __repr__(self):
        return f"Config(name={self.name}, base_command={self.base_command}, case_sensitive={self.case_sensitive}, options=<{len(self.options)}>)"


class Config:
    def init(path: str) -> bool:
        SingletonConfig().load_from_file(path)
        return SingletonConfig().is_valid()

    def to_string() -> str:
        return SingletonConfig().__repr__()

    def get_name() -> str:
        return SingletonConfig().name

    def get_case_sensitive() -> bool:
        return SingletonConfig().case_sensitive

    def get_base_command() -> str:
        return SingletonConfig().base_command

    def get_options_labels() -> list[str]:
        return [opt.label for opt in SingletonConfig().options]

    def get_option_by_label(label: str) -> Option | None:
        for opt in SingletonConfig().options:
            if opt.label == label:
                return opt
        return None

