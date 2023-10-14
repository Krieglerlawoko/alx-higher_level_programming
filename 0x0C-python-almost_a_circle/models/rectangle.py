#!/usr/bin/python3
"""rectangle class."""
from models.base import Base


class Rectangle(Base):
    """a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """a new Rectangle initialized"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setter and getter for width of the Rectangle"""
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
        """sets or gets height of the Rectangle"""
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
        """setter or getter for x coordinate of the Rectangle."""
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
        """getter or setter for y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) != int:
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """Return area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using `#` character"""
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif j == 1:
                    self.width = arg
                elif j == 2:
                    self.height = arg
                elif j == 3:
                    self.x = arg
                elif j == 4:
                    self.y = arg
                j += 1

        elif kwargs and len(kwargs) != 0:
            for a, s in kwargs.items():
                if a == "id":
                    if s is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = s
                elif a == "width":
                    self.width = s
                elif a == "height":
                    self.height = s
                elif a == "x":
                    self.x = s
                elif a == "y":
                    self.y = s

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
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
