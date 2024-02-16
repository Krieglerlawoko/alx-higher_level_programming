#!/usr/bin/python3

"""Integer adding function"""


def add_integer(a, b=98):
    """Returns sum of a and b"""
    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    if ((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")
    return (int(a) + int(b))
