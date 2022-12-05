#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for indx in range(0, len(my_list)):
            if my_list[indx] > max:
                max = my_list[indx]
        return max
    else:
        return None
