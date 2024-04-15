#!/usr/bin/python3
"""module to check if the object is an instance of a_class"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class otherwise return False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
