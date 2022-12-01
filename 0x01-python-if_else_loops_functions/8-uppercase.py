#!/usr/bin/python3
def uppercase(str):
    for up_cs in str:
        upper_case = ord(up_cs)
        print("{}".format(chr(upper_case - 32)
                          if (upper_case >= ord("a") and
                              upper_case <= ord("z")) else up_cs), end="")
    print()
