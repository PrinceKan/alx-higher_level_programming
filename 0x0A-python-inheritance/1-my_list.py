#!/usr/bin/python3

""" My class MyList """


class MyList(list):
    def print_sorted(self):
        """ print_sorted method """
        print(sorted(self))
