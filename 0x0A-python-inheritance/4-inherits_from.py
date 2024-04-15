#!/usr/bin/python3
"""module to check if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class otherwise False"""
    return isinstance(obj, a_class)
