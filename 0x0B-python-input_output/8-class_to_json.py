#!/usr/bin/python3

""" Define the class_to_json"""


def class_to_json(obj):
    """class_to_json method function that returns the dictionary
       description with simple data structure

       Args:
            obj:  an instance of a Class

       Return: the dictionary description with simple data structure
               (list, dictionary, string, integer and boolean)
               for JSON serialization of an object
    """
    return obj.__dict__
