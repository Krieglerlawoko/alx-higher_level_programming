#!/usr/bin/python3

def uppescase(str):
    """print uppercase str"""
    for charact in str:
        if ord(charact) <= 122 and ord(charact) >= 97:
            charact = chr(ord(c) - 32)
        print("{}".format(charact), end="")
        print("")
