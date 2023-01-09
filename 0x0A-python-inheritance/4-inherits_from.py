#!/usr/bin/python3

""" Define a function inherit_f.. """


def inherits_from(obj, a_class):
    """inherits_f.. meethod

       Args:
            obj: is on object
            a_class: class

       Return: false if the type is of object is a class otherwise fale
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
