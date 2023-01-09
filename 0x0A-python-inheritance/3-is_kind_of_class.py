#!/usr/bin/python3

""" Define the function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class method

        Args:
             obj: an object
             a_class: a class

        Return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
