#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient_list = []
    quotient = 0
    for idx in range(list_length):
        try:
            quotient = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            quotient_list.append(quotient)
    return quotient_list
