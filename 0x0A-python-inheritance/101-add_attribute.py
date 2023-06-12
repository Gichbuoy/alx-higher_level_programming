#!/usr/bin/python3
"""function that adds a new attributes to object if it's possible."""


def add_attribute(obj, att, value):
    """define attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
