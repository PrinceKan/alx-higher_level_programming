#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class name that inherit another
         class that named BaseGeometry
    """
    def __init__(self, width, height):
        """ __init__ method

            Args:
                 width(int): handle the width digit
                 height(int): handle the height digit
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ Return: the area """
        return (self.__width*self.__height)

    def __str__(self):
        """ Return: The retangle parameter """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
