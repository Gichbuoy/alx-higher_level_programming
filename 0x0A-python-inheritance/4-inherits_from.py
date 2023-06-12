#!/usr/bin/python3
"""function that returns True if the object is an instance of a class,
    otherwise false"""


def inherits_from(obj, a_class):
    """ddfine object that is an instance of a class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
