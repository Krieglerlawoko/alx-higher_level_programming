#!/usr/bin/python3
def remove_char_at(str, n):
    """copies a string with out char at n position"""
    a = n
    if a < 0:
        return (str)
    return (str[:a] + str[a+1:])
