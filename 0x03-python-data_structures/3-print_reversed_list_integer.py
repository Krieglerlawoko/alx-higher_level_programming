#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Prints integers a reversed list"""
    if isinstance(my_list, list):
        my_list.reverse()
        for a in my_list:
            print("{:d}".format(a))
