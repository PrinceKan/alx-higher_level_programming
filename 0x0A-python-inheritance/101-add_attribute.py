#!/usr/bin/python3i

""" Creating a function """


def add_attribute(obj, name, value):
    """add_attribute method

       Args:
           obj: is an argument that handle a name
           name: handle name
           value: halue a digit value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
