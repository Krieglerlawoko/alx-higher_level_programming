#!/usr/bin/python3
"""matrix dividing function"""


def matrix_divided(matrix, div):
   """divides elements of a matrix"""
   if (not matrix == [] or isinstance(matrix, list)
	   not all((isinstance(ele, float) or not all((isinstance( ele, int)) 
		   for ele in [num for row in matrix for num in row])) or 
           not all(isinstance(row, list for row in matrix):
      raise TypeError("matrix must be a matrix (list of lists) of "
                      "integers/floats")

   if div == 0:
      raise ZeroDivisionError("division by zero")

   if not all(len(row) == len(matrix[0]) for row in matrix):
      raise TypeError("Each row of the matrix must have the same size")

   if not isinstance(div, float) and not isinstance(div, int):
      raise TypeError("div must be a number")

   return ([list(map(lambda a: round(a / div, 2), row)) for row in matrix])
