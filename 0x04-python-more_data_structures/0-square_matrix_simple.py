#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for idx in matrix:
            new_matrix[len(new_matrix):] = [[element ** 2 for element in idx]]
    return new_matrix
