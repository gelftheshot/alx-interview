#!/usr/bin/python3
"""
    rotating the matrix to 90 degree
"""


def rotate_2d_matrix(matrix):
    ''' Rotate a 2D matrix in-place. '''
    n = len(matrix)
    order = []

    for i in range(n):
        for j in range(n - 1, -1, -1):
            order.append(matrix[j][i])

    for i in range(n):
        for j in range(n):
            matrix[i][j] = order.pop(0)
