import subprocess
from config import Config, Option

class Result:
    success: bool
    error_message: None | str

    def __init__(self, success: bool, err: None | str = None):
        self.success = success
        self.error_message = err

    def is_success(self) -> bool:
        return self.success

    def error(self) -> str:
        return "(no error)" if self.error_message is None else self.error_message


class RofiRunner:
    last_result = None | Result

    def get_rofi_command(self) -> str:
        conf = Config()
        return f'echo -e "{"\n".join(conf.get_options_labels())}" | rofi -dmenu {'-i' if conf.case_sensitive else ''} -p "{conf.name}"'

    def select_option(self) -> Option:
        rofi_command = self.get_rofi_command()
        option_label = subprocess.run(rofi_command, shell=True, capture_output=True, text=True).stdout.strip()
        return Config().get_option_by_label(option_label)

    def run(self) -> Result:
        conf = Config()
        if not conf.is_valid():
            res = Result(False, "Invalid config")
            self.last_result = res
            return res

        option = self.select_option()

        command = conf.get_base_command().replace("%1", option.value)

        if command:
            subprocess.run(command, shell=True)

