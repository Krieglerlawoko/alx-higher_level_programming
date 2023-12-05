#!/usr/bin/python3
"""file-appending function"""


def append_write(filename="", text=""):
    """string appended to end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
