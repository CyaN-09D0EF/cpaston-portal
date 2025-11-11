import json, os
from filelock import FileLock

DATA_PATH = os.environ.get("DATA_PATH", "data/capstone.json")
LOCK_PATH = DATA_PATH + ".lock"

def read_json():
    with FileLock(LOCK_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

def write_json(payload: dict):
    with FileLock(LOCK_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
