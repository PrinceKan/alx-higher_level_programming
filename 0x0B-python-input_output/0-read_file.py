#!/usr/bin/python3

""" Define the function read_file """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints its c to stdout """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
        f.close()
