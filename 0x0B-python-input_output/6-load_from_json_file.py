#!/urs/bin/python3
"""Module that creates a file from JSON file"""
import json


def load_from_json_file(filename):
    """Creates a file from json file"""
    with open(filename, "w") as f:
        return json.load(f)
