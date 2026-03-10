"""
utils/file_handler.py — JSON read/write utility
"""
import json
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")


def read_json(filename: str) -> dict:
    """Read and return data from a JSON file in /data/"""
    path = os.path.join(BASE_DIR, filename)
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"  [!] Data file not found: {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"  [!] Corrupted data file: {filename}")
        return {}


def write_json(filename: str, data: dict) -> bool:
    """Write data to a JSON file in /data/"""
    path = os.path.join(BASE_DIR, filename)
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"  [!] Failed to write {filename}: {e}")
        return False
