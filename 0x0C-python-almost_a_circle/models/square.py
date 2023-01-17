#!/usr/bin/python3

""" Creating class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defining the class that inherits from base """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ Return size getter wich is the public instance attributes """
        return self.height

    @size.setter
    def size(self, value):
        """size method that set a public attribute

           Args:
               value(int): handle integer value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update is a public methode that assigns an argument\
             to each attribute:
            Args:
                *args: is a \"no-keyword argument\" with an order to follow\
                for each argument handle
                1st argument should be the id attribute
                2nd argument should be the height attribute
                3rd argument should be the x attribute
                4th argument should be the y attribute
                **kwargs: is an \"key-worded argument\" with wich order is not
                important
        """
        counter = 0
        if args != ():
            for a in args:
                counter += 1
                if counter == 1:
                    self.id = a
                if counter == 2:
                    self.size = a
                if counter == 3:
                    self.x = a
                if counter == 4:
                    self.y = a
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
