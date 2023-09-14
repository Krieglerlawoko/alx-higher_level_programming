#!/usr/bin/python3
def number_keys(a_dictionary):
    digit = 0
    list_keys = list(a_dictionary.keys())

    for a in list_keys:
        digit += 1
    return (digit)
