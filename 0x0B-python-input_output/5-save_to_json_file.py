#!/usr/bin/python3

""" Define the function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file method that write an Object to a text file, using a
       JSON representation

       Args:
            my_obj (string): Hamdle the object wich is string
            filename (string): Hamdle the filename created wich is a string

       Return: A json representation file
    """
    with open(filename, "w") as f:
        return (json.dump(my_obj, f))
