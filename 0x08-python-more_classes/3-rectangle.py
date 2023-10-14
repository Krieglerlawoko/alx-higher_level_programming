#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """rectangle representation"""

    def __init__(self, width=0, height=0):
        """a new Rectangle is initialized"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter or setter for width"""
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
        """Getter or setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise VAlueError("height must be >= 0")
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
        """Return the printable representation Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rec = []
        for a in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if a != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))
