#!/usr/bin/python3
"""a Pascal's Triangle function"""


def pascal_triangle(n):
    """Pascal's Triangle of size n"""
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        tr = t[-1]
        tm = [1]
        for j in range(len(tr) - 1):
            tm.append(tr[j] + tr[j + 1])
        tm.append(1)
        t.append(tm)
    return t
