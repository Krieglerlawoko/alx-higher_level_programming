#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if object is inherited instance of class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
