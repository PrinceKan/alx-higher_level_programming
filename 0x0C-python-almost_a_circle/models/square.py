#!/usr/bin/python3

""" Creating class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defining the class that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Return size getter wich is the private instance attributes """
        return self.width

    @size.setter
    def size(self, value):
        """size method that set a private attribute

           Args:
               value(int): handle integer value
        """
        self.width = value
        self.height = value
