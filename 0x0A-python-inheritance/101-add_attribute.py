#!/usr/bin/python3
"""function adds attributes to objects"""


def add_attribute(obj, att, value):
    """if possible ,Add an attribute to object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
