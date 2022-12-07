#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for idx in my_list:
        if idx != search:
            new_list[len(new_list):] = [idx]
        else:
            new_list[len(new_list):] = [replace]
    return new_list
