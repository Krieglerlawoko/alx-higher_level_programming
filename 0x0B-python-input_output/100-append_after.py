#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """text after each line containing a given string in a file insertd"""
    txt = ""
    with open(filename) as a:
        for line in a:
            txt += line
            if serch_string in line:
                txt += new_string
    with open(filename, "w") as b:
        b.write(txt)
