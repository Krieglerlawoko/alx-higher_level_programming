#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx > (len(my_list) - 1) or idx < 0:
        return (my_list)

    newlist = [a for a in my_list]
    copy[idx] = element
    return (newlist)
