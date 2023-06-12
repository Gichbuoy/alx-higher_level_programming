#!/usr/bin/python3
"""function that defines a class that inherits BaseGeometry from task5"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that represents a rectangle"""
    def __init__(self, width, height):
        """initializes rectangle variables"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """defines the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
