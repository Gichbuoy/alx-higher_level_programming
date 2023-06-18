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

    def update(self, *args, **kwargs):
        """define the update of the square
        Args:
            *args (ints): New attribute values.
                - This 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.size = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """define the dictionary representation of a square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """define the string representatio of the square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x,
                self.y, self.width)
