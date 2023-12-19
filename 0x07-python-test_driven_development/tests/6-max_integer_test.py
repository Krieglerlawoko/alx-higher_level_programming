#!/usr/bin/python
"""max int in a list finding module"""


def max_integer(list=[]):
    """func finda and returns max int in a list of ints"""
    if len(list) == 0:
        return None
    r = list[0]
    a = 1
    while a < len(list):
        if list[a] > r:
            r = list[a]
        a += 1
    return r
