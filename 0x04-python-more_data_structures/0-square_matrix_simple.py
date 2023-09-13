#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for a in range(len(matrix)):
        new_matrix[a] = list(map(lambda j: j*j,matrix[a]))

        return (new_matrix)
