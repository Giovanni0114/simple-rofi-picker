#!/usr/bin/python3

import json
import argparse

from config import Config
from rofi_runner import RofiRunner

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a JSON configuration file for Picker.')
    parser.add_argument('filepath', type=str, help='Path to the JSON configuration file', default="-")
    args = parser.parse_args()

    try:
        Config.init(args.filepath)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        parser.exit(1, f"Error reading JSON file: {e}\n")
    except ValueError as e:
        parser.exit(2, f"Validation error: {e}\n")

    RofiRunner.run()

