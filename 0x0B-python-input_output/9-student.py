#!/usr/bin/python3

""" Define one class """


class Student:
    """Public instance attributes:
       first_name
       last_name
       age
    """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json public method that retrieves a dictionary
           representation of a Student

           Return: a dictionary representation of a Student instance
        """
        return self.__dict__
