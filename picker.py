#!/usr/bin/python3

import json
import argparse

import config
import rofi_runner

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a JSON configuration file for Notifier.')
    parser.add_argument('filepath', type=str, help='Path to the JSON configuration file')
    args = parser.parse_args()

    try:
        conf = config.Config()
        conf.load_from_file(args.filepath)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        exit(1)
    except ValueError as e:
        print(f"Validation error: {e}")
        exit(2)

    runnner = rofi_runner.RofiRunner()
    runnner.run()

