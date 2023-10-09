#!/usr/bin/python3
"""A base geometry class BaseGeometry."""


class BaseGeometry:
    """A base geometry."""

    def area(self):
        """Unimplemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if a parameter is an integer"""
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
