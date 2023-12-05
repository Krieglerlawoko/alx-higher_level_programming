#!/usr/bin/python3
"""file-writing function"""


def write_file(filename="", text=""):
    """string to written to UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as a:
        return a.write(text)
