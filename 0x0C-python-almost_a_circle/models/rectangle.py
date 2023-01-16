#!/usr/bin/python3

""" Creating class Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Defining the class that inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Return width getter wich is the private instance attributes """
        return self.__width

    @width.setter
    def width(self, value):
        """width method that set a private attribute

           Args:
               value(int): handle integer value
        """
        self.__width = value

    @property
    def height(self):
        """ Return height getter wich is the private instance attributes """
        return self.__height

    @height.setter
    def height(self, value):
        """height method that set a private attribute

           Args:
               value(int): handle integer value
        """
        self.__height = value

    @property
    def x(self):
        """ Return x getter wich is the private instance attributes """
        return self.__x

    @x.setter
    def x(self, value):
        """x method that set a private attribute

           Args:
               value(int): handle integer value
        """
        self.__x = value

    @property
    def y(self):
        """ Return y getter wich is the private instance attributes """
        return self.__y

    @y.setter
    def y(self, value):
        """y method that set a private attribute

           Args:
               value(int): handle integer value
        """
        self.__y = value
