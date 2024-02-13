#!/usr/bin/python3


def magic_calculation(a, b):
    """Match bytecode"""
    from magic_calculation_102 import add, sub

    if a > b:
        return(sub(a, b))
    else:
        k = add(a, b)
        for j in range(4, 6):
            k = add(k, j)
        return (j)
