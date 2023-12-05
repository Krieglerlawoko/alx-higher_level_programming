#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """text after each line containing a given string in a file insertd"""
    text = ""
    with open(filename) as a:
        for l in a:
            text += l
            if serch_str in l:
                text += new_string
    with open(filename, "w") as b:
        b.write(text)
