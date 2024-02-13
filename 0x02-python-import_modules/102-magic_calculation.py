#!/usr/bin/python3

def magic_calculation(a, b):
    """Calculator"""
    from magic_calculation_102 import add, sub

    if a < b:
        k = add(a, b)
        for j in range(4, 6):
            k = add(k, j)
        return (k)

    else:
        return(sub(a, b))
