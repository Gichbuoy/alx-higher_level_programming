#!/usr/bin/python3
"""function that writes an object to a text-file, using json rep"""
import json


def save_to_json_file(my_obj, filename):
    """define function that writes an object to a text file using json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
