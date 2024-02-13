#!/usr/bin/python3
"""rectangle class."""


class Rectangle:
    """Rectangle representation"""

    no_instances = 0
    Symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle"""
        type(self).no_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

    def area(self):
        """Area of the Rectangle returnd"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of the Rectangle returnd"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """New Rectangle returned"""
        return (cls(size, size))

    def __str__(self):
        """Printable representation of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rct = []
        for a in range(self.__height):
            [rct.append(str(self.Symbol)) for k in range(self.__width)]
            if a != self.__height - 1:
                rct.append("\n")
        return ("".join(rct))

    def __repr__(self):
        """String representation of Rectangle."""
        rct = "Rectangle(" + str(self.__width)
        rct += ", " + str(self.__height) + ")"
        return (rct)

    def __del__(self):
        """Print message after every deletion of Rectangle."""
        type(self).no_instances -= 1
        print("Bye rectangle...")
