#!/usr/bin/python3


def element_at(my_list, idx):
    """gets an element of a list."""
    if idx > (len(my_list) - 1) or idx < 0:
        return None
    return (my_list[idx])
