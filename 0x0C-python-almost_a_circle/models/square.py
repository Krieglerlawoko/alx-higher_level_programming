#!/usr/bin/python3
"""square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """a new Square is initialized"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of setter for the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """make updates to Square"""
        if len(args) != 0 and args:
            k = 0
            for arg in args:
                if k == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif k == 1:
                    self.size = arg
                elif k == 2:
                    self.x = arg
                elif k == 3:
                    self.y = arg
                k += 1

        elif len(kwargs) != 0 and kwargs:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def to_dictionary(self):
        """Return representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return printed and string rep of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
