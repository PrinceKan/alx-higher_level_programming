#!/usr/bin/python3

""" Define a function to_json_string """
import json


def to_json_string(my_obj):
    """to_json_string method that returns the JSON representation of
       an object (string)

        Args:
             my_obj (string): handle object wich is a string

        Returns: the JSON representation of an object (string)
    """
    return (json.dumps(my_obj))
