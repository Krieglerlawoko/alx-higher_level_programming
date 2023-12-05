#!/usr/bin/python3
"""JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Python object from a JSON file creator"""
    with open(filename) as a:
        return json.load(a)
