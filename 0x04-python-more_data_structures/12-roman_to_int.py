#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        result = 0
        convert_num = 0
        roman_base_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                              'C': 100, 'D': 500, 'M': 1000}
        for idx in reversed(roman_string):
            convert_num = roman_base_numbers[idx]
            if result < convert_num * 5:
                result = result + convert_num
            else:
                result = result - convert_num
        return result
    else:
        return 0
