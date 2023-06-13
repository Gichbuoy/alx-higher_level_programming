#!/usr/bin/python3
"""function that appends a tring at end of a text file (UTF8)
and returns number of characters added"""


def append_write(filename="", text=""):
    """define function that appends a string"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
