#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for n in str:
        if (j != n):
            string = string + n
        j = j + 1
    return(string)
