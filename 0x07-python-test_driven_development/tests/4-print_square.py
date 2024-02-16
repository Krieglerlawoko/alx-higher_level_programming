#!/usr/bin/python3

"""Square-printing function"""


def print_square(size):
    """Print a square with #"""
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for a in range(size):
        [print("#", end="") for k in range(size)]
        print("")
