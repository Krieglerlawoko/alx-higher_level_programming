#!/usr/bin/python3
"""a Pascal's Triangle function"""


def pascal_triangle(n):
    """Pascal's Triangle of size n"""
    if a <= 0:
        return []

    t = [[1]]
    while len(t) != a:
        tri = t[-1]
        tmp = [1]
        for j in range(len(tri) - 1):
            tmp.append(tri[j] + tri[j + 1])
        tmp.append(1)
        t.append(tmp)
    return t
