#!/usr/bin/python3

""" Define the function pascal_triangle """


def pascal_triangle(n):
    """pascal_triangle method that returns a list of lists of integers
       representing the Pascal’s triangle of n

       Args:
            n(int): an integer

       Return: an empty list if n <= 0
    """
    if n <= 0:
        return []
    big = []
    big.append([1, ])
    for i in range(0, n - 1):
        small = [1, ]
        for j in range(0, len(big[-1]) - 1):
            small.append(big[-1][j] + big[-1][j + 1])
        small.append(1)
        big.append(small)
    return big
