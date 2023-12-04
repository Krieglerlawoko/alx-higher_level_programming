#!/usr/bin/python3
"""class and inherited class-checking function defined"""


def is_kind_of_class(obj, a_class):
    """Checks if object is instance or inherited instance of class
    """
    if isinstance(obj, a_class):
        return True
    return False
