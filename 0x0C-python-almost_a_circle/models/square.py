#!/usr/bin/python3
"""square class defined"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """new Square initializes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter or setter for size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """Square updater"""
        if len(args) != 0 and args:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif len(kwargs) != 0 and kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """dictionary representation of the Square returned"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
