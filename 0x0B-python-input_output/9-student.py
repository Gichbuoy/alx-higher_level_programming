#!/usr/bin/python3
"""function that define a class Student, that defines a student by:
    first name, last name and age"""


class Student:
    """define a class"""

    def __init__(self, first_name, last_name, age):
        """initializes variables for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """define representation of the student"""
        return self.__dict__
