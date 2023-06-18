#!/usr/bin/python3
"""function that define a class Square, that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class that represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square and its variables.
        Args:
            size (int): This is the size of the new Square.
            x (int): This is the x coordinate of the new Square.
            y (int): This is the y coordinate of the new Square.
            id (int): This is the identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
