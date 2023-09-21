#!/usr/bin/python3

"""print alphabet in revers"""
a = 0
for chars in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chars(chars - a)), end="")
    a = 32 if a == 0 else 0
