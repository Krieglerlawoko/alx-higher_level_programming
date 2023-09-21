#!/usr/bin/python3

for digit in range(0, 100):
    if digit is not 99:
        print("{:02}".format(number), end=", ")
    else:
        print("{}".format(digit))
