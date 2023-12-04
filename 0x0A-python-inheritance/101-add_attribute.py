#!/usr/bin/python3
"""function that adds attributes to objects added"""


def add_attribute(obj, att, value):
    """new attribute to an object added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
