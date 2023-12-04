#!/usr/bin/python3
"""class Rectangleinherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry represented"""

    def __init__(self, width, height):
        """new Rectangle initialized
        """
        super().integer_validator("height", height)
        self.__height = height
        super().integer_valiator("width", width)
        self.__width = width

    def area(self):
        """area of the rectangle returned"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
