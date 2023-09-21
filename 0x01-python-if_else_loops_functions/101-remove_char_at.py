#!/usr/bin/python3

def romove_char_at(str, n):
    """copies a string with out char at n position"""
    if n is not 0:
        return(str[:n] + str[n+1:])
    else:
        return(str)
