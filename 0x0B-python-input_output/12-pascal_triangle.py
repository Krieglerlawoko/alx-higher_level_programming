#!/usr/bin/python3
"""Pascal's Triangle function defined"""


def pascal_triangle(n):
    """Pascal's Triangle of size n representaton"""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        triang = tri[-1]
        tm = [1]
        for a in range(len(triang) - 1):
            tm.append(triang[a] + triang[a + 1])
        tm.append(1)
        tri.append(tm)
    return tri
