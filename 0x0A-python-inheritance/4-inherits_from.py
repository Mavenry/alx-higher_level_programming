#!/usr/bin/python3
"""module that checks the object is and instance of a super class"""


def is_kind_of_class(obj, a_class):
    """return True if obj is an instance of super class otherwise False"""
    return isinstance(obj, a_class)
