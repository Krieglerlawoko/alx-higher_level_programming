#!/usr/bin/python3
"""class Student"""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """new Student initialized"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of Student"""
        if (type(attrs) == list and
                all(type(line) == str for line in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
