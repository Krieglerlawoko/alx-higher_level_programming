#!/usr/bin/python3
"""text file-reading function defined"""


def read_file(filename=""):
    """content of a UTF8 text file printed out"""
    with open(filename, encoding="utf-8") as a:
        print(a.read(), end="")
