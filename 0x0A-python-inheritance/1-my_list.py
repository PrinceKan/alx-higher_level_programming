#!/usr/bin/python3

""" My class MyList """


class MyList(list):
    """ Mylist is the de defined class """
    def print_sorted(self):
        """ print_sorted method """
        print(sorted(self))
