#!/usr/bin/python3
"""Python class-to-JSON function"""


def class_to_json(obj):
    """Return a dictionary represntation"""
    return obj.__dict__
