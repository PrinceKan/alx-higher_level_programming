#!/usr/bin/python3

""" Definee the function append_after """


def append_after(filename="", search_string="", new_string=""):
    """append_after method that inserts a line of text to a file,
       after each line containing a specific string

       Args:
            filename="": handle the file name
            search_string="": seek for the string
            new_string="": retrieve the new string
    """
    with open(filename, 'r') as f:
        text = ""
        letter = -1
        while letter != 0:
            line = f.readline()
            letter = len(line)
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as f:
        f.write(text)
