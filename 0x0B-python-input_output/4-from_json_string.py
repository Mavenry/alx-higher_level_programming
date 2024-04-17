#!/usr/bin/python3
"""Module that returns object represented by JSON string"""
import json


def from_json_string(my_str):
    """Function that returns JSON represented string"""
    return json.loads(my_str)

