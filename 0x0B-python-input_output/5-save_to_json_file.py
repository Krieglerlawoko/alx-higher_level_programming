#!/usr/bin/python3
"""JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """object written to a text file using JSON representation"""
    with open(filename, "w") as a:
        json.dump(my_obj, a)
