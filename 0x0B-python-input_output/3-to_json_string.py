#!/usr/bin/python3
"""a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Return the JSON string object representation"""
    return json.dumps(my_obj)
