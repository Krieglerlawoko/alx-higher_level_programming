#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())

    for a in keys:
        if a_dictionary.get(a) == value:
            del a_dictionary[a]

    return (a_dictionary)
