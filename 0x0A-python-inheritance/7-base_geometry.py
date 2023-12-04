#!/usr/bin/python3
"""base geometry class BaseGeometry defined"""


class BaseGeometry:
    """base geometry represented"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """parameter validated as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
