#!/usr/bin/python3

"""Defines a square"""


class Square():
    """represent asquare"""

    def __init__(self, size=0):
        """ __init__ method

        Args:
            size (int): integer that represents the square's size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns: The area of a square in process"""
        return (self.__size*self.__size)
