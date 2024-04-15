#!/usr/bin/python3
"""This module inherits from list module"""


class MyList(list):
    """ this class show the list of student in a class"""
    def print_sorted(self):
        """this method prints the sorted list"""
        print(sorted(self))
