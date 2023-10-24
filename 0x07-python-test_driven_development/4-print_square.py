#!/usr/bin/python3
"""function that prints a square"""

def print_square(size):
    """prints # square"""
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    for j in range(size):
        [print("#", end="") for k in range(size)]
        print("")
