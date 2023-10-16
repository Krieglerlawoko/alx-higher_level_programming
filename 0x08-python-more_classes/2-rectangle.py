#!/usr/bin/python3
"""a Rectangle class"""


class Rectangle:
    """a rectangle representation"""

    def __init__(self, width=0, height=0):
        """a new Rectangle initialized"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter of setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Getter of setter for height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Return the Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the Rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))