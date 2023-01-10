#!/usr/bin/python3

""" Define the function 'from_json_string' """"
import json


def from_json_string(my_str):
    """'from_json_string' method that returns an object (Python data structure)
        represented by a JSON string

        Args:
             my_str(string): Handle string as an argument

       Returns an object (Python data structure) represented by a JSON string
    """
    return (json.loads(my_str))
