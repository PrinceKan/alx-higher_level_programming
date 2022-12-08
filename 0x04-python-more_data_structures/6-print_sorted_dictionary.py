#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered = sorted(a_dictionary)
    for idx in ordered:
        print('{}: {}'.format(idx, a_dictionary[idx]))
