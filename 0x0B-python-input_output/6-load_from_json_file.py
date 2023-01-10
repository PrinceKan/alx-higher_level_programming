#!/usr/bin/python3

""" Define the function save_to_json_file """
import json


def load_from_json_file(filename):
    """save_to_json_file method that creates an Object from a “JSON file”

       Args:
            filename (string): Hamdle the filename created wich is a string

       Return: A file that will load from json
    """
    with open(filename, "r") as f:
        return(json.load(f))
