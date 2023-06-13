#!/usr/bin/python3
"""function that returns an object representation by a json string"""
import json


def from_json_string(my_str):
    """define object representation by json str"""
    return json.loads(my_str)
