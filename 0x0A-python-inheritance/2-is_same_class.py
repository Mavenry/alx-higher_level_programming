#!/usr/bin/python3
"""this module checks if the the object is an instance of a class"""


def is_same_class(obj, a_class):
    """Return true if the oject is an instance and false if not"""
    return (type(obj) == a_class)
