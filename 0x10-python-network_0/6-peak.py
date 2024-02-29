#!/usr/bin/python3
"""list of integers peak finding module"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    l_ = list_of_integers
    # if there is no list of integers return None
    if l_ == []:
        return None
    leng = len(l_)

    start, end = 0, leng - 1
    while start < end:
        mid = start + (end - start) // 2
        if l_[mid] > l_[mid - 1] and l_[mid] > l_[mid + 1]:
            return l_[mid]
        if l_[mid - 1] > l_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return l_[start]
