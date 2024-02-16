#!/usr/bin/python3
"""Max integer in a list finder"""


def max_integer(list=[]):
    """Finds and returns max integer in list of integers
        If the list is empty, returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    a = 1
    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return
