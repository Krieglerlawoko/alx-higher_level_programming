#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nL = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            nL.append(True)
        else:
            nL.append(False)
    return nL
