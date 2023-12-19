#!/usr/bin/python3
"""function finds max int in a list"""


def max_integer(list=[]):
    """Returns max int in a list"""
    if len(list) == 0:
        return None
    maxRes = list[0]
    a = 1
    while a < len(list):
       if list[a] > maxRes:
           maxRes = list[a]
       a += 1
    return maxRes
