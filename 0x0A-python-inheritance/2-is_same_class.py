#!/usr/bin/python3
"""function that returns true if the object is exactly an instance,
of specified class: otherwise False"""


def is_same_class(obj, a_class):
    """defines an object"""
    if type(obj) == a_class:
        return True
    return False
