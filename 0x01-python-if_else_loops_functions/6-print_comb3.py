#!/usr/bin/python3

"""prints different combinations of 2 numbers"""
for num in range(0, 10):
    for num2 in range(num + 1, 10):
        if num2 == 9 and num == 8:
            print("{}{}".format(num, num2))
        else:
            print("{}{}".format(num, num2), end=", ")
