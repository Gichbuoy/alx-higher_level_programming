#!/usr/bin/python3
"""program that defines a function for matrix division"""

def matrix_divided(matrix, div):
    """ dfine a function matrix_divided"""

    # Check if matrix is a list of non-empty lists containing only integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is an integer or a float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix containing the results of the division
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Return the new matrix
    return new_matrix
