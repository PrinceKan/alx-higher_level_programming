#!/usr/bin/python3

"""Define a Name holder"handler"""


def say_my_name(first_name, last_name=""):
    """say_my_name method that handle user name

       Args:
            first_name(string): String that hold the first name
            last_name(string): String that hold the first name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))