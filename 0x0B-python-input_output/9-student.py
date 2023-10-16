#!/usr/bin/python3
"""class Student"""


class Student:
    """a student representation"""

    def __init__(self, first_name, last_name, age):
        """a new Student initialized"""
        self.last_name = last_name
        self.age = age
        self.first_name = first_name
    def to_json(self):
        """a dictionary of Student represented"""
        return self.__dict__
