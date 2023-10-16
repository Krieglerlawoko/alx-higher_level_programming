#!/usr/bin/python3
"""JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Create a Python object"""
    with open(filename) as j:
        return json.load(j)
