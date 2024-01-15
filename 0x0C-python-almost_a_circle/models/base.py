#!/usr/bin/python3
"""Module that contains Base class"""
import json
import csv
import turtle
import os


class Base():
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class

        Args:
            id (int, optional): id of the base. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries
        """
        if (list_dictionaries is None or list_dictionaries == [] or 
        type(list_dictionaries) != list):
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if json_string == "" or json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file"""
        if list_objs is None or list_objs == []:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        filename = f"{cls.__name__}.json"

        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        r1 = cls(1, 1)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename) as f:
            content = f.read()
        dict_json_string = cls.from_json_string(content)
        list_obj = [cls.create(**dict) for dict in dict_json_string]
        return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Sterialization in CSV"""
        filename = f"{cls.__name__}.csv"

        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """"Desterialization in CSV"""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(f, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in d.items())
                             for d in list_dict]
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
