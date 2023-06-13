#!/usr/bin/pthon3
"""function that defines a class; Student that defines a student,
based on task9"""


class Student:
    """define a class that represents a studeent"""

    def __init__(self, first_name, last_name, age):
        """initializes variables for new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """defines dictionary representation for student"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
