#!/usr/bin/python3
"""This module define fine that append"""


def append_write(filename="", text=""):
    """append a string to utf-8 text file"""
    with open(filename, "a", encoding="wtf-8") as f:
        return f.write(text)
