#!/usr/bin/python3

""" Define the function append_write """


def append_write(filename="", text=""):
    """append_write method that function that appends a string at the end of a
       text file (UTF8) create the file if doesn't exist and overwrite the
       content of the file if it already exists.

       Args:
            filename="": Handle the file name
            text="": Handle the text into the file

       Return: eturns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
