#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    value = a_dictionary.get(key)

    if value is not None:
        del a_dictionary[key]
    return (a_dictionary)
