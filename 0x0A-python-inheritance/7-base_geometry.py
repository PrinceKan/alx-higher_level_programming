#!/usr/bin/python3

"""Create a class """


class BaseGeometry:
    """ Represent the BaseGeometry """

    def area(self):
        """ area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator method

           Args:
                name(string): handle a string
                value(int): handle an integer value for this function
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
