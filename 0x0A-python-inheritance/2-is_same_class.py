i#!/usr/bin/python3

""" This module contains one function: is_same_class """


def is_same_class(obj, a_class):
    """ returns True or False """
    return a_class is type(obj)
