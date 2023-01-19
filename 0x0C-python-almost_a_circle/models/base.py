#!/usr/bin/python3

"""Creating the class named base that will be the “base” of all other\
   classes in this project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method static method
           Args:
               list_dictionarieslist_dictionaries: is a list of dictionaries
           Return: a string \"[]\" or JSON string representation of\
                   list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_filethat  writes the JSON string representation
            of list_objs to a file
           Args:
               cls: is the class
               list_objs: is a list of instances who inherits of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as fl:
            index = []
            if list_objs is not None:
                for item in list_objs:
                    item = item.to_dictionary()
                    index.append(item)
            dico = cls.to_json_string(index)
            fl.write(dico)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string is a string method that represents a list
           of dictionarie
           Return: list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
