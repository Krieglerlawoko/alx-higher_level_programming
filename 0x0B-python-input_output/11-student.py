#!/usr/bin/python3
"""class Student defined"""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """new Student initialized"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of the Student"""
        if (type(attrs) == list and
                all(type(l) == str for l in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """all attributes of the Student replaced"""
        for a, b in json.items():
            setattr(self, a, b)
