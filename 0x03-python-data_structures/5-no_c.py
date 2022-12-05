#!/usr/bin/python3
def no_c(my_string):
    reverse = ""
    for idx in range(0, len(my_string)):
        if my_string[idx] != 'C' and my_string[idx] != 'c':
            reverse = reverse + my_string[idx]
    return reverse
