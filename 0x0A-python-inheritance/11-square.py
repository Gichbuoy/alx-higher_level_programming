#!/usr/bin/python3
"""function that defines a class; Square, that inherits from task10"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that represents a square"""

    def __init__(self, size):
        """initializes variables for the new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
