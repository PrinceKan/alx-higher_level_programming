#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = 0
    for index in argv[1:]:
        num += int(index)
    print('{:d}'.format(num))
