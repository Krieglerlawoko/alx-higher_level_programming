#!/usr/bin/python3
"""Defines a text file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after line"""
    t = ""
    with open(filename) as j:
        for k in j:
            t += k
            if string_search in k:
                t += new_string
    with open(filename, "w") as l:
        l.write(text)
