#!/usr/bin/python3
"""an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
