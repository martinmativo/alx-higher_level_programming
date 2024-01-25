#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for m in range(len(matrix)):
        nmatrix.append([])

        for n in range(len(matrix[m])):
            nmatrix[m].append(matrix[m][n] ** 2)

    return nmatrix)
