#!/usr/bin/python3
"""function that returns description with simple data structure,
for JSON serialization of an object"""


def class_to_json(obj):
    """define function that returns dictionary description for simple DS"""
    return obj.__dict__
