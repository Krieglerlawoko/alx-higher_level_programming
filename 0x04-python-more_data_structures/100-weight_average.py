#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        number = 0
        n = 0

        for a in my list:
            number += a[0] * a[1]
            n += a[1]

        return (number / n)
    else:
        return 0
