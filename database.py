
import json
import os

DB_FILE = "employee_data.json"

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}
