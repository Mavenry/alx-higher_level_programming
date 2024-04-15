#!/usr/bin/python3
"""this module checks if the instance of a class"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the class otherwise, return False"""
    return (type(obj) == a_class)
