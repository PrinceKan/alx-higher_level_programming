#!/usr/bin/python3

"""define function"""


def add_integer(a, b=98):
    """add_integer method

       Args:
            a(int): the first of the two arguments
            b(int): the second of the two arguments

       Return: The sum of the two arguments
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
