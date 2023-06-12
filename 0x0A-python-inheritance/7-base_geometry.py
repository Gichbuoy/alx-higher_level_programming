#!/usr/bin/python3
"""function that defines a base geometry based on task 5"""


class BaseGeometry:
    """parent class"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define validator as an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be grater that 0".format(name))
