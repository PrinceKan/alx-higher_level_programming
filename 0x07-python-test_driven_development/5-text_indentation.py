#!/usr/bin/python3

"""Definition of a fonction text_indentation"c"""


def text_indentation(text):
    """"text_indentation method

        Args:
             text(striny): is a string handler
    """

    buf = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        buf += letter
        if letter == "." or letter == "?" or letter == ":":
            while buf[0] == " ":
                buf = buf[1:]
            print(buf)
            print()
            buf = ""
    if len(buf) != 0:
        try:
            while buf[0] == " ":
                buf = buf[1:]
        except Exception as excpt:
            pass
        print(buf, end="")
