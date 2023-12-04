#!/usr/bin/python3
"""class MyInt inheriting from int defined"""


class MyInt(int):
    """Invert int operators"""

    def __eq__(self, value):
        """Override == opeartor"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator"""
        return self.real == value
