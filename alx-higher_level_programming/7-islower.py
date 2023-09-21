#!/usr/bin/python3
def islower(c):
    """checks for lowcase chars"""
    if ord(c) <= 122 and ord(c) >= 97:
        return True
    else:
        return False
