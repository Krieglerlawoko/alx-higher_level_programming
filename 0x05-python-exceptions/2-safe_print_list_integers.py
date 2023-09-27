#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first occurance of an elements of a list"""
    a = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            a += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (a)
