#!/usr/bin/python3
"""JSON-to-object function"""
import json


def from_json_string(my_str):
    """Python object representation of JSON string returned"""
    return json.loads(my_str)
