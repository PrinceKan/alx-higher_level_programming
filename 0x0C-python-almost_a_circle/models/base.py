#!/usr/bin/python3

"""Creating the class named base that will be the \"base\" of all other\
   classes in this project
"""


class Base:
    """The goal of this class is to manage id attribute in all your
       future classes and to avoid duplicating the same code
       (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
