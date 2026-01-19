# utils/save_json.py
import json

def save_json(result):
    with open("output/result.json", "w") as f:
        json.dump(result, f, indent=2)
