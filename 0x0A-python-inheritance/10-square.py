#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

""" creating a class """


class Square(Rectangle):
    """Rectangle class name that inherit another\
         class that named Rectangle
    """
    def __init__(self, size):
        """ __init__ method

            Args:
                 size(int): handle the size digit
        """

        self.__size = size
        self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the rectangle's area"""
        return (self.__size*self.__size)
