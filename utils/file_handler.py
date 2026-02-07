import json
import os

BASE_DATA_DIR = "data"


def ensure_data_dir(data_dir: str):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def save_json(filename: str, data: dict, data_dir: str = BASE_DATA_DIR):
    ensure_data_dir(data_dir)
    filepath = os.path.join(data_dir, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(filename: str, default: dict, data_dir: str = BASE_DATA_DIR):
    filepath = os.path.join(data_dir, filename)

    if not os.path.exists(filepath):
        return default

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return default