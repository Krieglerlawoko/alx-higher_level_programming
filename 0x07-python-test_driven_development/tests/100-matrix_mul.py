#!/usr/bin/python3

"""Matrix multipling function"""


def matrix_mul(m_a, m_b):
    """Two matrices multiplied"""

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    invert_k = []
    for a in range(len(m_b[0])):
        newRow = []
        for k in range(len(m_b)):
            newRow.append(m_b[k][a])
        invert_k.append(newRow)

    n_matrix = []
    for row in m_a:
        newRow = []
        for col in inverted_b:
            prod = 0
            for g in range(len(invert_k[0])):
                prod += row[g] * col[g]
            newRow.append(prod)
        n_matrix.append(newRow)

    return n_matrix
