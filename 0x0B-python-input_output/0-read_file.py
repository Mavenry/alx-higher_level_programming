#!/usr/bin/python3
""" this module reads a text file and prints it to stdout"""


def read_file(filename=""):
    """reads a text and print it to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
