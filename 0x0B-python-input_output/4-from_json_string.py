#!/usr/bin/python3
"""This module defines JSON-Python function"""
import json


def from_json_string(my_str):
    """Returns the python representation of JSON string"""
    return json.loads(my_str)

