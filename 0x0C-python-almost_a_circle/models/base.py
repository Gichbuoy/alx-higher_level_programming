#!/usr/bin/python3
"""script that defines a base model"""
import json


class Base:
    """This class represents the base model.
    The class represents the base for all other classes
    Attributes:
        __nb__objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base with its attributes.
        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """define static method that returns JSON string representation
        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None of list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of list_objs
        Args:
            list_objs (list): A list of inherited Base istance.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """class method that decentralizes a JSON string.
        Args:
            json_string (str): A json string representation of a list of dicts.
        Returns:
            If json_string is None or empty
            Otherwise the python list repreented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns class instantiated from a dict of attr.
        Args:
            *dictionary: key value pair of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of classes instantiated from a file
        Args:
            reads from '<cls.__name__>.json'
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
