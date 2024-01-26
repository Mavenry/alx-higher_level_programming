#!/usr/bin/python3
"""Defines a class"""


class Square:
    """class representation"""

    def __init__(self, size=0):
        """Initializing the Square class
        Args: size - is the size of the square aad it is initiated to 0
        Raises:
            TypeError: must be int
            ValueError: must be greater or equal to 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
