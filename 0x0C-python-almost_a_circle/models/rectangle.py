#!/usr/bin/python3
"""rectangle class defined"""
from models.base import Base


class Rectangle(Base):
    """rectangle represesntation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """new Rectangle initialized"""
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        """Setter or getter for width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) != int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Setter or getter for height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        if type(value) != int:
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def x(self):
        """Setter or getter for the x coordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        if type(value) != int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Setter or getter forthe y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) != int:
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Rectangle printed using the `#` character"""
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle"""
        if len(args) != 0 and args:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """dictionary representation of a Rectangle returned"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
