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

