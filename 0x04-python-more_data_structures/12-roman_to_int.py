#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    mlist = max(list_num)

    for j in list_num:
        if mlist > j:
            sub += j

    return (mlist - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lkeys = list(rom_n.keys())

    n = 0
    last_r = 0
    list_n = [0]

    for k in roman_string:
        for r_num in lkeys:
            if r_num == k:
                if rom_n.get(k) <= last_r:
                    n += to_subtract(list_n)
                    list_n = [rom_n.get(k)]
                else:
                    list_n.append(rom_n.get(k))

                last_r = rom_n.get(k)

    n += to_subtract(list_n)

    return (n)
