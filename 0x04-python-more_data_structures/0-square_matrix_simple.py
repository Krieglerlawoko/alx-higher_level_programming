#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = matrix.copy()

    for a in range(len(matrix)):
        matrix[a] = list(map(lambda a: a**2, matrix[a]))

    return (matrix2)
