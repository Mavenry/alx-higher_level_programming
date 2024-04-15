#!/usr/bin/python3
"""module that checks the object is and instance of a a_class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class otherwise False"""
    return isinstance(obj, a_class)
