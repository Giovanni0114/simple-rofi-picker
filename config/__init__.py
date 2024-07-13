import json
from .validator import validate_json_data

class Option:
    def __init__(self, label: str, value: str):
        self.label = label
        self.value = value

    def __repr__(self):
        return f"Option(label={self.label}, value={self.value})"

class ConfigSingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Config(metaclass=ConfigSingletonMeta):
    name = None | str
    base_command = None | str
    case_sensitive = None | bool
    options = None | list[Option]

    def __repr__(self):
        return f"Config(name={self.name}, base_command={self.base_command}, case_sensitive={self.case_sensitive}, options=<{len(self.options)}>)"

    def is_valid(self) -> bool:
        return self.name is not None and \
            self.base_command is not None and \
            self.case_sensitive is not None and \
            self.options is not None and len(self.options) > 0

    def load_from_file(self, filepath: str):
        with open(filepath, 'r') as file:
            data = json.load(file)

        validate_json_data(data)

        self.name = data["name"]
        self.base_command = data['base_command']
        self.case_sensitive = data['case_sensitive']
        self.options = [Option(opt['label'], opt['value']) for opt in data['options']]

    def get_name(self) -> str:
        assert self.name is not None
        return self.name

    def get_case_senitive(self) -> bool:
        assert self.case_sensitive is not None
        return self.case_sensitive

    def get_base_command(self) -> str:
        assert self.base_command is not None
        return self.base_command

    def get_options_labels(self) -> list[str]:
        assert self.options is not None
        assert len(self.options) > 0
        return [opt.label for opt in self.options]

    def get_option_by_label(self, label: str) -> Option | None:
        for opt in self.options:
            if opt.label == label:
                return opt
        return None


