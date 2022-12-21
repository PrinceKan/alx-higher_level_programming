#!/usr/bin/python3

"""Defines a square"""


class Square():
    """represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ __init__ method

        Args:
            size (int): integer that represents the square's size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """Return: the area of a square in process"""
        return (self.__size**2)

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """printa the square"""
        if self.__size == 0:
            print()

        else:
            for idx in range(0, self.__position[1]):
                print()
            for idx in range(0, self.__size):
                print("{}{}".format(" "*self.position[0], '#'*self.__size))
