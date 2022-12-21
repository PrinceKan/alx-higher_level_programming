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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return: the area of a square in process"""
        return (self.__size*self.__size)

    @property
    def size(self):
        """Return: the area of a square in process"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """printa the square"""
        if self.__size == 0:
            print()
        for idx in range(self.__size):
            if self.__size != 0:
                print('#'*self.__size)
