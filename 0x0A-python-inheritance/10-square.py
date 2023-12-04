#!/usr/bin/python3
"""a ractangle subclass defined"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square representation"""

    def __init__(self, size):
        """new square initialized"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
