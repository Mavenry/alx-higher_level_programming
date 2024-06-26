#!/usr/bin/python3
"""This module defines a JSON that write to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON form"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
