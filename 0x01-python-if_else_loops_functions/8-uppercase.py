#!/usr/bin/python3
def uppercase(str):
    for l in str:
        upper_case = ord(l)
        print("{}".format(chr(upper_case - 32)
                          if (upper_case >= ord("a") and
                              upper_case <= ord("z")) else l), end="")
    print()
