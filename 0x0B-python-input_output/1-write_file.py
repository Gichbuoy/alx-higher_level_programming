#!/usr/bin/python3
"""function that writes a string to a text file and returns number of
characters written"""


def write_file(filename="", text=""):
    """define function that writes into a string"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
