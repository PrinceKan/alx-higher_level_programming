#!/usr/bin/python3

"""Defines a square"""


class Square():
    """represent asquare"""

    def __init__(self, size):
        """ __init__ method

        Args:
            size (int): integer that represents the square's size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
