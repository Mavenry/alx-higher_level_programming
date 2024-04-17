#!/usr/bin/python3
"""This module defines a JSON to text file function"""
import json


def save_to_json_file(my_obj, filename):
    """This funtion writes an object to a text file using JSON representation"""

    json_string = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(json_string)
