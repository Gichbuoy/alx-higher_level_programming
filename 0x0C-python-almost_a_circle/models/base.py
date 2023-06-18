#!/usr/bin/python3
"""script that defines a base model"""

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
