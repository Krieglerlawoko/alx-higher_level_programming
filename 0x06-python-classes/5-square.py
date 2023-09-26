#!/usr/bin/python3
"""class Square."""


class Square:
    """class square."""

    def __init__(self, size):
        """Initialize"""
        self.size = size

    @property
    def size(self):
        """Get or set current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")

        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """Return current area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square"""
        for a in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
