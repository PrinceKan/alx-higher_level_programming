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
        self.all_setter_validator("width", value)
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
        self.all_setter_validator("height", value)
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
        self.all_setter_validator("x", value)
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
        self.all_setter_validator("y", value)
        self.__y = value

    @staticmethod
    def all_setter_validator(attribute, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "width" or attribute == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """ Return the rectangle's area """
        return self.height * self.width
