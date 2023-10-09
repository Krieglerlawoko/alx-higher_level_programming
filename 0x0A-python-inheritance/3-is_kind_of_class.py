#!/usr/bin/python3
"""function checks for class and inherited class"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inherited instance"""
    if isinstance(obj, a_class):
        return True
    return False
