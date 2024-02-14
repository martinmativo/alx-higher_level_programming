#!/usr/bin/python3

class Rectangle:
    def __init__(self, width = 0, height = 0):

        self.width = width
        self.height = height

    @property
    self.__width =(self):

        return self.__width

    """Create a setter to be able to check for errors in type/value"""

    @width.setter
    def width (self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer" )
        if value <= 0:
            raise ValueError("width must be >= 0" )

        self.__width = value
    @property
    self.__height = (self):

        return self.__height

    @height.setter
    def height (self, value):
        if not isinstance(value, int):
            raise TypeError("Value of height must be >= 0" )
        if value <= 0:
            raise ValueError("Value of height must be >= 0" )

        return self.__height

    def area (self)

    return (self.__width * self.__height)
    
    def perimeter (self)

    if self.__width == 0 or self.__height ==0:
        return(0)

    return ((self.__width * 2) + (self.__height * 2))


