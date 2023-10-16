#!/usr/bin/python3
""" This Module has a Base class"""
import json


class Base:
    """The Base Class"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Initiates the Base class

            Args:
                id (int) : public instance, if not none assigned id
        """
        if id == None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries == None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, mode="w") as f:
            if list_objs == None:
                f.write("[]")
            else:
                list_dict = []
                for o in list_objs:
                    list_dict.append(o.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string == None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary != None:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"cls.__name__.json"
        try:
            with open(filename, "r") as f:
                list_dic = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dic]
        except IOError:
            return []
