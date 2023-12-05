#!/usr/bin/python3
"""class Student"""


class Student:
    """student represented"""

    def __init__(self, first_name, last_name, age):
        """new Student initialized"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self):
        """dictionary representation of Student is got"""
        return self.__dict__
