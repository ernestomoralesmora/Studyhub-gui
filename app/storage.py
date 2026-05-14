import json
import os


def get_data_file():
    snap_user_data = os.environ.get("SNAP_USER_DATA")

    if snap_user_data:
        data_dir = os.path.join(snap_user_data, "data")
        os.makedirs(data_dir, exist_ok=True)
        return os.path.join(data_dir, "tasks.json")

    return os.path.join(os.path.dirname(__file__), "data", "tasks.json")


DATA_FILE = get_data_file()


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)