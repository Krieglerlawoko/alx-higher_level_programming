#!/usr/bin/python3
"""a class Student"""


class Student:
    """a student representation"""

    def __init__(self, first_name, last_name, age):
        """a new Student initialized"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {l: getattr(self, l) for l in attrs if hasattr(self, l)}
        return self.__dict__
