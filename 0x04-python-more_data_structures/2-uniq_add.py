#!/usr/bin/python3
def uniq_add(my_list=[]):
    list2 = set(my_list)
    digit = 0

    for a in list2:
        digit += a

    return (digit)

