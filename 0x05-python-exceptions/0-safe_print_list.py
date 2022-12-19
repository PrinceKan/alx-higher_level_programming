#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for item in range(0, x):
            counter += 1
            print("{}".format(my_list[item]), end="")
        print()
        return x
    except IndexError:
        print()
        return item
