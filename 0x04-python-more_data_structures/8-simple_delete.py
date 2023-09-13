#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    value = a_dictionary.get(key)

    if value != None:
        del a_dictionary[key]
    return (a_dictionary)

