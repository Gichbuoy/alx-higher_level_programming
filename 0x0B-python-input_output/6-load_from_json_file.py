#!/usr/bin/python3
"""function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """define a function that creates py object from json fie"""
    with open(filename) as f:
        return json.load(f)
