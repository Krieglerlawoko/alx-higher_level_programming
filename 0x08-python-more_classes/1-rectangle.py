#!/usr/bin/python3
"""Rectangle class defined"""


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """new Rectangle is initialized"""
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
        """Getter of setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
