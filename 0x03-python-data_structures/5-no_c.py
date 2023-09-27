#!/usr/bin/python3


def no_c(my_string):
    """Remove  characters c and C in string"""
    newlist = [a for a in my_string if a != 'c' and a != 'C']
    return ("".join(newlist))
