#!/usr/bin/python3
"""function that returns True if object is an instance of a class,
   otherwise False"""


def is_kind_of_class(obj, a_class):
    """define instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
