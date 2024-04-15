#!/usr/bin/python3
""" class that return the list of available attributes"""


def lookup(obj):
    """return a list of attributes"""
    return dir(obj)
