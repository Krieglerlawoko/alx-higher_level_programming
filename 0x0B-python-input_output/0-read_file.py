#!/usr/bin/python3
"""a file-reading function."""


def read_file(filename=""):
    """Prints contents of text files to stdout"""
    with open(filename, encoding="utf-8") as j:
        print(j.read(), end="")
