#!/usr/bin/python3
"""function that inherits from BaseGeometry in task 5"""


class Rectangle(BaseGeometry):
    """class that represents a rectangle"""

    def __init__(self, width, height):
        """initializes variables for rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
