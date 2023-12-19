#!/usr/bin/python3
"""matrix multiplying function defined"""


def matrix_mul(m_a, m_b):
    """two matrices multiplied"""
    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")
    if m_a == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if  not all((isinstance(ele, float) or isinstance(ele, int))
                for ele in [num for row in m_a for num in row]):
