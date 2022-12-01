#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for rm_letter in str:
        if (j != n):
            string = string + rm_letter
        j = j + 1
    return(string)
