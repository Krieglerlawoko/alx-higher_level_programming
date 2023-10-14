#!/usr/bin/python3

"""base model class."""
import json
import csv
import turtle


class Base:
    """Base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """new Base is initialized"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied from a dictionary"""
        if dictionary != {} and dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return list of classes instantiated from file of JSON strings"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of a list of objects to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs == [] or  list_objs is None:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for o in list_objs:
                    writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of classes instantiated from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([j, int(s)] for j, s in a.items())
                              for a in list_dicts]
                return [cls.create(**a) for a in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for r in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(r.x, r.y)
            turt.down()
            for j in range(2):
                turt.forward(r.width)
                turt.left(90)
                turt.forward(r.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for s in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(s.x, s.y)
            turt.down()
            for g in range(2):
                turt.forward(s.width)
                turt.left(90)
                turt.forward(s.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
