import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "tasks.json")


def load_tasks():
    """Load tasks from JSON file"""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)