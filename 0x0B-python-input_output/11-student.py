#!/usr/bin/python3
"""a class Student defined"""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """a new Student initialized"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of Student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {l: getattr(self, l) for l in attrs if hasattr(self, l)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of Student"""
        for j, k in json.items():
            setattr(self, j, k)
