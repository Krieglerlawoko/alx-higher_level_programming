#!/usr/bin/python3
"""a Rectangle class"""


class Rectangle:
    """a rectangle representation"""

    def __init__(self, width=0, height=0):
        """new Rectangle is initialized"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets or sets the width"""
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
        """Gets or sets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Return the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """Return the printable representation"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Return the string representation of Rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        """Print a message for every deletion"""
        print("Bye rectangle...")