#!/usr/bin/python3

"""Define a class named rectangle"""


class Rectangle:
    """represent a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ __init__ method
        Args:
            width (int): integer that represents the rectangle's width
            height (int): integer that represents the rectctangles height
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return: The rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Return: The rectangle height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return: The rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return: The rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2*(self.__width + self.__height))

    def __str__(self):
        """__str__  method

           Return: nothing or an area
        """
        if self.__width == 0 or self.__height == 0:
            return ('')
        x = ''
        for i in range(self.__height):
            x += str(str(self.print_symbol) * self.__width) + '\n'
        x = x[:-1]
        return x

    def __repr__(self):
        return('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """__repr__  method

           Return: a string representation
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal Static method

           Args:
                rect_1 (int): integer that represent an area_1
                rect_2 (int): integer that represent an area_2

           Return: an areat of one of the rectangle or an error message
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
