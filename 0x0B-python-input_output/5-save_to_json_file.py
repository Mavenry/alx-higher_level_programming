#!/usr/bin/python3
"""This module defines a JSON to text file function"""
import json


def save_to_json_file(my_obj, filename):
    """This funtion writes an object to a text file using JSON representation"""

    with open(filename, "w", encoding= "utf-8") as f:
        json.dump(my_obj, f)
