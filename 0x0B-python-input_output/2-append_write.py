#!/usr/bin/python3
"""file-appending function"""


def append_write(filename="", text=""):
    """Appends string to end of text file"""
    with open(filename, "a", encoding="utf-8") as j:
        return j.write(text)
