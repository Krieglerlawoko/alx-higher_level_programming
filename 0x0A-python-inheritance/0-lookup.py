#!/usr/bin/python3
"""lookup function of an object attribute"""


def lookup(obj):
    """list of available attributes of an object are returned"""
    return (dir(obj))
