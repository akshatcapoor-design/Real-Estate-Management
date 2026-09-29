import json
import os

DATA_FILE = "properties.json"

def connect_db():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as err:
        print(f"Error loading property data: {err}")
        return []


def create_table():
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump([], file)
        except IOError as err:
            print(f"Could not create data file: {err}")


def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except IOError as err:
        print(f"Error saving data to file: {err}")
        return False
