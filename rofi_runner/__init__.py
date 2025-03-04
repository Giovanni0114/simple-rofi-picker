import subprocess
from config import Config

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
    def get_rofi_command() -> str:
        case_ses = '' if Config.get_case_sensitive() else '-i'
        options_entry = "\n".join(Config.get_options_labels())
        return f'echo -e "{options_entry}" | rofi -dmenu {case_ses} -p "{Config.get_name()}"'

    def run() -> Result:
        rofi_command = RofiRunner.get_rofi_command()
        option_label = subprocess.run(rofi_command, shell=True, capture_output=True, text=True).stdout.strip()
        option = Config.get_option_by_label(option_label)

        if not option:
            return Result(False, "No such option")

        command = Config.get_base_command().replace("%1", option.value)
        if subprocess.run(command, shell=True).returncode != 0:
            return Result(False, "Error during execution")

        return Result(True)

