#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ln in matrix:
        for x in ln:
            print('{:d}'.format(x), end="")
            if x != ln[-1]:
                print(end=" ")
        print()
