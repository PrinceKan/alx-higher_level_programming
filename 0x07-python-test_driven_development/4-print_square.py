#!/usr/bin/python3

"""Define a function that print a square"""


def print_square(size):
    """print_square method

       Args:
            size (int): integer that represent the square's size
    """
    square = ""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for c in range(size):
        square += "#" * size + "\n"
    print(square, end="")
