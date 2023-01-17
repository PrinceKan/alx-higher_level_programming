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

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """

        rectangle = ""
        print("\n" * self.y, end="")
        for n in range(self.height):
            rectangle += (" " * self.x) + (self.width * "#") + "\n"
        print(rectangle, end="")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update is a public methode that assigns an argument
             to each attribute:
            Args:
                *args is a \"no-keyword argument\" with an order to follow
                for each argument handle
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute

                **kwargs is an \"key-worded argument\" with wich order is not
                important
        """
        counter = 0
        if args != ():
            for a in args:
                counter += 1
            if counter == 1:
                self.id = a
            if counter == 2:
                self.width = a
            if counter == 3:
                self.height = a
            if counter == 4:
                self.x = a
            if counter == 5:
                self.y = a
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return the dictionary representation of a Rectangle """
        dico = {}
        dico["id"] = self.id
        dico["width"] = self.width
        dico["height"] = self.height
        dico["x"] = self.x
        dico["y"] = self.y
        return dico
