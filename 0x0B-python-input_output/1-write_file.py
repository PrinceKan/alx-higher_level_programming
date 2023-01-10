#!/usr/bin/python3

""" Define the function write_file """


def write_file(filename="", text=""):
    """write_file method that Writes a string to a text file (UTF8)
       Create the file if doesn't exist and overwrite the content
       of the file if it already exists.
       Args:
            filename="": Handle the file name
            text="": Handle the text into the file

       Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
