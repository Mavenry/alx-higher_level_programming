#!/usr/bin/python3
""" defining a class """

    class Rectangle:
        """ this represents a class """
        def __init__ (self, width=0,height=0):
            """ Initializing the class rectangle
            Args:
                Width: represents the width of a rectangle
                height: represents the height of a rectangle
            Raises:
                TypeError: size must be an integer
                ValueError: size must be greater or equal to 0
            """
            self.width = width
            self.height = height

            @property
            def width(self):
                """ retrieving the width attribute """
                return self.__width
            
            @width.setter
            def width(self,value):
                """ setting the width attribute """
                if not isinstance(value, int):
                    raise TypeError("width must be an integer")
                if width < 0:
                    raise ValueError("width must be >= 0")
                else:
                    self.__width = value

           @property
           def height(self):
               """ retrieving the height"""
               return self.__height

           @height.setter
           def height(self, value):
               """ setting the height """
               if not isinstance(value, int):
                   raise TypeError("height must be an integer")
               if height < 0:
                   raise ValueError("height must be >= 0")
               else:
                   self.__height = value

