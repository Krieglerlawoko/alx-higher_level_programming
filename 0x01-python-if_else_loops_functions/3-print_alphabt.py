#!/usr/bin/python3
for charcter in range(97, 123):
    if chr(charcter) is not 'e' and chr(charcter) is not 'q':
        print("{}".format(chr(charcter)), end="")
