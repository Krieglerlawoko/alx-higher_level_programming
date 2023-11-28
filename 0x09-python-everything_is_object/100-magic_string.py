#!/usr/bin/python3
def magic_string():
    magicString.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magicString.n - 1) + "BestSchool")
