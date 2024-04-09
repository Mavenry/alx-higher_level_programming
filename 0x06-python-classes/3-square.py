#!/usr/bin/python3
'''Define a class'''


    Class Square:
        '''Class Representation'''

        def __init__ (self, size = 0):
            '''Initialization of class
            Agrs: size, which is the initial size of the square
            Raise:
                TypeError: size must be an integer
                ValueError: size must be greater or equal to 0
            '''
            if not isinstance (size, int):
                raise TypeError('size must be an integer')
            if size < 0:
                raise ValueError('size must be greater than 0')
        def area (self, size):
            return size * size
