#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = list(map(lambda a: replace if a == search else a, my_list))

    return (list2)
