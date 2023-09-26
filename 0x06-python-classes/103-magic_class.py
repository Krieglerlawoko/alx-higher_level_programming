#!/usr/bin/python3
"""Class"""

import math


class MagicClass:
    """a circle."""

    def __init__(self, radius=0):
        """Initializes."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the circle"""
        return (2 * math.pi * self.__radius)
