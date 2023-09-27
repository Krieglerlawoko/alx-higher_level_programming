#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """changes an element of a list at a position idx"""
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return (my_list)
