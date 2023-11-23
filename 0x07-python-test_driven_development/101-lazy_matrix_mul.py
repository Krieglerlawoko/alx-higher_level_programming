#!/usr/bin/python3
"""function multiplies matrix with Numpy"""
import numpy as nump


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrix"""

    return (nump.matmul(m_a, m_b))
