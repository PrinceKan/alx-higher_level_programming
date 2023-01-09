#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

""" Define a class named square""""


class Square(Rectangle):
    """Rectangle class name that inherit another\
         class that named Rectangle
    """
    def __init__(self, size):
        """ __init__ method

            Args:
                 size(int): handle the size digit
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """ Return the rectangle area """
        return (self.__size*self.__size)

    def __str__(self):
        """ Return the Square followed by sizes """
        return ('[Square] {}/{}'.format(self.__size, self.__size))
