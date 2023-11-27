#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """rectangle representation"""

    number_of_instance = 0
    print_symbl = "#"

    def __init__(self, width=0, height=0):
        """Rectangle initialization"""
        type(self).number_of_instance += 1
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
            raise ValueError("height msut be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Return the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectan = []
        for a in range(self.__height):
            [rectan.append(str(self.print_symbl)) for b in range(self.__width)]
            if a != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))

    def __repr__(self):
        """Return the string representation"""
        rectan = "Rectangle(" + str(self.__width)
        rectan += ", " + str(self.__height) + ")"
        return (rectan)

    def __del__(self):
        """Print a message for every deletion"""
        type(self).number_of_instance -= 1
        print("Bye rectangle...")
